---
id: ent_component_rollvis_satellite_roller_screw
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: Rollvis 卫星滚柱丝杠
  en: Rollvis Satellite Roller Screw
sources:
- id: src_rollvis_official
  type: website
- title: '"Rollvis 官网"'
  url: https://www.rollvis.com
- id: src_rollvis_rv_page
  type: website
- title: '"Rollvis RV / HRV Planetary Roller Screws"'
  url: https://rollvis.com/rv-planetary-roller-screws/
- id: src_rollvis_korta_pdf
  type: website
- title: '"Rollvis Satellite Roller Screws Technical Documentation"'
  url: http://www.korta.com/wp-content/uploads/2021/09/ROLLVIS_ROLLED_SCREWS_ENGLISH.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# Rollvis 卫星滚柱丝杠 / Rollvis Satellite Roller Screw

## 概述

Rollvis 卫星滚柱丝杠（Satellite Roller Screw）由瑞士 Rollvis SA 研制，以螺纹滚柱作为滚动体，布置在丝杠与螺母之间，将旋转运动转换为高精度、高承载的直线运动。与传统滚珠丝杠相比，滚柱丝杠具有更多接触点、更高轴向承载能力、更长寿命与更强抗冲击性能，是人形机器人线性关节、机床进给与航空作动系统的核心传动件。

## 工作原理 / 技术架构

电机驱动丝杠旋转，螺母内的行星滚柱既绕丝杠公转又自转，滚柱螺纹与丝杠、螺母螺纹啮合实现力的传递。由于滚柱不循环（RV/HRV 型），机构可承受更高转速与加速度。导程 $p$（mm）与输入转速 $n$（rpm）决定直线速度：

$$v = \frac{p \cdot n}{60}$$

输出推力 $F$ 与电机扭矩 $T$、传动效率 $\eta$ 的关系近似为：

$$F = \frac{2\pi \eta T}{p}$$

滚柱与丝杠、螺母之间为赫兹接触，承载能力远高于同尺寸滚珠丝杠。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 公称直径范围 | Ø3.5 – Ø240 mm | 产品手册 |
| 导程范围 | 1 – 60 mm | 产品手册 |
| 精度等级 | G1 – G9（Rollvis 内部分级） | 产品手册 |
| 额定动载荷 | 最高约 1500 kN（系列范围） | 产品手册 |
| 最高转速 | 可达 5000 rpm | 产品手册 |
| 加速度 | 可达 3 g | 产品手册 |
| 传动效率 | > 90% | 产品手册 |
| 材质 | 轴承钢 / 表面硬化钢 | 产品手册 |
| 具体型号规格 | 未公开 | 需按定制型号确认 |

## 应用场景

人形机器人下肢线性关节、飞机伺服作动器、机床高负载进给轴、注塑机、医疗手术机器人、半导体精密定位平台。

## 供应链关系

Rollvis SA（`ent_company_rollvis`，2022 年被 Nidec-Shimpo 收购）制造卫星滚柱丝杠；产品供应航空航天、机床、医疗与机器人 OEM，与 GSA、SKF、NSK、THK 等形成竞争。

## 来源与验证

- Rollvis 官网：https://www.rollvis.com
- Rollvis RV/HRV 滚柱丝杠页：https://rollvis.com/rv-planetary-roller-screws/
- Rollvis 技术文档（Korta）：http://www.korta.com/wp-content/uploads/2021/09/ROLLVIS_ROLLED_SCREWS_ENGLISH.pdf