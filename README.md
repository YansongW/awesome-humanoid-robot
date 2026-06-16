# Awesome Humanoid Robot 🤖

> A curated knowledge base for the **full humanoid robot industry chain**, from raw materials and component supply chains to manufacturing, assembly, testing, mass production, AI/models, applications, and markets.
>
> Curated with **AI4Sci** — AI-assisted scientific research, literature synthesis, and industrial intelligence.

---

## Why This Project Exists

Existing awesome lists for embodied AI and humanoid robots tend to focus narrowly on:

- Vision-Language-Action (VLA) models
- World models (WM)
- Datasets and training frameworks
- Simulation environments

While these are critical, they represent only one layer of the humanoid robot ecosystem. A humanoid robot is not just a model — it is the convergence of:

- **Precision manufacturing** and industrial engineering
- **Global component supply chains** (actuators, sensors, batteries, compute)
- **Materials science** (lightweight alloys, composites, rare-earth magnets)
- **Production processes** (machining, assembly, calibration, testing)
- **AI and control systems** (perception, planning, locomotion, manipulation)
- **Mass production economics** and scaling strategies
- **Application markets** (manufacturing, logistics, healthcare, home, defense)
- **Regulations, safety standards, and ethics**

Humanoid robotics may be one of the fastest transitions from laboratory to factory floor in human history. To understand it, we need a map of the **entire value chain**, not just the algorithmic layer.

This project aims to build that map.

---

## Scope

This project covers the following domains, organized as an industry-chain ontology:

| Domain | What We Track |
|--------|---------------|
| **Raw Materials & Resources** | Rare-earth elements, magnets, lightweight metals, composites, semiconductors, battery chemistries |
| **Components & Subsystems** | Actuators, motors, reducers/gearboxes, sensors, batteries, compute units, end effectors, cables, structural parts |
| **Supply Chain & Manufacturing** | Tier-1/Tier-2 suppliers, manufacturing processes, quality control, cost structures, regional ecosystems |
| **Design & Engineering** | Mechanical design, kinematics, dynamics, humanoid morphology, degrees of freedom, safety design |
| **Assembly, Integration & Testing** | Assembly lines, calibration, system integration, test benches, validation protocols |
| **Mass Production & Scaling** | Factory design, production ramp, unit economics, BOM analysis, yield optimization |
| **AI, Models & Algorithms** | VLAs, world models, locomotion policies, manipulation policies, planning, sim-to-real, SLAM, teleoperation |
| **Software & Middleware** | ROS 2, real-time OS, simulation stacks, digital twins, fleet management, data pipelines |
| **Data & Datasets** | Teleoperation data, motion capture, simulation data, multi-modal datasets, data licensing |
| **Benchmarks & Evaluation** | Sim benchmarks, real-world tasks, hardware-in-the-loop testing, safety standards |
| **Applications & Markets** | Industrial, logistics, healthcare, home, retail, research, defense, entertainment |
| **Companies & Ecosystem** | Startups, OEMs, component vendors, research labs, funding, partnerships |
| **Policy, Regulation & Ethics** | Safety standards, liability, labor impact, privacy, human-robot interaction norms |

---

## AI4Sci Methodology

This project is built with AI-assisted research workflows:

1. **Systematic literature and industry scanning** — track academic papers, patents, company announcements, supply-chain reports, and technical blogs.
2. **Structured extraction** — every entry is tagged by industry-chain position, company/institution, verification status, and relevance.
3. **Cross-reference and verification** — claims are traced to original sources; conflicting information is flagged.
4. **Ontology-driven organization** — entries are placed into a concept map rather than a flat list.
5. **Human review** — AI accelerates collection and synthesis, but all high-stakes claims are reviewed before public release.

See [`docs/ai4sci/`](docs/ai4sci/) for the detailed research pipeline and verification criteria.

---

## Project Status & Release Strategy

> **Current phase**: Private research and framework construction.  
> **Public release target**: `v0.1.0` after the ontology, initial content, and verification workflow are complete.

| Phase | Goal | Visibility |
|-------|------|------------|
| Pre-v0.1.0 | Build ontology, populate initial entries, establish verification workflow | **Private** |
| v0.1.0 | Public launch for community co-creation | **Public** |
| Post-v0.1.0 | Continuous updates, quarterly releases, deeper domain expansion | Public |

Until v0.1.0, the repository is private. All content is treated as a draft and subject to verification before public release.

---

## Directory Structure

```
awesome-humanoid-robot/
├── README.md                          # This file
├── docs/
│   ├── project_charter.md             # Detailed project scope, principles, and governance
│   ├── ontology/
│   │   ├── 00_overview.md             # Industry-chain concept map
│   │   ├── 01_raw_materials.md
│   │   ├── 02_components_supply_chain.md
│   │   ├── 03_manufacturing_processes.md
│   │   ├── 04_assembly_integration_testing.md
│   │   ├── 05_mass_production.md
│   │   ├── 06_applications_markets.md
│   │   ├── 07_ai_models_algorithms.md
│   │   ├── 08_evaluation_benchmarks.md
│   │   └── 09_regulations_ethics.md
│   ├── ai4sci/
│   │   ├── literature_review_pipeline.md
│   │   └── verification_criteria.md
│   └── reference_awesome/
│       └── comparison_with_embodied_vla_va_vln.md
├── research/
│   ├── papers/                        # Paper notes and summaries
│   ├── companies/                     # Company profiles and ecosystem maps
│   └── datasets/                      # Dataset notes
├── data/                              # Structured data files (CSV, JSON, etc.)
└── scripts/                           # AI4Sci helper scripts
```

---

## How to Use This Repository

- **For researchers**: Find the state of the art in humanoid robotics, organized by problem domain and industry layer.
- **For founders / investors**: Map the supply chain, identify gaps, and track competitors.
- **For engineers**: Discover component vendors, simulation tools, datasets, and benchmarks relevant to your subsystem.
- **For policymakers**: Understand the regulatory and ethical landscape.

---

## Contributing

> Public contribution guidelines will be published at `v0.1.0`.

Until then, content is curated by the core team with AI4Sci assistance. If you have access to this private repository, please:

- Add entries with source links and verification status.
- Flag uncertain or conflicting claims.
- Follow the ontology structure in [`docs/ontology/`](docs/ontology/).

---

## License

TBD — to be decided before public release.

---

## Acknowledgments

Inspired by projects like [awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln), but intentionally expanded beyond the algorithmic layer to cover the full humanoid robot value chain.
