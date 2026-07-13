---
id: ent_component_zhaowei_micro_joint
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 兆威微型关节模组
  en: Zhaowei Micro Joint Module
sources:
- id: src_zhaowei_official
  type: website
- title: '"兆威机电官网"'
  url: https://www.zhaowei-china.com
- id: src_zhaowei_robot_head
  type: website
- title: '"兆威机器人头部旋转舵机产品页"'
  url: https://www.szzhaowei.net/zt/book/a190.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 兆威微型关节模组 / Zhaowei Micro Joint Module

## 概述

兆威微型关节模组是深圳市兆威机电股份有限公司推出的电机+减速箱+输出机构一体化微型驱动单元，直径覆盖 10–30 mm，专为机器人手指、腕部、头部舵机及小型关节设计，具有高减速比、低噪音、定位可控的特点。

## 工作原理 / 技术架构

模组内部集成微型直流有刷/无刷电机与多级行星/蜗轮减速箱，电机输出经减速后驱动输出轴。输出扭矩与电机扭矩、减速比和效率的关系为：

$$T_{\text{out}} = T_{\text{motor}} \cdot i \cdot \eta$$

其中 $i$ 为减速比，$\eta$ 为传动效率。控制接口支持 PWM 或模拟信号，定位精度可达 ±0.5°。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 尺寸 | Ø10–Ø30 mm | 兆威产品手册 |
| 重量 | 5–60 g | 兆威产品手册 |
| 输出扭矩 | 0.1–5 N·cm | 兆威产品手册 |
| 减速比 | 10:1 – 500:1 | 兆威产品手册 |
| 供电电压 | DC 3–12 V | 兆威产品手册 |
| 通信接口 | PWM / 模拟 | 兆威产品手册 |
| 定位精度 | ±0.5° | 兆威产品手册 |
| 噪音水平 | ≤ 45 dB（部分型号） | 兆威产品手册 |
| 具体型号扭矩-转速曲线 | 未公开 | 需定制确认 |

## 应用场景

仿生机器人手指、教育机器人、服务机器人头部/手部、智能门锁、VR 手柄、汽车电子执行器。

## 供应链关系

兆威机电（`ent_company_zhaowei`）自主设计模具、齿轮与电控，具备 3.4 mm–38 mm 微型传动方案能力；下游客户覆盖消费电子、汽车 Tier 1、医疗器械与人形机器人整机厂，与 Faulhaber、Maxon、尼得科等竞争。

## 来源与验证

- 兆威机电官网：https://www.zhaowei-china.com
- 兆威机器人头部旋转舵机产品页：https://www.szzhaowei.net/zt/book/a190.html