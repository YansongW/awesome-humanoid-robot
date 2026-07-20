# Boston Dynamics / Boston Dynamics

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 波士顿动力 |
| **English Name** | Boston Dynamics |
| **Headquarters** | Waltham, Massachusetts, USA |
| **Founded** | 1992 |
| **Website** | [https://bostondynamics.com](https://bostondynamics.com) |
| **Supply Chain Role** | Humanoid/legged robot OEM, industrial automation |
| **Company Type** | Subsidiary of Hyundai Motor Group |
| **Parent Company/Group** | Hyundai Motor Group |
| **Data Source** | Boston Dynamics official website, product specification pages, public reports |

## Company Overview

Boston Dynamics, originating from MIT, is a robotics company known for legged robots such as Atlas and Spot. In 2024, it released the fully electric Atlas, positioning it as an enterprise-grade industrial humanoid robot.

Boston Dynamics has long led research in legged robot motion control. The new electric Atlas targets heavy-duty industrial handling and automotive assembly scenarios, emphasizing 360° perception, IP67 protection, and autonomous battery swapping; the Spot quadruped robot has achieved large-scale commercial deployment.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Atlas Humanoid Robot | Enterprise-grade industrial humanoid | Atlas (Electric Version) | Automotive manufacturing, heavy-duty handling |
| Spot Quadruped Robot | Mobile inspection platform | Spot | Industrial inspection, surveying, security |
| Stretch Logistics Robot | Warehouse loading/unloading | Stretch | Truck/container loading/unloading |

## Representative Products

### Boston Dynamics Atlas (Electric Version)

> Boston Dynamics Atlas (Electric Version): Please visit [official materials](https://bostondynamics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 190 cm (height) | Boston Dynamics product page |
| Weight | Approx. 90 kg | Boston Dynamics product page |
| Degrees of Freedom | 56 | Boston Dynamics product page |
| Payload/Torque | Instantaneous 50 kg / Continuous 30 kg | Boston Dynamics product page |
| Speed/RPM | Not disclosed | - |
| Battery Life | Approx. 4 hours; supports autonomous battery swapping | Boston Dynamics product page |
| Interface/Communication | Orbit platform, Wi-Fi, enterprise system integration | Official disclosure |
| Price | Not disclosed (enterprise inquiry) | - |

**Technical Highlights**: Fully electric actuators, 360° visual and tactile perception, continuous joint motion, IP67 protection, autonomous battery swapping, and Orbit fleet management.

**Application Scenarios**: Parts sorting, heavy-duty handling, outdoor and harsh environment operations in manufacturing enterprises such as Hyundai Motor.

### Boston Dynamics Spot

> Boston Dynamics Spot: Please visit [official materials](https://bostondynamics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 83 cm (height, standing) | Boston Dynamics product page |
| Weight | Approx. 32 kg | Public information |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Approx. 14 kg | Public information |
| Speed/RPM | Approx. 1.6 m/s | Public information |
| Battery Life | Approx. 90 minutes | Public information |
| Interface/Communication | Spot SDK, Ethernet, Wi-Fi | Official disclosure |
| Price | Starting from approx. 74,500 USD | Public quotation |

**Technical Highlights**: Quadruped mobility, multi-sensor payload, autonomous navigation, mature commercial deployment, and developer ecosystem.

**Application Scenarios**: Industrial facility inspection, construction surveying, public safety, scientific research, and education.

## Supply Chain Position

- **Upstream Key Components/Materials**: Hyundai Mobis supply chain, motors/actuators, high-performance sensors, NVIDIA Jetson and other computing modules.
- **Downstream Customers/Application Scenarios**: Hyundai Motor Group, industrial enterprises, energy/construction customers, research institutions.
- **Main Competitors/Peers**: Tesla Optimus, Figure AI, Apptronik Apollo, Agility Robotics Digit.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_boston_dynamics`
- Product/Platform Entities: `ent_product_boston_dynamics_atlas_electric`, `ent_product_boston_dynamics_spot`
- Key Relationships:
  - `rel_ent_company_boston_dynamics_manufactures_ent_product_boston_dynamics_atlas_electric` (`ent_company_boston_dynamics` → `manufactures` → `ent_product_boston_dynamics_atlas_electric`)
  - `rel_ent_company_boston_dynamics_manufactures_ent_product_boston_dynamics_spot` (`ent_company_boston_dynamics` → `manufactures` → `ent_product_boston_dynamics_spot`)

## References

1. [Boston Dynamics Official Website](https://bostondynamics.com)
2. [Boston Dynamics Atlas Product Page](https://bostondynamics.com/products/atlas/)
3. [Boston Dynamics Spot Product Page](https://bostondynamics.com/products/spot/)
