---
$id: ent_application_industrial_manufacturing
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: application_scenario
names:
  en: Industrial Manufacturing
  zh: 工业制造
  ko: 산업 제조
summary:
  en: The application of humanoid robots to tasks such as assembly, machine tending, inspection, and material handling in
    factories.
  zh: 将人形机器人应用于工厂中的装配、上下料、检测与物料搬运等任务。
  ko: 휴로봇을 공장의 조립·기계 관리·검사·자재 취급 등에 적용하는 분야.
domains:
- 11_applications_markets
layers:
- validation_markets
functional_roles:
- knowledge
tags:
- application
- chapter_27
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-06.md#6.8 供应链与主要厂商 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
工业制造是人形机器人领域的重要application_scenario。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
人形机器人计算、电源与热管理子系统的供应链高度全球化，同时受到半导体制造、电池材料和热界面材料等上游环节制约。

!!! note "术语解释：供应链、ODM、OEM、IDM、Fabless、Foundry"
    - **供应链（supply chain）**：从原材料到最终产品的所有环节和企业网络。
    - **ODM（Original Design Manufacturer）**：原始设计制造商，负责设计和制造，品牌方贴牌销售。
    - **OEM（Original Equipment Manufacturer）**：原始设备制造商，通常指代工厂或品牌整机厂。
    - **IDM（Integrated Device Manufacturer）**：同时从事芯片设计、制造和封测的垂直整合企业。
    - **Fabless**：无晶圆厂设计公司，只设计芯片，委托 Foundry 制造。
    - **Foundry**：晶圆代工厂，如台积电、三星、Intel Foundry。

**计算平台厂商**：NVIDIA（Jetson 系列、Thor）、Intel（NUC、Xeon）、Qualcomm（RB 系列、QCS 系列）、AMD（Kria FPGA、Ryzen Embedded）、Apple（M 系列）、NXP（i.MX、S32）、Renesas、Horizon Robotics、Rockchip、Allwinner 等。

**电源与电池厂商**：CATL、BYD、LG Energy Solution、Samsung SDI、Panasonic、EVE Energy、欣旺达、亿纬锂能、德州仪器（TI）、ADI、Infineon、ON Semiconductor、MPS、STMicroelectronics 等提供 BMS、功率半导体和电源管理 IC。

**热管理厂商**：Aavid（Boyd）、Delta、Nidec、Fujikura、双鸿、超众、奇鋐等提供散热器、热管、均热板、风扇和液冷方案；Shin-Etsu、Dow、Henkel、信越等提供 TIM 材料。

**制造瓶颈**。先进制程（7 nm 及以下）晶圆代工、HBM 高带宽内存、高端功率半导体（SiC/GaN）是当前机器人与自动驾驶计算平台的关键瓶颈。地缘政治和出口管制进一步增加了供应链不确定性。

**国产替代进展**。中国大陆在计算芯片、功率半导体和电池领域已形成完整产业链：华为昇腾、地平线征程、寒武纪思元、瑞芯微 RK 系列提供从端侧到边缘的 AI 算力；比亚迪、宁德时代在全球动力电池市场占据重要份额；士兰微、华润微、斯达半导、时代电气等在 IGBT 和 SiC 模块领域持续突破。国产替代的成熟度直接影响人形机器人成本可控性和供应链韧性。

!!! note "术语解释：国产替代、IGBT、SiC、GaN、HBM、晶圆代工"
    - **国产替代（domestic substitution）**：用本国或本地供应链产品替代进口产品的过程。
    - **IGBT（Insulated Gate Bipolar Transistor）**：绝缘栅双极型晶体管，中高压功率开关器件。
    - **SiC（Silicon Carbide）**：碳化硅，宽禁带半导体，适合高频高温功率应用。
    - **GaN（Gallium Nitride）**：氮化镓，另一种宽禁带半导体，适合高频高效电源。
    - **HBM（High Bandwidth Memory）**：高带宽存储器，通过 3D 堆叠实现高带宽。
    - **晶圆代工（wafer foundry）**：提供晶圆制造服务的半导体工厂。

**成本结构**。以一台高端人形机器人为例，计算平台（SoM + 载板 + 散热）可能占总 BOM 成本的 10%–20%；电池组占 15%–25%；电机与驱动占 30%–40%；结构件、传感器、线束和组装占其余部分。随着量产规模扩大和芯片集成度提高，计算与电源子系统的成本占比有望下降。

**整机计算架构案例**。当前主流人形机器人厂商多采用“中央大脑 + 分布式小脑”架构：

- **Tesla Optimus**：采用自研 FSD 芯片作为感知与决策主控，躯干和关节通过自定义通信总线连接，强调视觉主导的端到端控制。
- **Boston Dynamics Atlas**：使用嵌入式实时计算机处理状态估计与步态控制，液压/电动执行器由专用驱动板闭环控制，强调高动态运动的确定性。
- **Agility Digit / Figure 02**：采用 NVIDIA Jetson 或类似平台处理多相机感知与导航，下层通过 EtherCAT 或类似总线连接关节驱动器。
- **优必选 Walker / 智元远征 A2 / 傅利叶 GR-1**：多采用 NVIDIA Jetson AGX Orin / Xavier 或国产替代平台作为上位机，结合 ARM MCU/FPGA 做关节实时控制。

这些案例共同表明：人形机器人计算架构正在从早期的 PC/工控机 + 运动控制卡，向高度集成的嵌入式 SoC + 实时总线 + 云端协同演进。

## 参考
- Wiki extraction
- 项目 Wiki：chapter-06.md#6.8 供应链与主要厂商

