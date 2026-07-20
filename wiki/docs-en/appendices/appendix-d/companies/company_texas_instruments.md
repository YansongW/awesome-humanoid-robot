# Texas Instruments

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Texas Instruments |
| **English Name** | Texas Instruments |
| **Headquarters** | Dallas, Texas, USA |
| **Founded** | 1930 |
| **Website** | [https://www.ti.com](https://www.ti.com) |
| **Supply Chain Role** | Industrial MCU, Jacinto ADAS/Edge AI, Analog & Power Management |
| **Company Type** | Public (NASDAQ: TXN) |
| **Parent/Group** | None (Texas Instruments is the listed entity) |
| **Data Source** | TI official website, Jacinto product manuals, public press releases, industry research reports |

## Company Overview

Texas Instruments is one of the world's largest analog and embedded semiconductor companies, with products covering processors, MCUs, sensors, power management, and analog devices. Its Jacinto 7 series SoCs (e.g., TDA4VM) are specifically designed for ADAS and edge AI, integrating a deep learning accelerator (MMA), DSP, ISP, functional safety hardware, and rich industrial interfaces, widely used in automotive, industrial robotics, and machine vision.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Jacinto 7 / TDA4x | ADAS & Edge AI Processors | TDA4VM | Autonomous driving perception, Industrial AMR, Machine vision, Edge AI Box |
| Sitara / AM6x | Industrial-grade Arm Processors | AM68A / AM69A | Industrial gateways, Robot control, HMI, Real-time communication |

## Representative Products

### TI TDA4VM

> TI TDA4VM: Please visit the [official page](https://www.ti.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Process Node | 16 nm FinFET (public reports) | TI public info |
| CPU | Dual-core 64-bit Arm Cortex-A72 @ up to 2.0 GHz + Hexa-core Cortex-R5F @ 1.0 GHz | TI public info |
| AI Accelerator | C7x DSP + Matrix Multiply Accelerator (MMA) | TI public info |
| AI Compute | Up to 8 TOPS INT8 (MMA) | TI public info |
| DSP | 2× C7x + 2× C66x | TI public info |
| GPU | PowerVR Rogue 8XE GE8430 (~100 GFLOPS) | TI public info |
| ISP/Vision | Integrated 7th-gen ISP, VPAC, DMPAC | TI public info |
| Memory | Supports LPDDR4 | TI public info |
| Interfaces | PCIe hub, 8-port GbE switch, CSI-2, CAN-FD, USB 3.1, MCASP | TI public info |
| Power Consumption | Typical ~5–20 W (depending on configuration) | TI public info |
| Safety | ASIL-D / SIL-3 target functional safety | TI public info |
| Price | SK-TDA4VM development kit ~199 USD | TI public info |

**Technical Highlights**: Jacinto 7 heterogeneous architecture, 8 TOPS MMA, C7x vector DSP, integrated ISP & VPAC/DMPAC, ASIL-D functional safety, rich automotive/industrial interfaces.

**Application Scenarios**: **Industrial AMR/AGV**: Multi-sensor fusion, safety certification, real-time path planning and obstacle avoidance; **Machine Vision Inspection**: ISP + MMA for high-speed defect detection and object recognition; **ADAS Perception ECU**: Front/surround view, radar/LiDAR fusion, supporting ASIL-D.

### TI AM68A

> TI AM68A: Please visit the [official page](https://www.ti.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| CPU | Dual-core Cortex-A72 + Hexa-core Cortex-R5F | TI public info |
| AI Accelerator | MMA + C7x DSP | TI public info |
| AI Compute | Up to 8 TOPS | TI public info |
| Interfaces | PCIe, GbE, USB, CSI-2, CAN-FD | TI public info |
| Power Consumption | ~5–15 W | TI public info |
| Safety | Industrial-grade safety features | TI public info |
| Price | Not disclosed | TI public info |

**Technical Highlights**: A Jacinto 7 derivative platform for industrial and edge AI, balancing compute, power, and industrial interfaces.

**Application Scenarios**: Industrial gateways, Edge AI Box, Robot main controller, Smart retail.

## Supply Chain Position

- **Upstream Key Components/Materials**: TSMC/own fabs, ARM IP, proprietary C7x DSP/MMA, memory, PMIC, packaging & testing, PCB
- **Downstream Customers/Applications**: Automotive Tier1/OEM, Industrial automation vendors, Robotics companies, Machine vision integrators, Energy & infrastructure
- **Main Competitors/Alternatives**: NXP i.MX / S32, NVIDIA Jetson, Renesas RZ/V, Qualcomm Ride, Horizon Robotics Journey

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_texas_instruments`
- Product Entities: `ent_product_ti_tda4vm`, `ent_product_ti_am68a`
- Component Entities: `ent_component_ti_tda4vm_soc`, `ent_component_ti_am68a_soc`
- Key Relationships:
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_product_ti_tda4vm`
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_product_ti_am68a`
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_component_ti_tda4vm_soc`
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_component_ti_am68a_soc`
  - `ent_product_ti_tda4vm` -- `uses` --> `ent_component_ti_tda4vm_soc`
  - `ent_product_ti_am68a` -- `uses` --> `ent_component_ti_am68a_soc`

## References

1. [TI Official Website](https://www.ti.com)
2. [TDA4VM Product Page](https://www.ti.com/product/TDA4VM)
3. [Jacinto 7 Processors](https://www.ti.com/processors/automotive-processors/jacino-7-family.html)
