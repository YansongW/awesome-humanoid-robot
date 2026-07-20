# Aurora Optics / Aurora Optics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 奥普光电 |
| **English Name** | Aurora Optics / Changchun New Industries Optoelectronics Tech |
| **Headquarters** | Changchun, Jilin, China |
| **Founded** | 2001 |
| **Official Website** | [http://www.aoptek.com](http://www.aoptek.com) |
| **Supply Chain Role** | Optical encoders, photoelectric measurement and control equipment, optical materials |
| **Enterprise Type** | Listed company (Shenzhen Stock Exchange: 002338), Chinese Academy of Sciences background |
| **Parent Company/Group** | Changchun Institute of Optics, Fine Mechanics and Physics, Chinese Academy of Sciences (controlling shareholder) |
| **Data Source** | Aurora Optics announcements, subsidiary Yuheng Optics official website, public research reports |

## Company Profile

Aurora Optics is a listed platform controlled by the Changchun Institute of Optics, Fine Mechanics and Physics, Chinese Academy of Sciences. Its main businesses include photoelectric measurement and control instruments, new medical instruments, optical materials, optical encoders, and high-performance carbon fiber composite products.

The company's controlled subsidiary, Yuheng Optics, formerly known as Changchun First Optical Instrument Factory established in 1965, is the earliest professional manufacturer of photoelectric encoders in China. Yuheng Optics' leading products include metal grating angle encoders, absolute linear encoders, resolvers, gear encoders, and conventional encoders, widely used in CNC machine tools, servo motors, elevators, robots, aerospace, and military fields. Its technical level and market share rank first in the domestic industry.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Optical Encoders | Position/Angle Feedback | JFT / JZN / JKN Series | CNC machine tools, servo motors, robots |
| Absolute Linear Encoders | High-precision linear measurement | Not disclosed | High-end CNC, precision instruments |
| Resolvers/Gear Encoders | Rotary position sensing | Not disclosed | Elevators, new energy vehicles, servo |
| Photoelectric Measurement and Control Equipment | Aerospace/Military measurement and control | Photoelectric theodolite, radar antenna mount | National defense, aerospace |

## Representative Products

### Aurora Optics / Yuheng Optics JZN/JKN Series Optical Angle Encoders

> Aurora Optics JZN JKN: Please visit [official materials](http://www.aoptek.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | High-precision optical angle encoder | Public research report |
| Maximum Resolution | 29-bit absolute (publicly disclosed) | Investor interaction |
| Accuracy | Leading domestically, advanced internationally | Public research report |
| Features | Metal grating, high precision, high reliability | Public research report |
| Certifications | RoHS, CE, explosion-proof, military product experimental verification | Public research report |
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Breaks the long-standing market monopoly of foreign high-end encoders, with performance indicators reaching the advanced level of international counterparts, making it the preferred choice for batch domestic substitution.

**Application Scenarios**: High-end CNC machine tools, servo motor feedback, humanoid robot joints, aerospace, military measurement and control.

### Aurora Optics / Yuheng Optics JFT Series Encoders

> Aurora Optics JFT: Please visit [official materials](http://www.aoptek.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | High-end optical encoder series | Public research report |
| Industrialization Time | 2019 | Public research report |
| Market Positioning | Breaking foreign monopoly | Public research report |
| Application Areas | High-end CNC, servo, robots | Public research report |
| Performance Level | Advanced internationally, leading domestically | Public research report |
| Accuracy | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Promoted for domestic industrial application in 2019, filling the gap in domestic high-end encoders, with a price advantage of 20%–30% compared to international brands like Heidenhain.

**Application Scenarios**: High-end CNC machine tools, industrial robots, humanoid robot servo motors, elevator traction machines.

## Supply Chain Position

- **Upstream Key Components/Materials**: Optical glass/metal gratings, LED/laser light sources, photodetectors, precision bearings, electronic components
- **Downstream Customers/Application Scenarios**: CNC machine tools, servo systems, robots, elevators, new energy vehicles, aerospace, military
- **Main Competitors/Benchmarks**: Heidenhain, Renishaw, Tamagawa, Inovance Technology, Estun

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_aurora_optics`
- Product Entity: `ent_component_aurora_jzn_jkn`
- Product Entity: `ent_component_aurora_jft`
- Key Relationships:
  - `ent_company_aurora_optics` -- `manufactures` --> `ent_component_aurora_jzn_jkn`
  - `ent_company_aurora_optics` -- `manufactures` --> `ent_component_aurora_jft`
  - `ent_component_aurora_jzn_jkn` -- `used_in` --> `ent_product_humanoid_robot_joint`

## References

1. [Aurora Optics Official Website](http://www.aoptek.com)
2. [Financial World – Aurora Optics High-End Linear Encoders and Encoders Break Foreign Export Controls](https://www.163.com/dy/article/J75BDJMJ0519QIKK.html)
3. [Minsheng Securities – The Only Listed Platform of Changchun Institute of Optics, Encoder Leader Benefits from Domestic Substitution](https://pdf.dfcfw.com/pdf/H3_AP202306281591749134_1.pdf)
4. [Appendix D Product Catalog](../index-products.md)
