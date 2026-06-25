# AI4Sci 工作流谱系路线图

> **Status**: Draft v0.1 — 与 `docs/ontology/` 12 领域本体对齐，随项目演进持续更新  
> **Purpose**: 为人形机器人从 0 到 1 生产制造建立可执行、可扩展的系统性知识谱系，并把每个可调研主题映射为 `scripts/ai4sci_workstreams/` 下的 YAML 工作流。

---

## 1. 核心问题

本项目始终围绕一个问题组织知识：

> **How do we go from 0 to 1 on humanoid robot mass production and industrial application?**

回答这个问题需要的不是几篇论文或几家公司，而是理解“定义 → 设计 → 校核 → MVP → 测试 → EVT → DVT → PVT → 量产爬坡”全生命周期中，硬件、软件、数据、供应链、制造、质量、安全、市场、政策等多维系统的交互。

### 1.1 森林与根系

如果把人形机器人的知识体系想象成一片森林：

- **每棵树**是一个领域：硬件、软件、数据、供应链、市场、政策……
- **树的枝干**是该领域的子系统或子问题：驱动、感知、规划、控制、制造、认证……
- **每片叶子**是一个具体的知识点：某篇论文、某个组件、某个数据集、某个标准。
- **而树根**则是支撑所有这些树的底层基础学科：数学、物理、化学、计算机科学、经济学、运筹学。

因此，知识谱系不仅要把“看得见”的产品生命周期和工程领域画出来，还要把“看不见”的理论根系也连进去：当你查看某个 WBC 算法的公式时，应该能一路追溯到拉格朗日乘子、KKT 条件、凸优化，乃至线性代数与多元微积分。

---

## 2. 四维知识空间

知识谱系由四个正交维度张成。每个叶子工作流都是“阶段 × 领域 × 知识类型 × 理论深度”的一个具体切面。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 维度 A：产品开发阶段（横向生命周期）                                          │
│  Definition → Design → Verification Planning → MVP → Testing → EVT → DVT →  │
│  PVT → MP / Ramp                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ 维度 B：学科/领域（纵向专业）                                                │
│  硬件 │ 软件与 AI │ 数据系统 │ Infra/云/车队 │ 嵌入式 │ 机械结构 │ 仿真 │   │
│  供应链与制造 │ 质量与可靠性 │ 安全与认证 │ 应用与市场 │ 政策与伦理       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 维度 C：知识类型（横切）                                                      │
│  论文 │ 数据集 │ 基准 │ 技术 │ 组件 │ 公司 │ 报告 │ 标准                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 维度 D：理论深度（从基础到应用）                                              │
│  基础学科 foundation → 定理/原理 principle → 形式化 formalism →              │
│  方法/算法 method → 系统实现 system                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. 维度 A：产品开发阶段

基于硬件行业通用的阶段门模型（EVT / DVT / PVT / MP），并映射到人形机器人实际研发流程。

| 阶段 | 核心问题 | 典型交付物 | 对人形机器人的特殊含义 |
|------|----------|------------|------------------------|
| **Definition / 定义** | 要解决什么问题？为谁？值不值得做？ | PRD、用例矩阵、系统架构草案、ROI 模型、算法路线预研 | 决定成人尺寸/工业尺寸、自由度、负载、续航、目标售价 |
| **Design / 设计** | 如何设计硬件、软件、数据系统？ | CAD/CAE、DFM/DFA/DFS 报告、BOM 草案、软件架构、AI 架构、数据收集方案 | 关节布局、驱动器选型、传感器配置、实时控制架构、VLA/WBC 路线选择 |
| **Verification Planning / 校核规划** | 如何证明设计满足要求？ | 测试策略、标准映射、HIL/SIL 计划、安全案例 | 双足动态平衡、跌落安全、协作力限、功能安全 SIL 等级 |
| **MVP** | 最快验证核心假设的原型是什么？ | looks-like / works-like 原型、关键子系统 Demo | 单腿/双腿平衡、基础行走、单臂抓取 |
| **Testing / 测试** | 子系统和整机是否达到设计指标？ | 关节测试台、静态/动态平衡台、标定报告、环境测试 | 关节扭矩/摩擦/背隙、眼手标定、IMU/力传感器联合标定 |
| **EVT** | 工程概念是否成立？ | 功能样机、核心部件验证、热/机械/电气测试 | 3–50 台，用 3D 打印/软模，验证形态与功能 |
| **DVT** | 完整设计是否满足需求？ | 设计冻结、认证预测试、BOM 成本、DFM/DFA 落地 | 20–200 台，接近最终外观，完成认证所需测试 |
| **PVT** | 已批准设计能否稳定生产？ | 生产工装、产线调试、首批试产、金样板 | 50–500 台，用批量工艺，验证良率与一致性 |
| **MP / Ramp** | 如何持续扩产并降本？ | 工厂产线、供应链协同、MES/PLM、车队数据闭环 | 万台级以上，良率爬坡、成本曲线、OTA 与持续学习 |

**阶段门退出信号**：

- **EVT 退出**：核心功能和关键部件可行，可进入完整设计测试。
- **DVT 退出**：产品设计批准，可进入生产流程验证。
- **PVT 退出**：生产流程就绪，可进入批量生产。

---

## 4. 维度 B：学科/领域分解

每个领域再拆分到可直接作为工作流主题的子领域。

### 4.1 硬件 / Hardware

| 子领域 | 工作流主题示例 |
|--------|----------------|
| 驱动 / Actuation | 电机选型、减速器选型、一体化关节模组设计、直线驱动器、手部微驱动 |
| 感知 / Sensing | 视觉传感器、深度/3D 传感器、LiDAR、IMU、力/力矩传感器、触觉传感器、关节编码器 |
| 电源 / Power | 电芯化学体系、电池包/BMS、热管理、充电/换电 |
| 计算 / Compute | 边缘 AI SoC/GPU、实时控制器、通信总线（CAN-FD/EtherCAT/Ethernet） |
| 结构 / Structure | 轻量化材料、拓扑优化、壳体/骨架、密封/IP 等级、线缆布设 |

### 4.2 软件与 AI / Software & AI

| 子领域 | 工作流主题示例 |
|--------|----------------|
| 感知 / Perception | 视觉 SLAM、3D 重建、物体检测、触觉解释、多传感器融合 |
| 规划与推理 / Planning & Reasoning | 任务规划、LLM/VLM 高层规划器、世界模型、技能库 |
| 控制 / Control | 全身控制（WBC）、模型预测控制（MPC）、平衡控制、阻抗/导纳控制、力位混合控制、传统控制 |
| 学习 / Learning | 模仿学习（IL）、强化学习（RL）、Sim-to-Real、VLA 基础模型、操作策略、Loco-manipulation |
| 部署 / Deployment | 实时栈、安全回退、模型量化、边缘/云协同 |

### 4.3 数据系统 / Data Systems

- 遥操作数据、人体动作捕捉（MoCap）、跨本体数据集、合成数据、仿真数据、车队遥测、数据引擎、数据治理。

### 4.4 Infra / 云 / 车队

- ROS 2 / DDS 中间件、实时操作系统（RTOS/RT-Linux）、仿真平台（Isaac Sim/Lab、MuJoCo、Gazebo、Genesis）、数字孪生、车队管理、OTA、CI/CD for Robots、MES/PLM/ERP 集成。

### 4.5 嵌入式 / Embedded Systems

- 电机驱动器/ESC、传感器接口、安全控制器、固件、Bootloader、确定性总线、功能安全。

### 4.6 机械结构 / Mechanical Structure

- 形态学与自由度、运动学/动力学建模、人因工程（HRI）、DFM/DFA/DFS、跌落与冲击设计、维护可达性。

### 4.7 仿真 / Simulation

- 物理引擎、GPU 并行仿真、Sim-to-Real、Domain Randomization、系统辨识、数字孪生、虚拟调试。

### 4.8 供应链与制造 / Supply Chain & Manufacturing

- 原材料与关键矿物、零部件供应商、制造工艺、工厂设计、垂直整合 vs 外购、BOM 成本建模、良率优化、产能爬坡。

### 4.9 质量与可靠性 / Quality & Reliability

- EOL 测试、老化测试、MTBF/MTTR、可追溯性、SPC/Cpk、失效分析、可靠性增长。

### 4.10 安全与认证 / Safety & Certification

- ISO 13482（个人服务机器人）、ISO 10218（工业机器人）、ISO/TS 15066（协作机器人力限）、EU AI Act、机械法规、产品责任、网络安全、功能安全（IEC 61508）。

### 4.11 应用与市场 / Applications & Markets

- 汽车制造、物流仓储、医疗照护、养老、零售服务、教育科研、危险环境、TCO、商业模式（RaaS/租赁/按任务付费）。

### 4.12 政策与伦理 / Policy & Ethics

- 数据隐私（GDPR/CCPA）、劳动市场影响、人机交互伦理、区域监管差异、责任分配。

---

## 5. 维度 C：知识类型

每个叶子工作流都会产出以下一种或多种知识资产：

| 类型 | 说明 |
|------|------|
| `paper` | arXiv、会议、期刊论文 |
| `dataset` | 训练/测试/遥测数据集 |
| `benchmark` | 仿真或真实任务基准 |
| `technology` | 算法、方法、架构 |
| `component` | 电机、减速器、传感器、电池、计算单元等 |
| `organization` | OEM、Tier-1/Tier-2 供应商、软件平台商 |
| `report` | 行业分析、市场预测、拆解报告 |
| `standard` | 安全、测试、数据治理标准 |

---

## 6. 维度 D：理论深度（从基础到应用）

理论深度维度回答“这个知识点站在哪些基础理论之上”。它让知识谱系从“工程应用”延伸到“基础学科”。

| 深度层级 | 代码 | 说明 | 示例 |
|----------|------|------|------|
| **基础学科** | `foundation` | 数学、物理、化学、经济学、计算机科学等底层学科 | 多元微积分、线性代数、凸优化、刚体动力学、电化学 |
| **定理/原理** | `principle` | 已被证明的数学定理或物理/化学原理 | KKT 条件、Lyapunov 稳定性定理、热力学第二定律、欧拉拉格朗日方程 |
| **形式化** | `formalism` | 把问题写成数学对象 | QP 优化问题、拉格朗日函数、状态空间模型、哈密顿量 |
| **方法/算法** | `method` | 具体的算法、技术路线或设计模式 | WBC、MPC、VLA、Diffusion Policy、Kalman Filter |
| **系统实现** | `system` | 集成后的硬件/软件/产品 | Tesla Optimus、Unitree G1、ROS 2 控制栈、工厂产线 |

一个实体可以跨越多个深度层级。例如，一篇 WBC 论文可能：

- 在 `method` 层提出新的 WBC 方法；
- 在 `formalism` 层把它形式化为 QP；
- 在 `principle` 层引用 KKT 条件；
- 在 `foundation` 层依赖凸优化与多元微积分。

---

## 7. 基础学科领域

基础学科不是单一工作流，而是多棵树的根系。我们为每门基础学科预留独立的研究分支：

| 基础学科 | 支撑的上层领域 | 示例知识点 |
|----------|----------------|------------|
| **数学 / Mathematics** | 控制、AI、规划、优化、仿真、经济学 | 线性代数、微积分、概率论、凸优化、微分几何、图论、数值分析 |
| **物理 / Physics** | 驱动、结构、传感器、电池、仿真 | 刚体动力学、电磁学、热力学、接触力学、材料力学 |
| **化学 / Chemistry** | 电池、材料、表面处理 | 电化学、配位化学、高分子化学、腐蚀与防护 |
| **计算机科学 / Computer Science** | 软件、AI、数据、仿真、中间件 | 算法与数据结构、分布式系统、实时系统、机器学习理论 |
| **经济学 / Economics** | 市场、供应链、商业模式 | 成本分析、产业组织、博弈论、技术扩散 |
| **运筹学与工业工程 / OR & IE** | 制造、物流、产线、质量 | 排程优化、库存管理、可靠性工程、统计过程控制 |

---

## 8. 工作流与四维空间的映射示例

| 工作流 | 阶段 | 领域 | 主要知识类型 | 理论深度 |
|--------|------|------|--------------|----------|
| `vla` | Definition → Algorithm Survey | Software & AI | paper, dataset, benchmark, technology | method / formalism |
| `whole_body_control` | Definition → Algorithm Survey | Software & AI | paper, technology | method / formalism |
| `actuator_module_design` | Design → Hardware | Hardware | paper, component, technology | system / method |
| `force_torque_sensors` | Design → Hardware | Hardware | paper, component, technology | system / method |
| `rare_earth_magnets` | Mass Production → Supply Chain | Supply Chain & Manufacturing | material, report, organization | system / principle |
| `simulation_platforms` | Design → Infra | Infra / Cloud / Fleet | software_platform, paper, technology | system / method |
| `iso_13482` | Verification Planning → Safety | Safety & Certification | standard, report | system / principle |
| `ai_to_hardware_requirements` | Cross-Domain | Software & AI ↔ Hardware | paper, technology, component | method / system |
| `convex_optimization` | Foundation | Mathematics | paper, theorem, foundation | foundation / principle |
| `rigid_body_dynamics` | Foundation | Physics | paper, theorem, foundation | foundation / principle |
| `battery_electrochemistry` | Foundation | Chemistry | paper, principle, foundation | foundation / principle |

---

## 9. 长期演进方式

1. **新增叶子**：当某个子领域积累到足以独立调研时，从 `WORKSTREAM_TREE.md` 中拆出新 YAML。
2. **执行与回填**：每次用 `AgentSwarm` 执行一个或几个分支，产出实体与关系后更新 `WORKSTREAM_TREE.md` 的复选框。
3. **阶段迁移**：随着项目成熟，某些工作流可能从 `Definition` 向 `DVT/PVT` 推进（例如从算法调研到量产测试）。
4. **理论下钻**：对关键算法或组件，逐步补全其 `foundation → principle → formalism → method → system` 链路。
5. **与本体对齐**：所有工作流的 `target_domains` 必须映射到 `docs/ontology/` 的 12 领域代码；基础学科工作流可映射到最接近的工程领域或使用新增的基础学科域。

---

## 10. 关键参考来源

1. **EVT/DVT/PVT 阶段门模型**：OpenBOM、Encata、Instrumental、Teksun、MacroFab 等行业解释。
2. **人形机器人供应链**：Morgan Stanley *The Humanoid 100*、McKinsey *Turning humanoid supply chain constraints into billion-dollar wins*。
3. **硬件价值链**：Fraunhofer IPA *The Humanoid Hardware Value Chain*、IDTechEx *Humanoid Robots 2025-2035*。
4. **软件栈**：ROS 2 on DDS、IEEE INFOCOM 2025 DDS 延迟模型、NVIDIA Isaac Sim/Lab、MuJoCo、Genesis。
5. **AI/数据**：GR00T N1、π0、OpenVLA、Open X-Embodiment、HumanoidBench、OmniH2O、HumanPlus。
6. **安全/标准**：ISO 13482:2025、ISO 10218-1/2:2025、ISO/TS 15066:2016、EU AI Act、EU Machinery Regulation。
7. **项目本体**：`docs/ontology/00_overview.md` 至 `12_policy_regulation_ethics.md`。
