# 03 制造工艺

> **领域编码**：`03_manufacturing_processes`  
> **价值链层**：上游（Upstream）  
> **状态**：草案 —— v0.1.0 前需复核  
> **用途**：定义将原材料和零部件转化为人形机器人级部件的制造与加工工艺，并建立该领域与价值链其他环节的关联。

---

## 1. 核心问题

> **人形机器人的物理部件是如何制造的？哪些工艺选择决定了精度、良率、成本和可扩展性？**

人形机器人是对公差要求极高的机电一体化装配体：高扭矩密度关节、轻量化结构、密集的线缆布线以及紧凑的传感器/电子集成。某一部件在一次性原型中可行，但如果选错了成形、机加工、绕线或连接工艺，在批量生产中就可能失效。本领域追踪在子系统被组装成完整机器人之前的上游转化步骤。

---

## 2. 范围边界

### 2.1 在范围内

- 结构件和机械零件的机加工、铸造、模塑和成形。
- 定子/转子绕线、铁芯叠压、磁钢插入以及电机执行器装配。
- 齿轮切削、磨削、珩磨以及精密减速器装配。
- PCB 制造、SMT 贴装、线束制造以及连接器集成。
- 表面处理、热处理、涂层和清洗工艺。
- 制程中检测、下线检测、计量与质量控制。
- 工艺能力、良率以及面向制造的设计（DFM）权衡。

### 2.2 不在范围内

- 原材料开采与提炼（见 `01_raw_materials`）。
- 成品部件规格与供应商生态（见 `02_components_supply_chain`）。
- 最终机器人组装、标定与系统测试（见 `04_assembly_integration_testing`）。
- 工厂级产能爬坡与单位经济性（见 `05_mass_production`）。

---

## 3. 关键概念

### 3.1 结构件与机械零件加工

人形机器人需要轻量化、高刚度且定位精确的框架、关节壳体、执行器支架和护盖等部件。主要的工艺族在成本、精度和产量适用性上各不相同：

| 工艺 | 典型零件 | 公差 / 特征 | 批量经济性 |
|------|----------|-------------|-----------|
| CNC 机加工 | 关节壳体、执行器接口、支架 | 微米级重复精度，几何柔性高 | 小–中批量；周期较长，废品风险较高 |
| 压铸 | 铝制框架、电机壳体、结构外壳 | 表面质量好；需控制气孔以避免泄漏或焊接区缺陷 | 中–大批量；需模具投入 |
| 金属注射成形（MIM） | 微型齿轮、复杂钢制支架、集成齿轮轴组件 | 尺寸公差 ±0.3–0.5%；壁厚可低至 0.5–1.0 mm | 大批量；近净成形减少材料浪费 |
| 钣金加工 | 护盖、屏蔽罩、支架、外壳 | 速度快、成本低；限于 2.5D 形态 | 大批量；常与冲压、折弯结合 |
| 增材制造（金属/高分子） | 原型支架、拓扑优化连杆、定制夹具 | 设计自由度高；表面质量和疲劳性能因工艺而异 | 原型和小批量；生产应用正在兴起 |

**来源与证据**：
- 行业制造分析指出，人形机器人依赖精密 CNC 机加工、压铸、钣金加工、注塑和定制紧固件；关节壳体、执行器外壳和框架被列为质量直接影响稳定性、寿命和安全性的关键零件 [Yijin Solution 2026]。
- Fraunhofer IPA 与 P3 强调，欧洲汽车与机械制造企业可凭借轻量化设计、先进制造工艺和工业质量管理方面的能力，参与新兴的人形硬件价值链 [Fraunhofer IPA 2026]。
- 据报道，MIM 对复杂零件的材料利用率约 97%，而 CNC 机加工约 30%；±0.3–0.5% 的公差和 0.5–1.0 mm 的壁厚可实现紧凑的机器人关节几何 [JHMIM 2026]。

> 🔮 **推测 / 前瞻性**：增材制造常被视作拓扑优化、小批量机器人零件的使能技术，但疲劳寿命、表面质量和成形速率限制意味着其在大批量人形机器人生产中的角色仍不确定。当前价值主要体现在原型、夹具和非结构性定制件。

### 3.2 电机与执行器装配

大多数人形关节采用无刷永磁同步电机搭配减速器。电机制造序列是一个精密机电过程：

| 工序 | 关键操作 | 质量驱动因素 |
|------|----------|--------------|
| 定子铁芯制造 | 冲片冲压/激光切割、叠压、焊接/粘接 | 铁损、叠厚一致性、同轴度 |
| 定子绕线 | 针式/飞叉绕线、嵌线、扁线成型 | 槽满率、张力、匝数、绝缘完整性 |
| 整圆与焊接 | 线圈整形、相线激光/TIG 焊接 | 引线位置、接头电阻、热管理 |
| PCBA 集成 | 定子引线与控制 PCBA 焊接、三防涂覆 | 电气可靠性、焊点质量 |
| 转子装配 | 轴压装、磁钢插入/粘接、动平衡 | 磁钢位置精度、磁场均匀性、不平衡量 |
| 电机总装 | 定转子合装、轴承安装、编码器装配 | 气隙均匀性、齿槽转矩、噪声 |

**来源与证据**：
- GROB 提供自动化定子绕线、转子装配和电机总装产线，包括针式绕线、扁线加工、机器人磁钢插入以及浸漆单元；该公司指出转子磁钢插入和粘接对电机性能至关重要 [GROB 2026]。
- Magnetic Innovations 介绍了一种自动化转子装配单元，可测量每块磁钢的磁性能、采用大气等离子表面预处理，并扫描成品转子磁场以验证均匀性和可追溯性 [Magnetic Innovations 2024]。
- 一家人形执行器产线供应商记录了定子装配流程，包括绕线、整圆激光焊接、PCBA 焊接和机壳热套，并配备在线力、温度和压力监测 [Honest HLS 2024]。

> ⚠️ **部分验证**：Tesla Optimus、Unitree H1 或 Figure 02 电机的详细一手 BOM 和周期时间未公开。上述工序序列是工业 BLDC/PMSM 电机制造的代表性流程，需在有具体 OEM 拆解时进一步验证。

### 3.3 精密齿轮与减速器制造

减速器将电机的高速低扭矩输出转换为关节的低速高扭矩运动。人形机器人中常见的结构包括谐波减速器、行星减速器和摆线减速器。精度是制造的主要约束：

| 减速器类型 | 关键制造步骤 | 关键质量属性 |
|------------|--------------|--------------|
| 谐波减速器 | 柔轮成形/滚压、刚轮齿轮切削、波发生器加工 | 背隙、柔轮疲劳寿命、位置精度 |
| 行星减速器 | 太阳轮/行星轮/齿圈滚齿或磨齿、轴/行星架加工、轴承选型 | 背隙、扭转刚度、效率、噪声 |
| 摆线减速器 | 摆线盘磨削、针齿加工、输出轴装配 | 接触印痕、刚度、效率、润滑油保持 |

**来源与证据**：
- 一篇机器人精密齿轮制造综述指出，滚齿、磨齿、珩磨和硬齿面精加工是核心工艺，并强调加工精度、表面完整性和生产成本之间的权衡 [Zhang et al. 2021]。
- 关于类机器人齿轮的研究表明，齿廓修形、热处理和表面精加工显著影响载荷分布、噪声和疲劳寿命 [Oberneder et al. 2024]。
- PICEA MOTION 指出，谐波减速器柔轮必须承受持续弹性变形并保持微米级精度，装配需要先进设备和检测设备；并与大学合作解决材料和机械优化问题 [PICEA MOTION 2025]。
- 机器人精密减速器市场分析预计，全球市场将从 2024 年约 12 亿美元增长至 2033 年约 25 亿美元，复合年增长率约 9.2%，人形机器人被列为关键应用细分市场 [Verified Market Reports 2025]。

### 3.4 电子互联、表面处理与质量保证

人形机器人是高密度机电系统。制造必须在紧凑空间和可靠性约束下集成功率电子、传感器 PCB、通信线缆和防护涂层：

| 领域 | 关键工艺 | 人形机器人特定考量 |
|------|----------|--------------------|
| PCB 与 SMT | 多层 PCB 制造、SMT 贴装、回流焊、三防涂覆 | 小型化、信号完整性、热循环耐受 |
| 线束 | 裁切、剥线、压接、连接器装配、布线辅助 | 活动关节的高柔性循环要求；EMI 屏蔽 |
| 表面处理 | 阳极氧化、钝化、PVD/CVD 涂层、等离子清洗 | 耐磨、防腐、人体接触生物相容性 |
| 质量保证 | 三坐标测量、视觉检测、扭矩监测、功能测试台 | 可追溯性、SPC、工艺能力指数（Cp/Cpk） |

**来源与证据**：
- Fraunhofer IPA 发布的人形机器人工业基准包含 ISO 标准颗粒物排放和除气测试，表明污染行为和洁净室兼容性正成为敏感部署环境下正式的制造要求 [Fraunhofer IPA 2026；HyperSinc 2026]。
- ISO 10218-1 和 ISO 10218-2 规定了机器人设计/制造与系统集成的安全要求，包括保护性停止功能、速度/力监测以及安全功能验证；这些标准塑造了可部署机器人的制造测试协议 [ISO 10218-1:2011；ISO 10218-2:2025]。
- Magnetic Innovations 将自动化等离子清洗和粘接工艺控制记录为转子制造质量保证的一部分 [Magnetic Innovations 2024]。

---

## 4. 工艺能力与规模化考量

| 因素 | 原型阶段影响 | 量产阶段影响 |
|------|--------------|--------------|
| 公差累积 | 通过手工修配和选择性装配解决 | 需要基于 Cpk 的工艺和自动化计量 |
| 材料利用率 | 不太关键；绝对废品成本较小 | 决定单件成本和可持续性足迹 |
| 模具交付周期 | 3D 打印或软模可接受 | 需要硬模、多腔模具和自动化产线 |
| 表面质量 / 疲劳 | 外观和短周期检查 | 需要经验证的热处理、涂层和寿命测试 |
| 供应基础 | 单一来源定制供应商 | 需要具备产能的合格 Tier-2/Tier-3 生态 |

> 🔮 **推测 / 前瞻性**：人形机器人从原型到量产的过渡可能类似电动汽车电池的扩产经验，即早期成本压力和产业成熟度强烈影响区域价值创造。欧洲和北美拥有精密制造能力，但当前高产量执行器和减速器产能集中在亚洲。因此，人形制造能力的地理分布仍是一个开放的战略问题。

---

## 5. 与其他领域的关系模式

| 来源领域 | 目标领域 | 关系 | 逻辑 |
|----------|----------|------|------|
| `03_manufacturing_processes` | `01_raw_materials` | `consumes` / `processed_by` | 工艺将原材料（铝锭、磁粉、铜线）转化为半成品或成品零件 |
| `03_manufacturing_processes` | `02_components_supply_chain` | `produces` | 制造工艺产出部件：机加工壳体、绕线定子、装配好的减速器、PCB |
| `03_manufacturing_processes` | `04_assembly_integration_testing` | `is_prerequisite_for` | 零件必须先制造和检验，才能进行组装、标定和系统测试 |
| `03_manufacturing_processes` | `05_mass_production` | `enables` / `constrains` | 工艺能力（周期、良率、Cpk）决定产能能否爬坡至千台或百万台 |
| `03_manufacturing_processes` | `06_design_engineering` | `constrains` / `is_constrained_by` | 来自制造的 DFM 反馈影响关节布局和公差；设计选择决定可行工艺 |
| `03_manufacturing_processes` | `11_applications_markets` | `drives_cost_of` | 工艺选择和良率直接影响 BOM 成本，从而影响应用经济性 |
| `03_manufacturing_processes` | `12_policy_regulation_ethics` | `is_regulated_by` | 安全标准（ISO 10218）、环保法规和洁净室要求塑造工艺与测试协议 |

---

## 6. 受控词表

### 6.1 工艺类别

- `cnc_machining`（CNC 机加工）
- `die_casting`（压铸）
- `metal_injection_molding`（金属注射成形）
- `sheet_metal_fabrication`（钣金加工）
- `additive_manufacturing`（增材制造）
- `stator_winding`（定子绕线）
- `rotor_assembly`（转子装配）
- `magnet_insertion`（磁钢插入）
- `gear_hobbing`（滚齿）
- `gear_grinding`（磨齿）
- `gear_honing`（珩磨）
- `harmonic_drive_assembly`（谐波减速器装配）
- `planetary_reducer_assembly`（行星减速器装配）
- `pcb_fabrication`（PCB 制造）
- `smt_assembly`（SMT 贴装）
- `cable_harness_assembly`（线束装配）
- `surface_treatment`（表面处理）
- `heat_treatment`（热处理）
- `conformal_coating`（三防涂覆）
- `quality_control`（质量控制）
- `metrology`（计量）
- `functional_testing`（功能测试）

### 6.2 相关实体类型

依据项目信息模型：

- `process`（工艺）
- `tool_equipment`（工具/设备）
- `facility`（设施）
- `component`（零部件）
- `standard`（标准）
- `technology`（技术）

---

## 7. 关键来源

### 7.1 主要 / 权威来源

1. **Fraunhofer IPA & P3**. *The Humanoid Hardware Value Chain: Can the European Manufacturing Industry Capitalize on the Humanoid Momentum?* (2026). 分析感知、执行、结构和能源的人形硬件价值链；指出精密制造与质量管理是欧洲的关键能力。  
   URL: https://www.ipa.fraunhofer.de/content/dam/ipa/de/documents/Publikationen/Studien/260219_Humanoid_Value_Chain_final.pdf

2. **ISO 10218-1:2011**. *Robots and robotic devices — Safety requirements for industrial robots — Part 1: Robots*. 规定机器人制造商的设计与构造安全要求。  
   URL: https://www.iso.org/standard/51330.html

3. **ISO 10218-2:2025**. *Robots and robotic devices — Safety requirements for industrial robots — Part 2: Robot systems and integration*. 涵盖安装、安全防护、风险评估和人机协作应用要求。  
   URL: https://www.iso.org/standard/85697.html

### 7.2 行业与市场分析

4. **IDTechEx**. *Humanoid Robots 2025-2035: Technologies, Markets and Opportunities* (2025). 涵盖执行器、电机、减速器、传感器、电池、高性能材料及市场预测，与制造决策相关。  
   URL: https://www.idtechex.com/en/research-report/humanoid-robots/1093

5. **Verified Market Reports**. *Robot Precision Gear Reducer Market Outlook 2025* (2025). 估计全球机器人精密减速器市场 2024 年约 12 亿美元，2033 年约 25 亿美元，人形机器人为应用细分。  
   URL: https://www.verifiedmarketreports.com/product/robot-precision-gear-reducer-market/

6. **Yijin Solution**. *Top 10 Humanoid Robot Manufacturers* (2026). 以制造为视角的分析，指出 CNC 机加工、压铸、钣金、注塑和紧固件是人形机器人的核心工艺依赖。  
   URL: https://yijinsolution.com/cnc-guides/top-humanoid-robot-manufacturers/

### 7.3 领域专项来源

7. **GROB Group**. *Machines and Systems for Electric Motor Production* (2026). 介绍电机制造中使用的定子绕线、转子磁钢插入、电机总装和浸漆工艺设备。  
   URL: https://www.grobgroup.com/en/products/product-range/winding-and-inserting-technology/

8. **Magnetic Innovations**. *New Robot Automatically Assembles Rotors of Permanent Magnet Synchronous Motors* (2024). 记录自动化磁钢处理、等离子清洗、粘接和磁场扫描等转子质量保证流程。  
   URL: https://www.magneticinnovations.com/new-robot-automatically-assembles-rotors-of-permanent-magnet-synchronous-motors/

9. **JHMIM**. *Precision MIM Gears for Humanoid Robot Joints* (2026). 关于机器人齿轮金属注射成形的技术概述，包括公差、壁厚、材料利用率和规模化声称。  
   URL: https://jhmim.com/precision-mim-gears-for-humanoid-robot-joints/

10. **PICEA MOTION**. *Harmonic Reduction Gear in Humanoid Robots and the Challenges of Manufacturing* (2025). 讨论人形谐波减速器柔轮精度、装配精度和测试要求。  
   URL: https://www.piceamotiondrive.com/harmonic-reduction-gear-in-humanoid-robots-and-the-challenges.html

11. **Honest HLS**. *Humanoid Robot Actuator Motor Stator Assembly Line Solution* (2024). 记录人形执行器定子装配流程，包括绕线、激光焊接、PCBA 焊接和热套，并配备在线监测。  
   URL: https://www.honest-hls.com/humanoid-robot-actuator-stator-line

### 7.4 行业 / 基准报道

12. **HyperSinc Intelligence**. *Germany's Fraunhofer Institute Publishes First Industrial Benchmark for Humanoid Robots* (2026). 报道 Fraunhofer IPA 工业基准，包括面向洁净室部署的 ISO 标准颗粒物排放和除气测试。  
   URL: https://hypersinc.com/article/germanys-fraunhofer-institute-publishes-first-industrial-benchmark-for-humanoid--1779109343314

### 7.5 学术 / 同行评审来源

13. **Zhang Y., Huang G., Chen X.** *Precision gear manufacturing methods for robotics: A review*. Precision Engineering, 2021;72:45-56. 综述机器人应用中的滚齿、磨齿、珩磨和精加工工艺。  
   URL: https://doi.org/10.1016/j.precisioneng.2021.04.007

14. **Oberneder F., Landler S., Otto M., Vogel-Heuser B., Zimmermann M., Stahl K.** *Influences of Different Parameters on Selected Properties of Gears for Robot-Like Systems*. Frontiers in Robotics and AI, 2024;11:1414238.  
   URL: https://doi.org/10.3389/frobt.2024.1414238

---

## 8. 开放问题

1. 对于代表性人形执行器（电机 + 减速器 + 壳体），各工艺的成本和周期分解是否有一手验证数据？
2. 哪些制造工艺当前限制了人形机器人产能爬坡——柔轮成形、电机绕线、压铸气孔控制，还是其他环节？瓶颈在地理上如何分布？
3. 本体应如何表示工艺能力（如 Cpk、公差等级、表面粗糙度）以及不同产量场景下的良率数据？
4. 汽车或消费电子制造设备在多大程度上可复用于人形机器人零件？哪些环节必须依赖定制工装？
