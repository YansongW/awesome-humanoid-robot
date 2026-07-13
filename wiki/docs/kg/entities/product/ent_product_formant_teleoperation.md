---
id: ent_product_formant_teleoperation
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Formant 远程操作
  en: Formant Teleoperation
status: active
sources:
- id: src_ent_product_formant_teleoperation_website
  type: website
  url: https://www.formant.ai/
- id: src_ent_product_formant_teleoperation_blog
  type: website
  url: https://formant.io/news-and-blog/2019/07/12/company-updates/formant-acquires-formation-to-add-robot-remote-control-to-its-fleet-management-solutions/
- id: src_ent_product_formant_teleoperation_wiki
  type: website
  url: docs/appendices/appendix-d/companies/company_formant.md
- id: src_ent_product_formant_teleoperation_finder
  type: website
  url: https://softwarefinder.com/fleet-management-software/formant
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Formant 远程操作 / Formant Teleoperation

## 概述

Formant Teleoperation 是美国 Formant 公司提供的机器人远程操作模块，嵌入在 Formant 机器人运营（Robot Operations, RobOps）平台中。该模块通过云端或私有化部署，允许操作人员在浏览器端对机器人进行实时接管，支持键盘、游戏手柄、触屏及自定义 API 等多种控制方式，并集成多路摄像头实时回传、2D/3D 地图叠加、紧急停止、权限管理与操作审计，适用于仓库、巡检、农业、清洁等规模化机器人车队的异常干预与人工辅助。

## 工作原理与技术架构

Formant 平台在机器人端部署轻量级 Agent，将遥测数据、日志、视频流、点云和地图信息通过安全连接上传至云端。远程操作模块在浏览器端呈现统一的机器人状态面板，操作员发送的控制指令经云端转发回 Agent，再由 Agent 转换为 ROS/ROS2 或机器人原生 SDK 命令。

系统架构特点：

- **多源数据融合**：同时显示多路摄像头画面、激光雷达点云、2D/3D 地图及机器人状态。
- **低延迟传输**：利用 WebRTC 等协议实现视频与控制流的低延迟传输，实际端到端延迟取决于网络条件与边缘代理部署。
- **安全与合规**：支持紧急停止（E-Stop）、基于角色的权限控制、操作审计日志，并符合 SOC 2、GDPR 等合规要求。
- **网络适应性**：具备弱网/断网重连与边缘缓存能力，提升复杂网络环境下的可用性。

控制链路可抽象为：

$$
\text{Operator} \rightarrow \text{Formant Cloud} \rightarrow \text{Edge Agent} \rightarrow \text{Robot OS} \rightarrow \text{Actuators}
$$

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 部署形态 | 公有云 SaaS / 私有化部署 | — |
| 控制方式 | 键盘、游戏手柄、触屏、自定义 API | — |
| 视频流 | 多路摄像头实时回传 | — |
| 地图与导航 | 2D/3D 地图叠加、目标点导航 | — |
| 安全机制 | 紧急停止、权限管理、审计日志 | — |
| 接入中间件 | ROS 1 / ROS 2、MQTT、REST API | — |
| 网络适应性 | 弱网/断网重连、边缘缓存 | — |
| 遥操作延迟 | 未公开 | 依赖网络与边缘代理 |
| 支持车队规模 | 数千台机器人 | 公开报道 |
| 合规认证 | SOC 2、GDPR | — |
| 定价 | 按设备/数据量订阅 | 官方询价 |

## 应用场景

- **仓储 AMR 车队**：拥堵场景下人工接管、异常货物处理。
- **户外巡检机器人**：复杂地形或设备异常时的远程辅助操作。
- **农业机器人**：田间故障诊断与作业干预。
- **清洁服务机器人**：规模化运营中的远程调度与任务接管。
- **人形机器人远程辅助**：半自主模式下由操作员接管完成复杂抓取或导航任务。

## 供应链关系

- **开发商/运营商**：`ent_company_formant`（Formant, Inc.）。
- **上游基础设施**：AWS/Google Cloud/Azure 等公有云、边缘计算节点、ROS/ROS2、WebRTC、视频编解码与网络传输技术。
- **下游客户**：机器人制造商（如 SoftBank Robotics、Burro、Knightscope）与终端企业用户。
- **知识图谱关系**：
  - `ent_company_formant` — `manufactures` → `ent_product_formant_teleoperation`
  - `ent_product_formant_teleoperation` — `part_of` → `ent_product_formant_platform`

## 来源与验证

- Formant 官网介绍其平台连接机器人、操作员、企业系统与 AI Agent，支持监控、干预、证据与编排，并已服务超过 64.4 万个生产组织。
- Formant 博客披露其 2019 年收购 Formation 以增强远程控制能力，目标为浏览器端、云端化的机器人远程控制。
- 附录 D Wiki《Formant》词条摘录了 Teleoperation 的控制方式、视频回传、地图导航、安全机制、网络适应性等参数。
- 端到端遥操作延迟未在公开资料中披露，表中标注为“未公开”。