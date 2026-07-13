---
id: ent_product_fanuc_m20id_35
type: product
domain: 04_assembly_integration_testing
theoretical_depth: system
names:
  zh: FANUC M-20iD/35 工业机器人
  en: FANUC M-20iD/35 Industrial Robot
aliases:
- M-20iD/35
- FANUC M-20 系列
status: active
sources:
- id: fanuc_m20id35_page
  type: website
  url: https://www.fanucamerica.com/products/robot/m-20id-35
- title: FANUC M-20iD/35 Robot - FANUC America
- id: fanuc_m20id35_eu
  type: website
  url: https://www.fanuc.eu/es/en/robots/robot-filter-page/m-20-series/m-20id-35
- title: Material handling robot M-20iD/35 - FANUC Europe
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# FANUC M-20iD/35 工业机器人 / FANUC M-20iD/35 Industrial Robot

## 概述

FANUC M-20iD/35 是日本发那科（FANUC）公司 M-20 系列中的 35 kg 负载六轴工业机器人，水平 reach 1831 mm，重复定位精度 ±0.03 mm。该机型采用中空手腕与全内置管线设计，防护等级达 IP67，适用于搬运、装配、打磨、机床上下料等中载高速任务。

## 工作原理 / 技术架构

M-20iD/35 为六轴串联关节型机器人，各轴由 FANUC 伺服电机驱动，通过 R-30iB Plus 控制器实现运动规划与伺服控制。机器人正运动学将关节角 $\boldsymbol{\theta}=[\theta_1,\dots,\theta_6]^T$ 映射到末端位姿 $T_b^e(\boldsymbol{\theta})$。在笛卡尔空间轨迹规划中，控制器采用逆运动学求解与速度前馈补偿，确保高速下的轨迹精度。

其腕部中空直径 57 mm，允许电缆、气管与传感器线束全部内置于机械臂内部，降低外部管线磨损与干涉风险。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 控制轴数 | 6 |
| 额定负载 | 35 kg |
| 水平 reach | 1831 mm |
| 重复定位精度 | ±0.03 mm |
| 机械单元重量 | 约 250 kg |
| 控制器 | R-30iB Plus |
| J1 运动范围/最大速度 | 340°/370° / 180°/s |
| J2 运动范围/最大速度 | 260° / 180°/s |
| J3 运动范围/最大速度 | 458° / 200°/s |
| J4 运动范围/最大速度 | 400° / 350°/s |
| J5 运动范围/最大速度 | 360° / 350°/s |
| J6 运动范围/最大速度 | 900° / 400°/s |
| J4/J5 允许力矩/惯量 | 110 N·m / 4 kg·m² |
| J6 允许力矩/惯量 | 60 N·m / 1.5 kg·m² |
| 防护等级 | 本体 IP54，手腕/J3 手臂 IP67 |
| 安装方式 | 地面、倒挂、倾斜 |
| 中空手腕直径 | 57 mm |

## 应用场景

- 汽车与零部件搬运、焊接与装配
- 金属加工机床上下料
- 压铸、锻造后处理（打磨、去毛刺）
- 食品饮料行业的包装与码垛

## 供应链关系

FANUC 是全球少数实现控制器、伺服系统、减速器与机器人本体垂直整合的厂商。M-20iD/35 处于工业自动化产业链中游，上游核心部件由 FANUC 自产或指定供应商提供；下游通过系统集成商进入汽车、金属加工、物流等行业。FANUC 同时提供 iRVision 视觉、力传感器与 ROBOGUIDE 离线编程软件，形成完整生态。

## 来源与验证

参数来源于 FANUC America 官方产品页（https://www.fanucamerica.com/products/robot/m-20id-35）及 FANUC Europe 产品页（https://www.fanuc.eu/es/en/robots/robot-filter-page/m-20-series/m-20id-35）。完整 datasheet 可通过 FANUC 官方渠道获取。