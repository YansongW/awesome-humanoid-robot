# UL Solutions (Underwriters Laboratories)

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | UL Solutions (Underwriters Laboratories) |
| **English Name** | UL Solutions LLC |
| **Headquarters** | Northbrook, Illinois, USA |
| **Founded** | 1894 |
| **Website** | [https://www.ul.com](https://www.ul.com) |
| **Supply Chain Role** | Robot safety standards, safety certification, North American market access |
| **Company Type** | Third-party safety certification body (NRTL), publicly traded company |
| **Parent Company/Group** | UL Solutions LLC (NYSE: UL) |
| **Data Source** | UL website, UL 1740 standard page, robot safety certification service page |

## Company Overview

UL Solutions is a globally renowned independent safety science company, and its UL mark holds high credibility in the North American market. The company participates in the development and publication of UL 1740, the "Standard for Safety for Industrial Robots," providing safety assessment, testing, certification, and ongoing surveillance services for industrial robots, collaborative robots, and humanoid robots.

UL Solutions holds a significant position within the US OSHA Nationally Recognized Testing Laboratory (NRTL) system. Its certification results are accepted by the United States, Canada, and numerous countries in Latin America and the Asia-Pacific region, serving as a key compliance pathway for robot products entering the North American market.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| Robot Safety Standards | North American industrial robot safety requirements | [UL 1740 Standard for Safety for Industrial Robots](../products/product_ul_solutions_ul_1740.md) | Industrial robots, collaborative robots, humanoid robots |
| Safety Certification Services | NRTL safety certification | UL Mark certification services | Electrical/electronic, robotics, industrial equipment |
| Functional Safety & Cybersecurity | Control system and networked safety assessment | UL Functional Safety services, IEC 62443 services | Robot controllers, IoT devices |

## Representative Product

### UL 1740 Standard for Safety for Industrial Robots

> UL 1740: Please visit [official website](https://www.ul.com) for details.

| Specification Item | Value | Remarks/Source |
|---|---|---|
| Standard Number | UL 1740 | UL Solutions |
| Standard Name | Standard for Safety for Industrial Robots | UL Standards Catalog |
| Scope | Industrial robots, robot systems, collaborative applications | UL 1740 |
| Publication Status | Current / Under continuous maintenance | UL Standards Catalog |
| Corresponding Standards | ANSI/RIA R15.06, ISO 10218 | Public information |
| Certification Attribute | Can serve as basis for North American market access and insurance | UL Solutions |
| Price | Not disclosed | UL Standards Store |

**Technical Highlights**: A highly recognized robot safety standard in the North American market, emphasizing risk assessment, safety functions, electrical and mechanical guarding, harmonized with ANSI/RIA R15.06.

**Application Scenarios**: North American sales of industrial robots, automotive/electronics manufacturing lines, collaborative robot work cells, compliance for humanoid robots in industrial settings.

## Supply Chain Position

- **Upstream Key Components/Materials**: ANSI/RIA standard inputs, test equipment, NRTL qualifications, safety engineers, accident data
- **Downstream Customers/Application Scenarios**: North American robot OEMs, system integrators, importers, insurance companies, regulatory bodies
- **Main Competitors/Peers**: TÜV SÜD, SGS, Intertek, CSA Group, ETL (Intertek)

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_ul_solutions`
- Product Entity: `ent_product_ul_solutions_ul_1740`
- Component Entity: `ent_component_ul_solutions_ul_1740_core`
- Key Relationships:
  - `ent_company_ul_solutions` -- `manufactures` --> `ent_product_ul_solutions_ul_1740`
  - `ent_company_ul_solutions` -- `manufactures` --> `ent_component_ul_solutions_ul_1740_core`
  - `ent_product_ul_solutions_ul_1740` -- `uses` --> `ent_component_ul_solutions_ul_1740_core`

## References

1. [UL Solutions Official Website](https://www.ul.com)
2. [UL Product iQ](https://www.ul.com/piq)
3. [Appendix D Company Directory](../index-companies.md)
4. Public industry reports and market materials
5. Data update note: 2026-07-01
