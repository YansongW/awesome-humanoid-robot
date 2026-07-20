# VeriSilicon VIP9000 NPU IP

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [VeriSilicon](../companies/company_verisilicon.md) |
| **Product Category** | Neural Network Processor IP (NPU IP) |
| **Release Date** | VIP9000 series continuously iterated |
| **Status** | Commercial licensing |
| **Official Website/Source** | VeriSilicon official website, product manuals |

## Product Overview

The VeriSilicon VIP9000 series is a configurable and scalable neural network processor IP, providing efficient AI acceleration capabilities for edge AI, smart automotive, consumer electronics, and robotics chips.

VIP9000 supports precisions such as INT8/INT16/FP16/BFloat16 and can run mainstream networks including CNN, Transformer, and large language models. Its highly configurable hardware architecture allows customers to flexibly tailor performance, power, and area targets, and it works in synergy with VeriSilicon's ISP, GPU, and video codec IP to build end-to-end vision and AI solutions.

## Product Image

> VeriSilicon VIP9000: Please visit the [official website](https://www.verisilicon.com) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| IP Name | VeriSilicon VIP9000 Series NPU | VeriSilicon official website |
| Type | Neural Network Processor IP | VeriSilicon public information |
| Performance Range | 0.5–hundreds of TOPS (depending on configuration) | VeriSilicon public information |
| Precision Support | INT8 / INT16 / FP16 / BFloat16 | VeriSilicon public information |
| Model Support | TensorFlow / PyTorch / ONNX, etc. | VeriSilicon public information |
| Bus Interface | AXI / AHB | VeriSilicon public information |
| Process Node | Customer selectable | Public reports |
| Power Consumption | Depends on customer implementation | VeriSilicon public information |
| Licensing Model | IP licensing + chip customization services | VeriSilicon public information |
| Price | IP licensing, not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [VeriSilicon](../companies/company_verisilicon.md)
- **Core Components/Technology Source**: Self-developed NPU microarchitecture, EDA tools, customer wafer foundry/packaging and testing.
- **Downstream Applications/Customers**: Chip design companies, IDMs, Fabless, automotive electronics, consumer electronics, robotics chip manufacturers.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_verisilicon_vip9000`
- Component Entity: `ent_component_verisilicon_vip9000_npu`
- Manufacturer Entity: `ent_company_verisilicon`
- Key Relationships:
  - `rel_ent_company_verisilicon_manufactures_ent_product_verisilicon_vip9000` (`ent_company_verisilicon` → `manufactures` --> `ent_product_verisilicon_vip9000`)
  - `rel_ent_company_verisilicon_manufactures_ent_component_verisilicon_vip9000_npu` (`ent_company_verisilicon` → `manufactures` --> `ent_component_verisilicon_vip9000_npu`)
  - `ent_product_verisilicon_vip9000` -- `uses` --> `ent_component_verisilicon_vip9000_npu`

## Application Scenarios

- **Robotics Edge Perception**: Integrated into robot SoCs for vision, voice, and multimodal AI inference.
- **Smart Automotive ADAS**: Used in front-view, surround-view, and in-cabin perception systems.
- **Smart Security and AIoT**: Supports efficient AI vision for IPCs, doorbells, and wearable devices.

## Competitive Comparison

| Comparison Item | VeriSilicon VIP9000 | ARM Ethos | Synopsys ARC NPU |
|----------------|---------------------|-----------|------------------|
| Type | NPU IP | NPU IP | NPU IP |
| Configurability | High | Medium | High |
| Ecosystem Synergy | ISP/GPU/Video IP synergy | ARM ecosystem | Synopsys ecosystem |
| Licensing Model | IP licensing | IP licensing | IP licensing |

## Selection and Deployment Recommendations

- Select VIP9000 configuration and bus interface based on target model, performance, and power budget.
- Evaluate the adaptation of model quantization and compilation toolchains to the target network.
- It is recommended to obtain IP evaluation packages, reference designs, and technical support through VeriSilicon's official channels.

## Related Entries

- [Manufacturer: VeriSilicon](../companies/company_verisilicon.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [VeriSilicon Official Website](https://www.verisilicon.com)
2. [VeriSilicon AI Processor IP](https://www.verisilicon.com/IPPortfolio/Artificial-Intelligence-IP.html)
3. VeriSilicon 2024 Annual Report
