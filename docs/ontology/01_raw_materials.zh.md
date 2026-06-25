# 01 原材料与关键资源

> **领域编码**：`01_raw_materials`  
> **价值链层**：上游（Upstream）  
> **状态**：草案 —— v0.1.0 前需复核  
> **用途**：定义流入人形机器人零部件的原材料与关键资源概念，并建立该领域与价值链其他环节的关联。

---

## 1. 核心问题

> **建造一台人形机器人需要哪些物质资源？它们来自哪里？存在哪些供应风险？**

人形机器人是材料密集型系统。量产规模下，单台机器人微小的材料需求会被放大为对矿产、金属、磁材和聚合物的大规模、集中性依赖。本领域追踪这些在变成零部件之前的上游投入。

---

## 2. 范围边界

### 2.1 在范围内

- 用于电机、电池、传感器和电子器件的关键矿产与稀土元素。
- 用于结构件和导电部件的基础金属与合金。
- 用于轻量化与摩擦学应用的高性能聚合物、复合材料和陶瓷。
- 半导体级硅、镓、锗等材料。
- 材料供应链集中度、价格波动和地缘政治风险。
- 回收、二次供应和替代路径。

### 2.2 不在范围内

- 成品零部件（见 `02_components_supply_chain`）。
- 将原材料转化为零部件的制造工艺（见 `03_manufacturing_processes`）。
- 已确认与人形机器人无相关性的普通大宗商品材料。

---

## 3. 关键概念

### 3.1 磁材稀土

人形机器人关节用高扭矩密度电机主要依赖永磁同步电机，最常用的是**钕铁硼（NdFeB）**磁体。关键元素包括：

| 元素 | 在 NdFeB 中的作用 | 对人形机器人的意义 |
|------|-------------------|-------------------|
| 钕（Nd）/ 镨（Pr） | 基体合金（常以 NdPr 形式共用） | 提供高剩磁与磁能积 |
| 镝（Dy） | 重稀土添加剂 | 提高高温下的矫顽力 |
| 铽（Tb） | 重稀土添加剂 | 在高温下进一步增强矫顽力 |

**来源与证据**：
- 国际能源署（IEA）报告指出，磁材稀土元素（Nd、Pr、Dy、Tb）自 2015 年以来需求已翻倍，并在当前政策情景下到 2030 年将再增长约三分之一，驱动力来自电气化、自动化和机器人 [IEA Rare Earth Elements 2026]。
- 钕铁硼永磁体约占稀土总消费价值的 95%，支撑电动汽车电机、风力发电机、工业机器人电机、机器人与 AI 数据中心等应用 [IEA Rare Earth Elements 2026]。
- 中国控制全球大部分稀土加工产能；2023–2025 年对 Dy、Tb 的出口管制直接加剧了高矫顽力磁材的成本与可得性风险 [TDK Rare Earth Magnets 分析；Rare Earth Exchanges 2026]。

### 3.2 电池材料

当前人形机器人主要使用源自电动汽车电池技术的锂离子电池。常见正极体系包括：

| 化学体系 | 关键元素 | 特点 |
|----------|----------|------|
| 磷酸铁锂（LFP） | 锂、铁、磷 | 安全性高，能量密度较低（电芯约 90–160 Wh/kg） |
| 三元锂（NMC / NCA） | 锂、镍、钴、锰/铝 | 能量密度较高（电芯约 200–260 Wh/kg） |
| 固态电池（新兴） | 锂、硫化物/氧化物电解质 | 潜力 >300–500 Wh/kg，安全性更好 |

**来源与证据**：
- Fraunhofer IPA 白皮书指出，当前人形机器人使用的现货锂离子电池（LFP、NMC、NCA）能量密度约 200 Wh/kg，足以满足演示需求，但不足以支撑许多工业场景；固态电池有望超过 500 Wh/kg [Fraunhofer IPA 2026]。
- 行业分析显示，Tesla Optimus Gen-2 采用 2.3 kWh 电池包，动态续航约 2 小时；Unitree H1 配备 864 Wh 电池包 [Interact Analysis 2026]。
- 美国能源部设定了无钴无镍正极材料、固态/锂金属电池的长期目标：能量密度达 500 Wh/kg，生产成本低于 60 美元/kWh [BTBU-ECOSF 报告]。

### 3.3 结构与轻量化材料

人形机器人要求高比强度、耐疲劳性和可制造性。常见材料族包括：

| 材料 | 典型应用 | 说明 |
|------|----------|------|
| 铝合金 | 框架、外壳、支架 | 重量、成本与可加工性的平衡 |
| 镁合金 | 轻量化结构件 | 密度低于铝；耐腐蚀与成本存在挑战 |
| 碳纤维复合材料 | 肢体连杆、躯干面板 | 高刚度重量比；成本和周期较高 |
| PEEK（聚醚醚酮） | 齿轮、轴承、衬套、结构支架 | 高比强度、耐磨、耐热；作为金属替代材料兴起 |
| 钢 / 钛合金 | 高负载关节、紧固件 | 强度与耐久性 |

**来源与证据**：
- IDTechEx 将高性能材料（包括 PEEK、镁合金、碳纤维复合材料、超高分子量聚乙烯）列为人形机器人硬件追踪的组件类别 [IDTechEx Humanoid Robots 2025]。
- 多份行业分析报道称 Tesla Optimus Gen-2 通过在关节和结构件中使用 PEEK 实现了约 10 kg 减重；单台人形机器人 PEEK 用量估算约为 6.6 kg [Shunhan Plastics 2026；PEEKChina 2025 引用的行业估算]。
- PEEK 轴承级牌号（如 KT820SL30）加入 PTFE/石墨固体润滑剂，用于干摩擦关节；碳纤维填充 PEEK 据称在重量约为铝一半的情况下可达到接近航天铝的结构性能 [Shunhan Plastics 2026]。

### 3.4 半导体与传感器材料

- **硅（Si）**：计算芯片、图像传感器、MEMS。
- **镓（Ga）/ 锗（Ge）**：功率电子、光电子、高频器件。
- **铜（Cu）**：电机绕组、线束、母排。
- **铂族金属 / 特种合金**：力/力矩传感器应变元件、高可靠性触点。

---

## 4. 供应风险类别

| 风险类型 | 说明 | 示例 |
|----------|------|------|
| 地理集中度 | 采矿或加工集中在单一地区 | 中国约占全球稀土磁材制造和重稀土加工的 90% |
| 伴生依赖 | 某元素作为另一元素的副产品生产 | 镝、铽与离子型稀土矿开采伴生 |
| 价格波动 | 价格剧烈波动影响 BOM 成本 | Nd、Dy、Tb 在出口管制期间价格飙升 |
| 替代困难 | 技术上可替代材料有限 | 紧凑高扭矩电机对 NdFeB 的依赖 |
| 监管限制 | 出口管制或制裁 | 中国 2024–2025 年稀土/磁材出口许可制度 |

---

## 5. 与其他领域的关系模式

| 来源领域 | 目标领域 | 关系 | 逻辑 |
|----------|----------|------|------|
| `01_raw_materials` | `02_components_supply_chain` | `supplies` / `consumed_by` | 稀土磁材 → 伺服电机；锂 → 电池包；铝/PEEK → 结构件 |
| `01_raw_materials` | `03_manufacturing_processes` | `processed_by` | 矿石 → 分离氧化物 → 磁粉；铸锭 → CNC 加工件 |
| `01_raw_materials` | `05_mass_production` | `constrains` | 材料可得性与成本决定产能爬坡可行性 |
| `01_raw_materials` | `06_design_engineering` | `constrains` / `enables` | 材料密度与强度影响形态；磁材磁能积限制电机尺寸 |
| `01_raw_materials` | `11_applications_markets` | `drives_cost_of` | 材料成本影响终端价格与应用经济性 |
| `01_raw_materials` | `12_policy_regulation_ethics` | `is_regulated_by` | 出口管制、冲突矿产规则、关键矿产战略 |

---

## 6. 受控词表

### 6.1 材料类别

- `rare_earth_element`（稀土元素）
- `permanent_magnet_material`（永磁材料）
- `battery_cathode_material`（电池正极材料）
- `battery_anode_material`（电池负极材料）
- `electrolyte_material`（电解质材料）
- `lightweight_metal`（轻量化金属）
- `structural_polymer`（结构聚合物）
- `fiber_reinforced_composite`（纤维增强复合材料）
- `semiconductor_material`（半导体材料）
- `conductive_metal`（导电金属）

### 6.2 相关实体类型

依据项目信息模型：

- `material`（材料）
- `component`（零部件，用于讨论中间加工形态）
- `market_segment`（市场细分）
- `policy`（政策）

---

## 7. 关键来源

### 7.1 主要 / 权威来源

1. **International Energy Agency (IEA)**. *Rare Earth Elements* (2026). 执行摘要指出磁材稀土需求自 2015 年翻倍，NdFeB 磁体约占稀土消费价值的 95%。  
   URL: https://www.iea.org/reports/rare-earth-elements/executive-summary

2. **Fraunhofer IPA**. *The Humanoid Hardware Value Chain* (2026). 评估触觉传感器、电机、减速器、电池；指出锂电约 200 Wh/kg，固态电池潜力 >500 Wh/kg。  
   URL: https://www.ipa.fraunhofer.de/content/dam/ipa/de/documents/Publikationen/Studien/260219_Humanoid_Value_Chain_final.pdf

3. **IDTechEx**. *Humanoid Robots 2025-2035: Technologies, Markets and Opportunities* (2025). 涵盖执行器、电机、减速器、传感器、电池、高性能材料及市场预测。  
   URL: https://www.idtechex.com/en/research-report/humanoid-robots/1093

### 7.2 行业与市场分析

4. **Interact Analysis**. *Humanoid Robots and Lithium-Ion Batteries* (2026). 对比 Optimus 与 Unitree H1 电池配置；讨论三元材料主导地位和固态电池试点。  
   URL: https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/

5. **Research and Markets / Embodied AI and Humanoid Robot Market Research 2024-2025**. 供应链与零部件展望，包括执行器、传感器、电池、材料。  
   URL: https://www.researchandmarkets.com/reports/6078204/embodied-ai-humanoid-robot-market-research

### 7.3 材料专项来源

6. **Shunhan Plastics**. *PI vs. PEEK in Humanoid Robots* (2026). PEEK 性能、牌号（KT820SL30、KT820CF30）及在人形机器人试验中报告的减重/提速效果。  
   URL: https://www.shunhanplastics.com/blogs/article/pi-vs-peek-in-humanoid-robots-which-high-performance-plastic-powers-the-future-of-robotics

7. **PEEKChina**. *Why PEEK is the Key Material for Tesla's Humanoid Robot Optimus-Gen2?* (2025). 行业估算单台人形机器人 PEEK 用量约 6.6 kg。  
   URL: https://www.peekchina.com/blog/key-material-for-humanoid-robots-peek-polymer.html

8. **Rare Earth Exchanges / e-VAC**. *America's Rare Earth Magnet Industry Reawakening* (2026). 讨论美国进口依赖与全球磁材需求预测。  
   URL: https://rareearthexchanges.com/news/e-vac-goes-live-americas-rare-earth-magnet-industry-reawakening/

---

## 8. 开放问题

1. 代表机型（如 Tesla Optimus、Unitree H1、Figure 02）的 BOM 材料质量分解是否有一手来源验证？
2. 材料需求如何随产量规模变化，需要怎样的回收基础设施来闭环？
3. 哪些稀土减量或替代策略（如铁氧体辅助设计、同步磁阻电机、SmCo 替代）对人形执行器可行？
4. 本体应如何表示材料牌号差异（如 N35 vs N52 NdFeB、6061 vs 7075 铝合金）及其性能权衡？
