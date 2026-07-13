---
id: ent_product_ubtech_walker_s2
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 优必选 Walker S2
  en: UBTECH Walker S2
status: active
sources:
- id: src_ubtech_walker_s2_rbtx
  type: website
  url: https://rbtx.com/en-US/components/humanoid/ubtech-humanoid-walker-s2
- title: UBTECH Walker S2 - RBTX
- id: src_ubtech_walker_s2_humanoid_guide
  type: website
  url: https://humanoid.guide/product/walker-s2/
- title: UBTECH Robotics Walker S2 Specs & Price - Humanoid.Guide
- id: src_ubtech_walker_s2_awesomerobots
  type: website
  url: https://www.awesomerobots.xyz/robots/ubtech-walker-s2
- title: UBTech Walker S2 - Awesome Robots
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 优必选 Walker S2 / UBTECH Walker S2

## 概述

优必选 Walker S2 是优必选科技推出的下一代工业级全尺寸人形机器人，定位于汽车与通用制造场景。Walker S2 在 Walker S/S1 基础上将自由度提升至 52，配备第四代灵巧五指手、高扭矩腰部与自主热插拔双电池系统，旨在实现近 24/7 连续作业。

## 工作原理 / 技术架构

Walker S2 采用全身多关节伺服驱动，腿部 6 DOF×2、手臂 7 DOF×2、灵巧手 11 DOF×2（手部共 22 DOF），腰部 2 DOF，头部 2 DOF，全身总计 52 DOF。其控制系统基于 UBTECH ROSA 2.0 / Ubuntu，融合 VSLAM、BrainNet 2.0 与 Co-Agent AI 实现任务规划与多机协同。

自主热插拔电池系统使机器人可在 3 分钟内完成电池更换，无需人工干预。视觉系统采用纯 RGB 双目立体视觉方案，通过深度学习估计稠密深度图。机器人运动学与动力学控制支撑其以 2 m/s（7.2 km/h）速度稳定行走。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 身高 | 176 cm |
| 体重 | 约 70–75 kg（不同来源） |
| 全身自由度 | 52 |
| 手部自由度 | 22 |
| 单臂负载 | 15 kg |
| 行走速度 | 最高 7.2 km/h（2 m/s） |
| 腰部旋转 | ±162° |
| 身体俯仰角 | 170° |
| 工作空间 | 0–1.8 m |
| 电池系统 | 双电池，自主热插拔，约 3 min 换电 |
| 续航 | 约 2 h/单电池 |
| 视觉 | 双目 RGB 立体视觉 + 深度学习深度估计 |
| 操作系统 | Ubuntu + ROSA 2.0 |
| 通信 | Wi-Fi 6 / 蓝牙 / 可选 5G |

## 应用场景

- 汽车总装车间的搬运、质检与装配
- 3C 电子产线的精密上下料
- 仓储物流中的分拣与搬运
- 多机协同的柔性智能制造

## 供应链关系

优必选 Walker S2 位于人形机器人整机层，上游依赖自研一体化关节、伺服电机、减速器、灵巧手、视觉模组与电池系统；中游为整机集成、运动控制与 AI 算法；下游面向汽车制造商（如比亚迪、蔚来、奥迪一汽等）及工业集成商。Walker S2 是优必选工业人形机器人产品线的旗舰型号。

## 来源与验证

参数综合自 RBTX 产品页（https://rbtx.com/en-US/components/humanoid/ubtech-humanoid-walker-s2）、Humanoid.Guide（https://humanoid.guide/product/walker-s2/）及 Awesome Robots（https://www.awesomerobots.xyz/robots/ubtech-walker-s2）。不同来源对体重、续航等参数存在差异，优必选官方未公布完整 datasheet，部分指标标注为“未公开”。