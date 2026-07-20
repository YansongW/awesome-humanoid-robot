# SenseGlove

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | SenseGlove (感融科技) |
| **English Name** | SenseGlove B.V. |
| **Headquarters** | Delft, Netherlands |
| **Founded** | 2017 |
| **Website** | [https://senseglove.com](https://senseglove.com) |
| **Supply Chain Role** | Force feedback gloves, haptic feedback, teleoperation human-machine interface |
| **Company Type** | Startup |
| **Parent Company/Group** | None |
| **Data Source** | SenseGlove official website, product pages, public reports |

## Company Profile

SenseGlove is a Dutch startup specializing in force feedback and haptic feedback gloves. Its products are primarily used for virtual reality training, teleoperated robotics, medical rehabilitation, and engineering simulation. The Nova series wireless gloves provide active resistance feedback and vibrotactile feedback for each finger, enabling users to perceive grip force, shape, and texture in virtual or remote environments.

SenseGlove's force feedback solutions are widely applied in scenarios such as humanoid robot teleoperation, surgical robot training, nuclear power and space teleoperation, significantly reducing training costs and improving operational precision.

## Product Line

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Nova Series | Wireless force feedback gloves | [SenseGlove Nova 2](../products/product_senseglove_nova_2.md) | Teleoperation, VR training, medical rehabilitation |
| DK1/Exoskeleton | Early exoskeleton force feedback gloves | SenseGlove DK1 | Research, simulation |
| Software SDK | Hand tracking and force feedback integration | SenseGlove Unity/Unreal SDK | Developers, system integrators |

## Representative Product

### SenseGlove Nova 2

> SenseGlove Nova 2: Please visit the [official page](https://senseglove.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Wireless force feedback glove | SenseGlove official website |
| Feedback Method | 4 active resistance actuators + vibrotactile feedback | Product page |
| Finger Coverage | Thumb, index, middle, ring finger | Product page |
| Tracking | Compatible with SteamVR / Quest trackers (additional trackers required) | Product page |
| Wireless Connectivity | Bluetooth / 2.4 GHz proprietary protocol | Product page |
| Battery Life | Approx. 2–3 hours | Product page / exact value not disclosed |
| Weight | Approx. 320 g (single glove, exact value not disclosed) | Public information |
| Software Development | Unity, Unreal, C++ SDK | Official website |
| Price | Not disclosed | Business quotation |

**Technical Highlights**: Compact wireless design, 4-way active force feedback, high-fidelity vibrotactile feedback, plug-and-play SDK, suitable for humanoid robot teleoperation and complex training.

**Application Scenarios**: Humanoid robot remote operation, surgical robot training, VR industrial maintenance training, nuclear power/space teleoperation, rehabilitation hand function assessment.

## Supply Chain Position

- **Upstream Key Components/Materials**: Micro actuators/motors, flexible transmission mechanisms, sensors, batteries, Bluetooth modules, glove materials, tracker compatibility solutions
- **Downstream Customers/Application Scenarios**: Robot teleoperation, medical training, VR simulation, automotive/aviation maintenance training, research institutions
- **Main Competitors/Peers**: HaptX, Manus VR, Meta Haptic Glove, StretchSense, CyberGlove

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_senseglove`
- Product Entity: `ent_product_senseglove_nova_2`
- Component Entity: `ent_component_senseglove_nova_2_core`
- Key Relationships:
  - `ent_company_senseglove` -- `manufactures` --> `ent_product_senseglove_nova_2`
  - `ent_company_senseglove` -- `manufactures` --> `ent_component_senseglove_nova_2_core`
  - `ent_product_senseglove_nova_2` -- `uses` --> `ent_component_senseglove_nova_2_core`

## References

1. [SenseGlove Official Website](https://senseglove.com)
2. [SenseGlove Nova 2 Product Page](https://senseglove.com/products/nova-2/)
3. [Appendix D Company Directory](../index-companies.md)
