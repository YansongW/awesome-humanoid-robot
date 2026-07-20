# OFILM / OFILM

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 欧菲光 |
| **English Name** | OFILM |
| **Headquarters** | Shenzhen, Guangdong, China |
| **Founded** | 2002 |
| **Website** | [http://www.ofilm.com](http://www.ofilm.com) |
| **Supply Chain Role** | Camera modules, 3D ToF modules, fingerprint recognition, smart automotive electronics, machine vision |
| **Company Type** | Listed company (Shenzhen Stock Exchange: 002456), leading comprehensive optical and optoelectronic enterprise |
| **Parent Company/Group** | Independently listed |
| **Data Source** | OFILM official website, annual reports, public technical reports |

## Company Profile

OFILM Group is a leading Chinese manufacturer of precision optoelectronic thin-film components, specializing in camera modules, 3D depth sensing modules, fingerprint recognition modules, and smart automotive electronics. The company has complete vertical integration capabilities in 3D ToF, structured light, and high-pixel optical image stabilization modules, and is actively expanding into machine vision scenarios such as robotic vacuum cleaners and service robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Smartphone Camera Modules | High pixel / OIS / Periscope | MGL/CMP/GMP series | Phones, tablets |
| 3D Depth Sensing Modules | ToF / Structured light | D-ToF / I-ToF modules | Robotics, AR/VR, facial recognition |
| Fingerprint Recognition Modules | Optical / Ultrasonic under-display | Large-area ultrasonic fingerprint | Smartphones, smart locks |
| Smart Automotive Electronics | Vehicle cameras, millimeter-wave radar | ADAS modules, short-range radar | Smart vehicles |

## Representative Products

### OFILM 3D ToF Depth Camera Module

> OFILM 3D ToF Depth Camera Module: Please visit [Official Documentation](http://www.ofilm.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Time-of-flight 3D depth camera module | OFILM official website |
| Depth Resolution | VGA / QVGA (varies by model) | OFILM official website |
| RGB Resolution | Optional 2MP / 5MP | OFILM official website |
| Light Source | 940 nm VCSEL | OFILM official website |
| Field of View | 60°×45° / 70°×54° (typical) | OFILM official website |
| Range | 0.3 – 5 m | OFILM official website |
| Accuracy | Approx. 1% @ 1 m | OFILM official website |
| Frame Rate | Up to 30 fps | OFILM official website |
| Interface | MIPI / USB2.0 | OFILM official website |
| Power Supply | 3.3 V / 5 V DC | OFILM official website |
| Operating Temperature | -20°C – +70°C | OFILM official website |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: 940 nm infrared VCSEL + ToF sensor, real-time depth perception, supports RGB-D fusion, suitable for robot obstacle avoidance and spatial understanding.

**Application Scenarios**: Robotic vacuum cleaner obstacle avoidance, service robot navigation, AR/VR gestures, facial/biometric recognition, industrial 3D inspection.

### OFILM MGL High-Pixel Camera Module

> OFILM MGL High-Pixel Camera Module: Please visit [Official Documentation](http://www.ofilm.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | High-pixel smartphone camera module | Public technical reports |
| Pixel | 64MP / 108MP multiple models | Public technical reports |
| Features | Large aperture, optical image stabilization | Public technical reports |
| Price | Not disclosed | - |

**Technical Highlights**: High resolution, ultra-thin design, mass-produced and used in mainstream flagship models.

**Application Scenarios**: Smartphone main camera, multi-camera systems.

## Supply Chain Position

- **Upstream Key Components/Materials**: VCSEL, ToF image sensor, DOE/optical lens, ISP, PCB/FPC, structural parts
- **Downstream Customers/Application Scenarios**: Smartphones, intelligent robots, AR/VR, smart homes, automotive electronics
- **Main Competitors/Peers**: Sunny Optical, Q Technology, LG Innotek, Samsung Electro-Mechanics, ams Osram

## Knowledge Graph Nodes and Relationships

- Company entity: `ent_company_ofilm`
- Product entity: `ent_product_ofilm_tof_3d_module`
- Component entity: `ent_component_ofilm_tof_module_core`
- Key relationships:
  - `ent_company_ofilm` -- `manufactures` --> `ent_product_ofilm_tof_3d_module`
  - `ent_company_ofilm` -- `manufactures` --> `ent_component_ofilm_tof_module_core`
  - `ent_product_ofilm_tof_3d_module` -- `uses` --> `ent_component_ofilm_tof_module_core`

## References

1. [OFILM Official Website](http://www.ofilm.com)
2. [OFILM 3D ToF Depth Camera Module Product/Data Page](http://www.ofilm.com/en/products_inner1_39.html)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
