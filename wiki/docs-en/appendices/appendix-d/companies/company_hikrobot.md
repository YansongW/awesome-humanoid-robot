# Hikrobot

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 海康机器人 |
| **English Name** | Hikrobot |
| **Headquarters** | Hangzhou, China |
| **Founded** | 2014 (subsidiary of Hikvision) |
| **Website** | [https://www.hikrobotics.com](https://www.hikrobotics.com) |
| **Supply Chain Segment** | Industrial cameras, machine vision, mobile robots, RGB-D perception cameras |
| **Enterprise Attribute** | Controlled subsidiary of Hikvision, machine vision and mobile robot solution provider |
| **Parent Company/Group** | Hangzhou Hikvision Digital Technology Co., Ltd. |
| **Data Source** | Official website, product datasheets, public financial reports |

## Company Profile

Hikrobot is a globally leading provider of machine vision and mobile robot products and solutions, with product lines covering industrial cameras, smart cameras, 3D perception, and AMRs.

Leveraging its parent company's expertise in image sensing, ISP, and AI algorithms, Hikrobot offers industrial area/line scan cameras, smart cameras, RGB-D stereo cameras, laser galvanometer 3D cameras, and mobile robots. Its products are widely used in industrial inspection, positioning and guidance, logistics sorting, and smart manufacturing.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Industrial Cameras | Area/line scan industrial cameras | MV-CA / MV-CS / MV-CH series | Inspection, identification, positioning |
| RGB-D / Perception Cameras | Depth perception and navigation | MV-EB / MV-DB / MV-DLS series | Robot obstacle avoidance, grasping, AMR navigation |
| Mobile Robots | AGV/AMR | Towing, forklift, transfer series | Warehouse logistics, smart manufacturing |

## Representative Products

### Hikrobot MV-EB435i

> Hikrobot MV-EB435i: Please visit [official documentation](https://www.hikrobotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 91 mm × 26 mm × 31 mm | Distributor datasheet |
| Weight | Approx. 170 g | Distributor datasheet |
| Depth Technology | Binocular perception camera | Official datasheet |
| FOV | 84° × 55° | Distributor datasheet |
| Near/Far Field of View | 310×210 mm / 9200×5200 mm | Distributor datasheet |
| Clearance Distance/Measurement Range | 200 mm / 4800 mm | Distributor datasheet |
| Depth Map Detection Accuracy | 1.5% @ 0.2 m – 3 m | Distributor datasheet |
| Resolution | 1280×720 @ 30 fps / 640×360 @ 30 fps | Distributor datasheet |
| Interface | USB 3.0 (compatible with USB 2.0) | Distributor datasheet |
| Typical Power Consumption | 4.5 W @ 5 VDC | Distributor datasheet |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Compact size, wide field of view, USB powered, adaptable to multiple environments, suitable for mobile robot perception and obstacle avoidance.

**Application Scenarios**: AMR/AGV obstacle avoidance, spatial scanning, object recognition, robot positioning and guidance.

### Hikrobot MV-DB500S-S

> Hikrobot MV-DB500S-S: Please visit [official documentation](https://www.hikrobotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 200 mm × 47 mm × 100 mm | Product catalog |
| Weight | Approx. 1 kg | Distributor datasheet |
| Depth Technology | RGB-D intelligent binocular stereo camera | Product catalog |
| Near/Far Field of View | 580×470 mm / 2500×1800 mm | Product catalog |
| Clearance Distance/Measurement Range | 500 mm / 1500 mm | Product catalog |
| Depth Map Detection Accuracy | X,Y,Z: 5 mm @ 1 m; 10 mm @ 2 m | Product catalog |
| Scan Frame Rate | Up to 30 fps (single-item separation mode) | Product catalog |
| Interface | Gigabit Ethernet + 12-pin M12 | Product catalog |
| Power Supply | 12 – 24 VDC | Product catalog |
| Protection Rating | IP65 | Product catalog |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Built-in deep learning algorithms, RGB-D synchronous output, large field of view, IP65 protection, suitable for logistics and warehouse automation.

**Application Scenarios**: Parcel single-item separation, package grasping, volume measurement, automated loading/unloading.

## Supply Chain Position

- **Upstream Key Components/Materials**: CMOS image sensors, ISP chips, lasers, optical lenses, main control SoCs, motor drivers
- **Downstream Customers/Application Scenarios**: 3C/semiconductor manufacturing, automotive, lithium battery, logistics warehousing, AMR/AGV, humanoid robot perception modules
- **Main Competitors/Peers**: Orbbec, PerceptIn, Basler, Cognex, Daheng Image

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_hikrobot`
- Product Entity: `ent_component_hikrobot_mv_eb435i`
- Product Entity: `ent_component_hikrobot_mv_db500s_s`
- Key Relationships:
  - `ent_company_hikrobot` -- `manufactures` --> `ent_component_hikrobot_mv_eb435i`
  - `ent_company_hikrobot` -- `manufactures` --> `ent_component_hikrobot_mv_db500s_s`

## References

1. [Official Website](https://www.hikrobotics.com)
2. [Product Documentation and Public Reports](https://www.hikrobotics.com)
3. [Appendix D Product Catalog](../index-products.md)
