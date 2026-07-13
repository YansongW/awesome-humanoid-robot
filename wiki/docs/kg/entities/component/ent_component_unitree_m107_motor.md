---
id: ent_component_unitree_m107_motor
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 宇树 M107 关节电机
  en: Unitree M107 Joint Motor
status: active
sources:
- id: src_unitree_h1
  type: website
  url: https://www.unitree.com/h1/
- id: src_quadruped_h1_overview
  type: website
  url: https://www.docs.quadruped.de/projects/h1/html/h1_overview.html
- id: src_robozaps_h1_review
  type: website
  url: https://blog.robozaps.com/b/unitree-h1-review
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 宇树 M107 关节电机 / Unitree M107 Joint Motor

## 概述

Unitree M107 是宇树科技（Unitree Robotics）自研的高扭矩密度关节电机，采用内转子永磁同步电机（PMSM）与准直驱传动架构，专为通用人形机器人设计。该电机广泛应用于 Unitree H1、H1-2 与 G1 等人形机器人平台，承担髋、膝、踝、肩、肘等关键关节的功率输出与动态控制任务。其突出特点是在 1.9 kg 左右的电机质量下实现 360 N·m 的峰值扭矩，峰值扭矩密度达到 189 N·m/kg，支持高速奔跑与动态平衡。

## 工作原理 / 技术架构

M107 基于三相永磁同步电机，配合磁场定向控制（FOC）实现电流、转速与位置的闭环调节。电机采用内转子布局以降低转动惯量，转子内置永磁体，定子绕组由伺服驱动器按 SVPWM 方式供电。关节输出端通常连接低减速比行星减速器或谐波减速器，并集成交叉滚子轴承与中空走线结构，使动力线、编码器线可从关节中心穿过。

关节输出扭矩与电机电磁扭矩的关系可写为：

$$
\tau_{\text{joint}} = \eta \, N \, \tau_{\text{motor}}
$$

其中 $N$ 为减速比，$\eta$ 为传动效率。在准直驱设计中 $N$ 较小，电机输出扭矩本身较大，因而可实现高带宽力控。

电机功率密度与扭矩密度的定义分别为：

$$
\rho_P = \frac{P}{m}, \qquad \rho_{\tau} = \frac{\tau_{\text{peak}}}{m}
$$

按公开数据，M107 的 $\rho_{\tau} \approx 189\ \text{N·m/kg}$， knee 关节峰值扭矩 $360\ \text{N·m}$。

## 关键参数表

| 参数 | 数值 / 说明 |
|------|------------|
| 电机类型 | 内转子永磁同步电机（PMSM） |
| 控制方式 | FOC / SVPWM |
| 峰值扭矩（膝关节） | 360 N·m |
| 髋关节扭矩 | 220 N·m |
| 踝关节扭矩 | 45 N·m |
| 手臂关节扭矩 | 75 N·m |
| 电机质量 | 约 1.9 kg |
| 峰值扭矩密度 | 189 N·m/kg |
| 轴承 | 工业级交叉滚子轴承 |
| 编码器 | 双编码器 + 中空轴 |
| 应用平台 | Unitree H1 / H1-2 / G1 |
| 行走速度 | H1 > 1.5 m/s，潜在能力 > 5 m/s |

## 应用场景

M107 主要面向高性能人形机器人整机，适用于以下场景：

- 研究级双足机器人动态行走、奔跑与跳跃；
- 工业/服务人形机器人关节驱动；
- 高动态平衡控制与摔倒恢复算法验证；
- 机器人运动学、强化学习与具身智能研究平台。

## 供应链关系

在知识图谱的公司—产品—零部件网络中，`ent_component_unitree_m107_motor` 位于执行层零部件节点。其制造商 `ent_company_unitree` 同时生产整机产品 `ent_product_unitree_h1` 与 `ent_product_unitree_g1`，这两款人形机器人将 M107 作为核心关节电机使用。M107 向上依赖永磁材料、绕组铜线、轴承、编码器芯片与驱动器等上游零部件，向下为整机平台提供关节动力输出。

## 来源与验证

- Unitree 官方 H1 产品页说明 H1 采用自研 M107 关节电机，膝关节峰值扭矩 360 N·m，扭矩密度 189 N·m/kg。
- QUADRUPED Docs 的 H1 概述页列出 M107 最大扭矩 360 N·m、最大拉力 10000 N（3.5 cm 力臂等效）及中空轴、双编码器配置。
- RoboZaps 测评汇总了 H1 的 M107 电机参数与整机性能数据。
- 本条目参数均来自上述公开资料，未对未公开项进行臆测。