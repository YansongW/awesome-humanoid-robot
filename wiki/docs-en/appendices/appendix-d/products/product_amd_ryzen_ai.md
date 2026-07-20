# AMD Ryzen AI (Integrated XDNA NPU)

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [AMD / Advanced Micro Devices](../companies/company_amd.md) |
| **Product Category** | On-Device AI PC / Embedded AI Processor |
| **Release Date** | Ryzen AI series released iteratively with Ryzen processors |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | AMD Official Website, Ryzen AI Product Page |

## Product Overview

AMD Ryzen AI is a dedicated AI computing engine integrated into AMD Ryzen processors, based on the XDNA architecture NPU, providing high-efficiency AI inference capabilities for AI PCs, edge devices, and robotic endpoints.

Ryzen AI integrates Zen CPU, RDNA GPU, and XDNA NPU into a single SoC, supporting Windows AI, ONNX Runtime, and various on-device AI frameworks. Its 15–54 W power range covers laptops, mini PCs, edge boxes, and robot controllers, making it suitable for running on-device AI tasks such as VLM, speech recognition, and real-time vision.

## Product Image

> AMD Ryzen AI: Please visit [Official Materials](https://www.amd.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Processor | AMD Ryzen AI 300 Series | AMD Official Website |
| Architecture | Zen 5 CPU + RDNA GPU + XDNA NPU | AMD Public Information |
| Process Node | 4 nm | Public Reports |
| NPU Compute | Up to ~55 TOPS INT8 | AMD Public Information |
| CPU Cores | Up to 12 Zen 5 Cores | AMD Public Information |
| GPU | RDNA 3.5 Integrated Graphics | AMD Public Information |
| Memory | Supports LPDDR5X / DDR5 | AMD Public Information |
| Interfaces | USB4, PCIe, DP/HDMI, etc. | AMD Public Information |
| Power Consumption | ~15–54 W | Public Reports |
| Price | Depends on OEM System | - |

## Supply Chain Position

- **Manufacturer**: [AMD / Advanced Micro Devices](../companies/company_amd.md)
- **Core Components/Technology Sources**: TSMC foundry, self-developed XDNA NPU, LPDDR5X/DDR5 memory, motherboard/PCB, cooling.
- **Downstream Applications/Customers**: OEM PC manufacturers, edge device vendors, industrial automation, robot integrators, developers.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_amd_ryzen_ai`
- Component Entity: `ent_component_amd_ryzen_ai_npu`
- Manufacturer Entity: `ent_company_amd`
- Key Relationships:
  - `rel_ent_company_amd_manufactures_ent_product_amd_ryzen_ai` (`ent_company_amd` → `manufactures` --> `ent_product_amd_ryzen_ai`)
  - `rel_ent_company_amd_manufactures_ent_component_amd_ryzen_ai_npu` (`ent_company_amd` → `manufactures` --> `ent_component_amd_ryzen_ai_npu`)
  - `ent_product_amd_ryzen_ai` -- `uses` --> `ent_component_amd_ryzen_ai_npu`

## Application Scenarios

- **AI PC and Edge Boxes**: Running local large models, speech recognition, real-time translation, and vision applications.
- **Robotic On-Device Controller**: Serving as the robot's cerebellum/on-device brain for perception, navigation, and human-machine interaction.
- **Industrial HMI and Edge Gateway**: Providing graphics rendering, AI inference, and multi-device connectivity.

## Competitive Comparison

| Comparison Item | AMD Ryzen AI | Intel Core Ultra | Qualcomm Snapdragon X |
|-----------------|--------------|------------------|------------------------|
| NPU Architecture | XDNA | NPU (Meteor/Lunar Lake) | Hexagon NPU |
| Compute | Up to 55 TOPS | Up to ~48 TOPS | Up to ~45 TOPS |
| Ecosystem | Windows AI / ONNX | Windows AI / ONNX | Windows on ARM |
| Integration | CPU+GPU+NPU | CPU+GPU+NPU | CPU+GPU+NPU |

## Selection and Deployment Recommendations

- Choose H/HS/U series models based on power consumption and form factor; confirm driver support for the XDNA NPU in the target framework.
- When deploying robotic solutions, evaluate I/O interfaces, real-time performance, and thermal design.
- It is recommended to obtain the latest drivers, Ryzen AI SDK, and technical support through AMD official channels or OEMs.

## Related Entries

- [Manufacturer: AMD / Advanced Micro Devices](../companies/company_amd.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [AMD Official Website](https://www.amd.com)
2. [AMD Ryzen AI Product Page](https://www.amd.com/en/processors/ryzen-ai)
3. AMD Ryzen AI Developer Guide
