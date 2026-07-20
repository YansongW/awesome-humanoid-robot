# SenseGlove Nova 2 Haptic Force-Feedback Glove

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [SenseGlove](../companies/company_senseglove.md) |
| **Product Category** | Wireless force-feedback/haptic feedback glove |
| **Release Date** | Nova series continuously on sale, Nova 2 is the next generation |
| **Status** | Mass production/commercial |
| **Official Website/Source** | [SenseGlove Nova 2 Product Page](https://senseglove.com/products/nova-2/) |

## Product Overview

The SenseGlove Nova 2 is a wireless force-feedback glove designed for virtual reality, teleoperated robotics, and industrial training. It is equipped with active resistance actuators and vibrotactile modules at key finger locations, capable of simulating forces such as grasping, pressing, and friction. Paired with mainstream VR headsets and tracking solutions, it enables immersive remote control and training experiences. The Nova 2 is widely used in scenarios such as humanoid robot teleoperation, surgical robot training, and aviation maintenance simulation.

## Product Image

> SenseGlove Nova 2: Please visit the [official page](https://senseglove.com/products/nova-2/) for details.

## Specifications Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Wireless force-feedback glove | Official website |
| Feedback Actuators | 4 active resistance (thumb, index, middle, ring fingers) | Product page |
| Haptic Feedback | Vibrotactile feedback module | Product page |
| Finger Tracking | 5-finger tracking (relies on external tracker) | Product page |
| Wireless Connectivity | Bluetooth / 2.4 GHz proprietary protocol | Product page |
| Compatible Platforms | Meta Quest 2/3/Pro, SteamVR, PC VR | Product page |
| Battery Life | Approximately 2–3 hours | Product page |
| Weight per Glove | Approximately 320 g (exact value not disclosed) | Public information |
| Software Development | Unity, Unreal Engine, C++ SDK | Official website |
| Price | Not disclosed | Business quotation |

## Supply Chain Position

- **Manufacturer**: [SenseGlove](../companies/company_senseglove.md)
- **Core Components/Technology Sources**: Micro force-feedback actuators, flexible transmission, inertial/bending sensors, Bluetooth wireless module, battery, glove fabric, tracker adapter
- **Downstream Applications/Customers**: Robot teleoperation developers, medical surgical training, VR training integrators, automotive/aviation simulation, research institutions

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_senseglove_nova_2`
- Component Entity: `ent_component_senseglove_nova_2_core`
- Manufacturer Entity: `ent_company_senseglove`
- Key Relationships:
  - `rel_ent_company_senseglove_manufactures_ent_product_senseglove_nova_2` (`ent_company_senseglove` → `manufactures` → `ent_product_senseglove_nova_2`)
  - `rel_ent_company_senseglove_manufactures_ent_component_senseglove_nova_2_core` (`ent_company_senseglove` → `manufactures` → `ent_component_senseglove_nova_2_core`)
  - `rel_ent_product_senseglove_nova_2_uses_ent_component_senseglove_nova_2_core` (`ent_product_senseglove_nova_2` → `uses` → `ent_component_senseglove_nova_2_core`)

## Application Scenarios

- **Humanoid Robot Teleoperation**: Operators remotely control the hand grasping and manipulation of humanoid robots via the glove.
- **Surgical Robot Training**: Simulates tissue resistance and instrument tactile feedback to enhance training realism.
- **VR Industrial Maintenance Training**: Perceive forces such as bolt tightening and component disassembly in a virtual environment.
- **Rehabilitation Assessment**: Records hand movement and force feedback data for hand function rehabilitation training.

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | Wireless force-feedback glove | HaptX Gloves G1 | Manus VR Haptic Glove |
| Feedback | Active resistance + vibrotactile | Pneumatic high-fidelity force feedback | Primarily vibrotactile |
| Wireless | Yes | Requires external air source/cable | Yes |
| Price Range | Not disclosed | High-end | Mid-to-high-end |

## Selection and Deployment Recommendations

- Confirm the target platform tracking solution (Quest / SteamVR / optical tracking) and SDK support.
- Choose single or paired gloves based on the training scenario, and allocate time for force calibration and content adaptation.
- It is recommended to purchase from the official website or authorized distributors to obtain the latest firmware and technical support.

## Related Entries

- [Manufacturer: SenseGlove](../companies/company_senseglove.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [SenseGlove Official Website](https://senseglove.com)
2. [SenseGlove Nova 2 Product Page](https://senseglove.com/products/nova-2/)
3. Public product reviews and technical reports
4. [Appendix D Company Directory](../index-companies.md)
