# Enflame Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 燧原科技 |
| **English Name** | Enflame Technology |
| **Headquarters** | Shanghai, China |
| **Founded** | 2018 |
| **Website** | [https://www.enflame-tech.com](https://www.enflame-tech.com) |
| **Supply Chain Role** | AI training/inference chips, cloud AI acceleration, intelligent computing centers, domestic computing power |
| **Company Type** | Unicorn, domestic AI chip company |
| **Parent Company/Group** | None (independent entity) |
| **Data Source** | Enflame official website, product launches, public press releases, industry research reports |

## Company Overview

Enflame Technology focuses on cloud AI computing products, providing AI training and inference acceleration cards and systems to support the construction of domestic intelligent computing centers.

Enflame Technology is a representative cloud AI chip company in China. It has developed its own GCU architecture and launched the Cloudblazer T series training chips/acceleration cards and the Cloudblazer i series inference chips/acceleration cards. The products emphasize high computing power, high energy efficiency, and large-scale cluster interconnection, supported by the GCU-LARE interconnect technology and the Yushan software stack.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Training Acceleration Cards | Cloud large model training | Cloudblazer T20 / T21 | Large model training, AIGC |
| Inference Acceleration Cards | Cloud AI inference | Cloudblazer i20 / i10 | Large model inference, recommendation, CV |
| Cluster and Software | Large-scale AI clusters and toolchains | Cloudblazer Intelligent Computing Cluster / Yushan | Intelligent computing centers, supercomputing |

## Representative Products

### Enflame Cloudblazer T20 / T21 Training Acceleration Card

> Enflame Cloudblazer T20 / T21 Training Acceleration Card: Please visit [official materials](https://www.enflame-tech.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Architecture | Proprietary GCU architecture | Enflame public materials |
| Process Node | Not disclosed | - |
| Computing Power | FP32/BF16/FP16 hundreds of TFLOPS level | Enflame public materials |
| Memory | HBM2e | Public reports |
| Interconnect | GCU-LARE chip-to-chip interconnect | Enflame public materials |
| Power Consumption | Approx. 300–350 W | Public reports |
| Form Factor | Dual-slot full-height PCIe accelerator card / OAM | Enflame public materials |
| Price | Not disclosed | - |

**Technical Highlights**: Domestic cloud training chip, GCU-LARE high-speed interconnect, high energy efficiency, supporting large-scale intelligent computing cluster solutions.

**Application Scenarios**: Large model training, AIGC, scientific computing, intelligent computing centers.

### Enflame Cloudblazer i20 Inference Acceleration Card

> Enflame Cloudblazer i20 Inference Acceleration Card: Please visit [official materials](https://www.enflame-tech.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Positioning | Cloud AI inference | Enflame public materials |
| Computing Power | High throughput INT8/FP16 | Enflame public materials |
| Memory | Not disclosed | - |
| Interface | PCIe Gen4 | Public reports |
| Energy Efficiency | Not disclosed | - |
| Supported Models | CV, NLP, large model inference | Enflame public materials |
| Software Stack | Yushan | Enflame public materials |
| Price | Not disclosed | - |

**Technical Highlights**: High inference throughput, low latency, unified software stack with training cards, adapted for domestic intelligent computing centers.

**Application Scenarios**: Large model inference, recommendation systems, video analysis, intelligent customer service.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, HBM memory, packaging and testing, EDA, servers, high-speed interconnect IP.
- **Downstream Customers/Application Scenarios**: Major internet companies, cloud computing providers, intelligent computing centers, AI enterprises, research institutes.
- **Main Competitors/Comparables**: NVIDIA A100/H100, Huawei Ascend, Cambricon, Biren Technology, Muxi.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_enflame`
- Product Entities: `ent_product_enflame_yunsui_t20`, `ent_product_enflame_yunsui_i20`
- Key Relationships:
  - `ent_company_enflame` -- `manufactures` --> `ent_product_enflame_yunsui_t20`
  - `ent_company_enflame` -- `manufactures` --> `ent_product_enflame_yunsui_i20`
  - `ent_product_enflame_yunsui_t20` -- `uses` --> `ent_component_hbm_memory`
  - `ent_product_enflame_yunsui_i20` -- `uses` --> `ent_component_pcie_interface`

## References

1. [Official Website](https://www.enflame-tech.com)
2. [Enflame Technology Official Website](https://www.enflame-tech.com)
3. Enflame product launch materials
