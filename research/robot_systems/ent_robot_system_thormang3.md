---
$id: ent_robot_system_thormang3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: THORMANG3
  zh: THORMANG3 全尺寸人形机器人
  ko: THORMANG3
summary:
  en: A 137.5 cm, 42 kg full-size humanoid robot from ROBOTIS descending from the DARPA Robotics Challenge 2015 finals, with 29 degrees of freedom driven by DYNAMIXEL-P series servos, dual Intel NUC computers, ankle force-torque sensors and a complete ROS1 software stack, sold as a commercial platform with open-source control software and public STP models.
  zh: THORMANG3（Tactical Hazardous Operations Robot 3）是韩国 ROBOTIS 的全尺寸人形机器人，源于 DARPA Robotics Challenge 2015 决赛平台，身高 137.5 cm、重 42 kg，29 个自由度由 29 台 DYNAMIXEL-P 系列一体化伺服驱动，双 Intel NUC 分工运动控制与感知，配脚踝六维力/力矩传感器与完整 ROS1 软件栈，整机 STP 模型官方公开。
  ko: A 137.5 cm, 42 kg full-size humanoid robot from ROBOTIS descending from the DARPA Robotics Challenge 2015 finals, with 29 degrees of freedom driven by DYNAMIXEL-P series servos, dual Intel NUC computers, ankle force-torque sensors and a complete ROS1 software stack, sold as a commercial platform with open-source control software and public STP models.
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
- thormang3
- robotis
- dynamixel_p
- full_size_humanoid
- ros1
- darpa_robotics_challenge
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/thormang3.md（访问日期 2026-07-01）。官方无公开标价，经销商为询价制（交货期 12 周）；本质是商业整机 + 开源控制软件，ROS 软件包长期停更（多数仓库 2016-2018 年后无实质更新）。'
sources:
- id: src_001
  type: website
  title: THORMANG3 e-Manual
  url: https://emanual.robotis.com/docs/en/platform/thormang3/introduction/
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ROBOTIS-THORMANG-COMMON GitHub Repository
  url: https://github.com/robotis-git/robotis-thormang-common
  accessed_at: '2026-07-01'
---

## 概述

THORMANG3（Tactical Hazardous Operations Robot，第三代）是韩国 ROBOTIS 的全尺寸人形机器人，THOR 系列源于 DARPA Robotics Challenge 2015 决赛平台（Team ROBOTIS）。整机高 137.5 cm、重 42 kg，29 个自由度（来源：调研档案 thormang3.md，下同）。

开源属性：ROS 软件包开源于 GitHub（ROBOTIS-GIT/ROBOTIS-THORMANG-* 系列，COMMON 包许可证标记为"Other/未明确"）；整机 STP 三维模型官方公开下载；本质是商业整机 + 开源控制软件。硬件成本未知——官方无公开标价，经销商页面标注"需询价、交货期 12 周"（Cyber Robotics HK，2025 年页面）；历史定位为"相对可负担的全尺寸平台"。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 137.5 cm / 42 kg | e-Manual |
| 自由度 | 29 | e-Manual |
| 价格 | 未知（需询价、交货期 12 周） | 经销商页面 |
| 计算 | 2 台 Intel NUC（Core i5、8GB DDR4、128GB M.2 SSD），分工运动控制（MPC）与感知（PPC）；机载 D-Link DIR-806A 无线路由 | e-Manual |
| 传感器 | Logitech C920 相机；Intel RealSense（选配）；Hokuyo UTM-30LX-EW 激光雷达（选配）；双脚踝 ATI Mini58 六维力/力矩传感器 ×2；MicroStrain 3DM-GX4-25 IMU | e-Manual |
| 电池 | 22V 22000 mAh + 18.5V 11000 mAh 双电池；也可外接电源（执行器需 0-30V/100A 电源） | e-Manual |
| 新手友好度 | 1 / 5（调研档案评估） | 调研档案 |

### 执行器方案

- 29 台 DYNAMIXEL-P（原 DYNAMIXEL PRO）系列一体化伺服（2019 年 6 月起由 PRO 换型为 P 系列）：
  - PH54-200-S500-R（200W）× 10（腿部大关节）
  - PH54-100-S500-R（100W）× 11
  - PH42-020-S300-R（20W）× 8（小关节）
- 谐波减速 + 高功率密度伺服是 DRC 时代全尺寸平台的典型方案，扭矩充足但单台舵机价格昂贵，整机成本主要在此。
- 附带无线急停、吊装带（carabiner + rope）与升降架——全尺寸机型的安全标配。

### 软件栈与文档

- Ubuntu LTS 64 位 + ROS1，C++ 开发；官方提供行走（walking）、操作（manipulation）、感知（PPC）、Gazebo 仿真（COMMON 包）等完整 ROS 包；未提供 ROS2 官方支持（检索时点未见）。
- 全套 e-Manual 教程（快速上手、校准、教程、开发），完善程度与 OP3 同级；STP 模型可用于二次机械设计。
- GitHub `ROBOTIS-GIT/ROBOTIS-THORMANG-COMMON` 仅 5 stars / 10 forks，最后 push 2018-04-01；MPC/PPC/Tools 等兄弟仓库均为 2016 年创建、长期停更，软件栈停留在 ROS1 时代。

### 适合人群

- 适合：有全尺寸平台刚性需求的大学/研究所实验室——29 自由度全尺寸平台、F/T 传感器 + 激光雷达配置齐全、ROBOTIS 文档规范、DRC 血统。
- 门槛：42 kg、137 cm 的全尺寸机型对场地/安全/人员要求极高；价格需询价且必然远超个人预算；ROS1 软件栈陈旧，维护投入大；完全不适合个人新手——想玩全尺寸请直接看 OpenLoong 的仿真框架。

## 参考

- [THORMANG3 e-Manual](https://emanual.robotis.com/docs/en/platform/thormang3/introduction/)
- [ROBOTIS-THORMANG-COMMON 仓库](https://github.com/robotis-git/robotis-thormang-common)
- [ROS wiki: ROBOTIS](http://wiki.ros.org/ROBOTIS)
