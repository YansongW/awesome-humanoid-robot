---
$id: ent_robot_system_upkie
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Upkie Wheeled Biped Robot
  zh: Upkie 轮足双足机器人
  ko: Upkie Wheeled Biped Robot
summary:
  en: A fully open-source wheeled biped robot built from about 3,000 USD of off-the-shelf components plus 3D-printed parts, using mjbots quasi-direct-drive actuators and a Raspberry Pi 4, with Python-first software and out-of-the-box PID, MPC and reinforcement-learning balancing examples.
  zh: Upkie 是社区驱动的全开源轮足双足机器人（wheeled biped），约 3,000 美元现成组件加 60 小时以上 3D 打印即可复现，采用 mjbots qdd100 准直驱执行器与树莓派 4 主控，Python 优先的软件栈开箱自带 PID、MPC、强化学习三种平衡控制示例，是个人在真实硬件上学习平衡控制的低门槛路径。
  ko: A fully open-source wheeled biped robot built from about 3,000 USD of off-the-shelf components plus 3D-printed parts, using mjbots quasi-direct-drive actuators and a Raspberry Pi 4, with Python-first software and out-of-the-box PID, MPC and reinforcement-learning balancing examples.
domains:
- 02_components
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- system
- knowledge
tags:
- open_source
- wheeled_biped
- upkie
- mjbots
- quasi_direct_drive
- raspberry_pi
- python
- education
- balancing_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/upkie.md（访问日期 2026-07-01），事实均来自其列出的 GitHub 仓库、Hackaday 项目页、PyPI 文档与 FOSDEM 2026 演讲页。身高/重量未见官方统一数值，标注为未知。'
sources:
- id: src_001
  type: website
  title: upkie/upkie GitHub Repository
  url: https://github.com/upkie/upkie
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Upkie Wheeled Biped Robots on Hackaday
  url: https://hackaday.io/project/185729-upkie-wheeled-biped-robots
  accessed_at: '2026-07-01'
- id: src_003
  type: website
  title: upkie on PyPI
  url: https://pypi.org/project/upkie/
  accessed_at: '2026-07-01'
---

## 概述

Upkie 是社区驱动的开源轮足双足机器人（wheeled biped），核心作者为 Stéphane Caron（Inria）等，建立在 mjbots 开源执行器生态之上，含 Upkie Zero / Upkie Standard / 2026 硬件 v2 等构型。整机约 3,000 美元现成组件 + 60 小时以上 3D 打印即可复现（官方 Hackaday 口径），6 个自由度（每腿 3：髋、膝、驱动轮）；身高/重量未见官方统一数值（来源：调研档案 upkie.md，下同）。

许可证为 Apache-2.0（轮胎网格 CC BY 4.0），所用 mjbots 执行器的固件/硬件/软件同样全开源——从电机固件到上层控制全链路可改。GitHub 仓库 `upkie/upkie` 386 stars / 52 forks（2026-07-01 快照，仍高频更新），`upkie/parts`（CAD/打印件）与 `upkie/upkie_description`（URDF）同步维护，被 awesome-open-source-robots 等知名清单收录。轮足形态靠轮保持平衡、靠腿应对不平地形，相比纯步行双足控制难度与机械风险显著降低。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 自由度 | 6（每腿 3：髋、膝、驱动轮） | 调研档案 |
| 硬件成本 | 约 $3,000 现成组件 + 60 小时以上 3D 打印 | Hackaday 官方项目页 |
| 主控 | Raspberry Pi 4 + mjbots pi3hat（CAN 扩展板）+ 电源分配板 | 调研档案 |
| 传感器 | IMU 集成于 pi3hat；可选 OAK-D Lite 相机支架等社区配件 | 调研档案 |
| 身高 / 重量 | 未知（桌面级轮足，因构型而异） | 调研档案 |
| 新手友好度 | 4 / 5（调研档案评估） | 调研档案 |

### 执行器方案

- mjbots qdd100 准直驱（quasi-direct-drive）无刷伺服 ×4（髋/膝）+ moteus 驱动器（轮），全部固件开源、可力控。
- 轮足混合形态：靠轮保持平衡、靠腿应对不平地形，摔机代价小，成功率高。

### 软件栈

- Python 或 C++，Linux/macOS 开发、部署到机上树莓派；`pixi`/`uv` 一条命令即可跑仿真示例（PyBullet），仿真零成本上手，无需先买硬件。
- 开箱自带三种平衡控制范式示例：PID、MPC（qpmpc）、强化学习（Stable-Baselines3）；Gymnasium 标准接口；另有社区 GPU RL 方案（MjLab Upkie）。
- 不依赖 ROS（可用 xacro/URDF 描述，兼容 Pinocchio 等库）。

### 文档与社区

- 逐步构建指南（step-by-step build instructions）+ Hackaday 项目页 + GitHub Discussions/聊天室；FOSDEM 2026 有官方经验分享演讲并现场发布硬件 v2（躯干一体化打印、腿部重新设计、宽度缩减 6 cm）。
- 中文创客社区（DFRobot 等）有翻译报道。

### 适合人群

- 适合：想在真实硬件上学平衡控制/RL 部署的个人开发者与课程项目；可作为进阶纯双足（如 Berkeley Humanoid Lite）前的练兵平台。
- 门槛：60+ 小时打印与装配仍需耐心；轮足不是"走路"的人形，若目标是仿人步态研究则不匹配。

## 参考

- [upkie/upkie GitHub 仓库](https://github.com/upkie/upkie)
- [Hackaday 官方项目页（$3,000 组件、60+ 小时打印）](https://hackaday.io/project/185729-upkie-wheeled-biped-robots)
- [PyPI 文档](https://pypi.org/project/upkie/)
- [FOSDEM 2026 演讲页](https://fosdem.org/2026/schedule/event/8PUMMD-open-source-robotics-practice-upkie-wheeled-bipeds/)
