---
$id: ent_robot_system_berkeley_humanoid_lite
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Berkeley Humanoid Lite
  zh: 伯克利轻量人形机器人
  ko: Berkeley Humanoid Lite
summary:
  en: An open-source 0.8 m, 16 kg humanoid robot from UC Berkeley with 22 active degrees of freedom and a sub-5,000 USD bill of materials, built around self-designed quasi-direct-drive actuators with 3D-printed cycloidal reducers, trained in NVIDIA Isaac Lab with zero-shot sim-to-real reinforcement learning.
  zh: Berkeley Humanoid Lite 是 UC Berkeley 开源的轻量人形机器人，身高 0.8 m、重 16 kg，22 个主动自由度，整机 BOM 美国采购约 4,312 美元、中国采购约 3,236 美元，核心为 3D 打印摆线针轮减速的自研准直驱执行器，基于 NVIDIA Isaac Lab 训练并实现零样本 sim-to-real 的 RL 行走。
  ko: An open-source 0.8 m, 16 kg humanoid robot from UC Berkeley with 22 active degrees of freedom and a sub-5,000 USD bill of materials, built around self-designed quasi-direct-drive actuators with 3D-printed cycloidal reducers, trained in NVIDIA Isaac Lab with zero-shot sim-to-real reinforcement learning.
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
- berkeley_humanoid_lite
- uc_berkeley
- quasi_direct_drive
- cycloidal_reducer
- 3d_printed
- reinforcement_learning
- research_platform
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/berkeley-humanoid-lite.md（访问日期 2026-07-01），事实均来自其列出的 GitHub 仓库、项目主页、论文 arXiv:2504.17249 与 Berkeley EECS 技术报告 EECS-2025-207。'
sources:
- id: src_001
  type: website
  title: HybridRobotics/Berkeley-Humanoid-Lite GitHub Repository
  url: https://github.com/HybridRobotics/Berkeley-Humanoid-Lite
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Berkeley Humanoid Lite Project Page
  url: https://lite.berkeley-humanoid.org/
  accessed_at: '2026-07-01'
- id: src_003
  type: paper
  title: 'Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot (arXiv:2504.17249)'
  url: https://arxiv.org/abs/2504.17249
  accessed_at: '2026-07-01'
---

## 概述

Berkeley Humanoid Lite 是 UC Berkeley 混合机器人实验室（Hybrid Robotics Group，Koushil Sreenath 团队）与 SLICE 实验室发起的开源轻量人形机器人，属 BAIR Commons HIC 仓库，论文 arXiv:2504.17249（2025-04）。整机高 0.8 m、重 16 kg，22 个主动自由度（每条腿 6、每条臂 5），整机 BOM 美国采购约 4,312 美元、中国采购约 3,236 美元，官方宣传口径"低于 $5,000"（来源：调研档案 berkeley-humanoid-lite.md，下同）。

许可证方面，代码采用 MIT License，CAD 等其他资产采用 CC BY-SA 4.0。项目性价比在开源人形中属第一梯队：GitHub 仓库 `HybridRobotics/Berkeley-Humanoid-Lite` 约 1,417 stars / 215 forks（2026-07-01 快照，活跃），有 Discord 社区与微信群。全部结构件可用普通桌面 FDM 打印机（PLA）制造，组装周期约 3 天（现货件一周内到货、打印约一周）。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 0.8 m / 16 kg | 论文 arXiv:2504.17249 |
| 主动自由度 | 22（腿 6×2、臂 5×2） | 技术报告对比表 |
| 硬件成本（BOM） | 美国约 $4,312 / 中国约 $3,236（官方口径 sub-$5,000） | EECS-2025-207 技术报告 |
| 主控 | Intel N95 迷你 PC（约 $129） | 论文 |
| 通信 | 四肢各一条 CAN 2.0 总线（1 Mbps），执行器与 IMU 250 Hz | 论文 |
| 传感器 | BNO085 IMU（经 Arduino 以 USB 接入）；SteamVR 基站 + 手柄遥操作 | 论文 |
| 电池 | 6S 4000 mAh LiPo，约 30 分钟续航 | 论文 |
| 新手友好度 | 3.5 / 5（调研档案评估） | 调研档案 |

### 执行器方案

- 两种规格自研准直驱（quasi-direct-drive）执行器：6512（10 台）与 5010（12 台），核心为 3D 打印摆线针轮（cycloidal）减速器，全部结构件可用桌面 FDM 打印机（PLA）制造。
- 6512 执行器 BOM 约 $188（美国）/ $157（中国）：MAD Components M6C12 150KV 无人机无刷电机（$129）+ ST B-G431B-ESC1 驱动板（$19）+ AS5600 磁编码器（$3）+ 轴承/紧固件/打印件。
- 摆线齿轮多齿分担载荷，论文用 60 小时耐久测试验证塑料齿轮可靠性；兼容 Moteus / ODrive / VESC 等第三方驱动器。
- 单条 CAN 总线最多 64 设备，便于重构成四足/双足/半人马等形态；另有成人尺寸扩展构型（7 自由度腿 + 灵巧手）。

### 软件栈

- 训练与仿真基于 NVIDIA Isaac Lab 组织目录结构，URDF / MJCF / USD 三种描述格式齐全，支持策略训练与 sim2sim 验证。
- RL 运动控制策略实现零样本 sim-to-real；部署代码 `berkeley_humanoid_lite_lowlevel` 为真机底层 C 代码，独立于训练栈，单独拷到机上即可部署。
- 支持动捕、SteamVR 遥操作双臂（魔方、写字、搭积木演示）。

### 适合人群

- 适合：有一定动手能力、目标是做 RL 运动控制研究的个人/实验室——$4–5k 就能造出能跑 RL 行走的 22 自由度人形，文档 + BOM + 打印文件齐全，社区活跃。
- 门槛：需要自己打印摆线减速器并装配 22 台执行器、焊接 CAN 总线、烧录 FOC 固件，嵌入式与 3D 打印经验不足者容易卡壳；16 kg 机型已需要一定的操作安全意识；非零基础友好。

## 参考

- [HybridRobotics/Berkeley-Humanoid-Lite GitHub 仓库](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)
- [项目主页](https://lite.berkeley-humanoid.org/)
- [论文 arXiv:2504.17249](https://arxiv.org/abs/2504.17249)
- [Berkeley EECS 技术报告 EECS-2025-207（完整 BOM 表）](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf)
