<div align="center">

# Awesome Humanoid Robot 🤖

**A curated knowledge graph for going from 0 to 1 on humanoid robot mass production and industrial application.**

<p>
  <img src="https://img.shields.io/badge/status-private%20pre--v0.1.0-blueviolet" alt="Status: private pre-v0.1.0" />
  <img src="https://img.shields.io/badge/entries-91-green" alt="91 entries" />
  <img src="https://img.shields.io/badge/relationships-58-brightgreen" alt="58 relationships" />
  <img src="https://img.shields.io/badge/workstreams-23-orange" alt="23 workstreams" />
  <img src="https://img.shields.io/badge/validation-passing-success" alt="Validation passing" />
</p>

🌐 [English](README.md) · [简体中文](README.zh.md) · [한국어](README.ko.md)

</div>

---

## 📌 What is this project?

**Awesome Humanoid Robot** is a structured, living knowledge base built around one central question:

> **How do we go from 0 to 1 to achieve humanoid robot mass production and industrial application?**

It tracks every layer of the journey — from raw materials and components to manufacturing, design, AI, software, data, testing, mass production, applications, markets, policy, and regulation. Instead of a flat list of papers or products, we model the domain as a **knowledge graph**: entities are nodes, relationships are typed edges, and every claim is traceable to a source.

The project is **AI-assisted, human-verified**. We use AI4Sci pipelines to accelerate discovery, extraction, and synthesis, while keeping humans in the loop for approval before anything is promoted to production.

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

## 🗺️ What you will find here

| Domain | What we track |
|--------|---------------|
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
| **Foundations** | Cross-cutting math, physics, chemistry, and CS concepts that underpin every engineering domain |

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

## ⚙️ How it works: AI4Sci + human review

1. **Systematic scanning** — workstreams query arXiv, Semantic Scholar, and (planned) web sources for relevant papers and industry intelligence.
2. **Relevance classification** — an LLM scores each source against the central question and drops low-relevance items.
3. **Structured extraction** — the LLM drafts typed entries, multi-lingual summaries, and proposed relationships.
4. **Staging** — all AI drafts land in `.staging/` for isolated review.
5. **Human review** — a reviewer approves, edits, or rejects each draft.
6. **Integration & validation** — approved entries move to `research/` and `data/relationships/` and must pass `scripts/validate_entries.py`.

The full pipeline is documented in [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md).

---

## 🚀 Quick start

```bash
# 1. Clone the repository
git clone https://github.com/YansongW/awesome-humanoid-robot.git
cd awesome-humanoid-robot

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Validate the current knowledge graph
python scripts/validate_entries.py

# 4. Run a single workstream (example: VLA survey)
python scripts/ai4sci_batch_pipeline.py \
  scripts/ai4sci_workstreams/definition/algorithm_survey/vla.yaml \
  --max-papers 5 --max-workers 2

# 5. Or run multiple workstreams in parallel
python scripts/ai4sci_orchestrator.py --max-workers 2 --max-batch-workers 1 --max-papers 5

# 6. Review staged outputs
python scripts/ai4sci_review.py
```

For credential setup, see [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md).

---

## 📊 Project stats

| Metric | Count |
|--------|-------|
| Production entries | 91 |
| Relationships | 58 |
| Workstream configs | 23 |
| Ontology domains | 12 + `00_foundations` |
| Supported languages | en, zh, ko |
| Validation status | ✅ passing |

---

## 🛣️ Roadmap

| Phase | Goal | Status |
|-------|------|--------|
| **Phase 0** | Information architecture, schemas, validation | ✅ Complete |
| **Phase 1** | Per-domain ontology documents (01–12) | ✅ Complete |
| **Phase 2** | Workstream-driven content population | 🔄 In progress |
| **Phase 3** | Internal review, verification workflow, v0.1.0 public release | ⏳ Planned |

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

> Public contribution guidelines will be published at `v0.1.0`.

Until then, content is curated by the core team with AI4Sci assistance. If you have access to this private repository, please:

- Add entries with source links and verification status.
- Flag uncertain or conflicting claims.
- Follow the ontology structure in [`docs/ontology/`](docs/ontology/) and the entry format in [`docs/architecture/information_model.md`](docs/architecture/information_model.md).

---

## 📂 Directory structure

```
awesome-humanoid-robot/
├── README.md                          # This file
├── README.zh.md                       # 简体中文
├── README.ko.md                       # 한국어
├── docs/
│   ├── project_charter.md             # Project scope, principles, governance
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
│   └── relationships/                 # Standalone relationship files
├── scripts/                           # AI4Sci helper scripts
│   ├── ai4sci_lib/                    # Reusable pipeline stages
│   ├── ai4sci_workstreams/            # Workstream YAML configs
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

TBD — to be decided before public release.

---

<div align="center">

**Built with curiosity, rigor, and a belief that humanoid robotics needs a map, not just more demos.**

</div>
