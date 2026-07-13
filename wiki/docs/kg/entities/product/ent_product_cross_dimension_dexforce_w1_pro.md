---
id: ent_product_cross_dimension_dexforce_w1_pro
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 跨维智能 DexForce W1 Pro
  en: Cross-Dimension DexForce W1 Pro
status: active
sources:
- id: src_dexforce_w1_pro_waic
  type: website
  url: https://www.donews.com/news/detail/1/5761824.html
- title: 跨维智能发布第二代人形机器人 DexForce W1 Pro | DoNews
- id: src_dexforce_w1_pro_wrc
  type: website
  url: https://www.worldrobotconference.com/expo/product/387.html
- title: DexForce W1 Pro | 世界机器人大会
- id: src_dexforce_w1_pro_zhiding
  type: website
  url: https://m.zhiding.cn/article/3169520.htm
- title: 跨维智能发布第二代人形机器人 DexForce W1 Pro | 至顶网
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 跨维智能 DexForce W1 Pro / Cross-Dimension DexForce W1 Pro

## 概述

DexForce W1 Pro 是跨维智能（Cross-Dimension）推出的第二代通用具身智能机器人，定位为“为落地真实场景而生”的高精度操作型人形机器人。其硬件平台融合自研纯视觉双目感知系统、全身谐波关节、可选差速/全向移动底盘与 6 自由度灵巧手，软件平台则基于 X-Wiz 具身智能核心与 EmbodiChain 具身智能开发平台，支持 Engine-driven Sim2Real VLA（Vision-Language-Action）部署。

## 工作原理 / 技术架构

W1 Pro 的核心感知单元为头部集成的自研纯视觉双目仿人传感器，帧率 60 Hz，水平视场角 $90^{\circ}$、垂直视场角 $60^{\circ}$。双目标定误差控制在 ±0.05 像素以内，立体匹配精度达亚像素级（≤0.1 像素），可实时输出稠密点云与深度图。对于空间点 $P=(X,Y,Z)^T$，双目三角测量关系为

$$
Z = \frac{B \cdot f}{d}
$$

其中 $B$ 为基线距，$f$ 为焦距，$d$ 为左右图像视差。配合腕部近距离操作相机（FOV $87^{\circ} \times 58^{\circ}$，工作距离 7–50 cm）与底盘前后深度相机，构建全域感知网络。

双臂采用 7 自由度冗余构型，基于 AI Co-design 优化运动学模型与机械参数，使工作空间及可达性较初代扩展 75%。结合视觉伺服，重复定位精度达到 ≤0.5 mm。自动手眼标定功能在长时间运行后补偿相机-末端相对位姿漂移，保证持续高精度作业。

软件层面，EmbodiChain 平台依托 DexVerse 数据引擎，将真实数据采集升级为低成本、大规模的合成-真实混合数据管线，支持离线预训练与在线微调，从而缩短 VLA 模型真机部署周期。

## 关键参数表

| 参数 | W1 Pro | W1 Core | 备注 |
|------|--------|---------|------|
| 形态 | 双足 + 可选移动底盘 | 上半身（无底盘）| 双版本 |
| 全身自由度 | 34 / 40 DOF | 34 / 40 DOF（腿部以上）| 含灵巧手 |
| 单臂自由度 | 7 DOF | 7 DOF | 冗余构型 |
| 末端执行器 | 6 DOF 灵巧手 / 二指夹爪 | 同左 | 可选配 |
| 重复定位精度 | ≤0.5 mm | ≤0.5 mm | 结合视觉 |
| 头部双目帧率 | 60 Hz | 60 Hz | 较初代 15 Hz 提升 4 倍 |
| 头部双目 FOV | 90° × 60° | 90° × 60° | 仿人视野 |
| 双目标定误差 | ≤±0.05 像素 | ≤±0.05 像素 | 官方发布 |
| 立体匹配精度 | ≤0.1 像素 | ≤0.1 像素 | 亚像素级 |
| 腕部相机 FOV | 87° × 58° | 87° × 58° | 近距离操作 |
| 底盘前后深度相机 | 工作距离 0.2–2.5 m | 无 | W1 Pro 专属 |
| 移动底盘 | 差速 / 全向可选 | 无 | W1 Pro 专属 |
| 软件平台 | X-Wiz + EmbodiChain | X-Wiz + EmbodiChain | 跨维自研 |

## 应用场景

- **智能制造**：产线高精度柔性装配、带操作巡检、物料分拣，利用 ≤0.5 mm 重复定位精度完成精密插接。
- **科研教育**：作为 VLA 模型训练与机器人技能学习的可控、高精度平台，支持 Sim2Real 快速迁移。
- **商业服务**：展会、酒店、零售场景中的迎宾、导览、产品介绍，已在深圳 K11、桂林象山等景区试点。
- **家庭助理**：整理桌面、递送物品、辅助备餐等家务指令执行。

## 供应链关系

DexForce W1 Pro 属于 **人形机器人整机/具身智能平台层**，上游包括谐波减速器、力矩电机、纯视觉相机、计算平台（如 NVIDIA Jetson 或国产芯片）、电池与结构件；中游为跨维智能自研的 X-Wiz 感知-决策-执行核心与 EmbodiChain 数据引擎；下游面向工业集成商、科研院所与商业服务运营商。跨维智能同时通过 DexVerse 数据引擎连接数字仿真与真机部署，形成“数据-模型-硬件”闭环。

## 来源与验证

- 跨维智能 WAIC 2025 发布会报道（DoNews）：https://www.donews.com/news/detail/1/5761824.html
- 世界机器人大会展商产品页：https://www.worldrobotconference.com/expo/product/387.html
- 至顶网详细报道：https://m.zhiding.cn/article/3169520.htm

官方尚未公开全部机械参数（如整机重量、关节扭矩、电池容量），表中未标注项以发布会公开资料为准。