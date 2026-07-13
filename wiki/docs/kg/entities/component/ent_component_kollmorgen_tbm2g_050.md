---
id: ent_component_kollmorgen_tbm2g_050
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: Kollmorgen TBM2G-050 无框力矩电机
  en: Kollmorgen TBM2G-050 Frameless Torque Motor
status: active
sources:
- id: src_kollmorgen_tbm2g_selection_guide
  type: document
- title: TBM2G Frameless Motor Selection Guide
  url: https://www.kollmorgen.com/sites/default/files/TBM2G-KM_SG_00396_RevA_EN.pdf
- id: src_kollmorgen_tbm2g_product_page
  type: website
- title: Kollmorgen TBM2G Series Frameless Motors
  url: https://www.kollmorgen.com/en-us/products/motors/direct-drive/tbm2g-series-frameless
- id: src_kollmorgen_tbm2g_electromate
  type: document
- title: TBM2G Frameless Motor Selection Guide - Electromate
  url: https://www.electromate.com/media/assets/catalog-library/pdfs/kollmorgen/kollmorgen-tbm2g-selection-guide.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from Kollmorgen official selection guide and distributor
    datasheets; missing values marked as 未公开.
---


# Kollmorgen TBM2G-050 无框力矩电机 / Kollmorgen TBM2G-050 Frameless Torque Motor

## 概述

TBM2G-050 是 Kollmorgen TBM2G 系列中最小的无框力矩电机（frameless torque motor），专为 3–15 kg 负载的协作机器人与人形机器人小关节设计。其定子外径 50 mm，采用无外壳、无轴、无轴承的“三无”结构，可直接嵌入机器人关节内部，利用减速器或关节自身的轴承支撑转子，从而实现高扭矩密度、低齿槽转矩与紧凑集成。

## 工作原理 / 技术架构

TBM2G-050 为三相无刷直流（BLDC）电机，转子采用稀土永磁体（钕铁硼），定子为多极绕组。电子换向由外部伺服驱动器根据霍尔传感器或编码器反馈完成。无框设计将电磁组件与机械支撑解耦，使电机定子可直接压装到关节壳体中，借助壳体散热，提升连续扭矩输出能力。

电机的输出机械功率与电磁转矩关系为：

\[
P_m = T \cdot \omega = T \cdot \frac{2\pi n}{60}
\]

其中 \(T\) 为电磁转矩（N·m），\(n\) 为转速（rpm）。以 TBM2G-05013 为例，额定转速 8000 rpm、连续扭矩 0.38 N·m 时，额定机械功率约为：

\[
P_m = 0.38 \times \frac{2\pi \times 8000}{60} \approx 0.318 \text{ kW}
\]

公开资料给出的额定功率为 0.271 kW，差异源于具体绕组、热模型与测试条件不同。

电机常数 \(K_m\) 定义为连续转矩与绕组热损耗功率平方根之比：

\[
K_m = \frac{T_c}{\sqrt{P_{loss}}} \quad [\text{N·m}/\sqrt{\text{W}}]
\]

TBM2G-05008 的 \(K_m = 0.061\ \text{N·m}/\sqrt{\text{W}}\)，反映其将电功率转化为机械扭矩的能力。

## 关键参数

| 参数项 | TBM2G-05008 | TBM2G-05013 | TBM2G-05026 | 备注/来源 |
|--------|-------------|-------------|-------------|-----------|
| 外径（定子） | 50 mm | 50 mm | 50 mm | Kollmorgen 选型手册 |
| 内径（转子） | 24.75 mm | 24.75 mm | 24.75 mm | Kollmorgen 选型手册 |
| 叠长 | 8.2 mm | 12.7 mm | 26.3 mm | 选型手册 |
| 连续失速转矩 | 0.27 N·m | 0.38 N·m | 0.64 N·m | Kollmorgen 选型手册 |
| 额定转速 | 8000 rpm | 8000 rpm | 6600 rpm | Kollmorgen 选型手册 |
| 额定功率 | 0.205 kW | 0.271 kW | 0.363 kW | Kollmorgen 选型手册 |
| 电机常数 \(K_m\) | 0.061 N·m/√W | 0.082 N·m/√W | 0.128 N·m/√W | Kollmorgen 选型手册 |
| 额定电压 | ≤ 48 VDC | ≤ 48 VDC | ≤ 48 VDC | Kollmorgen |
| 反馈 | 可选集成霍尔传感器（050 框架部分型号不提供霍尔） | 同上 | 同上 | 选型手册 |
| 热传感器 | PT1000 / PTC（可选） | 同上 | 同上 | 选型手册 |
| 重量 | 未公开 | 未公开 | 未公开 | — |
| 价格 | 未公开 | 未公开 | 未公开 | — |

## 应用场景

- **协作机器人小臂/腕部关节**：小外径、低齿槽转矩特性适合 3–15 kg 协作机器人末端的精密运动。
- **人形机器人小关节**：可作为手指、腕部或肘部关节的内转子电机，搭配谐波减速器形成紧凑执行器。
- **精密转台与医疗机器人**：高响应、低速度纹波特性适用于光学对准、手术机器人等精密定位场景。

## 供应链关系

TBM2G-050 由 **Kollmorgen（实体 `ent_company_kollmorgen`）** 设计制造，母公司为 Regal Rexnord。上游依赖稀土永磁体、硅钢片、铜线、绝缘材料与轴承；下游主要面向协作机器人、人形机器人 OEM、航空航天与医疗设备厂商。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_kollmorgen` 相连，常与 Harmonic Drive、Nabtesco 等精密减速器组成一体化关节模组。

## 来源与验证

- Kollmorgen TBM2G 选型手册（https://www.kollmorgen.com/sites/default/files/TBM2G-KM_SG_00396_RevA_EN.pdf）
- Kollmorgen TBM2G 产品页（https://www.kollmorgen.com/en-us/products/motors/direct-drive/tbm2g-series-frameless）
- Electromate 经销商手册（https://www.electromate.com/media/assets/catalog-library/pdfs/kollmorgen/kollmorgen-tbm2g-selection-guide.pdf）

重量、单价与部分型号的霍尔配置在公开渠道未完整披露，已标注为“未公开”。