---
id: ent_product_lingxin_linker_hand_o6
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: component
names:
  zh: 灵心巧手 Linker Hand O6
  en: Linkerbot Linker Hand O6 Dexterous Hand
status: active
sources:
- id: src_linkerbot_o6_official
  type: website
  url: https://linkerbot.cn/product?page=O6
- title: Linker Hand O6 灵巧手 - 灵心巧手官网
- id: src_linkerbot_36kr
  type: website
  url: https://m.36kr.com/p/3568200976055175
- title: 月订单破千台，「灵心巧手」完成数亿元 A+ 轮融资 - 36氪
- id: src_linkerbot_ithome
  type: website
  url: https://www.ithome.com/0/946/273.htm
- title: 中国机器人创企“灵心巧手”寻求下一轮融资 - IT之家
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 灵心巧手 Linker Hand O6 / Linkerbot Linker Hand O6 Dexterous Hand

## 概述

Linker Hand O6 是灵心巧手（Linkerbot）推出的轻量化五指灵巧手，整机重量仅 370 g，具备 6 个主动自由度与 5 个被动自由度，最大抓握负载可达 50 kg。该产品面向物流搬运、工业装配、异形抓取、医疗假肢及中小型人形机器人末端操作，兼具小巧尺寸与高负载能力。

## 工作原理 / 技术架构

O6 采用连杆传动结构，由空心杯电机驱动，并经高精密谐波减速器放大扭矩。手指运动学可表示为

\[
\mathbf{p}_{\text{fingertip}} = f(\mathbf{q}_{\text{active}}, \mathbf{q}_{\text{passive}})
\]

其中主动关节 \(\mathbf{q}_{\text{active}}\) 通过连杆耦合驱动被动关节 \(\mathbf{q}_{\text{passive}}\)，实现多指协同包络抓取。内置高精度磁场编码器与力控算法，重复定位精度 \(\le \pm 0.20\,\text{mm}\)。控制器支持 CAN/CAN FD、RS485 与 EtherCAT 接口，可选配触觉传感器实现闭环力控。

指尖力方面，拇指最大指尖力 \(20\,\text{N}\)，四指最大指尖力 \(25\,\text{N}\)，五指协同最大抓握力 \(70\,\text{N}\)。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 主动自由度 | 6 |
| 被动自由度 | 5 |
| 重量 | 370 g |
| 最大负载 | 50 kg |
| 重复定位精度 | \(\le \pm 0.20\,\text{mm}\) |
| 拇指最大指尖力 | 20 N |
| 四指最大指尖力 | 25 N |
| 五指最大抓握力 | 70 N |
| 工作电压 | 24–48 V |
| 控制接口 | CAN/CAN FD、RS485、EtherCAT |
| 四指弯曲角度 | \(1.61\,\text{rad}\)（约 \(92.6^\circ\)） |
| 触觉传感器 | 选配 |

## 应用场景

- 物流仓储中的箱型/异形物体抓取
- 工业装配与螺丝拧紧
- 人形机器人末端灵巧操作
- 医疗假肢与康复辅助
- 科研教育与数据遥操作

## 供应链关系

Linker Hand O6 由灵心巧手（北京）科技有限公司研发制造。上游包括空心杯电机、谐波减速器、磁编码器、铝合金结构件与可选触觉传感器；中游为灵心巧手自研的连杆传动、驱控算法与端云融合技能库平台 LinkerSkillNet；下游面向人形机器人本体厂商、工业集成商与科研机构。灵心巧手同时提供 L6/L10/L20/L30 等覆盖 6–42 自由度的灵巧手产品矩阵。

## 来源与验证

参数直接引用灵心巧手官网产品页。部分动态性能（如关节最大角速度、防护等级、寿命循环次数）未在公开资料中披露，标注为“未公开”。