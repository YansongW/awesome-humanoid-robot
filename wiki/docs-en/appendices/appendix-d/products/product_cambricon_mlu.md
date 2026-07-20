# Cambricon MLU370

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Cambricon](../companies/company_cambricon.md) |
| **Product Category** | AI Inference/Training Accelerator Chip and Accelerator Card |
| **Release Date** | 2021: MLU370 series launched |
| **Status** | Mass Production/Commercial |
| **Official Website/Source** | Cambricon official website, product manual |

## Product Overview

The Cambricon MLU370 is Cambricon's third-generation cloud AI chip, based on the proprietary MLUarch03 architecture, providing domestic computing power support for cloud inference, training, and large model deployment.

The MLU370 series includes variants such as MLU370-X8, MLU370-S4, and MLU370-X4, covering PCIe accelerator cards, OAM modules, and complete machine solutions. The chip supports multi-precision computing including INT8/INT16/FP16/BF16, integrates high-bandwidth memory and MLU-Link inter-chip interconnect, and is paired with the Neuware software stack, capable of running CV, NLP, recommendation, and generative AI workloads.

## Product Image

> Cambricon MLU370: Please visit [official materials](https://www.cambricon.com) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| AI Processor | MLU370 | Cambricon official website |
| Architecture | Proprietary MLUarch03 | Cambricon public information |
| Process Node | 7 nm | Public reports |
| AI Compute Power | INT8 up to ~256 TOPS; FP16 ~128 TFLOPS | Cambricon public information |
| Memory | 48 GB LPDDR4X / HBM2e (varies by model) | Public reports |
| Memory Bandwidth | Not disclosed | - |
| Inter-chip Interconnect | MLU-Link | Cambricon public information |
| Interface | PCIe Gen4 / OAM | Cambricon public information |
| Power Consumption | ~75–250 W (varies by form factor) | Public reports |
| Software Stack | Neuware, PyTorch/TensorFlow adaptation | Cambricon public information |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Cambricon](../companies/company_cambricon.md)
- **Core Components/Technology Sources**: Proprietary MLU architecture, wafer foundry, LPDDR/HBM memory, packaging and testing, PCB, cooling.
- **Downstream Applications/Customers**: Cloud computing vendors, internet companies, AI computing centers, AI companies, research institutes, robot OEMs.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_cambricon_mlu370`
- Component Entity: `ent_component_cambricon_mlu370_chip`
- Manufacturer Entity: `ent_company_cambricon`
- Key Relationships:
  - `rel_ent_company_cambricon_manufactures_ent_product_cambricon_mlu370` (`ent_company_cambricon` → `manufactures` → `ent_product_cambricon_mlu370`)
  - `rel_ent_company_cambricon_manufactures_ent_component_cambricon_mlu370_chip` (`ent_company_cambricon` → `manufactures` → `ent_component_cambricon_mlu370_chip`)
  - `ent_product_cambricon_mlu370` -- `uses` --> `ent_component_cambricon_mlu370_chip`

## Application Scenarios

- **Cloud Large Model Inference**: Deploy generative models such as LLMs and VLMs to provide text/multimodal inference services.
- **AI Computing Centers**: Serve as domestic AI acceleration nodes to support mixed training and inference workloads.
- **Robot Brain**: Provide cloud/edge perception, planning, and decision-making computing power for humanoid robots.

## Competitive Comparison

| Comparison Item | Cambricon MLU370 | NVIDIA A10/L4 | Huawei Ascend 310/910 |
|----------------|------------------|---------------|-----------------------|
| Architecture | Proprietary MLU | NVIDIA Ampere/Ada | DaVinci |
| Ecosystem | Neuware + Domestic Frameworks | CUDA + PyTorch | CANN + MindSpore |
| Domestic Production | Independent and Controllable | Subject to Export Controls | Independent and Controllable |

## Procurement and Deployment Recommendations

- Select the X8/S4 or other form factor based on model type and precision requirements; prioritize confirming Neuware support for the target model.
- Before deployment, evaluate whether power supply, cooling, and PCIe topology meet multi-card interconnect requirements.
- It is recommended to obtain the latest firmware and SDK through Cambricon's official channels or authorized distributors.

## Related Entries

- [Manufacturer: Cambricon](../companies/company_cambricon.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Cambricon Official Website](https://www.cambricon.com)
2. [Cambricon MLU370 Product Page](https://www.cambricon.com/index.php?m=content&c=index&a=lists&catid=75)
3. Cambricon Product Manuals and White Papers
