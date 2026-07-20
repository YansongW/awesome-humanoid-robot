# Rokoko / Rokoko

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Rokoko |
| **English Name** | Rokoko |
| **Headquarters** | Copenhagen, Denmark |
| **Founded** | 2014 |
| **Official Website** | [https://rokoko.com](https://rokoko.com) |
| **Supply Chain Role** | Inertial motion capture, animation data, human-computer interaction data collection |
| **Enterprise Type** | Startup |
| **Parent Company/Group** | None |
| **Data Sources** | Rokoko official website, CGW News, Animation Xpress |

## Company Overview

Rokoko is an inertial motion capture (mocap) company targeting independent creators, gaming, film & television, sports science, and robotics. It is known for its high cost-effectiveness, ease of use, and real-time streaming capabilities.

The core product, Smartsuit Pro II, is a full-body inertial motion capture suit equipped with 17–19 9-DOF IMU sensors. It connects via Wi-Fi to the free Rokoko Studio software, enabling real-time recording, cleaning, editing, and streaming of animations to mainstream 3D tools such as Unreal Engine, Unity, Blender, Maya, and MotionBuilder. Rokoko also offers Smartgloves for hand tracking, Face Capture for facial capture, and AI-driven animation tools like Video to Animation.

Rokoko's motion data is increasingly used in the robotics field, providing natural motion references and training data for humanoid robots, digital humans, and embodied intelligence models.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Full-body Motion Capture | Inertial mocap suit | Smartsuit Pro II | Animation, Gaming, VFX |
| Hand Motion Capture | Finger tracking gloves | Smartgloves | Hand animation, Robotic dexterous hands |
| Software Platform | Recording, editing, streaming | Rokoko Studio | Mocap post-production, real-time driving |
| AI Animation Tools | Video/single-camera driven animation | Rokoko Video / Motion Library | Rapid animation generation |

## Representative Products

### Rokoko Smartsuit Pro II

> Rokoko Smartsuit Pro II: Please visit [official documentation](https://rokoko.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Sensors | 17× or 19× 9-DOF IMU | Rokoko official website |
| 3D Orientation Accuracy | ±1° | Rokoko public specifications |
| Sampling/Streaming Rate | 200 fps | Rokoko public specifications |
| Accelerometer Range | 16 g | Rokoko public specifications |
| Wireless Connection | Wi-Fi (max approx. 100 m) | Rokoko public specifications |
| Battery Life | Approx. 6 hours | Rokoko public specifications |
| Suit Sizes | S / M / L / XL | Rokoko official website |
| Price | Starting from approx. 2,745 USD | Public pricing |

**Technical Highlights**: Sensor Fusion 2.0 low-drift algorithm, multi-level tracking (stairs/ladders), high-impact motion optimization, washable fabric, native integration with Smartgloves, one-click real-time streaming.

**Application Scenarios**: Film & TV animation, game characters, virtual live streaming/VTubing, sports biomechanics analysis, robot/humanoid robot motion reference data collection.

### Rokoko Smartgloves

> Rokoko Smartgloves: Please visit [official documentation](https://rokoko.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Sensors | 7× 6-DOF hand trackers | Rokoko public specifications |
| Sampling Rate | 100 Hz | Rokoko public specifications |
| Latency | Approx. 20 ms | Rokoko public specifications |
| Wireless Connection | 2.4 / 5 GHz Wi-Fi | Rokoko public specifications |
| Magnetometer | None (anti-magnetic interference) | Rokoko public specifications |
| 3D Orientation Accuracy | ±1° | Rokoko public specifications |
| Price | Approx. 995 USD | Public pricing |

**Technical Highlights**: Magnetometer-free design for interference resistance, sub-millimeter fingertip tracking, shared battery and Wi-Fi link with Smartsuit Pro II, native integration with Rokoko Studio.

**Application Scenarios**: Hand animation, virtual character live streaming, robotic dexterous hand operation data collection, human-computer interaction research.

## Supply Chain Position

- **Upstream Key Components/Materials**: MEMS IMU sensors, Wi-Fi modules, wearable textiles, lithium batteries, sensor fusion algorithm chips.
- **Downstream Customers/Application Scenarios**: Independent animators, game studios (Ubisoft, EA, etc.), film & TV VFX, sports science research institutions, robot/humanoid robot companies.
- **Main Competitors/Peers**: Xsens / Movella, Noitom Perception Neuron, StretchSense, Manus, Vicon (optical mocap).

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_rokoko`
- Product/Platform Entities: `ent_product_rokoko_smartsuit_pro_ii`, `ent_product_rokoko_smartgloves`
- Key Relationships:
  - `rel_ent_company_rokoko_manufactures_ent_product_rokoko_smartsuit_pro_ii` (`ent_company_rokoko` → `manufactures` → `ent_product_rokoko_smartsuit_pro_ii`)
  - `rel_ent_company_rokoko_manufactures_ent_product_rokoko_smartgloves` (`ent_company_rokoko` → `manufactures` → `ent_product_rokoko_smartgloves`)

## References

1. [Rokoko Official Website](https://rokoko.com)
2. [CGW – Rokoko Smartsuit Pro II Launch](https://www.cgw.com/Press-Center/News/2021/Rokoko-Launches-the-Next-Gen-Smartsuit-Pro-II.aspx)
3. [Animation Xpress – Rokoko Smartsuit Pro II](https://www.animationxpress.com/latest-news/motion-capture-company-rokoko-launches-smartsuit-pro-ii/)
4. [Rokoko Studio Download Page](https://rokoko.com/studio)
