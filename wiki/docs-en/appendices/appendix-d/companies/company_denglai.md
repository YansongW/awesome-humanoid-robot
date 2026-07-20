# Denglai Technology

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 登临科技 |
| **English Name** | Denglai Technology |
| **Headquarters** | Pudong New Area, Shanghai, China |
| **Founded** | 2017 |
| **Website** | [https://www.denglai.com.cn](https://www.denglai.com.cn) |
| **Supply Chain Role** | General-purpose GPU, AI inference/training chips, domestic computing power |
| **Company Type** | Unicorn, domestic GPU enterprise |
| **Parent Company/Group** | None (independent entity) |
| **Data Source** | Denglai Technology official website, product launches, public press releases, industry research reports |

## Company Overview

Denglai Technology is a Chinese company focused on general-purpose GPU and AI accelerator design. It centers on the innovative "GPU+" architecture to deliver high-performance AI computing products.

Denglai Technology proposed the GPU+ (GPGPU + AI acceleration) architecture, balancing graphics/general computing and deep learning acceleration, and launched the Goldwasser series of accelerator cards. Its products emphasize high compute utilization, low power consumption, and CUDA compatibility, and are widely used in cloud inference, edge computing, intelligent computing centers, and large model deployment.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Goldwasser Series | Cloud AI training/inference accelerator cards | Goldwasser X / L / S Series | Large model inference, CV, NLP |
| Edge/Industry Solutions | Edge AI and industry all-in-one machines | Custom industry solutions | Smart manufacturing, smart cities |
| Software Stack | Chip enablement and development tools | Denglai Software Stack | Full series of accelerator cards |

## Representative Products

### Denglai Technology Goldwasser X (Goldwasser-XL)

> Denglai Technology Goldwasser X: Please visit [official materials](https://www.denglai.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Architecture | GPU+ innovative architecture (GPGPU + AI acceleration) | Denglai Technology public materials |
| Process Node | 7 nm (public reports) | Public reports |
| Compute Power | High throughput INT8 / FP16 (hundreds of TOPS level) | Denglai Technology public materials |
| Memory | 32 GB HBM2e (some models) | Public reports |
| Interconnect | Supports multi-card interconnect | Denglai Technology public materials |
| Interface | PCIe Gen4 | Public reports |
| Power Consumption | Approx. 150–300 W (varies by model) | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: GPU+ architecture balances general computing and AI acceleration, high compute utilization, CUDA compatibility, supports multi-precision inference.

**Application Scenarios**: Large model inference, AIGC, recommendation systems, video analysis, intelligent computing centers.

### Denglai Technology Goldwasser-L (Edge Inference)

> Denglai Technology Goldwasser L: Please visit [official materials](https://www.denglai.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Positioning | Edge/lightweight inference | Denglai Technology public materials |
| Compute Power | INT8 tens to hundreds of TOPS level | Denglai Technology public materials |
| Memory | Not disclosed | - |
| Interface | PCIe / M.2 | Public reports |
| Power Consumption | Approx. 25–75 W | Public reports |
| Software Stack | Denglai Technology SDK | Denglai Technology public materials |
| Application Scenarios | Edge computing, robot-side inference | Denglai Technology public materials |
| Price | Not disclosed | - |

**Technical Highlights**: Low-power edge inference, compact form factor, unified software stack with cloud cards.

**Application Scenarios**: Edge boxes, robot perception, industrial quality inspection, smart cities.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, HBM memory, packaging and testing, EDA/IP, PCB, cooling.
- **Downstream Customers/Application Scenarios**: Major internet companies, cloud computing providers, intelligent computing centers, AI enterprises, robotics companies, research institutes.
- **Main Competitors/Peers**: NVIDIA T4/L4, Cambricon, Enflame Technology, Tianshu Zhixin, Muxi.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_denglai`
- Product Entity: `ent_product_denglai_goldwasser_x`
- Component Entity: `ent_component_denglai_goldwasser_x_accelerator`
- Key Relationships:
  - `ent_company_denglai` -- `manufactures` --> `ent_product_denglai_goldwasser_x`
  - `ent_company_denglai` -- `manufactures` --> `ent_component_denglai_goldwasser_x_accelerator`
  - `ent_product_denglai_goldwasser_x` -- `uses` --> `ent_component_denglai_goldwasser_x_accelerator`

## References

1. [Denglai Technology Official Website](https://www.denglai.com.cn)
2. [Denglai Technology Product Page](https://www.denglai.com.cn/product/)
3. Denglai Technology product launch materials
