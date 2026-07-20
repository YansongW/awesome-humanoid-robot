# Keli Sensing Technology

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Keli Sensing Technology |
| **English Name** | Keli Sensing Technology |
| **Headquarters** | Ningbo, Zhejiang, China |
| **Founded** | 1995 |
| **Website** | [https://www.kelichina.com](https://www.kelichina.com) |
| **Supply Chain Role** | Strain gauge sensors, six-axis force/torque sensors, Industrial IoT |
| **Company Type** | Listed company (Shanghai Stock Exchange: 603662), National Manufacturing Single Champion |
| **Parent Company/Group** | Independently listed |
| **Data Source** | Keli Sensing Technology official website, annual reports, SSE e-interaction, public research reports |

## Company Overview

Keli Sensing Technology is a leading sensor and IoT system integrator in China, maintaining the top market share in the domestic mechanical sensor market for over a decade.

The company started with strain gauge load cells and has gradually expanded into multi-physics sensors, industrial IoT platforms, and robot sensors. In the robotics field, Keli Sensing Technology focuses on six-axis force/torque sensors, joint torque sensors, and tactile sensors. It has provided samples or supplied products to customers such as SAIC-GM-Wuling, Zhiyuan Robot, Huawei, and ByteDance, aiming to become a core global supplier of full-body sensors for robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Mechanical Sensors & Instruments | Weighing/Force Measurement | SBE / KELI Series | Industrial scales, automation equipment |
| Six-Axis Force/Torque Sensors | Robot end-effector and joint force control | KL6D-M30-B Series | Humanoid robots, collaborative robots |
| Joint Torque Sensors | Rotary joint torque | Not disclosed | Humanoid robots, industrial robots |
| Industrial IoT | Scenario-based system integration | Smart logistics, intelligent warehousing | Smart manufacturing, smart cities |

## Representative Products

### Keli Sensing Technology KL6D-M30-B Series Six-Axis Force Sensor

> Keli KL6D-M30-B: Please visit the [official website](https://www.kelichina.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Robot-specific six-axis force sensor | Public reports |
| Accuracy | 0.1% FS | Public reports |
| Sampling Rate | 1 kHz | Public reports |
| Measurement Principle | High-precision resistance strain gauge | Public reports |
| Communication Method | High-speed sampling digital communication (external data acquisition) | Public reports |
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Designed specifically for robot wrists, ankles, and industrial robotic arm end-effectors, combining structural decoupling with algorithmic decoupling to achieve high-speed sampling digital communication.

**Application Scenarios**: Force control for humanoid robot wrists/ankles, collaborative robot end-effectors, force detection for industrial robotic arms, precision assembly.

### Keli Sensing Technology SBE Strain Gauge Sensor

> Keli SBE: Please visit the [official website](https://www.kelichina.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Strain gauge force sensor | Distributor information |
| Measurement Principle | Resistance strain gauge | Distributor information |
| Features | High accuracy, stable structure, good linearity and repeatability | Distributor information |
| Application Areas | Weighing, force measurement, industrial automation, quality control | Distributor information |
| Range | Not disclosed | - |
| Accuracy | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: High long-term reliability, suitable for integration into various weighing and force measurement systems.

**Application Scenarios**: Industrial automation production lines, testing machines, weighing systems, automotive testing.

## Supply Chain Position

- **Upstream Key Components/Materials**: Strain gauges, high-performance steel, ASIC chips, packaging materials, precision machining
- **Downstream Customers/Application Scenarios**: Industrial scales, humanoid robots, collaborative robots, automotive OEMs, smart logistics, smart cities
- **Main Competitors/Peers**: Yuli Instrument, Kunwei Technology, HBM, Vishay, Hanwei Technology

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_keli`
- Product Entity: `ent_component_keli_kl6d_m30b`
- Product Entity: `ent_component_keli_sbe`
- Key Relationships:
  - `ent_company_keli` -- `manufactures` --> `ent_component_keli_kl6d_m30b`
  - `ent_company_keli` -- `manufactures` --> `ent_component_keli_sbe`
  - `ent_component_keli_kl6d_m30b` -- `used_in` --> `ent_product_humanoid_robot_wrist`

## References

1. [Keli Sensing Technology Official Website](https://www.kelichina.com)
2. [Sina Finance – Keli Sensing Technology Sends Six-Axis Force Sensor Samples to Zhiyuan](https://finance.sina.com.cn/stock/relnews/cn/2025-04-03/doc-inerwmtr2673181.shtml)
3. [Humanoid Robot Core Components Report – Keli Sensing Technology](http://mp.weixin.qq.com/s?__biz=MzIxNTcxNTczNQ==&mid=2247528030&idx=1&sn=3b1493830db732656e3ba2fc0ac3de39)
4. [Appendix D: Product Catalog](../index-products.md)
