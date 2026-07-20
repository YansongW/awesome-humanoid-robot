# Huawei Ascend / Atlas

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Huawei / Huawei](../companies/company_huawei.md) |
| **Product Category** | AI Computing Platform/Training & Inference Chip |
| **Release Date** | Ascend 910/310 released in 2018, with continuous iterations |
| **Status** | Mass Production/Commercial |
| **Official Website/Source** | See references in the main text |

## Product Overview

Huawei Ascend is a computing platform and processor series launched by Huawei for artificial intelligence scenarios, including the Ascend 910 training chip, Ascend 310 inference chip, and the Atlas series of computing hardware. Ascend, together with CANN, MindSpore, and the Pangu large model, forms a domestic AI software and hardware ecosystem and serves as one of the domestic computing power foundations for embodied intelligence and humanoid robot brains.

## Product Image

> Huawei Ascend / Atlas: Please visit the [official website](https://www.hiascend.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| AI Processor | Ascend 910 / 310 Series | Huawei Official Website |
| Computing Power | Ascend 910B FP16 approx. 320 TFLOPS / INT8 approx. 640 TOPS | Huawei Public Information |
| Memory | HBM2e / LPDDR4X (depending on model) | Huawei Public Information |
| Process Node | 7 nm (public reports) | Public Reports |
| Atlas Form Factor | Atlas 800 Training Server / Atlas 300I Inference Card | Huawei Official Website |
| Software Stack | CANN, MindSpore, MindIE | Huawei Ascend Community |
| Power Consumption | Approx. 310 W (Ascend 910 processor) | Public Information |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Huawei / Huawei](../companies/company_huawei.md)
- **Core Components/Technology Sources**: Self-developed Da Vinci architecture, wafer foundry, HBM memory, packaging and testing, PCB, cooling.
- **Downstream Applications/Customers**: Major internet companies, government and enterprise clients, intelligent computing centers, robot OEMs, research institutes.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_huawei_ascend`
- Manufacturer Entity: `ent_company_huawei`
- Key Relationships:
  - `rel_ent_company_huawei_manufactures_ent_product_huawei_ascend` (`ent_company_huawei` → `manufactures` → `ent_product_huawei_ascend`)
  - `ent_product_huawei_ascend` -- `uses` --> `ent_component_huawei_ascend_chip`
  - `ent_product_huawei_ascend` -- `runs` --> `ent_software_mindspore`

## Application Scenarios

- **Embodied Intelligence Brain**: Runs VLA/VLM large models for perception, understanding, and task planning.
- **Large Model Training**: Training of Pangu and third-party large models.
- **Edge Inference**: Atlas 200I and other edge devices for robot-side inference.

## Competitive Comparison

| Comparison Item | Ascend Atlas | NVIDIA Jetson/Data Center | Cambricon Siyuan |
|----------------|--------------|---------------------------|------------------|
| Ecosystem | CANN + MindSpore + Pangu | CUDA + PyTorch | Cambricon Neuware |
| Computing Power | High-end training/inference | Global leader | Training/inference |
| Domestic Production | Self-controllable | Subject to export controls | Self-controllable |

## Selection and Deployment Recommendations

- Select the appropriate model based on computing power, precision, and scenario requirements, prioritizing officially supported toolchains and ecosystem compatibility.
- Before deployment, confirm that power supply, cooling, mechanical interfaces, and communication protocols meet the overall system requirements.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Huawei / Huawei](../companies/company_huawei.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Huawei / Huawei Official Product/Company Page](https://www.hiascend.com)
2. [Huawei Ascend Community](https://www.hiascend.com)
3. Huawei Atlas Product Manual
