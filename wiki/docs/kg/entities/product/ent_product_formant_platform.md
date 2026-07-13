---
id: ent_product_formant_platform
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Formant 机器人数据与操作平台
  en: Formant Data & Operations Platform
status: active
sources:
- id: src_ent_product_formant_platform
  type: website
  url: ''
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Formant 机器人数据与操作平台 / Formant Data & Operations Platform

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Formant](../../../appendices/appendix-d/companies/company_formant.md) |
| **产品类别** | 机器人数据平台 / 远程运维 / 遥操作 |
| **发布时间** | 2017 年起持续迭代 |
| **状态** | 商用 / 规模化部署 |
| **官网/来源** | [Formant 官网](https://formant.io) |

## 产品概述

Formant 数据与操作平台是面向机器人开发商与终端企业的统一 RobOps 平台。通过轻量级 Formant Agent，机器人可在分钟级接入云端，实现遥测、日志、视频、地图、告警、远程控制与车队分析的一站式管理。

平台支持 ROS/ROS2、MQTT、REST API 等多种接入方式，兼容不同品牌、不同形态的机器人。Formant 强调“单一面板”（single pane of glass）管理异构车队，使运营人员能够以 100:1 甚至更高的机器-人比例管理规模化机器人部署。

2023 年，Formant 与 PickNik Robotics 合作集成 MoveIt Pro，进一步扩展了对机械臂遥操作与部署管理的支持。

## 产品图片

> Formant Platform：请访问 [官方资料](https://formant.io) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 部署形态 | 公有云 SaaS / 私有化部署 | Formant 官网 |
| 接入方式 | Formant Agent（一条命令安装） | Formant 文档 |
| 支持中间件 | ROS 1 / ROS 2、MQTT、REST API | 公开资料 |
| 数据类型 | 遥测、日志、视频、点云、地图、告警 | Formant 文档 |
| 可视化 | 实时仪表盘、2D/3D 视图、历史回放 | Formant 文档 |
| 遥操作 | 浏览器端远程控制、手柄/API | 公开资料 |
| 车队规模 | 支持数千台机器人 | BMW i Ventures 新闻 |
| 安全合规 | SOC 2、GDPR、加密传输 | Formant 官网 |
| 价格 | 按设备/数据量订阅 | 官方询价 |

## 供应链位置

- **制造商**：[Formant](../../../appendices/appendix-d/companies/company_formant.md)
- **核心零部件/技术来源**：AWS/Google Cloud/Azure 云基础设施、ROS/ROS2、视频编解码、WebRTC/网络传输、时序数据库。
- **下游应用/客户**：SoftBank Robotics、BP、Blue River Technology（John Deere）、Burro、Knightscope、Scythe。

## 知识图谱节点与关系

- 产品实体：`ent_product_formant_platform`
- 制造商实体：`ent_company_formant`
- 关键关系：
  - `rel_ent_company_formant_manufactures_ent_product_formant_platform`（`ent_company_formant` → `manufactures` → `ent_product_formant_platform`）

## 应用场景

- **仓储 AMR 车队监控**：实时查看位置、电池、任务状态，快速定位异常机器人。
- **农业机器人远程诊断**：通过视频与遥测回放分析田间故障根因。
- **清洁服务机器人规模化运营**：多品牌机器人统一面板管理，降低运维成本。
- **机械臂遥操作**：结合 MoveIt Pro 实现复杂抓取任务的人工接管与调试。

## 竞争对比

| 对比项 | Formant | InOrbit | Freedom Robotics |
|--------|---------|---------|------------------|
| 定位 | 机器人数据与操作平台 | 机器人运营与编排平台 | 机器人远程控制与车队管理 |
| 核心优势 | 开箱即用、数据可视化强 | 编排与互操作标准支持 | 一行代码接入、开发友好 |
| 遥操作 | 内置 | 内置 | 内置 |
| 互操作认证 | 较灵活 | InOrbit Connect | 较灵活 |
| 典型客户 | 机器人厂商 + 终端企业 | 大型企业混合车队 | 初创机器人公司 |

## 选购与部署建议

- 适合希望快速获得企业级机器人数据与运维能力、而不愿自建平台的团队。
- 部署前需评估数据出境与合规要求，选择公有云或私有化部署模式。
- 建议先接入小批量机器人，验证数据带宽、告警阈值与遥操作延迟。

## 参考资料

1. [Formant 官网](https://formant.io)
2. [BMW i Ventures – Formant 投资新闻](https://www.bmwiventures.com/news/operationalizing-robot-fleets-at-scale-our-lead-investment-in-formant)
3. [The Robot Report – Formant 与 SoftBank 合作](https://www.therobotreport.com/formants-data-platform-comes-to-softbanks-cleaning-robots/)
4. [SignalFire – Formant 投资博客](https://www.signalfire.com/blog/formant-robotics-investor)