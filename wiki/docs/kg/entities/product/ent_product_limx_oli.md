---
id: ent_product_limx_oli
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 逐际动力 LimX Oli
  en: LimX Dynamics Oli
status: active
sources:
- id: src_limx_oli_official
  type: website
  url: https://www.limxdynamics.com/oli
- title: 逐际动力 LimX Oli 产品页
- id: src_zol_limx_oli
  type: website
  url: https://ai.zol.com.cn/1022/10226146.html
- title: 逐际动力发布人形机器人 LimX Oli
- id: src_endux_limx_oli
  type: website
  url: https://endux.co.uk/blog/limx-oli-humanoid-robot-overview
- title: 'LimX OLI Review: A Gem Among Humanoids'
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 逐际动力 LimX Oli / LimX Dynamics Oli

## 概述

LimX Oli 是深圳逐际动力科技有限公司（LimX Dynamics）于 2025 年 7 月发布的全尺寸通用人形机器人，面向具身智能科研、算法开发及系统集成。整机身高 165 cm，体重 55 kg，具备 31 个机身主动自由度（不含末端执行器），提供 Lite、EDU、Super 三个配置版本，基础售价 15.8 万元起。

## 工作原理 / 技术架构

### 机构与运动学
LimX Oli 采用双足人形构型，31 个机身自由度分布为：

- 头部：2 DOF；
- 单臂：7 DOF；
- 腰部：3 DOF；
- 单腿：6 DOF。

机身位姿与关节角构成 37 维配置空间（6 维浮动基座 + 31 维关节）。足端位置由正向运动学确定：

$$
\mathbf{p}_{\text{foot}} = f_{\text{FK}}(T_{\text{base}}, \mathbf{q})
$$

其中 $T_{\text{base}} \in SE(3)$，$\mathbf{q} \in \mathbb{R}^{31}$。

### 运动控制算法
逐际动力采用“传统控制 + 强化学习 + 模仿学习”融合策略：

- **全身运动控制**：实现稳定而灵活的全身动作跟踪与动态协调；
- **模仿学习**：基于高质量动作数据，还原垫脚、扭腰、摆臂、转腕等细节；
- **强化学习**：提升复杂地形与扰动下的鲁棒性。

### 感知系统
- 自研 6 轴 IMU；
- 头部深度相机：Intel RealSense D435i；
- 胸前深度相机：Intel RealSense D435i；
- 预留充足外部接口：USB 3.0/3.2、千兆以太网 RJ45、24 V/12 V 供电接口，可扩展 LiDAR、额外相机等传感器。

### 计算与开发
- **主控**：RK3588（8 GB / 64 GB，来源为 Humanoid.Guide 第三方规格表）；
- **操作系统**：Linux；
- **开发支持**：模块化 SDK、开放上层与底层接口、Python 全流程开发、URDF、OTA 升级；
- **仿真支持**：NVIDIA Isaac Sim、MuJoCo、Gazebo。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 身高 | 165 cm（Lite/EDU）；175 cm（Super） |
| 体重 | 55 kg（Lite/EDU）；60 kg（Super） |
| 机身自由度 | 31（不含末端执行器） |
| 单臂自由度 | 7 |
| 单腿自由度 | 6 |
| 腰部自由度 | 3 |
| 头部自由度 | 2 |
|  walking 速度 | 5 km/h |
| 单臂负载 | 3 kg（Lite/EDU）；5 kg（Super） |
| 峰值关节扭矩 | 150 N·m（第三方数据） |
| 感知 | 自研 6 轴 IMU + 双 RealSense D435i |
| 主控 | RK3588 / 8 GB / 64 GB（第三方数据） |
| 通信 | WiFi 6、USB 3.0/3.2、千兆以太网 |
| 供电接口 | 24 V 5 A / 12 V 5 A |
| 操作系统 | Linux |
| 版本 | Lite / EDU / Super |
| 起售价 | 15.8 万元 |

## 应用场景

- **高校与科研机构**：具身智能、运动控制、感知算法验证；
- **机器人开发者**：基于 Python SDK 与 ROS 接口进行二次开发；
- **系统集成商**：面向导览、服务、轻量搬运等场景的整机集成；
- **公共演示**：人形机器人动态表演与技术展示。

## 供应链关系

LimX Oli 位于“人形机器人整机—核心零部件—上游算力/传感”链条的整机与科研平台层：

- **整机厂商**：深圳逐际动力科技有限公司；
- **自研部件**：自研 6 轴 IMU、关节模组；
- **感知模块**：Intel RealSense D435i 深度相机；
- **计算平台**：RK3588（第三方规格，逐际动力官方未明确披露）；
- **投资者与生态**：阿里巴巴、京东、联想创投、上汽资本、蔚来资本等战略投资。

## 来源与验证

- 逐际动力官网 LimX Oli 产品页（https://www.limxdynamics.com/oli）
- 中关村在线报道（2025-07-30）
- Endux 第三方评测（2025-12-10）
- Humanoid.Guide 产品数据库（2026-06-11）

> 注：主控型号、电池容量、续航时间、关节峰值扭矩等参数官方未完整披露，部分来自第三方数据库，标注为参考值。