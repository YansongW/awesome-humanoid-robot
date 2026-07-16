---
$id: ent_robot_system_robotis_op3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: ROBOTIS OP3 (DARwIn-OP Series)
  zh: ROBOTIS OP3 人形机器人（DARwIn-OP 系列）
  ko: ROBOTIS OP3 (DARwIn-OP Series)
summary:
  en: A 510 mm, 3.5 kg open-platform humanoid robot from ROBOTIS, the third generation of the NSF-funded DARwIn-OP line, with 20 degrees of freedom driven by DYNAMIXEL XM430-W350-R smart servos, an Intel NUC onboard computer and a ROS2-native software stack, widely used in education and RoboCup.
  zh: ROBOTIS OP3 是韩国 ROBOTIS 推出的开放平台人形机器人，为 NSF 资助的 DARwIn-OP（达尔文开放平台）产品线第三代，身高约 510 mm、重约 3.5 kg，20 个自由度由 20 台 DYNAMIXEL XM430-W350-R 智能舵机驱动，主控 Intel NUC + OpenCR，2025 年复刻版原生转向 ROS2，教学文档与 RoboCup 生态成熟。
  ko: A 510 mm, 3.5 kg open-platform humanoid robot from ROBOTIS, the third generation of the NSF-funded DARwIn-OP line, with 20 degrees of freedom driven by DYNAMIXEL XM430-W350-R smart servos, an Intel NUC onboard computer and a ROS2-native software stack, widely used in education and RoboCup.
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
- robotis_op3
- darwin_op
- robotis
- dynamixel
- ros2
- robocup
- education
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/robotis-op3-darwin-op.md（访问日期 2026-07-01）。该平台本质是"开放平台的商业整机"而非社区开源硬件项目：ROS 软件包 Apache-2.0，整机只能购买成品。'
sources:
- id: src_001
  type: website
  title: ROBOTIS OP3 e-Manual
  url: https://emanual.robotis.com/docs/en/platform/op3/introduction/
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ROBOTIS-GIT/ROBOTIS-OP3 GitHub Repository
  url: https://github.com/ROBOTIS-GIT/ROBOTIS-OP3
  accessed_at: '2026-07-01'
---

## 概述

ROBOTIS OP3 是韩国 ROBOTIS 主导的开放平台人形机器人，其前身为 DARwIn-OP（Dynamic Anthropomorphic Robot with Intelligence – Open Platform，达尔文开放平台）——2010 年由 Virginia Tech RoMeLa（Dennis Hong 团队）牵头，联合 University of Pennsylvania、Purdue University 与 ROBOTIS 开发，美国 NSF 资助。OP3 高约 510 mm、重约 3.5 kg（无外壳），20 个自由度（来源：调研档案 robotis-op3-darwin-op.md，下同）。

开源属性：OP3 ROS 软件包 Apache-2.0（GitHub ROBOTIS-GIT）；DARwIn-OP 硬件 CAD 与软件历史上免费公开（SourceForge `darwinop` 项目页仍可访问）；本质是"开放平台的商业整机"，非社区开源硬件项目。价格：OP3 现价 $13,764.35（robotis.us，2026 年页面快照）；Generation Robots 约 €12,113（含税）；DARwIn-OP 2010 年售价 $12,000（教育折扣 $9,600），第三方 3D 打印克隆约 $6,100。OP（DARwIn-OP）与 OP2 已停产（e-Manual 官方 WARNING），OP3 为当前在售型号。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | OP3 约 510 mm / 约 3.5 kg；DARwIn-OP 455 mm / 2.8 kg | e-Manual / RoMeLa |
| 自由度 | 20 | e-Manual |
| 价格 | OP3 $13,764.35（美国）/ 约 €12,113（欧洲） | robotis.us / Generation Robots |
| 主控 | Intel NUC（Core i3 双核、8GB DDR4、250GB M.2 SSD）；子控制器 OpenCR | e-Manual |
| 传感器 | Logitech C920 摄像头、IMU（陀螺+加速度计+磁力计各 3 轴）、扬声器、RGB LED、4 按键 | e-Manual |
| 电池 | 3 芯 11.1V LiPo（新版 3300 mAh），支持热插拔换电 | e-Manual |
| 新手友好度 | 3 / 5（调研档案评估） | 调研档案 |

### 执行器方案

- OP3：20 台 DYNAMIXEL XM430-W350-R 智能舵机（减速比 353.5:1，失速扭矩 4.1 N·m，支持电流环力控、DYNAMIXEL Protocol 2.0）。
- DARwIn-OP：20 台 MX-28（内置 maxon RE-max 电机，失速扭矩 2.5 N·m，Protocol 1.0）。
- 高减速比舵机方案：位置控制精度高、易用，但无本体感知力控能力，不适合高动态运动控制研究。

### 软件栈与文档

- 2025 年 OP3 复刻版原生转向 ROS2（e-Manual 口径），配套 DYNAMIXEL SDK，C++ 开发，Ubuntu 64 位；官方提供行走/动作编辑（op3_action_editor）、Gazebo 仿真模型等 ROS 包。
- ROBOTIS e-Manual 极其完善（规格、装配、教程、ROS 包逐条文档），是行业文档标杆；RoboCup 足球生态积累深厚（DARwIn-OP 曾获 RoboCup 2011、2012 儿童组冠军）。
- GitHub `ROBOTIS-GIT/ROBOTIS-OP3` 约 157 stars / 65 forks，最近 push 2025-02-26（伴随 2025 ROS2 复刻更新）。

### 适合人群

- 适合：预算充足的学校/实验室教学与 RoboCup 参赛——开箱即用的成熟产品、文档顶级、舵机即插即用、ROS2 生态入门路径清晰；对只想写上层算法不想造硬件的用户省事。
- 门槛：约 $1.4 万美元的价格对个人爱好者过高；"开源"主要体现在软件与 CAD 层面，整机只能买成品；舵机方案学不到准直驱/力控等当前主流技术。

## 参考

- [ROBOTIS OP3 e-Manual](https://emanual.robotis.com/docs/en/platform/op3/introduction/)
- [ROBOTIS-GIT/ROBOTIS-OP3 GitHub 仓库](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3)
- [DARwIn-OP 项目页（RoMeLa）](https://www.romela.org/darwin-op-open-platform-humanoid-robot-for-research-and-education/)
