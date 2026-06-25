# Information Model: Awesome Humanoid Robot

> **Status**: Draft v0.1 — subject to review before content population  
> **Purpose**: Define the core data architecture that enables the project to represent the full humanoid robot industry chain, its entities, relationships, layers, and cross-domain dependencies in a structured, extensible way.
>
> 🌐 [English](information_model.md)

---

## 1. Design Principles

The information model is designed to be:

1. **Graph-first**: Entities are nodes. Relationships are directed edges. Both are first-class citizens.
2. **Domain-aware but not domain-bound**: Every entity belongs to one or more ontology domains, but can connect freely across domains.
3. **Layer-orthogonal**: Entities carry both a value-chain layer and a functional role, allowing AI/software/data nodes to exist inside manufacturing or application contexts.
4. **Versioned and extensible**: Schemas are versioned. New entity types, relationship types, and domains can be added through a controlled process.
5. **Human-readable and machine-readable**: Entries use YAML frontmatter for structured data and Markdown for narrative content.
6. **Multi-lingual by design**: Names, descriptions, and summaries are stored as language maps.
7. **Verifiable**: Every claim carries verification status, confidence, reviewer, and sources.

---

## 2. Core Concepts

### 2.1 Entity

An **entity** is any discrete object in the knowledge graph: a company, a material, a robot system, a paper, a market segment, a regulation, etc.

Each entity has:

- A stable `id`
- A `type` from the controlled entity-type vocabulary
- A `names` map (multi-language)
- A `summary` map (multi-language)
- One or more `domains`
- One or more `layers`
- One or more `functional_roles`
- `verification` metadata
- `sources`
- Optional `relationships` (outgoing edges)
- Optional Markdown body for long-form content

### 2.2 Relationship

A **relationship** is a directed edge between two entities. It has its own identity, type, and verification metadata.

Relationships are not inferred from links inside Markdown. They are explicitly declared so the graph can be queried, validated, and visualized.

### 2.3 Domain

A **domain** corresponds to one of the ontology branches (e.g., `00_foundations`, `01_raw_materials`, `02_components`, `07_ai_models`).

Entities can belong to multiple domains when they sit at boundaries. Foundational knowledge that underpins multiple engineering domains is assigned to `00_foundations`.

### 2.4 Layer

A **layer** is a position along the value chain:

| Layer | Code | Description |
|-------|------|-------------|
| Foundations | `foundations` | Foundational disciplines: mathematics, physics, chemistry, economics, computer science |
| Upstream | `upstream` | Raw materials, components, manufacturing processes |
| Midstream | `midstream` | Design, assembly, integration, testing, mass production |
| Intelligence | `intelligence` | AI models, software, middleware, data |
| Validation & Markets | `validation_markets` | Benchmarks, applications, markets, policy, regulation |

An entity can belong to multiple layers if it spans them.

### 2.5 Functional Role

A **functional role** describes what the entity does in the system, independent of where it sits in the value chain:

| Role | Description |
|------|-------------|
| `material` | Physical substance or raw input |
| `component` | Hardware subsystem or part |
| `process` | Manufacturing, assembly, testing, or operational process |
| `system` | Integrated product or robot platform |
| `tool_equipment` | Machine, instrument, or software tool used to build or operate |
| `facility` | Factory, lab, test site, or production line |
| `intelligence` | Algorithm, model, data, or software capability |
| `organization` | Company, institution, standards body, or consortium |
| `market` | Market segment, application scenario, or business model |
| `policy` | Regulation, standard, certification, or ethical framework |
| `knowledge` | Paper, patent, report, dataset, benchmark, or concept |

### 2.6 Theoretical Depth

In addition to the value-chain layer, every entity can be positioned along a **theoretical-depth axis** that runs from foundational disciplines up to concrete systems:

| Depth Level | Code | Description |
|-------------|------|-------------|
| Foundation | `foundation` | Basic disciplines: mathematics, physics, chemistry, economics, computer science |
| Principle / Theorem | `principle` | Physical laws, mathematical theorems, lemmas, axioms |
| Formalism | `formalism` | Mathematical formulations: optimization problems, equations, models |
| Method / Algorithm | `method` | Algorithms, techniques, design patterns |
| System / Implementation | `system` | Integrated hardware/software products and deployments |

An entity can span multiple depth levels. For example, a paper may instantiate a `method`, formalize it as a `formalism`, and rely on a `principle`.

---

## 3. Entity Types

Entity types are organized into four families. The list is versioned and can be extended.

### 3.1 Organization

| Type | Description |
|------|-------------|
| `oem` | Humanoid robot manufacturer / brand |
| `tier1_supplier` | Direct supplier to OEMs |
| `tier2_supplier` | Supplier to Tier-1 suppliers |
| `component_manufacturer` | Manufacturer of specific components |
| `material_supplier` | Supplier of raw or processed materials |
| `software_vendor` | Provider of software, platform, or middleware |
| `research_institution` | University lab, research center, or open-source community |
| `standards_body` | Organization that defines standards or certifications |
| `industry_consortium` | Multi-company or multi-stakeholder group |

### 3.2 Product / Artifact

| Type | Description |
|------|-------------|
| `robot_system` | Complete humanoid robot platform |
| `component` | Hardware component or subsystem |
| `material` | Physical material or substance |
| `software_platform` | Software framework, OS, simulator, or middleware |
| `tool_equipment` | Production or testing equipment |
| `facility` | Factory, production line, or test facility |

### 3.3 Knowledge

| Type | Description |
|------|-------------|
| `paper` | Academic paper or preprint |
| `patent` | Patent or patent application |
| `report` | Industry report, teardown, or market analysis |
| `dataset` | Curated dataset for training or evaluation |
| `benchmark` | Benchmark, test, or evaluation protocol |
| `standard` | Technical standard, safety standard, or certification |
| `technology` | Concept, method, or technology route |
| `concept` | High-level concept or problem framing |
| `method` | Algorithm, technique, or methodological approach |
| `formalism` | Mathematical formulation (e.g., QP problem, Lagrangian) |
| `equation` | A specific equation or identity |
| `operator` | Mathematical operator or transformation (e.g., gradient, Jacobian, softmax) |
| `variable` | Variable or unknown in a formalism/equation |
| `constant` | Physical constant or fixed hyperparameter |
| `algorithm` | Concrete algorithm or solver |
| `approximation` | Approximation scheme or simplifying assumption |
| `theorem` | Proven mathematical statement or lemma |
| `principle` | Physical, chemical, or engineering principle |
| `foundation` | Foundational discipline topic (math, physics, chemistry, etc.) |

### 3.4 Market / Policy

| Type | Description |
|------|-------------|
| `market_segment` | Segment of the humanoid robot market |
| `application_scenario` | Specific use case or deployment scenario |
| `business_model` | Business or pricing model |
| `regulation` | Law, regulation, or policy |
| `certification` | Certification or approval process |

---

## 4. Relationship Types

Relationship types are grouped by semantic category. All relationship types are directed.

### 4.1 Supply Chain

| Type | Meaning | Example |
|------|---------|---------|
| `supplies` | A supplies B | rare-earth supplier → motor manufacturer |
| `consumes` | A consumes B | motor manufacturer → rare-earth magnets |
| `produces` | A produces B | motor manufacturer → servo motor |
| `integrates` | A integrates B into a product | OEM → servo motor |
| `sources_from` | A sources inputs from B | OEM → Shenzhen ecosystem |
| `distributes` | A distributes B | distributor → robot system |

### 4.2 Technical Dependency

| Type | Meaning | Example |
|------|---------|---------|
| `enables` | A enables B | high-torque actuator → dynamic bipedal walking |
| `requires` | A requires B | VLA → edge GPU |
| `constrains` | A constrains B | battery energy density → operating time |
| `compensates_for` | A compensates for limitation B | algorithm → low sensor accuracy |
| `is_alternative_to` | A is an alternative to B | hydraulic actuator ↔ electric motor |

### 4.3 Hierarchy / Composition

| Type | Meaning | Example |
|------|---------|---------|
| `is_part_of` | A is part of B | motor → actuator module |
| `is_subsystem_of` | A is subsystem of B | actuator module → leg |
| `is_instance_of` | A is an instance of B | Tesla Optimus → humanoid robot |
| `is_prerequisite_for` | A is prerequisite for B | simulation environment → sim-to-real training |
| `is_version_of` | A is a version of B | Optimus Gen-2 → Optimus |

### 4.4 Market & Policy

| Type | Meaning | Example |
|------|---------|---------|
| `serves` | A serves market/use case B | humanoid robot → automotive manufacturing |
| `is_regulated_by` | A is regulated by B | humanoid robot → ISO safety standard |
| `drives_demand_for` | A drives demand for B | labor shortage → humanoid robot |
| `competes_with` | A competes with B | humanoid robot ↔ industrial robot |
| `is_substitute_for` | A can substitute for B | humanoid worker ↔ human worker |

### 4.5 Knowledge & Provenance

| Type | Meaning | Example |
|------|---------|---------|
| `cites` | A cites B | entry → source paper |
| `is_based_on` | A is based on B | product → research paper |
| `verified_by` | claim A is verified by source B | statement → annual report |
| `conflicts_with` | A conflicts with B | source A ↔ source B |
| `formalizes` | A formalizes B as a mathematical/algorithmic object | QP formulation formalizes WBC |
| `uses_theorem` | A uses theorem/principle B in its derivation or proof | stability proof uses Lyapunov theorem |
| `derived_from` | A is derived from B | KKT conditions derived from Lagrange multipliers |
| `instantiates` | A is a concrete instance/implementation of B | paper implements WBC method |
| `builds_on` | A builds on prior work B | later paper → earlier paper |
| `has_prerequisite` | A requires foundational knowledge B | convex optimization → linear algebra |
| `uses` | A uses B | equation uses operator |
| `includes` | A includes B as a component/sub-equation | QP formulation includes objective equation |
| `solves` | A solves B | active-set method solves QP |
| `estimates` | A estimates B | score matching estimates score function |
| `minimizes` | A minimizes B | gradient descent minimizes loss |
| `approximates` | A approximates B | Fick's laws approximate Nernst-Planck |
| `proposes` | A proposes B | paper proposes method/algorithm |
| `evaluates_on` | A evaluates on B | paper evaluates on benchmark |
| `extends` | A extends B | method extends prior work |

---

## 5. File Format

### 5.1 Entry File

Each entity is stored as a Markdown file with YAML frontmatter:

```text
research/companies/tesla_optimus.md
research/materials/neodymium_magnet.md
research/papers/predimem_2026.md
```

Format:

```yaml
---
$id: "ent_001"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "material"

names:
  en: "Neodymium-Iron-Boron Magnet"
  zh: "钕铁硼磁体"
  ko: "네오디뮴 철 붕자석"

summary:
  en: "A high-performance permanent magnet used in servo motors."
  zh: "用于伺服电机的高性能永磁体。"
  ko: "서보 모터에 사용되는 고성능 영구자석。"

domains:
  - "01_raw_materials"

layers:
  - "upstream"

functional_roles:
  - "material"

tags:
  - "rare_earth"
  - "magnet"
  - "motor"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-16"
  confidence: "high"
  notes: "Based on multiple motor teardown reports and supplier data."

sources:
  - id: "src_001"
    type: "report"
    title: "Electric Motor Market Analysis 2025"
    url: "https://example.com/report"
    date: "2025-11-10"
    accessed_at: "2026-06-16"

related_entities:
  - id: "ent_002"
    relationship: "consumed_by"
    description: "Used in high-performance servo motors."

---

# Neodymium-Iron-Boron Magnet

Long-form narrative content goes here...
```

### 5.3 Required First Section: 抽象（Abstraction / Intuition）

Every concrete entry file (especially `equation`, `formalism`, `theorem`, `principle`, `method`, `algorithm`, `operator`, and `concept`) must begin with a section titled:

```markdown
## 抽象
```

This section must:

1. **Use a real-life analogy** that a non-specialist can relate to (e.g., a revolving door for Butler-Volmer, a shopping-mall constraint for KKT, attention while reading for self-attention).
2. **Explain the intuition** in one or two paragraphs: what problem the entity solves, why the formula/concept is shaped the way it is, and what each symbol represents at a high level.
3. **Bridge to the formal definition** in the next section.

Example:

```markdown
## 抽象

> **生活实例**：想象你在一个商场里想找到离出口最近的位置，但被告知“不能走进商店内部”（不等式约束）且“必须站在过道正中线上”（等式约束）。KKT 条件就是一套判断标准：如果你站的位置最优，那么要么你不在边界上（约束不影响你），要么边界上的“推力”刚好把你顶在最优位置。
>
> **自然语言逻辑**：把带约束的优化问题写成拉格朗日函数 → 对原变量和乘子分别求导并令其为零 → 得到 KKT 条件 → 这些条件是局部最优的必要条件（在凸问题下也是充分条件）。

## 形式化定义

...
```

### 5.4 Relationship File

Relationships can be declared inline within entity files (via `related_entities`) or stored separately in:

```text
data/relationships/
```

Standalone relationship file format:

```yaml
---
$id: "rel_001"
$schema: "../../data/schema/v1/relationship_schema.json"
$version: 1

type: "supplies"

source:
  id: "ent_010"
  name:
    en: "Neo Materials Co."

target:
  id: "ent_011"
  name:
    en: "Servo Motor Manufacturer X"

domains:
  source_domain: "01_raw_materials"
  target_domain: "02_components"

description:
  en: "Neo Materials Co. supplies NdFeB magnets to Servo Motor Manufacturer X."
  zh: "..."
  ko: "..."

verification:
  status: "verified"
  reviewed_by: "human"
  reviewed_at: "2026-06-16"
  confidence: "medium"

sources:
  - id: "src_020"
    type: "annual_report"
    title: "Neo Materials Co. Annual Report 2025"
    url: "https://..."
    date: "2026-03-15"
---
```

---

## 6. Schema Versioning and Extension

### 6.1 Versioning

Schemas live under:

```
data/schema/v1/
├── entry_schema.json
└── relationship_schema.json
```

When a breaking change is needed, a new version directory is created (`v2/`) and migration rules are documented.

### 6.2 Adding New Entity Types

To add a new entity type:

1. Propose the type with a definition and example.
2. Assign it to a family (Organization, Product, Knowledge, Market/Policy).
3. Update `entry_schema.json` enum.
4. Document it in this file.

### 6.3 Adding New Relationship Types

To add a new relationship type:

1. Identify the semantic category.
2. Ensure it is directional and unambiguous.
3. Update `relationship_schema.json` enum.
4. Document it in this file.

### 6.4 Adding New Domains

Domains are part of the ontology and should not change lightly. To add a domain:

1. Justify why the existing twelve domains cannot accommodate it.
2. Propose a domain code, name, and position in the value chain.
3. Update ontology documents and schemas.

---

## 7. Validation and Quality Rules

1. Every entity must have at least one domain, one layer, and one functional role.
2. Every relationship must connect two existing entities.
3. Relationship type must be from the controlled vocabulary.
4. Every `verified` claim must have at least one primary source.
5. Multi-language fields must include at least English; Chinese and Korean are strongly encouraged.
6. IDs must be globally unique and stable.

---

## 8. Open Questions

1. Should we enforce that every `component` entity must have at least one `is_part_of` or `integrates` relationship?
2. Should we store derived relationships (e.g., inferred transitive supply-chain paths) or compute them on demand?
3. How do we represent time-varying properties (e.g., price, company funding, product version) in the graph?
4. Should we adopt a graph database (e.g., Neo4j) later, or stay with file-based YAML/Markdown?
