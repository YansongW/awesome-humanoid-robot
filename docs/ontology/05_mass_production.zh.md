# 05 量产与规模化

> **领域编码**：`05_mass_production`  
> **价值链层**：中游（Midstream）  
> **状态**：草案 —— v0.1.0 前需复核  
> **用途**：定义工厂设计、产能爬坡、供应链协同、良率控制和单位经济性等概念，说明如何将一台可工作的人形机器人原型转变为可规模化生产的产品。

---

## 1. 核心问题

> **从一台可工作的人形机器人到数千台乃至数百万台可靠、经济可行的产品，需要跨越什么？**

量产是验证原型与经济可部署产品之间的桥梁。在这里，设计选择、零部件可得性、装配纪律、测试覆盖度和物流能力交汇。对人形机器人而言，该领域尤为关键，因为整个行业正从手工打造的原型阶段迈向专用工厂，而许多零部件供应链仍不成熟。

---

## 2. 范围边界

### 2.1 在范围内

- 人形机器人生产的工厂布局、产线设计与产能规划。
- 产能爬坡策略、节拍优化和良率管理。
- 供应链协同、垂直整合决策，以及 Tier-1/Tier-2 供应商认证。
- 用于机器人生产的制造执行系统（MES）、产品生命周期管理（PLM）、ERP 和仓库管理系统（WMS）。
- 下线（EOL）测试、老化筛选、可靠性验证和质量追溯。
- 单位经济性、物料清单（BOM）降本、学习曲线，以及面向制造的设计（DFM）反馈闭环。
- 产线人力规划与人机协作生产。

### 2.2 不在范围内

- 零部件级设计与性能（见 `02_components_supply_chain`）。
- 单独的制造工艺，如 CNC 加工或注塑成型（见 `03_manufacturing_processes`）。
- 子系统装配、标定和集成测试台（见 `04_assembly_integration_testing`）。
- 未与量产规模化决策挂钩的一般性经济预测。

---

## 3. 关键概念

### 3.1 工厂设计与产能爬坡

人形机器人工厂的建设策略差异很大，从垂直整合的自有工厂到模块化、轻资本支出的装配工厂均有代表。

| 模式 | 示例 | 设计逻辑 | 公开规模 |
|------|------|----------|----------|
| 垂直整合、自有工厂 | Figure AI BotQ（加州） | 控制知识产权、质量、迭代速度和利润；采用自研 MES 和 PLM | 首条线年产约 12,000 台；四年目标 10 万台 [Figure 2025; Figure 2026] |
| 轻资本模块化装配 | Agility Robotics RoboFab（俄勒冈州） | 避免重型工业设备；工作站架构支持快速扩产 | 峰值产能 1 万台/年；首年产出数百台 [Agility 2025] |
| 区域生态/试点产线 | 深圳/乐聚机器人 Roban 2 产线 | 在量产转移前验证工艺稳定性；利用本地供应商基础 | 试点 500–1,000 台/年；量产线 >1 万台/年，每 30 分钟一台 [Shenzhen Gov 2026] |
| 汽车式超级工厂 | Tesla Optimus 产线（弗里蒙特/得州超级工厂） | 复用电动车生产经验；瞄准消费级规模 | 弗里蒙特目标 100 万台/年；得州目标 1000 万台/年 [Tesla 2026] |

**来源与证据**：
- Figure AI 称 BotQ  facility 从头开始为大批量制造而建，设有执行器、电池、传感器、结构件和电子器件的专用产线，并采用自研 MES [Figure 2025]。
- 2026 年 4 月，Figure 宣布 Figure 03 产出在不到 120 天内从每天 1 台提升到每小时 1 台，下线一次通过率超过 80%，电池线良率达 99.3% [Figure 2026]。
- Agility Robotics 将 RoboFab 描述为轻资本装配设施，设有腿部、手臂、躯干和执行器模块化工作站，各子装配节拍大致相同 [Agility 2025]。
- UBTECH 2025 年年报披露全尺寸人形机器人销量 1,079 台，年化产能超过 6,000 台，全尺寸人形业务收入达 8.206 亿元人民币 [UBTECH 2026]。
- **推测性说明**：Tesla 得州超级工厂 1000 万台/年的目标被广泛认为是愿景性目标。独立分析师认为，综合考虑建筑许可和供应商认证周期，到 2027 年实现 200–500 万台/年可能更为现实 [Tesla 2026]。

### 3.2 供应链协同与垂直整合

由于成熟的人形机器人分层供应链尚未形成，OEM 必须决定哪些子系统自制、哪些外购。

| 决策维度 | 内部制造（垂直整合） | 外部采购 |
|----------|----------------------|----------|
| 逻辑 | 控制知识产权、质量、迭代速度和利润 | 利用现有规模、避免资本密集、借助供应商专业能力 |
| 典型模块 | 执行器、灵巧手、电池包、软件栈 | 紧固件、轴承、通用电子件、部分铸件/冲压件 |
| 风险 | 资本密集、人才稀缺、供应商学习曲线较慢 | 供应商认证周期长、良率波动、地缘政治/出口管制风险 |

**来源与证据**：
- Figure AI 表示，其在执行器、电池、传感器、结构件和电子器件等核心模块上垂直整合，同时与能够满足产量和质量目标的关键零部件供应商战略合作 [Figure 2025]。
- 与 Apptronik 合作 Apollo 人形机器人的合同制造商 Jabil 指出，人形机器人供应链处于 15–20 年前 AMR/AGV 供应链的阶段：关键零部件因产量低、供应链尚未成形而价格昂贵 [Jabil 2026]。
- 据报道，Tesla 2025 年的产能爬坡受到中国 2025 年 4 月对钕铁硼磁材出口限制的制约，说明上游材料政策会直接打乱量产计划 [Tesla 2026]。

### 3.3 良率、质量控制与下线测试

在低产量阶段，手工调试和返工可以掩盖质量问题。规模化后，一致的良率需要过程内检测、自动化测试工站以及全零部件追溯。

| 质量层级 | 目的 | 示例 |
|----------|------|------|
| 来料检验 | 在零部件进入装配前剔除不合格品 | 齿轮尺寸检测、磁材牌号、绕组电阻 |
| 过程内检测 | 在子装配阶段发现缺陷 | 润滑脂涂覆验证、背隙测量、转矩脉动检测 |
| 下线（EOL）测试 | 在出货前验证整机功能 | 关节运动范围、老化（深蹲、慢跑）、传感器标定、急停验证 |
| 现场追溯 | 将失效与生产批次关联 | MES 谱系、零部件序列号、OTA 诊断反馈 |

**来源与证据**：
- Figure AI 报告设有 50 多个过程内检测点、每台机器人 80 多项功能验证测试，以及让机器人做数千次深蹲、肩上推举和慢跑的老化环节 [Figure 2026]。
- EngineAI 深圳基地报告每台机器人交付前需通过 79 项全维度质量检测和 46 项工况模拟测试，并实现全链路数字化追溯 [EngineAI 2026]。
- EYOU 机器人技术的自动化关节产线 reportedly 通过自动化和标准化实现一次通过率超过 95% [EYOU 2026; Global Times 2026]。
- 无框力矩电机自动化装配线正在出现，节拍约 180 秒/件、良品率 ≥99%，并具备 MES 追溯接口。

### 3.4 单位经济性与 BOM 降本

早期人形机器人成本主要由小批量零部件、手工装配和高返工率构成。量产通过经验曲线、工艺工装和设计简化来压降成本。

| 成本驱动 | 早期阶段影响 | 规模化缓解手段 |
|----------|--------------|----------------|
| 执行器/关节 | 低产量时约占 BOM 成本的 40–55% [DBS/TrendForce via ResearchWise 2025] | 自动绕线、压铸、冲压、标准化集成关节模块 |
| 灵巧手 | 微型执行器和线束复杂、人工含量高 | 工装化、注塑成型、金属粉末注射成型 |
| 手工装配与返工 | 单台工时长、质量不一致 | 产线平衡、工装自动化、测试自动化 |
| 低产量工装摊销 | 单台折旧高 | 更高产量分摊模具/工装成本 |

**来源与证据**：
- Goldman Sachs 将 2035 年人形机器人市场预测从 60 亿美元上调至 380 亿美元，理由是制造成本同比下降 40%，高端机器人生产成本从 5–25 万美元降至约 3–15 万美元 [Goldman Sachs via BardAI 2024; CircuitNet 2024]。
- Figure AI 将 Figure 02 的整块坯料 CNC 原型工艺，转为 Figure 03 的注塑、压铸和冲压等模具工艺，称原先需 CNC 加工一周以上的零件现在可在 20 秒内用复杂钢模完成 [Figure 2025]。
- DBS/TrendForce 分析估计，"运动层"（执行与传动）约占人形机器人 BOM 成本的 55%，而中国本土供应商在中国制造机器人中已贡献约 71.8% 的成本占比 [ResearchWise 2025]。
- **推测性说明**：Tesla 提出的 Optimus 2–3 万美元消费级售价目标，取决于数百万台的年产量，属于前瞻性公司目标 [Tesla 2026]。

### 3.5 制造系统与人力资源

规模化生产不仅需要硬件，还需要规划、执行和追溯的软件基础设施，以及具备机器人、自动化和质量系统跨学科技能的人才。

| 系统 | 在量产中的作用 | 对人形机器人的意义 |
|------|----------------|--------------------|
| MES（制造执行系统） | 实时生产跟踪、谱系、测试数据采集 | 因现成软件缺乏人形专用流程，常见自研 MES |
| PLM / ERP / WMS | 设计变更控制、采购、库存、 outbound 物流 | 对多 SKU 执行器管理和快速设计迭代至关重要 |
| 数字孪生/仿真 | 产线布局、吞吐优化、离线编程 | 缩短调试时间，验证人机工作单元 |
| 人力资源 | 装配技师、制造工程师、质量工程师、自动化专家 | 兼具 AI 与制造经验的复合型人才短缺被广泛认为是规模化瓶颈 |

**来源与证据**：
- Figure AI 明确将自研 MES 称为 BotQ 的"骨干"，整合供应链跟踪、装配效率监控和严格质量控制 [Figure 2025]。
- 安全标准 ISO 10218-1/2 和 ISO/TS 15066 规定了协作机器人系统的功率/力限制、速度/距离监控和风险评估要求，这些标准决定了人形机器人如何集成到共享生产单元 [Universal Robots 2018; A3 2016]。

---

## 4. 与其他领域的关系模式

| 来源领域 | 目标领域 | 关系 | 逻辑 |
|----------|----------|------|------|
| `05_mass_production` | `02_components_supply_chain` | `consumes` / `sources_from` | 工厂消耗执行器、传感器、电池和结构件；供应商认证决定爬坡速度 |
| `05_mass_production` | `03_manufacturing_processes` | `is_based_on` / `uses` | 量产放大特定工艺（CNC、压铸、注塑、绕线、SMT） |
| `05_mass_production` | `04_assembly_integration_testing` | `is_prerequisite_for` / `requires` | 稳定的装配与测试流程是可重复量产的前提 |
| `05_mass_production` | `06_design_engineering` | `constrains` / `feeds_back_to` | 制造能力约束驱动 DFM 反馈；设计选择决定工装和节拍 |
| `05_mass_production` | `07_ai_models_algorithms` | `requires` / `enables` | AI 指导视觉检测、机器人装配和车队诊断；生产数据反哺模型 |
| `05_mass_production` | `08_software_middleware` | `requires` | MES、PLM、ERP、WMS 和数字孪生平台是规模化必需 |
| `05_mass_production` | `11_applications_markets` | `produces` / `serves` | 量产向工业、物流乃至消费市场供应机器人 |
| `05_mass_production` | `12_policy_regulation_ethics` | `is_regulated_by` | 工厂安全、劳动保护、产品认证和出口管制塑造生产运营 |
| `05_mass_production` | `01_raw_materials` | `consumes` | 规模化集中消耗磁材、锂、铜、铝和工程聚合物 |

---

## 5. 受控词表

### 5.1 量产概念

- `production_ramp`（产能爬坡）
- `factory_design`（工厂设计）
- `vertical_integration`（垂直整合）
- `contract_manufacturing`（合同制造）
- `yield_management`（良率管理）
- `end_of_line_testing`（下线测试）
- `burn_in_testing`（老化测试）
- `manufacturing_execution_system`（制造执行系统）
- `digital_twin`（数字孪生）
- `design_for_manufacturability`（面向制造的设计）
- `bill_of_materials`（物料清单）
- `learning_curve`（学习曲线）
- `cycle_time`（节拍）
- `throughput`（产出）
- `component_traceability`（零部件追溯）

### 5.2 相关实体类型

依据项目信息模型：

- `facility`（工厂、产线）
- `tool_equipment`（测试台、装配工装、自动化工站）
- `oem`（机器人制造商）
- `tier1_supplier`（Tier-1 供应商）
- `tier2_supplier`（Tier-2 供应商）
- `component_manufacturer`（零部件制造商）
- `software_platform`（MES、PLM、ERP、WMS）
- `report`（市场分析、拆解报告）
- `standard`（标准）

---

## 6. 关键来源

### 6.1 主要 / 权威来源

1. **Figure AI**. *BotQ + Ramping Figure 03 Production* (2025–2026). 公司官方来源，阐述垂直整合、从 CNC 到压铸/注塑的工装转换、自研 MES/PLM，以及从每天 1 台提升到每小时 1 台的爬坡，一次通过率 >80%。  
   URLs: https://www.figure.ai/news/botq; https://www.figure.ai/news/ramping-figure-03-production

2. **Agility Robotics**. *RoboFab* (2025). 官方介绍其 70,000 平方英尺轻资本工厂、模块化工作站及 10,000 台/年峰值产能。  
   URL: https://agilityrobotics.com/robofab

3. **UBTECH Robotics**. *Annual Report 2025* (2026). 披露 2025 年全尺寸人形机器人销量 1,079 台、相关收入 8.206 亿元人民币，年化产能超过 6,000 台。  
   URL: https://owebsite-cdn.ubtrobot.com/resources/file/2026/04/21/797179114676293.pdf

### 6.2 行业与市场分析

4. **Goldman Sachs / DBS-TrendForce**. *Humanoid Robot Market and BOM Cost Analysis* (2024–2025). Goldman Sachs 将 2035 年市场预测上调至 380 亿美元，并指出制造成本同比下降约 40%；DBS/TrendForce 估算运动/执行层约占 BOM 成本 55%，中国制造机器人中本土供应商成本贡献约 71.8%。  
   URLs: https://bardai.ai/2024/03/28/goldman-sachs-over-1-million-humanoids-will-likely-be-produced-annually-in-10-years/; https://researchwise.dbsvresearch.com/ResearchManager/DownloadResearch.aspx?E=ifaeakhah

5. **Jabil / Robotics and Automation News**. *Scaling Humanoid Robots from Prototype to Production* (2026). 合同制造商视角，讨论供应链成熟度、单位经济性、DFM 和安全验证。  
   URL: https://roboticsandautomationnews.com/2026/04/16/interview-jabil-on-scaling-humanoid-robots-from-prototype-to-production/100706/

### 6.3 领域专项来源

6. **中国量产生态**（2026）。Shenzhen Government Online 报道乐聚机器人试点产线及年产超 1 万台的自动化产线；EngineAI 介绍其 12,000 平方米深圳基地及 15 分钟节拍；EYOU/Global Times 报道世界首条人形机器人关节自动化产线，年产能 10 万件，一次通过率 >95%。  
   URLs: https://www.sz.gov.cn/en_szgov/news/infocus/aisz/news/content/post_12733795.html; https://www.morningstar.com/news/pr-newswire/20260529cn70096/engineai-launches-shenzhen-intelligent-manufacturing-base-as-first-batch-of-t800-humanoid-robots-roll-off-the-production-line-to-begin-mass-delivery; https://hotel.report/technology/chinese-company-launches-automated-production-line-for-robot-joints-step-toward-humanoid-robots-mass-production

7. **ISO/TS 15066 Collaborative Robot Safety**（Universal Robots 2018; A3 2016）。协作机器人系统的功率/力限制、速度/距离监控和风险评估技术规范。  
   URL: https://www.universal-robots.com/news-and-media/news-center/universal-robots-welcomes-the-new-technical-specification-on-collaborative-robot-design/

8. **Tesla / 行业报道中的 Optimus 量产目标**（2025–2026）。汇总第三方行业跟踪者报道的公司目标：2025 年 5,000–10,000 台、2026 年 5–10 万台、2–3 万美元消费级售价目标、得州超级工厂 1000 万台/年愿景。这些属于公司前瞻性目标，非独立核实的产量数据。  
   URLs: https://optimusk.blog/blog/what-is-tesla-optimus/; https://www.ccn.com/news/technology/how-much-does-tesla-optimus-cost-elon-musk/

---

## 7. 开放问题

1. 人形机器人装配的学习曲线指数是否有经验验证？哪些子系统（执行器、灵巧手、电池包）在产量扩大时主导成本下降？
2. 本体应如何表示工厂级数据：是否应将每条产线、每个工作站、每个测试工站作为独立的 `facility`/`tool_equipment` 实体，还是将工厂属性嵌入 OEM 实体？
3. 哪些人形机器人量产声明（如 Tesla 得州超级工厂 1000 万台/年目标、Figure 四年 10 万台目标）有可信的物理证据支持，哪些属于公司前瞻性指引？
4. 跨领域比较 OEM 量产成熟度时，最有效的指标是什么：良率、节拍、产能利用率，还是单台单系统成本？
