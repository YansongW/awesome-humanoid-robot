---
id: ent_component_ewellix_linear_guide
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: Ewellix 直线导轨
  en: Ewellix Linear Guide
status: active
sources:
- id: src_ewellix_llt_pdf
  type: datasheet
- title: Ewellix Profile Rail Guide LLT Specification Sheet
  url: https://www.mifp.com/wp-content/uploads/2020/10/IL-06004-1-EN-May_2020_Profile_rail_guides_LLT_2021_CN.pdf
- id: src_ewellix_official
  type: website
- title: Ewellix Official Website
  url: https://www.ewellix.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自 Ewellix 公开产品规格书；缺失值标注为“未公开”。
---


# Ewellix 直线导轨 / Ewellix Linear Guide

## 概述

Ewellix（伊维莱）直线导轨由原 SKF 线性驱动技术业务独立而来，产品包括 LLT / LLTH / LLRA 等系列，承接 SKF 制造工艺，面向医疗、工业自动化、机器人与汽车等领域。Ewellix 强调高能效、紧凑设计与智能控制，其导轨可选配 K1 长期润滑单元，实现免维护或长维护周期运行。

## 工作原理 / 技术架构

Ewellix 直线导轨基于滚动体在导轨与滑块滚道之间的滚动实现直线运动。滚动导轨的额定寿命计算遵循 ISO 14728 标准，滚珠型基本额定寿命公式为

$$
L_{10} = \left( \frac{C}{P} \right)^3 \times 100 \ \mathrm{km}
$$

其中 $C$ 为基本额定动载荷，$P$ 为当量动载荷。LLT 系列采用优化的滚道轮廓与密封设计，可在洁净室、高负载及高速应用中保持低摩擦、高刚性与长寿命。

## 关键参数表

| 参数 | 典型值 / 范围 | 备注 |
|------|--------------|------|
| 系列 | LLT / LLTH / LLRA | 产品手册 |
| 导轨宽度 | 15–65 mm | 产品手册 |
| 精度等级 | 普通 / 高 / 精密级 | 产品手册 |
| 预紧 | 普通预紧 / 轻预紧等 | 产品手册 |
| 额定动载荷 | 未公开（依型号） | 产品手册 |
| 滑块型式 | 法兰 / 四方 / 窄型 | 产品手册 |
| 材质 | 轴承钢 | 产品手册 |
| 最大速度 | 未公开 | - |
| 润滑/防护 | 可选 K1 润滑单元、双密封、表面涂层 | 产品手册 |
| 价格 | 未公开 | - |

## 应用场景

- 机床、半导体设备与自动化平台
- 人形机器人线性关节
- 医疗设备与实验室自动化
- 包装机械与食品机械
- 3C 制造与电子组装

## 供应链关系

制造商为 Ewellix（`ent_company_ewellix`），2023 年被 Triton 收购。上游关键原材料包括轴承钢、滚珠、润滑脂与密封件；下游客户包括工业自动化、医疗设备、机器人 OEM 与汽车厂商。知识图谱中的关键关系为：`ent_company_ewellix` -- `manufactures` --> `ent_component_ewellix_linear_guide`。

## 来源与验证

本卡片参数引自 Ewellix Profile Rail Guide LLT 公开产品规格书与官网。具体型号额定载荷、价格未公开。