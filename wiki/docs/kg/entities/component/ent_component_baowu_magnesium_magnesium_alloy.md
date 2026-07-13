---
id: ent_component_baowu_magnesium_magnesium_alloy
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 宝武镁业镁合金锭
  en: Baowu Magnesium Alloy Ingot
status: active
sources:
- id: src_baowu_magnesium_official
  type: website
- title: 宝武镁业官网
  url: https://www.baowumagnesium.com
- id: src_az91d_baidu_baike
  type: website
- title: 百度百科 - 镁合金 AZ91D
  url: https://baike.baidu.com/item/%E9%95%81%E5%90%88%E9%87%91AZ91D/1260875
- id: src_nadca_magnesium
  type: datasheet
- title: NADCA Magnesium Alloy Data
  url: https://cwmdiecast.com/wp-content/uploads/2021/06/2021-NADCA-Magnesium.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自宝武镁业官网、百度百科与 NADCA 数据手册；缺失值标注为“未公开”。
---


# 宝武镁业镁合金锭 / Baowu Magnesium Alloy Ingot

## 概述

宝武镁业镁合金锭是宝武镁业科技有限公司（Baowu Magnesium Technology）生产的轻量化金属材料，涵盖 AZ91D、AM60B、AE44、AS41 等牌号。宝武镁业前身为云海金属，现由中国宝武钢铁集团控股，是全球最大的镁合金生产商之一，产品广泛应用于汽车、3C、航空航天及人形机器人轻量化结构件。

## 工作原理 / 技术架构

镁合金以镁为基体，添加铝、锌、锰、稀土等元素形成合金。其密度约 1.78–1.82 g/cm³，约为铝合金的 2/3、钢的 1/4，具有优异比强度与阻尼减振性能。镁合金在弹性范围内受到冲击时吸收的能量比铝合金大，适合用作轻量化与减振结构材料。压铸成型壁厚最小可达 0.5 mm，适合复杂薄壁结构的一体化成型。

比强度 $\sigma_s$ 定义为抗拉强度 $R_m$ 与密度 $\rho$ 之比：

$$
\sigma_s = \frac{R_m}{\rho}
$$

以 AZ91D 为例，$R_m \approx 250 \ \mathrm{MPa}$，$\rho \approx 1.82 \ \mathrm{g/cm^3}$，则

$$
\sigma_s \approx \frac{250}{1.82 \times 10^{-3}} \approx 1.37 \times 10^5 \ \mathrm{Pa}/(\mathrm{kg/m^3})
$$

## 关键参数表

| 参数 | AZ91D | AM60B | 备注 |
|------|-------|-------|------|
| 牌号体系 | Mg-Al-Zn | Mg-Al-Mn | 产品手册 |
| 密度 | 1.82 g/cm³ | 1.78 g/cm³ | 产品手册 |
| 熔点 / 熔化范围 | 约 596 ℃ | 约 615 ℃ | 产品手册 |
| 抗拉强度 | 200–250 MPa | 180–230 MPa | 产品手册 |
| 屈服强度 | 150–160 MPa | 120–130 MPa | 产品手册 |
| 延伸率 | 3–7% | 8–10% | 产品手册 |
| 弹性模量 | 45 GPa | 45 GPa | 产品手册 |
| 导热系数 | 72 W/(m·K) | 62 W/(m·K) | 产品手册 |
| 硬度 | 75 BHN / 96 HV | 62 BHN / 88 HV | 产品手册 |
| 主要应用 | 结构件、外壳、骨架 | 吸能件、运动部件 | 产品手册 |
| 价格 | 未公开 | 未公开 | - |

## 应用场景

- 人形机器人关节壳体与躯干骨架
- 汽车仪表盘支架、转向柱支架与座椅骨架
- 3C 产品外壳与内部支撑结构
- 无人机结构件与航空航天轻量化部件
- 运动器材与自行车零部件

## 供应链关系

制造商为宝武镁业科技有限公司（`ent_company_baowu_magnesium`），中国宝武钢铁集团控股。上游关键原材料包括白云石、硅铁、原镁与铝合金锭；下游客户包括特斯拉、比亚迪、蔚来、小鹏、联想、戴尔及机器人整机厂。知识图谱中的关键关系为：`ent_company_baowu_magnesium` -- `manufactures` --> `ent_component_baowu_magnesium_magnesium_alloy`。

## 来源与验证

本卡片参数引自宝武镁业官网、百度百科 AZ91D 条目及 NADCA 镁合金数据手册。具体牌号价格、批量供应规格未公开。