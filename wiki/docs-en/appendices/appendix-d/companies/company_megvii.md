# Megvii Technology / Megvii

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 旷视科技 |
| **English Name** | Megvii |
| **Headquarters** | Beijing, China |
| **Founded** | 2011 |
| **Official Website** | [https://www.megvii.com](https://www.megvii.com) |
| **Supply Chain Segment** | Computer Vision, AIoT, Logistics Robots, Embodied Intelligence, Large Models |
| **Enterprise Attribute** | Unicorn, One of the Four AI Dragons |
| **Parent Company/Group** | None (Independent Entity) |
| **Data Source** | Megvii Official Website, Prospectus, Public Press Releases, Industry Research Reports |

## Company Profile

Megvii Technology focuses on self-developed deep learning frameworks and computer vision technology, providing perception, decision-making, and execution solutions for AIoT and logistics robots.

Megvii is one of China's earliest AI unicorns, with its self-developed deep learning framework MegEngine. Its business covers Consumer IoT, Urban IoT, and Supply Chain IoT. In the robotics field, Megvii offers intelligent pallet four-way shuttles, AMRs, robotic arms, and the Hetu software platform, while exploring embodied intelligence and multimodal large model applications.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Smart Logistics | Warehouse and manufacturing logistics robots | Pallet four-way shuttle, AMR, robotic arm | Warehousing, Manufacturing, Retail |
| AIoT Platform | Perception and decision-making operating system | Hetu / Megvii Pangu | Buildings, Parks, Cities |
| Vision & Large Models | Computer vision and multimodal AI | MegEngine / Multimodal models | Robot perception, Industrial inspection |

## Representative Products

### Megvii Logistics Robots / Four-Way Shuttle & AMR

> Megvii Logistics Robots / Four-Way Shuttle & AMR: Please visit [Official Materials](https://www.megvii.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Intelligent pallet four-way shuttle, AMR, bin robot, robotic arm | Megvii Official Website |
| Load Range | Hundreds of kg to several tons (varies by model) | Public Information |
| Navigation Method | Laser SLAM / Visual SLAM / QR Code | Megvii Official Website |
| Scheduling System | Megvii Hetu | Megvii Official Website |
| Accuracy | Positioning accuracy ±5–±10 mm | Public Information |
| Speed | 1–2 m/s (varies by model) | Public Information |
| Communication | Wi-Fi / 5G | Megvii Official Website |
| Price | Not disclosed | - |

**Technical Highlights**: AI-driven logistics robots, integrated hardware-software solutions, Hetu intelligent scheduling, high-density storage, and flexible handling.

**Application Scenarios**: Smart warehousing, manufacturing logistics, retail distribution centers, cold chain logistics.

### Megvii MegEngine

> Megvii MegEngine: Please visit [Official Materials](https://www.megvii.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Domestic deep learning framework | Megvii Official Website |
| Core Features | Unified training and inference, dynamic/static graphs, edge-cloud support | MegEngine Documentation |
| Model Library | Pre-trained models for image classification, detection, segmentation, etc. | MegEngine Documentation |
| Deployment | Python/C++ / Mobile / Embedded | MegEngine Documentation |
| Open Source License | Apache 2.0 | GitHub |
| Community | Open source on GitHub | GitHub |
| Operator Support | Common CV/NLP operators | MegEngine Documentation |
| Price | Free and open source | GitHub |

**Technical Highlights**: Self-developed and controllable deep learning framework, optimized for computer vision, supports edge and embedded deployment.

**Application Scenarios**: Robot vision algorithms, industrial inspection, autonomous driving, smart terminals.

## Supply Chain Position

- **Upstream Key Components/Materials**: AI chips/servers, camera modules, LiDAR, reducers, motors, sensors.
- **Downstream Customers/Application Scenarios**: Logistics companies, manufacturing enterprises, retail companies, park/urban governance clients.
- **Main Competitors/Peers**: Hikrobot, Geek+, Quicktron, Hai Robotics; in vision, peers include SenseTime, CloudWalk.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_megvii`
- Product Entities: `ent_product_megvii_logistics_robot`, `ent_product_megvii_megengine`
- Key Relationships:
  - `ent_company_megvii` -- `manufactures` --> `ent_product_megvii_logistics_robot`
  - `ent_company_megvii` -- `manufactures` --> `ent_product_megvii_megengine`
  - `ent_product_megvii_logistics_robot` -- `uses` --> `ent_product_megvii_megengine`
  - `ent_product_megvii_logistics_robot` -- `uses` --> `ent_component_lidar_sensor`

## References

1. [Official Website](https://www.megvii.com)
2. [Megvii Official Website](https://www.megvii.com)
3. Megvii Technology Prospectus and Public Information
