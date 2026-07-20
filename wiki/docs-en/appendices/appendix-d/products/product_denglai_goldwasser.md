# Denglai Technology Goldwasser X

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Denglai Technology](../companies/company_denglai.md) |
| **Product Category** | General-purpose GPU+ AI training/inference accelerator card |
| **Release Date** | Goldwasser series continuously iterated |
| **Status** | Mass production/commercial |
| **Official Website/Source** | Denglai Technology official website, product manual |

## Product Overview

Denglai Technology Goldwasser X is a cloud-based AI accelerator card based on a self-developed GPU+ innovative architecture. It integrates GPGPU general-purpose computing with AI-specific acceleration capabilities, providing energy-efficient domestic computing power for large model inference, training, and general-purpose computing.

Goldwasser X adopts Denglai Technology's GPU+ architecture, integrating general-purpose computing units and tensor acceleration units on a unified chip, balancing CUDA compatibility with AI task efficiency. The product supports multi-precision inference, multi-card interconnection, and mainstream framework adaptation, suitable for scenarios such as intelligent computing centers, internet companies, and AI enterprises.

## Product Image

> Denglai Technology Goldwasser X: Please visit [Official Materials](https://www.denglai.com.cn) for details.

## Specification Parameter Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Accelerator | Goldwasser X series | Denglai Technology official website |
| Architecture | GPU+ (GPGPU + AI acceleration) | Denglai Technology public information |
| Process Node | 7 nm | Public reports |
| AI Computing Power | Hundreds of TOPS (INT8 / FP16) | Denglai Technology public information |
| Memory | 32 GB HBM2e (some models) | Public reports |
| Memory Bandwidth | Not disclosed | - |
| Interconnect | Supports multi-card interconnection | Denglai Technology public information |
| Interface | PCIe Gen4 / OAM | Public reports |
| Power Consumption | Approximately 150–300 W (depending on model) | Public reports |
| Software Stack | CUDA-compatible runtime, Denglai SDK | Denglai Technology public information |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Denglai Technology](../companies/company_denglai.md)
- **Core Components/Technology Sources**: Self-developed GPU+ architecture, wafer foundry, HBM2e memory, packaging and testing, PCB, cooling.
- **Downstream Applications/Customers**: Internet enterprises, cloud computing providers, intelligent computing centers, AI companies, robotics companies, research institutes.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_denglai_goldwasser_x`
- Component Entity: `ent_component_denglai_goldwasser_x_accelerator`
- Manufacturer Entity: `ent_company_denglai`
- Key Relationships:
  - `rel_ent_company_denglai_manufactures_ent_product_denglai_goldwasser_x` (`ent_company_denglai` → `manufactures` --> `ent_product_denglai_goldwasser_x`)
  - `rel_ent_company_denglai_manufactures_ent_component_denglai_goldwasser_x_accelerator` (`ent_company_denglai` → `manufactures` --> `ent_component_denglai_goldwasser_x_accelerator`)
  - `ent_product_denglai_goldwasser_x` -- `uses` --> `ent_component_denglai_goldwasser_x_accelerator`

## Application Scenarios

- **Large Model Inference and Deployment**: Supports high-throughput inference for generative models such as LLM and VLM.
- **Cloud AI Training**: Used for small to medium-scale model training and fine-tuning tasks.
- **Robot Cloud Brain**: Provides remote perception, planning, and model service computing power for humanoid robots.

## Competitive Comparison

| Comparison Item | Goldwasser X | Cambricon MLU370 | NVIDIA T4/L4 |
|----------------|--------------|------------------|--------------|
| Architecture | GPU+ Fusion | Self-developed MLU | NVIDIA Tensor Core |
| Ecosystem | CUDA Compatible | Neuware | CUDA |
| Positioning | Training/Inference Balanced | Inference/Training | Inference-focused |
| Domestic Production | Self-controllable | Self-controllable | Subject to export controls |

## Purchase and Deployment Recommendations

- Select sub-models X/L/S based on workload, and pay attention to CUDA compatibility layer support for target operators.
- Confirm interconnect solutions, driver versions, and cluster scheduling tools for multi-card deployment.
- It is recommended to obtain the latest firmware, SDK, and technical support through Denglai Technology's official channels.

## Related Entries

- [Manufacturer: Denglai Technology](../companies/company_denglai.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Denglai Technology Official Website](https://www.denglai.com.cn)
2. [Denglai Technology Product Page](https://www.denglai.com.cn/product/)
3. Denglai Technology product launch materials
