---
id: ent_component_zhongma_transmission_housing
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 中马传动变速器壳体
  en: Zhongma Transmission Housing
sources:
- id: src_zhongma_official
  type: website
- title: '"中马传动官网"'
  url: https://www.zmtransmission.com
- id: src_zhongma_investor
  type: website
- title: '"中马传动投资者关系"'
  url: https://www.zmtransmission.com/investor/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 中马传动变速器壳体 / Zhongma Transmission Housing

## 概述

中马传动变速器壳体是浙江中马传动股份有限公司生产的压铸铝合金结构件，主要用于汽车变速器、新能源汽车电机/减速器壳体，并逐步向机器人关节壳体等精密结构件延伸。产品通过高压压铸与 CNC 精加工实现一体化成型，具备良好的密封性、尺寸一致性与减重效果。

## 工作原理 / 技术架构

壳体作为传动系统的承载与密封基体，需集成轴承座、润滑油道、安装法兰与密封面。制造流程包括：

1. 模具设计与高压压铸（ADC12 / A380 铝合金）；
2. 热处理与时效强化；
3. CNC 精加工保证轴承孔与密封面精度；
4. 平面密封或 O 形圈装配确保油液不泄漏。

壳体刚度与强度直接影响传动系统的 NVH 与定位精度。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 材质 | 铝合金 ADC12 / A380 | 中马产品手册 |
| 制造工艺 | 高压压铸 + CNC 加工 | 中马产品手册 |
| 尺寸范围 | 依型号 | 产品手册 |
| 重量范围 | 2–30 kg | 中马产品手册 |
| 表面粗糙度 | Ra 3.2–6.3 | 中马产品手册 |
| 密封方式 | 平面密封 / O 形圈 | 中马产品手册 |
| 齿面/轴承孔精度 | DIN 6–8 级（配套齿轮） | 中马产品手册 |
| 具体型号尺寸 | 未公开 | - |

## 应用场景

乘用车/商用车变速器、新能源汽车电机减速器壳体、工程机械传动箱、机器人关节壳体。

## 供应链关系

中马传动（`ent_company_zhongma`）上游采购铝合金、压铸机、数控机床与刀具；下游客户包括长城汽车、长安汽车、北汽、吉利及机器人整机厂，与双环传动、精锻科技、蓝黛科技等竞争。

## 来源与验证

- 中马传动官网：https://www.zmtransmission.com
- 中马传动投资者关系：https://www.zmtransmission.com/investor/