---
id: ent_product_limx_cl1
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 逐际动力 CL-1
  en: LimX Dynamics CL-1
status: active
sources:
- id: src_limx_cl1_botmarket24
  type: website
  url: https://botmarket24.com/en/robot-database/limx-cl1/
- title: LimX Dynamics CL-1 | BotMarket24
- id: src_limx_cl1_mikekalil
  type: website
  url: https://mikekalil.com/robots/cl-1-limx-dynamics/
- title: CL-1 Advanced AI Robot by LimX Dynamics
- id: src_limx_official
  type: website
  url: https://www.limxdynamics.com
- title: LimX Dynamics 官网
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 逐际动力 CL-1 / LimX Dynamics CL-1

## 概述

LimX Dynamics CL-1 是深圳逐际动力（LimX Dynamics）早期发布的全尺寸双足人形机器人，强调动态双足运动、实时地形感知与稳定楼梯攀爬。与当时依赖预建地图的竞品不同，CL-1 声称可通过相机、激光雷达与 IMU 融合感知，在未知楼梯上动态调整步态。CL-1 曾作为逐际动力展示全身运动控制能力的原型平台，后续公司推出了面向科研与商业的 LimX Oli、LimX Luna 等迭代机型。

## 工作原理 / 技术架构

CL-1 采用电驱动关节与 32 个自由度（DOF）设计，全身运动控制结合传统模型预测控制（MPC）与强化学习。设机器人质心状态为 $\mathbf{x}_{\text{COM}}$，足端接触力为 $\mathbf{f}_i$，则动力学约束可写为

$$
M(\mathbf{q})\ddot{\mathbf{q}} + C(\mathbf{q},\dot{\mathbf{q}})\dot{\mathbf{q}} + G(\mathbf{q}) = \mathbf{S}^T\boldsymbol{\tau} + \sum_i J_i^T \mathbf{f}_i
$$

其中 $M$ 为质量矩阵，$C$ 为科氏力与离心力项，$G$ 为重力项，$\mathbf{S}$ 为驱动关节选择矩阵，$J_i$ 为接触点雅可比。MPC 在预测时域内优化质心轨迹与接触力，保证动态平衡与地形适应性。

感知层融合摄像头、激光雷达与 IMU，生成实时地形高度图与可通行区域，用于步态规划与落脚点选择。软件栈基于 ROS，支持科研二次开发。

## 关键参数表

| 参数 | 数值/说明 | 来源 |
|------|-----------|------|
| 身高 | 1.57 m | BotMarket24 |
| 体重 | 50 kg | BotMarket24 |
| 全身自由度 | 32 DOF | BotMarket24 |
| 最大速度 | 4.32 km/h（约 1.2 m/s）| BotMarket24 |
| 最大负载 | 20 kg | BotMarket24 |
| 续航时间 | 2 h | BotMarket24 |
| 计算架构 | ROS-based | BotMarket24 |
| 行走能力 | 动态双足行走、楼梯攀爬 | 官方视频/第三方报道 |
| 感知系统 | 相机、激光雷达、IMU 融合 | 第三方报道 |
| 驱动方式 | 电驱动 | 第三方报道 |
| 参考价格 | 约 40,000 美元（估算）| BotMarket24 估算，官方未公开 |

## 应用场景

- **工业巡检**：在多层厂房、仓库中爬楼梯完成设备巡检与仪表读数。
- **物流搬运**：动态负载 20 kg 条件下在复杂地形中搬运物料。
- **科研平台**：基于 ROS 的开放架构支持运动控制、感知与强化学习算法研究。
- **制造产线**：作为早期全尺寸人形原型，验证全身移动操作可行性。

## 供应链关系

LimX CL-1 属于 **人形机器人整机/早期原型层**，上游依赖高性能关节执行器、激光雷达、深度相机、计算平台与电池；中游由逐际动力自研运动控制算法与感知系统；下游面向科研机构、工业集成商与早期技术验证客户。随着 LimX Oli、Luna 等量产导向机型的发布，CL-1 在逐际动力产品矩阵中逐步过渡到技术验证与品牌展示角色。

## 来源与验证

- BotMarket24 参数聚合页：https://botmarket24.com/en/robot-database/limx-cl1/
- Mike Kalil 机器人数据库：https://mikekalil.com/robots/cl-1-limx-dynamics/
- LimX Dynamics 官网：https://www.limxdynamics.com

**重要提示**：CL-1 的详细规格（身高、体重、自由度、速度、负载等）均来自第三方机器人数据库与行业报道，逐际动力官方未发布完整 datasheet 或产品页。表中参数应视为行业估算值，未公开项标注为“未公开”。本实体仅能确认部分公开资料。