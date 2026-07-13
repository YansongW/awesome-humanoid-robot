---
id: ent_component_baowu_magnesium_die_cast_part
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 宝武镁业镁合金压铸结构件
  en: Baowu Magnesium Die-cast Structural Part
status: active
sources:
- id: src_baowu_official
  type: website
  url: https://www.baowumagnesium.com/
- id: src_baowu_investor
  type: website
  url: https://www.baowumagnesium.com/investor/
- id: src_asm_mg
  type: white_paper
  url: https://www.asminternational.org/search?
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 宝武镁业镁合金压铸结构件

## 概述

宝武镁业镁合金压铸结构件由中国宝武钢铁集团控股的宝武镁业科技股份有限公司（深交所：002182）生产。该产品以镁合金锭（AZ91D、AM60B 等牌号）为原料，经高压压铸（HPDC）与 CNC 精加工制成，广泛应用于人形机器人轻量化结构件、新能源汽车零部件及 3C 外壳。镁合金密度仅为铝合金的约 2/3、钢的约 1/4，兼具高比强度、优良阻尼减振与电磁屏蔽性能。

## 工作原理 / 技术架构

高压压铸工艺将熔融镁合金在高压下快速充填入金属模具型腔，经保压、冷却定型后获得近净成形结构件。后续通过 CNC 精加工保证尺寸精度与装配接口。

材料性能上，镁合金压铸件的比强度可表示为：

$$
\sigma_{\text{specific}} = \frac{\sigma_{\text{ tensile}}}{\rho}
$$

其中 $\sigma_{\text{tensile}}$ 为抗拉强度，$\rho$ 为材料密度。以 AZ91D 为例，$\rho \approx 1.81 \ \text{g/cm}^3$，$\sigma_{\text{tensile}} \approx 240 \ \text{MPa}$，其比强度显著高于普通钢材。相比铝合金结构件，镁合金压铸件可实现 **30–40%** 的减重。

典型力学性能范围（AZ/AM 系列压铸件）：

$$
\rho = 1.78\text{–}1.82 \ \text{g/cm}^3, \quad \sigma_{\text{tensile}} = 200\text{–}280 \ \text{MPa}, \quad \sigma_{\text{yield}} = 120\text{–}160 \ \text{MPa}
$$

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 制造商 | 宝武镁业科技股份有限公司 |
| 材质牌号 | AZ91D / AM60B / AE44 / AS41 等 |
| 密度 | 1.78–1.82 g/cm³ |
| 抗拉强度 | 200–280 MPa |
| 屈服强度 | 120–160 MPa |
| 延伸率 | 3–15% |
| 弹性模量 | 约 45 GPa |
| 工作温度 | −40 °C – +150 °C |
| 制造工艺 | 高压压铸 + CNC 精加工 |
| 壁厚范围 | 0.8–5 mm |
| 尺寸精度 | CT4–CT6 |
| 表面处理 | 微弧氧化 / 涂装 / 钝化 |
| 价格 | 未公开 |

## 应用场景

- **人形机器人**：关节壳体、躯干骨架、腿部支架、手部结构件等轻量化零件。
- **新能源汽车**：座椅骨架、仪表盘支架、转向柱支架、电池包端板。
- **消费电子**：笔记本电脑外壳、相机机身、无人机骨架。
- **航空航天**：直升机变速箱壳体、导弹结构件、卫星支架。

## 供应链关系

在公司—产品—零部件网络中，镁合金压铸结构件处于**轻量化结构材料/零部件层**：

- **上游**：白云石、原镁、硅铁、铝合金元素、压铸机、模具钢、CNC 加工服务。
- **自身位置**：`ent_company_baowu_magnesium -- manufactures --> ent_component_baowu_magnesium_die_cast_part`。
- **下游**：人形机器人整机厂、汽车 OEM、3C 品牌商、航空航天制造商。

## 来源与验证

- 宝武镁业官网：https://www.baowumagnesium.com/
- 宝武镁业投资者关系：https://www.baowumagnesium.com/investor/
- 镁合金力学性能参考 ASM Handbook 及公开产品手册

牌号、密度、强度范围与压铸工艺参数来自宝武镁业产品手册与行业材料标准；具体零件报价与定制尺寸需以厂商询价为准。