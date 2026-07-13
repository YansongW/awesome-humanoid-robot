---
id: ent_component_shuanghuan_shpr_20e
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 双环传动 SHPR-20E RV 减速器
  en: Shuanghuan SHPR-20E RV Reducer
sources:
- id: src_shuanghuan_official
  type: website
- title: '"双环传动官网"'
  url: http://www.shuanghuandrive.com
- id: src_shuanghuan_waic_pdf
  type: website
- title: '"环动科技 SHPR-E 高精密关节减速机产品资料"'
  url: https://www.worldrobotconference.com/uploads/exfile/video/25k3ju.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 双环传动 SHPR-20E RV 减速器 / Shuanghuan SHPR-20E RV Reducer

## 概述

SHPR-20E 是浙江双环传动子公司环动机器人关节科技推出的主轴承内置型 RV 减速器，属于 SHPR-E 系列中小规格型号。产品采用两级摆线行星传动结构，具有高刚性、抗冲击、大减速比和低背隙特点，适用于中小负载机器人关节、精密转台与协作机器人。

## 工作原理 / 技术架构

RV 减速器由第一级渐开线行星齿轮减速与第二级摆线针轮行星减速组成。输入轴带动太阳轮，行星轮在太阳轮与内齿圈之间公转并驱动偏心轴；偏心轴使摆线轮在固定针轮内做偏心运动，通过齿数差实现大减速比输出。总传动比为两级减速比之积：

$$i = i_1 \cdot i_2,\quad i_2 = \frac{Z_c}{Z_c - Z_b}$$

其中 $Z_c$ 为针轮齿数，$Z_b$ 为摆线轮齿数。SHPR-E 系列将主轴承内置于减速器本体，可直接承受外部弯矩与轴向力，结构更加紧凑。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 系列 | SHPR-E | 环动科技 |
| 型号 | SHPR-20E | 盖尔斯威/环动产品资料 |
| 减速比 | 57 / 81 / 105 / 121 / 141 / 161 : 1 | 产品资料 |
| 额定扭矩 | 未公开 | - |
| 背隙 | ≤ 1 arcmin | 产品资料 |
| 结构 | 两级摆线行星 + 内置主轴承 | 产品资料 |
| 传动效率 | 通常 85%–95%（RV 减速器范围） | 行业公开资料 |
| 重量 | 未公开 | - |
| 最高输入转速 | 未公开 | - |

## 应用场景

SCARA、协作机器人肩/肘关节、人形机器人腿部关节、焊接变位机、精密旋转台。

## 供应链关系

双环传动（`ent_company_shuanghuan`）通过环动科技制造 SHPR-E 系列 RV 减速器；已批量供应宇树科技等机器人整机厂，并与 Nabtesco、中大力德等形成国产替代竞争关系。

## 来源与验证

- 双环传动官网：http://www.shuanghuandrive.com
- 环动科技 SHPR-E 产品资料（WAIC PDF）：https://www.worldrobotconference.com/uploads/exfile/video/25k3ju.pdf