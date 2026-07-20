# Hailo-8 AI Processor

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Hailo](../companies/company_hailo.md) |
| **Product Category** | Edge AI Accelerator / NPU |
| **Release Date** | Hailo-8 released in 2019 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | Hailo official website, product manual |

## Product Overview

Hailo-8 is an edge AI processor launched by Hailo, featuring an innovative Dataflow Architecture that achieves high AI computing power at low power consumption. It is widely used in robotics, automotive, security, and industrial vision.

Hailo-8 is available in BGA package, M.2 module, or PCIe card form, allowing direct integration into existing embedded platforms. Its dataflow architecture is deeply optimized for neural network inference, offering superior computing power utilization and energy efficiency compared to traditional SIMD/GPU solutions. It is suitable for multi-channel video analysis, real-time object detection, and robotic edge perception.

## Product Image

> Hailo-8 AI Processor: Please visit the [official website](https://hailo.ai) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| AI Processor | Hailo-8 | Hailo official website |
| Architecture | Dataflow Architecture | Hailo public information |
| Process Node | 16 nm | Public reports |
| AI Computing Power | Up to 26 TOPS INT8 | Hailo public information |
| Energy Efficiency | Approx. 3 TOPS/W typical | Hailo public information |
| Precision Support | INT8 / INT4 / FP16 (partial) | Hailo public information |
| Package Size | Approx. 15 mm × 15 mm (BGA) | Hailo public information |
| Interface | PCIe Gen3 / M.2 / BGA | Hailo public information |
| Power Consumption | Approx. 2.5 W typical | Hailo public information |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Hailo](../companies/company_hailo.md)
- **Core Components/Technology Source**: Self-developed dataflow architecture, wafer foundry, packaging and testing, modules/carrier boards.
- **Downstream Applications/Customers**: Automotive Tier1/OEM, security vendors, industrial camera companies, robot integrators, AIoT device manufacturers.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_hailo_8`
- Component Entity: `ent_component_hailo_8_npu`
- Manufacturer Entity: `ent_company_hailo`
- Key Relationships:
  - `rel_ent_company_hailo_manufactures_ent_product_hailo_8` (`ent_company_hailo` → `manufactures` --> `ent_product_hailo_8`)
  - `rel_ent_company_hailo_manufactures_ent_component_hailo_8_npu` (`ent_company_hailo` → `manufactures` --> `ent_component_hailo_8_npu`)
  - `ent_product_hailo_8` -- `uses` --> `ent_component_hailo_8_npu`

## Application Scenarios

- **Robotic Edge Perception**: Real-time object detection, semantic segmentation, pose estimation, and navigation assistance.
- **Smart Security Cameras**: Edge video analysis and event detection.
- **Automotive ADAS**: Front-view/surround-view perception, in-cabin monitoring, and low-latency inference.

## Competitive Comparison

| Comparison Item | Hailo-8 | Intel Movidius VPU | Horizon Journey 3 |
|----------------|---------|--------------------|-------------------|
| Computing Power | 26 TOPS | Approx. 4 TOPS | Approx. 5 TOPS |
| Power Consumption | Approx. 2.5 W | Approx. 1 W | Approx. 2.5 W |
| Architecture | Dataflow | VPU / SHAVE | Self-developed BPU |
| Ecosystem | Hailo SDK | OpenVINO | Horizon OpenExplorer |

## Selection and Deployment Recommendations

- Prioritize using the Hailo Dataflow Compiler to evaluate the performance and accuracy of target models on Hailo-8.
- Select M.2, PCIe, or BGA form factor based on the host interface, and confirm driver and BSP compatibility.
- It is recommended to obtain the latest SDK, reference designs, and technical support through Hailo's official channels.

## Related Entries

- [Manufacturer: Hailo](../companies/company_hailo.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Hailo Official Website](https://hailo.ai)
2. [Hailo-8 Product Page](https://hailo.ai/products/hailo-8/)
3. Hailo-8 Datasheet and Developer Documentation
