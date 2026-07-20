# Moore Threads

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 摩尔线程 |
| **English Name** | Moore Threads |
| **Headquarters** | Beijing, China |
| **Founded** | 2020 |
| **Official Website** | [https://www.moorethreads.com](https://www.moorethreads.com) |
| **Supply Chain Role** | Full-function GPU, AI Computing, Graphics Rendering, Domestic Computing Power, Metaverse |
| **Company Type** | Unicorn, Domestic Full-function GPU Enterprise |
| **Parent Company/Group** | None (Independent Entity) |
| **Data Source** | Moore Threads Official Website, Product Launch Events, Public Press Releases, Industry Research Reports |

## Company Overview

Moore Threads is dedicated to the development of full-function GPUs, providing graphics rendering, AI computing, and video encoding/decoding capabilities, and building a domestic GPU software and hardware ecosystem.

Moore Threads is a representative enterprise of China's full-function GPU sector, launching the MTT S series of desktop and data center GPUs. It supports DirectX, Vulkan, OpenGL, CUDA compatibility, and AI frameworks. The company emphasizes the integration of graphics and computing, providing computing power for cloud gaming, AI inference, digital twins, and the metaverse.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Desktop GPU | Consumer/Workstation Graphics | MTT S80 / S70 | Gaming, Design, Office |
| Data Center GPU | AI Inference & Cloud Rendering | MTT S3000 / S4000 | Intelligent Computing Centers, Cloud Gaming, AIGC |
| Software Ecosystem | Drivers & Development Tools | MUSA / MTTensor | AI Frameworks, Graphics Applications |

## Representative Products

### Moore Threads MTT S80

> Moore Threads MTT S80: Please visit [Official Documentation](https://www.moorethreads.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Architecture | MUSA (Moore Threads Unified System Architecture) | Moore Threads Official Website |
| Process Node | Not disclosed | - |
| Memory | 16 GB GDDR6 | Moore Threads Official Website |
| Interface | PCIe Gen5 | Moore Threads Official Website |
| Graphics API | DirectX, Vulkan, OpenGL | Moore Threads Official Website |
| AI Compute | Not disclosed | - |
| Video Codec | Supports AV1, H.265, H.264 | Moore Threads Official Website |
| Price | Approx. 2999 RMB (Reference Price) | Public Reports |

**Technical Highlights**: Domestic gaming/graphics GPU, PCIe Gen5, support for mainstream graphics APIs and video codecs, MUSA software ecosystem.

**Application Scenarios**: Desktop gaming, graphic design, video editing, lightweight AI inference.

### Moore Threads MTT S4000

> Moore Threads MTT S4000: Please visit [Official Documentation](https://www.moorethreads.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Architecture | MUSA | Moore Threads Official Website |
| Positioning | Data Center Full-function GPU | Moore Threads Official Website |
| Memory | 48 GB (Public Reports) | Public Reports |
| AI Compute | FP32/TF32/INT8 Multi-precision | Moore Threads Public Documentation |
| Graphics Rendering | Supports Cloud Gaming, Digital Twins | Moore Threads Official Website |
| Video | Multi-channel Video Codec | Moore Threads Public Documentation |
| Interface | PCIe | Public Reports |
| Price | Not disclosed | - |

**Technical Highlights**: Data center-grade domestic GPU, integration of graphics/AI/video, adapted for cloud gaming and AIGC inference scenarios.

**Application Scenarios**: Intelligent computing centers, cloud gaming, AIGC inference, digital twins, metaverse.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, GDDR/HBM memory, packaging and testing, EDA, graphics/compute IP, server manufacturers.
- **Downstream Customers/Application Scenarios**: Gamers, design studios, cloud service providers, intelligent computing centers, AIGC enterprises.
- **Main Competitors/Peers**: NVIDIA GeForce/RTX, AMD Radeon, Intel Arc; domestic peers include Biren Technology, Muxi.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_moore_threads`
- Product Entities: `ent_product_moore_threads_s80`, `ent_product_moore_threads_s4000`
- Key Relationships:
  - `ent_company_moore_threads` -- `manufactures` --> `ent_product_moore_threads_s80`
  - `ent_company_moore_threads` -- `manufactures` --> `ent_product_moore_threads_s4000`
  - `ent_product_moore_threads_s80` -- `uses` --> `ent_component_gddr6_memory`
  - `ent_product_moore_threads_s4000` -- `uses` --> `ent_component_pcie_interface`

## References

1. [Official Website](https://www.moorethreads.com)
2. [Moore Threads Official Website](https://www.moorethreads.com)
3. Moore Threads Product Launch Materials
