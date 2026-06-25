"""LLM-based extraction of structured paper information."""

from __future__ import annotations

import json
from datetime import date
from typing import Any

from . import config, llm_client


def _trim_text(text: str, max_chars: int = 120_000) -> str:
    """Trim paper text to fit within context window and remove null bytes."""
    text = text.replace("\x00", " ")
    if len(text) <= max_chars:
        return text
    # Keep beginning and end; middle is often less critical.
    half = max_chars // 2
    return text[:half] + "\n\n...[middle truncated]...\n\n" + text[-half:]


def _today() -> str:
    return date.today().isoformat()


def extract_paper_metadata(text: str, source_url: str, pdf_url: str | None = None) -> dict[str, Any]:
    """Extract core metadata from the full paper text."""
    system_prompt = (
        "You are an AI research assistant for a project building a curated knowledge base "
        "on humanoid robot mass production and industrial application. "
        "Extract structured metadata from the provided academic paper text. "
        "Respond only with a JSON object. Be concise and factual."
    )

    user_prompt = f"""Extract the following metadata from this academic paper.

Source URL: {source_url}
PDF URL: {pdf_url or source_url}

Return a JSON object with these keys:
- title: string, the full paper title
- authors: list of strings (full names)
- year: integer or string (publication year; use the arXiv/v1 date if no venue year)
- venue: string or null (conference/journal; use arXiv if preprint)
- doi: string or null
- arxiv_id: string or null
- abstract: string, the paper abstract
- problem: string, one sentence describing the problem addressed
- method: string, one sentence describing the key method/approach
- key_contributions: list of 3-5 short strings
- datasets_used: list of dataset names mentioned/used (empty if none)
- benchmarks_used: list of benchmark names mentioned/used (empty if none)
- components_or_materials: list of hardware components or materials discussed (empty if none)
- companies_or_institutions: list of companies or institutions prominently involved (empty if none)
- humanoid_relevance: string, one sentence explaining relevance to humanoid robot mass production or deployment
- limitations: list of 2-4 short strings

Paper text:
{_trim_text(text)}
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    return llm_client.chat_completion_json(messages)


def classify_relevance(metadata: dict[str, Any]) -> dict[str, Any]:
    """Classify how relevant the paper is to the project scope."""
    system_prompt = (
        "You are a relevance classifier for a humanoid-robot knowledge base. "
        "Respond only with JSON."
    )
    user_prompt = f"""Rate the relevance of this paper to the project scope:
"How do we go from 0 to 1 on humanoid robot mass production and industrial application?"

Paper title: {metadata.get("title", "")}
Abstract: {metadata.get("abstract", "")}
Problem: {metadata.get("problem", "")}
Method: {metadata.get("method", "")}
Humanoid relevance: {metadata.get("humanoid_relevance", "")}

Return JSON:
{{
  "score": "high" | "medium" | "low",
  "score_value": 3 for high, 2 for medium, 1 for low,
  "reason": "one sentence explaining the score",
  "primary_domain": "one of: ai_models_algorithms, software_middleware, data_datasets, evaluation_benchmarks, components, raw_materials, manufacturing_processes, assembly_integration_testing, mass_production, design_engineering, applications_markets, policy_regulation_ethics, none",
  "secondary_domains": ["..."] // may be empty
}}
"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    return llm_client.chat_completion_json(messages)


def propose_entry(
    metadata: dict[str, Any],
    relevance: dict[str, Any],
    model: str | None = None,
) -> dict[str, Any]:
    """Generate a full entry proposal from metadata and relevance."""
    system_prompt = (
        "You are an ontology engineer for a humanoid-robot knowledge base. "
        "Generate a structured entry proposal in JSON that conforms to the project's schema. "
        "All fields must be factual, sourced to the paper, and avoid speculation."
    )

    domain_options = list(config.DOMAIN_MAP.values())
    type_options = [
        "paper", "dataset", "benchmark", "technology", "component", "material",
        "software_platform", "robot_system", "patent", "report", "standard",
    ]

    user_prompt = f"""Generate a knowledge-base entry proposal for this paper.

Metadata:
{json.dumps(metadata, indent=2, ensure_ascii=False)}

Relevance classification:
{json.dumps(relevance, indent=2, ensure_ascii=False)}

Allowed domain codes:
{json.dumps(domain_options, indent=2)}

Allowed entry types:
{json.dumps(type_options, indent=2)}

Return JSON with this structure:
{{
  "entry": {{
    "type": "paper" (or most appropriate type),
    "names": {{"en": "...", "zh": "...", "ko": "..."}},
    "summary": {{"en": "...", "zh": "...", "ko": "..."}},
    "domains": ["07_ai_models_algorithms"], // use codes from allowed list
    "functional_roles": ["knowledge", "intelligence"], // from: material, component, process, system, tool_equipment, facility, intelligence, organization, market, policy, knowledge
    "tags": ["vla", "..."],
    "verification": {{
      "status": "partially_verified",
      "reviewed_by": "ai",
      "reviewed_at": "{_today()}",
      "confidence": "medium",
      "notes": "AI-extracted from full text; requires human review before verification."
    }},
    "sources": [
      {{
        "id": "src_001",
        "type": "paper",
        "title": "...",
        "url": "...",
        "date": "YYYY-MM-DD or YYYY",
        "accessed_at": "{_today()}"
      }}
    ],
    "related_entities": [
      {{
        "id": "existing_entity_id_or_proposed_id",
        "relationship": "cites",
        "description": {{"en": "...", "zh": "...", "ko": "..."}}
      }}
    ]
  }},
  "body": {{
    "overview": "2-3 paragraphs",
    "key_contributions": "bullet list",
    "relevance_to_humanoid": "1-2 paragraphs"
  }},
  "relationships": [
    {{
      "type": "cites",
      "target_id": "...",
      "target_name": {{"en": "..."}},
      "target_domain": "...",
      "description": {{"en": "...", "zh": "...", "ko": "..."}},
      "source_citation": "section or sentence in the paper supporting this relationship"
    }}
  ],
  "review_notes": [
    "Uncertain claim or missing info to verify",
    "..."
  ]
}}

Guidelines:
- Summaries should be 1-2 sentences and fact-based.
- Names and summaries must be provided in English, Simplified Chinese, and Korean.
- Domains should reflect the paper's primary focus; use multiple only if genuinely cross-domain.
- Tags should be lowercase, snake_case, and specific to humanoid robotics.
- Related_entities and relationships should only include items explicitly discussed in the paper.
- For each proposed relationship, include a source_citation from the paper text.
- If a target entity does not yet exist in the knowledge base, propose a stable target_id and target_name.
- Mark any uncertain claims in review_notes.
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    return llm_client.chat_completion_json(messages, model=model)


def _render_text(value: Any) -> str:
    """Render a string or list of strings as Markdown."""
    if isinstance(value, list):
        rendered = []
        for item in value:
            line = str(item).strip()
            if line:
                rendered.append(f"- {line}")
        return "\n".join(rendered) if rendered else ""
    return str(value).strip()


def build_markdown_body(body_data: dict[str, Any]) -> str:
    """Convert structured body data to Markdown."""
    overview = _render_text(body_data.get("overview", ""))
    contributions = _render_text(body_data.get("key_contributions", ""))
    relevance = _render_text(body_data.get("relevance_to_humanoid", ""))

    md = f"""## Overview

{overview}

## Key Contributions

{contributions}

## Relevance to Humanoid Robotics

{relevance}
"""
    return md.strip()
