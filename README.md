<div align="center">

# Awesome Humanoid Robot 🤖

**A curated, multilingual knowledge graph for going from 0 to 1 on humanoid robot mass production and industrial application.**

<p>
  <img src="https://img.shields.io/badge/status-public%20v0.1.0-success" alt="Status: public v0.1.0" />
  <img src="https://img.shields.io/badge/entries-2144-green" alt="2144 entries" />
  <img src="https://img.shields.io/badge/relationships-5687-brightgreen" alt="5687 relationships" />
  <img src="https://img.shields.io/badge/languages-zh%2Fen%2Fko-blue" alt="Languages: zh/en/ko" />
  <img src="https://img.shields.io/badge/validation-passing-success" alt="Validation passing" />
</p>

🌐 **Live site**: [kg.rounds-tech.com](https://kg.rounds-tech.com)  
🌐 [English](README.md) · [简体中文](README.zh.md) · [한국어](README.ko.md)

⭐ If this map helps your research or build, please give us a star — it helps more researchers and builders find it.

</div>

---

## 📌 What is this project?

**Awesome Humanoid Robot** is a structured, living, open-source knowledge base built around one central question:

> **How do we go from 0 to 1 to achieve humanoid robot mass production and industrial application?**

It tracks every layer of the journey — from raw materials and components to manufacturing, design, AI, software, data, testing, mass production, applications, markets, policy, and regulation. Instead of a flat list of papers or products, we model the domain as a **knowledge graph**: entities are nodes, relationships are typed edges, and every claim is traceable to a source.

At **v0.1.0**, the project has evolved from a research pipeline into a productized knowledge service:

- 🌐 A public, multilingual website at **[kg.rounds-tech.com](https://kg.rounds-tech.com)** with search, interactive graph browsing, and a linked Wiki.
- 📖 An in-repo **Wiki** derived from the book *Humanoid Robots: From Mine to Market*, providing systematic, chapter-by-chapter narrative coverage.
- 🔗 Bidirectional links between Wiki chapters and KG entities, so readers can move smoothly from narrative to structured data and back.

The project is **AI-assisted, human-verified**. We use AI4Sci pipelines to accelerate discovery, extraction, and synthesis, while keeping humans in the loop for approval before anything is promoted to production.

---

## ✨ What's new in v0.1.0

- 🌐 **Live product site** at [kg.rounds-tech.com](https://kg.rounds-tech.com) — trilingual UI, full-text search, interactive Cytoscape graph, and linked Wiki.
- 📖 **In-repo Wiki** — 30 narrative chapters + 7 appendices derived from *Humanoid Robots: From Mine to Market*, rendered with admonitions, Mermaid diagrams, and KaTeX formulas.
- 🗂️ **2,144 validated KG entries** and **5,687 typed relationships** covering the full stack from raw materials to market applications.
- 🔄 **Automated CI/CD** — GitHub Actions builds and deploys the site to GitHub Pages on every push to `main`.
- 🛡️ **Hardened deployment** — concurrency control and clean `gh-pages` branch recreation prevent race-condition failures.
- 🧩 **Backfilled core non-paper entity bodies** — 233 critical entities now have structured Chinese bodies with 概述 / 核心内容 / 参考 sections, sourced from the Wiki where available and from entity metadata otherwise.
- 🌏 **Machine-translated missing English names and summaries** — all process and paper entries missing `names.en` / `summary.en` have been filled via machine translation and marked for human review.
- 📝 **Backfilled structured bodies for all critical paper entries** — 215 paper entries now have Chinese 概述 / 核心内容 / 参考 sections generated from metadata and marked for human review; quality audit shows 0 critical issues.

---

## 🎯 Why we are building it

Humanoid robotics is at an inflection point. Labs around the world can already build robots that walk, manipulate, and interact. But a robot that works in a demo is not the same as a robot that can be **mass-produced, deployed, and maintained at scale**.

The gap is not just an AI problem. It is a **systems problem** that connects:

- 🪨 **Materials science** — rare-earth magnets, battery chemistries, lightweight alloys
- ⚙️ **Precision manufacturing** — machining, winding, casting, assembly, quality control
- 🌐 **Global supply chains** — tier-1/tier-2 suppliers, regional ecosystems, cost structures
- 🧠 **AI & software** — VLAs, world models, control, planning, sim-to-real
- 📊 **Data infrastructure** — datasets, simulators, benchmarks, fleet telemetry
- 🏭 **Mass production** — factory design, yield optimization, BOM cost engineering
- ⚖️ **Policy & society** — safety standards, certification, liability, labor impact

Today, information about these layers is scattered across academic papers, company press releases, teardowns, industry reports, and technical blogs. Decision makers — researchers, engineers, founders, investors, policymakers — lack a single, structured map that shows how the pieces fit together, where the bottlenecks are, and what trade-offs determine success.

This project is that map.

> Our goal is not to collect every paper. It is to understand the **full journey from mine to market**, and to make that understanding verifiable, reusable, and community-curated.

---

## 🌐 Product: the KG website

The `website/` directory builds a static, product-level frontend for the knowledge graph.

**Live URL**: [https://kg.rounds-tech.com](https://kg.rounds-tech.com)

Features at v0.1.0:

- **Trilingual interface** — independent `zh`, `en`, and `ko` sites with a language switcher in the header.
- **Domain browsing** — explore the graph by industry domain or entity type.
- **Full-text search** — client-side search with type filters and language-aware labels.
- **Interactive relation graph** — Cytoscape.js visualization with cluster view and full-graph view.
- **Entity pages** — summaries, domains, layers, relationships, related entities, and linked Wiki chapters.
- **Integrated Wiki** — 30 chapters + 7 appendices rendered with admonitions, Mermaid diagrams, and KaTeX formulas.

Build it locally:

```bash
cd website
pip install -r requirements.txt
python3 -m builder.build
# Serve the dist/ directory
python3 -m http.server 8080 --directory dist
```

The experimental FastAPI backend (natural-language Q&A) lives in `web/` and is documented in [`web/README.md`](web/README.md).

---

## 🗺️ What you will find here

| Domain | What we track |
|--------|---------------|
| **Foundations** | Cross-cutting math, physics, chemistry, and CS concepts that underpin every engineering domain |
| **Raw Materials & Resources** | Rare-earth elements, magnets, lightweight metals, composites, semiconductors, battery chemistries |
| **Components & Subsystems** | Actuators, motors, reducers/gearboxes, sensors, batteries, compute units, end effectors, cables, structural parts |
| **Supply Chain & Manufacturing** | Tier-1/Tier-2 suppliers, manufacturing processes, quality control, cost structures, regional ecosystems |
| **Design & Engineering** | Mechanical design, kinematics, dynamics, morphology, degrees of freedom, safety design |
| **Assembly, Integration & Testing** | Assembly lines, calibration, system integration, test benches, validation protocols |
| **Mass Production & Scaling** | Factory design, production ramp, unit economics, BOM analysis, yield optimization |
| **AI, Models & Algorithms** | VLAs, world models, locomotion policies, manipulation policies, planning, sim-to-real, SLAM, teleoperation |
| **Software & Middleware** | ROS 2, real-time OS, simulation stacks, digital twins, fleet management, data pipelines |
| **Data & Datasets** | Teleoperation data, motion capture, simulation data, multi-modal datasets, data licensing |
| **Benchmarks & Evaluation** | Sim benchmarks, real-world tasks, hardware-in-the-loop testing, safety standards |
| **Applications & Markets** | Industrial manufacturing, logistics, healthcare, home service, retail, research, defense, entertainment |
| **Companies & Ecosystem** | Startups, OEMs, component vendors, research labs, funding, partnerships |
| **Policy, Regulation & Ethics** | Safety standards, liability, labor impact, privacy, human-robot interaction norms |

---

## 🏗️ Architecture-first approach

Before adding content, we built a formal information model that can represent the entire industry chain as a graph.

- **Graph-first**: entities are nodes, relationships are directed, typed edges.
- **Dual tagging**: every entity has both a **value-chain layer** (foundations / upstream / midstream / intelligence / validation-markets) and a **functional role** (material / component / process / system / intelligence / etc.).
- **Foundational knowledge domain**: cross-cutting math, physics, chemistry, and CS topics live in `00_foundations` so they can be shared across engineering trees.
- **Relationships as first-class citizens**: cross-domain links are explicit, typed, and verifiable.
- **Multi-lingual by design**: names, summaries, and descriptions are stored as language maps (en / zh / ko).
- **Versioned schemas**: entry and relationship schemas are versioned and extensible.
- **Fine-grained theoretical depth**: equations, operators, variables, constants, algorithms, and approximations can be explicit nodes.
- **YAML frontmatter + Markdown**: entries are human-readable and machine-readable.

See [`docs/architecture/information_model.md`](docs/architecture/information_model.md) and [`data/schema/v1/`](data/schema/v1/) for the full specification.

---

## ⚙️ How it works: unified ingestion + AI4Sci enrichment

1. **Curated ingestion** — `scripts/ingestion/pipeline.py` pulls high-confidence sources daily:
   - arXiv RSS, curated GitHub lists, paper-notebook progress files
   - Company/lab blogs and news APIs (Unitree, NVIDIA, etc.)
   - WeChat articles (when a URL list or text dump is provided)
   - New items are deduplicated against titles, arXiv IDs, and source URLs before writing.
2. **AI4Sci enrichment** *(currently paused pending quality-gate redesign)* — workstreams query arXiv/Semantic Scholar for deeper synthesis, cross-layer relationships, and proprietary/industry intelligence.
3. **Staging & review** — AI drafts land in `.staging/` for isolated review.
4. **Autonomous review** — `scripts/ai4sci_autonomous_review.py` validates schema, checks sources/duplicates, and archives high-confidence drafts automatically.
5. **Human review** — a reviewer inspects the remaining queue and rejects or fine-tunes edge cases.
6. **Integration & validation** — approved entries move to `research/` and `data/relationships/` and must pass `scripts/validate_entries.py`.

Run the daily ingestion pipeline:

```bash
bash scripts/ingest_all_sources.sh
```

The framework is documented in [`docs/ingestion/README.md`](docs/ingestion/README.md); the legacy AI4Sci pipeline is in [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md).

---

## 🚀 Quick start

```bash
# 1. Clone the repository
git clone https://github.com/YansongW/awesome-humanoid-robot.git
cd awesome-humanoid-robot

# 2. Validate the current knowledge graph
python scripts/validate_entries.py

# 3. Build the product website
cd website
pip install -r requirements.txt
python3 -m builder.build
python3 -m http.server 8080 --directory dist

# 4. Run the unified ingestion pipeline (daily cron)
python -m ingestion.pipeline --all

# 5. Start the experimental FastAPI Q&A backend (optional)
pip install -r web/requirements.txt
export AI4SCI_API_KEY="your-openai-compatible-key"
export AI4SCI_BASE_URL="https://api.deepseek.com/v1"
uvicorn web.app:app --reload --host 127.0.0.1 --port 8000
```

For credential setup, see [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md) and [`web/README.md`](web/README.md).

---

## 📊 Project stats

| Metric | Count |
|--------|-------|
| Production entries | 2,144 |
| Relationships | 5,687 |
| Ontology domains | 13 (12 + `00_foundations`) |
| Entity types | 24 |
| Wiki chapters | 30 |
| Wiki appendices | 7 |
| Supported languages | en, zh, ko |
| Validation status | ✅ passing |
| Quality audit | 1,643 ok / 285 warning / 215 paper-body gaps |

---

## 🛣️ Roadmap

| Phase | Goal | Status |
|-------|------|--------|
| **Phase 0** | Information architecture, schemas, validation | ✅ Complete |
| **Phase 1** | Per-domain ontology documents (01–12) | ✅ Complete |
| **Phase 2** | Workstream-driven content population + schema/relationship evolution | ✅ Complete |
| **Phase 2.5** | Static product website with search, graph, and Wiki | ✅ Complete |
| **Phase 3** | Public v0.1.0 release (open source + live site) | ✅ Complete |
| **Phase 4** | Content completeness: fill gaps, deepen foundational knowledge, expand Wiki–KG links | 🔄 In progress (non-paper core entities done; English translation done; paper abstract backfill remaining) |
| **Phase 5** | Verification workflow, community contributions, v0.2.0 | ⏳ Planned |

See [`docs/ai4sci/WORKSTREAM_TREE.md`](docs/ai4sci/WORKSTREAM_TREE.md) for the full workstream TODO list and [`docs/session_status.md`](docs/session_status.md) for the latest session notes.

---

## 👥 Who is this for?

- **Researchers** — find the state of the art organized by problem domain and industry layer.
- **Engineers** — discover component vendors, simulation tools, datasets, and benchmarks relevant to your subsystem.
- **Founders / investors** — map the supply chain, identify gaps, and track competitors.
- **Manufacturing & operations** — understand factory design, yield, cost drivers, and scaling trade-offs.
- **Policymakers** — understand the regulatory, safety, and ethical landscape.

---

## 🤝 Contributing

Public contribution guidelines will be published in Phase 5. Until then:

- Content is curated by the core team with AI4Sci assistance.
- If you have access, add entries with source links and verification status.
- Flag uncertain or conflicting claims via issues.
- Follow the ontology structure in [`docs/ontology/`](docs/ontology/) and the entry format in [`docs/architecture/information_model.md`](docs/architecture/information_model.md).

---

## 📂 Directory structure

```
awesome-humanoid-robot/
├── README.md                          # This file
├── README.zh.md                       # 简体中文
├── README.ko.md                       # 한국어
├── LICENSE                            # MIT license (code)
├── docs/
│   ├── project_charter.md             # Project scope, principles, governance
│   ├── WIKI-KG-SYNC.md                # Wiki ↔ KG synchronization workflow
│   ├── ontology/                      # Industry-chain ontology documents (01–12 + overview)
│   ├── architecture/                  # Information model and pre-design analysis
│   └── ai4sci/                        # AI4Sci pipeline docs and workstream taxonomy
├── research/                          # Production knowledge-base entries
│   ├── foundations/                   # Math, physics, chemistry, CS concepts
│   ├── materials/                     # Raw materials
│   ├── components/                    # Components and subsystems
│   ├── companies/                     # Company profiles and ecosystem maps
│   ├── papers/                        # Paper notes
│   └── datasets/                      # Dataset notes
├── data/
│   ├── schema/v1/                     # JSON Schemas
│   ├── relationships/                 # Standalone relationship files
│   └── wiki-chapter-mapping.yaml      # Wiki chapter ↔ KG entity mapping
├── wiki/                              # In-repo Wiki source (Markdown + MkDocs config)
│   ├── docs/chapters/                 # 30 narrative chapters
│   ├── docs/appendices/               # 7 appendices
│   └── mkdocs.yml                     # MkDocs configuration
├── website/                           # Static product website builder + assets
│   ├── builder/                       # Python static-site generator
│   ├── templates/                     # Jinja2 HTML templates
│   ├── src/                           # CSS / JS assets
│   └── dist/                          # Generated site (ignored by git)
├── web/                               # Experimental FastAPI frontend for Q&A
│   ├── app.py
│   ├── kg_store.py
│   ├── llm_qa.py
│   └── README.md
├── scripts/                           # AI4Sci helper scripts
│   ├── ai4sci_lib/
│   ├── ai4sci_workstreams/
│   ├── ai4sci_paper_pipeline.py
│   ├── ai4sci_batch_pipeline.py
│   ├── ai4sci_orchestrator.py
│   ├── ai4sci_review.py
│   ├── ai4sci_status.py
│   └── validate_entries.py
└── .staging/                          # AI-generated drafts pending human review
```

---

## 📜 License

- **Code** (builder, scripts, website frontend, etc.): [MIT](LICENSE)
- **Wiki content** (`wiki/`): [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

<div align="center">

**Built with curiosity, rigor, and a belief that humanoid robotics needs a map, not just more demos.**

</div>
