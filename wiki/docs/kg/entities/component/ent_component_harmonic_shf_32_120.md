---
id: ent_component_harmonic_shf_32_120
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: Harmonic Drive SHF-32-120 谐波减速器
  en: Harmonic Drive SHF-32-120 Harmonic Drive
sources:
- id: src_harmonic_official
  type: website
- title: '"Harmonic Drive Systems 官网"'
  url: https://www.harmonicdrive.net
- id: src_harmonic_product
  type: website
- title: '"SHF-32-120-2UH-LW 产品页"'
  url: https://global.harmonicdrive.net/products/gear-units/hollow-shaft-gear-units/shf-2uh-lw/shf-32-120-2uh-lw
- id: src_tradebearings_shf
  type: website
- title: '"SHF-32-120-2SH 技术规格"'
  url: https://en.tradebearings.com/SHF_32_120_2SH-1508697.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# Harmonic Drive SHF-32-120 谐波减速器 / Harmonic Drive SHF-32-120 Harmonic Drive

## 概述

SHF-32-120 是日本 Harmonic Drive Systems 推出的中空型谐波减速器，减速比 120:1。产品采用 S 齿形柔轮与刚轮啮合，配合交叉滚子轴承输出法兰，具有零背隙、高扭矩密度、大中空孔径与高定位精度，广泛用于协作机器人、人形机器人腰/髋部与医疗机器人关节。

## 工作原理 / 技术架构

谐波减速器由波发生器、柔轮（Flexspline）与刚轮（Circular Spline）组成。波发生器使柔轮产生可控弹性变形，柔轮齿与刚轮齿逐齿啮合实现减速。减速比为：

$$i = \frac{Z_{\text{flex}}}{Z_{\text{circ}} - Z_{\text{flex}}}$$

对于 SHF-32-120，$i = 120:1$。柔轮与刚轮齿数差通常为 2。大中空结构允许电缆、气管从中穿过，简化机器人关节布线。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 系列/型号 | SHF-32-120 | Harmonic Drive |
| 减速比 | 120:1 | 产品规格 |
| 外径 | 约 147 mm | Amazon/经销商资料 |
| 厚度 | 约 65.5 mm | Amazon/经销商资料 |
| 重量 | 约 1.665 kg（整件）/ 3.1 kg（含轴承单元） | 经销商资料 |
| 额定扭矩 L10 | 137 N·m | SHF-32-120-2SH 规格 |
| 平均扭矩限值 | 216 N·m | SHF-32-120-2SH 规格 |
| 反复峰值扭矩 | 353 N·m | SHF-32-120-2SH 规格 |
| 瞬间最大扭矩 | 686 N·m | SHF-32-120-2SH 规格 |
| 平均输入转速 | 3500 rpm | SHF-32-120-2SH 规格 |
| 标准精度 | 1 arcmin | SHF-32-120-2SH 规格 |
| 扭转刚度 K1/K2/K3 | 67 000 / 110 000 / 120 000 N·m/rad | SHF-32-120-2SH 规格 |
| 容许力矩负载 Mc | 580 N·m | SHF-32-120-2SH 规格 |
| 背隙 | 接近零 | 谐波减速器特性 |

## 应用场景

协作机器人肩部/肘部、人形机器人腰/髋部、医疗机器人、半导体转台、精密定位平台。

## 供应链关系

Harmonic Drive Systems（`ent_company_harmonic_drive`）是谐波减速器发明者与全球领导者；下游客户包括工业机器人、协作机器人与人形机器人 OEM，与绿的谐波、来福谐波、Nabtesco 等竞争。

## 来源与验证

- Harmonic Drive 官网：https://www.harmonicdrive.net
- SHF-32-120-2UH-LW 产品页：https://global.harmonicdrive.net/products/gear-units/hollow-shaft-gear-units/shf-2uh-lw/shf-32-120-2uh-lw
- SHF-32-120-2SH 规格：https://en.tradebearings.com/SHF_32_120_2SH-1508697.html