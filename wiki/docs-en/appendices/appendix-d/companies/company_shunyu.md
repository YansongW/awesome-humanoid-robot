# Sunny Optical

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 舜宇光学 |
| **English Name** | Sunny Optical |
| **Headquarters** | Ningbo, Zhejiang, China (Headquarters), Listed in Hong Kong |
| **Founded** | 1984 |
| **Official Website** | [https://www.sunnyoptical.com](https://www.sunnyoptical.com) |
| **Supply Chain Role** | Optical lenses, camera modules, automotive vision, robot vision, LiDAR optical components |
| **Company Type** | Listed Company (HKEX: 2382), Global Leading Comprehensive Optical Manufacturer |
| **Parent Company/Group** | Independently Listed |
| **Data Source** | Sunny Optical official website, annual reports, public product materials |

## Company Profile

Sunny Optical Technology (Sunny Optical) is a globally leading comprehensive optical component and product manufacturer, with business covering terminals such as mobile phones, automobiles, security surveillance, robotics, and AR/VR. The company possesses one-stop R&D and manufacturing capabilities from optical lenses and lens assemblies to camera modules, and is deeply involved in 3D ToF, structured light, and panoramic vision modules required for robot vision.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Smartphone Camera Module | Mid-to-high-end Imaging Module | COB/COF High-definition Module | Mobile phones, Tablets |
| Automotive Camera Module | ADAS/Intelligent Cockpit Vision | Front-view/Surround-view/In-cabin Monitoring Module | Smart Vehicles |
| Robot/IoT Vision Module | 3D ToF, Structured Light, Panoramic Vision | Robot Guidance and Obstacle Avoidance Module | Service/Industrial Robots |
| LiDAR Optical Components | Transmitter/Receiver Lenses and Scanning Modules | LiDAR Lenses, RX/TX Modules | Autonomous Driving, Robotics |

## Representative Products

### Sunny Optical Automotive/Robot Camera Module

> Sunny Optical Automotive/Robot Camera Module: Please visit [Official Materials](https://www.sunnyoptical.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Type | Automotive-grade Camera Module | Official Product Materials |
| Resolution | 2MP / 3MP / 8MP Multiple Models | Official Product Materials |
| Sensor | 1/2.7" – 1/2.3" CMOS | Official Product Materials |
| Field of View | 30° – 120° (Varies by Model) | Official Product Materials |
| Lens | Glass-plastic Hybrid High-resolution Lens | Official Product Materials |
| Interface | GMSL2 / FPD-Link III / Coaxial | Official Product Materials |
| Frame Rate | Up to 60 fps (Varies by Resolution and Interface) | Official Product Materials |
| Protection Rating | IP67 / IP69K | Official Product Materials |
| Operating Temperature | -40℃ – +85℃ | Official Product Materials |
| Power Supply | 12 V DC (Typical) | Official Product Materials |
| Weight | Approx. 50 – 150 g | Official Product Materials |
| Price | Not Disclosed | - |

**Technical Highlights**: Sunny Optical's self-developed lens + module integrated design, automotive-grade reliability, supports high-speed long-distance transmission, suitable for robot vision, ADAS, and in-cabin monitoring scenarios.

**Application Scenarios**: Humanoid robot/service robot visual guidance, autonomous driving perception, intelligent cockpit DMS/OMS, industrial inspection.

### Sunny Optical LiDAR Scanning/Receiving Module

> Sunny Optical LiDAR Scanning/Receiving Module: Please visit [Official Materials](https://www.sunnyoptical.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Type | LiDAR Scanning/Receiving Optical Module | Sunny Automotive Official Website |
| Solution | Mechanical/MEMS/3D Flash/OPA | Sunny Automotive Official Website |
| Application | Autonomous Driving, Robot Obstacle Avoidance | Sunny Automotive Official Website |
| Price | Not Disclosed | - |

**Technical Highlights**: Covers multiple LiDAR technology routes, providing integrated solutions for transmitter/receiver lenses and scanning modules.

**Application Scenarios**: Autonomous driving perception, robot navigation, surveying and mapping.

## Supply Chain Position

- **Upstream Key Components/Materials**: CMOS Image Sensor, Optical Lens, Voice Coil Motor, FPC/PCB, ISP Chip, Structural Parts
- **Downstream Customers/Application Scenarios**: Smartphone OEMs, Automotive OEMs/Tier1, Robot Manufacturers, AR/VR Manufacturers
- **Main Competitors/Peers**: O-Film, Q Technology, LG Innotek, Samsung Electro-Mechanics, Largan Precision

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_shunyu`
- Product Entity: `ent_product_shunyu_automotive_camera_module`
- Component Entity: `ent_component_shunyu_camera_module_core`
- Key Relationships:
  - `ent_company_shunyu` -- `manufactures` --> `ent_product_shunyu_automotive_camera_module`
  - `ent_company_shunyu` -- `manufactures` --> `ent_component_shunyu_camera_module_core`
  - `ent_product_shunyu_automotive_camera_module` -- `uses` --> `ent_component_shunyu_camera_module_core`

## References

1. [Sunny Optical Official Website](https://www.sunnyoptical.com)
2. [Sunny Optical Automotive/Robot Camera Module Product/Materials Page](https://www.sunnyoptical.com/en/pro/009017006/index.html)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
