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


def classify_relevance(metadata: dict[str, Any], context: str | None = None) -> dict[str, Any]:
    """Classify how relevant the paper is to the project scope.

    Args:
        metadata: Paper metadata extracted from the full text.
        context: Optional workstream-specific guidance appended to the prompt
            (e.g. for foundational or cross-domain workstreams).
    """
    system_prompt = (
        "You are a relevance classifier for a humanoid-robot knowledge base. "
        "Respond only with JSON."
    )
    context_note = ""
    if context:
        context_note = f"\nAdditional guidance for this workstream:\n{context}\n"
    user_prompt = f"""Rate the relevance of this paper to the project scope:
"How do we go from 0 to 1 on humanoid robot mass production and industrial application?"
{context_note}
Paper title: {metadata.get("title", "")}
Abstract: {metadata.get("abstract", "")}
Problem: {metadata.get("problem", "")}
Method: {metadata.get("method", "")}
Humanoid relevance: {metadata.get("humanoid_relevance", "")}

Return JSON:
{{
  "score": "high" | "medium" | "low",
  "score_value": 3 for high, 2 for medium, 1 for low,
  "reason": "one sentence explaining the score and the explicit connection to humanoid robots or robotics/automation",
  "primary_domain": "one of: ai_models_algorithms, software_middleware, data_datasets, evaluation_benchmarks, components, raw_materials, manufacturing_processes, assembly_integration_testing, mass_production, design_engineering, applications_markets, policy_regulation_ethics, none",
  "secondary_domains": ["..."] // may be empty
}}

Score LOW if:
- The paper is a generic theory/method paper with no robotics, automation, or humanoid-robot application.
- The paper studies materials, chemistry, economics, math, or CS without connecting them to robots/actuators/manufacturing.
- The abstract and problem statement never mention robots, humanoids, automation, or relevant hardware.

Score MEDIUM if:
- The paper is in a foundational area (math/CS/economics/chemistry) but explicitly targets robotics, automation, or humanoid-related systems.

Score HIGH if:
- The paper directly addresses humanoid robots, legged locomotion, manipulation, robot mass production, or key enabling technologies.
"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    return llm_client.chat_completion_json(messages)


def pre_classify_relevance(
    title: str,
    summary: str,
    context: str | None = None,
) -> dict[str, Any]:
    """Lightweight relevance pre-filter using title and abstract only.

    This is much cheaper than extracting the full paper text.  Papers scored
    ``low`` can be skipped before PDF download.
    """
    system_prompt = (
        "You are a fast relevance pre-filter for a humanoid-robot knowledge base. "
        "Respond only with JSON."
    )
    context_note = ""
    if context:
        context_note = f"\nAdditional guidance for this workstream:\n{context}\n"
    user_prompt = f"""Rate the relevance of this paper to the project scope:
"How do we go from 0 to 1 on humanoid robot mass production and industrial application?"
{context_note}
Title: {title}
Abstract: {summary}

Return JSON:
{{
  "score": "high" | "medium" | "low",
  "score_value": 3 for high, 2 for medium, 1 for low,
  "reason": "one sentence explaining the score"
}}

Examples of LOW relevance:
- A pure mathematics paper with no robot application.
- A general economics or game-theory paper not applied to robotics/automation.
- A hardware/materials paper that never mentions robots, actuators, or automation.

Examples of MEDIUM/HIGH relevance:
- A paper on optimal control with legged robot or manipulation examples.
- A paper on battery electrochemistry for mobile/robotic applications.
- A paper on learning/simulation specifically for humanoid or general robots.
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
    candidate_entities: list[str] | None = None,
) -> dict[str, Any]:
    """Generate a full entry proposal from metadata and relevance.

    Args:
        metadata: Paper metadata extracted from the full text.
        relevance: Relevance classification result.
        model: LLM model override.
        candidate_entities: 知识图谱中真实存在的候选实体清单（每项格式为
            "ent_id=名称"），由调用方按论文 primary_domain 过滤后传入。
            relationships 与 related_entities 的 target_id 只允许从该清单中
            选取，以杜绝 LLM 编造不存在 target_id 的幻觉问题。
    """
    system_prompt = (
        "You are an ontology engineer for a humanoid-robot knowledge base. "
        "Generate a structured entry proposal in JSON that conforms to the project's schema. "
        "All fields must be factual, sourced to the paper, and avoid speculation."
    )

    domain_options = list(config.DOMAIN_MAP.values())
    type_options = [
        "paper", "dataset", "benchmark", "technology", "component", "material",
        "software_platform", "robot_system", "patent", "report", "standard",
        "concept", "method", "formalism", "equation", "operator", "variable",
        "constant", "algorithm", "approximation", "theorem", "principle", "foundation",
    ]
    depth_options = ["foundation", "principle", "formalism", "method", "system"]

    # 候选实体清单区块：target_id 只能从真实存在的实体中选取，杜绝幻觉。
    if candidate_entities:
        candidate_block = (
            "Candidate entities already in the knowledge base (format: entity_id=name).\n"
            "The target_id of every relationship and the id of every related_entities item "
            "MUST be copied verbatim from this list; if no candidate fits, omit the item "
            "(leave the list empty). Do NOT invent new target ids under any circumstance:\n"
            + "\n".join(f"- {c}" for c in candidate_entities)
        )
    else:
        candidate_block = (
            "No candidate entity list was provided. Leave relationships and "
            "related_entities empty rather than inventing target ids."
        )

    user_prompt = f"""Generate a knowledge-base entry proposal for this paper.

Metadata:
{json.dumps(metadata, indent=2, ensure_ascii=False)}

Relevance classification:
{json.dumps(relevance, indent=2, ensure_ascii=False)}

Allowed domain codes:
{json.dumps(domain_options, indent=2)}

Allowed entry types:
{json.dumps(type_options, indent=2)}

Allowed theoretical_depth values (from foundation to system):
{json.dumps(depth_options, indent=2)}

{candidate_block}

Return JSON with this structure:
{{
  "entry": {{
    "type": "paper" (or most appropriate type),
    "names": {{"en": "...", "zh": "...", "ko": "..."}},
    "summary": {{"en": "...", "zh": "...", "ko": "..."}},
    "domains": ["07_ai_models_algorithms"], // use codes from allowed list
    "theoretical_depth": ["method"], // one or more values from allowed list
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
        "id": "entity_id_from_candidate_list",
        "relationship": "cites",
        "description": {{"en": "...", "zh": "..."}}
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
      "target_id": "entity_id_from_candidate_list",
      "target_name": {{"en": "..."}},
      "target_domain": "...",
      "description": {{"en": "...", "zh": "..."}},
      "source_citation": "section or sentence in the paper supporting this relationship"
    }}
  ],
  "knowledge_chain": [
    {{
      "proposed_child_id": "ent_method_...",
      "child_type": "method",
      "child_theoretical_depth": "method",
      "names": {{"en": "...", "zh": "...", "ko": "..."}},
      "summary": {{"en": "...", "zh": "...", "ko": "..."}},
      "relationship_to_paper": "uses",
      "description": {{"en": "...", "zh": "...", "ko": "..."}},
      "source_citation": "..."
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
- theoretical_depth: choose the deepest level the paper primarily operates at. Papers that introduce a method are "method"; papers that mainly compare hardware are "system"; papers that derive a new formalism are "formalism".
- Tags should be lowercase, snake_case, and specific to humanoid robotics.
- Related_entities and relationships should only include items explicitly discussed in the paper.
- For each proposed relationship, include a source_citation from the paper text.
- target_id (and related_entities id) MUST be copied verbatim from the candidate entity list above; if no candidate fits, omit the item. Never propose a target_id for an entity that is not in the candidate list.
- Each relationship must conform to data/schema/v1/relationship_schema.json:
  - "type" must come from the controlled relationship vocabulary (e.g. cites, uses, requires, enables, builds_on, is_based_on, extends, integrates, formalizes, instantiates, derived_from, has_prerequisite, solves, evaluates_on, verified_by, is_alternative_to, is_part_of, is_subsystem_of, produces, sources_from, proposes, surveys; see the schema file for the full list).
  - "description" must include at least English ("en") and Simplified Chinese ("zh").
  - The pipeline will attach the mandatory "verification" block (status / reviewed_by / confidence) and "sources" (at least 1 entry) downstream, so do not fabricate them.
- knowledge_chain: extract 1-3 key methods/formalisms/equations the paper introduces or relies on. For each child, specify the relationship to the paper (e.g. uses, formalizes, instantiates, builds_on, derived_from). These will later be expanded into standalone knowledge-base nodes.
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
