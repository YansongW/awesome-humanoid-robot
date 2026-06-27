"""Natural-language Q&A over the knowledge graph."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from ai4sci_lib import llm_client  # noqa: E402
from web.kg_store import get_store  # noqa: E402


MAX_CONTEXT_ENTRIES = 6
MAX_BODY_CHARS = 1200


def _entry_context(entry, store) -> str:
    lines = [
        f"【{entry.name}】 (ID: {entry.id})",
        f"类型：{entry.type} | 领域：{', '.join(entry.domains)} | 层级：{', '.join(entry.layers)}",
        f"摘要：{entry.summary}",
    ]
    body = entry.body.strip()
    if len(body) > MAX_BODY_CHARS:
        body = body[:MAX_BODY_CHARS] + "…"
    if body:
        lines.append(f"内容：\n{body}")
    out_rels = store.outgoing.get(entry.id, [])
    in_rels = store.incoming.get(entry.id, [])
    if out_rels or in_rels:
        rel_lines = []
        for rel in out_rels[:5]:
            rel_lines.append(f"  → {rel.type} → {rel.target_name} ({rel.target_id})")
        for rel in in_rels[:5]:
            rel_lines.append(f"  ← {rel.type} ← {rel.source_name} ({rel.source_id})")
        lines.append("关系：\n" + "\n".join(rel_lines))
    return "\n".join(lines)


def answer(question: str) -> dict[str, Any]:
    store = get_store()
    retrieved = store.search(question, top_k=MAX_CONTEXT_ENTRIES)

    context_parts = []
    for entry in retrieved:
        context_parts.append(_entry_context(entry, store))
    context = "\n\n---\n\n".join(context_parts)

    if not context.strip():
        return {
            "answer": "抱歉，知识图谱中没有找到与问题相关的条目。请尝试使用更具体的关键词。",
            "sources": [],
        }

    system_prompt = (
        "你是一个熟悉人形机器人行业的知识图谱助手。请严格依据下面提供的知识图谱内容回答问题。"
        "如果资料中没有足够信息，请明确说明。回答请使用中文，并在相关处引用条目 ID（如 ent_process_p4_1_1）。"
    )
    user_prompt = f"知识图谱资料：\n\n{context}\n\n用户问题：{question}\n\n请回答："

    try:
        response = llm_client.chat_completion(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
            max_tokens=2048,
        )
    except Exception as exc:
        return {
            "answer": f"检索到相关条目，但 LLM 调用失败：{exc}. 请检查环境变量 AI4SCI_API_KEY/OPENAI_API_KEY。",
            "sources": [{"id": e.id, "name": e.name} for e in retrieved],
        }

    return {
        "answer": response.strip(),
        "sources": [{"id": e.id, "name": e.name} for e in retrieved],
    }
