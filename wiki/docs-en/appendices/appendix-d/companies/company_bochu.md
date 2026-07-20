---
id: ent_company_bochu
schema_version: 1
type: company
title: Bochu Electronic Technology
domain: 02_components
theoretical_depth: system
names:
  zh: 柏楚电子
  en: Bochu Electronic Technology
status: active
sources:
  - id: src_bochu_official
    type: website
    title: Bochu Electronic Official Website
    url: https://www.bochu.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Bochu Electronic Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 柏楚电子 |
| **English Name** | Bochu Electronic Technology |
| **Headquarters** | Shanghai, China |
| **Founded** | 2007 |
| **Official Website** | [https://www.bochu.com](https://www.bochu.com) |
| **Supply Chain Segment** | Laser Cutting Control System / Motion Control / Industrial Software |
| **Enterprise Attribute** | Domestic Brand, Listed Company (688188.SH) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Source** | Bochu Official Website, Product Manuals, Annual Reports, WAIC 2026 Reports |

## Company Overview

Bochu Electronic Technology is a leading enterprise in China's laser cutting control systems and motion control software, holding a dominant position in the high-power laser cutting field.

The company's core product is the FSCUT series laser cutting control system, offering complete control solutions from low-power to ultra-large format, and expanding into intelligent welding, precision machining, and humanoid robot motion control. Bochu has deep expertise in motion control algorithms, trajectory planning, process databases, and bus technology, representing a key domestic alternative in high-end motion control software.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| FSCUT Laser Cutting System | Laser Cutting Control Platform | FSCUT4000 / FSCUT8000 | Laser Cutting |
| Intelligent Welding System | Robot Welding Control | Not disclosed | Automotive, Steel Structures |
| Motion Control Card | General Multi-Axis Control | Not disclosed | Automation |

## Representative Products

### FSCUT4000 Laser Cutting Control System

> FSCUT4000 Laser Cutting Control System: Please visit [Official Materials](https://www.bochu.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Laser Cutting CNC System | Bochu Official Website |
| Controlled Axes | 4 axes (X/Y/Z + auxiliary axis) | Product Manual |
| Interpolation Cycle | Not disclosed | - |
| Laser Power Compatibility | Low to Medium Power (Reference) | Product Manual |
| Communication Interface | EtherCAT / Pulse | Product Manual |
| Operating System | Embedded / Windows | Product Manual |
| Price | Not disclosed | Inquiry Required |

**Technical Highlights**: Rich process database, precise follow-up control, optimized cutting efficiency and cross-section quality.

**Application Scenarios**: Sheet metal processing, kitchenware, cabinets and enclosures, sign cutting, 3C metal parts processing.

### FSCUT8000 Bus Laser Cutting System

> FSCUT8000 Bus System: Please visit [Official Materials](https://www.bochu.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Bus-Type Laser Cutting Control System | Bochu Official Website |
| Controlled Axes | Multi-axis (depending on configuration) | Product Manual |
| Communication Protocol | EtherCAT | Product Manual |
| Laser Power Compatibility | High Power (Reference) | Product Manual |
| Price | Not disclosed | Inquiry Required |

**Technical Highlights**: Full bus architecture, high real-time performance, supports high-power large-format cutting and automated production line integration.

**Application Scenarios**: High-power laser cutting machines, ultra-high-power laser production lines, large-scale sheet metal processing.

## Supply Chain Position

- **Upstream Key Components/Materials**: Industrial computers, FPGA/DSP, PCBs, capacitors and resistors, connectors, display panels, encoder interface chips.
- **Downstream Customers/Application Scenarios**: Laser cutting machine manufacturers, sheet metal processing enterprises, automotive body-in-white, steel structures, humanoid robot control solution providers.
- **Main Competitors/Peers**: Weihong, PA, Siemens, Beckhoff, Googol Technology.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_bochu`
- Product Entities: `ent_component_bochu_fscut4000`, `ent_component_bochu_fscut8000`
- Key Relationships:
  - `ent_company_bochu` -- `manufactures` --> `ent_component_bochu_fscut4000`
  - `ent_company_bochu` -- `manufactures` --> `ent_component_bochu_fscut8000`

## References

1. [Bochu Electronic Official Website](https://www.bochu.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. Bochu Electronic Annual Reports and Product Manuals
