---
id: ent_component_electronic_expansion_valve
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 电子膨胀阀
  en: Electronic Expansion Valve (EEV)
status: active
sources:
- id: src_ent_component_electronic_expansion_valve_sanhua
  type: document
  url: https://cdn.sanhuaeurope.co.uk/new_content/static/uploads/files/catalogue/standard-catalogue-2022-june-pdf-1655212497.pdf
- id: src_ent_component_electronic_expansion_valve_article
  type: website
  url: http://mp.weixin.qq.com/s?__biz=MzkyODg5NzYxOQ==&mid=2247484944&idx=1&sn=ed41201f294696097cf8eec50e21b003
- id: src_ent_component_electronic_expansion_valve_driver
  type: document
  url: https://www.alfaco.cz/sanhua/sanhua-katalog-standard-2015.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 电子膨胀阀 / Electronic Expansion Valve (EEV)

## 概述

电子膨胀阀（Electronic Expansion Valve，EEV）是一种由步进电机驱动的电调制节流装置，广泛应用于制冷、空调、热泵及新能源汽车热管理系统。它通过调节阀针开度，精确控制进入蒸发器的制冷剂流量，使蒸发器出口过热度保持在目标值，从而提升系统能效与控温精度。与传统热力膨胀阀（TXV）相比，EEV 响应更快、调节范围更宽，且可与整车/整机控制器进行数字协同。

## 工作原理与技术架构

EEV 由阀体、阀针、阀座、步进电机及驱动线圈组成。控制器根据蒸发器出口温度与压力计算实际过热度：

$$
\Delta T_{\text{SH}} = T_{\text{out}} - T_{\text{sat}}(P_{\text{evap}})
$$

其中 $T_{\text{out}}$ 为蒸发器出口温度，$T_{\text{sat}}$ 为对应蒸发压力下的饱和温度。控制器将该过热度与目标值比较，输出脉冲序列驱动步进电机改变阀针开度。

制冷剂质量流量可近似表示为：

$$
\dot{m} = C_d A(x) \sqrt{2\rho(P_{\text{in}} - P_{\text{out}})}
$$

其中 $C_d$ 为流量系数，$A(x)$ 为与开度 $x$ 相关的流通面积，$\rho$ 为制冷剂密度，$P_{\text{in}}$、$P_{\text{out}}$ 为阀前后压力。多数 EEV 采用等百分比（equal-percentage）流量特性，即单位行程变化引起的相对流量变化恒定，便于 PID 控制整定。

典型驱动采用 1-2 相单极性励磁，全行程由 500 或 2000 个脉冲完成；脉冲频率 30–90 pps 时，全行程时间约 6 s。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 驱动方式 | 步进电机 | 1-2 相单极性励磁（典型） |
| 额定电压 | 12 V DC ±10% | 线圈驱动 |
| 励磁脉冲频率 | 30–90 pps | 公开规格 |
| 全行程时间 | 约 6 s @ 90 pps | 依型号 |
| 线圈电流 | 260 mA/相（20 ℃） | 典型值 |
| 线圈电阻 | 46 ± 3.7 Ω/相（20 ℃） | 典型值 |
| 绝缘等级 | E 级 | — |
| 防护等级 | IP67（阀体/线圈） | 部分型号 |
| 工作温度 | -30 ℃ ~ +55 ℃ | 控制器/阀体 |
| 相对湿度 | ≤90% RH | 无凝露 |
| 适用制冷剂 | R22、R134a、R407C、R404A、R410A 等 | 依密封材料 |
| 流量特性 | 等百分比 | 公开资料 |
| 额定容量 / Kv | 未公开 | 型号相关 |
| 控制器供电 | 24 Vac/Vdc（VSD2010 系列） | 0–10 V / 4–20 mA 输入 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **家用与商用空调**：变频多联机、精密空调、数据中心温控。
- **热泵系统**：空气源热泵、电动汽车热泵空调。
- **新能源汽车热管理**：电池热管理、电机/电控冷却回路的电子节流。
- **机器人与电子设备热管理**：人形机器人或高性能计算平台的液冷/相变冷却系统。

## 供应链关系

- **制造商**：三花智控（Sanhua）、丹佛斯（Danfoss）等制冷控制部件供应商。
- **上游关键物料**：铜材、不锈钢阀体、O 型圈/密封件、步进电机、磁材、线圈。
- **下游集成**：空调/OEM、热泵整机厂、新能源汽车热管理系统集成商、机器人热管理方案商。
- **知识图谱关系**：
  - `ent_company_sanhua` / `ent_company_danfoss` — `manufactures` → `ent_component_electronic_expansion_valve`
  - `ent_component_electronic_expansion_valve` — `used_in` → 空调/热泵/热管理系统产品节点

## 来源与验证

- Sanhua 2022 标准样本中公布了 EEV 线圈电气参数（12 V DC、1-2 相励磁、30–90 pps、260 mA、46 Ω、E 级绝缘、IP67）及等百分比流量特性。
- 行业技术文章《电子膨胀阀应用和设计布局》阐述了过热度控制、流量特性、结构与电气参数选型逻辑。
- 具体阀体的额定容量、Kv 值及全系列尺寸未在公开资料中完整披露，表中标记为“未公开/型号相关”。