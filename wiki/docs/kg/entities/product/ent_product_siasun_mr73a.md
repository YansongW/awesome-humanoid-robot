---
id: ent_product_siasun_mr73a
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 新松 睿可 MR73A
  en: SIASUN Rico MR73A Wheeled Humanoid Robot
status: active
sources:
- id: src_siasun_mr73a_xinhua
  type: website
  url: http://sh.news.cn/20250710/6e8faea1b9d04e1e9b37bb2bcc083885/c.html
- title: 中科新松推人形机器人双机开启工业智能新篇章 - 新华网
- id: src_siasun_mr73a_cnr
  type: website
  url: https://www.cnr.cn/shanghai/tt/20250709/t20250709_527253671.shtml
- title: 中科新松推人形机器人双机 - 央广网
- id: src_siasun_mr73a_official
  type: website
  url: https://www.siasun.com/news-detail954.html
- title: 新松参展2025世界智能制造大会 - 新松机器人官网
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 新松 睿可 MR73A / SIASUN Rico MR73A Wheeled Humanoid Robot

## 概述

睿可 MR73A 是中科新松有限公司于 2025 年 7 月发布的双臂轮式人形机器人，属于新松机器人集团（股票代码：300024）旗下“多可（DUCO）”品牌。该机器人以“手脑并用”为设计定位，具备 27 个自由度，强调双臂柔顺控制与智能感知，适用于仓储、工厂、展馆等复杂场景中的移动操作任务。

## 工作原理 / 技术架构

MR73A 采用“移动底盘 + 双臂 + 躯干 + 头部感知”的复合构型。双臂搭载柔顺控制技术，支持上肢协同阻抗控制与牵引拖动示教，并配备躯干避碰与外力碰撞检测系统，以保障人机协作安全。其运动控制可基于操作空间阻抗模型描述：

\[
\mathbf{F} = \mathbf{M}_d(\ddot{\mathbf{x}}_d - \ddot{\mathbf{x}}) + \mathbf{D}_d(\dot{\mathbf{x}}_d - \dot{\mathbf{x}}) + \mathbf{K}_d(\mathbf{x}_d - \mathbf{x})
\]

其中 \(\mathbf{M}_d\)、\(\mathbf{D}_d\)、\(\mathbf{K}_d\) 为期望惯性、阻尼与刚度矩阵，\(\mathbf{x}\) 为末端位姿，\(\mathbf{F}\) 为环境交互力。

感知与决策层面，MR73A 集成自主定位导航系统、动态避障与多点巡逻路径规划，融合人脸识别与物体识别的 AI 视觉技术，并搭载语音大模型实现多语言自然交互。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 类型 | 双臂轮式人形机器人 |
| 自由度 | 27 |
| 核心技术 | 双臂柔顺控制、智能感知 |
| 移动能力 | 自主定位导航、动态避障、多点巡逻 |
| 交互能力 | 语音大模型、多语言、人脸识别、物体识别 |
| 开放接口 | RS485、IO、ROS/ROS2，可扩展 EtherCAT |
| 最大移动速度 | 未公开 |
| 单臂负载 | 未公开 |
| 整机重量 / 续航 | 未公开 |

## 应用场景

- 仓库与工厂中的搬运、拾取、分拣
- 设备状态巡检与工厂安全巡查
- 展馆、园区的导览与讲解
- 产线旁非标准件的柔性上下料
- 人机协作的半自动化工作站

## 供应链关系

睿可 MR73A 由中科新松有限公司研发，新松机器人自动化股份有限公司为母公司。上游包括伺服电机、减速器、控制器、激光雷达、视觉相机、语音大模型与计算平台；中游为新松自研的运动控制、导航与 AI 视觉算法；下游面向工业制造、物流仓储与公共服务领域。同期发布的 MR73B 聚焦升降平台与灵活移动，两者共享底层核心技术。

## 来源与验证

参数来自新华网、央广网及新松官网报道。最大移动速度、单臂负载、整机重量、续航等关键性能指标未在公开资料中披露，标注为“未公开”。