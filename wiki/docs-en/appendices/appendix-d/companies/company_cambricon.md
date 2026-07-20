# Cambricon

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 寒武纪 |
| **English Name** | Cambricon Technologies |
| **Headquarters** | Haidian District, Beijing, China |
| **Founded** | 2016 |
| **Website** | [https://www.cambricon.com](https://www.cambricon.com) |
| **Supply Chain Role** | AI Chips, Cloud/Edge Intelligent Acceleration, Domestic Computing Power |
| **Enterprise Type** | Listed Company (STAR Market: 688256) |
| **Parent Company/Group** | None (Independent Listed Entity) |
| **Data Source** | Cambricon official website, annual reports, product manuals, public press releases |

## Company Profile

Cambricon is a leading AI chip design company in China, providing intelligent acceleration chips and basic system software for cloud, edge, and terminal scenarios.

With its proprietary MLU (Machine Learning Unit) architecture at the core, Cambricon covers cloud training/inference, edge computing, and terminal intelligent scenarios, supported by the Neuware software stack. Its cloud intelligent chip Siyuan series is widely used in internet, cloud computing, intelligent computing centers, and large model inference, serving as one of the domestic computing power alternatives for embodied intelligent systems such as humanoid robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Cloud Intelligent Chips | Data Center AI Training/Inference | Siyuan 370 / 590 Series | Large Model Inference, Intelligent Computing Centers |
| Edge Intelligent Chips | Edge AI Inference | Siyuan 220 Series | Edge Boxes, Industrial Inspection, Robotics |
| Terminal Intelligent Processor IP | Mobile/IoT/Embedded Devices | Cambricon-1A / 1H Series | Smart Terminals, Autonomous Driving |
| Basic System Software | Chip Enablement Software Stack | Neuware | Full Series of Chips |

## Representative Products

### Cambricon Siyuan 370 (MLU370-X8 / S4, etc.)

> Cambricon Siyuan 370: Please visit [official documentation](https://www.cambricon.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Architecture | Proprietary MLUarch03 | Cambricon public information |
| Process Node | 7 nm (public reports) | Public reports |
| Computing Power | INT8 up to ~256 TOPS; FP16 ~128 TFLOPS | Cambricon public information |
| Memory | 48 GB LPDDR4X (some models) | Public reports |
| Interconnect | MLU-Link (chip-to-chip) | Cambricon public information |
| Power Consumption | ~75–250 W (depending on form factor) | Public reports |
| Interface | PCIe Gen4 / OAM | Cambricon public information |
| Price | Not disclosed | - |

**Technical Highlights**: New-generation MLU architecture, on-chip high-bandwidth memory, MLU-Link multi-card interconnect, support for Transformer and large model inference.

**Application Scenarios**: Cloud large model inference, intelligent computing centers, recommendation systems, video analysis, embodied intelligence brain.

### Cambricon Siyuan 220 (Edge Inference)

> Cambricon Siyuan 220: Please visit [official documentation](https://www.cambricon.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Architecture | Proprietary MLUarch02 | Cambricon public information |
| Process Node | 16 nm (public reports) | Public reports |
| Computing Power | INT8 up to ~16 TOPS | Cambricon public information |
| Memory | LPDDR4X | Public reports |
| Power Consumption | ~8–15 W | Public reports |
| Interface | M.2 / PCIe mini / Edge Module | Cambricon public information |
| Software Stack | Neuware | Cambricon public information |
| Price | Not disclosed | - |

**Technical Highlights**: Low-power edge inference, small form factor module, support for CV and voice applications, unified with cloud software stack.

**Application Scenarios**: Edge boxes, robot-side perception, industrial quality inspection, smart cameras.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, packaging and testing, memory, EDA/IP, PCB, thermal solutions.
- **Downstream Customers/Application Scenarios**: Internet companies, cloud computing providers, intelligent computing centers, AI companies, robot OEMs, research institutes.
- **Main Competitors/Peers**: NVIDIA GPU, Huawei Ascend, Baidu Kunlun Chip, Enflame Technology, Hygon Information Technology.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_cambricon`
- Product Entity: `ent_product_cambricon_mlu370`
- Component Entity: `ent_component_cambricon_mlu370_chip`
- Key Relationships:
  - `ent_company_cambricon` -- `manufactures` --> `ent_product_cambricon_mlu370`
  - `ent_company_cambricon` -- `manufactures` --> `ent_component_cambricon_mlu370_chip`
  - `ent_product_cambricon_mlu370` -- `uses` --> `ent_component_cambricon_mlu370_chip`

## References

1. [Cambricon Official Website](https://www.cambricon.com)
2. [Cambricon Product Page](https://www.cambricon.com/index.php?m=content&c=index&a=lists&catid=75)
3. Cambricon 2024 Annual Report
