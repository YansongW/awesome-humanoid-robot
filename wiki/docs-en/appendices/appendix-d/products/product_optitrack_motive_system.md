# OptiTrack Motion Capture System

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [OptiTrack](../companies/company_optitrack.md) |
| **Product Category** | Optical Motion Capture System |
| **Release Date** | PrimeX series continuously on sale; Motive 3 current |
| **Status** | Mass production/commercial |
| **Official Website/Source** | [OptiTrack Camera Product Page](https://optitrack.com/cameras/) |

## Product Overview

The OptiTrack Motion Capture System consists of PrimeX series infrared cameras, Motive tracking software, and active/passive markers. It achieves sub-millimeter, low-latency 6DoF pose tracking in indoor environments. This system is widely used in humanoid robot motion validation, teleoperation training, gait analysis, drone/AGV positioning calibration, and film/animation production.

## Product Image

> OptiTrack Motion Capture System: Please visit [Official Materials](https://optitrack.com/cameras/) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| System Composition | PrimeX cameras + Motive software + markers | Official website |
| Representative Cameras | PrimeX 13 (1.3 MP), PrimeX 41 (2048×2048) | Product page |
| Tracking Accuracy | Sub-millimeter (exact value not disclosed) | Public materials |
| Latency | As low as a few milliseconds | Product page |
| Maximum Frame Rate | PrimeX 13: 240 fps; PrimeX 41: 180 fps | Product page |
| Field of View | Not disclosed | Product page |
| Synchronization Method | eSync / Ethernet | Product page |
| Software Interface | Motive 3, C/C++ SDK, Python, ROS, VRPN | Official website |
| Working Distance | Not disclosed | Product page |
| Price | Not disclosed | Business quotation |

## Supply Chain Position

- **Manufacturer**: [OptiTrack](../companies/company_optitrack.md)
- **Core Components/Technology Sources**: Infrared image sensors, optical lenses, FPGA/processing chips, infrared illumination, calibration algorithms, network synchronization, and 3D solving software
- **Downstream Applications/Customers**: Film and animation companies, robot/drone R&D teams, universities and research institutes, sports/rehabilitation institutions

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_optitrack_motive_system`
- Component Entity: `ent_component_optitrack_motive_system_core`
- Manufacturer Entity: `ent_company_optitrack`
- Key Relationships:
  - `rel_ent_company_optitrack_manufactures_ent_product_optitrack_motive_system` (`ent_company_optitrack` → `manufactures` → `ent_product_optitrack_motive_system`)
  - `rel_ent_company_optitrack_manufactures_ent_component_optitrack_motive_system_core` (`ent_company_optitrack` → `manufactures` → `ent_component_optitrack_motive_system_core`)
  - `rel_ent_product_optitrack_motive_system_uses_ent_component_optitrack_motive_system_core` (`ent_product_optitrack_motive_system` → `uses` → `ent_component_optitrack_motive_system_core`)

## Application Scenarios

- **Humanoid Robot Motion Calibration**: Capture full-body joint trajectories to validate motion planning and control algorithms.
- **Teleoperation Training**: Record operator hand/body movements for training teleoperation strategies.
- **Drone/AGV Positioning Validation**: Provide high-precision ground truth to evaluate SLAM and positioning algorithms.
- **Film, Animation, and Gaming**: Character motion capture and real-time virtual production.

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | Optical infrared motion capture | Vicon Vero/Vantage | Qualisys Miqus/Arqus |
| Accuracy | Sub-millimeter | Sub-millimeter | Sub-millimeter |
| Latency | Low latency | Low latency | Low latency |
| Price | Not disclosed | High-end | High-end |

## Selection and Deployment Recommendations

- Choose the number and model of cameras based on capture space size and accuracy requirements.
- Ensure the venue has controllable infrared reflection conditions, avoiding sunlight and strong infrared interference.
- Perform system calibration before deployment and verify SDK interface compatibility with the target software stack.

## Related Entries

- [Manufacturer: OptiTrack](../companies/company_optitrack.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [OptiTrack Official Website](https://optitrack.com)
2. [OptiTrack Camera Product Page](https://optitrack.com/cameras/)
3. Motive software documentation and public technical materials
4. [Appendix D Company Directory](../index-companies.md)
