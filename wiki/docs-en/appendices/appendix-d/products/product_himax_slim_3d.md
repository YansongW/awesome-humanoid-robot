# Himax SLiM 3D Sensing Module

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Himax Technologies](../companies/company_himax.md) |
| **Product Category** | Structured Light 3D Sensing Module |
| **Release Date** | Commercial since 2018 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Himax SLiM 3D Sensing Module Product/Info Page](https://www.himax.com.tw/products/structured-light-sensing/) |

## Product Overview

SLiM (Structured Light Module) is a structured light 3D sensing total solution launched by Himax Technologies. It integrates an infrared projector, WLO optical elements, and a receiving sensor to achieve high-precision, low-power 3D depth perception. Its miniaturized design makes it suitable not only for smartphone face unlock but also for robot close-range obstacle avoidance, gesture recognition, and object grasping guidance.

## Product Image

> Himax SLiM 3D Sensing Module: Please visit the [official page](https://www.himax.com.tw/products/structured-light-sensing/) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Structured Light 3D Sensing Module | Official Website/Press Release |
| Depth Technology | Structured Light / Active Infrared Projection | Official Website/Press Release |
| Depth Resolution | VGA level (640 × 480) @ 30 fps | Official Website/Press Release |
| Field of View | Horizontal approx. 67° (typical) | Official Website/Press Release |
| Working Distance | Approx. 0.3 m – 1.0 m | Official Website/Press Release |
| Depth Accuracy | Not disclosed | - |
| Dimensions | Miniaturized module (specifics not disclosed) | Official Website/Press Release |
| Power Consumption | Not disclosed | - |
| Interface | MIPI / USB2.0 (varies by solution) | Official Website/Press Release |
| Emitter | VCSEL / EEL + WLO DOE | Official Website/Press Release |
| Receiver | NIR Enhanced CMOS / ToF | Official Website/Press Release |
| Operating Temperature | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Himax Technologies](../companies/company_himax.md)
- **Core Components/Technology Source**: In-house WLO diffractive optical elements, infrared projector, NIR CMOS receiver, depth algorithm ASIC, module packaging.
- **Downstream Applications/Customers**: Smartphone OEMs, robot integrators, AR/VR device manufacturers, smart lock/access control vendors, payment terminal manufacturers.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_himax_slim_3d`
- Component Entity: `ent_component_himax_slim_3d_module`
- Manufacturer Entity: `ent_company_himax`
- Key Relationships:
  - `rel_ent_company_himax_manufactures_ent_product_himax_slim_3d` (`ent_company_himax` → `manufactures` → `ent_product_himax_slim_3d`)
  - `rel_ent_company_himax_manufactures_ent_component_himax_slim_3d_module` (`ent_company_himax` → `manufactures` → `ent_component_himax_slim_3d_module`)
  - `rel_ent_product_himax_slim_3d_uses_ent_component_himax_slim_3d_module` (`ent_product_himax_slim_3d` → `uses` → `ent_component_himax_slim_3d_module`)

## Application Scenarios

- **Robot Obstacle Avoidance and Grasping**: Close-range high-precision depth maps assist robotic arm path planning.
- **Face Recognition and Payment**: Structured light liveness detection enhances security levels.
- **AR/VR Gestures**: Low-latency hand tracking and interaction.
- **3D Scanning**: Miniaturized module for handheld or fixed 3D reconstruction.

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | Structured Light 3D Module | Orbbec Gemini 335 | Intel RealSense D435i |
| Depth Technology | Structured Light | Active + Passive Stereo | Active Infrared Stereo |
| Optimal Range | 0.3–1.0 m | 0.1–20 m+ | 0.3–10 m |
| Core Advantage | WLO miniaturization, payment-grade security | Outdoor strong light, MX6800 ASIC | Mature ecosystem, ROS support |

## Selection and Deployment Recommendations

- Select the specific model based on the target application's resolution, range, accuracy, or computing power requirements.
- Confirm interface, power supply, heat dissipation, mechanical installation, and ambient temperature range compatibility before deployment.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Himax Technologies](../companies/company_himax.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Himax Technologies Official Website](https://www.himax.com.tw)
2. [Himax SLiM 3D Sensing Module Product/Info Page](https://www.himax.com.tw/products/structured-light-sensing/)
3. Product datasheets and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
