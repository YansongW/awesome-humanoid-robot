# 09 数据与数据集

> **领域编码**：`09_data_datasets`  
> **价值链层**：智能层（Intelligence）  
> **状态**：草案 —— v0.1.0 前需复核  
> **用途**：定义用于训练、验证并持续改进人形机器人系统所需的数据资产、采集方法、数据管道与治理概念。

---

## 1. 核心问题

> **训练、评估并持续改进人形机器人需要哪些数据？如何在生产规模下采集、整理与治理这些数据？**

人形机器人的技能来自数据：遥操作演示、人体动作捕捉、仿真 rollout 以及真实世界中的车队日志。与可基于静态互联网文本训练的大语言模型不同，具身智能需要能够捕捉物理交互的数据：接触力、执行器响应、传感器噪声以及恢复行为。本领域追踪将原始记录转化为可复用训练燃料所需的数据集、格式、基础设施以及法律/伦理框架。

---

## 2. 范围边界

### 2.1 在范围内

- 用于全身人形控制与操作的遥操作和人类演示数据集。
- 跨本体机器人学习数据集与标准化格式（如 RLDS）。
- 人体动作捕捉（MoCap）数据集与重定向管道。
- 仿真生成与合成数据集，包括世界模型输出。
- 融合视觉、语言、动作、本体感觉与力/触觉传感器的多模态数据集。
- 数据基础设施：日志、标注、存储、回放、车队遥测与数据飞轮。
- 数据治理：许可、隐私、同意、匿名化、安全与监管合规。

### 2.2 不在范围内

- 消费数据的算法（见 `07_ai_models_algorithms`）。
- 作为软件产品的中间件、仿真器与部署工具（见 `08_software_middleware`）。
- 作为测量系统的评测协议与基准（见 `10_evaluation_benchmarks`）。
- 已确认与机器人学习无相关性的通用计算机视觉或自然语言处理数据集。

---

## 3. 关键概念

### 3.1 遥操作与真实世界演示数据

遥操作允许人类操作员控制人形机器人并记录专家轨迹。这些演示是模仿学习与行为克隆所需高质量真实世界数据的主要来源。

| 数据来源 | 模态 | 规模 / 关键事实 | 对人形机器人的意义 |
|----------|------|----------------|-------------------|
| **HumanPlus**（Fu 等，2024） | RGB 摄像头 → 全身跟随 | 33 自由度、180 cm 定制人形机器人；约 40 条演示即可学习任务，成功率 60–100% | 首个让机器人从以自我为中心的人类数据中学习运动与自主技能的完整系统 [HumanPlus 2024]。 |
| **OmniH2O-6**（He 等，2024） | VR + 全身遥操作 | 六个日常任务；约 40 分钟真实世界演示；包含 30 Hz 的 RGB-D、运动目标与关节目标 | 首个公开发布的人形全身控制数据集；支持通过模仿或前沿模型实现自主 [OmniH2O 2024]。 |
| **工业遥操作** | 动作捕捉服、VR 头显、外骨骼 | Tesla、Figure 等设有专门数据采集团队，穿戴动捕设备进行车队学习 | 表明数据采集正在成为人形量产化 pipeline 中的运营岗位 [Tesla 职位公告 2025]。 |

**来源与证据**：
- HumanPlus 在仿真中使用 40 小时人体运动数据训练底层策略，并将其迁移到现实世界，通过 RGB 摄像头实现跟随，再利用行为克隆学习任务，例如叠运动衫、从仓库货架卸货和打字 [HumanPlus 2024]。
- OmniH2O 展示了具有灵巧双手的 Unitree H1 全身遥操作，并发布了六个任务的配对视觉与运动数据集 [OmniH2O 2024]。
- Tesla 的 "Data Collection Operator, Optimus" 职位公告描述操作员穿戴动作捕捉服和 VR 头显采集全身运动与操作数据，说明遥操作数据采集正在工业化 [Tesla 职位公告 2025]。

### 3.2 跨本体与大规模机器人数据集

跨本体数据集将多种机器人平台的演示整合到统一格式中，使通用策略能够在不同硬件之间迁移。它们相当于机器人领域的"预训练语料库"。

| 数据集 | 范围 | 规模 | 关键发现 |
|--------|------|------|----------|
| **Open X-Embodiment（OXE）** | 22 种机器人本体、21 家机构 | 超过 100 万条轨迹、527 项技能、160,266 项任务 | 在 OXE 上训练的 RT-2-X 在新兴技能上的表现约为仅使用 Google 机器人数据训练的 RT-2 的 3 倍 [Open X-Embodiment 2023]。 |
| **DROID** | 52 个实验室的 Franka Panda 机械臂 | 76,000 条轨迹、564 个场景 | 采用标准化协议采集，用于跨本体预训练与多样化"野外"场景研究 [DROID 2024]。 |
| **Bridge Data V2** | WidowX 厨房操作 | 约 60,000 条演示 | 被广泛用于 OXE 中的低成本操作研究子集 [Open X-Embodiment 2023]。 |

**来源与证据**：
- Open X-Embodiment 合作发布了迄今最大规模的开放机器人学习数据集，并证明在混合机器人数据上训练的单一高性能策略（RT-X）优于各平台专用策略，确立了跨本体预训练的可行性 [Open X-Embodiment 2023]。
- DROID 提供大规模、可复现的采集流程，用于研究跨场景与跨任务泛化 [DROID 2024]。
- 这些数据集通常采用 RLDS（Robot Learning Dataset Specification）格式存储，基于 TensorFlow Datasets，每个 episode 包含观察、动作、奖励与元数据 [RLDS / OXE 文档]。

> **推测性说明**：跨本体数据是否足以支持高自由度人形控制——而非主要用于单臂操作——仍是开放研究问题。全身动力学与平衡可能仍需要人形专用数据集。

### 3.3 人体动作捕捉与重定向数据

由于人形机器人具有类似人体的运动结构，人体运动是丰富的先验知识。动捕数据集提供的参考动作可被重定向到机器人关节空间，用于训练底层技能或运动先验。

| 数据集 / 系统 | 内容 | 用途 |
|---------------|------|------|
| **AMASS** | SMPL 格式的大规模人体动作捕捉数据 | 训练运动先验并重定向到人形运动学 [Clone 2025；CLOT 2026]。 |
| **ExBody / ExBody2** | 从人体运动生成富有表现力的人形全身控制 | 训练人形机器人执行多样化、动态的人体动作 [ExBody2 2024]。 |
| **CLOT 人体运动数据集** | 约 20 小时、120 Hz 的 OptiTrack 全身运动捕捉 | 专为人形遥操作设计；包含行走、跑步、武术、舞蹈与平衡 [CLOT 2026]。 |

**来源与证据**：
- CLOT 采集了超过 20 小时全身人体运动，明确考虑足地接触一致性与执行器限制，并通过在线重定向实时作用于 31 自由度的 Adam Pro 人形机器人进行闭环遥操作 [CLOT 2026]。
- Clone 通过动作编辑对 AMASS 进行增广，并额外采集面向人形控制器的动捕数据，指出动画导向的数据集低估了真实控制所需的构型与动态转换 [Clone 2025]。
- ExBody2 利用人体运动数据与强化学习推进富有表现力的全身人形控制 [ExBody2 2024]。

### 3.4 仿真、合成数据与世界模型

仿真能够以物理世界难以实现的规模生成数据。合成数据对罕见场景、接触丰富操作以及安全关键边缘案例尤其有价值。

| 平台 / 数据集 | 输出 | 声明 / 结果 |
|---------------|------|-------------|
| **NVIDIA Isaac GR00T Blueprint** | 合成人形运动轨迹 | 在 11 小时内生成 78 万条合成轨迹（约 6,500 小时人类演示当量）；合成 + 真实数据使 GR00T N1 性能比仅用真实数据提升 40% [NVIDIA GR00T N1 2025]。 |
| **HumanoidBench** | 仿真基准任务 | MuJoCo 中 27 项全身运动与操作任务；最先进的 RL 算法在多数任务上表现不佳，凸显了数据与层次化方法的需求 [HumanoidBench 2024]。 |
| **DexGraspNet** | 合成灵巧抓取 | 在 NVIDIA Isaac Sim 中生成 132 万条 ShadowHand 抓取，覆盖 5,355 个物体、133 个类别 [DexGraspNet 2024]。 |

**来源与证据**：
- NVIDIA 在 GR00T N1 发布中说明，基于 Omniverse 与 Cosmos 世界模型的合成数据生成可将有限的人类演示放大为大型训练语料库，并显著提升基础模型性能 [NVIDIA GR00T N1 2025]。
- HumanoidBench 提供基于 Unitree H1 模型与灵巧手的高维仿真环境，用于在不依赖易损硬件的情况下加速算法研究 [HumanoidBench 2024]。
- DexGraspNet 证明仿真可生成比此前真实世界采集规模大得多的抓取数据集，并展示 sim-to-real 迁移 [DexGraspNet 2024]。

> **推测性说明**：生产级人形训练所需的合成数据与真实数据比例尚不确定。现有证据表明合成数据是强大的倍增器，但尚不能完全替代真实世界的物理交互数据。

### 3.5 数据治理、许可与隐私

随着人形机器人部署于家庭、工厂与公共空间，其采集的数据引发治理问题：数据归谁所有、需要何种同意、保留多久、如何保障安全。

| 关注点 | 相关框架 / 实践 | 对人形机器人的意义 |
|--------|----------------|-------------------|
| **个人数据采集** | GDPR（欧盟）、CCPA/CPRA（加州）、BIPA（伊利诺伊州） | 摄像头、麦克风、激光雷达与三维空间地图可能捕捉人脸、声音与空间布局；通常需要进行隐私影响评估 [Robot Data Privacy Guide 2026；Kite Compliance 2025]。 |
| **数据最小化与匿名化** | 端侧处理、面部模糊、假名化 | 降低监管风险与存储成本；符合 GDPR 的数据最小化与存储限制原则 [Robot Data Privacy Guide 2026]。 |
| **安全与遥测** | 加密通道、安全启动、供应商 DPA | 研究人员观察到人形机器人在无显式同意的情况下自动传输遥测数据，引发 GDPR 与网络安全担忧 [Help Net Security 2025]。 |
| **数据集许可** | OXE 子集混合许可、知识共享、商业限制 | 聚合数据集中的混合许可使商业使用与再分发复杂化 [Open X-Embodiment 2023]。 |

**来源与证据**：
- 机器人数据隐私合规指南指出，仓库或公共场所中的摄像头机器人采集个人数据，受 GDPR、CCPA 与 BIPA 约束，GDPR 最高罚款可达全球年收入的 4% [Robot Data Privacy Guide 2026]。
- Kite Compliance 将隐私、偏见与透明度列为人类机器人合规的四大支柱之一，与物理安全、功能安全和网络安全并列 [Kite Compliance 2025]。
- 2025 年对一款消费级人形机器人的安全分析发现 DDS 流量未加密、TLS 证书校验被禁用，并自动传输包括摄像头、麦克风与空间数据在内的遥测信息，暴露出具体网络安全漏洞 [Help Net Security 2025]。

---

## 4. 与其他领域的关系模式

| 来源领域 | 目标领域 | 关系 | 逻辑 |
|----------|----------|------|------|
| `09_data_datasets` | `07_ai_models_algorithms` | `is_prerequisite_for` | 数据集是 VLA 模型、世界模型、运动/操作策略以及模仿学习算法的训练基础。 |
| `09_data_datasets` | `08_software_middleware` | `requires` | 数据管道依赖仿真器（Isaac Sim、MuJoCo）、中间件（ROS 2、DDS）、日志框架与车队管理工具。 |
| `09_data_datasets` | `02_components_supply_chain` | `requires` | 数据采集需要传感器、边缘计算、存储与网络带宽；组件精度限制信号质量与频率。 |
| `09_data_datasets` | `10_evaluation_benchmarks` | `is_prerequisite_for` / `verified_by` | 基准测试需要代表性数据集来训练与测试策略；评测结果又反馈到数据集筛选。 |
| `09_data_datasets` | `04_assembly_integration_testing` | `produces` | 系统集成与现场测试产生遥测、故障日志与演示数据，形成数据闭环。 |
| `09_data_datasets` | `11_applications_markets` | `serves` / `drives_demand_for` | 应用场景定义需要采集何种数据；部署规模催生对车队数据基础设施的需求。 |
| `09_data_datasets` | `12_policy_regulation_ethics` | `is_regulated_by` | 数据采集、保留与共享受隐私法、安全标准与新兴 AI/数据治理法规约束。 |

---

## 5. 受控词表

### 5.1 数据类别

- `teleoperation_data`（遥操作数据）
- `human_demonstration_data`（人类演示数据）
- `motion_capture_data`（动作捕捉数据）
- `cross_embodiment_data`（跨本体数据）
- `simulation_data`（仿真数据）
- `synthetic_data`（合成数据）
- `multimodal_dataset`（多模态数据集）
- `vision_language_action_dataset`（视觉-语言-动作数据集）
- `fleet_telemetry`（车队遥测）
- `failure_log`（故障日志）
- `world_model_data`（世界模型数据）

### 5.2 相关实体类型

依据项目信息模型：

- `dataset`（数据集）
- `benchmark`（基准）
- `software_platform`（软件平台）
- `paper`（论文）
- `report`（报告）
- `technology`（技术）
- `policy`（政策）

---

## 7. 关键来源

### 7.1 主要 / 权威来源

1. **Fu, Z. 等**。 *HumanPlus: Humanoid Shadowing and Imitation from Humans*（2024）。arXiv:2406.10454。提出通过跟随与行为克隆让人形机器人从人类数据中学习运动与自主技能的完整系统。  
   URL: https://arxiv.org/abs/2406.10454

2. **He, T. 等**。 *OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning*（2024）。arXiv:2406.08858。提出全身遥操作系统并发布 OmniH2O-6 人形数据集。  
   URL: https://arxiv.org/abs/2406.08858

3. **Open X-Embodiment Collaboration**。 *Open X-Embodiment: Robotic Learning Datasets and RT-X Models*（2023）。arXiv:2310.08864。整合 21 家机构 22 种机器人本体的超过 100 万条轨迹，并用 RT-X 验证跨本体迁移。  
   URL: https://arxiv.org/abs/2310.08864

4. **Sferrazza, C. 等**。 *HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation*（2024）。arXiv:2403.10506。提供 MuJoCo 中 27 项人形学习与控制基准任务。  
   URL: https://arxiv.org/abs/2403.10506

### 7.2 行业与市场分析

5. **NVIDIA**。 *Accelerate Generalist Humanoid Robot Development with NVIDIA Isaac GR00T N1*（2025）。介绍 GR00T N1、合成数据生成蓝图，以及合成 + 真实数据使模型性能提升 40% 的声明。  
   URL: https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1/

6. **Khazatsky, A. 等**。 *DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset*（2024）。arXiv:2403.12945。记录 52 个实验室 564 个场景中的 76,000 条操作轨迹，用于跨本体研究。  
   URL: https://arxiv.org/abs/2403.12945

### 7.3 领域专项来源

7. **Robotomated**。 *Robot Data Privacy: GDPR, CCPA, and Camera-Equipped Robot Compliance*（2026）。面向摄像头机器人的隐私框架、数据最小化实践与合规处罚实用指南。  
   URL: https://robotomated.com/learn/guides/robot-data-privacy-compliance

8. **Tesla**。 *Data Collection Operator, Optimus* 职位公告（2025）。人形开发中动作捕捉与 VR 全身数据采集的运营管理证据。  
   URL: https://www.tesla.com/careers/search/job/data-collection-operator-optimus-222857

---

## 8. 开放问题

1. 训练通用的人形策略需要怎样的真实遥操作、合成仿真与跨本体数据比例？这种比例如何随任务类型（运动、操作、长程规划）变化？
2. 本体应如何表达数据集质量维度——如动作空间一致性、本体差距、接触丰富度与标注密度——以便下游模型开发者判断其适用性？
3. 对于在工厂或仓库中持续录制视频、音频与工人交互数据的工业人形车队，需要怎样的数据治理框架与技术标准？
4. 社区如何在保护个人隐私、设施信息与知识产权的前提下，构建足以媲美专有工业数据集的开放人形数据集？
