---
id: ent_component_lithium_battery
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 锂离子电池
  en: Lithium-ion Battery
status: active
sources:
- id: src_panasonic_ncr18650b
  type: website
  url: https://www.dnkpower.com/ncr18650b/
- id: src_panasonic_cell
  type: website
  url: https://makerselectronics.com/product/panasonic-ncr18650b-3-6v-15a-3350mah/
- id: src_battery_university
  type: website
  url: https://batteryuniversity.com/article/bu-205-types-of-lithium-ion
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 锂离子电池 / Lithium-ion Battery

## 概述

锂离子电池是一类以锂离子在正负极之间嵌入/脱嵌实现充放电的可充电电池，具有能量密度高、自放电低、无记忆效应等特点。本词条以 Panasonic NCR18650B 圆柱形 NCA 电芯为例，给出机器人电池组设计中常用的关键参数。

## 工作原理 / 技术架构

电池由正极（LiNiCoAlO₂）、石墨负极、隔膜与电解液组成。放电时锂离子从负极经电解液迁移至正极，电子经外电路做功；充电过程相反。电芯储存的能量与质量/体积能量密度为：
\[
E=C \cdot V_{\text{nom}},
\]
\[
\rho_e=\frac{E}{m}\quad\text{或}\quad\rho_v=\frac{E}{V},
\]
其中 \(C\) 为容量（Ah），\(V_{\text{nom}}\) 为标称电压，\(m\) 为质量，\(V\) 为体积。

## 关键参数表

| 规格项 | 数值（以 Panasonic NCR18650B 为例） | 备注/来源 |
|--------|-------------------------------------|-----------|
| 化学体系 | 锂离子（NCA） | DNK Power |
| 标称电压 | 3.6 V | DNK Power |
| 额定容量 | 3200 mAh；典型 3350 mAh | DNK Power |
| 充电电压 | 4.20 ± 0.03 V | DNK Power |
| 放电截止电压 | 2.5 V | DNK Power |
| 最大持续放电电流 | 4.875 A | DNK Power |
| 能量密度 | 676 Wh/L（体积）/ 243 Wh/kg | DNK Power |
| 内阻 | ≤100 mΩ | DNK Power |
| 尺寸 | Φ18.25 mm × 65.10 mm | DNK Power |
| 重量 | ≤47.5 g | DNK Power |
| 循环寿命 | 约 1000 次 | 行业资料 |
| 工作温度 | 充电 0–40 °C；放电 -20–60 °C | DNK Power |

## 应用场景

- 人形机器人躯干/背包电池组
- 移动机器人与无人车动力电源
- 电动工具与便携设备
- 储能系统

## 供应链关系

锂离子电池由松下、宁德时代、三星 SDI、LG 新能源等电芯厂生产，经电池模组/PACK 厂集成 BMS 后供应给机器人整机厂。在知识图谱中，`ent_component_lithium_battery` 作为能源子系统的基础部件，被多种移动机器人产品通过 `uses` 关系引用。

## 来源与验证

- [Panasonic NCR18650B Datasheet (DNK Power)](https://www.dnkpower.com/ncr18650b/)
- [Panasonic NCR18650B Specifications](https://makerselectronics.com/product/panasonic-ncr18650b-3-6v-15a-3350mah/)
- [Battery University - Lithium-ion Overview](https://batteryuniversity.com/article/bu-205-types-of-lithium-ion)