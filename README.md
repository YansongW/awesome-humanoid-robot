# Awesome Humanoid Robot 🤖

> A curated knowledge base for going **from 0 to 1 on humanoid robot mass production and industrial application**.
>
> Curated with **AI4Sci** — AI-assisted scientific research, literature synthesis, and industrial intelligence.
>
> 🌐 [English](README.md) · [简体中文](README.zh.md) · [한국어](README.ko.md)

---

## Why This Project Exists

This project is built around one question:

> **How do we go from 0 to 1 to achieve humanoid robot mass production and industrial application?**

A humanoid robot that works in a lab is not the same as a humanoid robot that can be mass-produced, deployed, and maintained in the real world. The gap between a working prototype and a scalable product spans every layer of the system:

- **Raw materials and resources**: What minerals, metals, magnets, and chemicals does a humanoid robot consume? Where do they come from? What are the supply risks?
- **Components and subsystems**: Motors, reducers, sensors, batteries, compute, end effectors, structural parts — who makes them, how do they perform, and what do they cost?
- **Manufacturing processes**: How are these components machined, cast, wound, assembled, and tested at precision and scale?
- **Design and systems engineering**: What determines the robot's morphology, kinematics, dynamics, reliability, and safety?
- **Software and AI**: What algorithms enable perception, planning, locomotion, manipulation, and long-horizon autonomy?
- **Data and infrastructure**: What datasets, simulators, middleware, and toolchains are needed to develop and validate these systems?
- **Assembly, integration, and testing**: How does a robot go from a pile of parts to a calibrated, validated product?
- **Mass production**: What factory design, supply-chain coordination, yield control, and cost engineering are required to produce thousands or millions of units?
- **Applications and markets**: In which industries and tasks are humanoid robots actually useful and economically viable today? Tomorrow?
- **Policy and regulation**: What safety standards, certifications, liability frameworks, and social norms enable or block deployment?

We use **AI4Sci** — AI-assisted research, synthesis, and verification — to map this full journey. But the goal is not just to collect papers or products. It is to understand how every piece fits together, where the bottlenecks are, and what decisions determine whether humanoid robotics succeeds as an industry.

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

TBD.
