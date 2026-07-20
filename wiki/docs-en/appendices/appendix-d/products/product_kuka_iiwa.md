# KUKA LBR iiwa Collaborative Robot

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [KUKA Robotics](../companies/company_kuka.md) |
| **Product Category** | 7-axis collaborative robot |
| **Release Date** | 2013 |
| **Status** | Released/Commercial |
| **Official Website/Source** | [https://www.kuka.com](https://www.kuka.com) |

## Product Overview

The LBR iiwa is one of the world's first commercially available 7-axis force-controlled collaborative robots. Each joint integrates a torque sensor, enabling rapid force reduction upon contact with humans or workpieces, making it suitable for fence-free collaborative scenarios. Its open Java interface and iiQKA operating system support rapid deployment.

## Product Image

> LBR iiwa: Please visit [official materials](https://www.kuka.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of axes | 7 | KUKA official website |
| Maximum payload | 14 kg (iiwa 14) / 7 kg (iiwa 7) | KUKA official website |
| Maximum working radius | 820 mm / 1260 mm | KUKA official website |
| Repeatability | ± 0.1 mm | KUKA official website |
| Mechanical unit weight | Not disclosed | KUKA official website |
| Protection rating | IP54 | KUKA official website |
| Mounting orientation | Floor / Ceiling / Wall | KUKA official website |
| Price | Not disclosed | Inquire for pricing |

## Supply Chain Position

- **Manufacturer**: [KUKA Robotics](../companies/company_kuka.md)
- **Core Components/Technology Source**: Self-developed controller and software; externally purchased servo motors, reducers, torque sensors, structural parts, and cables.
- **Downstream Applications/Customers**: Automotive OEMs, electronics manufacturers, logistics and warehousing, medical surgical equipment, automation integrators.

## Knowledge Graph Nodes and Relationships

- Product entity: `ent_product_kuka_iiwa`
- Manufacturer entity: `ent_company_kuka`
- Key relationships:
  - `rel_ent_company_kuka_manufactures_ent_product_kuka_iiwa` (`ent_company_kuka` → `manufactures` → `ent_product_kuka_iiwa`)

## Application Scenarios

- **Precision assembly, screw tightening, polishing and grinding, flexible assembly and testing of humanoid robot components.**
- **Commercial services**: Used for guided tours, reception, exhibitions, and brand interaction.
- **Industrial manufacturing**: Performs tasks such as handling, assembly, and inspection on flexible production lines.
- **Scientific research and education**: Serves as a hardware platform for robot control, AI training, and embodied intelligence research.

## Expansion and Ecosystem

- The manufacturer provides official SDK, simulation tools, and after-sales training; specific details must be confirmed through official channels.
- Can interface with mainstream MES/WMS/PLC systems, but interface protocols must be based on official documentation.
- Scenario-specific validation and compatibility testing are recommended before deployment.

## Competitive Comparison

| Comparison Item | This Product | Main Competitors |
|-----------------|--------------|------------------|
| Positioning | Not disclosed | Similar products depend on specific scenarios |
| Core Advantage | Built-in joint torque sensors enable compliance control and human-robot safety collaboration; open Java interface and iiQKA operating system support rapid deployment. | Not disclosed |
| Price | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

- It is recommended to confirm the latest software version, SDK support, and after-sales training through official channels.
- Research and education users should prioritize evaluating secondary development interfaces, simulation platform compatibility, and community activity.
- Industrial users should verify load, precision, protection rating, and integration interfaces based on specific processes.

## References

1. [LBR iiwa Product Page](https://www.kuka.com/en-us/products/robotics-systems/industrial-robots/lbr-iiwa)
2. [KUKA Robotics Official Website](https://www.kuka.com)
3. [Public Materials and Industry Reports](https://www.kuka.com)
