---
id: ent_component_jonhon_ev_hv_connector
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 中航光电新能源汽车高压连接器（EVH/EVC 系列）
  en: JONHON EV High-Voltage Connector (EVH/EVC Series)
status: active
sources:
- id: src_jonhon_official
  type: website
- title: 中航光电官网
  url: https://www.jonhon.cn
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from company Wiki and product manual summaries; missing
    values marked as 未公开.
---


# 中航光电新能源汽车高压连接器（EVH/EVC 系列） / JONHON EV High-Voltage Connector (EVH/EVC Series)

## 概述

中航光电（JONHON）新能源汽车高压连接器是面向电动汽车及高功率移动平台的大电流、高电压互连组件，典型系列包括 EVH、EVC 等。产品采用铜合金接触件、工程塑料壳体及高压互锁（HVIL）设计，具备高防护等级、长插拔寿命与抗振动能力，适用于电池包、电机控制器、电驱系统及人形机器人高功率关节的电力连接。

## 工作原理 / 技术架构

高压连接器通过多触点铜合金端子实现大电流传输，接触电阻 $R_c$ 决定导通损耗与温升：

$$
P_{\text{loss}} = I^2 R_c
$$

其中 $I$ 为额定工作电流。为抑制电磁干扰（EMI）并保障人身安全，连接器集成屏蔽层与高压互锁回路（HVIL）：HVIL 在插头未完全插入时断开，使高压系统无法上电。

绝缘性能以耐电压 $V_{\text{withstand}}$ 与绝缘电阻 $R_{\text{iso}}$ 表征：

$$
I_{\text{leak}} = \frac{V_{\text{test}}}{R_{\text{iso}}}
$$

设计目标为使漏电流 $I_{\text{leak}}$ 低于安全限值。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 额定电压 | 1000 V DC | 中航光电公司 Wiki |
| 额定电流 | 80–350 A | 中航光电公司 Wiki |
| 耐电压 | 3000 V AC / 1 min | 中航光电公司 Wiki |
| 防护等级 | IP67 / IP6K9K | 中航光电公司 Wiki |
| 工作温度 | −40 °C – +125 °C | 中航光电公司 Wiki |
| 插拔寿命 | ≥ 10,000 次 | 中航光电公司 Wiki |
| 壳体材料 | 铜合金 / PBT / PA66 | 中航光电公司 Wiki |
| 接触电阻 | ≤ 5 mΩ（同系列参考） | 中航光电公司 Wiki |
| 高压互锁（HVIL） | 支持 | 中航光电产品手册 |
| 屏蔽 | 支持 | 中航光电产品手册 |
| 具体型号尺寸 | 未公开 | - |
| 防护帽/密封件 | 未公开 | - |

## 应用场景

- **新能源汽车**：电池包、电机、电控之间的高压大电流连接。
- **人形机器人高功率关节**：为下肢大扭矩电机、电缸等提供动力连接。
- **储能系统**：电池簇、PCS、高压配电单元的互连。
- **轨道交通与工业装备**：高可靠、长寿命高压连接需求。

## 供应链关系

- **上游**：铜合金、工程塑料（PBT/PA66）、电镀材料、密封件、精密机加工件。
- **制造商**：`ent_company_jonhon` -- `manufactures` --> `ent_component_jonhon_ev_hv_connector`。
- **下游客户**：新能源汽车 OEM、机器人整机厂、储能系统集成商、航空航天与军工客户。
- **竞争对手/对标**：TE Connectivity、Amphenol、Molex、立讯精密、永贵电器。

## 来源与验证

1. 中航光电官网：https://www.jonhon.cn
2. 附录 D 企业 Wiki：company_jonhon.md
3. 中航光电年报与产品手册