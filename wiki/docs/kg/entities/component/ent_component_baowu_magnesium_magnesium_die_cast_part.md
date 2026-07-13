---
id: ent_component_baowu_magnesium_magnesium_die_cast_part
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 宝武镁业镁合金压铸结构件
  en: Baowu Magnesium Die-Cast Structural Part
sources:
- id: src_baowu_magnesium_official
  type: website
- title: 宝武镁业官网
  url: https://www.baowumagnesium.com
- id: src_magnesium_die_cast_alloy_data
  type: website
- title: NADCA Magnesium Die Casting Alloys Material Properties
  url: https://cwmdiecast.com/wp-content/uploads/2021/06/2021-NADCA-Magnesium.pdf
- id: src_magnesium_alloy_properties
  type: website
- title: Magnesium Die Casting Alloy Data
  url: https://www.soldy.com/wp-content/uploads/2020/03/nadca-alloy-data.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from official company materials and industry standard
    alloy datasheets; exact part-level properties depend on mold design and post-processing.
---


# 宝武镁业镁合金压铸结构件 / Baowu Magnesium Die-Cast Structural Part

## 概述

宝武镁业镁合金压铸结构件（Baowu Magnesium Die-Cast Structural Part）是由宝武镁业科技股份有限公司（Baowu Magnesium）采用高压压铸工艺生产的轻量化金属结构件。该产品以 AZ91D、AM60B 等镁合金为原料，通过高压压铸与 CNC 精加工成型，具有密度低、比强度高、电磁屏蔽性能好、阻尼减振等特性，广泛应用于人形机器人躯干/腿部骨架、汽车座椅骨架、转向柱支架、3C 外壳及无人机结构件。

## 工作原理 / 技术架构

镁合金压铸结构件的生产涉及材料、模具与高压充型工艺的协同：

1. **合金熔炼与保护**：镁合金熔点约 470–643 °C，熔炼过程中需使用 SF₆/CO₂ 或 SO₂ 等保护气体防止氧化燃烧。
2. **高压压铸**：在冷室或热室压铸机中，将熔融镁液以高速（>6 m/s）高压射入精密模具型腔，快速凝固形成复杂薄壁结构。
3. **CNC 精加工**：对压铸件进行去毛刺、钻孔、攻丝与尺寸精修，满足机器人关节壳体、躯干骨架的装配精度。
4. **表面处理**：通过微弧氧化（MAO）、涂装或钝化提升耐蚀性与外观质量。

压铸件的比强度（强度/密度）是衡量其轻量化优势的关键指标。以 AZ91D 为例，其抗拉强度约 230 MPa，密度约 1.81 g/cm³，比强度约为钢的 2 倍以上：

$$
\frac{\sigma_b}{\rho} \approx \frac{230 \text{ MPa}}{1.81 \text{ g/cm}^3} \approx 127 \text{ MPa·cm}^3\!/\text{g}
$$

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 宝武镁业 / Baowu Magnesium | 公司官网 |
| 常用材质 | AZ91D / AM60B | 产品手册 |
| 制造工艺 | 高压压铸 + CNC 精加工 | 产品手册 |
| 尺寸范围 | 依模具定制 | 产品手册 |
| 壁厚 | 0.8–5 mm | 产品手册 |
| 尺寸精度 | CT4–CT6 | 产品手册 |
| 密度（AZ91D） | 1.81 g/cm³ | NADCA 合金数据 |
| 抗拉强度（AZ91D） | 230 MPa | NADCA 合金数据 |
| 屈服强度（AZ91D） | 155 MPa | NADCA 合金数据 |
| 延伸率（AZ91D） | 3% | NADCA 合金数据 |
| 硬度（AZ91D） | 75 BHN | NADCA 合金数据 |
| 抗拉强度（AM60B） | 220 MPa | NADCA 合金数据 |
| 屈服强度（AM60B） | 140 MPa | NADCA 合金数据 |
| 延伸率（AM60B） | 6–8% | NADCA 合金数据 |
| 弹性模量 | 45 GPa | NADCA 合金数据 |
| 热膨胀系数 | 25.0–26.1 μm/m·K | NADCA 合金数据 |
| 表面处理 | 微弧氧化 / 涂装 / 钝化 | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **人形机器人轻量化结构件**：用于关节壳体、躯干骨架、腿部支架，较铝合金减重 30–40%。
- **汽车座椅骨架与转向柱支架**：利用镁合金高比强度与优良压铸性能，实现汽车零部件轻量化。
- **3C 产品外壳**：笔记本电脑、相机壳体等消费电子产品的薄壁结构件。
- **无人机结构件**：借助低密度与高刚性，提升无人机续航与载荷能力。

## 供应链关系

宝武镁业（`ent_company_baowu_magnesium`）是全球最大的镁合金生产商之一，由中国宝武钢铁集团控股，拥有从白云石开采、原镁冶炼到镁合金深加工的完整产业链。镁合金压铸结构件（`ent_component_baowu_magnesium_magnesium_die_cast_part`）是公司面向机器人、汽车、3C 等领域的重要产品线。上游包括白云石、硅铁、原镁、铝合金锭、压铸机与模具钢；下游客户包括特斯拉、比亚迪、蔚来、小鹏、联想、戴尔及机器人整机厂。在知识图谱中，宝武镁业同时制造镁合金材料（`ent_component_baowu_magnesium_alloy`）与镁合金压铸结构件。其主要竞争对手包括万丰奥威、瑞鹄模具、文灶股份等。

## 来源与验证

- 宝武镁业官网与年报确认其镁合金压铸件业务及下游应用布局。
- NADCA（北美压铸协会）发布的镁合金压铸材料性能手册提供了 AZ91D、AM60B 等合金的标准力学性能数据。
- 行业研报与 WAIC 参展报道补充了镁合金在人形机器人结构件中的应用趋势，但未公开宝武镁业具体客户份额。