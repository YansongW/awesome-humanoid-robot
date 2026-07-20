# 星动纪元 / Star1

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 星动纪元 |
| **English Name** | Star1 / RobotEra |
| **Headquarters** | Beijing, China |
| **Founded** | 2023 |
| **Website** | [https://www.robotera.com](https://www.robotera.com) |
| **Supply Chain Role** | Complete Machine OEM / High-Performance General-Purpose Humanoid Robot |
| **Company Type** | Incubated by the Institute for Interdisciplinary Information Sciences (IIIS), Tsinghua University |
| **Parent Company/Group** | None |
| **Data Source** | Star1 Official Website, IT Home, Phoenix New Media, Brand 100 Network |

## Company Profile

Star1 is incubated by the Institute for Interdisciplinary Information Sciences (IIIS) at Tsinghua University. Its founder, Chen Jianyu, is a doctoral supervisor at Tsinghua University.

The company proposes the concept of "Native General-Purpose Embodied Intelligent Agent = Native Robot Foundation Model + AI-Defined Hardware Platform," emphasizing software-hardware co-evolution and Sim2Real efficiency. STAR1 is known for its high torque, high speed, and high load capacity, and is one of the first humanoid platforms in the industry to publicly demonstrate outdoor running capabilities.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| High-Performance Humanoid | High-dynamic motion, general-purpose manipulation | STAR1 | Scientific research, rescue, home service |
| Dexterous Hand | High-degree-of-freedom end-effector | XHAND1 / XHAND1 Lite / PRO | Scientific research, industry |

## Representative Products

### STAR1

> Star1 STAR1: Please visit the [official website](https://www.robotera.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | 171 cm | Brand 100 Network / robotsj.cn |
| Weight | 63 kg | Brand 100 Network / robotsj.cn |
| Degrees of Freedom | 55 DOF | IT Home / Brand 100 Network |
| Load/Torque | Total load 160 kg; Arm load >20 kg; Joint peak torque 400 N·m | Public reports |
| Speed/Rotation Rate | Max running speed >6 m/s; Outdoor real-world scenario 3.6 m/s | Official claims / Media reports |
| Battery Life | Not disclosed | - |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Self-developed integrated joints, 12 active DOF dexterous hand XHAND1, native robot foundation model, modular "transformable body."

**Application Scenarios**: Scientific research algorithm validation, rescue inspection, home service, heavy object handling.

### XHAND1 Dexterous Hand

| Specification | Value | Notes/Source |
|---|---|---|
| Degrees of Freedom | 12 Active DOF | Brand 100 Network |
| Load | Max single-hand grip 25 kg / 80 N | Brand 100 Network |
| Sensors | Array fingertip tactile sensors | Brand 100 Network |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Fully self-driven five fingers, high-resolution 3D tactile sensing, lateral swing capability, compatible with STAR1 and third-party platforms.

**Application Scenarios**: Fine manipulation, scientific research, industrial grasping.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed integrated joint modules; externally purchased frameless torque motors, planetary gearboxes, encoders, drivers.
- **Downstream Customers/Application Scenarios**: Universities, research institutions, emergency rescue, special operations.
- **Main Competitors/Comparables**: Unitree H1, LimX Dynamics CL-1, Boston Dynamics Atlas.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_star1`
- Product Entity: `ent_product_star1_star1`
- Key Relationships:
  - `ent_company_star1` -- `manufactures` --> `ent_product_star1_star1`
  - `ent_product_star1_star1` -- `uses` --> `ent_component_star1_xhand1`

## References

1. [Star1 Official Website](https://www.robotera.com)
2. [IT Home – Star1 STAR1 Launch](https://www.ithome.com/0/790/117.htm)
3. [Phoenix New Media – Star1 STAR1 Multi-Terrain Running](https://news.qq.com/rain/a/20241015A07P3L00)
4. [Brand 100 Network – Star1 Introduction](https://m.cnpp100.com/brand/152931.html)
5. [Appendix D.4 Key Product Wiki](../index-products.md)
