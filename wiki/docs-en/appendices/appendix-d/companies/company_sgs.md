# SGS S.A.

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 瑞士通用公证行 |
| **English Name** | SGS S.A. |
| **Headquarters** | Geneva, Switzerland |
| **Founded** | 1878 |
| **Website** | [https://www.sgs.com](https://www.sgs.com) |
| **Supply Chain Role** | Robotics testing, certification, verification, functional safety, global market access |
| **Enterprise Type** | Third-party testing and certification body (TIC), publicly listed company |
| **Parent/Group** | SGS S.A. (listed on SIX Swiss Exchange) |
| **Data Source** | SGS official website, robotics testing service page |

## Company Overview

SGS is one of the world's largest inspection, verification, testing, and certification organizations, covering industries such as agriculture, industry, consumer goods, and life sciences. In the robotics sector, SGS provides testing, certification, and functional safety assessment services ranging from raw materials and components to complete systems, supporting manufacturers in accessing global markets including the EU, North America, and Asia-Pacific.

SGS's robotics services cover electrical safety, mechanical safety, electromagnetic compatibility, wireless radio frequency, functional safety, software assessment, and cybersecurity, and can also provide factory audits, supply chain verification, and training. It serves as a key compliance and quality gatekeeper in the robotics industry chain.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Robotics Testing and Certification | Compliance for complete machines and components | [SGS Robotics Testing and Certification Services](../products/product_sgs_robotics_testing.md) | Industrial robots, collaborative robots, service robots, humanoid robots |
| Functional Safety Services | SIL/PL assessment | IEC 61508 / ISO 13849 services | Robot controllers, safety systems |
| Supply Chain and System Certification | ISO 9001/14001/45001 | Management system certification | Robot manufacturers and integrators |

## Representative Product

### SGS Robotics Testing and Certification Services

> SGS Robotics Testing and Certification: Please visit [official website](https://www.sgs.com) for details.

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Service Type | Testing, certification, verification, auditing | SGS official website |
| Applicable Regulations | CE, UKCA, FCC, IC, VCCI, CCC, etc. | Public information |
| Applicable Standards | ISO 10218, ISO/TS 15066, ISO 13482, IEC 61508, ISO 13849, IEC 60204 | SGS |
| Test Content | Electrical safety, mechanical safety, EMC, wireless, functional safety, environmental reliability | Public information |
| Service Cycle | Not disclosed | Project-based |
| Certification Marks | SGS mark, CE, CB, North American NRTL, etc. | SGS |
| Price | Not disclosed | Commercial quotation |

**Technical Highlights**: One of the world's largest TIC networks, cross-industry experience, providing full-chain compliance and quality services from R&D to mass production.

**Application Scenarios**: Consumer robot FCC/CE certification, industrial robot export, collaborative robot safety verification, humanoid robot complete machine compliance and supply chain auditing.

## Supply Chain Position

- **Upstream Key Components/Materials**: International standards, testing equipment, global laboratory network, certification qualifications, industry experts
- **Downstream Customers/Application Scenarios**: Robot OEMs, component suppliers, traders, retailers, regulatory bodies
- **Main Competitors/Peers**: TÜV SÜD, UL Solutions, Intertek, Bureau Veritas, DEKRA

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_sgs`
- Product Entity: `ent_product_sgs_robotics_testing`
- Component Entity: `ent_component_sgs_robotics_testing_core`
- Key Relationships:
  - `ent_company_sgs` -- `manufactures` --> `ent_product_sgs_robotics_testing`
  - `ent_company_sgs` -- `manufactures` --> `ent_component_sgs_robotics_testing_core`
  - `ent_product_sgs_robotics_testing` -- `uses` --> `ent_component_sgs_robotics_testing_core`

## References

1. [SGS Official Website](https://www.sgs.com)
2. [SGS Service Catalog](https://www.sgs.com)
3. [Appendix D Enterprise Directory](../index-companies.md)
4. Public industry reports and market materials
5. Data update note: 2026-07-01
