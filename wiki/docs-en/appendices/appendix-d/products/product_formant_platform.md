# Formant Robot Data & Operations Platform

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Formant](../companies/company_formant.md) |
| **Product Category** | Robot Data Platform / Remote Operations / Teleoperation |
| **Release Date** | Continuously iterated since 2017 |
| **Status** | Commercial / Large-scale Deployment |
| **Official Website/Source** | [Formant Official Website](https://formant.io) |

## Product Overview

The Formant Data & Operations Platform is a unified RobOps platform for robot developers and end-user enterprises. Through the lightweight Formant Agent, robots can connect to the cloud within minutes, enabling one-stop management of telemetry, logs, video, maps, alerts, remote control, and fleet analytics.

The platform supports multiple integration methods including ROS/ROS2, MQTT, and REST API, and is compatible with robots of different brands and form factors. Formant emphasizes managing heterogeneous fleets via a "single pane of glass," allowing operators to manage large-scale robot deployments at a machine-to-human ratio of 100:1 or higher.

In 2023, Formant integrated with MoveIt Pro in collaboration with PickNik Robotics, further extending support for robotic arm teleoperation and deployment management.

## Product Image

> Formant Platform: Please visit the [official website](https://formant.io) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Deployment Model | Public Cloud SaaS / Private Deployment | Formant Official Website |
| Integration Method | Formant Agent (single command installation) | Formant Documentation |
| Supported Middleware | ROS 1 / ROS 2, MQTT, REST API | Public Information |
| Data Types | Telemetry, Logs, Video, Point Clouds, Maps, Alerts | Formant Documentation |
| Visualization | Real-time Dashboards, 2D/3D Views, Historical Playback | Formant Documentation |
| Teleoperation | Browser-based Remote Control, Joystick/API | Public Information |
| Fleet Scale | Supports thousands of robots | BMW i Ventures News |
| Security & Compliance | SOC 2, GDPR, Encrypted Transmission | Formant Official Website |
| Pricing | Subscription based on devices/data volume | Official Inquiry |

## Supply Chain Position

- **Manufacturer**: [Formant](../companies/company_formant.md)
- **Core Components/Technology Sources**: AWS/Google Cloud/Azure Cloud Infrastructure, ROS/ROS2, Video Codec, WebRTC/Network Transport, Time-Series Database.
- **Downstream Applications/Customers**: SoftBank Robotics, BP, Blue River Technology (John Deere), Burro, Knightscope, Scythe.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_formant_platform`
- Manufacturer Entity: `ent_company_formant`
- Key Relationships:
  - `rel_ent_company_formant_manufactures_ent_product_formant_platform` (`ent_company_formant` → `manufactures` → `ent_product_formant_platform`)

## Application Scenarios

- **Warehouse AMR Fleet Monitoring**: Real-time viewing of location, battery, and task status; quick identification of abnormal robots.
- **Agricultural Robot Remote Diagnosis**: Analyze root causes of field failures through video and telemetry playback.
- **Large-scale Cleaning Service Robot Operations**: Unified panel management for multi-brand robots, reducing operational costs.
- **Robotic Arm Teleoperation**: Combined with MoveIt Pro for manual takeover and debugging of complex grasping tasks.

## Competitive Comparison

| Comparison Item | Formant | InOrbit | Freedom Robotics |
|-----------------|---------|---------|------------------|
| Positioning | Robot Data & Operations Platform | Robot Operations & Orchestration Platform | Robot Remote Control & Fleet Management |
| Core Advantage | Out-of-the-box, Strong Data Visualization | Support for Orchestration & Interoperability Standards | Single-line Code Integration, Developer-friendly |
| Teleoperation | Built-in | Built-in | Built-in |
| Interoperability Certification | More Flexible | InOrbit Connect | More Flexible |
| Typical Customers | Robot Manufacturers + End Enterprises | Large Enterprise Mixed Fleets | Startup Robotics Companies |

## Selection and Deployment Recommendations

- Suitable for teams that want to quickly gain enterprise-level robot data and operations capabilities without building their own platform.
- Assess data export and compliance requirements before deployment, and choose public cloud or private deployment mode.
- It is recommended to first connect a small batch of robots to verify data bandwidth, alert thresholds, and teleoperation latency.

## References

1. [Formant Official Website](https://formant.io)
2. [BMW i Ventures – Formant Investment News](https://www.bmwiventures.com/news/operationalizing-robot-fleets-at-scale-our-lead-investment-in-formant)
3. [The Robot Report – Formant and SoftBank Collaboration](https://www.therobotreport.com/formants-data-platform-comes-to-softbanks-cleaning-robots/)
4. [SignalFire – Formant Investment Blog](https://www.signalfire.com/blog/formant-robotics-investor)
