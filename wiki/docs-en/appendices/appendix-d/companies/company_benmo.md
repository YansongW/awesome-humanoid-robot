# Benmo Technology / Direct Drive Technology

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 本末科技 |
| **English Name** | Benmo Technology / Direct Drive Technology |
| **Headquarters** | Songshan Lake, Dongguan, Guangdong, China |
| **Founded** | 2018 |
| **Website** | [https://directdrive.com](https://directdrive.com) |
| **Supply Chain Role** | Core Components + Complete Machine OEM / Direct Drive Motor Modules + Wheel-Legged Robots |
| **Company Attributes** | Direct Drive Technology, Gearless, Wheel-Legged Robots |
| **Parent Company/Group** | None |
| **Data Source** | Benmo Technology official website, Benmo company introduction PDF, Hard氪 reports |

## Company Profile

Benmo Technology focuses on gearless direct drive motors, providing power modules to the robotics, fitness, and industrial sectors, and has launched complete wheel-legged robots and an open-source platform.

Benmo has R&D and manufacturing facilities in Songshan Lake, Dongguan, with full-chain capabilities from design to mass production of direct drive motor modules. In 2021, it released the world's first commercial direct-drive two-wheel-legged robot "Diablo," in 2023 launched the 8-axis wheel-legged robot TITA, and in 2025 released the modular two-wheel-legged commercial robot D1, continuously expanding into security patrol, logistics delivery, agriculture, and home scenarios.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Direct Drive Power Modules | Robot joints and drive wheels | M06/M07/M11/M15 Series | Sweeping robots, AGV/AMR, fitness equipment |
| Wheel-Legged Robots | Open development platform and complete machines | Diablo / TITA / D1 | Patrol, delivery, mapping, home use |

## Representative Products

### Benmo TITA

> Benmo TITA: Please visit [official materials](https://directdrive.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Standing 510×590×490 mm; Crouching 510×590×300 mm | Benmo company introduction PDF |
| Weight | 24.1 kg (without battery) | Benmo company introduction PDF |
| Degrees of Freedom | 8 DOF | Benmo company introduction PDF |
| Load/Torque | Moving load 10 kg | Benmo company introduction PDF |
| Speed/RPM | Max speed 3 m/s (5 m/s requires API unlock) | Benmo company introduction PDF |
| Battery Life | Approximately 2 hours with dual batteries, hot-swappable | Benmo company introduction PDF |
| Interface/Communication | NVIDIA Jetson Orin NX 16G, RPC/onboard programming, behavior-level and joint-level interfaces | Benmo company introduction PDF |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Quasi-direct drive 8-axis wheel-leg, standing/jumping/obstacle crossing/auto-recovery, top universal rail modular expansion, infrared laser + ultrasonic + binocular camera perception

**Application Scenarios**: Smart campus patrol, logistics delivery, terrain mapping, agriculture, home companionship, mobile filming.

### Benmo Diablo

![Benmo Diablo](https://directdrive.com/public/uploads/images/20220413/f1570d9332275b20e351666402783281.jpg)

> Image source: Benmo Technology official website product image.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Standing 540×371×491 mm; Crouching 540×371×270 mm | Benmo company introduction PDF |
| Weight | 22.9 kg | Benmo company introduction PDF |
| Degrees of Freedom | 6 DOF | Benmo company introduction PDF |
| Load/Torque | Moving load 4 kg; Crawling max load 80 kg | Benmo company introduction PDF |
| Speed/RPM | Max speed 2 m/s | Benmo company introduction PDF |
| Battery Life | Approximately 3 hours (standing state) | Benmo company introduction PDF |
| Interface/Communication | Horizon X3 / Raspberry Pi 4B main controller, expandable LiDAR navigation tower | Benmo company introduction PDF |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: World's first commercial direct-drive self-balancing wheel-legged robot, 6 M1502D direct drive joints, low noise, high dynamic balance

**Application Scenarios**: Security patrol, mapping and surveying, educational development, personal companionship.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed direct drive motors, M15/M07 series joint modules, hub motors, controllers, batteries, and navigation towers (LiDAR).
- **Downstream Customers/Application Scenarios**: Sweeping/service robot manufacturers, AGV/AMR, fitness equipment manufacturers, patrol and logistics customers.
- **Main Competitors/Peers**: Deep Robotics, Unitree Go2, Sunny Optical, wheel-leg solution providers

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_benmo`
- Product Entity: `ent_product_benmo_tita`
- Component Entity: `ent_component_benmo_m1502d`
- Key Relationships:
  - `ent_company_benmo` -- `manufactures` --> `ent_product_benmo_tita`
  - `ent_company_benmo` -- `manufactures` --> `ent_component_benmo_m1502d`
  - `ent_product_benmo_tita` -- `uses` --> `ent_component_benmo_m1502d`

## References

1. [Benmo Technology Official Website](https://directdrive.com)
2. [Benmo Technology Company Introduction PDF](https://www.worldrobotconference.com/profile/robot/download/2025/07/10/250110%20%E6%9C%AC%E6%9C%AB%E7%A7%91%E6%8A%80%E4%BB%8B%E7%BB%8D_20250710110734A073.pdf)
3. [Hard氪 – Benmo Technology Financing Report](http://mp.weixin.qq.com/s?__biz=MzkwMTI4MjU0Mw==&mid=2247520049&idx=2&sn=36133880658fdda8d838fcf5d975fbb0)
