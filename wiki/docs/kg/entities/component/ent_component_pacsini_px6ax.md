---
id: ent_component_pacsini_px6ax
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 帕西尼 PX-6AX 多维触觉传感器
  en: Pacsini PX-6AX Multidimensional Tactile Sensor
status: active
sources:
- id: src_paxini_px6ax_gen3
  type: website
  url: https://paxini.com/robot/ax/gen3
- id: src_paxini_ces2026
  type: website
  url: https://www.prnewswire.com/apac/news-releases/paxini-unveils-the-tactile-infrastructure-for-embodied-ai-redefining-full-stack-product-matrix-at-ces-2026-302655239.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 帕西尼 PX-6AX 多维触觉传感器 / Pacsini PX-6AX Multidimensional Tactile Sensor

## 概述

PX-6AX 是帕西尼感知科技（Pacsini Technology）推出的第三代集成式多维触觉传感单元，基于霍尔阵列式（Hall-array）触觉感知技术，能够同时输出三维力、三维力矩以及接触位置、材质、温度、硬度、回弹等多维物理信息。该产品是帕西尼“传感器—灵巧手—人形机器人”全栈产品矩阵中的核心感知部件，已集成于 DexH13 多维触觉灵巧手与 TORA-ONE 人形机器人。

## 工作原理 / 技术架构

PX-6AX 采用第三代自研 ITPU（Intelligent Tactile Processing Unit）芯片与霍尔效应传感阵列：

- **多维力/力矩测量**：通过检测弹性体在接触力作用下的磁场分布变化，解算接触点处的三轴力 \(F_x, F_y, F_z\) 与三轴力矩 \(T_x, T_y, T_z\)。
- **高密度阵列**：单个传感单元内最多可提供 717 路阵列力信号，实现 0.1 mm 级空间分辨率。
- **快速采样**：内部采样率高达 1 MHz，最大输出频率 1000 Hz，可捕捉瞬态接触事件。
- **温度与材质感知**：集成温度补偿与材质/硬度推断算法，支持 15 种物理信息解读。
- **高可靠封装**：工业级寿命超过 1000 万次按压，防护等级达 IP68，可在复杂工业环境中长期使用。

传感器的最小可识别力为 0.01 N，重复性优于 0.5% FS，安全过载 200%，冲击过载 300%。

## 关键参数表

| 参数项 | PX-6AX GEN3（典型值） |
|---|---|
| 传感维度 | 6D（三维力 + 三维力矩） |
| 输出信号 | 三轴力阵列、三轴合力、三轴合力矩 |
| 阵列力信号数 | 最多 717 路 |
| 法向力测量范围 | 0–25 N |
| 切向力测量范围 | ±10 N |
| 最小可识别力 | 0.01 N |
| 空间分辨率 | 0.1 mm |
| 内部采样率 | 1 MHz |
| 最大输出频率 | 1000 Hz |
| 重复性 | <0.5% FS |
| 安全过载 | 200% |
| 冲击过载 | 300% |
| 使用寿命 | >1000 万次连续按压 |
| 防护等级 | IP68 |
| 工作温度 | 0–50 °C |
| 工作电压 | 3–5 V |
| 型号规格示例 | 18 mm × 13 mm × 10 mm（指尖型） |

## 应用场景

- **灵巧手指尖**：为 DexH13 等五指灵巧手提供全手指尖环绕式触觉感知。
- **机器人电子皮肤**：覆盖机械臂、手掌等大面积区域，实现接触力分布与滑移检测。
- **精密装配与分拣**：检测接触状态与物体硬度，辅助装配、插拔与易碎品抓取。
- **医疗假肢与智能穿戴**：提供接近人类皮肤的力/温度感知能力。

## 供应链关系

- **上游**：霍尔传感器芯片、柔性基材、磁敏材料、ASIC 信号处理芯片、封装材料。
- **制造商**：帕西尼感知科技（Pacsini Technology）自主研发与生产。
- **下游**：人形机器人 OEM、灵巧手厂商、工业机器人集成商、医疗康复设备厂商。
- **图谱位置**：`ent_company_pacsini` → `manufactures` → `ent_component_pacsini_px6ax`；并通过 `used_in` 关系集成至 `ent_product_pacsini_dexh13` 与 `ent_product_pacsini_tora_one`。

## 来源与验证

- PX-6AX GEN3 详细参数来自帕西尼官方产品页（paxini.com/robot/ax/gen3）。
- CES 2026 新闻稿对 15 维感知、1000 万次寿命与 <0.5% FS 重复性进行了公开报道。
- 附录 D 企业 Wiki 提供了公司与产品矩阵的供应链关系。