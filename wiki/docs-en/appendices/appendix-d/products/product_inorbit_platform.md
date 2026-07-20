# InOrbit RobOps Platform

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [InOrbit](../companies/company_inorbit.md) |
| **Product Category** | Robot Operations (RobOps) / Fleet Orchestration Platform |
| **Release Date** | Continuously iterated since 2017 |
| **Status** | Commercial / Free Edition + Enterprise Edition |
| **Official Website/Source** | [InOrbit Official Website](https://inorbit.ai) |

## Product Overview

The InOrbit RobOps Platform is an industry-leading RobOps solution that helps robot developers and enterprises achieve observability, remote operations, optimization, and orchestration across heterogeneous robot fleets. The platform is built on the "Four O's" philosophy: Observability, Operations, Optimization, and Orchestration.

InOrbit provides robot-agnostic Agents, Adaptive Diagnostics™, real-time map tracking, one-click incident response, Time Capsule™ historical data replay, and the InOrbit Connect certification program supporting VDA 5050 and MassRobotics AMR interoperability standards. In 2025, InOrbit further launched Space Intelligence, extending orchestration capabilities from robots to people, manual vehicles, and fixed facilities.

InOrbit was recognized by Gartner as a 2024 Cool Vendor in Logistics and Robotics Technology, with customers including large enterprises such as Colgate-Palmolive and Genentech/Roche.

## Product Image

> InOrbit RobOps Platform: Please visit the [official website](https://inorbit.ai) for details.

## Specification Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Deployment Model | Public Cloud SaaS / Private Deployment | InOrbit Official Website |
| Integration Method | InOrbit Agent / Robot SDK / VDA 5050 | InOrbit Documentation |
| Supported Robot Types | AMR, AGV, Robotic Arm, Service Robot | Public Information |
| Observability Capabilities | Telemetry, Map Location, Alerts, Diagnostics | InOrbit Documentation |
| Adaptive Diagnostics | Adaptive Diagnostics™ | Official Information |
| Historical Replay | Time Capsule™ | InOrbit News |
| Interoperability Standards | VDA 5050, MassRobotics AMR | InOrbit Documentation |
| Free Edition | Unlimited Robots Free Edition | Automate.org |
| Pricing | Free / Standard / Developer / Enterprise | InOrbit Official Website |

## Supply Chain Position

- **Manufacturer**: [InOrbit](../companies/company_inorbit.md)
- **Core Components/Technology Sources**: AWS/Google Cloud Infrastructure, ROS/ROS2, SICK Tag-LOC Positioning Systems, VDA 5050 / MassRobotics Interoperability Standards.
- **Downstream Applications/Customers**: Colgate-Palmolive, Genentech/Roche, Logistics 3PL, Manufacturing and Retail Enterprises.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_inorbit_robops_platform`
- Manufacturer Entity: `ent_company_inorbit`
- Key Relationship:
  - `rel_ent_company_inorbit_manufactures_ent_product_inorbit_robops_platform` (`ent_company_inorbit` → `manufactures` → `ent_product_inorbit_robops_platform`)

## Application Scenarios

- **Multi-brand AMR Mixed Fleet**: Unified orchestration of AMRs/AGVs from different manufacturers to avoid traffic conflicts.
- **Warehouse Human-Robot Traffic Management**: Assign traffic priority for personnel, forklifts, and robots via a rules engine.
- **Robot Anomaly Response**: Adaptive Diagnostics automatically classifies faults, enabling one-click takeover or ticket generation.
- **Production Facility Robot Orchestration**: Integration with WMS/ERP/MES for material delivery and production line coordination.

## Competitive Comparison

| Comparison Item | InOrbit | Formant | Freedom Robotics |
|-----------------|---------|---------|------------------|
| Positioning | RobOps & Fleet Orchestration | Data & Operations Platform | Remote Control & Fleet Management |
| Core Advantage | Orchestration, Interoperability Standards, Free Edition | Data Visualization, Teleoperation | Quick Integration, Developer Friendly |
| Interoperability Certification | InOrbit Connect | More Flexible | More Flexible |
| Enterprise Integration | WMS/ERP/MES | Third-party Integration | Third-party Integration |
| Target Customers | Large Enterprises with Mixed Fleets | Robot Manufacturers + End Enterprises | Startup Robotics Companies |

## Selection and Deployment Recommendations

- Suitable for large enterprises with multi-brand, multi-scenario robot fleets requiring unified orchestration and enterprise system integration.
- The Free Edition can be used for small-scale pilots to verify Agent stability and data visualization effectiveness.
- Before deployment, review existing robot interface standards and prioritize devices supporting VDA 5050 or the InOrbit Robot SDK.

## References

1. [InOrbit Official Website](https://inorbit.ai)
2. [Automate.org – InOrbit Free Edition Launch](https://www.automate.org/news/inorbit-launches-free-edition-to-democratize-robot-operations)
3. [Automate.org – SICK and InOrbit Partnership](https://www.automate.org/news/sick-and-inorbit-ai-achieve-groundbreaking-advances-in-robot-and-facility-operations)
4. [Robotics 247 – InOrbit Series A Funding](https://www.robotics247.com/article/inorbit.ai_closes_series_a_funding_round_to_scale_robot_orchestration_platform/designer)
