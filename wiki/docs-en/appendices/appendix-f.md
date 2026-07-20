# Appendix F Knowledge Graph Query Examples

This appendix introduces how to search and browse the knowledge graph on this site (kg.rounds-tech.com), and provides query paths for common questions.

## F.1 Site Structure Overview

| Entry | Address | Content |
|---|---|---|
| Homepage | `/` | Domain navigation, type navigation, featured entities |
| Search | `/search/` | Full-text search (name, abstract, body, arXiv ID) |
| Graph | `/graph/` | Full relational network and community clustering visualization |
| Wiki | `/wiki/` | 30-chapter monograph + appendices |
| Entity Card | `/entry/<entity ID>/` | Summary, body, relations, and sources of a single entity |
| Type List | `/types/<type>/` | All entities of a given type |

## F.2 Search Tips

**Keyword search**: Enter Chinese or English in `/search/`, for example:

- `宇树` or `Unitree` — find companies, products, and related papers
- `2304.13705` — directly locate a paper using its arXiv ID (e.g., ACT)
- `全身控制` — match methods, concepts, and paper sections

**Filter by type**: Click the type tag at the top of the search results page, or use URL parameters:

```
/search/?type=paper            only papers
/search/?type=company          only companies
```

**Filter by domain**: Use the `domain` parameter (the domain cards on the homepage link here):

```
/search/?domain=07_ai_models_algorithms     AI Models and Algorithms
/search/?domain=04_actuators                Actuators
/search/?domain=11_applications_markets     Applications and Markets
```

Parameters can be combined: `/search/?domain=09_simulation_digital&type=benchmark` (benchmarks in the simulation domain).

## F.3 Graph Page Usage

- **Full graph mode**: Displays the entity network colored by community (cluster); supports zooming and dragging.
- **Single entity subgraph**: View the one-hop neighbors of any entity on its card page under "Relation Subgraph"; the search box in the upper right corner of the graph page can jump to a specified entity.
- **Relation types**: Edge labels are localized, e.g., `is_based_on` (based on), `evaluates_on` (evaluated on), `uses_dataset` (uses dataset).

## F.4 Common Question Query Paths

**"What is the principle and source of a certain method?"**
Search for the method name → enter the entity card → view "Core Content" and "References"; under "Outgoing Relations" of the card, `has_prerequisite` lists prerequisite theories.

**"Which works use a certain benchmark/dataset?"**
Enter the benchmark entity card → under "Incoming Relations", `evaluates_on` (which methods are evaluated on it) and `uses_dataset` (which works use the data).

**"What are the products and supply chain of a certain company?"**
Enter the company card → view `manufacturer_of` (manufactured products), `supplies`/`sources_from` (supply and procurement) relations; for a full supply chain overview, see also Wiki Chapter 7 and Appendix D.

**"A systematic review of a certain topic in humanoid robots?"**
First, check the corresponding Wiki chapter (table of contents at `/wiki/`); entities cited within the chapter have card pages for further exploration.

## F.5 Entity ID Naming Convention

Entity IDs follow the format `ent_<type>_<name>[_year]`, for example:

- `ent_paper_action_chunking_transformer_2023` — paper
- `ent_method_whole_body_control` — method
- `ent_company_unitree_robotics_2024` — company
- `ent_standard_iso_13482_personal_care_robot_2014` — standard

Relation IDs follow the format `rel_<source entity ID>_<relation type>_<target entity ID>`.

## F.6 Programmatic Access

This site is a static site; graph data is publicly available as JSON:

```
/data/search-index.json   search index (includes abstracts, domains, type tags)
/data/relations.json      full nodes and edges
/data/clusters.json       community clustering results
/data/subgraphs/<entity ID>.json   one-hop subgraph of a single entity
```

These can be directly fetched via `fetch` for secondary development; source data (YAML/Markdown) is hosted on the GitHub repository `YansongW/awesome-humanoid-robot`.
