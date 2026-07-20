# MetaX

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 沐曦 |
| **English Name** | MetaX |
| **Headquarters** | Shanghai, China |
| **Founded** | 2020 |
| **Website** | [https://www.metax-tech.com](https://www.metax-tech.com) |
| **Supply Chain Role** | High-performance GPU, AI Inference/Training, Data Center, Domestic Computing Power |
| **Company Type** | Unicorn, Domestic High-Performance GPU Enterprise |
| **Parent Company/Group** | None (Independent Entity) |
| **Data Source** | MetaX official website, product launches, public press releases, industry research reports |

## Company Profile

MetaX focuses on high-performance GPU R&D, providing AI inference and training, graphics rendering, and scientific computing chips, building a domestic autonomous GPU computing ecosystem.

MetaX is a Chinese high-performance GPU innovation enterprise, with products covering three major directions: AI inference, AI training, and graphics rendering. The company has developed its own GPU architecture and software stack, launching the Xisi (inference) and Xiyun (training/general-purpose) product series, and provides solutions for data centers, intelligent computing centers, and edge scenarios.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Xisi Inference GPU | AI Inference Acceleration | MXN Series | Large model inference, recommendation, CV |
| Xiyun General-Purpose GPU | AI Training & General-Purpose Computing | MXC Series | Large model training, HPC, cloud gaming |
| Software Ecosystem | Compiler & Development Tools | MXMACA | AI framework adaptation, migration optimization |

## Representative Products

### MetaX High-Performance GPU / Xiyun MXC Series

> MetaX High-Performance GPU / Xiyun MXC Series: Please visit [Official Materials](https://www.metax-tech.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Architecture | MetaX self-developed high-performance GPU architecture | MetaX public materials |
| Process Node | 7 nm | Public reports |
| Compute Power | FP16/BF16 hundreds to thousands of TFLOPS | MetaX public materials |
| Memory | HBM2e / GDDR6 (varies by model) | Public reports |
| Interconnect | xGMI / PCIe (varies by model) | MetaX public materials |
| Power Consumption | Not disclosed | - |
| Form Factor | PCIe accelerator card / OAM module | MetaX public materials |
| Price | Not disclosed | - |

**Technical Highlights**: Domestic high-performance general-purpose GPU, unified software stack, supports training, inference, and graphics rendering, compatible with domestic server ecosystem.

**Application Scenarios**: Large model training and inference, intelligent computing centers, cloud gaming, scientific computing.

### MetaX Xisi MXN Inference GPU

> MetaX Xisi MXN Inference GPU: Please visit [Official Materials](https://www.metax-tech.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Positioning | Data center AI inference | MetaX public materials |
| Compute Power | High-throughput INT8/FP16 inference | MetaX public materials |
| Memory | Tens of GB (varies by model) | Public reports |
| Interface | PCIe Gen4 | Public reports |
| Energy Efficiency | Not disclosed | - |
| Supported Models | CV, NLP, recommendation, large models | MetaX public materials |
| Deployment | Data center servers | Not disclosed |
| Price | Not disclosed | - |

**Technical Highlights**: High inference throughput, low latency, unified software ecosystem with training cards, adapted for domestic computing power scenarios.

**Application Scenarios**: Large model inference, recommendation systems, video analysis, intelligent customer service.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, HBM/GDDR memory, packaging and testing, EDA, IP cores, server manufacturers.
- **Downstream Customers/Application Scenarios**: Major internet and cloud computing companies, intelligent computing centers, AI enterprises, research institutes.
- **Main Competitors/Peers**: NVIDIA, AMD, Biren Technology, Moore Threads, Haiguang Information, Cambricon.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_metax`
- Product Entities: `ent_product_metax_mxc`, `ent_product_metax_mxn`
- Key Relationships:
  - `ent_company_metax` -- `manufactures` --> `ent_product_metax_mxc`
  - `ent_company_metax` -- `manufactures` --> `ent_product_metax_mxn`
  - `ent_product_metax_mxc` -- `uses` --> `ent_component_hbm_memory`
  - `ent_product_metax_mxn` -- `uses` --> `ent_component_pcie_interface`

## References

1. [Official Website](https://www.metax-tech.com)
2. [MetaX Official Website](https://www.metax-tech.com)
3. MetaX product launch materials
