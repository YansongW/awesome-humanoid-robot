# Iluvatar CoreX Tianyi 200 / Iluvatar BI-V200

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Iluvatar CoreX](../companies/company_iluvatar.md) |
| **Product Category** | General-purpose GPU / AI Training and Inference Accelerator Card |
| **Release Date** | Iterated to Tianyi 200 after Tianyi 100 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | Iluvatar CoreX official website, product manual |

## Product Overview

Iluvatar CoreX Tianyi 200 (BI-V200) is a new generation general-purpose GPU accelerator card launched by Iluvatar CoreX. Based on a self-developed general-purpose GPU architecture, it provides domestic computing power for AI training, inference, and high-performance computing.

Tianyi 200 supports multi-precision computing such as FP32/FP16/BF16/INT8, is equipped with HBM2e high-bandwidth memory and a PCIe Gen4 interface, and is compatible with the mainstream CUDA application ecosystem. Its general-purpose GPU architecture is not only suitable for deep learning but can also support tasks such as scientific computing, graphics rendering, and robot simulation training.

## Product Image

> Iluvatar CoreX Tianyi 200: Please visit [Official Materials](https://www.iluvatar.com.cn) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|--------|-------|----------------|
| GPU | Tianyi 200 (BI-V200) | Iluvatar CoreX official website |
| Architecture | Self-developed general-purpose GPU architecture | Iluvatar CoreX public information |
| Process Node | 7 nm | Public reports |
| AI Compute Power | FP16 / BF16 / FP32 hundreds of TFLOPS level | Iluvatar CoreX public information |
| Memory | 32 GB HBM2e (some models) | Public reports |
| Memory Bandwidth | Not disclosed | - |
| Interconnect | Supports multi-card interconnection | Iluvatar CoreX public information |
| Interface | PCIe Gen4 / OAM | Public reports |
| Power Consumption | Approx. 300–350 W | Public reports |
| Software Stack | CUDA-compatible runtime, Iluvatar CoreX SDK | Iluvatar CoreX public information |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Iluvatar CoreX](../companies/company_iluvatar.md)
- **Core Components/Technology Sources**: Self-developed general-purpose GPU architecture, wafer foundry, HBM2e memory, packaging and testing, PCB, cooling.
- **Downstream Applications/Customers**: Internet companies, cloud computing providers, intelligent computing centers, AI companies, research institutes, robotics companies.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_iluvatar_biv200`
- Component Entity: `ent_component_iluvatar_biv200_gpu`
- Manufacturer Entity: `ent_company_iluvatar`
- Key Relationships:
  - `rel_ent_company_iluvatar_manufactures_ent_product_iluvatar_biv200` (`ent_company_iluvatar` → `manufactures` --> `ent_product_iluvatar_biv200`)
  - `rel_ent_company_iluvatar_manufactures_ent_component_iluvatar_biv200_gpu` (`ent_company_iluvatar` → `manufactures` --> `ent_component_iluvatar_biv200_gpu`)
  - `ent_product_iluvatar_biv200` -- `uses` --> `ent_component_iluvatar_biv200_gpu`

## Application Scenarios

- **Large Model Training and Fine-tuning**: Supports distributed training of models with tens of billions to hundreds of billions of parameters.
- **AIGC and Scientific Computing**: Used for generative AI, molecular simulation, CFD, and other high-performance computing tasks.
- **Robot Simulation and Training**: Combined with simulation platforms like Isaac Sim/Gazebo to accelerate policy learning and Sim2Real.

## Competitive Comparison

| Comparison Item | Tianyi 200 | NVIDIA A100 | Huawei Ascend 910B |
|--------|------|------|------|
| Architecture | General-purpose GPU | NVIDIA Ampere | DaVinci |
| Ecosystem | CUDA compatible | CUDA | CANN + MindSpore |
| Memory | 32 GB HBM2e | 40/80 GB HBM | HBM2e |
| Localization | Independent and controllable | Subject to export control restrictions | Independent and controllable |

## Selection and Deployment Recommendations

- Before migrating CUDA applications, verify the completeness and performance of the Iluvatar CoreX compatibility layer.
- For multi-card training scenarios, confirm the interconnect bandwidth, NCCL compatibility, and cluster topology.
- It is recommended to obtain the latest drivers, SDKs, and technical support through Iluvatar CoreX's official channels.

## Related Entries

- [Manufacturer: Iluvatar CoreX](../companies/company_iluvatar.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Iluvatar CoreX Official Website](https://www.iluvatar.com.cn)
2. [Iluvatar CoreX Product Page](https://www.iluvatar.com.cn/product/)
3. Iluvatar CoreX Product Launch Materials
