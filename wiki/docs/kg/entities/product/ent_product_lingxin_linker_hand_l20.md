---
id: ent_product_lingxin_linker_hand_l20
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: component
names:
  zh: 灵心巧手 Linker Hand L20
  en: Linkerbot Linker Hand L20
status: active
sources:
- id: src_linkerbot_l20_page
  type: website
  url: https://linkerbot.cn/product?page=L20
- title: Linker Hand L20 - 灵心巧手官网
- id: src_linkerbot_l20_bjnews
  type: website
  url: https://m.bjnews.com.cn/detail/1770890673129749.html
- title: 灵心巧手张延柏：从北京出发，打造世界级灵巧手产业生态 - 新京报
- id: src_linkerbot_l20_report
  type: report
  url: https://pdf.dfcfw.com/pdf/H3_AP202504261662702285_1.pdf
- title: 灵巧之“手”，解锁人形机器人黄金赛道 - 东方财富
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 灵心巧手 Linker Hand L20 / Linkerbot Linker Hand L20

## 概述

Linker Hand L20 是灵心巧手（北京）科技有限公司推出的高自由度连杆传动灵巧手，具备 21 个总自由度（其中 16 个主动自由度）与近 20 个自研电机。L20 采用连杆传动与自研电机+减速器驱动方案，融合指尖触觉传感器与指内三维力传感器，可完成穿针引线等精细操作，面向科研、工业精密操作及人形机器人末端执行。

## 工作原理 / 技术架构

L20 采用连杆传动机构将电机旋转运动转换为手指关节屈伸与侧摆。每个手指拥有多个自由度：食指/中指/无名指/小指在侧摆与屈伸方向独立运动，拇指具备横摆与旋转自由度。手指末端集成触觉传感器，实时反馈接触力与位姿信息。

手指力控制可建模为：

$$
\tau = J^T F + M(\theta)\ddot{\theta} + C(\theta,\dot{\theta})\dot{\theta} + G(\theta)
$$

其中 $J$ 为手指雅可比矩阵，$F$ 为末端接触力，$M$、$C$、$G$ 分别为质量矩阵、科氏力/离心力项与重力项。通过力位混合控制实现柔顺抓取。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 总自由度 | 21 |
| 主动自由度 | 16（工业版 17） |
| 自研电机数量 | 近 20 个 |
| 整手重量 | 约 1 kg |
| 最大负载 | 5 kg |
| 拇指最大抓握力 | 15 N |
| 四指最大抓握力 | 10 N |
| 重复定位精度 | ±0.2 mm |
| 传动方式 | 连杆传动 |
| 传感器 | 指尖触觉传感器、指内微型三维力传感器 |
| 通信接口 | 未公开 |

## 应用场景

- 人形机器人末端精细操作（抓取、装配、穿针）
- 科研教育与具身智能数据采集
- 工业精密装配与质量检测
- 医疗辅助与康复训练

## 供应链关系

灵心巧手处于灵巧手整机与方案层，上游自研微型减速器、执行器与传感器，采购电机、结构件与电子皮肤材料；中游为灵巧手本体、云端智脑与数据采集系统；下游面向人形机器人本体厂商（如具身智能头部企业、比亚迪、美的等）与科研机构。Linker Hand 产品线覆盖 O6/L10/L20/L30 等多个系列，L20 定位高自由度科研与工业应用。

## 来源与验证

参数来源于灵心巧手官网（https://linkerbot.cn/product?page=L20）、新京报报道（https://m.bjnews.com.cn/detail/1770890673129749.html）及东方财富行业研报（https://pdf.dfcfw.com/pdf/H3_AP202504261662702285_1.pdf）。不同来源对主动自由度数值存在 16/17 的差异，以官网与最新工业版规格为准。