---
id: ent_product_xvariable_quanta_x2
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 自变量 Quanta X2（量子 2 号）轮式仿人形机器人
  en: XVariable Quanta X2 Wheeled Humanoid Robot
status: active
sources:
- id: src_xvariable_quantum2_page
  type: website
  url: https://x2robot.com/product/quantum2
- title: 自变量 Quanta X2 产品页
- id: src_xvariable_home
  type: website
  url: https://x2robot.com/
- title: 自变量机器人官网
- id: src_xvariable_huaying
  type: article
  url: http://mp.weixin.qq.com/s?__biz=Mzk0NjUxNDkxMw==&mid=2247536295&idx=3&sn=ef650ac5efb696388595b143a88ccff3
- title: 自变量机器人发布 Quanta X2
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 自变量 Quanta X2 / XVariable Quanta X2

## 概述

自变量 Quanta X2（量子 2 号）是自变量机器人推出的新一代通用轮式仿人形机器人，围绕自研 WALL-A 操作大模型构建端到端具身智能系统。该产品采用轮式移动底盘 + 高自由度双臂 + 五指灵巧手的构型，可在 0–2 m 工作高度范围内完成工业组装、家庭服务、物流分拣等跨场景任务。Quanta X2 全身 62 个自由度，单臂重复定位精度 ±0.03 mm，末端速度 1.8 m/s。

## 工作原理 / 技术架构

Quanta X2 采用“统一大模型驱动”的端到端架构：

1. **感知层**：2D 激光雷达、超声波、RGBD、3D-ToF、单点 ToF、红外等多传感器融合，构建环境语义与几何模型。
2. **决策与规划层**：WALL-A 操作大模型（百亿级参数）将视觉、语言与任务目标映射为动作序列，实现跨任务、跨场景泛化。
3. **执行层**：高自由度双臂（单臂展 765 mm）配合 20 自由度灵巧手或 2 自由度夹爪完成精细操作；轮式底盘实现 1 m/s 移动。
4. **学习与进化**：通过真实世界交互数据持续优化模型，具备长时序任务规划与复杂物体操作能力。

双臂协同操作的运动学约束可表示为

$$
\mathbf{x}_i=f_i(\mathbf{q}_i),\quad i\in\{L,R\},
$$

其中 $\mathbf{q}_i$ 为单臂关节角，$\mathbf{x}_i$ 为末端执行器位姿。双臂共同搬运负载时还需满足闭链约束

$$
g(\mathbf{x}_L,\mathbf{x}_R,\mathbf{o})=0,
$$

其中 $\mathbf{o}$ 为被抓取物体位姿。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 产品定位 | 通用轮式仿人形机器人 |
| 全身自由度 | 62 DOF |
| 身高 | 164 cm |
| 工作高度 | 0–2 m |
| 躯干自由度 | 6 |
| 单臂展 | 765 mm |
| 重复定位精度 | ±0.03 mm |
| 末端速度 | 1.8 m/s |
| 单臂额定负载 | 6 kg |
| 最大双臂负载 | 25 kg |
| 夹爪自由度 | 2 |
| 灵巧手自由度 | 20 |
| 移动速度 | 1 m/s |
| 底盘自由度 | 2 |
| 传感器 | 2D LiDAR、超声波×4、RGBD、3D-ToF、单点 ToF、红外 |
| 搭载模型 | WALL-A 操作大模型（百亿级参数） |

## 应用场景

- **工业制造**：复杂装配、线束整理、质量检测。
- **家庭服务**：整理桌面、衣物收纳、饮品制作、花卉养护。
- **物流分拣**：快递分拣、物品归类、柔性抓取。
- **商业服务**：酒店补给、迎宾导览、机器人荷官等交互场景。
- **科研教育**：VLA 模型训练、机器人技能学习平台。

## 供应链关系

- **上游**：轮式底盘、谐波/行星关节模组、灵巧手、多模态传感器、计算平台、电池供应商。
- **同层**：自变量机器人作为整机与基础模型开发商，提供 Quanta X2 硬件与 WALL-A 大模型。
- **下游**：工业客户、家庭用户、商业服务运营商、科研机构与开发者。

## 来源与验证

- 自变量 Quanta X2 产品页：https://x2robot.com/product/quantum2
- 自变量机器人官网：https://x2robot.com/
- 华映资本报道：http://mp.weixin.qq.com/s?__biz=Mzk0NjUxNDkxMw==&mid=2247536295&idx=3&sn=ef650ac5efb696388595b143a88ccff3