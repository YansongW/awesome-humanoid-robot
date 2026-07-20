# Vastai Technologies

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 瀚博半导体 |
| **English Name** | Vastai Technologies |
| **Headquarters** | Pudong New Area, Shanghai, China |
| **Founded** | 2018 |
| **Website** | [https://www.vastai.com](https://www.vastai.com) |
| **Supply Chain Role** | AI inference/video chips, cloud/edge AI computing, domestic computing power |
| **Company Type** | Unicorn, domestic AI chip company |
| **Parent Company/Group** | None (independent entity) |
| **Data Source** | Vastai Technologies official website, product launches, public press releases, industry research reports |

## Company Overview

Vastai Technologies is a Chinese company specializing in AI and video processing chip design, providing cloud-based AI inference and video acceleration solutions.

Vastai Technologies has launched the SV100 series cloud AI inference accelerator cards and the VA1 series video accelerator cards, featuring a self-developed VPU/AI architecture that emphasizes high throughput, low latency, low power consumption, and video scenario optimization. Its products are widely used in cloud computing, live video streaming, smart cities, content moderation, and large model inference.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| SV100 Series | Cloud AI inference accelerator cards | SV100 / SV200 series | Large model inference, CV, video analysis |
| VA1 Series | Video processing accelerator cards | VA1 | Video transcoding, live streaming, cloud gaming |
| Edge Solutions | Edge AI computing | Custom edge solutions | Edge boxes, robots |
| Software Stack | Chip enablement and development tools | VastStream / SDK | All series accelerator cards |

## Representative Products

### Vastai Technologies SV100

> Vastai Technologies SV100: Please visit the [official website](https://www.vastai.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Architecture | Self-developed AI inference architecture | Vastai Technologies public information |
| Process Node | 7 nm (public reports) | Public reports |
| Compute Power | INT8 ~200 TOPS level | Vastai Technologies public information |
| Memory | 32 GB LPDDR4X / HBM (varies by model) | Public reports |
| Video Capability | Supports multi-channel video encoding/decoding | Vastai Technologies public information |
| Interface | PCIe Gen4 | Public reports |
| Power Consumption | ~75–150 W | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: Video + AI integrated acceleration, high-concurrency video processing, low-latency inference, support for large models and multimodal applications.

**Application Scenarios**: Cloud video analysis, content moderation, live transcoding, large model inference, embodied intelligence perception.

### Vastai Technologies VA1

> Vastai Technologies VA1: Please visit the [official website](https://www.vastai.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Positioning | Video processing accelerator card | Vastai Technologies public information |
| Video Performance | Multi-channel 4K/8K video encoding/decoding | Vastai Technologies public information |
| Interface | PCIe Gen3/Gen4 | Public reports |
| Power Consumption | ~25–75 W | Public reports |
| Application Scenarios | Video cloud, live streaming, cloud gaming, security | Vastai Technologies public information |
| Software Stack | VastStream | Vastai Technologies public information |
| Price | Not disclosed | - |

**Technical Highlights**: High-density video transcoding, low power consumption, collaborative video understanding solutions with AI cards.

**Application Scenarios**: Video cloud, live streaming platforms, cloud gaming, smart security, robot vision feedback.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, memory, packaging and testing, EDA/IP, PCB, cooling.
- **Downstream Customers/Application Scenarios**: Internet video platforms, cloud computing providers, telecom operators, smart cities, robotics companies.
- **Main Competitors/Comparables**: NVIDIA T4/L4, Cambricon, Enflame Technology, Horizon Robotics, Intel Flex.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_vastai`
- Product Entity: `ent_product_vastai_sv100`
- Component Entity: `ent_component_vastai_sv100_accelerator`
- Key Relationships:
  - `ent_company_vastai` -- `manufactures` --> `ent_product_vastai_sv100`
  - `ent_company_vastai` -- `manufactures` --> `ent_component_vastai_sv100_accelerator`
  - `ent_product_vastai_sv100` -- `uses` --> `ent_component_vastai_sv100_accelerator`

## References

1. [Vastai Technologies Official Website](https://www.vastai.com)
2. [Vastai Technologies Product Page](https://www.vastai.com/products.html)
3. Vastai Technologies Product Launch Materials
