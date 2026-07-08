# Unified Ingestion Framework

The `scripts/ingestion/` package replaces the ad-hoc `import_*.py` / `ingest_*.py` scripts with a single, source-agnostic pipeline.

## Goals

- **One command to run everything**: `bash scripts/ingest_all_sources.sh`
- **Pluggable adapters**: each source implements `fetch(Source) -> list[ParsedItem]`.
- **Deduplication by default**: titles, arXiv IDs, and source URLs are checked against production + staging before writing.
- **Schema-compliant output**: entries are written with valid frontmatter, inferred layers, and `verification.status`.
- **Dry-run support**: preview counts without touching `research/`.

## Source registry

Configured in `data/sources.yaml`:

| Source ID | Type | Schedule | Status |
|-----------|------|----------|--------|
| `awesome_vla_models` | `curated_json` | on_demand | imported (disabled) |
| `awesome_humanoid_robot_learning` | `curated_json` | on_demand | imported (disabled) |
| `humanoid_paper_notebooks_progress` | `github_json` | daily | healthy |
| `arxiv_ro_rss` | `rss` | daily | healthy |
| `unitree_news` | `api` | weekly | healthy |
| `nvidia_robotics_blog` | `rss` | weekly | healthy |
| `robotics_tomorrow_rss` | `rss` | daily | healthy |
| `ieee_spectrum_robotics_rss` | `rss` | daily | healthy |
| `iso_robotics_news` | `rss` | weekly | blocked (anti-scraping) |
| `wechat_articles` | `wechat` | on_demand | pending |

## Running the pipeline

```bash
# All enabled sources
PYTHONPATH=scripts python -m ingestion.pipeline --all

# Single source, preview only
PYTHONPATH=scripts python -m ingestion.pipeline --source arxiv_ro_rss --dry-run

# Machine-readable output
PYTHONPATH=scripts python -m ingestion.pipeline --all --json
```

The cron wrapper at `scripts/ingest_all_sources.sh` activates the venv, runs the pipeline, then regenerates the coverage dashboard.

## Adding a new source

1. Create `scripts/ingestion/adapters/my_source.py` with a class that has:
   - `source_id: str`
   - `fetch(self, source: Source) -> list[ParsedItem]`
2. Register the adapter in `scripts/ingestion/adapters/__init__.py` and `scripts/ingestion/pipeline.py:ADAPTER_MAP`.
3. Add the source to `data/sources.yaml`.
4. Run a dry-run: `python -m ingestion.pipeline --source my_source --dry-run`.

## Deduplication rules

`DedupService` normalizes titles (strips numbering/punctuation/URLs, lowercases) and checks:

- normalized title against existing entry names
- arXiv ID against existing sources
- source URL against existing sources

Newly written items within the same batch are also registered so intra-batch duplicates are skipped.

## Adapters

### Curated JSON (`curated_json.py`)

Reads `data/curated/awesome_vla_papers.json` and `data/curated/awesome_humanoid_robot_learning.json`, maps categories to domains/tags, and extracts arXiv IDs.

### Progress JSON (`progress_json.py`)

Fetches `Humanoid_Robot_Learning_Paper_Notebooks/progress.json` via GitHub API or local path, maps folder names to the project taxonomy.

### arXiv RSS (`arxiv_rss.py`)

Parses `http://export.arxiv.org/rss/cs.RO` and filters by configured keywords.

### Unitree API (`unitree_api.py`)

Calls `/website/news/list` and `/news/info`, keeps English-language items that match humanoid/robotics keywords, and imports them as `report` entries.

### NVIDIA RSS (`nvidia_rss.py`)

Parses the NVIDIA robotics blog RSS and imports matching posts. Posts about GR00T/Isaac/Cosmos are typed as `technology`/`software_platform`; others are `report`.

### RoboticsTomorrow (`robotics_tomorrow.py`)

Parses `https://www.roboticstomorrow.com/rss/news` for industry, business, and hardware news. Classifies items into `report`, `company`, `component`, or `technology` based on title keywords.

### IEEE Spectrum Robotics (`ieee_spectrum.py`)

Parses `https://spectrum.ieee.org/feeds/topic/robotics.rss` for technical and research articles; all items are typed as `report`.

### ISO Standards (`iso_standards.py`)

Configured for ISO robotics standards news but currently disabled because `iso.org` blocks automated RSS requests. Enable after obtaining a WebBridge text dump or proxy access.

### WeChat (`wechat_article.py`)

Expects either:

- a JSON file at `source.fetch_url` containing extracted paper metadata, or
- a URL list in `source.extra["urls"]` with extracted texts in `source.extra["texts"]`.

Because WeChat anti-crawls heavily, the adapter is currently disabled pending a URL list or Kimi WebBridge text dump.

## Legacy scripts

Old ad-hoc scripts are archived in `scripts/legacy/` for reference but are no longer run by the cron job.
