# International Organization for Standardization (ISO)

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 国际标准化组织 |
| **English Name** | International Organization for Standardization (ISO) |
| **Headquarters** | Geneva, Switzerland |
| **Founded** | 1947 |
| **Website** | [https://www.iso.org](https://www.iso.org) |
| **Supply Chain Role** | Robot standards, safety standards, testing specifications, conformity assessment |
| **Company Type** | Non-governmental international organization |
| **Parent Company/Group** | None |
| **Data Source** | ISO official website, ISO/TC 299 technical committee page |

## Company Profile

ISO is the world's largest non-governmental international standards organization, composed of over 170 national standards bodies. Its subcommittee ISO/TC 299 "Robotics" is responsible for developing safety, performance, and interoperability standards for industrial robots, service robots, collaborative robots, and personal care robots, making it one of the most important sources of standards for the global robotics industry.

ISO/TC 299 works in coordination with committees such as IEC/TC 44. Standards it publishes, including ISO 10218, ISO/TS 15066, and ISO 13482, are widely adopted by national regulations, certification bodies, and robot manufacturers, providing a benchmark for the safety design of humanoid robots, collaborative robots, and mobile service robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| ISO/TC 299 Robot Standards | Robot safety and performance specifications | [ISO/TC 299 Robot Standards Family](../products/product_iso_tc299_standards.md) | Industrial robots, collaborative robots, service robots, humanoid robots |
| Conformity Assessment and Guidelines | Certification, testing, and implementation guidance | ISO/IEC 17000 series, ISO/TR 20218 | Third-party testing, regulatory compliance, market access |
| Training and Publications | Standard interpretation and implementation support | ISO online store, technical reports | Manufacturers, integrators, regulatory bodies |

## Representative Products

### ISO/TC 299 Robot Standards Family

> ISO/TC 299: Please visit [official materials](https://www.iso.org) for details.

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Technical Committee | ISO/TC 299 (Robotics) | ISO official website |
| Core Standards | ISO 10218-1/-2, ISO/TS 15066, ISO 13482, ISO/TR 20218-1/-2 | ISO/TC 299 |
| Scope of Application | Industrial robots, collaborative robots, service robots, humanoid robots | ISO public materials |
| Publication Status | Continuously updated/Current | ISO official website |
| Standard Languages | English, French; Chinese as national adoption version | ISO |
| Member Countries | Approximately 30 participating countries + observer countries | ISO/TC 299 |
| Price | Not disclosed | ISO online store |

**Technical Highlights**: Global consensus development process, joint work with IEC/TC 44, covers the entire lifecycle safety of robots, can be directly transformed into national standards and the basis for CE/UKCA and other regulatory compliance.

**Application Scenarios**: Industrial robot safety design, collaborative robot collision threshold setting, personal care robot risk assessment, humanoid robot whole machine and system integration compliance.

## Supply Chain Position

- **Upstream Key Components/Materials**: Technical experts from member countries, industry alliances, research institutions, test data, regulatory requirements
- **Downstream Customers/Application Scenarios**: Robot OEMs, system integrators, certification bodies (TÜV SÜD, SGS, UL), regulatory agencies, end users
- **Main Competitors/Counterparts**: IEC/TC 44, IEEE SA, ANSI/RIA, CEN/CENELEC, national standards bodies

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_iso`
- Product Entity: `ent_product_iso_tc299_standards`
- Component Entity: `ent_component_iso_tc299_standards_core`
- Key Relationships:
  - `ent_company_iso` -- `manufactures` --> `ent_product_iso_tc299_standards`
  - `ent_company_iso` -- `manufactures` --> `ent_component_iso_tc299_standards_core`
  - `ent_product_iso_tc299_standards` -- `uses` --> `ent_component_iso_tc299_standards_core`

## References

1. [ISO Official Website](https://www.iso.org)
2. [ISO/TC 299 Robotics Technical Committee](https://www.iso.org/committee/5915511.html)
3. [Appendix D Company Directory](../index-companies.md)
4. [Appendix D Product Directory](../index-products.md)
5. Public industry reports and market materials
6. Data update note: 2026-07-01
