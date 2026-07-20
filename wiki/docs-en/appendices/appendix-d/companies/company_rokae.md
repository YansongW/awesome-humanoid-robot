# ROKAE Robotics

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 珞石机器人 |
| **English Name** | ROKAE Robotics |
| **Headquarters** | Zoucheng, Shandong, China (R&D center in Beijing) |
| **Founded** | 2015 |
| **Website** | [https://www.rokae.com](https://www.rokae.com) |
| **Supply Chain Role** | OEM / Industrial Robots / Collaborative Robots / Humanoid Robot Components |
| **Enterprise Attribute** | Domestic brand, representative of high-speed and high-precision robots |
| **Parent Company/Group** | None |
| **Data Source** | ROKAE official website, product brochures, WAIC 2026 reports, public press releases |

## Company Overview

ROKAE Robotics focuses on the development of high-performance industrial robots and collaborative robots, known for their high-speed, high-precision, and high-rigidity control systems.

The company has developed its own xCore control system, covering the XB series of industrial six-axis robots, the xMate series of collaborative robots, and flexible intelligent manufacturing solutions. ROKAE has accumulated numerous implementation cases in automotive parts, 3C, medical, and metal processing industries, and also provides joint and motion control technologies for humanoid robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Industrial Robots | High-speed, high-precision six-axis | XB Series | Automotive parts, 3C, metal processing |
| Collaborative Robots | Industrial-grade flexible collaboration | xMate CR / SR / ER Series | Assembly, inspection, medical |
| Controllers and Software | Self-developed control system | xCore | Full series of robots |

## Representative Products

### xMate CR Series Collaborative Robots

> xMate CR: Please visit [official materials](https://www.rokae.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | 6-DOF industrial-grade collaborative robot | ROKAE official website |
| Weight | Not disclosed | - |
| Payload | 3–12 kg (depending on model) | Product brochure |
| Reach | 717–1304 mm (depending on model) | Product brochure |
| Degrees of Freedom | 6/7 DOF (depending on model) | Public specifications |
| Repeatability | ±0.02–±0.03 mm | Product brochure |
| Maximum End-Effector Speed | Not disclosed | - |
| Protection Rating | IP54 | Product brochure |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Self-developed xCore control system, high trajectory accuracy, drag teaching, force-controlled grinding, supporting complex processes and human-robot collaboration.

**Application Scenarios**: 3C precision assembly, automotive parts grinding, medical device loading/unloading, force-controlled polishing, scientific research and education.

### xMate SR Series Collaborative Robots

> xMate SR: Please visit [official materials](https://www.rokae.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | 6-DOF collaborative robot | ROKAE official website |
| Payload | 5–10 kg (depending on model) | Product brochure |
| Reach | Not disclosed | - |
| Degrees of Freedom | 6 DOF | Public specifications |
| Repeatability | ±0.03 mm | Product brochure |
| Protection Rating | IP54 | Product brochure |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Compact structure, flexible deployment, targeting flexible automation and lightweight human-robot collaboration scenarios for small and medium-sized enterprises.

**Application Scenarios**: Assembly, inspection, loading/unloading, packaging, educational training.

## Supply Chain Position

- **Upstream Key Components/Materials**: Harmonic reducers, servo motors, encoders, self-developed controllers, structural parts, cables, sensors.
- **Downstream Customers/Application Scenarios**: Automotive, 3C, new energy, metal processing, medical, humanoid robot OEMs.
- **Main Competitors/Peers**: Estun, Inovance, JAKA, AUBO, Yaskawa, KUKA.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_rokae`
- Product Entities: `ent_product_rokae_xmate_cr`, `ent_product_rokae_xmate_sr`
- Key Relationships:
  - `ent_company_rokae` -- `manufactures` --> `ent_product_rokae_xmate_cr`
  - `ent_company_rokae` -- `manufactures` --> `ent_product_rokae_xmate_sr`

## References

1. [ROKAE Robotics Official Website](https://www.rokae.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. ROKAE product brochures and public press releases
