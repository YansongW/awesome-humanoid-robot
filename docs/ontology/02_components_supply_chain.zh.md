# 02 零部件与供应链

> **领域编码**：`02_components_supply_chain`  
> **价值链层**：上游（Upstream）  
> **状态**：草案 —— v0.1.0 前需复核  
> **用途**：定义位于原材料与制造/组装之间的零部件与供应链概念，并建立该领域与价值链其他环节的关联。

---

## 1. 核心问题

> **人形机器人的主要硬件构成模块是什么？由谁供应？它们的性能、成本和可得性如何决定量产可行性？**

人形机器人是机电、感知、能源、计算与结构子系统的高度集成体。本领域追踪的是在它们被组装成完整机器人之前的那些子系统：电机、减速器、传感器、电池、边缘计算机、线束、结构件，以及生产这些部件的分层供应商网络。这里的零部件选择会向下游传导为设计约束、制造复杂度、单位经济性以及应用场景能力。

---

## 2. 范围边界

### 2.1 在范围内

- 执行器、电机、减速器/齿轮箱、传动机构、末端执行器。
- 传感器：相机、深度传感器、激光雷达、IMU、力/力矩传感器、触觉传感器、关节编码器。
- 能源子系统：电芯/电池包、电池管理系统（BMS）、充电器、热管理。
- 计算单元：边缘 AI SoC/GPU、嵌入式实时控制器、传感器接口。
- 结构件、线束、连接器、紧固件。
- 供应商层级（Tier-2、Tier-1、OEM）、集成策略与 BOM 成本驱动因素。
- 供应链风险：交期、地理集中度、单一来源、认证瓶颈。

### 2.2 不在范围内

- 原材料开采与冶炼（见 `01_raw_materials`）。
- 数控加工、绕线、PCB 制造等转化工艺（见 `03_manufacturing_processes`）。
- 最终组装、标定与系统级测试（见 `04_assembly_integration_testing`）。
- AI 模型、软件栈与数据集（见 `07_ai_models_algorithms`、`08_software_middleware`、`09_data_datasets`）。
- 终端应用市场与政策框架（见 `11_applications_markets`、`12_policy_regulation_ethics`），除非直接影响零部件需求或成本。

---

## 3. 关键概念

### 3.1 执行与传动子系统

人形机器人的运动与操作需要紧凑、高扭矩、可反向驱动的关节。当前多数电动人形机器人采用无刷直流或永磁同步电机，配合减速器、位置传感器和驱动器，组成一体化关节模组。

| 零部件 | 功能 | 常见技术 | 关键指标 |
|--------|------|----------|----------|
| 旋转关节模组（rotary actuator module） | 产生可控关节扭矩 | BLDC/PMSM 电机 + 减速器 + 编码器 + 驱动器 | 扭矩密度、峰值扭矩、可反向驱动性、效率、成本 |
| 减速器/齿轮箱（reducer / gearbox） | 扭矩放大与减速 | 谐波减速器、摆线减速器、行星减速器、准直驱（QDD） | 减速比、背隙、效率、刚度、寿命 |
| 线性执行器（linear actuator） | 提供直线驱动力，如腿部伸展 | 无框电机 + 滚珠/滚柱丝杠 | 出力、行程、速度、力密度 |
| 末端执行器/手（end effector / hand） | 抓取与操作物体 | 腱传动、齿轮传动、欠驱动 | 自由度、夹持力、触觉感知、成本 |

**来源与证据**：
- Fraunhofer IPA 的自底向上硬件价值链分析指出，执行器、齿轮、电池和传感器在鲁棒性、使用寿命和成本结构方面尚未充分满足工业要求；该研究还将柔性手列为当前最大的规模化瓶颈 [2]。
- IDTechEx 提供了零部件级技术与成本分析，涵盖执行器、电机、减速器、丝杠、轴承、末端执行器等，并给出各类零部件的十年市场预测 [1]。
- 一项针对人形机器人低背隙行星减速器的对比研究表明，所提出的行星方案背隙小于 4 角分、效率约 97%、承载能力约为同类谐波减速器的 4 倍、价格约低 5 倍，外形尺寸相近而质量约大 10%，说明行星替代方案正变得可行 [6]。
- Unitree H1 展示了当前执行器性能：膝关节峰值扭矩约 360 N·m， reported 峰值扭矩密度约 189 N·m/kg [4]。

### 3.2 感知子系统

传感器将物理世界转换为感知与控制算法可用的信号。人形机器人通常融合外部感知传感器（相机、深度、激光雷达）与本体感知传感器（IMU、编码器、力/力矩），并越来越多地采用触觉阵列以支持操作。

| 传感器类型 | 作用 | 示例 | 关键指标 |
|------------|------|------|----------|
| 视觉相机（vision cameras） | RGB/视觉感知 | 立体 RGB、全局快门、鱼眼 | 分辨率、视场、延迟、动态范围 |
| 深度/三维传感器（depth / 3D sensors） | 场景几何与障碍物检测 | 立体深度、ToF、结构光、激光雷达 | 量程、精度、点密度、抗强光能力、成本 |
| IMU | 姿态与加速度 | MEMS IMU | 零偏稳定性、噪声密度、带宽 |
| 关节编码器（joint encoders） | 关节位置与速度 | 光电/磁电增量式与绝对式编码器 | 分辨率、精度、鲁棒性 |
| 力/力矩与触觉（force/torque & tactile） | 接触检测与柔顺操作 | 腕部六维力/力矩传感器、指尖触觉阵列 | 分辨率、量程、柔顺性、耐久性 |

**来源与证据**：
- IDTechEx 将相机、激光雷达、雷达、超声波和触觉传感器纳入其人形机器人零部件级分析 [1]。
- Unitree H1 标配 3D 激光雷达与深度相机实现 360° 全景扫描，并配备 IMU、关节编码器和力传感器 [4]。
- Fraunhofer IPA 将感知列为四大硬件价值链支柱之一（传感器、执行器、结构、能源），并指出传感器的可靠性与成本是工业可扩展性的核心 [2]。
- Figure 02 集成六颗车载 RGB 相机与车载视觉-语言模型；其手部具备 16 自由度并配备触觉感知以支持灵巧操作 [7]。

### 3.3 能源与热管理子系统

功率密度与热管理直接决定续航、动态性能与安全。当前人形机器人主要复用电动汽车或消费电子供应链的锂离子电池，而固态电池及更高能量密度化学体系仍在发展中。

| 零部件 | 功能 | 典型化学体系/架构 | 关键指标 |
|--------|------|-------------------|----------|
| 电芯/电池包（battery cells / pack） | 储能与放电 | 磷酸铁锂、三元锂/镍钴铝；固态电池新兴 | 能量密度（Wh/kg）、循环寿命、倍率、成本（$/kWh） |
| 电池管理系统（BMS） | 安全、均衡与状态估计 | BMS + 接触器 + 保险丝 + 温度传感器 | SoC/SoH 精度、热失控防护 |
| 充电/换电（charging / swapping） | 补能或更换电池 | 充电桩、传导充电、热插拔电池包 | 充电时间、换电时间、车队可用率 |
| 热管理（thermal management） | 维持执行器与计算单元温度 | 散热片、风扇、热管、液冷、导热界面材料 | 热设计功耗、结温、可靠性 |

**来源与证据**：
- Interact Analysis 对比了当前人形机器人的电池配置：Tesla Optimus Gen-2  reportedly 采用 2.3 kWh 电池包，动态续航约 2 小时；Unitree H1 采用 864 Wh 可换电电池包；三元材料占主导，固态电池试点正在出现 [3]。
- Fraunhofer IPA 指出，当前约 200 Wh/kg 的现货锂离子电池足以满足演示需求，但不足以支撑多数工业场景；固态电池有望超过 500 Wh/kg [2]。
- Unitree 官方规格显示 H1 电池为 15 Ah（0.864 kWh），最高电压 67.2 V，支持快速更换 [4]。
- Figure 02 采用躯干集成的 2.25 kWh 电池包，能量较 Figure 01 提升约 50%，依据任务强度可支持约 5 至 10 小时运行 [7]。

### 3.4 计算、通信与结构骨架

计算单元需在严格的功耗与热预算内完成高速传感器融合、感知、规划和底层电机控制。结构骨架与线束则需承载载荷、布设动力/信号，并承受反复运动和跌落的冲击。

| 零部件 | 作用 | 示例 | 关键指标 |
|--------|------|------|----------|
| 边缘 AI 计算（edge AI compute） | 运行感知、规划与学习模型 | NVIDIA Jetson AGX Orin / Thor、Intel Core、定制 SoC | TOPS/W、内存带宽、延迟、I/O |
| 实时控制器（real-time controller） | 确定性关节控制与安全 | 微控制器、FPGA、电机驱动器 | 控制周期、确定性总线、功能安全支持 |
| 通信总线（communication buses） | 连接传感器、执行器与计算 | CAN-FD、EtherCAT、以太网、USB、MIPI CSI-2 | 带宽、延迟、确定性、布线复杂度 |
| 结构件与线束（structural parts & cabling） | 机械骨架、线束、连接器 | 铝/镁/复合材料骨架、线束、连接器 | 比强度、模块化、EMI 屏蔽、可维护性 |

**来源与证据**：
- NVIDIA Jetson AGX Orin 系列最高提供 275 TOPS AI 算力，功耗 15–60 W，最高 64 GB LPDDR5 内存与 204.8 GB/s 内存带宽，并支持多路高速相机接口 [5]。
- Unitree H1 标配 Intel Core i5/i7 计算单元，可选 NVIDIA Jetson Orin NX；软件栈兼容 ROS2 [4]。
- Fraunhofer IPA 将结构与能源列为核心硬件价值链环节，并强调不同硬件决策会显著影响系统总成本 [2]。
- IDTechEx 追踪软件/AI、高性能材料和末端执行器等零部件，突出计算与机械设计的交互 [1]。

### 3.5 供应链架构与分层

人形零部件供应链尚不成熟。多数领先 OEM 选择垂直整合执行器与手部以保护知识产权并控制成本，而连接器、紧固件、标准传感器等通用件则从既有 Tier-1/Tier-2 供应商采购。

| 层级 | 典型角色 | 对人形机器人的意义 |
|------|----------|-------------------|
| Tier-2 | 材料、加工件与半导体 | 漆包线、稀土磁材、齿轮坯、MEMS 芯片、电芯、铸件 |
| Tier-1 | 子系统/模组供应商 | 关节模组、电池包、传感器模组、计算模组、线束 |
| OEM / 机器人品牌 | 系统集成与最终产品 | Tesla、Figure、Unitree、Agility、Apptronik、Boston Dynamics |
| 售后/服务 | 备件、换电、翻新、回收 | 服务网络、再制造、电池闭环回收 |

**来源与证据**：
- Fraunhofer IPA 认为，欧洲零部件制造商可通过专注于成本与性能相关的硬件零部件，并及早与人形机器人 OEM 合作，进入这一新兴价值链 [2]。
- IDTechEx 的市场预测按执行器、电机、减速器、传感器、电池和高性能材料等维度拆分零部件需求，从需求侧刻画供应商机会 [1]。
- *推测*：随着产量增长，我们预计 Tier-1 模组供应商将向标准化的执行器、电池和计算平台集中；但目前 OEM 专用设计仍占主导，垂直整合程度较高。

---

## 4. 与其他领域的关系模式

| 来源领域 | 目标领域 | 关系 | 逻辑 |
|----------|----------|------|------|
| `02_components_supply_chain` | `01_raw_materials` | `consumes` | 电机消耗钕铁硼磁材和铜；电池包消耗锂电芯；结构件消耗铝、镁和复合材料 |
| `03_manufacturing_processes` | `02_components_supply_chain` | `produces` | 电机需绕线与组装；齿轮需滚齿/磨齿；PCB 需制造与贴片；电芯需成组封装 |
| `02_components_supply_chain` | `04_assembly_integration_testing` | `is_part_of` | 关节模组、传感器套件、电池包和计算单元被集成并标定到整机中 |
| `02_components_supply_chain` | `05_mass_production` | `constrains` | 零部件成本、交期、良率和供应商产能决定产能爬坡与单位经济性 |
| `02_components_supply_chain` | `06_design_engineering` | `enables` / `constrains` | 执行器扭矩密度与传感器能力约束形态、运动学与控制架构 |
| `02_components_supply_chain` | `07_ai_models_algorithms` | `requires` / `enables` | VLA 需要边缘算力；力/力矩传感器支持接触丰富的学习；低延迟总线支持全身控制 |
| `11_applications_markets` | `02_components_supply_chain` | `drives_demand_for` | 工业任务驱动负载、续航、防护等级与安全传感器的需求 |

---

## 5. 受控词表

### 5.1 类别标签

- `actuator`（执行器）
- `motor`（电机）
- `reducer`（减速器）
- `gearbox`（齿轮箱）
- `harmonic_drive`（谐波减速器）
- `cycloidal_drive`（摆线减速器）
- `planetary_gearbox`（行星减速器）
- `quasi_direct_drive`（准直驱）
- `sensor`（传感器）
- `camera`（相机）
- `lidar`（激光雷达）
- `depth_sensor`（深度传感器）
- `imu`（惯性测量单元）
- `force_torque_sensor`（力/力矩传感器）
- `tactile_sensor`（触觉传感器）
- `encoder`（编码器）
- `battery_pack`（电池包）
- `bms`（电池管理系统）
- `edge_compute`（边缘计算）
- `jetson`（Jetson 计算平台）
- `end_effector`（末端执行器）
- `robot_hand`（机器手）
- `cable_harness`（线束）
- `structural_part`（结构件）
- `tier1_supplier`（一级供应商）
- `tier2_supplier`（二级供应商）
- `component_manufacturer`（零部件制造商）
- `bill_of_materials`（物料清单/BOM）

### 5.2 相关实体类型

依据项目信息模型：

- `component`
- `tier1_supplier`
- `tier2_supplier`
- `component_manufacturer`
- `robot_system`
- `technology`
- `report`
- `standard`

---

## 6. 关键来源

### 6.1 主要 / 权威来源

1. **IDTechEx**. *Humanoid Robots 2025-2035: Technologies, Markets and Opportunities* (2025). 零部件级技术与成本分析，涵盖执行器、电机、减速器、丝杠、轴承、相机、激光雷达、触觉传感器、电池和末端执行器，并提供十年市场预测。  
   URL: https://www.idtechex.com/en/research-report/humanoid-robots/1093

2. **Fraunhofer IPA**. *The Humanoid Hardware Value Chain* (2026). 白皮书分析传感器、执行器、结构和能源四大硬件领域，建立自底向上成本模型，并指出零部件在鲁棒性、使用寿命和成本方面的工业缺口。  
   URL: https://www.ipa.fraunhofer.de/content/dam/ipa/de/documents/Publikationen/Studien/260219_Humanoid_Value_Chain_final.pdf

3. **Interact Analysis**. *Humanoid Robots and Lithium-Ion Batteries* (2026). 对比 Tesla Optimus 与 Unitree H1 的电池配置，讨论锂离子电池化学体系选择与固态电池试点。  
   URL: https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/

### 6.2 行业与产品来源

4. **Unitree Robotics**. *Unitree H1 Humanoid Robot — Product Specifications* (2025). 官方产品页列出关节扭矩、电池容量、传感器套件、计算选项与外形尺寸。  
   URL: https://unitreerobotics.us/products/unitree-h1-humanoid-robot

5. **NVIDIA**. *Jetson AGX Orin Series*（官方产品页）。 说明最高 275 TOPS AI 性能、15–60 W 功耗、内存带宽及相机/IO 支持。  
   URL: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/

6. **Built In**. *What Is Figure AI Building?* (2024). 介绍 Figure 02 硬件，包括六颗 RGB 相机、2.25 kWh 电池、16 自由度手部以及较前代 3 倍计算能力提升。  
   URL: https://builtin.com/articles/figure-ai

### 6.3 领域专项 / 技术来源

7. **Pencic, M. 等**. *Development of the Low Backlash Planetary Gearbox for Humanoid Robots*. FME Transactions, vol. 45 (2017). 同行评审的低背隙行星减速器与谐波减速器对比研究，报告效率、承载能力与成本权衡。  
   URL: https://www.mas.bg.ac.rs/_media/istrazivanje/fme/vol45/1/20_mpencic_et_al_doi.pdf

---

## 7. 开放问题

1. 基于已验证的拆解或 OEM 披露，商业化人形机器人（如 Unitree H1、Figure 02、Agility Digit）的零部件成本分解与供应商映射是怎样的？
2. 当产量从数百台增长到数万台时，谐波减速器、摆线减速器、行星减速器和准直驱架构之间的选择将如何演变？
3. 对于工业任务，哪些传感器与计算配置是“必要”而非“充分”的，它们与电池续航和热预算之间存在怎样的权衡？
4. 本体应如何表示零部件变型（如电机绕组、减速比、电池化学体系）以及 Tier-1/Tier-2 供应商之间的多源供应关系？
