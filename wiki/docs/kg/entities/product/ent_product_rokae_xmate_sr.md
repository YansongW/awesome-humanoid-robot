---
id: ent_product_rokae_xmate_sr
schema_version: 1
type: product
domain: 04_assembly_integration_testing
theoretical_depth: system
names:
  zh: 珞石 xMate SR 系列协作机器人
  en: ROKAE xMate SR Series Collaborative Robot
status: active
sources:
- id: src_rokae_xmate_sr_official
  type: website
  url: https://www.rokae.com/cn/product/show/544/xMateSR.html
- title: xMate SR - 珞石机器人 ROKAE 官网
- id: src_rokae_collaborative_official
  type: website
  url: https://www.rokae.com/cn/product.html
- title: 柔性协作机器人 - 珞石机器人 ROKAE 官网
- id: src_rokae_imrobotic
  type: website
  url: http://www.imrobotic.com/jiqiren/detail/2292.html
- title: 珞石 xMate SR3 参数 - 机器人在线
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 珞石 xMate SR 系列协作机器人 / ROKAE xMate SR Series Collaborative Robot

## 概述

xMate SR 系列是珞石机器人面向商用场景推出的新一代柔性协作机器人，目前包括 SR3、SR5 等型号。该系列采用工业级核心零部件、全关节力矩传感器配置与无控制柜设计，强调轻量拖动示教、灵敏碰撞检测与快速部署，适用于新零售、教育、餐饮、医疗及轻工业装配等场景。

## 工作原理 / 技术架构

xMate SR 为六轴串联协作机器人，每个关节配置力矩传感器，通过全状态反馈实现直接力控制。其动力学方程为

\[
\boldsymbol{\tau} = \mathbf{M}(\mathbf{q})\ddot{\mathbf{q}} + \mathbf{C}(\mathbf{q},\dot{\mathbf{q}})\dot{\mathbf{q}} + \mathbf{g}(\mathbf{q}) + \boldsymbol{\tau}_{\text{ext}}
\]

控制器基于该模型实现力/位混合控制，在位置控制高精度同时具备柔顺交互能力。珞石自研的 OptiMotion、TrueMotion 与 SyncMotion 算法保障路径精度；吸合式抱闸与动力学前馈补偿使上下电位置保持精度达到 \(\pm 0.1\,\text{mm}\)。

安全方面，xMate SR 具备 10 级碰撞检测、独立安全控制与 22 项安全功能，支持 1 N 超轻拖动示教与图形化编程。

## 关键参数表

| 参数 | xMate SR3 数值 |
|------|----------------|
| 负载 | 3 kg |
| 本体重量 | 约 13.8 kg |
| 工作半径 | 705 mm |
| 自由度 | 6 |
| 重复定位精度 | \(\pm 0.03\,\text{mm}\) |
| IP 防护等级 | IP54 |
| 供电电源 | 48 V DC |
| 工具端最大速度 | \(\le 1.5\,\text{m/s}\) |
| 力控相对精度 | \(0.5\,\text{N}\) / \(0.1\,\text{N}\cdot\text{m}\) |
| 笛卡尔刚度可调范围 | \(0\!\sim\!3000\,\text{N/m}\) |
| 安装方式 | 任意角度 |
| 工作温度范围 | \(0^\circ\text{C} \sim 50^\circ\text{C}\) |

## 应用场景

- 新零售中的咖啡制作、饮品调配与食品分装
- 3C 电子产品轻量装配与检测
- 医疗辅具与康复训练
- 教育科研与人机协作演示
- 物流分拣与小型工件上下料

## 供应链关系

xMate SR 系列由珞石（北京）科技有限公司研发制造。上游包括伺服电机、力矩传感器、谐波减速器、控制器与结构件；中游为珞石自研的运动控制算法、力控工艺包与 RokaeStudio 离线编程软件；下游面向系统集成商、商用服务机器人厂商与制造业终端。珞石同时提供 xMate CR、xMate ER 等面向工业重载与长臂展需求的协作机器人系列。

## 来源与验证

参数直接引用珞石官网产品页。SR5 等型号的详细关节速度、防护细节与价格未在公开资料中披露，标注为“未公开”。