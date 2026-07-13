---
id: ent_component_eve_lf280k_cell
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 亿纬锂能 LF280K 磷酸铁锂电芯
  en: EVE Energy LF280K LiFePO4 Prismatic Cell
status: active
sources:
- id: src_eve_lf280k_datasheet
  type: pdf
- title: EVE LF280K Specification Sheet
  url: https://akkudoktor.net/uploads/short-url/jEC8pfYYVepQ4z81Qz6rOgbA2BJ.pdf
- id: src_eve_batteryusa
  type: website
- title: EVE Energy North America Product Specifications
  url: https://www.evebatteryusa.com/copy-of-18650-and-21700-specifications
- id: src_eve_dnkpower
  type: website
- title: DNK Power – EVE LF280K Cell Specification
  url: https://www.dnkpower.com/eve-lf280k-3-2v-280ah-prismatic-lifepo4-battery-cell/
- id: src_eve_imr
  type: website
- title: IMR Batteries – EVE LF280K Specifications
  url: https://imrbatteries.com/products/eve-lf280k-280ah-3-2v-lifepo4-prismatic-battery-grade-a-1
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheet and verified distributor listings;
    missing values marked as 未公开.
---


# 亿纬锂能 LF280K 磷酸铁锂电芯 / EVE Energy LF280K LiFePO4 Prismatic Cell

## 概述

LF280K 是亿纬锂能（EVE Energy）量产的大容量方形磷酸铁锂（LiFePO₄/LFP）电芯，标称容量 280 Ah、标称电压 3.2 V，主要面向储能系统、商用车底盘及长续航移动平台。该电芯以高循环寿命、高安全性与较低内阻为特点，也可作为人形机器人底盘电池包或备用电源的高可靠性单元。

## 工作原理 / 技术架构

磷酸铁锂电芯以 LiFePO₄ 为正极、石墨为负极，通过锂离子在正负极之间的嵌入/脱嵌实现充放电。其能量由平均工作电压 $V_{\text{avg}}$ 与容量 $Q$ 决定：

$$
E = V_{\text{avg}} \cdot Q
$$

以质量 $m$ 计算的质量能量密度为

$$
\rho_E = \frac{E}{m}
$$

LF280K 标称能量约 896 Wh，重量约 5.42 kg，对应质量能量密度约 165 Wh/kg（公开资料估算值）。

充放电倍率常用 C 表示，1C 对应 280 A 电流；标准充放电电流为 0.5C（140 A），最大连续充放电电流为 1C，脉冲（30 s）可达 2C。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 化学体系 | 磷酸铁锂（LiFePO₄） | EVE 官方 datasheet |
| 标称容量 | 280 Ah | EVE 官方 datasheet |
| 标称电压 | 3.2 V | EVE 官方 datasheet |
| 标称能量 | 896 Wh | EVE 官方 datasheet |
| 尺寸 | 约 173.7 × 71.5/72.0 × 207.2/207.5 mm | 多家经销商 / EVE datasheet |
| 重量 | 5.42 ± 0.3 kg | EVE 官方 datasheet |
| 质量能量密度 | 约 165 Wh/kg | 公开资料估算 |
| 充电截止电压 | 3.65 V | EVE 官方 datasheet |
| 放电截止电压 | 2.5 V（>0 °C） | EVE 官方 datasheet |
| 标准充/放电电流 | 0.5C（140 A） | EVE 官方 datasheet |
| 最大连续充/放电电流 | 1C（280 A） | EVE 官方 datasheet |
| 脉冲充/放电电流（30 s） | 2C（560 A） | 经销商规格 |
| 交流内阻（1 kHz） | ≤ 0.25 mΩ | EVE 官方 datasheet |
| 25 °C 标准循环寿命 | ≥ 6000 次（容量保持率 ≥ 80%） | EVE 官方 datasheet |
| 推荐 SOC 窗口 | 10%–90% | 经销商规格 |
| 充电温度 | 0 °C – 60 °C | EVE 官方 datasheet |
| 放电温度 | −30 °C – 60 °C | EVE 官方 datasheet |
| 极柱 | M6 螺纹孔 | 经销商规格 |

## 应用场景

- **电网与工商业储能**：集装箱式储能系统的核心电芯。
- **商用车动力电池**：电动巴士、物流车底盘电池包。
- **人形机器人底盘/备用电源**：长续航、高循环寿命需求平台。
- **特种车辆与船舶**：对安全性与循环寿命要求高的场景。

## 供应链关系

- **上游**：磷酸铁锂正极、石墨负极、隔膜、电解液、铝壳、结构件、铜箔/铝箔。
- **制造商**：`ent_company_eve_energy` -- `manufactures` --> `ent_component_eve_lf280k_cell`。
- **下游客户**：储能系统集成商、商用车 OEM、机器人整机厂、特种车辆厂商。
- **竞争对手/对标**：CATL、BYD、国轩高科、欣旺达、LG Energy Solution。

## 来源与验证

1. EVE LF280K 官方规格书（PDF）：https://akkudoktor.net/uploads/short-url/jEC8pfYYVepQ4z81Qz6rOgbA2BJ.pdf
2. EVE Energy North America 产品页：https://www.evebatteryusa.com/copy-of-18650-and-21700-specifications
3. DNK Power 产品规格页：https://www.dnkpower.com/eve-lf280k-3-2v-280ah-prismatic-lifepo4-battery-cell/
4. IMR Batteries 规格页：https://imrbatteries.com/products/eve-lf280k-280ah-3-2v-lifepo4-prismatic-battery-grade-a-1