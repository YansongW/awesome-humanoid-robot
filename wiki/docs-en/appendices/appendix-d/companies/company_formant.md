# Formant / Formant

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Formant |
| **English Name** | Formant |
| **Headquarters** | San Francisco, California, USA |
| **Founded** | 2017 |
| **Website** | [https://formant.io](https://formant.io) |
| **Supply Chain Role** | Robot data platform, remote operations, fleet management, teleoperation |
| **Enterprise Type** | Startup |
| **Parent Company/Group** | None |
| **Data Source** | Formant official website, BMW i Ventures investment news, The Robot Report |

## Company Profile

Formant is a cloud computing company focused on Robot Operations (RobOps), providing a unified data, monitoring, analysis, and remote operation platform for robot developers and end-user enterprises.

The platform supports ROS/ROS2 and any robot SDK, enabling robots to connect to the cloud with a single command or a lightweight Agent. Formant offers real-time telemetry visualization, alerts, data logging, teleoperation, task scheduling, and fleet-level analytics, helping enterprises achieve large-scale deployment with less engineering resources. Its customers span agriculture, warehousing, inspection, cleaning, and manufacturing.

Formant completed an $18 million Series A funding round in 2022 and secured an additional $21 million in funding led by BMW i Ventures in 2024, further expanding its fleet operations and data platform capabilities.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Robot Data Platform | Real-time telemetry, logs, visualization | Formant Observe | Fleet monitoring, troubleshooting |
| Remote Operations Platform | Low-latency teleoperation and human-robot collaboration | Formant Operate | Anomaly intervention, complex scenario control |
| Data Analytics Platform | Fleet-level insights and KPIs | Formant Analyze | Operational optimization, ROI reporting |
| Application Building Framework | White-label/custom robot applications | Formant Platform SDK | Multi-brand fleet integration |

## Representative Products

### Formant Data and Operations Platform

> Formant Platform: Please visit the [official documentation](https://formant.io) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Deployment Model | Public cloud SaaS / Private deployment | Formant official website |
| Integration Method | Formant Agent (single command installation) | Formant documentation |
| Supported Middleware | ROS 1 / ROS 2, MQTT, REST API | Public information |
| Data Types | Telemetry, logs, video, point clouds, maps | Formant documentation |
| Teleoperation Latency | Not disclosed (depends on network and edge agent) | - |
| Fleet Scale | Supports thousands of robots | BMW i Ventures news |
| Security & Compliance | SOC 2, GDPR, encrypted transmission | Formant official website |
| Pricing | Subscription based on devices/data volume | Official inquiry |

**Technical Highlights**: Out-of-the-box robot data visualization, low-code alerts and automated workflows, unified multi-brand fleet management, remote control and one-click takeover, integration with ecosystems like PickNik MoveIt.

**Application Scenarios**: AMR warehouse fleet monitoring, remote diagnosis of agricultural robots, anomaly takeover of inspection robots, large-scale operation of cleaning service robots.

### Formant Teleoperation

> Formant Teleoperation: Please visit the [official documentation](https://formant.io) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Control Methods | Keyboard, gamepad, touchscreen, custom API | Formant documentation |
| Video Stream | Real-time multi-camera feed | Public information |
| Maps & Navigation | 2D/3D map overlay, click-to-navigate | Formant documentation |
| Safety Mechanisms | Emergency stop, permission management, audit logs | Public information |
| Network Adaptability | Weak network/reconnection, edge caching | Formant documentation |
| Pricing | Included in enterprise subscription | Official inquiry |

**Technical Highlights**: Low-latency remote control from the browser, multi-camera and sensor fusion view, native integration with the Formant data platform, permission levels and operation auditing.

**Application Scenarios**: Manual takeover in warehouse congestion scenarios, anomaly handling in outdoor inspections, remote assistance for semi-autonomous robots, new employee training and robot demonstrations.

## Supply Chain Position

- **Upstream Key Components/Materials**: AWS/Google Cloud/Azure cloud infrastructure, edge computing modules, ROS/ROS2, video codec and network transmission technology.
- **Downstream Customers/Application Scenarios**: SoftBank Robotics, BP, Blue River Technology (John Deere), Burro, Knightscope, Scythe, and other robot manufacturers and end-user enterprises.
- **Main Competitors/Peers**: InOrbit, Freedom Robotics, AWS RoboMaker, Google Cloud Robotics, Boston Dynamics Orbit.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_formant`
- Product/Platform Entities: `ent_product_formant_platform`, `ent_product_formant_teleoperation`
- Key Relationships:
  - `rel_ent_company_formant_manufactures_ent_product_formant_platform` (`ent_company_formant` → `manufactures` → `ent_product_formant_platform`)
  - `rel_ent_company_formant_manufactures_ent_product_formant_teleoperation` (`ent_company_formant` → `manufactures` → `ent_product_formant_teleoperation`)

## References

1. [Formant Official Website](https://formant.io)
2. [BMW i Ventures – Formant Investment News](https://www.bmwiventures.com/news/operationalizing-robot-fleets-at-scale-our-lead-investment-in-formant)
3. [The Robot Report – Formant and SoftBank Partnership](https://www.therobotreport.com/formants-data-platform-comes-to-softbanks-cleaning-robots/)
4. [SignalFire – Formant Investment Blog](https://www.signalfire.com/blog/formant-robotics-investor)
