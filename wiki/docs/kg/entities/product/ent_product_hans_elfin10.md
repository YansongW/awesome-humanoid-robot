---
id: ent_product_hans_elfin10
schema_version: 1
type: product
domain: 04_assembly_integration_testing
theoretical_depth: system
names:
  zh: 大族 Elfin 10 协作机器人
  en: Han's Elfin 10 Collaborative Robot
status: active
sources:
- id: src_hans_elfin10_official
  type: website
  url: https://us.hanslaser.net/products/elfin-series-collaborative-robot.html
- title: Elfin Series Collaborative Robot - Han's Laser
- id: src_hans_elfin10_canonical
  type: website
  url: https://canonicalrobots.com/en/collaborative-robots/2011/hans-robot-elfin-10-detail
- title: Han's Robot Elfin 10 Specifications - Canonical Robots
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 大族 Elfin 10 协作机器人 / Han's Elfin 10 Collaborative Robot

## 概述

大族 Elfin 10 是大族机器人（Han's Robot）推出的 6 轴协作机器人，额定负载 10 kg，工作半径 1000 mm，面向装配、搬运、检测、上下料等柔性制造场景。该机型采用模块化双关节设计，支持正装、倒装、侧装及倾斜安装，并具备图形化编程、拖拽示教与 ROS 接口，适用于人机协作产线。

## 工作原理 / 技术架构

Elfin 10 为串联 6 自由度（6-DOF）机械臂，各关节由伺服电机经谐波减速器驱动，通过 EtherCAT 总线与控制器通信。其运动学可用 Denavit-Hartenberg（D-H）参数描述，末端位姿由正运动学映射：

$$
T_{0}^{6} = \prod_{i=1}^{6} A_i(\theta_i)
$$

其中 $A_i(\theta_i)$ 为第 $i$ 个关节的齐次变换矩阵。协作安全通过力矩/电流监测实现碰撞检测，满足 ISO/TS 15066 协作机器人安全要求。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 额定负载 | 10 kg |
| 工作半径 | 1000 mm |
| 自由度 | 6 |
| 重复定位精度 | ±0.05 mm |
| 最大工具速度 | 1 m/s |
| 关节范围 | ±360°（各关节） |
| 关节最大速度 | 90°/s |
| 本体重量 | 约 40 kg |
| 防护等级 | IP54 |
| 通信接口 | EtherCAT / TCP/IP / Modbus |
| 供电 | 200–240 VAC，50–60 Hz |
| 典型功耗 | 约 350 W |

## 应用场景

- 汽车零部件装配与拧紧
- 3C 电子元器件上下料与检测
- 金属加工机床上下料
- 食品与医药行业分拣与包装

## 供应链关系

大族机器人隶属于大族激光科技产业集团，上游自研/采购伺服电机、谐波减速器、控制器与力传感器；中游为整机集成与算法开发；下游面向汽车、3C、新能源等集成商与终端工厂。Elfin 10 作为系统级产品，处于“核心零部件—整机本体—行业解决方案”链条的中游。

## 来源与验证

参数综合自大族激光美国官网 Elfin 系列产品页（https://us.hanslaser.net/products/elfin-series-collaborative-robot.html）及 Canonical Robots 官方分销规格表（https://canonicalrobots.com/en/collaborative-robots/2011/hans-robot-elfin-10-detail）。部分分销商数据存在差异，以制造商公开规格为准。