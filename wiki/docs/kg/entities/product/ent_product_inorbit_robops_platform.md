---
id: ent_product_inorbit_robops_platform
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: InOrbit RobOps 平台
  en: InOrbit RobOps Platform
status: active
sources:
- id: src_ent_product_inorbit_robops_platform_1
  type: website
  url: https://www.inorbit.ai/warehouseautomation
- id: src_ent_product_inorbit_robops_platform_2
  type: website
  url: https://mobile-industrial-robots.com/zh/products/mir-go/inorbit-robot-operations-platform
- id: src_ent_product_inorbit_robops_platform_3
  type: website
  url: https://roboticsandautomationnews.com/2021/08/25/inorbit-to-support-massrobotics-amr-interoperability-standard/45834/
- id: src_ent_product_inorbit_robops_platform_4
  type: website
  url: https://www.automation.com/article/inorbit-developer-edition-robot-orchestration
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# InOrbit RobOps 平台

## 概述

InOrbit RobOps 平台是 InOrbit.AI 推出的云原生机器人运营（Robot Operations, RobOps）软件即服务（SaaS）。该平台以“四个 O”——可观测性（Observability）、操作（Operations）、优化（Optimization）与编排（Orchestration）——为核心，帮助机器人开发商与终端企业在全球范围内开发、部署、监控并运营异构机器人车队。它是 InOrbit Space Intelligence 的基础层，也可独立用于中小规模车队管理。

## 工作原理 / 技术架构

平台通过 InOrbit Agent 或 Robot SDK 与机器人建立安全连接，兼容 ROS 1、ROS 2 及主流商业车队管理软件。数据经加密通道上传至云端后，提供实时遥测、地图位置、告警、事件响应与远程遥操作能力。

核心能力包括：

- **Adaptive Diagnostics™**：基于机器学习自动分类机器人故障，减少平均修复时间（MTTR）。
- **Time Capsule™**：历史数据回放，用于事后分析与问题复现。
- **Advanced Teleoperation**：低延迟远程接管与地图级控制。
- **Config as Code / Audit Log**：将配置以代码形式管理，支持版本控制与审计追踪。
- **InOrbit Connect**：机器人认证计划，支持 VDA 5050、MassRobotics AMR Interoperability Standard、Open-RMF 等协议。

平台的互操作性使其可连接 30 余家机器人品牌，包括 Mobile Industrial Robots (MiR)、Omron、OTTO Motors 等。部署形态包括公有云 SaaS、私有云或本地部署，并提供 Free / Standard / Developer / Enterprise 等订阅层级。

## 关键参数表

| 参数项 | 数值/描述 | 备注/来源 |
|--------|-----------|-----------|
| 产品形态 | 云原生 SaaS / 私有化部署 | InOrbit 官网 |
| 核心框架 | Observability / Operations / Optimization / Orchestration | InOrbit 官方 |
| 接入方式 | InOrbit Agent / Robot SDK / VDA 5050 / MassRobotics | InOrbit 仓库自动化页 |
| 兼容中间件 | ROS 1、ROS 2、Fleet Management Software | MiR Go 产品页 |
| 认证机器人品牌 | 30+（MiR、Omron、OTTO 等） | Automation.com |
| 安全特性 | 安全消息通道、RBAC、SSO、安全数据管道 | MiR Go 产品页 |
| 关键功能 | Adaptive Diagnostics、Time Capsule、远程遥操作、审计日志 | InOrbit 官方 |
| 订阅层级 | Free / Standard / Developer / Enterprise | InOrbit 仓库自动化页 |
| 开发者门户 | https://developer.inorbit.ai | MiR Go 产品页 |
| 定价 | 未公开 | 订阅制，需询价 |

## 应用场景

- **AMR/AGV 车队监控**：统一查看多品牌移动机器人的状态、位置、电池与健康度。
- **远程运维与事件响应**：在机器人异常时一键接管、触发工单或与 PagerDuty 等 incident 平台集成。
- **机器人开发商快速上市**：通过 Developer Edition 与 SDK 在平台基础上构建定制化应用。
- **仓储与制造数据分析**：利用 Time Capsule 与可配置仪表盘分析 KPI、定位瓶颈。

## 供应链关系

InOrbit RobOps 平台由 `ent_company_inorbit` 开发运营，是 InOrbit 产品体系的基础层。上游依赖 AWS/Google Cloud 云基础设施、ROS 社区、VDA 5050 / MassRobotics 等互操作标准以及 SICK 等定位系统；下游客户包括机器人 OEM、系统集成商、3PL、制造与零售企业。在知识图谱中：

- `ent_company_inorbit` -- `manufactures` --> `ent_product_inorbit_robops_platform`
- `ent_product_inorbit_robops_platform` -- `integrates_with` --> ROS/ROS2 / VDA 5050 / MassRobotics
- `ent_product_inorbit_robops_platform` -- `evolves_into` --> `ent_product_inorbit_space_intelligence`

## 来源与验证

- InOrbit RobOps 平台的功能与订阅层级来自 InOrbit Warehouse Automation 官方页。
- 与 MiR 等品牌的兼容性、安全特性与开发者门户来自 MiR Go 认证解决方案页。
- MassRobotics 与 VDA 5050 互操作支持来自 Robotics and Automation News 与 Automation.com 报道。