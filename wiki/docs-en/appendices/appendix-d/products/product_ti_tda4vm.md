# TI TDA4VM Jacinto Processor

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Texas Instruments](../companies/company_texas_instruments.md) |
| **Product Category** | ADAS / Industrial Edge AI SoC / Functional Safety Processor |
| **Release Date** | Released in 2020, mass production in 2021 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [TI TDA4VM Product Page](https://www.ti.com/product/TDA4VM) |

## Product Overview

The TI TDA4VM is a heterogeneous SoC based on the Jacinto 7 architecture, targeting ADAS and industrial edge AI. The chip integrates an 8 TOPS INT8 Matrix Multiply Accelerator, C7x vector DSP, dual-core Cortex-A72 and six-core real-time Cortex-R5F, along with ISP, vision accelerator, 8-port Gigabit Ethernet switch, and PCIe hub. Its ASIL-D functional safety support makes it an ideal choice for high-reliability robotics, autonomous driving perception, and industrial vision.

## Product Image

> TI TDA4VM Jacinto Processor: Please visit the [official page](https://www.ti.com/product/TDA4VM) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Process Node | 16 nm FinFET (publicly reported) | TI public information |
| CPU | Dual-core 64-bit Arm Cortex-A72 @ up to 2.0 GHz + six-core Cortex-R5F @ 1.0 GHz | TI public information |
| AI Accelerator | C7x DSP + Matrix Multiply Accelerator (MMA) | TI public information |
| AI Compute | Up to 8 TOPS INT8 (MMA) | TI public information |
| DSP | 2× C7x + 2× C66x | TI public information |
| GPU | PowerVR Rogue 8XE GE8430 (approx. 100 GFLOPS) | TI public information |
| ISP/Vision | Integrated 7th-gen ISP, VPAC, DMPAC | TI public information |
| Memory | Supports LPDDR4 | TI public information |
| Interfaces | PCIe hub, 8-port GbE switch, CSI-2, CAN-FD, USB 3.1, MCASP | TI public information |
| Power Consumption | Typical approx. 5–20 W (depending on configuration) | TI public information |
| Safety | ASIL-D / SIL-3 target functional safety | TI public information |
| Price | SK-TDA4VM development kit approx. 199 USD | TI public information |

## Supply Chain Position

- **Manufacturer**: [Texas Instruments](../companies/company_texas_instruments.md)
- **Core Components/Technology Sources**: TI self-developed C7x/MMA/ISP, ARM CPU/GPU IP, 16 nm foundry, LPDDR4, PMIC, carrier board
- **Downstream Applications/Customers**: Automotive Tier1/OEM, industrial AMR/AGV manufacturers, machine vision integrators, robot OEMs

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_ti_tda4vm`
- Component Entity: `ent_component_ti_tda4vm_soc`
- Manufacturer Entity: `ent_company_texas_instruments`
- Key Relationships:
  - `rel_ent_company_texas_instruments_manufactures_ent_product_ti_tda4vm` (`ent_company_texas_instruments` → `manufactures` --> `ent_product_ti_tda4vm`)
  - `rel_ent_company_texas_instruments_manufactures_ent_component_ti_tda4vm_soc` (`ent_company_texas_instruments` → `manufactures` --> `ent_component_ti_tda4vm_soc`)
  - `ent_product_ti_tda4vm` -- `uses` --> `ent_component_ti_tda4vm_soc`

## Application Scenarios

- **Industrial AMR/AGV**: Multi-sensor fusion, safety certification, real-time path planning and obstacle avoidance
- **Machine Vision Inspection**: ISP + MMA for high-speed defect detection and object recognition
- **ADAS Perception ECU**: Front-view/surround-view, radar/LiDAR fusion, supports ASIL-D

## Competitive Comparison

| Comparison Item | TI TDA4VM | NXP S32G / i.MX 8M Plus | NVIDIA Jetson Orin NX |
|---|---|---|---|
| AI Compute | 8 TOPS | 2.3 TOPS / S32G no NPU | Up to 100 TOPS |
| Functional Safety | ASIL-D target | ASIL-B/D depending on version | Industrial grade |
| CPU | Dual-core A72 + six-core R5F | Quad-core A53 + M7 | Eight-core / twelve-core ARM |

## Selection and Deployment Recommendations

Use the TI Processor SDK (Linux/RTOS) to evaluate MMA and C7x performance; confirm functional safety level requirements; choose appropriate thermal and carrier board designs for industrial deployment.

## Related Entries

- [Manufacturer: Texas Instruments](../companies/company_texas_instruments.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [TI TDA4VM Product Page](https://www.ti.com/product/TDA4VM)
2. [TI Jacinto 7 Page](https://www.ti.com/processors/automotive-processors/jacino-7-family.html)
3. [SK-TDA4VM Development Kit](https://www.ti.com/tool/SK-TDA4VM)
