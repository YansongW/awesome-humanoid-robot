"""Configurable OpenAI-compatible LLM client with Kimi CLI fallback."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

from . import config


def _get_client():
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise ImportError(
            "The 'openai' package is required. Install it with: "
            "pip install openai"
        ) from exc

    api_key = config.DEFAULT_LLM_API_KEY
    base_url = config.DEFAULT_LLM_BASE_URL

    if not api_key:
        raise RuntimeError(
            "No LLM API key found. Set AI4SCI_API_KEY or OPENAI_API_KEY environment variable.\n"
            "Example: export AI4SCI_API_KEY='your-key'\n"
            "You can also set AI4SCI_BASE_URL if using a non-default endpoint."
        )

    return OpenAI(api_key=api_key, base_url=base_url)


def _kimi_cli_path() -> str | None:
    """Return the path to the local Kimi CLI binary, if available."""
    cli = shutil.which("kimi")
    if cli:
        return cli
    fallback = Path.home() / ".kimi-code" / "bin" / "kimi"
    if fallback.exists() and os.access(fallback, os.X_OK):
        return str(fallback)
    return None


def _format_messages_for_cli(messages: list[dict[str, str]]) -> str:
    """Convert a message list into a single prompt string for the CLI."""
    parts: list[str] = []
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        if role == "system":
            parts.append(f"[System]\n{content}")
        elif role == "user":
            parts.append(f"[User]\n{content}")
        elif role == "assistant":
            parts.append(f"[Assistant]\n{content}")
        else:
            parts.append(f"[{role}]\n{content}")
    return "\n\n".join(parts)


def _kimi_cli_chat_completion(
    messages: list[dict[str, str]],
    model: str | None = None,
    temperature: float = 0.2,
    max_tokens: int = 4096,
) -> str:
    """Use the local Kimi CLI as a fallback LLM backend.

    This is useful when only a Kimi Code CLI credential is available and no
    standard OpenAI-compatible API key works.
    """
    cli = _kimi_cli_path()
    if not cli:
        raise RuntimeError(
            "Kimi CLI fallback requested but no 'kimi' binary found. "
            "Install Kimi Code CLI or provide a standard API key."
        )

    prompt = _format_messages_for_cli(messages)
    # Ask the model to return JSON when needed by appending an explicit reminder.
    prompt += (
        "\n\n[User]\nReturn your response as plain text. "
        "If the request asks for JSON, return only the JSON object inside a ```json code block."
    )

    cmd = [cli, "-p", prompt, "--output-format", "stream-json"]
    if model:
        cmd.extend(["-m", model])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("Kimi CLI request timed out after 600 seconds.") from exc

    if result.returncode != 0:
        raise RuntimeError(
            f"Kimi CLI failed (exit {result.returncode}): {result.stderr.strip() or result.stdout.strip()[:500]}"
        )

    # Parse stream-json output: JSON Lines with role and meta messages.
    content_lines: list[str] = []
    for line in result.stdout.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if obj.get("role") == "assistant" and "content" in obj:
            content_lines.append(obj["content"])

    if not content_lines:
        raise RuntimeError(f"Kimi CLI returned no assistant content. Output:\n{result.stdout[:1000]}")

    return "\n".join(content_lines)


def chat_completion(
    messages: list[dict[str, str]],
    model: str | None = None,
    temperature: float = 0.2,
    max_tokens: int = 4096,
    response_format: dict[str, str] | None = None,
) -> str:
    """Send a chat completion request and return the text content.

    If AI4SCI_USE_KIMI_CLI is set (or the HTTP API returns an auth error), fall
    back to the local Kimi CLI binary.
    """
    use_cli = os.getenv("AI4SCI_USE_KIMI_CLI", "").lower() in ("1", "true", "yes")

    if not use_cli:
        try:
            client = _get_client()
            resolved_model = model or config.DEFAULT_LLM_MODEL

            kwargs: dict[str, Any] = {
                "model": resolved_model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }
            if response_format:
                kwargs["response_format"] = response_format

            response = client.chat.completions.create(**kwargs)
            return response.choices[0].message.content or ""
        except Exception as exc:  # noqa: BLE001
            error_msg = str(exc).lower()
            if any(code in error_msg for code in ("401", "403", "invalid authentication", "access_terminated")):
                if _kimi_cli_path():
                    print("[llm_client] HTTP API auth failed; falling back to Kimi CLI.")
                    use_cli = True
                else:
                    raise
            else:
                raise

    return _kimi_cli_chat_completion(messages, model=model, temperature=temperature, max_tokens=max_tokens)


def chat_completion_json(
    messages: list[dict[str, str]],
    model: str | None = None,
    temperature: float = 0.2,
    max_tokens: int = 4096,
) -> Any:
    """Send a chat completion request and parse the response as JSON."""
    content = chat_completion(
        messages,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        response_format={"type": "json_object"},
    )
    # Some providers return markdown code fences even with json_object format.
    text = content.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].strip().startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return json.loads(text)
