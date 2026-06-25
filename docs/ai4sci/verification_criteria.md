# Verification Criteria

> **Status**: Draft  
> **Purpose**: Define how claims, entries, and relationships are verified before they enter the public knowledge graph.

---

## 1. Verification Status

Every entity and relationship in the project carries a `verification.status` field. The allowed values are:

| Status | Emoji | Meaning | Use When |
|--------|-------|---------|----------|
| `verified` | ✅ | Claim is supported by a primary source and has been reviewed by a human. | A human has checked the claim against the original source. |
| `partially_verified` | ⚠️ | Claim is supported by the source but has only been AI-extracted or spot-checked. | AI processed full text; human has not fully reviewed every detail. |
| `unverified` | ❓ | Source mentions the claim but it has not been independently confirmed. | The claim appears in a secondary source or press release only. |
| `speculative` | 🔮 | Forward-looking or analytical claim, clearly labeled as such. | The claim is a projection, opinion, or inference from available data. |

---

## 2. Source Types

The `sources.type` field classifies the evidence behind a claim:

| Type | Description | Reliability |
|------|-------------|-------------|
| `primary` | Original research paper, patent, or official dataset. | High |
| `secondary` | Review article, market analysis, or curated report based on primary sources. | Medium |
| `report` | Industry report, teardown, or whitepaper. | Medium–High |
| `press_release` | Official company or institution announcement. | Medium |
| `annual_report` | Company financial or operational report. | High |
| `website` | Project page, documentation, or repository. | Medium |
| `interview` | Published interview or talk transcript. | Medium |
| `other` | Anything not covered above. | Variable |

---

## 3. Reviewed-By Field

The `verification.reviewed_by` field records who performed the last review:

| Value | Meaning |
|-------|---------|
| `human` | A human reviewer verified the entry. |
| `ai` | The entry was generated or checked by AI only. |
| `human_and_ai` | Both AI extraction and human review contributed. |

---

## 4. Confidence Levels

The `verification.confidence` field indicates the reviewer's confidence:

| Level | Meaning |
|-------|---------|
| `high` | Multiple independent sources agree, or a single highly authoritative source supports the claim. |
| `medium` | One credible source supports the claim, or minor inference is required. |
| `low` | The claim is plausible but lacks strong direct evidence. |

---

## 5. Rules for Promoting an Entry to `verified`

Before changing `verification.status` to `verified`, the reviewer must confirm:

1. **Identity**: Title, authors, year, URL, and identifiers (arXiv ID, DOI) are correct.
2. **Scope**: Domains, layers, and functional roles accurately reflect the entity.
3. **Claims**: Every factual claim in the summary or body is supported by a listed source.
4. **Sources**: Sources are primary or reputable secondary; content-farm or unverified marketing material is not used as sole support.
5. **Relationships**: Each relationship is explicitly supported by the source and uses the correct relationship type.
6. **Language**: English is complete; Chinese and Korean summaries are reasonable (human or AI-generated but reviewed).
7. **Speculation**: Any forward-looking claim is labeled `speculative`.

---

## 6. Rules for `partially_verified` AI Drafts

AI-generated drafts that have not been fully human-reviewed should use `partially_verified` with:

- `reviewed_by: ai`
- `confidence: medium` or `low`
- A note such as: "AI-extracted from full text; requires human review before verification."

These drafts remain in `.staging/` until a human approves them.

---

## 7. Handling Conflicts

If two sources disagree:

1. Create entries for both sources.
2. Add a `conflicts_with` relationship between the contradictory claims.
3. Describe the nature of the conflict and any evidence that favors one side.
4. Do not mark either claim as `verified` until the conflict is resolved.

---

## 8. Examples

### Example 1: Paper Entry

```yaml
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: "2026-06-22"
  confidence: medium
  notes: "AI-extracted from arXiv PDF; human review pending."
```

### Example 2: Approved Material Entry

```yaml
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: "2026-06-22"
  confidence: high
  notes: "Confirmed against supplier datasheet and multiple teardown reports."
```

### Example 3: Speculative Market Projection

```yaml
verification:
  status: speculative
  reviewed_by: human
  reviewed_at: "2026-06-22"
  confidence: low
  notes: "Forward-looking market estimate based on analyst assumptions; not a guaranteed outcome."
```
