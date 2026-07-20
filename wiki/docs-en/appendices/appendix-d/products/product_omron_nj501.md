# OMRON NJ501 Sysmac Controller / NJ501

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Omron / OMRON](../companies/company_omron.md) |
| **Product Category** | Machine Automation Controller (MAC) |
| **Release Date** | Since 2011 (current main model) |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Omron Official Website](https://www.omron.com) |

## Product Overview

The NJ501 series is a machine automation controller on Omron's Sysmac platform, integrating the logic control of traditional PLCs with multi-axis motion control in the same hardware and software environment.

Through the EtherCAT bus, the NJ501 can synchronously control servos, inverters, I/O, and vision devices, and supports IEC 61131-3 programming and PLCopen motion control function blocks. It is suitable for high-end equipment requiring integrated logic and motion control.

## Product Image

> OMRON NJ501 Sysmac Controller: Please visit [Official Materials](https://www.omron.com) for details.

## Specification Table

| Specification Item | Value | Notes/Source |
|--------------------|-------|--------------|
| Product Type | Machine Automation Controller (MAC) | Official materials |
| Maximum Controlled Axes | 64 axes (EtherCAT) | Official materials |
| Maximum I/O Points | 2,560 points | Official materials (depends on model) |
| Program Capacity | Not disclosed | Not disclosed |
| Communication Interfaces | EtherCAT, EtherNet/IP, USB, OPC UA | Official materials |
| Programming Standard | IEC 61131-3 / PLCopen Motion Control Function Blocks | Official materials |
| Supply Voltage | 24 VDC | Official materials |
| Price | Not disclosed | Not disclosed |

## Supply Chain Position

- **Manufacturer**: [Omron / OMRON](../companies/company_omron.md)
- **Core Components/Technology Source**: Self-developed controller hardware and Sysmac Studio software; processors, communication chips, power devices, and memory are purchased externally.
- **Downstream Applications/Customers**: 3C manufacturing, automotive parts, packaging machinery, robot system integration, humanoid robot prototype control.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_omron_nj501`
- Manufacturer Entity: `ent_company_omron`
- Key Relationship:
  - `ent_company_omron` → `manufactures` → `ent_product_omron_nj501` (Relationship file: `rel_ent_company_omron_manufactures_ent_product_omron_nj501.md`)

## Application Scenarios

- **3C Electronics**: Motion control for pick-and-place, assembly, and inspection equipment.
- **Packaging Machinery**: Multi-axis synchronization, flying shear, and rotary shear control.
- **Robot Integration**: Joint control for industrial robots and humanoid robots.
- **Automotive Parts**: Assembly lines for engines and transmissions.

## Competitive Comparison

| Comparison Item | OMRON NJ501 Sysmac Controller | Mitsubishi iQ-R | Schneider M580 |
|----------------|-------------------------------|-----------------|----------------|
| Controlled Axes | Up to 64 axes | Not disclosed | Not disclosed |
| Programming Environment | Sysmac Studio | GX Works3 | EcoStruxure |
| Main Communication | EtherCAT / EtherNet/IP | CC-Link IE / Ethernet | Ethernet / Modbus TCP |
| Price | Not disclosed | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

For equipment requiring deep integration of logic and motion with up to several dozen axes, the NJ501 can be prioritized. When selecting a model, confirm the I/O scale and EtherCAT slave compatibility.

## References

1. [Omron Official Website](https://www.omron.com)
2. [OMRON NJ501 Sysmac Controller Product Page](https://www.omron.com.cn/products/family/3194/)
3. OMRON FA product catalog / Sysmac Studio documentation
