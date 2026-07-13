---
$id: ent_report_internal_robot_data_collection_survey_v2_1_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: Robot Whole-Body Data Collection Survey Report V2.1
  zh: 机器人整机数据采集调研报告 V2.1
  ko: ''
summary:
  en: |
    Internal survey report (V2.1, 85 pages) on embodied-AI data collection for humanoid and general robots.
    Key findings: (1) egocentric human video follows a predictable scaling law and can outperform robot teleoperation data per hour;
    (2) cross-embodiment transfer has both bright and dark sides—embodiment grouping mitigates negative transfer;
    (3) the UMI route reduces single-trajectory collection cost by 10–40×, making large-scale manipulation data affordable;
    (4) simulation-to-real pipelines (Isaac Gym / ManiSkill 3) can cut marginal data cost by ~27×;
    (5) the bottleneck for humanoid data has shifted from technical feasibility to cost structure and throughput.
    The report maps the field as a "five-vertical × four-horizontal" matrix: manipulation routes (homogeneous, UMI, egocentric, VR/DexCap, tactile/force) and locomotion routes (traditional SLAM, end-to-end VLA navigation, imitation/RL, sim-to-real).
    Actionable recommendations include a 70 % simulation / 30 % real dual-track pipeline, elevating egocentric video to a first-class data source, and mandating tactile sensing for contact-rich tasks.
  zh: |
    内部调研报告 V2.1（共85页），系统梳理具身智能时代机器人整机数据采集的技术路线、产业现状与投资建议。
    核心发现：①人类自我中心视频存在可预测的对数线性 Scaling Law，单位小时数据收益可超过机器人遥操作；②跨本体迁移同时存在正迁移与负迁移，按形态图距离分组训练可缓解负迁移；③UMI 路线将单条数据采集成本降低10–40倍；④仿真到真实管线（Isaac Gym / ManiSkill 3）可将边际数据成本降低约27倍；⑤人形机器人数据采集的瓶颈已从“能不能采”转向成本结构与吞吐量。
    报告提出“五纵四横”技术矩阵：操作采集路线包括同构采集、UMI、Ego第一人称、VR/DexCap遥操作、力触觉采集；导航路线包括传统SLAM、端到端VLA导航、模仿学习/强化学习、Sim-to-Real。
    三大行动建议：建立70%仿真+30%真实的双轨数据管线；将人类自我中心视频提升为第一类数据源；在接触丰富任务中强制集成触觉模态。
  ko: ''
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 11_applications_markets
- 06_design_engineering
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
- market
tags:
- data_collection
- teleoperation
- imitation_learning
- egocentric_video
- tactile
- simulation
- humanoid
- survey
- vla
- cross_embodiment
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-13'
  confidence: medium
  notes: 'Ingested from local PDF survey report; factual claims should be cross-checked against cited papers.'
sources:
- id: src_001
  type: report
  title: 机器人整机数据采集调研报告 V2.1
  url: .staging/pdfs/机器人数据采集调研报告_V2.1.pdf
  date: '2026-06-17'
---

# 机器人整机数据采集调研报告 V2.1

## 报告定位

本报告为内部具身智能数据采集领域的全景式调研，覆盖**操作（Manipulation）**与**移动（Locomotion）**两大场景，重点回答：

- 数据采集的主流技术路线有哪些？各自的成本、精度、成熟度如何？
- 人类数据 vs. 机器人数据、仿真数据 vs. 真实数据、同构采集 vs. 跨本体迁移的边界在哪里？
- 产业化落地应选择何种数据管线组合？

## 核心发现摘要

1. **Scaling Law 已验证**：EgoScale、HumanNet 等研究显示，人类自我中心视频数据在数小时到数十万小时范围内呈现对数线性缩放，预训练后只需少量真机数据即可微调。
2. **跨本体迁移的双面性**：形态差异过大会导致负迁移（gradient conflict），按 embodiment graph 距离分组可提升性能达 39.8%。
3. **UMI / 无本体采集成本极低**：原始 UMI DIY 成本 $371，FastUMI Pro 单条约 $0.5，YUBI 已达 120 万 episodes。
4. **仿真数据边际成本低**：Isaac Gym / ManiSkill 3 可在数小时内生成百万级轨迹，与真实数据混合使用可显著降低成本。
5. **触觉模态是接触任务的必要项**：GelSight Mini、DIGIT、Taccel 等触觉传感器可填补视觉盲区，接触丰富任务成功率提升可达 +50%。

## 五纵四横技术矩阵

### 操作采集五条纵向路线

| 路线 | 核心思想 | 代表工作 |
|------|----------|----------|
| 同构采集 | 用目标机器人本体直接采集，零 embodiment gap | ALOHA / ALOHA 2、AgiBot World、MonoDuo |
| UMI（无本体） | 手持夹爪替代真机，末端动作跨平台复用 | UMI、FastUMI Pro、YUBI、RDT2、exUMI |
| Ego 第一人称 | 人类视角原生获取视觉-动作绑定 | EgoScale、EgoDex、EgoMimic、EgoVLA |
| VR / DexCap 遥操作 | 沉浸式头显/可穿戴动捕实现精细控制 | OPEN TEACH、DexCap、Bunny-VisionPro、LeVR |
| 力触觉 | 以接触力/触觉图像作为独立模态 | GelSight Mini、Taccel、FeelTheForce、TactAlign |

### 移动四条横向路线

| 路线 | 核心数据 | 代表工作 |
|------|----------|----------|
| 传统 SLAM | 位姿、点云、栅格地图 | ORB-SLAM3、RTAB-Map、Cartographer、LIO-SAM |
| 端到端 VLA 导航 | 图像 + 语言指令 + 动作 token | SayCan、RT-2、GOAT、NoMaD、OpenDriveVLA |
| 模仿学习 / 强化学习 | 图像 + 目标 + 动作 | GNM/ViNT、HIL-SERL、Sim-to-Real Locomotion |
| Sim-to-Real | 仿真轨迹 + 域随机化 + 少量真实微调 | Isaac Gym、ManiSkill 3、Domain Randomization |

## 行动建议

1. **双轨管线**：70% 仿真 + 30% 真实，覆盖结构化场景与接触动力学。
2. **Ego 优先**：采购低成本 Ego 采集设备，将人类视频作为核心预训练信号。
3. **触觉必选**：在插入、装配、打磨、擦拭等任务中强制集成触觉传感器。

## 来源

- 本地 PDF：`机器人数据采集调研报告_V2.1.pdf`
