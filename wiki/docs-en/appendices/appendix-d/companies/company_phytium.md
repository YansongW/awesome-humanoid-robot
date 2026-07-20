# Phytium

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 飞腾 |
| **English Name** | Phytium Technology |
| **Headquarters** | Binhai New Area, Tianjin, China |
| **Founded** | 2014 |
| **Website** | [https://www.phytium.com.cn](https://www.phytium.com.cn) |
| **Supply Chain Role** | Domestic CPU, Server/Desktop/Embedded Processors, Autonomous Controllable Computing Platform |
| **Enterprise Type** | State-controlled High-tech Enterprise |
| **Parent Company/Group** | China Electronics Corporation (CEC) |
| **Data Sources** | Phytium official website, product manuals, public press releases, industry research reports |

## Company Overview

Phytium is a leading domestic provider of autonomous core chips, specializing in the R&D of high-performance general-purpose CPUs based on the ARM architecture, providing a domestic computing power foundation for servers, desktops, embedded systems, and AI computing.

Based on the ARMv8 instruction set, Phytium independently develops high-performance processor cores, forming three major series: Phytium Tengyun, Tengrui, and Tenglong, which are compatible with domestic operating systems and software ecosystems. Its products are widely used in government affairs, finance, telecommunications, energy, industrial control, and intelligent computing fields, and can serve as domestic main control CPUs for edge/embedded systems such as robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Tengyun Series | High-performance Server CPU | Phytium S5000C / S2500 | Servers, Cloud Computing, Intelligent Computing Centers |
| Tengrui Series | Desktop/Embedded CPU | Phytium D3000 / D2000 | Desktops, Laptops, Industrial Control |
| Tenglong Series | Embedded CPU | Phytium E2000 | Embedded Systems, Edge Devices, Robot Control |
| AI Computing | CPU+AI Integrated Computing | Solutions adapted with domestic AI accelerators | Intelligent Computing, Robotics |

## Representative Products

### Phytium Tengyun S5000C

> Phytium Tengyun S5000C: Please visit [Official Documentation](https://www.phytium.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Architecture | ARMv8 Self-developed FTC862 Core | Phytium public documentation |
| Core Count | Up to 64 cores | Phytium public documentation |
| Process Node | 7 nm (public reports) | Public reports |
| Clock Speed | Up to 2.1 GHz | Phytium public documentation |
| Memory | Supports DDR4 / DDR5 (depending on model) | Phytium public documentation |
| Interconnect | Supports multi-way interconnect | Phytium public documentation |
| Power Consumption | Approx. 150–250 W (depending on model) | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: Self-developed FTC core, high-concurrency multi-core performance, domestic security and trustworthiness, compatible with domestic operating systems and middleware.

**Application Scenarios**: Domestic servers, cloud computing, databases, intelligent computing centers, robot backend training and simulation.

### Phytium Tengrui D3000

> Phytium Tengrui D3000: Please visit [Official Documentation](https://www.phytium.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Architecture | ARMv8 Self-developed FTC862 Core | Phytium public documentation |
| Core Count | Up to 8 cores | Phytium public documentation |
| Clock Speed | Up to 2.5 GHz | Phytium public documentation |
| Memory | DDR4 / DDR5 | Phytium public documentation |
| Interfaces | PCIe, USB, SATA, etc. | Phytium public documentation |
| Power Consumption | Approx. 25–40 W | Public reports |
| Application Scenarios | Desktop, Industrial Control, Edge Computing | Phytium public documentation |
| Price | Not disclosed | - |

**Technical Highlights**: Desktop-level performance, low power consumption, high integration, supports domestic office and industrial software ecosystems.

**Application Scenarios**: Domestic desktop terminals, industrial controllers, edge gateways, robot local main control.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, packaging and testing, memory, motherboard/PCB, BIOS/firmware, operating system adaptation.
- **Downstream Customers/Application Scenarios**: Government, finance, telecommunications, energy, rail transit, industrial automation, robot OEMs, research institutes.
- **Main Competitors/Peers**: Huawei Kunpeng, Hygon Information Technology, Loongson, Zhaoxin, Intel Xeon, AMD EPYC.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_phytium`
- Product Entity: `ent_product_phytium_s5000c`
- Component Entity: `ent_component_phytium_s5000c_cpu`
- Key Relationships:
  - `ent_company_phytium` -- `manufactures` --> `ent_product_phytium_s5000c`
  - `ent_company_phytium` -- `manufactures` --> `ent_component_phytium_s5000c_cpu`
  - `ent_product_phytium_s5000c` -- `uses` --> `ent_component_phytium_s5000c_cpu`

## References

1. [Phytium Official Website](https://www.phytium.com.cn)
2. [Phytium Product Page](https://www.phytium.com.cn/product/)
3. Phytium Public Product Manuals
