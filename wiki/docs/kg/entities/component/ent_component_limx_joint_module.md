---
id: ent_component_limx_joint_module
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 逐际动力关节模组
  en: LimX Dynamics Joint Module
status: active
sources:
- id: src_ent_component_limx_joint_module_1
  type: website
  url: https://limxdynamics.com/en/products/oli/spec
- id: src_ent_component_limx_joint_module_2
  type: website
  url: https://humanoid.press/database/humanoid-press-database-oli-limx/
- id: src_ent_component_limx_joint_module_3
  type: website
  url: https://www.robotshop.com/products/limx-dynamics-oli-edu-humanoid-robot
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 逐际动力关节模组

## 概述

逐际动力（LimX Dynamics）关节模组是深圳逐际动力为其全尺寸人形机器人 Oli 及 CL 系列自研的高响应、模块化驱动单元。该模组采用电机、减速器、编码器与控制器的一体化设计，覆盖髋、膝、踝、肩、肘、腕等部位，支撑机器人实现高动态行走、负重深蹲、楼梯攀爬与全身协调操作。

## 工作原理 / 技术架构

关节模组的核心是“永磁同步电机 + 谐波/行星减速器 + 双编码器”架构。电机输出的电磁功率 $P_e$ 经减速器传递到负载端，满足

$$
P_j = \tau_j \omega_j = \eta \cdot P_e = \eta \cdot \tau_m \omega_m
$$

其中 $\tau_j$、$\omega_j$ 为关节输出扭矩与转速，$\tau_m$、$\omega_m$ 为电机端扭矩与转速，$\eta$ 为传动效率。减速比 $i$ 与输出扭矩的关系为

$$
\tau_j = \eta \, i \, \tau_m
$$

对于同一电机，提高减速比可提升关节输出扭矩，但会降低最大关节转速 $\omega_j = \omega_m / i$，因此需根据关节功能（高扭矩髋膝 vs 高转速踝腕）进行减速比匹配。

根据 LimX 官方 Oli 规格页，整机最高关节扭矩为 150 N·m（标准版），高配版可达 250 N·m。以 250 N·m 关节为例，若电机峰值扭矩为 5 N·m、减速器效率 0.80，则所需减速比约为

$$
i = \frac{250}{0.80 \times 5} = 62.5
$$

该计算仅作量级示意，实际产品减速比与电机参数未公开。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 最大关节扭矩 | 150 N·m（标准版）；250 N·m（增强版） | LimX Oli 官方规格页 |
| 整机自由度 | 31–33 DOF（Oli）；52 DOF（CL 系列汇总） | LimX 官网 / Humanoid.Press |
| 单臂最大负载 | 3 kg（标准版）；5 kg（增强版） | LimX Oli 官方规格页 |
| 最高移动速度 | 5 km/h | LimX 官方 |
| 腿部自由度 | 6 DOF × 2 | 髋 3 + 膝 1 + 踝 2 |
| 编码器 | 绝对式编码器（各主动关节） | Humanoid.Press / 官方 |
| 电机形式 | 未公开（推测为无框力矩电机/空心电机） | 未公开 |
| 减速比 | 未公开 | 未公开 |
| 关节质量 | 未公开 | 未公开 |

## 应用场景

- **全尺寸人形机器人整机驱动**：用于 LimX Oli 与 CL 系列，实现双足行走、跑步、负重搬运与复杂地形通过。
- **科研与算法验证**：LimX Oli EDU 面向高校与研究机构，关节模组支持 ROS2 与 Python SDK，便于运动控制算法开发。
- **工业物流与智能制造**：未来可扩展至仓库搬运、货架补货、产线协作等场景。

## 供应链关系

逐际动力关节模组由 `ent_company_limx` 自研并集成到 `ent_product_limx_oli` 与 `ent_product_limx_cl1` 等整机。上游包括磁钢、稀土磁材、轴承、编码器、谐波减速器柔轮/钢轮、功率驱动芯片与结构件；下游为机器人整机与终端应用客户。知识图谱中的关键关系为：

- `ent_company_limx` -- `manufactures` --> `ent_product_limx_cl1`
- `ent_product_limx_cl1` -- `uses` --> `ent_component_limx_joint_module`

## 来源与验证

- 关节扭矩、整机自由度、单臂负载、移动速度等数据来自 LimX Dynamics 官网 Oli 规格页。
- 补充背景（ROS2、SDK、应用场景）来自 Humanoid.Press 与 RobotShop 产品页。
- 单关节的电机参数、减速比与质量等逐际动力未单独公开，已标注为“未公开”。