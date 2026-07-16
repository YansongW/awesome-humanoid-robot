---
$id: ent_robot_system_toddlerbot
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: ToddlerBot
  zh: ToddlerBot 幼儿机器人
  ko: ToddlerBot
summary:
  en: An open-source child-size humanoid robot from Stanford University, 0.56 m tall and 3.4 kg, with 30 active degrees of freedom, a bill of materials of about 6,000 USD, ROBOTIS Dynamixel bus servos and an onboard Jetson Orin NX, designed for reproducible machine-learning loco-manipulation research at home.
  zh: ToddlerBot 是斯坦福大学开源的幼儿尺寸人形机器人，身高 0.56 m、重 3.4 kg，全身 30 个主动自由度，BOM 约 6,000 美元，采用 ROBOTIS Dynamixel 总线舵机与 Jetson Orin NX 机载电脑，纯 Python 软件栈，目标是在家可复现的机器学习全身运动操作研究平台。
  ko: An open-source child-size humanoid robot from Stanford University, 0.56 m tall and 3.4 kg, with 30 active degrees of freedom, a bill of materials of about 6,000 USD, ROBOTIS Dynamixel bus servos and an onboard Jetson Orin NX, designed for reproducible machine-learning loco-manipulation research at home.
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
- toddlerbot
- stanford
- research_platform
- dynamixel
- 3d_printed
- reinforcement_learning
- imitation_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/toddlerbot.md（访问日期 2026-07-01），事实均来自其列出的 GitHub 仓库、项目主页与论文 arXiv:2502.00893。'
sources:
- id: src_001
  type: website
  title: hshi74/toddlerbot GitHub Repository
  url: https://github.com/hshi74/toddlerbot
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ToddlerBot Project Page
  url: https://toddlerbot.github.io/
  accessed_at: '2026-07-01'
- id: src_003
  type: paper
  title: 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation (arXiv:2502.00893)'
  url: https://arxiv.org/html/2502.00893v2
  accessed_at: '2026-07-01'
---

## 概述

ToddlerBot 是斯坦福大学（TML 与 REALab，作者 Haochen Shi、Weizhuo Wang、Shuran Song、C. Karen Liu）发起的开源幼儿尺寸人形机器人，论文发表于 CoRL 2025（arXiv:2502.00893）。整机高 0.56 m、重 3.4 kg，全身 30 个主动自由度（每条臂 7、每条腿 6、颈 2、腰 2，不含末端执行器），总 BOM 约 6,000 美元，其中约 90% 花在电机与电脑上（来源：调研档案 toddlerbot.md，下同）。

许可证方面，代码与文档采用 MIT License；设计文件（Onshape、STL）采用非商业型 CC 许可，商用受限。项目设计目标是"在家可复现"：3D 打印结构件、现成舵机、pip 一键安装的纯 Python 软件栈，并有论文级复现验证——一名无硬件经验的 CS 学生 3 天内独立完成整机装配（含打印）。GitHub 仓库 `hshi74/toddlerbot` 约 718 stars / 88 forks（2026-07-01 快照，高度活跃），并有 Discord 与微信社区。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 0.56 m / 3.4 kg（3,484 g） | 论文 arXiv:2502.00893 |
| 主动自由度 | 30（臂 7×2、腿 6×2、颈 2、腰 2） | 项目主页 / 论文 |
| 硬件成本（BOM） | 约 $6,000（90% 为电机与电脑） | 论文 |
| 主控 | NVIDIA Jetson Orin NX 16GB | 论文 |
| 传感器 | 双鱼眼相机、胸部 IMU、扬声器、双麦克风 | 项目主页 |
| 续航 | 行走 RL 策略约 19 分钟（过热降频为止） | 项目主页 |
| 新手友好度 | 4.5 / 5（调研档案评估） | 调研档案 |

### 执行器与机械设计

- 采用 ROBOTIS Dynamixel 总线舵机，共 5 种型号按关节空间/扭矩/成本选型（具体型号清单在论文补充材料 VIII-E，档案未逐一列出）。
- 通信为 5V TTL 串行协议、2 Mbps 波特率，30 台电机全状态反馈 50 Hz，使用现成通信板即可。
- 传动设计：直齿轮（臂轴对齐）、耦合锥齿轮（腰 yaw/roll 两电机耦合）、平行连杆（膝、颈 pitch，降惯量）。
- 末端执行器两种可 2 分钟快换：平行夹爪与柔顺手掌；示教臂（leader arms）握把内嵌 FSR 力敏电阻。
- 损坏维修成本低：可承受约 7 次摔倒，修复仅需 21 分钟打印 + 14 分钟装配。

### 计算平台与软件栈

- 主控 Jetson Orin NX 16GB 机上实时推理：300M 参数扩散策略约 100 ms 延迟；2.0 版本用 Foundation Stereo 在机上跑 10 Hz 立体深度估计。
- 纯 Python、pip 一键安装（>= 3.10），含底层控制、RL 训练（MuJoCo / MJX，PPO）、扩散策略训练、真机部署全部代码；不依赖 ROS。
- 数字孪生：3D 打印零点校准治具（1 分钟内完成）+ 可迁移的电机系统辨识（同型号电机只做 1 次 sysID），支撑零样本 sim-to-real；策略在两台实例间零样本互迁，双臂操作 90% 成功率复现。
- 遥操作：同构示教臂 + 掌机（Steam Deck / ROG Ally X）；2.0 支持 Meta Quest 2 VR 遥操作。
- 版本脉络：2025-08-25 发布 ToddlerBot 2.0；2026-01 发布多技能全身运动系统（深度图技能分类器 + 多策略切换）。

### 适合人群

- 适合：想做全身 loco-manipulation、模仿/强化学习数据采集的研究生与进阶爱好者；零基础但动手能力强者亦可按手册完成；Python 栈对 ML 背景新手极友好；3.4 kg 小体型在家操作安全。
- 门槛：BOM $6,000 不算便宜；设计文件为非商业许可；Dynamixel 舵机性能上限（速度/扭矩/通信）制约高动态动作（论文自述）。

## 参考

- [hshi74/toddlerbot GitHub 仓库](https://github.com/hshi74/toddlerbot)
- [ToddlerBot 项目主页](https://toddlerbot.github.io/)
- [论文 arXiv:2502.00893v2](https://arxiv.org/html/2502.00893v2)
