---
id: ent_product_stanley_darwin
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 斯坦德 DARWIN
  en: Standard Robots DARWIN
status: active
sources:
- id: src_standard_robots_darwin
  type: website
  url: https://en.standard-robots.com/products/cid-2.html
- title: Standard Robots DARWIN Product Page
- id: src_standard_robots_36kr
  type: website
  url: https://eu.36kr.com/en/p/3639213176278404
- title: Robotics Firm with 61% CAGR Readies for IPO — 36Kr
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 斯坦德 DARWIN / Standard Robots DARWIN

## 概述

DARWIN 是深圳斯坦德机器人股份有限公司（Standard Robots）推出的工业具身智能机器人，采用“双臂 + 全向移动底盘”构型，面向精密制造、半导体、3C 电子等场景的物料搬运与复杂操作。DARWIN-01 为该系列的代表型号，具备 23 个自由度、全向底盘与多传感器融合感知能力，通过多模态算法与端到端模型实现感知-决策-控制一体化。

## 工作原理 / 技术架构

### 机构设计
DARWIN 采用双足轮式（wheeled humanoid）构型：

- **移动底盘**：全向移动（omnidirectional chassis），可在狭窄产线内横向、斜向移动；
- **躯干**：可折叠升降，支持蹲姿与站姿切换，适应不同高度的操作工位；
- **双臂**：每条手臂多自由度，末端可快速更换夹爪、吸盘或专用工具；
- **执行器**：全身配置 28 个关节电机，模拟类人运动。

### 感知与智能
DARWIN 配备“感官矩阵”（Sensory Matrix）多传感器融合系统，结合远距离目标识别与高精度测距，实现动态环境下的全空间感知。其智能系统采用：

- **多模态感知网络**：视觉、深度、力觉等多源信息融合；
- **端到端模型**：将环境感知直接映射为操作决策与运动控制；
- **模块化末端执行器系统**：支持夹爪、吸盘、专用工具的快速更换，覆盖重载搬运到精细操作。

操作空间可近似为以肩高为基准、臂长为半径的球冠区域；DARWIN-01 工作范围 >1,900 mm，满足常见工业工位的上下料与设备操作。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 型号 | DARWIN-01 |
| 外形尺寸 | 680 × 640 × 1,736 mm |
| 自由度 | 23（整机，不含末端执行器） |
| 关节电机 | 28 个 |
| 最大移动速度 | 1.5 m/s |
| 续航 | 8 h |
| 负载 | 10 kg |
| 工作范围 | >1,900 mm |
| 底盘类型 | 全向移动底盘 |
| 末端执行器 | 快换夹爪 / 吸盘 / 专用工具 |
| 感知系统 | 多传感器融合（视觉 + 深度 + 测距） |

## 应用场景

- **半导体制造**：晶圆盒、载具的精密搬运与设备上下料；
- **3C 电子产线**：零部件转运、装配辅助、SMT 产线物料配送；
- **新能源电池生产**：电芯、模组的柔性搬运；
- **汽车与精密仪器**：总装线边物流与轻量化装配。

## 供应链关系

DARWIN 位于“整机集成—零部件—上游算法/传感器”链条的整机层：

- **整机厂商**：深圳斯坦德机器人股份有限公司；
- **移动平台**：自研全向 AMR 底盘（基于 Standard Robots 在 3C 行业 AMR 的技术积累）；
- **感知模块**：集成 3D 视觉、LiDAR、IMU 等供应商方案；
- **下游客户**：半导体、3C、新能源等行业的头部制造企业。

## 来源与验证

- Standard Robots 官方英文产品页（https://en.standard-robots.com/products/cid-2.html）
- 36Kr 英文报道《Robotics Firm with 61% CAGR Readies for IPO》（2026-01-14）

> 注：部分电机型号、减速器规格、计算平台型号等细节未在公开资料中披露，标注为“未公开”。