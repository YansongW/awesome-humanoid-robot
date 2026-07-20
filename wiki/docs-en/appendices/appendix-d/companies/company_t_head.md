# T-Head Semiconductor

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 平头哥半导体 |
| **English Name** | T-Head Semiconductor |
| **Headquarters** | Hangzhou, Zhejiang Province, China |
| **Founded** | 2018 |
| **Website** | [https://www.t-head.cn](https://www.t-head.cn) |
| **Supply Chain Role** | RISC-V/ARM processor IP, AI chips, cloud computing chips, embedded computing |
| **Enterprise Nature** | Wholly-owned subsidiary of Alibaba Group |
| **Parent Company/Group** | Alibaba Group |
| **Data Source** | T-Head official website, Alibaba Cloud Apsara Conference materials, product manuals, public press releases |

## Company Profile

T-Head Semiconductor is Alibaba's chip company, focusing on RISC-V and ARM architecture processor IP, AI acceleration chips, and cloud computing chip development.

T-Head's core product lines include the "XuanTie" RISC-V processor IP, the "Hanguang" AI inference chip, and the "Yitian" ARM server CPU, building end-edge-cloud full-stack computing power. Its RISC-V ecosystem and AI acceleration capabilities provide high flexibility and energy-efficient computing solutions for robotics, IoT, and edge intelligence.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| XuanTie RISC-V | RISC-V processor IP | XuanTie C906 / C910 / C920 / R908 | MCU, edge AI, robot control |
| Hanguang AI Chip | Cloud/edge AI inference | Hanguang 800 | Data centers, cloud AI inference |
| Yitian CPU | Cloud-native server CPU | Yitian 710 | Cloud computing, servers |
| Wujian Platform | SoC design platform | Wujian 100 / 600 | Chip customization |

## Representative Products

### T-Head XuanTie C920

> T-Head XuanTie C920: Please visit [official materials](https://www.t-head.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Architecture | RISC-V RV64GC + Vector 1.0 | T-Head public materials |
| Pipeline | 12-stage out-of-order superscalar | T-Head public materials |
| Frequency | Up to 3 GHz (public reports) | Public reports |
| Compute Performance | Not disclosed | - |
| Cache | Supports multi-level cache | T-Head public materials |
| Interfaces | AXI / ACE and other standard buses | T-Head public materials |
| Power Consumption | Depends on implementation scenario | T-Head public materials |
| Price | IP licensing, not disclosed | - |

**Technical Highlights**: High-performance RISC-V core, supports Vector extension, can integrate AI accelerator, rich open-source software ecosystem.

**Application Scenarios**: Edge AI computing, robot main control MCU/MPU, industrial control, AIoT.

### T-Head Hanguang 800

> T-Head Hanguang 800: Please visit [official materials](https://www.t-head.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Architecture | Self-developed deep neural network inference architecture | T-Head public materials |
| Process Node | 12 nm (public reports) | Public reports |
| Compute Performance | INT8 up to approximately 80,000 TOPS (peak) | T-Head public materials |
| Memory | HBM2 | Public reports |
| Interface | PCIe Gen3 x16 | Public reports |
| Power Consumption | Not disclosed | - |
| Application Scenarios | Data center AI inference, visual recognition | T-Head public materials |
| Price | Not disclosed | - |

**Technical Highlights**: High inference throughput, low latency, optimized for e-commerce/vision/search scenarios, deeply integrated with Alibaba Cloud services.

**Application Scenarios**: Cloud-based image recognition, video analysis, recommendation systems, large model inference acceleration.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, packaging and testing, HBM/memory, EDA/IP, PCB, thermal management.
- **Downstream Customers/Application Scenarios**: Alibaba Cloud, IoT device manufacturers, chip design companies, robot OEMs, industrial automation enterprises.
- **Main Competitors/Peers**: ARM Cortex, SiFive, Andes, Huawei Ascend, Cambricon, NVIDIA T4.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_t_head`
- Product Entity: `ent_product_t_head_xuantie_c920`
- Component Entity: `ent_component_t_head_xuantie_c920_ip`
- Key Relationships:
  - `ent_company_t_head` -- `manufactures` --> `ent_product_t_head_xuantie_c920`
  - `ent_company_t_head` -- `manufactures` --> `ent_component_t_head_xuantie_c920_ip`
  - `ent_product_t_head_xuantie_c920` -- `uses` --> `ent_component_t_head_xuantie_c920_ip`

## References

1. [T-Head Official Website](https://www.t-head.cn)
2. [T-Head XuanTie Series](https://www.t-head.cn/product/)
3. Alibaba Cloud Apsara Conference public materials
