---
$id: ent_robot_system_bruce
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: BRUCE (Bipedal Robot Unit with Compliance Enhanced)
  zh: BRUCE 儿童尺寸人形机器人
  ko: BRUCE (Bipedal Robot Unit with Compliance Enhanced)
summary:
  en: A 70 cm, 4.8 kg child-size bipedal humanoid platform co-developed by Westwood Robotics and UCLA RoMeLa, with 16 degrees of freedom, proprioceptive quasi-direct-drive Koala BEAR actuators with liquid cooling on key joints, and a variable-frequency MPC stack for highly dynamic walking, running and jumping.
  zh: BRUCE（Bipedal Robot Unit with Compliance Enhanced）是 Westwood Robotics（西木科技）与 UCLA RoMeLa 联合开发的 70 cm / 4.8 kg 儿童尺寸双足人形平台，16 个自由度，搭载本体感知准直驱 Koala BEAR 执行器（关键关节液态冷却），采用可变周期 MPC 运控算法支持行走/跑步/跳跃等高动态行为，整机以商务采购渠道获取。
  ko: A 70 cm, 4.8 kg child-size bipedal humanoid platform co-developed by Westwood Robotics and UCLA RoMeLa, with 16 degrees of freedom, proprioceptive quasi-direct-drive Koala BEAR actuators with liquid cooling on key joints, and a variable-frequency MPC stack for highly dynamic walking, running and jumping.
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
- humanoid_robot
- bruce
- westwood_robotics
- ucla_romela
- quasi_direct_drive
- liquid_cooling
- mpc
- high_dynamic_locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/bruce-westwood.md（访问日期 2026-07-01）。官方宣称开源软件与模型，但整机控制框架的公开仓库在检索中未找到，整机开源程度存疑；价格约 $6.5K 来自第三方论文对比表（ToddlerBot, arXiv:2502.00893 Table I），官方为询价制。'
sources:
- id: src_001
  type: website
  title: Westwood-Robotics GitHub Organization
  url: https://github.com/Westwood-Robotics
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: BRUCE at World Robot Conference
  url: https://www.worldrobotconference.com/ex/product/244.html
  accessed_at: '2026-07-01'
- id: src_003
  type: website
  title: BRUCE on aparobot.com
  url: https://www.aparobot.com/robots/bruce
  accessed_at: '2026-07-01'
---

## 概述

BRUCE（Bipedal Robot Unit with Compliance Enhanced）是 Westwood Robotics（西木科技，2018 年由 UCLA RoMeLa 前核心成员创立）与 UCLA RoMeLa 联合开发的儿童尺寸双足人形平台，设计论文为 Liu et al., ICRA 2022。整机高 70 cm、重 4.8 kg，16 个自由度（每条腿 5、每条臂 3），是"能跑能跳"的少数派小型高动态双足平台（来源：调研档案 bruce-westwood.md，下同）。

开源情况需要说清楚：官方定位为"开放平台（open platform）"，宣称开源软件与模型，但整机控制框架的公开仓库在 GitHub 检索中未找到（截至 2026-07-01，未能直接验证其许可证条款）；组件级仓库（PyBEAR、BRUCE_SENSE、Wireless_ESTOP 等）开源于 `Westwood-Robotics` 组织。硬件成本方面，第三方论文对比表（ToddlerBot, arXiv:2502.00893 Table I）列为约 $6.5K 量级；官方页面为询价制，未公开标价，获取渠道为商务采购而非自助复刻。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 70 cm / 4.8 kg | WRC 展品页 / 第三方论文 |
| 自由度 | 16（腿 5×2、臂 3×2） | WRC 展品页 |
| 硬件成本 | 约 $6.5K 量级（第三方论文对比表）；官方询价制 | ToddlerBot 论文 Table I |
| 主控 | 算力 6 TOPS、8GB 内存、32GB 存储，支持主流深度学习框架 | 展品页口径 |
| 传感器 | 4 个足底接触传感器；6 轴 IMU，通信/采样速率 2 kHz | aparobot.com |
| 电池 | 3000 mAh，连续动态运行约 20 分钟；独立无线急停装置 | aparobot.com |
| 新手友好度 | 2 / 5（调研档案评估） | 调研档案 |

### 执行器方案

- 自研 Koala BEAR 本体感知（proprioceptive）准直驱执行器：单台仅 250 g，峰值扭矩 10.5 N·m（腿部关节口径）；关键关节（膝等）采用液态冷却以支撑爆发力矩与持续高动态输出。
- 碳纤维复合材料骨架，拓扑优化，高度模块化，便于维修更换——技术血统与 UCLA ARTEMIS 的 BEAR 系列执行器一致（半直驱/QDD 路线）。

### 软件栈

- 可变周期（variable-frequency）MPC 运控算法，支持行走/跑步/跳跃等高动态行为；模型库与仿真环境被多篇第三方论文用作 benchmark（如 arXiv:2511.00840 的步态规划对比研究）。
- 官方宣称"开源软件和模型""积极迭代 GitHub Repo 和 Wiki"；实际公开内容以执行器（PyBEAR）、传感（BRUCE_SENSE）、无线急停等组件级仓库为主；无 ROS/ROS2 官方栈的公开证据。

### 适合人群

- 适合：高校实验室做高动态双足运控研究——70 cm / 4.8 kg 小体型 + 准直驱 + 液冷，BEAR 执行器与 MPC 栈对研究高动态运控的人很有价值；被多所欧美大学与研究公司采用（如 UCL）。
- 门槛：整机开源程度存疑（公开仓库只见组件级），个人无法自助复刻，只能商务采购；文档面向专业用户；不建议作为 0→1 首台机器人，新手可关注其开源组件（PyBEAR 等）学习准直驱执行器。

## 参考

- [Westwood-Robotics GitHub 组织（组件级开源仓库）](https://github.com/Westwood-Robotics)
- [WRC 展品页](https://www.worldrobotconference.com/ex/product/244.html)
- [aparobot.com 产品页](https://www.aparobot.com/robots/bruce)
