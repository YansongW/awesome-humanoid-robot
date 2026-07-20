# OptiTrack (NaturalPoint)

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | OptiTrack (NaturalPoint) |
| **English Name** | OptiTrack (NaturalPoint, Inc.) |
| **Headquarters** | Corvallis, Oregon, USA |
| **Founded** | 1996 |
| **Website** | [https://optitrack.com](https://optitrack.com) |
| **Supply Chain Role** | Optical motion capture, tracking cameras, motion measurement |
| **Enterprise Type** | Private company (under NaturalPoint) |
| **Parent Company/Group** | NaturalPoint, Inc. |
| **Data Source** | OptiTrack official website, product pages, public reports |

## Company Overview

OptiTrack is a world-leading supplier of optical motion capture systems. Its products are known for high precision, low latency, and large capture volume, and are widely used in film and animation, gaming, biomechanics, sports science, drone/robot positioning, and humanoid robot motion validation. OptiTrack's camera array, combined with Motive software, enables sub-millimeter 6DoF pose tracking.

OptiTrack offers the PrimeX series of high-resolution infrared cameras, Motive tracking software, and active/passive marker solutions. It is a common tool in robotics R&D for gait analysis, full-body motion capture, teleoperation validation, and algorithm calibration.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| PrimeX Camera Series | High-performance infrared motion capture cameras | [OptiTrack Motion Capture System](../products/product_optitrack_motive_system.md) | Film, sports, robotics |
| Motive Software | Data acquisition and real-time solving | Motive 3 | Motion capture, analysis |
| Tracking Accessories | Markers, calibration tools, synchronization devices | Active/Passive Marker Sets | R&D, integration |

## Representative Product

### OptiTrack Motion Capture System

> OptiTrack Motion Capture System: Please visit [official documentation](https://optitrack.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| System Type | Optical infrared motion capture system | OptiTrack official website |
| Representative Camera | PrimeX 13 / PrimeX 41, etc. | Product page |
| Tracking Accuracy | Sub-millimeter (exact value not disclosed) | Public information |
| Latency | As low as a few milliseconds | Product page |
| Resolution | Up to approximately 2048×2048 (PrimeX 41) | Product page |
| Frame Rate | Up to 240 fps or higher (depending on model) | Product page |
| Software | Motive 3 (real-time solving, data export) | Official website |
| Synchronization Interface | eSync / Ethernet | Product page |
| Price | Not disclosed | Business quotation |

**Technical Highlights**: High-resolution infrared imaging, sub-millimeter accuracy, low-latency real-time solving, large-scale multi-camera synchronization, rich SDK and data interfaces.

**Application Scenarios**: Humanoid robot gait and motion calibration, teleoperation training, drone/AGV positioning validation, film and animation, sports biomechanics, rehabilitation medicine.

## Supply Chain Position

- **Upstream Key Components/Materials**: Infrared image sensors, optical lenses, FPGA/processing chips, infrared LEDs, precision structural parts, calibration algorithms, network synchronization modules
- **Downstream Customers/Application Scenarios**: Film production companies, game developers, robot/drone R&D institutions, university laboratories, sports/medical institutions
- **Main Competitors/Peers**: Vicon, Motion Analysis, Qualisys, Noitom, Xsens (inertial)

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_optitrack`
- Product Entity: `ent_product_optitrack_motive_system`
- Component Entity: `ent_component_optitrack_motive_system_core`
- Key Relationships:
  - `ent_company_optitrack` -- `manufactures` --> `ent_product_optitrack_motive_system`
  - `ent_company_optitrack` -- `manufactures` --> `ent_component_optitrack_motive_system_core`
  - `ent_product_optitrack_motive_system` -- `uses` --> `ent_component_optitrack_motive_system_core`

## References

1. [OptiTrack Official Website](https://optitrack.com)
2. [OptiTrack Camera Product Page](https://optitrack.com/cameras/)
3. [Appendix D Enterprise Directory](../index-companies.md)
