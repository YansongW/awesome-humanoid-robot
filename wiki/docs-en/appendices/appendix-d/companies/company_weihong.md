---
id: ent_company_weihong
schema_version: 1
type: company
title: Weihong Electronic Technology
domain: 02_components
theoretical_depth: system
names:
  zh: 维宏股份
  en: Weihong Electronic Technology
status: active
sources:
  - id: src_weihong_official
    type: website
    title: Weihong Official Website
    url: https://www.weihong.com.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Weihong Electronic Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 维宏股份 |
| **English Name** | Weihong Electronic Technology |
| **Headquarters** | Shanghai, China |
| **Founded** | 2007 |
| **Official Website** | [https://www.weihong.com.cn](https://www.weihong.com.cn) |
| **Supply Chain Role** | Motion Controller / CNC System / Servo Drive |
| **Company Type** | Domestic brand, listed company (300508.SZ) |
| **Parent Company/Group** | None (independently listed) |
| **Data Source** | Weihong official website, product manuals, annual reports, WAIC 2026 coverage |

## Company Overview

Weihong Electronic Technology is a representative enterprise in China's motion control and CNC system field, specializing in control systems for engraving machines, cutting machines, laser processing, and CNC machine tools.

Centered on an open motion control platform, the company provides complete solutions ranging from control cards and all-in-one machines to servo drives, serving a large customer base in woodworking, advertising, metal processing, and 3C industries. Weihong's CNC systems are known for high cost-performance, ease of secondary development, and strong industry adaptability, and are gradually expanding into core control areas for industrial robots and humanoid robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| NK Series Motion Controllers | Multi-axis integrated controller | NK300BX / NK280 | Engraving, cutting, CNC |
| Engraving Machine Control Systems | Industry-specific CNC | NcStudio | Advertising, woodworking, molds |
| Servo Drives | Feed axis drive | Not disclosed | Machine tools, robots |

## Representative Products

### NK300BX Motion Controller

> NK300BX Motion Controller: Please visit [official materials](https://www.weihong.com.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Multi-axis integrated motion controller | Weihong official website |
| Controlled Axes | Up to 6 axes | Product manual |
| Simultaneous Axes | 3/4/5 axes (depending on configuration) | Product manual |
| Control Accuracy | 0.001 mm (reference) | Product manual |
| Communication Interface | Ethernet / USB | Product manual |
| Programming Language | G-code / Macro program | Product manual |
| Operating System | Embedded Linux / Windows | Product manual |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: High integration, user-friendly interface, support for multiple process packages, suitable for engraving, cutting, and small CNC equipment.

**Application Scenarios**: Woodworking engraving machines, advertising cutting machines, metal mold machines, 3C processing equipment.

### NcStudio Engraving Control System

> NcStudio Control System: Please visit [official materials](https://www.weihong.com.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | PC-based CNC software + control card | Weihong official website |
| Controlled Axes | 3–5 axes | Product manual |
| Interpolation Method | Linear / Circular / Spline | Product manual |
| Interface | PCI/PCIe/Ethernet | Product manual |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Wide industry adaptability, convenient secondary development, and a high market share control solution in the domestic engraving machine market.

**Application Scenarios**: Advertising engraving, woodworking carving, mold processing, jade carving.

## Supply Chain Position

- **Upstream Key Components/Materials**: Industrial computers, display panels, FPGA/DSP, PCBs, connectors, capacitors, resistors.
- **Downstream Customers/Application Scenarios**: Engraving/cutting machine manufacturers, machine tool factories, 3C processing, advertising equipment, woodworking machinery.
- **Main Competitors/Peers**: Beckhoff Automation, Googol Technology, Siemens, Fanuc, Mitsubishi.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_weihong`
- Product Entities: `ent_component_weihong_nk300bx`, `ent_component_weihong_ncstudio`
- Key Relationships:
  - `ent_company_weihong` -- `manufactures` --> `ent_component_weihong_nk300bx`
  - `ent_company_weihong` -- `manufactures` --> `ent_component_weihong_ncstudio`

## References

1. [Weihong Electronic Technology Official Website](https://www.weihong.com.cn)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. Weihong Electronic Technology Annual Reports and Product Manuals
