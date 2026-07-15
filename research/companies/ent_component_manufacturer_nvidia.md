---
$id: ent_component_manufacturer_nvidia
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: NVIDIA
  zh: 英伟达
  ko: 엔비디아
summary:
  en: American semiconductor and software company supplying GPUs, edge AI compute modules, simulation platforms, and robot-learning
    tools used in humanoid development.
  zh: '## 概述 英伟达是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。'
  ko: GPU, 엣지 AI 컴퓨팅 모듈, 시뮬레이션 플랫폼 및 로봇 학습 도구를 공급하는 미국 반도체 및 소프트웨어 기업입니다.
domains:
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- upstream
- intelligence
functional_roles:
- organization
- component
- intelligence
tags:
- nvidia
- jetson
- isaac
- gpu
- edge_compute
- simulation
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from appendix-d/companies/company_nvidia.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: NVIDIA Jetson AGX Orin Series
  url: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/
  date: '2026'
  accessed_at: '2026-06-24'
- id: src_002
  type: website
  title: NVIDIA Isaac Sim / Isaac Lab
  url: https://developer.nvidia.com/isaac
  date: '2026'
  accessed_at: '2026-06-24'
theoretical_depth:
- system
---

## 概述
英伟达是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## NVIDIA（英伟达） / NVIDIA Corporation

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | NVIDIA（英伟达） |
| **英文名** | NVIDIA Corporation |
| **总部** | 美国加利福尼亚州圣克拉拉 |
| **成立时间** | 1993 |
| **官网** | [https://www.nvidia.com](https://www.nvidia.com) |
| **供应链环节** | AI 计算平台、机器人软件/仿真、芯片供应商 |
| **企业属性** | 上市公司（NASDAQ: NVDA） |
| **母公司/所属集团** | 无（NVIDIA Corporation 为上市主体） |
| **数据来源** | NVIDIA 官网、Jetson/Isaac 官方文档、公开新闻稿 |

### 公司简介

NVIDIA 为机器人与人形机器人提供 Jetson 边缘计算、Isaac Sim 仿真、Isaac Lab 训练与 GR00T 人形基础模型，是物理 AI 的核心使能者。

Jetson Thor 专为物理 AI 与人形机器人设计，集成 Blackwell GPU 与大容量统一内存；Isaac Sim 提供高保真仿真与合成数据；GR00T 提供 VLA 基础模型。多家头部人形机器人公司采用 NVIDIA 平台。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Jetson | 边缘 AI 计算模组 | Jetson Thor / AGX Orin 等 | 机器人/人形大脑、感知推理 |
| Isaac Sim / Isaac Lab | 仿真与训练平台 | Isaac Sim / Isaac Lab | Sim2Real、数字孪生、强化学习 |
| Isaac GR00T | 人形机器人基础模型 | GR00T N1.5 等 | VLA、自然语言任务执行 |

### 代表产品

#### NVIDIA Jetson Thor（T5000）

> NVIDIA Jetson Thor（T5000）：请访问 [官方资料](https://www.nvidia.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| AI 算力 | 最高 2070 FP4 TFLOPS | NVIDIA 官方 |
| GPU 架构 | NVIDIA Blackwell | NVIDIA 官方 |
| CPU | 14 核 Arm Neoverse-V3AE | NVIDIA 官方 |
| 内存 | 128 GB LPDDR5X（273 GB/s） | NVIDIA 官方 |
| 网络 | 4×25 GbE | NVIDIA 官方 |
| 功耗 | 40–130 W 可调 | NVIDIA 官方 |
| 尺寸 | 100 mm × 87 mm（模组） | NVIDIA 官方 |
| 价格 | 开发者套件 3,499 USD；模组 2,999 USD（1k 起） | NVIDIA 公开报价 |

**技术亮点**：Blackwell GPU、大容量统一内存、支持多模态生成式 AI 与 VLA 模型、4×25GbE 高带宽传感器接口、面向人形机器人。

**应用场景**：人形机器人主控、自动驾驶、医疗机器人、工业 AMR。


#### NVIDIA Isaac Sim

> NVIDIA Isaac Sim：请访问 [官方资料](https://www.nvidia.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 底层平台 | NVIDIA Omniverse / PhysX | NVIDIA 官方 |
| 渲染 | RTX 实时光追 | NVIDIA 官方 |
| 物理引擎 | PhysX | NVIDIA 官方 |
| ROS 集成 | ROS 2 桥接与 Isaac ROS | NVIDIA 官方 |
| 训练框架 | Isaac Lab（强化学习/模仿学习） | NVIDIA 官方 |
| 数字孪生 | 支持 USD 场景与传感器模型 | NVIDIA 官方 |
| 部署方式 | 本地、容器、云端 | NVIDIA 官方 |
| 价格 | 免费（需 NVIDIA 账号/Omniverse） | 官方说明 |

**技术亮点**：照片级仿真、PhysX 物理、与 Jetson/GR00T 打通的 Sim2Real 流程、大规模合成数据生成。

**应用场景**：人形机器人训练、数字孪生工厂、传感器验证、强化学习研究。


### 供应链位置

- **上游关键零部件/材料**：台积电代工、存储器、传感器与摄像头合作伙伴、Omniverse 生态。
- **下游客户/应用场景**：Tesla、Figure AI、Boston Dynamics、Agility Robotics、Apptronik、1X Technologies 等整机厂与开发者。
- **主要竞争对手/对标**：Qualcomm RB、Intel Movidius/AMD、仿真平台 Gazebo/Unity/Unreal。

### 知识图谱节点与关系

- 公司实体：`ent_company_nvidia`
- 产品/平台实体：`ent_software_platform_nvidia_jetson_thor`、`ent_software_platform_nvidia_isaac_sim`
- 关键关系：
  - `rel_ent_company_nvidia_develops_ent_software_platform_nvidia_jetson_thor`（`ent_company_nvidia` → `develops` → `ent_software_platform_nvidia_jetson_thor`）
  - `rel_ent_company_nvidia_develops_ent_software_platform_nvidia_isaac_sim`（`ent_company_nvidia` → `develops` → `ent_software_platform_nvidia_isaac_sim`）

### 参考资料

1. [NVIDIA 官网](https://www.nvidia.com)
2. [NVIDIA Jetson Thor 产品页](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
3. [NVIDIA Isaac Sim 官方页面](https://developer.nvidia.com/isaac/sim)

## 参考
- [NVIDIA Jetson AGX Orin Series](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)
- [NVIDIA Isaac Sim / Isaac Lab](https://developer.nvidia.com/isaac)
- 项目 Wiki：appendix-d/companies/company_nvidia.md


