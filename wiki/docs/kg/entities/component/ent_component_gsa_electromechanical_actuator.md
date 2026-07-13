---
id: ent_component_gsa_electromechanical_actuator
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: GSA 机电执行器
  en: GSA Electromechanical Actuator
sources:
- id: src_gsa_official
  type: website
- title: GSA SA 官网
  url: https://www.gsa-sa.ch
- id: src_gsa_products
  type: website
- title: GSA Products
  url: https://www.gsa-sa.ch/en/products
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from GSA SA company profile and public product information;
    detailed EMA model-level parameters are not fully disclosed and marked as 未公开.
---


# GSA 机电执行器 / GSA Electromechanical Actuator

## 概述

GSA 机电执行器（Electromechanical Actuator, EMA）是瑞士 GSA SA 基于其行星滚柱丝杠技术开发的一体化线性执行机构。该产品将伺服电机、行星滚柱丝杠（或滚珠丝杠）、导向机构、传感器与控制器集成于一体，作为液压/气动执行器的替代方案，具有高功率密度、高定位精度、低维护及环境友好等特点，广泛应用于航空飞控、医疗手术机器人、核工业阀门及高负载机器人关节。

## 工作原理与技术架构

GSA EMA 的核心是机电转换与精密丝杠传动：

1. **旋转-直线运动转换**：伺服电机输出转矩 $T_m$，经减速或直连驱动丝杠旋转，丝杠螺母将旋转运动转换为直线推力 $F$ 与位移 $x$。
2. **行星滚柱丝杠传动**：GSA 的 EMA 常采用行星滚柱丝杠（Planetary Roller Screw, PRS），通过多个行星滚柱与丝杠、螺母同时啮合，提供高承载能力与长寿命。
3. **力/位置闭环控制**：集成编码器或 resolver 反馈电机/螺母位置，通过电流环估算输出力，实现位置、速度、力矩多模式控制。
4. **一体化设计**：电机、丝杠、轴承、壳体与传感器高度集成，可直接替代液压作动筒。

关键力学关系：

- **输出推力与输入转矩**：
  $$
  F = \frac{2 \pi \eta T_m}{P}
  $$
  其中 $P$ 为丝杠导程，$\eta$ 为传动效率。

- **直线速度与电机转速**：
  $$
  v = n \cdot P
  $$
  其中 $n$ 为丝杠转速（rev/s）。

- **行星滚柱丝杠额定动载荷**：GSA 标准系列最高可达约 1200 kN，最高转速可达 6000 rpm。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | GSA SA（瑞士洛桑）| GSA company profile |
| 传动类型 | 行星滚柱丝杠 / 滚珠丝杠 | GSA product line |
| 丝杠公称直径 | Ø8 mm – Ø150 mm（系列范围）| GSA product line |
| 导程 | 1 mm – 50 mm（系列范围）| GSA product line |
| 精度等级 | IT1 – IT5 / G1 – G5 | GSA product line |
| 行星滚柱丝杠额定动载荷 | 最高约 1200 kN | GSA product line |
| 行星滚柱丝杠最高转速 | 可达 6000 rpm | GSA product line |
| EMA 推力范围 | 未公开（依定制）| - |
| EMA 行程 | 依定制 | GSA product line |
| EMA 速度 | 未公开（依定制）| - |
| 反馈 | 编码器 / resolver 可选 | GSA product line |
| 防护等级 | 未公开 | - |
| 价格 | 未公开 | - |

注：GSA EMA 作为高度定制化产品，具体推力、速度、行程、防护等级等参数需根据客户应用定制，公开资料未给出标准型号完整参数表。

## 应用场景

- **飞机飞控作动**：舵面、襟翼、起落架的电动作动，替代传统液压系统。
- **医疗手术机器人**：高刚度、高精度的直线驱动，用于手术臂与器械定位。
- **核工业阀门**：高可靠性、免维护的远程阀门驱动。
- **人形机器人高负载关节**：作为线性或旋转关节的高力矩输出执行器。
- **机床与工业自动化**：重载直线定位与夹紧机构。

## 供应链关系

- **上游**：高端轴承钢、伺服电机、编码器/resolver、控制器、润滑脂、精密磨具、铝合金/钛合金结构件。
- **制造商**：GSA SA 通过关系 `ent_company_gsa -- manufactures --> ent_component_gsa_electromechanical_actuator` 记录于知识图谱。GSA 同时制造 `ent_component_gsa_roller_screw` 行星滚柱丝杠，构成 EMA 的核心传动部件。
- **下游**：航空航天 OEM、医疗设备厂商、机器人整机厂、核工业、机床制造商。主要竞争对手包括 Rollvis、Moog、SKF、NSK、恒立液压等。

## 来源与验证

GSA SA 的公司背景、产品线及行星滚柱丝杠参数来自企业 Wiki 与官网公开资料。EMA 具体型号参数未在公开渠道完整披露，已标注为未公开。