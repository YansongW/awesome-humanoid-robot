---
id: ent_component_nabtesco_rv_40e_105
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: Nabtesco RV-40E-105 RV 减速器
  en: Nabtesco RV-40E-105 Precision RV Reducer
status: active
sources:
- id: src_nabtesco_rv_catalog
  type: document
- title: Nabtesco RV Series Full Catalog
  url: https://s3.amazonaws.com/www.motionusa.com/nabtesco/RV_Series_Full_Catalog.pdf
- id: src_nabtesco_rv_catalog_de
  type: document
- title: Precision Reduction Gear RV Catalog
  url: https://www.nabtesco.de/fileadmin/04_Service/05_Downloads/01_Produktkataloge/RV_Katalog_EN.pdf
- id: src_nabtesco_company_wiki
  type: document
- title: 附录 D 企业 Wiki - Nabtesco
  url: docs/appendices/appendix-d/companies/company_nabtesco.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications extracted from Nabtesco official RV catalog and company
    Wiki; exact weight and dimensions should be verified with latest datasheet.
---


# Nabtesco RV-40E-105 RV 减速器 / Nabtesco RV-40E-105 Precision RV Reducer

## 概述

RV-40E-105 是日本 Nabtesco（纳博特斯克）RV-E 系列精密减速器的代表型号之一，广泛应用于工业机器人重载关节、人形机器人腰/髋部以及重载变位机。它采用摆线针轮与行星齿轮复合传动结构，具有高刚性、高扭矩、抗冲击与长寿命的特点，是六轴工业机器人 J1–J3 关节的标准选择之一。

## 工作原理 / 技术架构

RV 减速器由第一级行星齿轮减速与第二级摆线针轮减速串联组成：

1. **第一级**：输入轴驱动中心轮，带动多个行星轮绕中心轮公转，实现初步减速。
2. **第二级**：行星轮通过偏心轴驱动摆线轮（cycloidal disc），摆线轮与针齿壳上的针齿啮合，产生低速大扭矩输出。

总减速比 \(i\) 为第一级减速比 \(i_1\) 与第二级减速比 \(i_2\) 的乘积：

\[
i = i_1 \cdot i_2
\]

对于 RV-40E-105，\(i = 105:1\)。输出转速 \(n_{out}\) 与输入转速 \(n_{in}\) 的关系为：

\[
n_{out} = \frac{n_{in}}{i}
\]

在额定输入转速下，输出转速约为输入转速的 1/105。输出扭矩 \(T_{out}\) 与输入扭矩 \(T_{in}\) 满足：

\[
T_{out} = T_{in} \cdot i \cdot \eta
\]

其中 \(\eta\) 为传动效率，RV-E 系列通常在 85%–95% 之间。

RV 减速器内置主轴承，可直接承受外部径向、轴向与倾覆力矩，无需额外支撑结构。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 系列 | RV-E 系列 | Nabtesco 产品目录 |
| 型号 | RV-40E-105 | 产品编号 |
| 减速比 | 105:1 | Nabtesco 产品页 |
| 外径 | 约 105 mm | Nabtesco RV-E 手册 |
| 重量 | 9.3 kg | 行业研报 / Nabtesco 参数表 |
| 额定扭矩 | 412 N·m | Nabtesco 产品页 |
| 启动停止容许扭矩 | 1,029 N·m | Nabtesco 产品页 |
| 瞬时最大扭矩 | 2,058 N·m | Nabtesco 产品页 |
| 容许输出转速 | 70 rpm（100% 占空比） | Nabtesco 产品页 |
| 背隙 | < 1 arc-min | Nabtesco 产品页 |
| 额定寿命 | 6,000 h | Nabtesco 产品页 |
| 传动效率 | 约 85%–95% | 产品手册 |
| 主轴承 | 内置角接触球轴承 | 产品手册 |
| 润滑 | 专用润滑脂 | 产品手册 |
| 安装方式 | 法兰输出 / 组件型 | 产品手册 |
| 价格 | 未公开 | — |

## 应用场景

- **六轴工业机器人 J1–J3 关节**：承担基座、大臂、肩部等重载位置的高扭矩、高刚性减速。
- **人形机器人腰/髋部**：为躯干与下肢大关节提供抗冲击与高刚性的旋转驱动。
- **重载变位机与机床转台**：利用内置主轴承直接支撑外部负载，简化机械设计。

## 供应链关系

RV-40E-105 由 **Nabtesco Corporation 子公司 Nabtesco Motion（实体 `ent_company_nabtesco`）** 制造。上游依赖合金钢、摆线轮、针齿壳、轴承与润滑脂；下游客户包括工业机器人四大家族、国产机器人厂商与人形机器人 OEM。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_nabtesco` 相连，常与 Kollmorgen、Wolong 等大扭矩电机及五洲新春、NSK 等轴承配套组成重载机器人关节。

## 来源与验证

- Nabtesco RV Series Full Catalog（https://s3.amazonaws.com/www.motionusa.com/nabtesco/RV_Series_Full_Catalog.pdf）
- Nabtesco Precision Reduction Gear RV Catalog（https://www.nabtesco.de/fileadmin/04_Service/05_Downloads/01_Produktkataloge/RV_Katalog_EN.pdf）
- 附录 D 企业 Wiki《Nabtesco》（docs/appendices/appendix-d/companies/company_nabtesco.md）

价格与部分型号的精确尺寸在公开渠道未完整披露，已标注为“未公开”。