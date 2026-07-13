---
id: ent_component_zhongda_40zde_10
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 中大力德 40ZDE-10 精密行星减速器
  en: Zhongda 40ZDE-10 Precision Planetary Gearbox
sources:
- id: src_zhongda_official
  type: website
- title: '"中大力德官网"'
  url: https://www.zd-drivers.com
- id: src_zhongda_pdf
  type: website
- title: '"ZDE/ZDF 系列高精度行星减速机手册"'
  url: https://zd-drivers.com.ar/pdf/planetary-gearbox_pdf01.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 中大力德 40ZDE-10 精密行星减速器 / Zhongda 40ZDE-10 Precision Planetary Gearbox

## 概述

40ZDE-10 是宁波中大力德智能传动股份有限公司 ZDE 系列单级精密行星减速器，机座号 40，减速比 10:1。产品结构紧凑、传动效率高、成本低，适用于小负载机器人关节、AGV 轮毂、协作机器人腕部与 3C 自动化模组。

## 工作原理 / 技术架构

行星减速器由太阳轮、行星轮、内齿圈与行星架组成。输入端驱动太阳轮，行星轮同时与太阳轮和内齿圈啮合，并通过行星架输出。单级减速比为：

$$i = 1 + \frac{Z_{\text{ring}}}{Z_{\text{sun}}}$$

40ZDE-10 为单级 10:1，回程间隙控制在 12 arcmin 以内，满载效率约 96%。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 机座号 | 40 | 中大力德手册 |
| 减速比 | 10:1（单级） | 中大力德手册 |
| 输出扭矩 | 4–6 N·m | 五矿证券研报引用中大力德官网 |
| 回程间隙 | < 12 arcmin | 中大力德手册 |
| 满载效率 | 96% | 中大力德手册 |
| 重量 | 0.4 kg | 中大力德手册 |
| 箱体长度 | 39 mm | 中大力德手册 |
| 防护等级 | IP54 | 中大力德手册 |
| 设计寿命 | 20,000 h | 中大力德手册 |
| 输入转速 | 最高 6000 rpm | 产品手册 |

## 应用场景

AGV 轮毂、协作机器人关节、人形机器人手指/腕部、3C 自动化、小型 SCARA。

## 供应链关系

中大力德（`ent_company_zhongda`）制造 40ZDE-10 行星减速器，并为宇树科技、智元机器人等供应传动部件；与双环传动、绿的谐波、Nabtesco 等在中高端减速器市场形成竞争。

## 来源与验证

- 中大力德官网：https://www.zd-drivers.com
- ZDE/ZDF 系列手册：https://zd-drivers.com.ar/pdf/planetary-gearbox_pdf01.pdf