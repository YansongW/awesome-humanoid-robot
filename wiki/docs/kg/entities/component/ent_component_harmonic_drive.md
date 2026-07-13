---
id: ent_component_harmonic_drive
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 谐波减速器
  en: Harmonic Drive
status: active
sources:
- id: src_ent_component_harmonic_drive_official
  type: website
  url: https://www.harmonicdrive.net
- id: src_ent_component_harmonic_drive_electromate
  type: website
  url: https://www.electromate.com/csf-32-50-2a-gr/
- id: src_ent_component_harmonic_drive_tradebearings
  type: website
  url: https://en.tradebearings.com/CSF_32_100_2UH-1508123.html
- id: src_ent_component_harmonic_drive_wiki
  type: website
  url: docs/appendices/appendix-d/companies/company_harmonic_drive.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 谐波减速器 / Harmonic Drive

## 概述

谐波减速器（Harmonic Drive）是一种基于柔性齿轮弹性变形原理的精密减速装置，由波发生器（Wave Generator）、柔性齿轮（Flexspline）和刚性内齿圈（Circular Spline）组成。其核心优势为零背隙、高减速比、高扭矩密度和高定位精度，广泛应用于工业机器人、协作机器人、人形机器人关节、数控机床转台、半导体设备及医疗机器人。

## 工作原理与技术架构

波发生器为椭圆形凸轮，外圈装有薄壁轴承；其旋转使柔性齿轮发生周期性椭圆变形。柔性齿轮外齿与刚性内齿圈啮合，由于两者齿数相差通常 2 齿，柔性齿轮每转一周，相对刚轮只转过 2 个齿距，从而实现大减速比。

减速比可表示为：

$$
i = \frac{N_f}{N_c - N_f}
$$

其中 $N_c$ 为刚轮齿数，$N_f$ 为柔轮齿数。以 CSF-32-100-2UH 为例，$i=100:1$。

输出转矩与输入转矩的关系为：

$$
T_{\text{out}} = i \cdot T_{\text{in}} \cdot \eta
$$

其中 $\eta$ 为传动效率，谐波减速器典型效率约为 80%–90%。扭转刚度通常用分段线性模型描述：在 $T_1$ 以内为 $K_1$，$T_1$–$T_2$ 之间为 $K_2$，大于 $T_2$ 为 $K_3$。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 代表型号 | CSF-32-100-2UH | Harmonic Drive Systems |
| 规格尺寸 | Size 32 | 外径约 110 mm |
| 减速比 | 30:1 – 160:1（系列范围） | 本表取 100:1 |
| 额定扭矩 L10 | 137 N·m | CSF-32-100-2UH |
| 平均扭矩限值 | 216 N·m | — |
| 反复峰值扭矩 | 333 N·m | — |
| 瞬时峰值扭矩 | 647 N·m | — |
| 最高输入转速 | 3500 rpm | — |
| 标准精度 | ≤1 arcmin | — |
| 背隙 | 接近零 | 谐波传动特性 |
| 扭转刚度 K1/K2/K3 | 67,000 / 110,000 / 120,000 N·m/rad | — |
| 允许弯矩负载 | 313 N·m | — |
| 径向动态承载 | 15,000 N | — |
| 重量 | 3.2 kg | CSF-32-100-2UH |
| 润滑 | 专用润滑脂 | — |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **工业机器人**：六轴机器人腕部、小臂关节的高精度减速。
- **协作机器人与人形机器人**：肩部、肘部、髋部、腕部关节的力矩放大与精密定位。
- **数控机床**：第四/五轴转台、分度头。
- **半导体与医疗**：晶圆转台、手术机器人关节。

## 供应链关系

- **主要制造商**：Harmonic Drive Systems（日本）、绿的谐波（Leaderdrive，中国）、来福谐波（Laifu，中国）等。
- **上游关键物料**：合金钢（柔轮/刚轮）、交叉滚子轴承、专用润滑脂、铝壳。
- **下游集成**：工业机器人 OEM、人形机器人整机厂、数控机床厂、半导体设备商、医疗机器人厂商。
- **知识图谱关系**：
  - `ent_company_harmonic_drive` — `manufactures` → `ent_component_harmonic_drive`
  - `ent_product_estun_robot` — `uses` → `ent_component_harmonic_drive`

## 来源与验证

- Harmonic Drive Systems 官网为品牌与产品系列来源。
- Electromate 产品页给出 CSF-32-50-2A-GR 的尺寸、重量（0.89 kg）、减速比 50:1、最大连续扭矩 76 N·m、最高输入转速 7000 rpm、精度 <1 arcmin。
- Tradebearings 技术规格页给出 CSF-32-100-2UH 的额定扭矩 137 N·m、反复峰值扭矩 333 N·m、瞬时峰值扭矩 647 N·m、扭转刚度、允许弯矩及重量 3.2 kg。
- 附录 D Wiki 确认了谐波减速器在机器人关节中的供应链位置。