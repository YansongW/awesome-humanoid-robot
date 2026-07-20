# Iluvatar CoreX

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 天数智芯 |
| **English Name** | Iluvatar CoreX |
| **Headquarters** | Pudong New Area, Shanghai, China |
| **Founded** | 2015 |
| **Website** | [https://www.iluvatar.com.cn](https://www.iluvatar.com.cn) |
| **Supply Chain Role** | General-purpose GPU, AI training/inference chips, domestic computing power |
| **Enterprise Type** | Unicorn, domestic GPU enterprise |
| **Parent Company/Group** | None (independent entity) |
| **Data Source** | Iluvatar CoreX official website, product launches, public press releases, industry research reports |

## Company Profile

Iluvatar CoreX is a Chinese enterprise focused on the design of general-purpose GPUs and high-performance computing chips, dedicated to building autonomous and controllable cloud-based AI training and inference computing power.

Iluvatar CoreX has launched the "Tian'e" series of general-purpose GPU accelerator cards and the "Zhikai" series of inference accelerator cards. These products adopt a self-developed general-purpose GPU architecture, are compatible with the mainstream CUDA ecosystem, and support large model training, inference, and scientific computing. Its products are positioned as domestic alternatives, providing high-performance computing power for intelligent computing centers, the internet, finance, and scientific research.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Tian'e Series | General-purpose GPU training accelerator cards | Tian'e 100 / 200 | Large model training, HPC |
| Zhikai Series | AI inference accelerator cards | Zhikai 100 / 200 | Large model inference, CV, recommendation |
| Software Stack | Chip enablement and development tools | Iluvatar CoreX software stack | All series accelerator cards |

## Representative Products

### Iluvatar CoreX Tian'e 200 (BI-V200)

> Iluvatar CoreX Tian'e 200: Please visit [official materials](https://www.iluvatar.com.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Architecture | Self-developed general-purpose GPU architecture | Iluvatar CoreX public materials |
| Process Node | 7 nm (public reports) | Public reports |
| Computing Power | FP16 / BF16 / FP32 hundreds of TFLOPS level | Iluvatar CoreX public materials |
| Memory | 32 GB HBM2e (some models) | Public reports |
| Interconnect | Supports multi-card interconnection | Iluvatar CoreX public materials |
| Interface | PCIe Gen4 / OAM | Public reports |
| Power Consumption | Approx. 300–350 W | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: General-purpose GPU architecture, CUDA compatible, supports large-scale parallel computing, complete software stack.

**Application Scenarios**: Large model training, AIGC, scientific computing, intelligent computing centers, robot simulation and training.

### Iluvatar CoreX Zhikai 100 (MR-V100)

> Iluvatar CoreX Zhikai 100: Please visit [official materials](https://www.iluvatar.com.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Positioning | Cloud AI inference | Iluvatar CoreX public materials |
| Computing Power | INT8 / FP16 high throughput | Iluvatar CoreX public materials |
| Memory | Not disclosed | - |
| Interface | PCIe Gen4 | Public reports |
| Energy Efficiency | Not disclosed | - |
| Software Stack | Iluvatar CoreX inference software stack | Iluvatar CoreX public materials |
| Power Consumption | Approx. 150 W | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: High inference throughput, low latency, unified architecture and software ecosystem with training cards.

**Application Scenarios**: Large model inference, recommendation systems, video analysis, intelligent customer service, embodied intelligence cloud inference.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, HBM memory, packaging and testing, EDA/IP, servers, high-speed interconnects.
- **Downstream Customers/Application Scenarios**: Major internet companies, cloud computing providers, intelligent computing centers, AI enterprises, research institutes, robotics companies.
- **Main Competitors/Comparables**: NVIDIA A100/H100, AMD MI series, Huawei Ascend, Biren Technology, Muxi.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_iluvatar`
- Product Entity: `ent_product_iluvatar_biv200`
- Component Entity: `ent_component_iluvatar_biv200_gpu`
- Key Relationships:
  - `ent_company_iluvatar` -- `manufactures` --> `ent_product_iluvatar_biv200`
  - `ent_company_iluvatar` -- `manufactures` --> `ent_component_iluvatar_biv200_gpu`
  - `ent_product_iluvatar_biv200` -- `uses` --> `ent_component_iluvatar_biv200_gpu`

## References

1. [Iluvatar CoreX Official Website](https://www.iluvatar.com.cn)
2. [Iluvatar CoreX Product Page](https://www.iluvatar.com.cn/product/)
3. Iluvatar CoreX Product Launch Materials
