# TÜV SÜD

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 南德意志集团 |
| **English Name** | TÜV SÜD |
| **Headquarters** | Munich, Germany |
| **Founded** | 1866 |
| **Website** | [https://www.tuvsud.com](https://www.tuvsud.com) |
| **Supply Chain Role** | Robot testing, safety certification, CE marking, functional safety assessment |
| **Enterprise Type** | Third-party testing and certification body (TIC), listed company |
| **Parent Company/Group** | TÜV SÜD AG |
| **Data Source** | TÜV SÜD official website, robot certification service page |

## Company Profile

TÜV SÜD is one of the world's leading third-party testing, inspection, and certification bodies, with a long history in industrial machinery, automotive, electrical/electronic, and medical equipment. Its robot safety certification services cover industrial robots, collaborative robots, service robots, and humanoid robots, helping enterprises meet EU Machinery Directive, CE marking, functional safety (ISO 13849 / IEC 61508), and market access requirements.

TÜV SÜD operates multiple testing laboratories globally, offering one-stop compliance services including risk assessment, type testing, technical documentation review, on-site audits, and ongoing surveillance. It is a key partner for bringing robot products into European and global high-end markets.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Robot Safety Certification | CE marking, Machinery Directive compliance | [TÜV SÜD Robot Safety Certification](../products/product_tuv_sud_robot_certification.md) | Industrial robots, collaborative robots, humanoid robots |
| Functional Safety Assessment | SIL/PL assessment and verification | ISO 13849 / IEC 61508 services | Robot control systems, safety components |
| Cybersecurity and Reliability | IoT/robot network risk assessment | IEC 62443 related services | Connected robots, service robots |

## Representative Product

### TÜV SÜD Robot Safety Certification Service

> TÜV SÜD Robot Certification: Please visit [official materials](https://www.tuvsud.com) for details.

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Service Type | Third-party safety certification, testing, auditing | TÜV SÜD official website |
| Applicable Regulations | EU Machinery Directive, CE marking, UKCA, functional safety | Public information |
| Applicable Standards | ISO 10218, ISO/TS 15066, ISO 13482, ISO 13849, IEC 61508 | TÜV SÜD |
| Testing Content | Risk assessment, type testing, electromagnetic compatibility, technical documentation review | Public information |
| Service Cycle | Not disclosed | Project-based |
| Certification Mark | TÜV SÜD mark, CE conformity | TÜV SÜD |
| Price | Not disclosed | Commercial quotation |

**Technical Highlights**: Global testing network, cross-disciplinary safety experts, covering the full chain of mechanical/electrical/software/cybersecurity, supporting compliance closure from R&D to mass production.

**Application Scenarios**: Export of industrial robots to the EU, CE certification for collaborative robots, market access for service robots, safety assessment and type testing for humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Standard texts (ISO/IEC), testing equipment, laboratory space, certification qualifications, safety experts
- **Downstream Customers/Application Scenarios**: Robot OEMs, component suppliers, system integrators, export traders, regulatory bodies
- **Main Competitors/Benchmarks**: SGS, UL Solutions, Intertek, DEKRA, Bureau Veritas

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_tuv_sud`
- Product Entity: `ent_product_tuv_sud_robot_certification`
- Component Entity: `ent_component_tuv_sud_robot_certification_core`
- Key Relationships:
  - `ent_company_tuv_sud` -- `manufactures` --> `ent_product_tuv_sud_robot_certification`
  - `ent_company_tuv_sud` -- `manufactures` --> `ent_component_tuv_sud_robot_certification_core`
  - `ent_product_tuv_sud_robot_certification` -- `uses` --> `ent_component_tuv_sud_robot_certification_core`

## References

1. [TÜV SÜD Official Website](https://www.tuvsud.com)
2. [TÜV SÜD Product Certification Services](https://www.tuvsud.com/en/services/product-certification)
3. [Appendix D Enterprise Directory](../index-companies.md)
4. Public industry reports and market materials
5. Data update note: 2026-07-01
