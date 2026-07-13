---
id: ent_component_harmonic_csf_32_50
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: Harmonic Drive CSF-32-50-2A-GR 谐波减速器
  en: Harmonic Drive CSF-32-50-2A-GR Harmonic Drive
status: active
sources:
- id: src_harmonic_csf32_electromate
  type: website
- title: CSF-32-50-2A-GR Harmonic Drive - Electromate
  url: https://www.electromate.com/csf-32-50-2a-gr/
- id: src_harmonic_drive_csg_page
  type: website
- title: Harmonic Drive CSG-32-50-2A-GR Product Page
  url: https://www.harmonicdrive.net/products/component-sets/cup-type/csg-2a/csg-32-50-2a-gr
- id: src_harmonic_drive_catalog
  type: document
- title: Harmonic Drive Gears Catalog
  url: https://harmonicdrive.de/fileadmin/Downloads/Produkte/Kataloge/Harmonic_Drive_Gears_EN_1053522.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from Harmonic Drive distributor and official catalog;
    CSF/CSG-32-50 share similar kinematics and dimensions, exact dynamic ratings should
    be confirmed with official datasheet.
---


# Harmonic Drive CSF-32-50-2A-GR 谐波减速器 / Harmonic Drive CSF-32-50-2A-GR Harmonic Drive

## 概述

CSF-32-50-2A-GR 是日本 Harmonic Drive Systems 推出的杯型（cup-type）组件式谐波减速器。它由波发生器、柔性齿轮（柔轮）与刚性齿轮（刚轮）三个同轴基本构件组成，具有单级大减速比、零背隙、高扭矩密度与紧凑外形的特点，广泛应用于工业机器人腕部、协作机器人关节与人形机器人小臂/腕部。

## 工作原理 / 技术架构

谐波减速器基于弹性变形啮合原理。波发生器（通常内置椭圆凸轮与柔性轴承）装入薄壁柔轮内孔后，使柔轮产生可控椭圆变形；柔轮长轴处齿与刚轮齿啮合，短轴处脱离。波发生器连续旋转时，柔轮相对刚轮产生“错齿”运动，实现减速输出。

单级减速比 \(i\) 由刚轮齿数 \(z_c\) 与柔轮齿数 \(z_f\) 决定：

\[
i = \frac{z_c}{z_c - z_f}
\]

对于 CSF-32-50-2A-GR，\(i = 50:1\)，即刚轮比柔轮多 2 齿（典型设计），代入得 \(z_c - z_f = 2\)，因此 \(z_c = 100\)、\(z_f = 98\)。

输出转速 \(n_{out}\) 与输入转速 \(n_{in}\) 的关系为：

\[
n_{out} = \frac{n_{in}}{i}
\]

在额定输入转速 2000 rpm 时，输出转速约为 40 rpm。输出扭矩 \(T_{out}\) 与输入扭矩 \(T_{in}\) 在忽略效率损失时满足：

\[
T_{out} = T_{in} \cdot i \cdot \eta
\]

其中 \(\eta\) 为传动效率，谐波减速器通常在 80%–90% 之间。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 系列/类型 | CSF 组件型（cup-type component set） | Electromate |
| 规格号 | 32 | Electromate |
| 减速比 | 50:1 | Electromate / 产品编号 |
| 最大外径 | 110 mm | Electromate |
| 长度 | 44 mm | Electromate |
| 重量 | 0.89 kg | Electromate |
| 最大连续扭矩 | 76 N·m | Electromate |
| 最高输入转速 | 7,000 rpm | Electromate |
| 背隙 | ≤ 1 arc-min | 行业公开资料 |
| 安装方式 | 法兰输出 / 组件型 | Electromate |
| 输出轴承 | 需外部支撑（组件型） | 产品手册 |
| 润滑 | 专用谐波润滑脂 | 产品手册 |
| 效率 | 约 80%–90% | 产品手册 |
| 额定寿命 | 依负载与速度，L10 寿命需按工况计算 | 产品手册 |
| 价格 | 未公开 | — |

## 应用场景

- **工业机器人腕部**：六轴机器人 J4–J6 关节利用谐波减速器实现高精度、小体积减速。
- **协作机器人与人形机器人关节**：与人形机器人小臂、腕部、手指关节的紧凑执行器集成。
- **半导体转台与光学平台**：零背隙与高重复定位精度适合晶圆转台、激光扫描系统。

## 供应链关系

CSF-32-50-2A-GR 由 **Harmonic Drive Systems Inc.（实体 `ent_company_harmonic_drive`）** 制造。上游依赖合金钢（柔轮/刚轮）、交叉滚子轴承、润滑脂与铝壳；下游客户包括工业机器人、人形机器人、半导体设备与医疗机器人 OEM。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_harmonic_drive` 相连，常与 Kollmorgen、Maxon 等无框电机及五洲新春、NSK 等轴承配套形成一体化旋转关节。

## 来源与验证

- Electromate CSF-32-50-2A-GR 产品页（https://www.electromate.com/csf-32-50-2a-gr/）
- Harmonic Drive 官网 CSG-32-50-2A-GR 产品页（https://www.harmonicdrive.net/products/component-sets/cup-type/csg-2a/csg-32-50-2a-gr）
- Harmonic Drive 产品目录（https://harmonicdrive.de/fileadmin/Downloads/Produkte/Kataloge/Harmonic_Drive_Gears_EN_1053522.pdf）

价格与部分寿命参数在公开渠道未完整披露，已标注为“未公开”。