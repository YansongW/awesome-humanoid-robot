# Biren Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 壁仞科技 |
| **English Name** | Biren Technology |
| **Headquarters** | Shanghai, China |
| **Founded** | 2019 |
| **Official Website** | [https://www.birentech.com](https://www.birentech.com) |
| **Supply Chain Role** | General-purpose GPU, AI training/inference chips, intelligent computing centers, domestic computing power |
| **Company Type** | Unicorn, domestic GPU unicorn |
| **Parent Company/Group** | None (independent entity) |
| **Data Source** | Biren official website, product launches, public press releases, industry research reports |

## Company Overview

Biren Technology focuses on general-purpose GPU R&D, providing high-performance AI training and inference chips, and is committed to building a domestically controlled and independent computing power foundation.

Biren Technology is one of the representative companies in China's general-purpose GPU field. Its core product, the BR100 series, is based on the self-developed Biren architecture and is designed for large model training, inference, and high-performance computing. The company emphasizes software-hardware synergy, offers the BIRENSUPA software stack, and actively participates in the construction of domestic intelligent computing centers.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| General-purpose GPU Chips | AI training/inference and HPC | BR100 / BR104 | Large models, AIGC, scientific computing |
| Accelerator Cards and Servers | Data center AI acceleration | BR100 accelerator card / OAM module | Intelligent computing centers, cloud computing |
| Software Stack | Compiler and development tools | BIRENSUPA | AI framework adaptation, model migration |

## Representative Products

### Biren BR100 Series GPU

> Biren BR100 Series GPU: Please visit [official materials](https://www.birentech.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Architecture | Biren self-developed general-purpose GPU architecture | Biren public materials |
| Process Node | 7 nm | Public reports |
| Transistor Count | Approximately 77 billion | Biren product launch |
| Compute Power | FP32 ~1000 TFLOPS; BF16/FP16 ~2000 TFLOPS | Biren public materials |
| Memory | 64 GB HBM2e / HBM3 | Public reports |
| Interconnect | BLink chip-to-chip interconnect | Biren public materials |
| Power Consumption | Approximately 550 W | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: High-performance domestic general-purpose GPU, large computing power and high-bandwidth memory, BLink high-speed interconnect, support for large model training and inference.

**Application Scenarios**: Large model training, AIGC, scientific computing, intelligent computing centers.

### Biren BIRENSUPA Software Platform

> Biren BIRENSUPA Software Platform: Please visit [official materials](https://www.birentech.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Components | Driver, compiler, runtime, operator library | Biren public materials |
| Framework Support | PyTorch, TensorFlow, PaddlePaddle, etc. | Biren public materials |
| Model Library | Large model, CV, NLP examples | Biren public materials |
| Migration Tools | Model migration and performance tuning tools | Biren public materials |
| Deployment Method | Local / Cluster / Cloud | Not disclosed |
| Development Language | Python / C++ | Biren public materials |
| License | Not disclosed | - |
| Price | Provided with hardware | Not disclosed |

**Technical Highlights**: Domestic GPU software stack, adaptation to mainstream AI frameworks, reduced model migration costs.

**Application Scenarios**: AI model training and inference, domestic computing power adaptation, intelligent computing center operations.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry (TSMC/domestic foundries), HBM memory, packaging and testing, EDA tools, IP cores.
- **Downstream Customers/Application Scenarios**: Major internet companies, intelligent computing centers, research institutes, AI startups, cloud computing providers.
- **Main Competitors/Peers**: NVIDIA A100/H100, AMD MI series, Huawei Ascend, Haiguang Information, Cambricon.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_biren`
- Product Entities: `ent_product_biren_br100`, `ent_product_biren_supa`
- Key Relationships:
  - `ent_company_biren` -- `manufactures` --> `ent_product_biren_br100`
  - `ent_company_biren` -- `manufactures` --> `ent_product_biren_supa`
  - `ent_product_biren_br100` -- `uses` --> `ent_component_hbm_memory`
  - `ent_product_biren_br100` -- `runs_with` --> `ent_product_biren_supa`

## References

1. [Official Website](https://www.birentech.com)
2. [Biren Technology Official Website](https://www.birentech.com)
3. Biren BR100 Product Launch Materials
