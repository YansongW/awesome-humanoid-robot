# American National Standards Institute / Robotics Industries Association / ANSI/RIA

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | American National Standards Institute / Robotics Industries Association |
| **English Name** | ANSI / Robotics Industries Association (RIA, now A3) |
| **Headquarters** | ANSI: Washington, D.C., USA; RIA/A3: Ann Arbor, Michigan, USA |
| **Founded** | ANSI 1918; RIA 1974 (merged into A3 in 2019) |
| **Official Website** | [https://www.ansi.org](https://www.ansi.org), [https://www.a3.org](https://www.a3.org) |
| **Supply Chain Role** | US robot safety standards, industry training, certification coordination |
| **Enterprise Type** | ANSI is a non-profit standards coordination body; RIA/A3 is an industry association |
| **Parent Company/Group** | None (ANSI independent; A3 is an industry association) |
| **Data Source** | ANSI official website, A3/RIA official website, R15.06 standard page |

## Company Profile

ANSI coordinates the US voluntary standards and conformity assessment system and represents the US in ISO/IEC standards activities. RIA (now the A3 Robotics Division) is the leading robotics industry association in the US, having long dominated the development and promotion of industrial robot safety standards.

ANSI/RIA R15.06 is the most important industrial robot safety standard in the US. It is harmonized with the international standard ISO 10218-1/-2 and is widely referenced by OSHA, NFPA, and various state regulations, serving as a key compliance basis for industrial robots entering the US market.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Robot Safety Standard | North American industrial robot safety requirements | [ANSI/RIA R15.06](../products/product_ansi_ria_r15_06.md) | Industrial robots, collaborative robots, integrated systems |
| Industry Certification & Training | CMRA Certified Robot Integrator, etc. | RIA certification courses | System integrators, end users |
| Market Research & Events | Industry statistics and exhibitions | A3 Business Forum | Robot industry chain |

## Representative Product

### ANSI/RIA R15.06 Industrial Robot Safety Standard

> ANSI/RIA R15.06: Please visit [official materials](https://www.ansi.org) for details.

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Standard Number | ANSI/RIA R15.06-2012 | ANSI/A3 |
| Corresponding International Standard | ISO 10218-1:2011 / ISO 10218-2:2011 | ANSI adoption note |
| Scope of Application | Industrial robots, robot systems, integrated applications | R15.06 |
| Publication Status | Current / Under continuous maintenance | ANSI/A3 |
| Technical Content | Safety design, installation, operation, maintenance, risk assessment | Public information |
| Price | Not disclosed | ANSI/A3 store |
| Certification Attribute | Widely referenced by US regulations and insurance systems | ANSI/A3 |

**Technical Highlights**: Harmonized with ISO 10218, covering robot bodies, robot systems, and integrated applications, emphasizing hazard identification, safety distances, and protective devices.

**Application Scenarios**: Automotive welding/painting robot production lines, collaborative robot workstations, palletizing/material handling system integration, humanoid robot industrial deployment.

## Supply Chain Position

- **Upstream Key Components/Materials**: ANSI technical committees, RIA/A3 member companies, ISO/TC 299 input, accident and test data
- **Downstream Customers/Application Scenarios**: North American robot OEMs, system integrators, end manufacturers, insurance companies, regulatory bodies
- **Main Competitors/Peers**: ISO/TC 299, IEEE SA, CSA Z434, EN ISO 10218

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_ansi_ria`
- Product Entity: `ent_product_ansi_ria_r15_06`
- Component Entity: `ent_component_ansi_ria_r15_06_core`
- Key Relationships:
  - `ent_company_ansi_ria` -- `manufactures` --> `ent_product_ansi_ria_r15_06`
  - `ent_company_ansi_ria` -- `manufactures` --> `ent_component_ansi_ria_r15_06_core`
  - `ent_product_ansi_ria_r15_06` -- `uses` --> `ent_component_ansi_ria_r15_06_core`

## References

1. [ANSI Official Website](https://www.ansi.org)
2. [A3 Official Website](https://www.a3.org)
3. [ANSI/RIA R15.06 Standard Page](https://webstore.ansi.org/standards/ria/ansiriar15062012)
4. [Appendix D Enterprise Directory](../index-companies.md)
5. Public industry reports and market materials
6. Data update note: 2026-07-01
