# Xsens / Movella Xsens

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Xsens (思旷) |
| **English Name** | Xsens / Movella Xsens |
| **Headquarters** | Enschede, Netherlands (Xsens); USA (Movella Holdings) |
| **Founded** | 2000 (Xsens); Movella integrated in 2021 |
| **Official Website** | [https://xsens.com](https://xsens.com) / [https://movella.com](https://movella.com) |
| **Supply Chain Role** | Inertial sensors, inertial motion capture, motion analysis |
| **Enterprise Type** | Subsidiary of a listed company (Movella Holdings) |
| **Parent Company/Group** | Movella Holdings Inc. |
| **Data Source** | Xsens official website, Movella official website, Macnica Galaxy technical documentation |

## Company Profile

Xsens is one of the global pioneers in inertial motion tracking and motion capture technology. Founded in 2000 in Enschede, Netherlands, it was integrated into Movella Holdings in 2021 following the merger of mCube, Xsens, and Kinduct. The Xsens brand continues to operate as Movella's professional motion capture and motion analysis product line.

The Xsens MVN product line includes MVN Link (tight-fitting Lycra suit, 17 wired IMUs), MVN Awinda (strap-on wireless 17 IMUs), and MVN Analyze / MVN Animate software. The products are renowned for high precision, magnetic interference immunity, real-time low latency, and outdoor/field usability, and are widely used in film and television, gaming, sports science, biomechanics, ergonomics, and robotics research.

In the robotics field, Xsens MVN is used to capture natural human motion data, verify humanoid robot motion control algorithms, and provide full-body posture references for humanoid robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Professional Inertial Motion Capture Suit | High-end full-body motion capture | MVN Link | Film, TV, Gaming, VFX |
| Wireless Portable Motion Capture System | Mid-range wireless solution | MVN Awinda / Awinda Starter | Education, Sports, Research |
| Motion Analysis Software | Biomechanics & Ergonomics | MVN Analyze | Medical Rehabilitation, Ergonomics |
| Animation Software | Character Animation Production | MVN Animate | Gaming, Film, Virtual Production |
| Inertial Sensor Modules | Embedded IMU / AHRS | MTi Series, Movella DOT | Robotics, Drones, Vehicles |

## Representative Products

### Xsens MVN Link

> Xsens MVN Link: Please visit the [official documentation](https://xsens.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Sensors | 17× wired IMU + 1 prop sensor | Xsens public specifications |
| Update Rate | Up to 240 Hz | Xsens public specifications |
| Latency | Approx. 20 ms | Xsens public specifications |
| Wireless Range | Approx. 150 m | Xsens public specifications |
| Battery Life | Approx. 10 hours | Xsens public specifications |
| Biomechanical Model | 23 segments, 22 joints | Macnica Galaxy technical documentation |
| Positional Drift | Approx. 1% (without external aid) | Macnica Galaxy technical documentation |
| Price | Enterprise inquiry | Official channels |

**Technical Highlights**: High-precision inertial sensor fusion, magnetic interference immunity, real-time low latency, optional GNSS, full-body biomechanical model, outdoor and field usability, integration with finger tracking solutions like Metagloves.

**Application Scenarios**: High-end film and animation, professional sports biomechanics analysis, rehabilitation medicine, ergonomics research, humanoid robot motion data collection and algorithm validation.

### Xsens MVN Awinda

> Xsens MVN Awinda: Please visit the [official documentation](https://xsens.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Sensors | 17× wireless IMU | Xsens public specifications |
| Update Rate | Up to 60 Hz | Xsens public specifications |
| Latency | Approx. 30 ms | Xsens public specifications |
| Wireless Range | Approx. 50 m (Starter approx. 25 m) | Xsens public specifications |
| Battery Life | Approx. 6–12 hours | Xsens public specifications |
| Wearing Method | Adjustable straps, can be worn over clothing | Xsens public specifications |
| Price | Lower than MVN Link | Official channels |

**Technical Highlights**: Quick to wear, no motion capture studio required, can be worn over everyday clothing, magnetic interference immunity, cost-effective professional solution, compatible with MVN Analyze/Animate software.

**Application Scenarios**: Education and training, on-field sports analysis, rehabilitation assessment, small-to-medium team animation production, robot motion reference data collection.

## Supply Chain Position

- **Upstream Key Components/Materials**: MEMS IMU chips, magnetometers, gyroscopes, accelerometers, Lycra/elastic fabrics, wireless RF modules, sensor fusion algorithm IP.
- **Downstream Customers/Application Scenarios**: Electronic Arts, NBC Universal, Netflix, Daimler, Siemens, 500+ professional sports teams, film studios, research institutions, robotics companies.
- **Main Competitors/Comparables**: Rokoko, Noitom, Vicon (optical), OptiTrack (optical), StretchSense, Manus.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_xsens_movella`
- Product/Platform Entities: `ent_product_xsens_mvn_link`, `ent_product_xsens_mvn_awinda`
- Key Relationships:
  - `rel_ent_company_xsens_movella_manufactures_ent_product_xsens_mvn_link` (`ent_company_xsens_movella` → `manufactures` → `ent_product_xsens_mvn_link`)
  - `rel_ent_company_xsens_movella_manufactures_ent_product_xsens_mvn_awinda` (`ent_company_xsens_movella` → `manufactures` → `ent_product_xsens_mvn_awinda`)

## References

1. [Xsens Official Website](https://xsens.com)
2. [Movella Official Website](https://movella.com)
3. [Macnica Galaxy – Xsens MVN Link Technical Introduction](https://www.macnica.com/apac/galaxy/zh_tw/products-support/technical-articles/movella-xsens-mvn-link/)
4. [Xsens MVN Awinda Product Page](https://shop.movella.com/us/product-lines/motion-capture/products/xsens-mvn-awinda)
