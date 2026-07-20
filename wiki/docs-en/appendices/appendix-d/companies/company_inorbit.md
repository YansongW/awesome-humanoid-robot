# InOrbit / InOrbit.AI

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | InOrbit |
| **English Name** | InOrbit.AI |
| **Headquarters** | Mountain View, California, USA |
| **Founded** | 2017 |
| **Website** | [https://inorbit.ai](https://inorbit.ai) |
| **Supply Chain Role** | Robot Operations (RobOps), Fleet Orchestration, Remote Operations |
| **Enterprise Type** | Startup |
| **Parent Company/Group** | None |
| **Data Source** | InOrbit website, Automate.org, Gartner Cool Vendor report |

## Company Profile

InOrbit is a cloud computing company focused on Robot Operations (RobOps) and fleet orchestration, dedicated to enabling efficient collaboration between humans, robots, and AI in real production environments.

The platform is centered around the "four O's"—Observability, Operations, Optimization, and Orchestration—providing robot-agnostic Agents, Adaptive Diagnostics™, real-time map tracking, one-click incident response, remote teleoperation, and cross-brand fleet orchestration. The InOrbit Connect certification program supports various access methods including VDA 5050 and MassRobotics AMR interoperability standards, helping enterprises integrate robots from different vendors.

In 2024, InOrbit was selected for the Google for Startups Latino Founders Fund; in 2025, it completed a $10 million Series A funding round co-led by L'Attitude Ventures and Globant Ventures.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| Robot Operations Platform | Observability, Diagnostics, Remote Control | InOrbit Control | Logistics, Manufacturing, Retail |
| Fleet Orchestration Platform | Multi-brand Robot Coordination | InOrbit Space Intelligence | Large-scale Mixed Fleets |
| Developer Platform | API, SDK, White-label Applications | InOrbit Developer Edition | System Integrators, Robot OEMs |
| Interoperability Certification | Robot Access Standards | InOrbit Connect | Multi-vendor Ecosystem |

## Representative Products

### InOrbit RobOps Platform

> InOrbit RobOps: Please visit the [official website](https://inorbit.ai) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Deployment Model | Public Cloud SaaS / Private Deployment | InOrbit website |
| Access Methods | InOrbit Agent / Robot SDK / VDA 5050 | InOrbit documentation |
| Supported Robot Types | AMR, AGV, Robotic Arm, Service Robot | Public information |
| Real-time Monitoring | Telemetry, Map Location, Alerts | InOrbit documentation |
| Adaptive Diagnostics | Adaptive Diagnostics™ | Official information |
| Time Capsule | Time Capsule™ Historical Data Replay | InOrbit news |
| Free Edition | Unlimited Robots Free Edition | Automate.org |
| Pricing | Free / Standard / Developer Subscription | InOrbit website |

**Technical Highlights**: Robot-agnostic observability layer, cross-brand mixed fleet orchestration, AI-driven adaptive diagnostics, Time Capsule historical replay, deep integration with positioning systems like SICK Tag-LOC.

**Application Scenarios**: Multi-brand AMR coordination in 3PL warehouses, human-robot mixed traffic management in manufacturing plants, large-scale retail and service robot operations, hospital logistics robot scheduling.

### InOrbit Space Intelligence

> InOrbit Space Intelligence: Please visit the [official website](https://inorbit.ai) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Positioning | Physical World Orchestration Layer | InOrbit news |
| Core Capabilities | Coexistence, Coordination, Collaboration (3C) | Public information |
| Integrated Systems | WMS / ERP / MES | InOrbit documentation |
| Positioning Technology | Supports UWB, Tag-LOC, SLAM | InOrbit & SICK partnership news |
| Automation Rules | Traffic Priority, Charging Scheduling, Zone Control | Public information |
| Pricing | Enterprise Subscription | Official inquiry |

**Technical Highlights**: Software-defined physical operations, unified human-robot-vehicle orchestration, integration with enterprise business systems, rule engine-driven dynamic scheduling.

**Application Scenarios**: Human-robot mixed traffic in large warehouses, unified scheduling of multi-brand AMRs, material delivery on factory production lines, robot orchestration in large facilities like airports/hospitals.

## Supply Chain Position

- **Upstream Key Components/Materials**: AWS/Google Cloud infrastructure, SICK and other positioning sensors, ROS/ROS2, VDA 5050 / MassRobotics interoperability standards.
- **Downstream Customers/Application Scenarios**: Colgate-Palmolive, Genentech/Roche, Logistics 3PL, Manufacturing and Retail enterprises.
- **Main Competitors/Comparables**: Formant, Freedom Robotics, AW RoboMaker, Google Cloud Robotics, Locus Robotics fleet management.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_inorbit`
- Product/Platform Entities: `ent_product_inorbit_robops_platform`, `ent_product_inorbit_space_intelligence`
- Key Relationships:
  - `rel_ent_company_inorbit_manufactures_ent_product_inorbit_robops_platform` (`ent_company_inorbit` → `manufactures` → `ent_product_inorbit_robops_platform`)
  - `rel_ent_company_inorbit_manufactures_ent_product_inorbit_space_intelligence` (`ent_company_inorbit` → `manufactures` → `ent_product_inorbit_space_intelligence`)

## References

1. [InOrbit Website](https://inorbit.ai)
2. [Automate.org – InOrbit Free Edition Launch](https://www.automate.org/news/inorbit-launches-free-edition-to-democratize-robot-operations)
3. [Automate.org – SICK and InOrbit Partnership](https://www.automate.org/news/sick-and-inorbit-ai-achieve-groundbreaking-advances-in-robot-and-facility-operations)
4. [Robotics 247 – InOrbit Series A Funding](https://www.robotics247.com/article/inorbit.ai_closes_series_a_funding_round_to_scale_robot_orchestration_platform/designer)
