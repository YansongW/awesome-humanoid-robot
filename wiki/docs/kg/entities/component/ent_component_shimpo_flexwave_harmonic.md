---
id: ent_component_shimpo_flexwave_harmonic
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 日本新宝 FLEXWAVE 谐波减速器
  en: Nidec-Shimpo FLEXWAVE Harmonic Drive
status: active
sources:
- id: src_ent_component_shimpo_flexwave_harmonic_1
  type: website
  url: https://www.nidec.com/en/nidec-drivetechnology/product/search/category/B108/M102/S100/iNSCJ-WPU-SGH/
- id: src_ent_component_shimpo_flexwave_harmonic_2
  type: website
  url: https://moen.nidec.com/en/automation/Products/Gear-Motors-and-Gearing/Strain-Wave-Harmonic-Gear-Units
- id: src_ent_component_shimpo_flexwave_harmonic_3
  type: website
  url: https://sitspa.com/wp-content/uploads/_documents/en/Flexwave-high-precision-reducers.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 日本新宝 FLEXWAVE 谐波减速器 / Nidec-Shimpo FLEXWAVE Harmonic Drive

## 概述

日本新宝（Nidec-Shimpo）FLEXWAVE 系列属于应变波齿轮（谐波减速器）精密传动部件，由波发生器、柔轮（flexspline）和刚轮（circular spline）三大核心件构成。该系列产品以单级大减速比、近零背隙、高扭矩密度和高重复定位精度为特征，广泛应用于工业机器人关节、协作机器人、人形机器人末端关节、半导体转台、医疗机器人及精密数控机床等领域。Nidec-Shimpo 为 Nidec 集团成员，其 FLEXWAVE 产品线与 VRSF 行星减速器、Smart Flex 伺服电机模组共同构成机器人传动解决方案。

## 工作原理 / 技术架构

谐波减速器依靠波发生器迫使柔轮产生可控弹性变形，使柔轮外齿与刚轮内齿在椭圆长轴两端啮合。波发生器旋转一周，柔轮相对于刚轮沿齿差方向转过少量齿数，从而实现高减速比输出。设柔轮齿数为 $z_f$，刚轮齿数为 $z_c$，在刚性固定刚轮、波发生器为输入、柔轮为输出的常规配置下，减速比可表示为

$$
i = \frac{z_f}{z_c - z_f}
$$

典型设计中 $z_c - z_f = 2$，因此单级减速比通常可达 $30:1$ 至 $320:1$。输出扭矩与输入扭矩的关系为

$$
T_{\text{out}} = \eta \, i \, T_{\text{in}}
$$

其中 $\eta$ 为传动效率。FLEXWAVE 的柔轮采用杯型或礼帽型薄壁结构，配合交叉滚子轴承承载径向、轴向及倾覆力矩，实现零背隙传动。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 结构形式 | 波发生器 + 柔轮 + 刚轮 | 谐波减速器标准构型 |
| 外径尺寸 | 8–100 mm（系列范围） | Nidec-Shimpo 产品手册 |
| 减速比 | 30:1 – 320:1（系列范围）；WPU 系列 50:1 – 120:1 | 产品手册 / 官方选型页 |
| 额定输出扭矩 | 0.5–500 N·m（系列范围）；WPU 系列 3.7–382 N·m | 产品手册 |
| 最大输出扭矩 | WPU 系列 12–841 N·m | 官方 WPU 规格页 |
| 背隙 | ≤ 1 arcmin | 产品手册 |
| 传动效率 | ≥ 80%（典型 70–85%，视尺寸与载荷） | 产品手册 |
| 额定输入转速 | 3000 r/min | 官方 WPU 规格页 |
| 最大输入转速 | 4000–8500 r/min（视型号） | 官方 WPU 规格页 |
| 设计寿命 | 7000–10000 h | 产品手册 |
| 防护等级 | 视型号可达 IP65 | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **人形机器人**：手腕、手指、脚踝等末端关节需要高减速比、紧凑体积与零背隙的精密旋转传动。
- **协作机器人**：关节模组中作为减速与增扭核心件，配合无框力矩电机实现力控操作。
- **半导体与医疗设备**：晶圆转台、手术机器人、影像设备旋转轴，对定位精度和重复性要求极高。
- **数控机床**：五轴转台、精密分度机构，替代部分进口谐波减速器实现国产替代。

## 供应链关系

- **制造商**：日本新宝 / Nidec-Shimpo（`ent_company_shimpo`）。
- **上游关键零部件/材料**：高精度轴承、齿轮钢、润滑剂、密封件、交叉滚子轴承，Nidec 集团内部可供应伺服电机。
- **下游客户/应用场景**：工业机器人整机厂、人形机器人整机厂、半导体设备商、机床厂、医疗设备制造商。
- **竞争/对标**：Harmonic Drive Systems、Nabtesco、绿的谐波、来福谐波、中大力德等。
- **知识图谱关系**：`ent_company_shimpo` — `manufactures` → `ent_component_shimpo_flexwave_harmonic`；该产品常作为 `ent_product_humanoid_joint` 等关节模组的减速环节。

## 来源与验证

1. [Nidec-Shimpo FLEXWAVE 高扭矩 WPU 系列官方规格页](https://www.nidec.com/en/nidec-drivetechnology/product/search/category/B108/M102/S100/iNSCJ-WPU-SGH/)
2. [Nidec Automation 应变波谐波齿轮单元概述](https://moen.nidec.com/en/automation/Products/Gear-Motors-and-Gearing/Strain-Wave-Harmonic-Gear-Units)
3. [FLEXWAVE 高精度减速器产品目录 PDF](https://sitspa.com/wp-content/uploads/_documents/en/Flexwave-high-precision-reducers.pdf)
4. [附录 D 企业 Wiki：日本新宝 / Nidec-Shimpo](../../../appendices/appendix-d/companies/company_shimpo.md)