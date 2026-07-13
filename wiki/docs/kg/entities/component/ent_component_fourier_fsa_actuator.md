---
id: ent_component_fourier_fsa_actuator
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 傅利叶 FSA 智能执行器
  en: Fourier FSA Intelligent Actuator
status: active
sources:
- id: src_fourier_gr2_official
  type: website
  url: https://www.fftai.com/products-gr2
- id: src_humanoid_guide_gr2
  type: website
  url: https://humanoid.guide/product/gr-2/
- id: src_top3dshop_humanoid
  type: website
  url: https://top3dshop.com/blog/humanoid-robots-types-history-best-models
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 傅利叶 FSA 智能执行器

## 概述

FSA（Fourier Smart Actuator，傅利叶智能执行器）是上海傅利叶智能科技有限公司自研的一体化关节执行器，广泛应用于其 GR-1、GR-2 等人形机器人及康复外骨骼产品。FSA 将无框力矩电机、伺服驱动器、减速器与双编码器集成于轴向堆叠的紧凑壳体内，形成“电机—减速器—驱动—传感”四位一体的关节模组。GR-2 搭载的 FSA 2.0 版本峰值关节扭矩超过 $380\,\text{N}\cdot\text{m}$，部分关节最高可达 $436\,\text{N}\cdot\text{m}$，并采用双编码器设计以将控制精度提升一倍。

## 工作原理 / 技术架构

FSA 执行器基于永磁同步力矩电机与低减速比（准直驱）传动方案。电机输出经谐波减速器或行星减速器放大扭矩后驱动关节输出端。忽略传动损耗时，输出扭矩 $T_{\text{out}}$ 与电机峰值扭矩 $T_{\text{motor}}$、减速比 $i$、传动效率 $\eta$ 的关系为

$$
T_{\text{out}} = T_{\text{motor}} \cdot i \cdot \eta.
$$

FSA 2.0 采用双编码器闭环：电机端高速编码器用于电流环与速度环的高频反馈，输出端低速编码器直接测量关节角度，用于位置环与末端力矩估计。双编码器可补偿减速器弹性变形与回程误差，提升定位精度。结合电流环中的力矩观测，系统可在不额外安装六维力传感器的情况下实现关节层面的柔顺控制与碰撞检测。

## 关键参数表

| 参数 | 规格 |
|---|---|
| 产品名称 | Fourier FSA / FSA 2.0 智能执行器 |
| 峰值关节扭矩 | $>380\,\text{N}\cdot\text{m}$（FSA 2.0，部分关节最高 $436\,\text{N}\cdot\text{m}$） |
| 执行器类型 | 一体化旋转关节执行器 |
| 电机类型 | 永磁同步无框力矩电机 |
| 减速机构 | 谐波/行星减速器（依关节类型） |
| 编码器配置 | 双编码器（电机端 + 输出端） |
| 控制方式 | 位置 / 速度 / 力矩三环闭环 |
| 应用机型 | GR-1、GR-2 等人形机器人 |
| 配套软件 | 支持 ROS、NVIDIA Isaac Lab、MuJoCo |

## 应用场景

FSA 执行器主要服务于傅利叶自身的人形机器人平台，并在以下场景展现价值：

- **人形机器人全身运动**：为 GR-2 的 53 个自由度提供高扭矩密度关节驱动，实现 bipedal 行走、上下楼梯及全身动态平衡。
- **工业装配与搬运**：高峰值扭矩使机器人能够搬运数公斤级工件并完成插拔、拧紧等接触式作业。
- **康复与外骨骼**：FSA 的力控能力使其适用于康复机器人关节，实现柔顺的人机交互训练。
- **具身 AI 研究**：与 NVIDIA Isaac Lab、MuJoCo 等仿真平台兼容，便于在仿真中训练策略并迁移到真实机器人。

## 供应链关系

傅利叶智能作为 FSA 执行器的设计者与集成商，处于机器人产业链中“核心零部件/子系统”层。其上游包括无框力矩电机绕组、谐波减速器（如绿的谐波）、磁编码器芯片、功率半导体与结构件供应商；下游则直接服务于傅利叶自有的 GR 系列人形机器人，并可能向其他机器人本体厂商或研究机构提供关节模组。FSA 的自主研发使傅利叶在“机器人本体—关节执行器—运动控制算法”链条上具备较强的垂直整合能力。

## 来源与验证

- 傅利叶官方 GR-2 产品页（https://www.fftai.com/products-gr2）明确列出 FSA 2.0 峰值扭矩 $>380\,\text{N}\cdot\text{m}$、53 个关节、双编码器系统及 Isaac Lab/ROS/MuJoCo 兼容性。
- Humanoid.Guide 产品数据库确认 GR-2 身高 $175\,\text{cm}$、体重 $63\,\text{kg}$、53 DOF、FSA 2.0 峰值扭矩及 $5\,\text{km/h}$ 行走速度。
- Top3DShop 人形机器人指南指出 FSA 将电机、驱动器、减速器与编码器集成于一体，是傅利叶从康复机器人拓展到人形机器人的关键技术。