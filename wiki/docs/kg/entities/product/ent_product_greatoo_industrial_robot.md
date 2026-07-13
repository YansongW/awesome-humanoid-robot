---
id: ent_product_greatoo_industrial_robot
schema_version: 1
type: product
domain: 02_components
theoretical_depth: system
names:
  zh: 巨轮智能 JLRB06 轻载工业机器人
  en: Greatoo JLRB06 Light-load Industrial Robot
status: active
sources:
- id: src_greatoo_jlrb06_official
  type: website
  url: http://www.greatoo.com/GongYeJiQiRen/show/4.html
- title: 轻载机器人（JLRBO6）- 巨轮智能装备股份有限公司
- id: src_greatoo_company_profile
  type: website
  url: http://www.greatoo.com
- title: 巨轮智能装备股份有限公司官网
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 巨轮智能 JLRB06 轻载工业机器人 / Greatoo JLRB06 Light-load Industrial Robot

## 概述

巨轮智能装备股份有限公司（股票代码：002031）是国内较早布局工业机器人业务的装备制造企业之一，其工业机器人产品线涵盖轻载、重载、码垛等类型。JLRB06 为 JL 系列轻载六轴工业机器人，本体小巧、模块化程度高，主要用于上下料、分拣、装配、弧焊、抛光去毛刺等工序。该机型是巨轮智能面向 3C、汽车零部件、橡胶塑料及机床自动化单元推出的代表性产品。

## 工作原理 / 技术架构

JLRB06 采用串联六自由度关节型构型，各关节由伺服电机经减速器驱动，通过控制器实现位置、速度与力矩闭环。机器人运动学可基于改进 Denavit-Hartenberg（D-H）参数描述，末端位姿

\[
\mathbf{T}_{\text{end}} = \prod_{i=1}^{6} {^{i-1}\mathbf{T}_i}(\theta_i)
\]

其中 \(\theta_i\) 为第 \(i\) 个关节角。控制器接收目标轨迹后，通过逆运动学求解关节角序列，再利用前馈补偿与伺服闭环完成高速高精度跟踪。重复定位精度达到 \(\pm 0.04\,\text{mm}\) 级别，支持地面、壁挂、倒挂三种安装方式，可在狭小空间内灵活作业。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 轴数 | 6 |
| 手腕最大负载 | 6 kg |
| 最大工作半径 | 1380 mm |
| 重复定位精度 | \(\pm 0.04\,\text{mm}\) |
| 安装方式 | 地面 / 壁挂 / 倒挂 |
| 整机重量 | 未公开 |
| 最大关节速度 | 未公开 |
| 防护等级 | 未公开 |

## 应用场景

JLRB06 适用于组建小型自动化单元，典型场景包括：

- 机床上下料与工件转运
- 3C 零部件装配、分拣与包装
- 汽车及橡胶塑料件弧焊、密封涂胶
- 金属件抛光去毛刺

## 供应链关系

JLRB06 由巨轮智能装备股份有限公司及其子公司巨轮中德机器人智能制造有限公司、巨轮（广州）机器人与智能制造有限公司研发制造。上游涉及伺服电机、减速器、控制器、线缆等核心零部件；下游面向自动化集成商及终端制造企业的智能产线。巨轮智能同时生产 RV/XT 减速器、精密机床、轮胎硫化机等，具备从核心部件到整机装备的纵向布局能力。

## 来源与验证

参数与描述主要来源于巨轮智能官网产品页。整机重量、最大关节速度、防护等级等细节未在公开资料中披露，标注为“未公开”。