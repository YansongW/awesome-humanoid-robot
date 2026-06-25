# Productization Roadmap

> **Version**: Draft  
> **Status**: Private pre-v0.1.0  
> **Goal**: Move `awesome-humanoid-robot` from an ad-hoc research project to a reproducible, maintainable, community-ready knowledge-base product.

---

## 1. Why productize now?

The project has proven its core hypothesis: a graph-first, AI-assisted, human-verified knowledge base can cover the full 0→1 journey of humanoid robot mass production. To scale beyond a single researcher or small team, we need standardized inputs, outputs, interfaces, and automation.

Productization does not mean abandoning depth. It means making the depth reproducible.

---

## 2. Standardized interfaces

### 2.1 Command-line interface (CLI)

All common operations should be runnable through a stable, documented surface. The `Makefile` is the first layer; a dedicated CLI package can follow.

| Command | Purpose |
|---------|---------|
| `make setup` | One-command environment setup |
| `make validate` | Validate production entries/relationships |
| `make validate-all` | Validate production + staged workstream outputs |
| `make status` | Show pending reviews and workstream progress |
| `make review` | Interactive review of staged drafts |
| `make run-next` | Run the next unexecuted workstream |
| `make run-workstream W=...` | Run a specific workstream |
| `make orchestrate` | Run multiple workstreams in parallel |

Future: consolidate into a single `ahr` CLI entry point (e.g., `ahr validate`, `ahr workstream run-next`).

### 2.2 Workstream config schema

Workstream YAMLs are currently validated only by convention. We will add a JSON Schema for workstream configs so that:

- Every config has required fields (`name`, `description`, `seed_queries`, `target_entity_types`, etc.).
- Domain codes, entity types, and relationship patterns are checked automatically.
- New contributors can write configs with IDE autocomplete and validation.

### 2.3 Entry and relationship schemas

The existing `data/schema/v1/` schemas are stable. Next steps:

- Version bump procedure when extending the vocabulary.
- Automated migration scripts for existing entries when a new schema version lands.
- Schema linting in CI.

---

## 3. Automation

### 3.1 Continuous validation

A GitHub Actions workflow should run on every push and pull request:

1. Install dependencies.
2. Run `make validate-all`.
3. Report schema violations with file paths.
4. Block merges on validation failures.

### 3.2 Scheduled workstream execution

The `scripts/ai4sci_run_next_workstream.py` daemon provides a lightweight scheduler that runs the next unexecuted workstream at fixed intervals. This lets the knowledge base grow continuously without manual invocation.

Monitoring checklist:
- Hourly `TaskOutput` check of the daemon task.
- Daily review of `.staging/review/`.
- Weekly promotion of validated drafts to production.

### 3.3 Health dashboard

`scripts/ai4sci_status.py` is the seed of a dashboard. Future versions could expose:

- Coverage heatmap by ontology domain.
- Pending review queue.
- Workstream completion rate.
- Relationship graph integrity score.

---

## 4. Contributor experience

### 4.1 Contribution guidelines

At v0.1.0, publish:

- `CONTRIBUTING.md` with entry/relationship format examples.
- Issue templates for "missing entity", "incorrect claim", "new workstream".
- Pull-request checklist (validated, sources cited, multi-language summaries).

### 4.2 Templates

- `docs/ai4sci/entry_template.md` ✅ exists.
- Add `docs/ai4sci/workstream_template.yaml` for new workstreams.
- Add `docs/ai4sci/relationship_template.md` for manual relationships.

### 4.3 Local environment

- `Makefile` ✅ added.
- Optional: Docker image with venv, dependencies, and mounted volumes for reproducible runs.
- Optional: `devcontainer.json` for VS Code / GitHub Codespaces.

---

## 5. Data quality and governance

### 5.1 Verification workflow

- AI-extracted drafts default to `partially_verified` / `reviewed_by: ai`.
- Human review upgrades to `partially_verified` / `reviewed_by: human_and_ai`.
- High-confidence, source-checked claims can be marked `verified` / `reviewed_by: human`.

### 5.2 Dangling-edge detection

The cleanup script used to remove 41 dangling relationships should become a standard check:

- Run as part of `make validate` or as a separate `make graph-check`.
- Optionally auto-create placeholder target entries for frequently referenced proposed entities.

### 5.3 Source provenance

- Every factual claim must cite a source.
- Prefer primary sources (papers, standards, official reports).
- Flag speculative or analytic claims explicitly.

---

## 6. Release milestones

| Milestone | Goal |
|-----------|------|
| **v0.1.0** | Public repository, contribution guidelines, ≥100 validated entries, CI validation. |
| **v0.2.0** | Complete foundational workstreams, BOM/component map skeleton, company/supplier ecosystem. |
| **v0.3.0** | Manufacturing and mass-production coverage, cost/yield models, factory-design workstreams. |
| **v0.4.0** | Application/market analysis, policy/regulation coverage, interactive graph exports. |

---

## 7. Open questions

1. Should we expose the knowledge graph via a static site (e.g., MkDocs + graph visualizations) or keep it repository-native?
2. What license best balances open access and attribution?
3. How do we handle conflicting supply-chain claims from multiple sources?
4. Should we integrate with external databases (arXiv, Semantic Scholar, Crunchbase, UN Comtrade) via APIs?

---

## 8. Immediate next productization tasks

- [x] Add `Makefile` with standardized commands.
- [ ] Add JSON Schema for workstream configs and a validation command.
- [ ] Add GitHub Actions CI for `make validate-all`.
- [ ] Add `docs/ai4sci/workstream_template.yaml`.
- [ ] Add `make graph-check` for dangling-edge detection.
- [ ] Draft `CONTRIBUTING.md` and issue/PR templates.
