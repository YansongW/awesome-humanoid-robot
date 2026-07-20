# Vastai SV100 / Vastai SV100

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Vastai Technologies](../companies/company_vastai.md) |
| **Product Category** | Cloud AI Inference and Video Processing Accelerator Card |
| **Release Date** | SV100 series released with the company's product iteration |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | Vastai Technologies official website, product manual |

## Product Overview

The Vastai SV100 is a high-performance accelerator card designed for cloud AI inference and video understanding scenarios, integrating AI computing and video encoding/decoding capabilities, suitable for multimodal content processing.

Based on Vastai's self-developed AI and video processing architecture, the SV100 supports INT8/FP16 precision and can simultaneously process multiple high-definition video streams while running deep learning models. Its video+AI fusion feature gives it advantages in scenarios such as live transcoding, content moderation, smart security, and robotic vision backhaul.

## Product Image

> Vastai SV100: Please visit [Official Materials](https://www.vastai.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Accelerator | Vastai SV100 | Vastai Technologies official website |
| Architecture | Self-developed AI inference + video processing architecture | Vastai Technologies public materials |
| Process Node | 7 nm | Public reports |
| AI Compute | INT8 ~200 TOPS level | Vastai Technologies public materials |
| Memory | 32 GB LPDDR4X / HBM (depending on model) | Public reports |
| Video Capability | Multi-channel 4K/8K video encoding/decoding | Vastai Technologies public materials |
| Interface | PCIe Gen4 | Public reports |
| Power Consumption | ~75–150 W | Public reports |
| Software Stack | VastStream, SDK | Vastai Technologies public materials |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Vastai Technologies](../companies/company_vastai.md)
- **Core Components/Technology Sources**: Self-developed AI/video architecture, wafer foundry, memory, packaging and testing, PCB, cooling.
- **Downstream Applications/Customers**: Internet video platforms, cloud computing providers, telecom operators, smart cities, robotics companies.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_vastai_sv100`
- Component Entity: `ent_component_vastai_sv100_accelerator`
- Manufacturer Entity: `ent_company_vastai`
- Key Relationships:
  - `rel_ent_company_vastai_manufactures_ent_product_vastai_sv100` (`ent_company_vastai` → `manufactures` --> `ent_product_vastai_sv100`)
  - `rel_ent_company_vastai_manufactures_ent_component_vastai_sv100_accelerator` (`ent_company_vastai` → `manufactures` --> `ent_component_vastai_sv100_accelerator`)
  - `ent_product_vastai_sv100` -- `uses` --> `ent_component_vastai_sv100_accelerator`

## Application Scenarios

- **Cloud Video Understanding**: Real-time video analysis, content moderation, intelligent recommendations.
- **Live Streaming and Cloud Gaming**: High-density video transcoding and low-latency streaming.
- **Robotic Vision Backhaul**: Edge/cloud collaborative processing of multi-channel video data from robots.

## Competitive Comparison

| Comparison Item | Vastai SV100 | Cambricon MLU370 | NVIDIA T4 |
|----------------|--------------|------------------|-----------|
| Capability | AI + Video Fusion | AI Inference/Training | AI Inference |
| Video | Strong | Weak | Medium |
| Ecosystem | VastStream | Neuware | CUDA |
| Localization | Self-controlled | Self-controlled | Subject to export controls |

## Procurement and Deployment Recommendations

- Prioritize evaluating whether the number of video channels, resolution, and AI model concurrency requirements match the SV100's capabilities.
- Confirm VastStream's support for target video formats and model frameworks before deployment.
- It is recommended to obtain the latest drivers, SDKs, and reference solutions through Vastai Technologies' official channels.

## Related Entries

- [Manufacturer: Vastai Technologies](../companies/company_vastai.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Vastai Technologies Official Website](https://www.vastai.com)
2. [Vastai Technologies Product Page](https://www.vastai.com/products.html)
3. Vastai Technologies Product Launch Materials
