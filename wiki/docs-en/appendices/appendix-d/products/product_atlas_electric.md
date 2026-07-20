# Boston Dynamics Atlas (Electric Version)

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Boston Dynamics](../companies/company_boston_dynamics.md) |
| **Product Category** | Industrial-grade humanoid robot |
| **Release Date** | Electric version announced in April 2024; early mass production in 2026 |
| **Status** | Early mass production / Enterprise internal testing |
| **Official Website/Source** | [Boston Dynamics Atlas](https://bostondynamics.com/products/atlas/) |

## Product Overview

In April 2024, Boston Dynamics announced the retirement of the hydraulic-driven classic Atlas and introduced the fully electric version. The new Atlas uses custom high-power electric actuators, with the hip, waist, and neck supporting 360° continuous rotation. The entire robot has 56 degrees of freedom, with load capacity and range of motion among the best in the industry.

The electric Atlas is positioned for heavy-duty industrial tasks, including material handling, equipment operation, and automotive manufacturing processes. Its battery supports autonomous hot-swapping, and combined with the Boston Dynamics Orbit fleet management platform, it can achieve near-continuous operation. Initial deployments are expected to focus on Hyundai Motor Group manufacturing bases and Google DeepMind research scenarios.

## Product Image

> Boston Dynamics Atlas Electric: Please visit the [official page](https://bostondynamics.com/products/atlas/) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 190 cm (height) | Official spec page |
| Weight | Approx. 90 kg | Official spec page |
| Degrees of Freedom (Total) | 56 DOF | Official spec page |
| Key Performance Indicators | Instantaneous load 50 kg; Sustained load 30 kg; Maximum reach 2.3 m | Official spec page |
| Walking Speed | Approx. 9 km/h | Third-party review |
| Battery Life | Approx. 4 hours (typical tasks) | Official spec page |
| Protection Rating | IP67 | Official spec page |
| Operating Temperature | -20°C to 40°C | Official spec page |
| Price | Not disclosed (industry estimate approx. 150,000 USD) | Third-party estimate |

## Supply Chain Position

- **Manufacturer**: [Boston Dynamics](../companies/company_boston_dynamics.md)
- **Core Components/Technology Sources**: Custom electric actuators, multi-camera 360° vision, proprietary real-time control stack and Orbit software platform; Hyundai Group provides manufacturing and supply chain support.
- **Downstream Applications/Customers**: Hyundai automotive manufacturing, Google DeepMind research, heavy-duty industrial scenarios.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_boston_dynamics_atlas_electric`
- Manufacturer Entity: `ent_company_boston_dynamics`
- Key Relationship:
  - `rel_ent_company_boston_dynamics_manufactures_ent_product_boston_dynamics_atlas_electric` (`ent_company_boston_dynamics` → `manufactures` → `ent_product_boston_dynamics_atlas_electric`)

## Application Scenarios

- **Automotive Manufacturing**: Heavy material handling, parts transport, and complex assembly in Hyundai Motor Group factories.
- **Heavy-Duty Industry**: Replacing manual labor for repetitive handling over 30 kg, equipment maintenance, and operations in high-risk areas.
- **Research and Development**: Used by institutions like Google DeepMind for robot learning and dynamic motion control algorithm validation.

## Competitive Comparison

| Comparison Item | Boston Dynamics Atlas (Electric) | Tesla Optimus Gen 3 | Agility Digit |
|-----------------|----------------------------------|---------------------|---------------|
| Positioning | Heavy-duty industrial humanoid | General/industrial humanoid | Logistics/warehouse humanoid |
| Total DOF | 56 | 28+ torso + 22×2 hands | 16–28 |
| Load Capacity | 50 kg instantaneous / 30 kg sustained | Approx. 20 kg | 16 kg |
| Core Advantages | Motion capability, load capacity, 360° joints | Cost target, AI data loop | Commercial deployment maturity |

## Selection and Deployment Recommendations

- Currently, the electric Atlas is primarily for enterprise pilots and Hyundai Motor Group ecosystem customers. It is recommended to inquire through Boston Dynamics' business channels.
- Before deployment, assess site load capacity, human-robot collaboration safety solutions, and integration requirements with MES/WMS.

## References

1. [Boston Dynamics Atlas Official Product Page](https://bostondynamics.com/products/atlas/)
2. [Boston Dynamics Blog – Electric Atlas Reveal](https://bostondynamics.com/)
3. [Robozaps – Boston Dynamics Atlas Review](https://blog.robozaps.com/b/boston-dynamics-atlas-review)
4. [Humanoid.Guide – Atlas](https://humanoid.guide/product/atlas/)
