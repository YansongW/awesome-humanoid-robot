# Q-Tech / Q-Tech

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 丘钛科技 |
| **English Name** | Q-Tech |
| **Headquarters** | Kunshan, Jiangsu, China (operational headquarters), listed in Hong Kong |
| **Founded** | 2007 |
| **Official Website** | [https://www.qtechsmartvision.com](https://www.qtechsmartvision.com) |
| **Supply Chain Role** | Mid-to-high-end camera modules, fingerprint recognition modules, machine vision, automotive vision |
| **Company Type** | Listed company (HKEX: 01478), world's third-largest smartphone camera module packaging and testing enterprise |
| **Parent Company/Group** | Independently listed (Kunshan Q-Tech Microelectronics is a wholly-owned subsidiary) |
| **Data Source** | Q-Tech official website, prospectus, public product materials |

## Company Overview

Q-Tech is a globally leading manufacturer of mid-to-high-end camera modules and fingerprint recognition modules for smart mobile terminals, equipped with advanced packaging technologies such as COB, COF, MOB, and MOC. The company's products cover resolutions from 2 megapixels to 108 megapixels and actively expand into machine vision fields including automotive, drones, smart homes, and industrial robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Smartphone Camera Modules | Ultra-thin/OIS/Multi-camera | 200MP–108MP Series | Smartphones, Tablets |
| 3D Structured Light/Micro-Gimbal Modules | High-end Functional Modules | Structured Light, Micro-Gimbal | High-end Phones, Robots |
| Automotive/IoT Camera Modules | Automotive-grade Machine Vision | ADAS, Surround View, In-cabin Modules | Smart Cars, Drones |
| Fingerprint Recognition Modules | Capacitive/Optical/Under-display | Side/Under-display Fingerprint Modules | Smartphones, Smart Locks |

## Representative Products

### Q-Tech Machine Vision/Automotive Camera Module

> Q-Tech Machine Vision/Automotive Camera Module: Please visit [Official Materials](https://www.qtechsmartvision.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Machine Vision/Automotive-grade Camera Module | Q-Tech Official Website |
| Resolution | 2MP / 5MP / 8MP Multiple Models | Q-Tech Official Website |
| Sensor | 1/2.8" – 1/2.3" CMOS | Q-Tech Official Website |
| Shutter | Global Shutter / Rolling Shutter (Optional) | Q-Tech Official Website |
| Field of View | 120° / 140° / Custom | Q-Tech Official Website |
| Interface | MIPI / GMSL2 | Q-Tech Official Website |
| Protection Rating | IP67 (Automotive Models) | Q-Tech Official Website |
| Operating Temperature | -40℃ – +85℃ | Q-Tech Official Website |
| Power Supply | 12 V DC (Typical) | Q-Tech Official Website |
| Weight | Approx. 30 – 80 g | Q-Tech Official Website |
| Price | Not disclosed | - |

**Technical Highlights**: Advanced COB/COF/MOB packaging, automotive-grade reliability, support for global shutter and high-speed serial interfaces, meeting high-dynamic scenarios in robotics and automotive.

**Application Scenarios**: Industrial robot vision inspection, drone aerial photography, smart car surround view/front view, service robot SLAM.

### Q-Tech 3D Structured Light Module

> Q-Tech 3D Structured Light Module: Please visit [Official Materials](https://www.qtechsmartvision.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | 3D Structured Light Depth Module | Public Materials |
| Application | Facial Recognition, Robot Obstacle Avoidance | Public Materials |
| Feature | First to mass-produce domestically | Public Materials |
| Price | Not disclosed | - |

**Technical Highlights**: Highly integrated 3D structured light solution, supporting high-precision 3D reconstruction.

**Application Scenarios**: Phone Face ID, robot grasping, payment-grade facial recognition.

## Supply Chain Position

- **Upstream Key Components/Materials**: CMOS image sensors, lenses, voice coil motors, FPC, driver ICs, structural parts
- **Downstream Customers/Application Scenarios**: Smartphone OEMs, Automotive OEMs/Tier1, Drones, Robots, IoT Manufacturers
- **Main Competitors/Peers**: Sunny Optical, O-Film, LG Innotek, Samsung Electro-Mechanics, Shengtai Optoelectronics

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_qtech`
- Product Entity: `ent_product_qtech_machine_vision_camera_module`
- Component Entity: `ent_component_qtech_camera_module_core`
- Key Relationships:
  - `ent_company_qtech` -- `manufactures` --> `ent_product_qtech_machine_vision_camera_module`
  - `ent_company_qtech` -- `manufactures` --> `ent_component_qtech_camera_module_core`
  - `ent_product_qtech_machine_vision_camera_module` -- `uses` --> `ent_component_qtech_camera_module_core`

## References

1. [Q-Tech Official Website](https://www.qtechsmartvision.com)
2. [Q-Tech Machine Vision/Automotive Camera Module Product/Materials Page](https://www.qtechsmartvision.com/)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
