# Black Sesame Technologies

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 黑芝麻智能 |
| **English Name** | Black Sesame Technologies |
| **Headquarters** | Wuhan, Hubei Province, China |
| **Founded** | 2016 |
| **Website** | [https://www.blacksesame.com.cn](https://www.blacksesame.com.cn) |
| **Supply Chain Role** | Autonomous driving chips, edge AI computing, robot perception computing |
| **Company Type** | Listed company (Hong Kong Stock Exchange: 02533) |
| **Parent Company/Group** | None (independently listed entity) |
| **Data Source** | Black Sesame Technologies official website, Hong Kong Stock Exchange prospectus, product launches, public press releases |

## Company Overview

Black Sesame Technologies is a leading intelligent vehicle computing chip company in China, focusing on autonomous driving chips and perception solutions, and expanding into embodied intelligence scenarios such as robotics.

Black Sesame Technologies has developed the self-designed Huashan series of high-performance autonomous driving chips and the Wudang series of cross-domain computing chips, providing a complete computing platform from perception to decision-making. Its chips feature high computing power, low latency, and functional safety, supporting high-level autonomous driving and robot tasks such as multi-sensor fusion, SLAM, and path planning.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| Huashan Series | High-performance autonomous driving chips | Huashan A1000 / A2000 | Autonomous driving, robot brain |
| Wudang Series | Cross-domain computing chips | Wudang C1200 | Cockpit-driving integration, robot control |
| Perception Solution | Algorithms and middleware | BSS Perception | Autonomous driving, robot perception |

## Representative Products

### Black Sesame Technologies Huashan A1000

> Black Sesame Technologies Huashan A1000: Please visit [official materials](https://www.blacksesame.com.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Architecture | Self-developed NeuralIQ ISP + DynamAI NN engine | Black Sesame public materials |
| Process Node | 16 nm (public reports) | Public reports |
| Computing Power | INT8 approx. 58 TOPS; single chip supports L2+/L3 autonomous driving | Black Sesame public materials |
| CPU | ARM Cortex-A55 multi-core | Public reports |
| Functional Safety | ASIL-B / ASIL-D (target for some modules) | Black Sesame public materials |
| Interfaces | Multi-channel camera, LiDAR, millimeter-wave radar interfaces | Black Sesame public materials |
| Power Consumption | Approx. 15–25 W | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: Self-developed ISP and NN engine, multi-sensor fusion, automotive-grade functional safety, scalable to multi-chip solutions.

**Application Scenarios**: Autonomous driving domain controller, robot perception and decision-making, multi-modal fusion positioning.

### Black Sesame Technologies Wudang C1200

> Black Sesame Technologies Wudang C1200: Please visit [official materials](https://www.blacksesame.com.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Positioning | Cross-domain computing chip (cockpit-driving integration) | Black Sesame public materials |
| Process Node | 7 nm (public reports) | Public reports |
| Computing Power | Not disclosed | - |
| Functional Safety | Supports ASIL-D | Black Sesame public materials |
| Interfaces | Supports multi-channel cameras, display, automotive Ethernet | Black Sesame public materials |
| Application Scenarios | Intelligent vehicles, robot control hub | Black Sesame public materials |
| Power Consumption | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Single-chip cross-domain integration, reduces vehicle wiring harness and cost, designed for next-generation electronic/electrical architecture.

**Application Scenarios**: Integration of intelligent cockpit and autonomous driving, robot central computing platform.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, packaging and testing, automotive-grade memory, ISP/NN IP, automotive Ethernet PHY, PCB.
- **Downstream Customers/Application Scenarios**: OEMs, Tier 1 suppliers, autonomous driving solution providers, robot manufacturers, sensor vendors.
- **Main Competitors/Peers**: NVIDIA DRIVE, Mobileye EyeQ, Horizon Journey, Huawei Ascend/MDC, Qualcomm Snapdragon Ride.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_black_sesame`
- Product Entity: `ent_product_black_sesame_a1000`
- Component Entity: `ent_component_black_sesame_a1000_chip`
- Key Relationships:
  - `ent_company_black_sesame` -- `manufactures` --> `ent_product_black_sesame_a1000`
  - `ent_company_black_sesame` -- `manufactures` --> `ent_component_black_sesame_a1000_chip`
  - `ent_product_black_sesame_a1000` -- `uses` --> `ent_component_black_sesame_a1000_chip`

## References

1. [Black Sesame Technologies Official Website](https://www.blacksesame.com.cn)
2. [Black Sesame Technologies Huashan Series](https://www.blacksesame.com.cn/products/1.html)
3. Black Sesame Technologies Hong Kong Stock Exchange Prospectus
