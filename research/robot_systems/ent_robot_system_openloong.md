---
$id: ent_robot_system_openloong
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: OpenLoong (Qinglong) Open-Source Humanoid Robot
  zh: OpenLoong / 青龙开源人形机器人
  ko: OpenLoong (Qinglong) Open-Source Humanoid Robot
summary:
  en: The full-size open-source humanoid reference platform from China's National and Local Co-built Humanoid Robot Innovation Center, 185 cm and over 80 kg with 43 active degrees of freedom including dexterous hands, open-sourced under the OpenAtom Foundation with an MPC plus WBC whole-body control framework deployable in MuJoCo.
  zh: OpenLoong（开放龙）/ 青龙是国家地方共建人形机器人创新中心推出的全尺寸开源人形机器人公版机，身高超 185 cm、体重超 80 kg，全身 43 个主动自由度（含五指灵巧手），经开放原子开源基金会孵化运营，开源内容包括硬件图纸、基于 MPC + WBC 的全身动力学控制框架（可部署于 MuJoCo 仿真）与数据集。
  ko: The full-size open-source humanoid reference platform from China's National and Local Co-built Humanoid Robot Innovation Center, 185 cm and over 80 kg with 43 active degrees of freedom including dexterous hands, open-sourced under the OpenAtom Foundation with an MPC plus WBC whole-body control framework deployable in MuJoCo.
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
- openloong
- qinglong
- full_size_humanoid
- mpc
- whole_body_control
- ethercat
- openatom
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/openloong-qinglong.md（访问日期 2026-07-01）。BOM 成本与执行器具体型号在公开检索中未见统一规格表，标注为未知；硬件/数据集仓库许可证为自定义或未明确（NOASSERTION）。'
sources:
- id: src_001
  type: website
  title: OpenLoong-Dyn-Control GitHub Repository (loongOpen)
  url: https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OpenLoong on AtomGit
  url: https://atomgit.com/openloong
  accessed_at: '2026-07-01'
---

## 概述

OpenLoong（开放龙）/ "青龙"（Qinglong）是由国家地方共建人形机器人创新中心（上海，2023-12-28 成立、2024-05-17 揭牌）与人形机器人（上海）有限公司推出的全尺寸开源人形机器人公版机，2024-12-19 通过开放原子开源基金会（OpenAtom）TOC 评审，捐赠基金会孵化运营。整机身高超 185 cm、体重超 80 kg，全身 43 个主动自由度（含五指灵巧手，覆盖头/臂/腿/腰/踝）（来源：调研档案 openloong-qinglong.md，下同）。

项目定位是产业"公版机/根技术"，被媒体称为全球首个全尺寸人形全栈开源（硬件图纸 + MPC/WBC 控制 + 数据集）。主要代码仓库采用 Apache-2.0 许可证；OpenLoong-Hardware、OpenLoong-Dataset 许可证为自定义/未明确（GitHub 标记 NOASSERTION）。硬件成本未知——开源公版机不自售，媒体口径"最终由生产商定价"。2025-08 社区另推出更轻量、更低成本的 NanoLoong（小型双足）并已开源。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 超 185 cm / 超 80 kg | 媒体与官方演讲口径 |
| 主动自由度 | 43（含五指灵巧手） | 媒体报道 |
| 硬件成本（BOM） | 未知（公版机不自售，由生产商定价） | 调研档案 |
| 主控 | 400 TOPS 高算力控制器；具身智能操作系统（us 级响应目标） | 2024 WAIC 发布口径 |
| 总线 | EtherCAT | 行业分析文章与 SDK 仓库佐证 |
| 新手友好度 | 2 / 5（调研档案评估） | 调研档案 |

### 执行器与硬件

- 2024 款"青龙"以旋转执行器为主驱动单元（2024 WAIC 官方演讲口径）；下一代公版机计划采用直线执行器。
- 具体电机/减速器型号、扭矩参数未见统一规格表，需查阅 OpenLoong-Hardware 仓库的选型文件。
- 硬件开源包含设计指标、STEP 模型、电路原理图、安装维护手册。
- 传感器：官方未发布统一清单；生态项目（dora-rs/dora-openloong）实机集成 Intel RealSense D435 RGB-D 相机与麦克风阵列。

### 软件栈

- OpenLoong-Dyn-Control：基于 MPC（模型预测控制）+ WBC（全身控制）的全身动力学控制框架，可部署于 MuJoCo 仿真，提供行走/跳跃/盲踩障碍三个示例，已在实物样机实现行走与盲踩障碍；内置主要依赖、分层模块化、强调易部署/易扩展/易理解。
- 其他仓库：Gymloong（训练平台）、MiniGym、Unity-RL-Playground、OpenLoong-ROS、OpenLoong-Brain（大模型技能调度）、loong_driver_sdk、loong_sim/loong_deployment、OpenLoong-Dataset（行走/桌面分拣/场景作业数据）。
- 同步发布于 GitHub（`loongOpen` 组织）与 AtomGit（atomgit.com/openloong）；软件层另有"朱雀"大脑大模型、"玄武"小脑强化学习模型、"白虎"数据集、"麒麟"训练场等配套体系（属创新中心整体生态，非全部开源）。

### 社区与适合人群

- openloong.org.cn 社区 + SIG 组 + 线上线下活动（ROSCon China、ROS 暑期学校合作）；中文文档为主，对国内开发者友好，英文资料少。
- GitHub 星标快照：OpenLoong-Dyn-Control 339 stars、Unity-RL-Playground 315 stars、OpenLoong-Hardware 115 stars（2026-07-01 检索时点），组织整体在维护。
- 适合：国内高校/企业团队做全尺寸整机二次开发；185 cm / 80 kg 全尺寸机型个人无法在家复现，个人新手建议只用其 MuJoCo 控制框架做学习，或关注 NanoLoong。

## 参考

- [OpenLoong-Dyn-Control 仓库（MPC+WBC 框架）](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md)
- [AtomGit 镜像](https://atomgit.com/openloong)
- [dora-rs/dora-openloong 生态项目](https://github.com/dora-rs/dora-openloong)
