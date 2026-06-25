# AI4Sci Literature Review Pipeline

> **Status**: Multi-Agent Workstream Mode — `scripts/ai4sci_orchestrator.py` and Kimi Code CLI (`AgentSwarm`) are used to run parallel domain workstreams.  
> **Last updated**: 2026-06-25  
> **Purpose**: Define the automated, human-in-the-loop workflow for discovering, reading, extracting, and staging academic/industry sources for the `awesome-humanoid-robot` knowledge base.

---

## 1. Overview

This project uses **AI4Sci** — AI-assisted research, synthesis, and verification — to populate a structured knowledge graph about humanoid robot mass production. The literature pipeline turns raw papers and industry sources into draft entries and relationship files, while keeping humans in control of final approval.

The pipeline is now organized around **workstreams**. A workstream is a focused research task mapped to one leaf of the 0→1 knowledge tree defined in [`workstream_roadmap.md`](workstream_roadmap.md) and tracked in [`WORKSTREAM_TREE.md`](WORKSTREAM_TREE.md).

The pipeline has four phases:

| Phase | Deliverable | Status |
|-------|-------------|--------|
| 1 | Single-paper draft generator | ✅ Ready |
| 2 | Relevance-based discovery feed & workstream runner | ✅ Ready (arXiv sort-by-relevance fix landed) |
| 3 | Review & approval workflow | ✅ Ready |
| 4 | CI/dashboard integrations | 🚧 Future |

---

## 2. Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              Workstream Tree                                 │
│   (docs/ai4sci/WORKSTREAM_TREE.md)                                           │
└─────────────────────────────────┬───────────────────────────────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Workstream YAML Configs                              │
│   (scripts/ai4sci_workstreams/**/*.yaml)                                     │
└─────────────────────────────────┬───────────────────────────────────────────┘
                                  ▼
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
   Discovery              Relevance Rank            Full-Text Get
        │                         │                         │
        └─────────────┬───────────┴───────────┬─────────────┘
                      ▼                       ▼
              LLM Extraction ──▶ Staging ──▶ Human Review ──▶ Integration ──▶ Validation
```

### 2.1 Discovery

Sources used by workstreams:

- **arXiv API** — primary source; search uses `relevance` sort and deduplicates against existing entries.
- **Semantic Scholar API** — secondary source for arXiv-backed papers (no API key required for light usage).
- *Planned/future*: Google Scholar keyword alerts, conference proceedings RSS, company technical blogs and preprints, web search for industry reports, teardowns, and standards updates.

### 2.2 Relevance Ranking

Two-stage filter:

1. **Hard keyword filter**: title/abstract must contain terms from the humanoid-robotics vocabulary (e.g., humanoid, bipedal, VLA, actuator, supply chain).
2. **LLM classifier**: scores each paper/source as `high`, `medium`, or `low` relevance to the central question: *How do we go from 0 to 1 on humanoid robot mass production and industrial application?*

### 2.3 Full-Text Acquisition

- Prefer arXiv PDFs (open access).
- Extract clean text from downloaded PDFs.
- Fallback to abstract-only extraction when PDF access fails.
- For manual URLs, the pipeline resolves arXiv IDs and PDF links automatically.

### 2.4 LLM Extraction

The LLM reads the source and produces:

- Core metadata (title, authors, year, venue, abstract, problem, method).
- Structured entry frontmatter (type, names, summaries in en/zh/ko, domains, layers, roles, theoretical depth, tags, sources).
- Markdown body (overview, key contributions, relevance to humanoid robotics).
- Proposed relationships to existing or new entities, including foundational links (`formalizes`, `uses_theorem`, `derived_from`, `instantiates`, `builds_on`, `has_prerequisite`, `uses`, `includes`, `solves`, `estimates`, `minimizes`, `approximates`).
- Review notes flagging uncertain claims.

### 2.5 Staging

All AI-generated drafts land in `.staging/`:

```
.staging/
├── research/
│   ├── papers/
│   ├── datasets/
│   ├── benchmarks/
│   ├── technologies/
│   └── ...
├── data/relationships/
├── review/
├── rejected/
└── pdfs/
```

Workstream outputs are isolated in `.staging/workstreams/<name>/` so different workstreams do not collide.

Drafts are **not** part of the validated knowledge graph until approved.

### 2.6 Human Review

A reviewer inspects:

- The draft entry file.
- The proposed relationship files.
- The generated review report.

Actions:

- **Approve**: move to production paths and run validation.
- **Edit**: modify the draft, then approve.
- **Reject**: move to `.staging/rejected/` with a reason.

### 2.7 Integration & Validation

Approved entries are moved to `research/` and `data/relationships/`. The project validation script ensures schema compliance:

```bash
source .venv/bin/activate
python scripts/validate_entries.py
# include workstream staging
python scripts/validate_entries.py --include-workstreams
```

---

## 3. Multi-Agent Workstream Mode

For parallel content population across multiple domains, the pipeline supports **workstreams**. Each workstream is a YAML config in `scripts/ai4sci_workstreams/` that defines seed queries, target entity types, target domains, and relationship patterns.

The workstream directory is organized as a tree that mirrors the 0→1 knowledge taxonomy:

```
scripts/ai4sci_workstreams/
├── definition/
│   └── algorithm_survey/
│       └── vla.yaml
├── design/
│   ├── hardware/
│   │   └── actuation/
│   │       └── actuator_module_design.yaml
│   └── software_ai/
├── mass_production/
│   ├── factory/
│   └── supply_chain/
├── safety_certification/
├── cross_domain/
└── ...
```

A workstream can be executed:

- **As a single batch**:
  ```bash
  python scripts/ai4sci_batch_pipeline.py scripts/ai4sci_workstreams/definition/algorithm_survey/vla.yaml --max-papers 10 --max-workers 2
  ```

- **Via the multi-agent orchestrator**:
  ```bash
  python scripts/ai4sci_orchestrator.py --max-workers 2 --max-batch-workers 1 --max-papers 10
  ```

- **By dispatching parallel AI subagents** (e.g., via Kimi Code CLI `AgentSwarm`), each subagent reads one workstream config, performs web/arXiv discovery, drafts entries and relationships, validates them, and stages them for review.

Review and approval can happen per workstream:

```bash
python scripts/ai4sci_review.py --workstream vla
python scripts/ai4sci_review.py --all-workstreams --auto-approve  # use with caution
```

---

## 4. Current Scripts

### 4.1 `scripts/ai4sci_paper_pipeline.py`

Generate a draft entry from a single paper.

**Option A — Standard API key (OpenAI-compatible):**

```bash
export AI4SCI_API_KEY="your-api-key"
export AI4SCI_BASE_URL="https://api.moonshot.cn/v1"
export AI4SCI_MODEL="kimi-latest"
python scripts/ai4sci_paper_pipeline.py https://arxiv.org/abs/2604.23001
```

**Option B — Desktop credential file (recommended for this workspace):**

A preconfigured credential file lives at `~/Desktop/ai4sci_api_key.txt`. Source it before running any pipeline:

```bash
source .venv/bin/activate
export $(grep -v '^#' ~/Desktop/ai4sci_api_key.txt | xargs)
python scripts/ai4sci_paper_pipeline.py https://arxiv.org/abs/2604.23001
```

**Option C — Kimi Code CLI-only credential (no standard API key):**

If your key only works inside Kimi Code CLI / IDE plugins, force the pipeline to call the local `kimi` binary:

```bash
export AI4SCI_USE_KIMI_CLI=1
python scripts/ai4sci_paper_pipeline.py https://arxiv.org/abs/2604.23001
```

The pipeline will fall back to the CLI automatically when the HTTP API returns `401`/`403`.

Options:
- `--dry-run`: print draft without writing files.
- `--relevance-threshold {low,medium,high}`: skip papers below threshold.
- `--type`: override entity type.
- `--output-dir`: write to a custom directory.

### 4.2 `scripts/ai4sci_review.py`

Interactive review and approval of staged drafts.

```bash
source .venv/bin/activate
python scripts/ai4sci_review.py
```

Actions per staged item:

- **approve**: promote to production and upgrade verification status.
- **edit**: open the file in `$EDITOR`, then re-review.
- **reject**: move to `.staging/rejected/` with a reason.
- **skip**: leave in staging for later.

Use `--auto-approve` only when you have already reviewed files manually.

### 4.3 `scripts/ai4sci_batch_pipeline.py`

Batch runner for a single workstream. Discovers papers, classifies relevance, and extracts entries/relationships in parallel.

```bash
python scripts/ai4sci_batch_pipeline.py scripts/ai4sci_workstreams/definition/algorithm_survey/vla.yaml --max-papers 10 --max-workers 2
```

### 4.4 `scripts/ai4sci_orchestrator.py`

Multi-workstream dispatcher. Recursively discovers all `.yaml` configs under `scripts/ai4sci_workstreams/` and runs them in parallel (local subprocess mode).

```bash
python scripts/ai4sci_orchestrator.py --max-workers 2 --max-papers 10
# verify discovery without running
python scripts/ai4sci_orchestrator.py --dry-run
```

### 4.5 `scripts/ai4sci_status.py`

Dashboard showing pending reviews and workstream progress.

```bash
python scripts/ai4sci_status.py
```

### 4.6 `scripts/ai4sci_literature_watch.py` (planned)

Poll discovery sources and queue high-relevance papers for processing.

---

## 5. Configuration

The pipeline reads environment variables:

| Variable | Default | Purpose |
|----------|---------|---------|
| `AI4SCI_API_KEY` | — | LLM API key (falls back to `OPENAI_API_KEY`) |
| `AI4SCI_BASE_URL` | `https://api.moonshot.cn/v1` | OpenAI-compatible endpoint |
| `AI4SCI_MODEL` | `kimi-latest` | Model name |
| `AI4SCI_USE_KIMI_CLI` | `false` | Force local Kimi Code CLI backend instead of HTTP API |

For non-Kimi endpoints (e.g., DeepSeek), set `AI4SCI_BASE_URL` and `AI4SCI_MODEL` accordingly (e.g., `https://api.deepseek.com/v1` and `deepseek-chat`).

For non-Kimi endpoints, set `AI4SCI_BASE_URL` and `AI4SCI_MODEL` accordingly.

---

## 6. Quality Rules

1. Every AI draft defaults to `verification.status: partially_verified` and `reviewed_by: ai`.
2. A human reviewer must upgrade to `verified` after spot-checking claims.
3. Speculative or analytical claims must be explicitly labeled.
4. Every proposed relationship must include a source citation from the source.
5. Duplicates are blocked by checking existing `$id`s.
6. All approved entries must pass `scripts/validate_entries.py`.
7. Each workstream must map its outputs to the 12 ontology domains listed in `docs/ontology/00_overview.md`.

---

## 7. Open Questions

1. Should the discovery feed also monitor non-paper sources (company blogs, teardowns, standards bodies) on a regular schedule?
2. How should we handle paywalled papers where full text is unavailable?
3. What is the right balance between LLM-generated multi-language summaries and human translation review?
4. Should we maintain a separate "pending sources" queue for sources that are relevant but not yet processed?
5. How do we version workstream configs as the taxonomy evolves?
