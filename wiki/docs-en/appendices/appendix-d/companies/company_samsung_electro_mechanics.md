# Samsung Electro-Mechanics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 三星电机 (Samsung Electro-Mechanics) |
| **English Name** | Samsung Electro-Mechanics |
| **Headquarters** | Suwon, Gyeonggi-do, South Korea |
| **Founded** | 1973 |
| **Website** | [https://www.samsungsem.com](https://www.samsungsem.com) |
| **Supply Chain Role** | Camera Module, MLCC, Printed Circuit Board, Inductor, RF Module |
| **Company Type** | Subsidiary of Samsung Electronics, Global leader in MLCC/Camera Modules |
| **Parent/Group** | Samsung Electronics (part of Samsung Group) |
| **Data Source** | Samsung Electro-Mechanics official website, annual reports, product press releases |

## Company Overview

Samsung Electro-Mechanics is a global leading supplier of camera modules, MLCCs, and substrates, providing key passive/optical components for smartphones, automobiles, and robots.

Samsung Electro-Mechanics, a subsidiary of Samsung Group, has core businesses including Camera Modules, Multilayer Ceramic Capacitors (MLCC), Printed Circuit Boards (PCB/HDI), and RF/Power Inductors. Its high-resolution camera modules, combining Samsung ISOCELL image sensors with high-precision optical structures, are widely used in flagship phones, automotive surround-view systems, and robot vision. MLCC and substrate products are fundamental passive components for robot controllers, joint drives, and power modules.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Camera Module | Smartphone/Automotive/Robotics | 200MP Main Camera Module / Telephoto / ToF | Mobile phones, Automotive, Robotics |
| MLCC | Multilayer Ceramic Capacitor | 0201 / 0402 / 0603 / 0805 | Automotive electronics, Robot control boards |
| Package Substrate | FC-BGA / FC-CSP | High-end computing & mobile AP substrates | SoC, AI chips |
| RF/Power Inductor | 5G/Communication Modules | Thin-film inductor / Wire-wound inductor | Communication, IoT |

## Representative Products

### Samsung Electro-Mechanics 200MP ISOCELL Camera Module

> Samsung Electro-Mechanics 200MP ISOCELL Camera Module: Please visit the [official page](https://www.samsungsem.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | High-resolution camera module | Website/Press release |
| Effective Pixels | 200 MP | Website/Press release |
| Optical Format | Approx. 1/1.3"–1/1.4" | Website/Press release |
| Pixel Size | Approx. 0.56 µm | Website/Press release |
| Lens | Multi-element plastic/glass hybrid lens | Website/Press release |
| Focus | VCM auto-focus | Website/Press release |
| Stabilization | Optional OIS | Website/Press release |
| Field of View | Not disclosed | - |
| Interface | MIPI D-PHY / C-PHY | Website/Press release |
| Module Size | Not disclosed | - |
| Power Consumption | Not disclosed | - |
| Operating Temperature | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Ultra-high pixel count, miniaturized module design, integrated VCM focus and OIS stabilization, fully leveraging ISOCELL's high resolution and multi-pixel binning low-light advantages.

**Application Scenarios**: Smartphone main camera, robot vision navigation, drone aerial photography, automotive surround view & ADAS, industrial inspection.

### Samsung Electro-Mechanics MLCC (Multilayer Ceramic Capacitor)

> Samsung Electro-Mechanics MLCC (Multilayer Ceramic Capacitor): Please visit the [official page](https://www.samsungsem.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Multilayer Ceramic Capacitor | Website |
| Size | 0201 / 0402 / 0603 / 0805, etc. | Website |
| Capacitance Range | Not disclosed | - |
| Voltage Rating | Not disclosed | - |
| Application | Automotive electronics, Robot control boards, Communication | Website |
| Price | Not disclosed | - |

**Technical Highlights**: High-reliability automotive-grade MLCC, suitable for robot joint drives, power filtering, and controller decoupling.

**Application Scenarios**: Robot controllers, automotive electronics, servers, communication equipment, consumer electronics.

## Supply Chain Position

- **Upstream Key Components/Materials**: Ceramic powder, internal electrode materials, image sensor wafers, optical lenses, VCM motors, PCB/FPC, package substrates
- **Downstream Customers/Applications**: Smartphone OEMs, Automotive Tier 1 suppliers, Robot integrators, Communication equipment manufacturers, Consumer electronics brands
- **Main Competitors/Peers**: Sony Semiconductor, OmniVision, LG Innotek, Sunny Optical, Q Technology, Murata, TDK, Yageo

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_samsung_electro_mechanics`
- Product Entity: `ent_product_samsung_electro_mechanics_200mp_camera_module`
- Component Entity: `ent_component_samsung_electro_mechanics_200mp_camera_module`
- Key Relationships:
  - `ent_company_samsung_electro_mechanics` -- `manufactures` --> `ent_product_samsung_electro_mechanics_200mp_camera_module`
  - `ent_company_samsung_electro_mechanics` -- `manufactures` --> `ent_component_samsung_electro_mechanics_200mp_camera_module`
  - `ent_product_samsung_electro_mechanics_200mp_camera_module` -- `uses` --> `ent_component_samsung_electro_mechanics_200mp_camera_module`

## References

1. [Samsung Electro-Mechanics Official Website](https://www.samsungsem.com)
2. [Samsung Electro-Mechanics 200MP ISOCELL Camera Module Product/Data Page](https://www.samsungsem.com/product/camera-module)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
