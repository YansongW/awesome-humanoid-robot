# Rokoko Smartsuit Pro II

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Rokoko](../companies/company_rokoko.md) |
| **Product Category** | Inertial Motion Capture Suit |
| **Release Date** | Released October 2021 |
| **Status** | Commercial |
| **Official Website/Source** | [Rokoko Official Website](https://rokoko.com) |

## Product Overview

The Rokoko Smartsuit Pro II is Rokoko's second-generation full-body inertial motion capture suit, targeting independent creators, game studios, film and television production, sports science, and robotics research. The suit connects via Wi-Fi to the free Rokoko Studio software, enabling real-time recording, cleaning, editing, and streaming of motion data to mainstream 3D tools such as Unreal Engine, Unity, Blender, Maya, and MotionBuilder.

Compared to the first generation, the Smartsuit Pro II features significant improvements in drift suppression, high-impact motion stability, multi-level tracking (stairs/ladders/vertical movement), and integration with Smartgloves hand tracking. Its 17–19 9-DOF IMU sensors, 200 fps streaming, and approximately 6-hour battery life make it a representative high-value professional motion capture solution.

In the robotics field, the Smartsuit Pro II can be used to capture natural human motion data, providing motion references and training data for humanoid robots, digital humans, and embodied intelligence models.

## Product Image

> Rokoko Smartsuit Pro II: Please visit the [official website](https://rokoko.com) for details.

## Specifications Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Sensors | 17× or 19× 9-DOF IMU | Rokoko Official Website |
| 3D Orientation Accuracy | ±1° | Rokoko Public Specifications |
| Sampling/Streaming | 200 fps | Rokoko Public Specifications |
| Accelerometer Range | 16 g | Rokoko Public Specifications |
| Wireless Connectivity | Wi-Fi (up to approx. 100 m) | Rokoko Public Specifications |
| Battery Life | Approx. 6 hours | Rokoko Public Specifications |
| Suit Sizes | S / M / L / XL | Rokoko Official Website |
| Fabric | Washable Nylon/Elastic Fabric | Rokoko Public Specifications |
| Price | Starting from approx. 2,745 USD | Public Quotation |

## Supply Chain Position

- **Manufacturer**: [Rokoko](../companies/company_rokoko.md)
- **Core Components/Technology Sources**: MEMS IMU sensors, Wi-Fi modules, wearable textiles, lithium batteries, sensor fusion algorithm chips, Rokoko Studio software.
- **Downstream Applications/Customers**: Independent animators, game studios (Ubisoft, EA, etc.), film/TV VFX, sports science research institutions, robotics/humanoid robot companies.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_rokoko_smartsuit_pro_ii`
- Manufacturer Entity: `ent_company_rokoko`
- Key Relationships:
  - `rel_ent_company_rokoko_manufactures_ent_product_rokoko_smartsuit_pro_ii` (`ent_company_rokoko` → `manufactures` → `ent_product_rokoko_smartsuit_pro_ii`)

## Application Scenarios

- **Film/TV and Game Animation**: Real-time character driving, rapid generation of high-quality animation.
- **Virtual Streaming / VTubing**: Low-latency driving of virtual avatars.
- **Sports Biomechanics**: Analyzing athlete movements, postures, and force application patterns.
- **Robot Motion Reference**: Capturing natural motion data for humanoid robots, used for imitation learning and motion planning.

## Competitive Comparison

| Comparison Item | Rokoko Smartsuit Pro II | Xsens MVN Link | Noitom Perception Neuron |
|----------------|------------------------|----------------|--------------------------|
| Positioning | High-value professional inertial mocap | High-end professional inertial mocap | Entry-level inertial mocap |
| Sensors | 17–19× 9-DOF IMU | 17× wired IMU | Fewer IMUs |
| Update Rate | 200 fps | Up to 240 Hz | Lower |
| Price | Starting from approx. 2,745 USD | Enterprise inquiry | Starting from approx. 1,500 USD |
| Software Ecosystem | Rokoko Studio (free basic version) | MVN Analyze/Animate | Proprietary software |

## Selection and Deployment Recommendations

- Suitable for teams with limited budgets requiring professional full-body motion capture, especially independent creators and small to medium-sized studios.
- For high-impact motion or vertical movement capture, ensure the firmware is the latest version supporting multi-level tracking.
- When used for robot data collection, additional calibration of skeleton proportions is required, and export to common formats such as BVH/FBX/CSV is recommended.

## References

1. [Rokoko Official Website](https://rokoko.com)
2. [CGW – Rokoko Smartsuit Pro II Launch](https://www.cgw.com/Press-Center/News/2021/Rokoko-Launches-the-Next-Gen-Smartsuit-Pro-II.aspx)
3. [Animation Xpress – Rokoko Smartsuit Pro II](https://www.animationxpress.com/latest-news/motion-capture-company-rokoko-launches-smartsuit-pro-ii/)
4. [Rokoko Studio Download Page](https://rokoko.com/studio)
