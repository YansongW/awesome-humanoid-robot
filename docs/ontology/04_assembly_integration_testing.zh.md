# 04 组装、集成与测试

> **领域编码**：`04_assembly_integration_testing`  
> **价值链层**：中游（Midstream）  
> **状态**：草案 —— v0.1.0 前需复核  
> **用途**：定义将人形机器人零部件转化为经过验证系统的组装、集成与测试概念，并建立该领域与价值链其他环节的关联。

---

## 1. 核心问题

> **人形机器人如何从一堆零部件变成一台经过校准、验证且可部署的产品？**

人形机器人是现代制造业中机械与软件密度最高的产品之一。数十个高精度执行器、传感器、计算单元和线束必须被组装成运动链，校准到亚毫米精度，并针对安全性与性能要求进行验证，机器人才能出厂。本领域追踪从零部件到产品的转化过程。

---

## 2. 范围边界

### 2.1 在范围内

- 主要机械模块的子组装：腿部、躯干、手臂、头部和手部。
- 系统集成：布线、连接器、计算单元、电源分配和软件烧录。
- 运动学与传感器校准（关节编码器、IMU、力/力矩、视觉）。
- 关节性能、静态/动态平衡和全身行为的测试台。
- 硬件在环（HIL）与软件在环（SIL）验证。
- 安全验证：碰撞行为、紧急停止、力/压力限值。
- 环境测试：温度、振动、粉尘、防护等级。
- 质量门、可追溯记录和出厂验收标准。

### 2.2 不在范围内

- 单个零部件设计（见 `02_components_supply_chain` 和 `06_design_engineering`）。
- 生产原材料的制造工艺（见 `03_manufacturing_processes`）。
- 量产线经济性及良率优化（见 `05_mass_production`）。
- AI 模型与策略训练（见 `07_ai_models_algorithms`）。
- 现场部署与应用经济性（见 `11_applications_markets`）。

---

## 3. 关键概念

### 3.1 子组装与模块化集成

人形机器人通常以子组装堆叠的方式集成，而非一次性整体装配。这种模块化对诊断、维修和未来量产至关重要。

| 子组装 | 典型内容 | 集成风险 |
|--------|----------|----------|
| 腿部 | 髋/膝/踝关节执行器、足底力传感器、IMU 安装座 | 双足运动链对齐；背隙累积 |
| 躯干 | 电池包、主计算单元、电源分配、脊柱关节 | 热管理；线缆穿过活动关节的布线 |
| 手臂 | 肩/肘/腕执行器、触觉传感器 | 手眼协调依赖臂杆长度精度 |
| 头部 | 相机、激光雷达、麦克风、显示屏/扬声器 | 多传感器到头颈运动链的外参校准 |
| 手部 | 手指执行器、触觉阵列、腱/缆传动 | 零件数量多；需要精细机械调整 |

**来源与证据**：
- Boston Dynamics 描述其电动版 Atlas 面向企业应用，吸收了真实世界测试的经验，并持续迭代夹爪设计和全身控制集成 [Boston Dynamics Atlas 2026]。
- Fraunhofer IPA 的 KMUmanoid 项目搭建了变速箱装配演示器，研究人形机器人如何集成到中小企业工作流，重点关注可达性、安全距离和空间需求 [Fraunhofer IPA 2026]。
- 行业部署数据显示，汽车试点（BMW Figure 02、Mercedes Apollo、Tesla Optimus、Hyundai Atlas）目前仅执行物料搬运、零件配送等有限子任务，表明复杂装配工作流的全面集成仍处于试点阶段 [IDTechEx Humanoid Robots 2025；Fraunhofer IPA 2026]。

### 3.2 校准与运动学辨识

校准将名义 CAD 尺寸和传感器读数转化为控制软件可信任的一致身体模型。缺少校准，重复性会下降，操作精度会崩溃。

| 校准目标 | 估计对象 | 重要性 |
|----------|----------|--------|
| 关节编码器零位偏移 | 每个旋转关节的绝对零位 | 可重复的启动姿态和轨迹执行 |
| 连杆长度 / 关节轴 | Denavit-Hartenberg 或 URDF 几何参数 | 正/逆运动学和步态规划的精度 |
| IMU 安装对齐 | IMU 坐标系相对于骨盆/躯干的姿态 | 平衡控制的状态估计正确性 |
| 相机-手部（眼-手） | 相机到末端执行器的外参 | 精确抓取和视觉伺服 |
| 力/力矩传感器 | 零偏、标度、串扰、安装姿态 | 安全接触检测和阻抗控制 |

**来源与证据**：
- 一篇发表于 *Frontiers in Robotics and AI* 的 iCub 人形机器人论文提出无标记眼-手运动学校准方法，使用序贯蒙特卡洛参数估计来估计从头到手运动链的关节偏移 β，显著降低了感知手部位姿与模拟手部位姿之间的投影误差 [Vicente et al. 2018]。
- 相关校准研究指出，将视觉传感器、IMU 及其与人形机器人运动链联合进行外参校准，比单独校准每个传感器更困难；自动方法也比手动调谐更快、更准确 [Vicente et al. 2018]。

### 3.3 测试台与硬件在环（HIL）验证

在人形机器人下地行走之前，各子系统需在专用测试设备上运行。HIL 通过将真实控制器连接到模拟被控对象，弥合仿真与物理测试之间的差距。

| 测试类型 | 目的 | 典型设备 |
|----------|------|----------|
| 关节级测试台 | 扭矩/速度/摩擦特性、背隙测量 | 测功机、扭矩传感器、参考编码器 |
| 静态平衡平台 | 压力中心、重量分布、足底力校准 | 测力台、运动捕捉参考系统 |
| 动态步态测试装置 | 吊索保护下的行走、踏步、抗扰动 | 天车/系绳、 instrumented floor（带传感器的测力地板） |
| 操作测试台 | 抓取策略、夹爪耐久性、力控 | 物体集、力/力矩传感器、视觉系统 |
| 硬件在环（HIL） | 在模拟机器人/环境中验证控制器固件 | 实时仿真器（dSPACE、Speedgoat、NI）、被测控制器 |

**来源与证据**：
- MathWorks 文档将 HIL 测试定义为通过模拟/数字信号和 CAN、以太网等协议，把真实控制器硬件连接到实时仿真被控对象，从而在完整物理系统可用之前完成验证 [MathWorks HIL 2025]。
- Fraunhofer IPA 的人形机器人基准测试在六个模块中记录客观测量数据：基础能力、复杂能力、洁净室适用性、功能安全、网络安全和能效，使用 3D 跟踪系统和力传感器 [Fraunhofer IPA 2026]。
- 关于机电执行器的研究指出 HIL 变体包括信号/计算机 HIL（sHIL/cHIL）、功率 HIL（pHIL）和机械 HIL（mHIL），且这些技术要求实时仿真以捕捉动力学、时延和计算负载 [MathWorks HIL 2025]。

### 3.4 安全与环境验证

人形机器人兼具工业机器人、移动机器人、动力机械和电池系统的风险。由于目前尚无专门针对人形机器人的安全标准，现有部署依赖既有标准的组合。

| 标准 / 框架 | 范围 | 对人形机器人的相关性 |
|-------------|------|----------------------|
| ISO 10218-1:2025 | 工业机器人设计安全 | 机器人设计、执行器、紧急停止、保护性停止 |
| ISO 10218-2:2025 | 工业机器人系统集成 | 工作单元布局、风险评估、安全防护、验证 |
| ISO/TS 15066:2016 | 协作机器人（已并入 ISO 10218-2:2025） | 功率/力限制、速度/距离监控、生物力学阈值 |
| ISO 13482:2014 | 个人护理机器人 | 服务/家用型人形机器人；稳定性、避碰、故障安全行为 |
| ISO 25785-1（提案中） | 动态稳定人形机器人 | 双足移动与平衡风险 —— 尚未发布 |

**来源与证据**：
- ISO/TS 15066:2016 按身体部位定义了生物力学力/压力阈值（例如颅骨/前额瞬态力 130 N、胸部 140 N、手/指 140 N），并规定了功率/力限制和速度/距离监控等四种协作模式 [ISO/TS 15066:2016]。
- Fraunhofer IPA 的基准测试发现 Unitree G1 的碰撞力可超过 500 N，远高于 ISO/TS 15066 允许的疼痛阈值，揭示了当前硬件与协作力限之间的差距 [Fraunhofer IPA 2026]。
- ISO 13482:2014 针对移动服务机器人、物理辅助机器人和人员运送机器人，是目前服务导向型人形机器人最相关的既有标准，涵盖稳定性、避碰和故障安全行为 [ISO 13482:2014]。

### 3.5 软件集成与固件烧录

集成不仅是机械层面的。中间件、实时操作系统、设备驱动、安全控制器和 AI 推理栈必须能够启动、同步并从故障中恢复。

| 层级 | 集成关注点 | 典型产物 |
|------|------------|----------|
| 实时控制 | 关节控制器、安全停止、看门狗 | EtherCAT/CAN 总线配置、伺服驱动参数 |
| 中间件 | 感知、规划、控制之间的通信 | ROS 2、DDS、共享内存、时间同步（PTP） |
| 感知/AI 栈 | 相机、激光雷达、IMU 融合；策略推理 | 校准文件、模型权重、运行时流水线 |
| 车队/云端 | OTA 更新、任务调度、遥测 | 更新包、回滚镜像、事件日志 |
| 数字孪生 | 物理样机建造前的虚拟调试 | 与生产配置同步的仿真模型 |

**来源与证据**：
- Boston Dynamics 将 Atlas 与其 Orbit 车队管理平台集成，用于场地地图、任务调度、远程相机访问和人工巡检，展示了从单机到车队所需的软件层 [Boston Dynamics Atlas 2026]。
- 校准文献强调，相机、IMU 和运动学校准文件是必须与固件一起加载并版本控制的软件产物 [Vicente et al. 2018]。

---

## 4. 与其他领域的关系模式

| 来源领域 | 目标领域 | 关系 | 逻辑 |
|----------|----------|------|------|
| `04_assembly_integration_testing` | `02_components_supply_chain` | `integrates` | 组装领域将电机、传感器、电池、计算单元和结构件集成成机器人系统。 |
| `04_assembly_integration_testing` | `03_manufacturing_processes` | `consumes` / `is_prerequisite_for` | 组装消耗制造出来的零件；工艺能力（公差、表面质量）决定组装良率。 |
| `04_assembly_integration_testing` | `05_mass_production` | `is_prerequisite_for` | 经过验证的组装与测试流程是可重复量产的前提。 |
| `04_assembly_integration_testing` | `06_design_engineering` | `constrains` / `is_constrained_by` | 组装可行性与可维护性约束设计；设计选择决定组装顺序。 |
| `04_assembly_integration_testing` | `07_ai_models_algorithms` | `requires` / `is_validated_by` | 集成软件需要 AI 模型；测试台和真实试点验证控制与感知策略。 |
| `04_assembly_integration_testing` | `08_software_middleware` | `requires` | 系统集成依赖实时操作系统、中间件（ROS 2 / DDS）和通信总线。 |
| `04_assembly_integration_testing` | `10_evaluation_benchmarks` | `is_evaluated_by` | 组装质量、校准精度和安全性由基准与标准评估。 |
| `04_assembly_integration_testing` | `11_applications_markets` | `is_prerequisite_for` | 经过验证的机器人是工厂、物流或服务现场部署的前提。 |
| `04_assembly_integration_testing` | `12_policy_regulation_ethics` | `is_regulated_by` | 安全、环境和网络安全测试受标准与合格评定规则监管。 |

---

## 5. 受控词表

### 5.1 组装 / 集成 / 测试类别

- `subassembly`（子组装）
- `system_integration`（系统集成）
- `calibration`（校准）
- `kinematic_identification`（运动学辨识）
- `test_bench`（测试台）
- `hardware_in_the_loop` (`HIL`)（硬件在环）
- `software_in_the_loop` (`SIL`)（软件在环）
- `safety_validation`（安全验证）
- `environmental_testing`（环境测试）
- `firmware_flashing`（固件烧录）
- `OTA_update`（OTA 更新）
- `quality_gate`（质量门）
- `digital_twin_commissioning`（数字孪生调试）
- `factory_acceptance_test`（出厂验收测试）

### 5.2 相关实体类型

依据项目信息模型：

- `process`（流程）
- `tool_equipment`（工具/设备）
- `facility`（设施）
- `system`（系统）
- `standard`（标准）
- `benchmark`（基准）

---

## 6. 关键来源

### 6.1 主要 / 权威来源

1. **Fraunhofer IPA**. *Standardized analyses for application-relevant criteria of humanoid robots* (2026). 介绍包含六个模块的人形机器人基准测试（基础能力、复杂能力、洁净室、功能安全、网络安全、能效），并以 Unitree G1 为例；报告碰撞力超过 500 N，以及站立 2 小时 49 分钟 / 站走混合 1 小时 49 分钟的续航。同时涵盖面向中小企业的 KMUmanoid 变速箱装配演示器。  
   URL: https://silicon-saxony.de/en/fraunhofer-ipa-standardized-analyses-for-application-relevant-criteria-of-humanoid-robots/; https://silicon-saxony.de/en/fraunhofer-ipa-kmumanoid-project-tests-humanoid-robots-for-smes/

2. **International Organization for Standardization (ISO)**. *ISO 10218-1:2025 Robots and robotic devices — Safety requirements for industrial robots — Part 1: Robots* 与 *ISO 10218-2:2025 Part 2: Robot systems and integration* (2025). 工业机器人设计与集成的核心安全标准；2025 版整合了协作机器人要求并新增网络安全考量。  
   URL: https://www.iso.org/standard/86780.html (Part 1); https://www.iso.org/standard/86781.html (Part 2)

3. **International Organization for Standardization (ISO)**. *ISO/TS 15066:2016 Collaborative robots — Safety requirements* (2016). 定义功率/力限制、速度/距离监控、手动引导以及按身体部位划分的生物力学接触阈值；内容已并入 ISO 10218-2:2025。  
   URL: https://www.iso.org/standard/62996.html

4. **International Organization for Standardization (ISO)**. *ISO 13482:2014 Robots and robotic devices — Safety requirements for personal care robots* (2014). 针对移动服务机器人、物理辅助机器人和人员运送机器人的安全要求；是目前服务导向型人形机器人最相关的既有标准。  
   URL: https://www.iso.org/standard/53820.html

### 6.2 行业与市场分析

5. **IDTechEx**. *Humanoid Robots 2025-2035: Technologies, Markets and Opportunities* (2025). 跟踪零部件集成、汽车试点部署和市场时间线；指出汽车和物流是领先应用领域。  
   URL: https://www.idtechex.com/en/research-report/humanoid-robots/1093

6. **Boston Dynamics**. *Atlas Humanoid Robot* (2026). 官方产品页面，描述电动版 Atlas 的企业就绪状态、集成路线图、Orbit 车队软件以及在 Hyundai 的现场测试。  
   URL: https://bostondynamics.com/products/atlas/

### 6.3 领域专项来源

7. **Vicente P., Jamone L., Bernardino A.** "Markerless Eye-Hand Kinematic Calibration on the iCub Humanoid Robot." *Frontiers in Robotics and AI* 5:46 (2018). 开放获取论文，使用序贯蒙特卡洛参数估计沿眼-手运动链估计关节偏移。  
   URL: https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2018.00046/full

8. **MathWorks**. "What Is Hardware-in-the-Loop (HIL)?" (2025). 工程指南，解释 HIL 架构、MIL/SIL/PIL/HIL 的区别以及实时仿真器接口。  
   URL: https://www.mathworks.com/discovery/hardware-in-the-loop-hil.html

---

## 7. 开放问题

1. 高自由度人形机器人的最优模块化组装顺序和工装集是什么？从试制到量产会如何变化？
2. 如何在已部署车队中自动监测并修正关节零位、IMU 和眼-手校准漂移？
3. ISO 25785-1 或同类人形机器人专项安全标准发布后，将如何改变测试台要求和验收准则？
4. HIL、SIL 和数字孪生调试能在多大程度上减少商业发布前所需的物理样机和现场测试小时数？
