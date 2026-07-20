# Tesla Optimus Gen 3

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Tesla](../companies/company_tesla.md) |
| **Product Category** | General-purpose humanoid robot |
| **Release Date** | Gen 3 hand disclosed at the end of 2024; full robot mass production advanced in 2026 |
| **Status** | Internal mass production / factory deployment |
| **Official Website/Source** | [Tesla Official Website](https://www.tesla.com) |

## Product Overview

The Tesla Optimus Gen 3 is the latest iteration of Tesla's humanoid robot platform, with key upgrades in hand degrees of freedom and whole-body electromechanical integration. Building on the 173 cm torso of Gen 2, Gen 3 increases single-hand degrees of freedom from 11 DOF to 22 DOF, equipping each hand with 25 actuators (50 actuators for both hands combined), significantly enhancing fine grasping and tool manipulation capabilities.

Optimus Gen 3 leverages Tesla's self-developed FSD visual neural network, automotive-grade battery packs, and actuator technology. Its target scenarios include battery sorting and material handling within Tesla's own factories, with a long-term vision toward the consumer market. Elon Musk has publicly stated a target retail price of $20,000–$30,000 USD, but as of 2026, this remains a target plan and the product has not been formally sold externally.

## Product Images

> Tesla Optimus Gen 3: Please visit [Official Materials](https://www.tesla.com) for details.

## Specifications Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 173 cm (height) | Tesla AI Day public materials |
| Weight | Approx. 57 kg (Gen 2 torso baseline) | Public materials; Gen 3 full weight not disclosed |
| Degrees of Freedom (whole body) | Torso 28+; Hands 22×2 | Gen 3 hand upgrade |
| Key Performance Indicators | Two-hand carrying approx. 20 kg; 50 hand actuators | Public demo / media compilation |
| Walking Speed | Approx. 8 km/h (target) | Third-party review |
| Battery Life | Approx. 2–4 hours (depending on task) | Not officially confirmed |
| Power Consumption | Not disclosed | - |
| Price | Target retail price $20,000–$30,000 USD | Musk public statement |

## Supply Chain Position

- **Manufacturer**: [Tesla](../companies/company_tesla.md)
- **Core Components/Technology Sources**: Self-developed linear/rotary actuators, FSD visual perception, battery pack and power management, automotive-grade computing platform; some structural parts outsourced.
- **Downstream Applications/Customers**: Tesla's own factories (battery sorting, material handling); future enterprise and consumer markets.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_tesla_optimus_gen3`
- Manufacturer Entity: `ent_company_tesla`
- Key Relationship:
  - `rel_ent_company_tesla_manufactures_ent_product_tesla_optimus_gen3` (`ent_company_tesla` → `manufactures` → `ent_product_tesla_optimus_gen3`)

## Application Scenarios

- **Automotive Manufacturing**: Performs battery cell sorting, material handling, box palletizing, and production line inspection in Tesla factories.
- **General Industrial**: Replaces repetitive, high-intensity, or safety-hazardous manual tasks such as handling and assembly assistance.
- **Future Consumer/Service**: Home cleaning, personal assistant, and care services (still in long-term planning stage).

## Competitive Comparison

| Comparison Item | Tesla Optimus Gen 3 | Figure 02 | Boston Dynamics Atlas |
|-----------------|---------------------|-----------|-----------------------|
| Positioning | General-purpose / industrial humanoid | Industrial manufacturing humanoid | Heavy-load industrial humanoid |
| Hand DOF | 22×2 | 16 (both hands) | Not disclosed |
| Price Direction | Target $20,000–$30,000 USD | Not disclosed | Not disclosed (estimated high-end) |
| Core Advantages | Mass production target, FSD vision, self-developed actuators | Helix VLA model, BMW deployment | 56 DOF, 50 kg payload, locomotion capability |

## Selection and Deployment Recommendations

- Currently, Optimus Gen 3 is only available for Tesla internal use and specific enterprise pilots; consumer sales are not yet open.
- Enterprise customers interested in humanoid robot alternatives are advised to also evaluate already-deployed platforms such as Figure 02 and Digit.

## References

1. [Tesla Official Website](https://www.tesla.com)
2. [Tesla AI Day Public Demo](https://www.tesla.com/AI)
3. [Robozaps – Tesla Optimus Gen 3 Specs](https://blog.robozaps.com/b/tesla-optimus-gen-3)
4. [Optimusk – Tesla Optimus Capabilities 2025-2026](https://optimusk.blog/blog/tesla-optimus-capabilities/)
