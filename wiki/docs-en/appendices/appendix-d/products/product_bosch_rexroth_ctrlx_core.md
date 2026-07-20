# Bosch Rexroth ctrlX CORE / ctrlX CORE

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Bosch Rexroth](../companies/company_bosch_rexroth.md) |
| **Product Category** | Industrial Automation Controller |
| **Release Date** | 2020 |
| **Status** | Mass Production / Commercial |
| **Official Website / Source** | [Bosch Rexroth Official Website](https://www.boschrexroth.com) |

## Product Overview

The ctrlX CORE is the core controller of the Bosch Rexroth ctrlX AUTOMATION platform. It uses a Linux-based real-time operating system and supports extending PLC, motion, robotics, and IoT functions via apps.

The controller has built-in multi-protocol communication capabilities and can serve as an edge computing node to interface with upper-layer cloud platforms. It is suitable for automation systems requiring high flexibility and software-defined functionality.

## Product Image

> Bosch Rexroth ctrlX CORE: Please visit [Official Documentation](https://www.boschrexroth.com) for details.

## Specification Table

| Specification | Value | Remarks / Source |
|---------------|-------|------------------|
| Product Type | Industrial Automation Controller / IPC | Official Documentation |
| Operating System | ctrlX OS (based on Linux real-time kernel) | Official Documentation |
| Processor | Not disclosed | Not disclosed |
| Number of Controlled Axes | Up to 99 axes | Official Documentation |
| Communication Interfaces | EtherCAT, Sercos III, PROFINET, OPC UA, MQTT | Official Documentation |
| Supply Voltage | 24 VDC | Official Documentation |
| Operating Temperature | 0 °C ~ 50 °C | Official Documentation |
| Price | Not disclosed | Not disclosed |

## Supply Chain Position

- **Manufacturer**: [Bosch Rexroth](../companies/company_bosch_rexroth.md)
- **Core Components / Technology Source**: Self-developed ctrlX OS and control software; processors, communication modules, power devices, and storage are externally sourced.
- **Downstream Applications / Customers**: Smart machine tools, packaging, logistics, mobile machinery, humanoid robot control platforms.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_bosch_rexroth_ctrlx_core`
- Manufacturer Entity: `ent_company_bosch_rexroth`
- Key Relationship:
  - `ent_company_bosch_rexroth` → `manufactures` → `ent_product_bosch_rexroth_ctrlx_core` (Relationship file: `rel_ent_company_bosch_rexroth_manufactures_ent_product_bosch_rexroth_ctrlx_core.md`)

## Application Scenarios

- **Smart Machine Tools**: Multi-axis coordination and process optimization.
- **Packaging Machinery**: Flying shear, rotary shear, and electronic cam.
- **Mobile Robots**: AGV/AMR motion control and scheduling.
- **Humanoid Robots**: As body controllers or joint drive gateways.

## Competitive Comparison

| Comparison Item | Bosch Rexroth ctrlX CORE | Siemens SIMATIC S7-1500 | Beckhoff CX2030 |
|-----------------|---------------------------|--------------------------|------------------|
| Operating System | Linux RT (ctrlX OS) | Real-time Windows / Linux | TwinCAT/BSD |
| Software Form | app-based | Traditional PLC project | TwinCAT runtime |
| Number of Controlled Axes | Up to 99 axes | Depends on model | Depends on model |
| Price | Not disclosed | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

Suitable for projects that aim for software-defined automation, rapid integration of third-party algorithms, and cloud-edge collaboration; the maturity of the app ecosystem and real-time requirements need to be evaluated.

## References

1. [Bosch Rexroth Official Website](https://www.boschrexroth.com)
2. [Bosch Rexroth ctrlX CORE Product Page](https://www.boschrexroth.com/en/us/products/product-groups/controls/ctrlx-automation/ctrlx-core)
3. Bosch Rexroth ctrlX AUTOMATION product pages
