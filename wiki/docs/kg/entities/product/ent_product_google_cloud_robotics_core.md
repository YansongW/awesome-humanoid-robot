---
id: ent_product_google_cloud_robotics_core
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Google Cloud Robotics Core
  en: Google Cloud Robotics Core
status: active
sources:
- id: src_google_cloud_robotics_github
  type: website
  url: https://github.com/googlecloudrobotics/core
- id: src_google_cloud_robotics_docs
  type: website
  url: https://googlecloudrobotics.github.io/core/
- id: src_google_cloud_robotics_overview
  type: website
  url: https://googlecloudrobotics.github.io/core/overview.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Google Cloud Robotics Core / Google Cloud Robotics Core

## 概述

Google Cloud Robotics Core 是 Google Cloud 推出的开源云机器人平台，目标是利用 Kubernetes、Google AI/ML 服务与 ROS/ROS2 生态，构建可扩展的机器人车队管理与自动化解决方案。它提供机器人-云安全双向通信、应用包管理、联邦配置以及与 Google Cloud 服务（Vertex AI、Cloud Storage、BigQuery、Cartographer）的集成。

## 工作原理 / 技术架构

Cloud Robotics Core 采用分层架构：

- **Layer 0：机器人端 Kubernetes** — 在机器人上运行单节点 Kubernetes 集群，部署容器化 ROS/ROS2 工作负载。
- **Layer 1：车队连接与安全** — 每机器人拥有唯一密钥对，云侧授权服务基于 BeyondCorp 零信任模型发放短期 OAuth 令牌；同时提供轻量级集群联邦，在断网场景下同步自定义资源。
- **Layer 2：应用管理** — 基于 Helm 的应用包机制，决定哪些组件运行在云端、哪些运行在机器人端。
- **云服务集成** — 通过 gRPC/HTTPS 与 Vertex AI、Cloud Storage、BigQuery、Cloud Operations Suite 及 Cartographer SLAM 交互。

## 关键参数表

| 规格项 | 数值/说明 | 备注/来源 |
|--------|-----------|-----------|
| 代码仓库 | github.com/googlecloudrobotics/core | GitHub |
| 开源协议 | Apache 2.0 | GitHub |
| 部署形态 | 云集群 + 机器人边缘集群 | 文档 |
| 编排引擎 | Kubernetes / GKE | 文档 |
| 中间件支持 | ROS / ROS2 | 文档 |
| 通信协议 | gRPC、MQTT、HTTPS | 文档 |
| 认证方式 | OAuth / Workload Identity | 文档 |
| 核心能力 | 联邦配置、应用包管理、安全双向通信 | GitHub |
| 集成服务 | Vertex AI、Cloud Storage、BigQuery、Cartographer | Google Cloud |

## 应用场景

- 多品牌 AMR 车队编排
- 云端 SLAM 与地图共享
- 视觉-语言-动作（VLA）模型部署
- 工业数字孪生与远程运维

## 供应链关系

Google Cloud Robotics（`ent_company_google_cloud_robotics`）维护 Cloud Robotics Core。上游依赖 Google Cloud 基础设施、Kubernetes 生态、ROS/ROS2、Cartographer 及 Edge TPU；下游客户为工业机器人 OEM、AMR 厂商、系统集成商与制造企业。在知识图谱中，`ent_company_google_cloud_robotics` 通过 `manufactures` 关系指向 `ent_product_google_cloud_robotics_core` 与 `ent_product_google_cloud_robotics_platform`。

## 来源与验证

- [Cloud Robotics Core GitHub](https://github.com/googlecloudrobotics/core)
- [Cloud Robotics Core Documentation](https://googlecloudrobotics.github.io/core/)
- [Cloud Robotics Core Overview](https://googlecloudrobotics.github.io/core/overview.html)