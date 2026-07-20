# {{company_name_zh}} / {{company_name_en}}

> This entry belongs to [Appendix D Enterprise/Product Wiki](../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | {{company_name_zh}} |
| **English Name** | {{company_name_en}} |
| **Headquarters** | {{hq}} |
| **Founded** | {{founded}} |
| **Website** | `{{website}}` |
| **Supply Chain Segment** | {{tags}} |
| **Enterprise Attribute** | {{attributes}} |
| **Parent Company/Group** | {{parent}} |
| **Data Source** | {{sources}} |

## Company Profile

{{one_sentence_positioning}}

{{company_description}}

## Product Lines

| Product Line | Positioning | Representative Products | Application Fields |
|--------------|-------------|-------------------------|--------------------|
| {{product_line_1}} | {{positioning_1}} | {{representative_1}} | {{application_1}} |
| {{product_line_2}} | {{positioning_2}} | {{representative_2}} | {{application_2}} |

## Representative Products

### {{product_name_1}}

> Image: Please refer to official public materials.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | {{dimension_1}} | {{source_1}} |
| Weight | {{weight_1}} | {{source_1}} |
| Degrees of Freedom | {{dof_1}} | {{source_1}} |
| Payload/Torque | {{payload_1}} | {{source_1}} |
| Speed/RPM | {{speed_1}} | {{source_1}} |
| Endurance | {{endurance_1}} | {{source_1}} |
| Interface/Communication | {{interface_1}} | {{source_1}} |
| Price | {{price_1}} | {{source_1}} |

**Technical Highlights**: {{highlights_1}}

**Application Scenarios**: {{applications_1}}

### {{product_name_2}}

> Image: Please refer to official public materials.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | {{dimension_2}} | {{source_2}} |
| Weight | {{weight_2}} | {{source_2}} |
| Degrees of Freedom | {{dof_2}} | {{source_2}} |
| Payload/Torque | {{payload_2}} | {{source_2}} |
| Speed/RPM | {{speed_2}} | {{source_2}} |
| Endurance | {{endurance_2}} | {{source_2}} |
| Interface/Communication | {{interface_2}} | {{source_2}} |
| Price | {{price_2}} | {{source_2}} |

**Technical Highlights**: {{highlights_2}}

**Application Scenarios**: {{applications_2}}

## Supply Chain Position

- **Upstream Key Components/Materials**: {{upstream}}
- **Downstream Customers/Application Scenarios**: {{downstream}}
- **Main Competitors/Benchmarks**: {{competitors}}

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_{{company_id}}`
- Product Entities: `ent_product_{{product_id_1}}`, `ent_product_{{product_id_2}}`
- Key Relationships:
  - `ent_company_{{company_id}}` -- `manufactures` --> `ent_product_{{product_id_1}}`
  - `ent_product_{{product_id_1}}` -- `uses` --> `ent_component_xxx`
  - `ent_company_{{company_id}}` -- `supplies` --> `ent_company_xxx`

## References

1. Official Website: `{{website}}`
2. WAIC 2026 Exhibition Report: `{{waic_source}}`
3. Other Public Materials: `{{other_source}}`
