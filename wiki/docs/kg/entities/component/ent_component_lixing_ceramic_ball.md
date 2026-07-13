---
id: ent_component_lixing_ceramic_ball
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 力星氮化硅陶瓷球
  en: Lixing Silicon Nitride Ceramic Ball
sources:
- id: src_lixing_company_official
  type: website
- title: 力星股份官网
  url: https://www.lxballs.com
- id: src_lixing_ceramic_ball_datasheet
  type: website
- title: 精密陶瓷球产品特性（威酸传动）
  url: https://www.wjbmotion.com/proimages/pro/ceramic-ball/ceramic-ball.pdf
- id: src_ceramic_ball_grade_reference
  type: website
- title: Si3N4 陶瓷球等级与性能参考
  url: https://www.51sourcing.com/post/750.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from official company profile, product manuals and
    ceramic ball industry references; missing values marked as 未公开.
---


# 力星氮化硅陶瓷球 / Lixing Silicon Nitride Ceramic Ball

## 概述

力星氮化硅陶瓷球（Lixing Silicon Nitride Ceramic Ball）是江苏力星通用钢球股份有限公司（力星股份）生产的高性能精密滚动体，以氮化硅（Si₃N₄）为基体材料，通过等静压成型与气压烧结工艺制备。相较于传统轴承钢球，氮化硅陶瓷球具有密度低、硬度高、耐高温、耐腐蚀、低热膨胀与无磁性等特性，广泛应用于高速主轴、航空航天轴承、精密仪器以及高端机器人关节轴承。

## 工作原理 / 技术架构

氮化硅陶瓷球作为滚动轴承的核心滚动体，其工作性能由材料力学与接触力学共同决定：

1. **轻量化离心力控制**：陶瓷密度约 3.2 g/cm³，仅为轴承钢（7.8 g/cm³）的 40% 左右。在高速旋转时，球体离心力

$$
F_c = m \omega^2 r = \rho V \omega^2 r
$$

显著低于钢球，从而降低对外圈的离心载荷，允许更高的 dn 值（轴承内径 mm × 转速 rpm）。

2. **高硬度与耐磨性**：氮化硅显微硬度可达 1,500–1,700 HV（约 HRC 75–80），显著高于轴承钢，耐磨寿命更长。

3. **低摩擦与自润滑**：陶瓷表面化学稳定性高，可在贫油或特殊润滑介质下工作，且不易发生粘着磨损。

4. **热稳定性**：热膨胀系数约为钢的 25%，在高温环境下可保持较好的尺寸稳定性与配合精度。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 力星股份 / Lixing | 公司官网 |
| 材料 | 氮化硅 Si₃N₄ | 产品手册 |
| 直径范围 | Ø1.588–Ø25.4 mm（力星公开范围） | 产品手册 |
| 精度等级 | G5 / G10 / G16 | 产品手册 |
| 密度 | 3.2 g/cm³ | 产品手册 |
| 硬度 | 1,500–1,700 HV（约 HRC 75–80） | 产品手册 / 行业资料 |
| 弹性模量 | 310 GPa | 产品手册 |
| 球直径公差（G5） | ±0.13 μm | 行业标准 |
| 球形误差（G5） | 0.13 μm | 行业标准 |
| 表面粗糙度 Ra（G5） | ≤0.014 μm | 行业标准 |
| 批直径变动量（G5） | 0.25 μm | 行业标准 |
| 工作温度 | 长期 ≤800 °C，短时可达 1,000 °C | 行业资料 |
| 热膨胀系数 | 约 3.2 × 10⁻⁶ /°C | 行业资料 |
| 耐腐蚀性 | 耐多数酸碱，除氢氟酸与磷酸外 | 行业资料 |
| 磁性 | 无磁性 | 材料特性 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **人形机器人关节轴承**：作为谐波减速器、RV 减速器与机器人关节轴承的滚动体，降低高速运动时的离心载荷与摩擦热。
- **高速电主轴**：在 CNC 主轴、半导体设备主轴中实现高转速、高精度、长寿命运转。
- **航空航天轴承**：用于航空发动机、飞行控制系统的轴承组件，满足高温、高可靠性需求。
- **精密仪器与医疗器械**：利用其无磁性、耐腐蚀特性，应用于核磁共振设备、精密测量仪器。

## 供应链关系

力星股份（`ent_company_lixing`）是国内最大的专业化精密轴承钢球与陶瓷球制造商之一，其产品通过 SKF、Schaeffler、NSK 等国际轴承巨头以及国内主流轴承厂进入终端市场。氮化硅陶瓷球（`ent_component_lixing_ceramic_ball`）位于机器人供应链上游，上游原材料包括轴承钢丝/氮化硅粉体、磨削液、热处理炉等；下游客户包括机器人轴承厂、谐波减速器厂商与人形机器人整机 OEM。力星股份与山东东阿钢球、江苏钢锐精密、日本椿中岛、东芝材料等形成竞争关系。

## 来源与验证

- 力星股份公司官网与年报确认其为国内领先的精密钢球与陶瓷球供应商，产品覆盖 Ø0.5–Ø50.8 mm 钢球及陶瓷球。
- 力星产品手册提供了氮化硅陶瓷球的密度、硬度、弹性模量、精度等级等参数。
- 陶瓷球行业通用标准（GB/T 308、ISO 3290）补充了 G5/G10/G16 等级的公差与表面质量参数。