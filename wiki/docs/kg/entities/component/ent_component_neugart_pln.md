---
id: ent_component_neugart_pln
schema_version: 1
type: component
'title:': Neugart PLN 高精度行星减速器
domain: 02_components
theoretical_depth: system
names:
  zh: Neugart PLN 高精度行星减速器
  en: Neugart PLN Precision Planetary Gearbox
status: active
sources:
- id: src_neugart_neugart_pln_official
  type: website
  url: https://www.neugart.com/en/gearboxes/precision-gearboxes/pln
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Neugart PLN 高精度行星减速器 / Neugart PLN Precision Planetary Gearbox

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [纽卡特 / Neugart](../../../appendices/appendix-d/companies/company_neugart.md) |
| **产品类别** | 高精度行星减速器 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [纽卡特 官网](https://www.neugart.com) |

## 产品概述

PLN 是 Neugart 标准高精度行星减速器，采用直齿高刚性设计和预紧圆锥滚子轴承，提供 1 级和 2 级传动。系列尺寸从 PLN 070 到 PLN 190，减速比 3–100，1 级额定扭矩 14–800 N·m，2 级可达 43–2,880 N·m。

PLN 具有 IP65 防护、终身润滑、PCS-2 快速电机适配和长中心定位 collar，定位精度可达到 <1 arcmin（选项），是机床、机器人和半导体设备的高性价比精密传动选择。

## 产品图片

> Neugart PLN 高精度行星减速器 / Neugart PLN Precision Planetary Gearbox：请访问 [官方资料](https://www.neugart.com/en/gearboxes/precision-gearboxes/pln) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 减速比 | 3:1 – 100:1 | 产品手册 |
| 框号尺寸 | PLN 070 / 090 / 115 / 142 / 190 | 产品手册 |
| 额定输出扭矩 | 14 – 800 N·m（1 级）；43 – 2,880 N·m（2 级） | 产品手册 |
| 背隙 | 标准 <3 arcmin；可选 <1 arcmin | 产品手册 |
| 效率 | 最高约 98% | 产品手册 |
| 防护等级 | IP65 | 产品手册 |
| 最大输入转速 | 最高 8,000 rpm（依尺寸） | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[纽卡特 / Neugart](../../../appendices/appendix-d/companies/company_neugart.md)
- **核心零部件/技术来源**：直齿行星齿轮、预紧轴承、密封件、润滑脂、电机适配法兰
- **下游应用/客户**：数控机床、工业机器人、人形机器人、半导体与医疗设备

## 知识图谱节点与关系

- 零部件实体：`ent_component_neugart_pln`
- 制造商实体：`ent_company_neugart`
- 关键关系：
  - `rel_ent_company_neugart_manufactures_ent_component_neugart_pln`（`ent_company_neugart` --> `manufactures` --> `ent_component_neugart_pln`）

## 应用场景

- **工业机器人**：机器人腕部、肩部、转台
- **人形机器人**：手臂、腿部关节精密减速
- **数控机床**：机床进给、刀库、第四/五轴转台
- **其他自动化**：包装、印刷、医疗定位平台

## 竞争对比

| 对比项 | PLN 行星减速器 | Wittenstein SP+ | Apex Dynamics AB |
|--------|------------------------|---------------|---------------|
| 核心优势 | 高精度、终身润滑、PCS-2 | 螺旋齿、恒定背隙 | 台湾高性价比、 helical |
| 背隙/精度 | <1–3 arcmin | ≤1–3 arcmin | ≤1–5 arcmin |
| 价格水平 | 高端 | 高端 | 中高端 |
| 交付周期 | 中等 | 中等 | 较短 |

## 选购与部署建议

高定位精度场景优先选降低背隙选项；注意 PLN 为直齿，若对噪音敏感可考虑 PLE 或 helical 竞品。

## 参考资料

1. [纽卡特 官网](https://www.neugart.com)
2. [Neugart PLN Precision Planetary Gearbox](https://www.neugart.com/en/gearboxes/precision-gearboxes/pln)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)