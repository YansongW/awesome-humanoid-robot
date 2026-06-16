# Project Charter: Awesome Humanoid Robot

> **Version**: Draft  
> **Status**: Private pre-v0.1.0  
> **Purpose**: Define what this project is, why it exists, how it is organized, and how it will be maintained.

---

## 1. Mission

To build the most comprehensive, structured, and verifiable knowledge base for answering the question:

> **How do we go from 0 to 1 to achieve humanoid robot mass production and industrial application?**

We believe that humanoid robotics is not merely an AI research problem. It is a systems problem that connects materials science, precision manufacturing, global supply chains, software engineering, and real-world deployment.

This means tracking every layer required to turn a humanoid robot from an idea into a mass-produced, deployable, economically viable product: raw materials, components, manufacturing processes, design engineering, software, AI, data infrastructure, assembly, testing, mass production, applications, markets, policy, and regulation.

We are not building a bibliography of algorithms. We are building a map of the entire journey.

---

## 2. Vision

A living, community-curated map that enables anyone to answer questions like:

- What raw materials and components are needed, where do they come from, and what do they cost?
- Which manufacturing processes and supply-chain decisions determine whether a design can scale?
- How do mechanical design, AI, software, and data infrastructure interact in a production system?
- What does it take to move from prototype to mass production?
- Which applications are economically viable today, and which require further technical or cost breakthroughs?
- What policy, safety, and regulatory frameworks enable or block deployment?
- Where are the bottlenecks, risks, and investment opportunities across the full journey?

---

## 3. Core Principles

### 3.1 Full-chain coverage

We do not reduce humanoid robotics to AI models. Every layer of the value chain — from mine to market — is in scope.

### 3.2 Verifiability

Every claim should be traceable to a source. Uncertain or unverified claims are explicitly flagged.

### 3.3 Structured organization

Flat lists are useful but insufficient. We organize knowledge as an **ontology** — a concept map with relationships, not just categories.

### 3.4 AI-assisted, human-verified

We use AI to accelerate collection, summarization, and synthesis. But public-facing claims are reviewed by humans before release.

### 3.5 Openness after v0.1.0

The project will be open-sourced at v0.1.0 to enable community co-creation. Before that, it is private to allow the core team to establish a solid foundation.

---

## 4. Scope Boundaries

### 4.1 In Scope

- Raw materials and critical minerals for robotics
- Component supply chains (actuators, sensors, batteries, compute, structural parts)
- Manufacturing processes and quality control
- Assembly, integration, and testing workflows
- Mass production, factory design, and unit economics
- Humanoid morphology, kinematics, and mechanical design
- AI models: VLAs, world models, locomotion/manipulation policies, planning, sim-to-real
- Software stacks: ROS 2, real-time systems, simulation, digital twins
- Datasets, benchmarks, evaluation protocols
- Companies, startups, research labs, and ecosystems
- Applications and market analysis
- Regulations, standards, safety, and ethics

### 4.2 Out of Scope (For Now)

- Non-humanoid robots (e.g., industrial arms, drones, quadrupeds) except where directly relevant to humanoid supply chains
- General AI research not applied to robotics
- Science fiction or speculative long-term predictions without grounded analysis
- Investment advice

---

## 5. Industry-Chain Ontology

The project is organized around the following ten domains. Each domain has its own ontology document in [`docs/ontology/`](ontology/).

```
Upstream
├── 01 Raw Materials & Critical Resources
├── 02 Components & Subsystems
└── 03 Manufacturing Processes

Midstream
├── 04 Assembly, Integration & Testing
├── 05 Mass Production & Scaling
└── 06 Design & Engineering

Intelligence Layer
├── 07 AI Models & Algorithms
├── 08 Software & Middleware
└── 09 Data & Datasets

Validation & Deployment
├── 10 Evaluation & Benchmarks
├── 11 Applications & Markets
└── 12 Policy, Regulation & Ethics
```

The ontology is not a taxonomy of equal categories. It is a **value-chain map**: changes upstream (e.g., rare-earth prices) cascade downstream (e.g., actuator costs, robot BOM, market pricing).

---

## 6. AI4Sci Workflow

### 6.1 Inputs

- Academic papers (arXiv, conferences, journals)
- Company press releases, investor presentations, and teardowns
- Patent filings
- Industry reports and supply-chain analysis
- Government policy documents and standards
- Technical blogs and interviews

### 6.2 Extraction Template

For every entry, we record:

| Field | Description |
|-------|-------------|
| **Name** | Company, paper, component, or concept |
| **Domain** | Position in the industry-chain ontology |
| **Source** | Primary URL or citation |
| **Status** | Verified / Partially verified / Unverified / Speculative |
| **Summary** | One-paragraph description |
| **Relevance** | Why it matters for humanoid robotics |
| **Cross-links** | Related entries in other domains |
| **Last reviewed** | Date of last human or AI review |

### 6.3 Verification Levels

| Level | Meaning |
|-------|---------|
| ✅ Verified | Claim is supported by a primary source and has been reviewed |
| ⚠️ Partially verified | Supported by secondary sources or plausible inference |
| ❓ Unverified | Mentioned in sources but not independently confirmed |
| 🔮 Speculative | Forward-looking or analytic claim, clearly marked as such |

---

## 7. Governance & Release Plan

### 7.1 Pre-v0.1.0 (Private)

- Core team curates ontology and initial content.
- AI assists with literature scanning and summarization.
- All entries are internally reviewed before v0.1.0.

### 7.2 v0.1.0 (Public)

- Repository becomes public.
- Contribution guidelines published.
- Initial ontology and at least 100 curated entries across all domains.

### 7.3 Post-v0.1.0

- Community contributions via pull requests.
- Quarterly release cycles with changelog.
- Domain maintainers for each ontology branch.

---

## 8. Success Metrics

- Ontology covers all ten domains with explicit relationships.
- At least one verified entry per domain at v0.1.0.
- Every public-facing claim is traceable to a source.
- Active community contributions post-v0.1.0.

---

## 9. Open Questions

1. Should we include detailed company financials and funding data?
2. How should we handle conflicting supply-chain claims (e.g., multiple sources for the same component)?
3. Should we build interactive visualizations of the ontology?
4. What license best supports both open access and attribution?
