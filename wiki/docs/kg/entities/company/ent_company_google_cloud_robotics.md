---
id: ent_company_google_cloud_robotics
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Google Cloud Robotics
  en: Google Cloud Robotics
status: active
sources:
- id: src_google_cloud_robotics_official
  type: website
  url: https://cloud.google.com/solutions/robotics
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---





# Google Cloud Robotics / Google Cloud Robotics

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Google Cloud Robotics |
| **英文名** | Google Cloud Robotics |
| **总部** | 美国加利福尼亚州山景城 |
| **成立时间** | 2018 年宣布，2019 年开发者预览 |
| **官网** | [https://cloud.google.com/solutions/robotics](https://cloud.google.com/solutions/robotics) |
| **供应链环节** | 云机器人平台、机器人-云联邦编排、AI/ML 服务 |
| **企业属性** | 公有云部门服务 |
| **母公司/所属集团** | Google Cloud / Alphabet Inc. |
| **数据来源** | Google Cloud 官网、Cloud Robotics Core GitHub、The Robot Report |

## 公司简介

Google Cloud Robotics 是 Google Cloud 面向机器人开发者与企业推出的云机器人平台，核心目标是利用 Kubernetes、Google AI/ML 服务与开源 ROS 生态，构建可扩展的机器人车队管理与自动化解决方案。

平台以 Cloud Robotics Core 为核心开源项目，提供机器人-云安全双向通信、应用包管理、联邦配置以及与 Google Cloud 服务（Vertex AI、BigQuery、Cloud Storage、Cartographer SLAM、TensorFlow）的深度集成。其“对象智能”与“空间智能”服务可支持抓取规划、库存管理与动态环境中的机器人感知。

虽然 Google Cloud Robotics 的完整商业化路径相较于 AWS RoboMaker 更为低调，但其开源核心与 Kubernetes 原生架构在多云/混合云部署、DevOps 友好的机器人应用分发方面具有代表性。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 云机器人核心平台 | 开源机器人-云联邦框架 | Cloud Robotics Core | 工业自动化、AMR 车队 |
| AI/ML 服务 | 对象识别、姿态估计、SLAM | Vertex AI + Cartographer | 抓取、导航、数字孪生 |
| 机器人应用市场 | Kubernetes 应用包分发 | Cloud Robotics App Management | 多品牌机器人集成 |
| 数据与监控 | 日志、监控、告警 | Google Cloud Operations Suite | 远程运维、车队分析 |

## 代表产品

### Google Cloud Robotics Platform

> Google Cloud Robotics Platform：请访问 [官方资料](https://cloud.google.com/solutions/robotics) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 部署形态 | 公有云 PaaS / 开源核心 | Google Cloud 官网 |
| 开源核心 | Cloud Robotics Core（GitHub） | Google Cloud Robotics GitHub |
| 编排引擎 | Kubernetes / GKE | Google Cloud 文档 |
| 中间件支持 | ROS / ROS2 | Cloud Robotics Core 文档 |
| 通信协议 | gRPC、MQTT、HTTPS | 公开资料 |
| AI 服务 | Vertex AI、AutoML、TensorFlow | Google Cloud 公开资料 |
| 空间智能 | Cartographer（2D/3D SLAM） | Google 开源项目 |
| 价格 | 按 Google Cloud 资源使用计费 | Google Cloud 定价页 |

**技术亮点**：Kubernetes 原生机器人应用管理、安全双向机器人-云通信、与 Vertex AI 联动的感知与决策、开源 Cloud Robotics Core、可移植的数据所有权模型。

**应用场景**：多品牌 AMR 车队编排、工业数字孪生、云端 SLAM 与地图共享、基于 Gemini/Vertex AI 的机器人视觉-语言-动作模型。

### Cloud Robotics Core

> Cloud Robotics Core：请访问 [官方资料](https://cloud.google.com/solutions/robotics) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 代码仓库 | github.com/googlecloudrobotics/core | GitHub |
| 开源协议 | Apache 2.0 | GitHub |
| 主要语言 | Go、Bazel、Terraform | GitHub |
| 核心能力 | 联邦配置、应用包、安全通信 | GitHub README |
| 部署方式 | 云集群 + 机器人边缘集群 | 文档 |
| 认证方式 | OAuth / Workload Identity | 文档 |
| 价格 | 开源免费；云资源按 Google Cloud 计费 | GitHub / Google Cloud |

**技术亮点**：声明式机器人-云资源配置、应用生命周期管理、设备身份与证书管理、与 Google Cloud 服务的统一身份认证。

**应用场景**：企业私有云机器人平台搭建、跨地域机器人车队管理、需要高度定制化的云-边协同机器人系统。

## 供应链位置

- **上游关键零部件/材料**：Google Cloud 基础设施、Kubernetes 生态、ROS/ROS2、Edge TPU、NVIDIA/Intel 计算平台、开源 SLAM/感知算法。
- **下游客户/应用场景**：工业机器人 OEM、AMR 厂商、系统集成商、物流与制造企业、科研机构。
- **主要竞争对手/对标**：AWS RoboMaker、Microsoft Azure IoT / ROS、Formant、InOrbit、Freedom Robotics。

## 知识图谱节点与关系

- 公司实体：`ent_company_google_cloud_robotics`
- 产品/平台实体：`ent_product_google_cloud_robotics_platform`、`ent_product_google_cloud_robotics_core`
- 关键关系：
  - `rel_ent_company_google_cloud_robotics_manufactures_ent_product_google_cloud_robotics_platform`（`ent_company_google_cloud_robotics` → `manufactures` → `ent_product_google_cloud_robotics_platform`）
  - `rel_ent_company_google_cloud_robotics_manufactures_ent_product_google_cloud_robotics_core`（`ent_company_google_cloud_robotics` → `manufactures` → `ent_product_google_cloud_robotics_core`）

## 参考资料

1. [Google Cloud Robotics 官网](https://cloud.google.com/solutions/robotics)
2. [Cloud Robotics Core GitHub](https://github.com/googlecloudrobotics/core)
3. [Cloud Robotics Core 文档](https://googlecloudrobotics.github.io/core/)
4. [The Robot Report – Google Cloud Robotics Platform 报道](https://www.therobotreport.com/google-cloud-robotics-platform/)