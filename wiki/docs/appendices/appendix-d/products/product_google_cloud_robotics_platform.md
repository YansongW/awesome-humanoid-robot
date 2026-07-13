# Google Cloud Robotics 平台 / Google Cloud Robotics Platform

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Google Cloud Robotics](../companies/company_google_cloud_robotics.md) |
| **产品类别** | 云机器人平台 / 机器人-云联邦编排 |
| **发布时间** | 2018 年宣布，2019 年开发者预览 |
| **状态** | 开源核心 + 企业云服务 |
| **官网/来源** | [Google Cloud Robotics](https://cloud.google.com/solutions/robotics) |

## 产品概述

Google Cloud Robotics Platform 是 Google Cloud 面向机器人开发者与企业推出的云机器人解决方案。平台以开源项目 Cloud Robotics Core 为基础，通过 Kubernetes 联邦架构连接机器人与云端，使开发者能够像管理云应用一样管理机器人应用。

平台提供安全双向通信、应用包分发、设备身份管理，并无缝集成 Vertex AI、Cloud Storage、BigQuery、Cloud Operations Suite 以及 Cartographer SLAM 等 Google 服务。其设计强调开放性：客户拥有数据，可按需迁移，且核心基础设施开源。

与 AWS RoboMaker 的托管式路径不同，Google Cloud Robotics 更偏向“平台 + 开源核心”模式，适合需要高度定制化、多云/混合云部署或深度集成 Google AI 能力的企业。

## 产品图片

> Google Cloud Robotics Platform：请访问 [官方资料](https://cloud.google.com/solutions/robotics) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 部署形态 | 公有云 PaaS / 开源核心 | Google Cloud 官网 |
| 开源核心 | Cloud Robotics Core | GitHub |
| 编排引擎 | Kubernetes / GKE | Google Cloud 文档 |
| 中间件支持 | ROS / ROS2 | Cloud Robotics Core 文档 |
| 通信协议 | gRPC、MQTT、HTTPS | 公开资料 |
| AI/ML 服务 | Vertex AI、AutoML、TensorFlow | Google Cloud 公开资料 |
| 空间智能 | Cartographer 2D/3D SLAM | Google 开源项目 |
| 数据服务 | Cloud Storage、BigQuery | Google Cloud 文档 |
| 价格 | 按 Google Cloud 资源使用计费 | Google Cloud 定价页 |

## 供应链位置

- **制造商**：[Google Cloud Robotics](../companies/company_google_cloud_robotics.md)
- **核心零部件/技术来源**：Google Cloud 基础设施、Kubernetes 生态、ROS/ROS2、Cartographer、Edge TPU、Vertex AI。
- **下游应用/客户**：工业机器人 OEM、AMR 厂商、系统集成商、物流与制造企业、科研机构。

## 知识图谱节点与关系

- 产品实体：`ent_product_google_cloud_robotics_platform`
- 制造商实体：`ent_company_google_cloud_robotics`
- 关键关系：
  - `rel_ent_company_google_cloud_robotics_manufactures_ent_product_google_cloud_robotics_platform`（`ent_company_google_cloud_robotics` → `manufactures` → `ent_product_google_cloud_robotics_platform`）

## 应用场景

- **多品牌 AMR 车队编排**：通过 Kubernetes 应用包统一管理不同厂商的机器人软件与配置。
- **云端 SLAM 与地图共享**：利用 Cartographer 与 Cloud Storage 实现多机器人地图更新与共享。
- **视觉-语言-动作模型**：结合 Vertex AI 与 Gemini API 为机器人提供多模态感知与推理能力。
- **工业数字孪生**：通过 Google Cloud 仿真与 AI 服务构建高保真数字孪生环境。

## 竞争对比

| 对比项 | Google Cloud Robotics | AWS RoboMaker | Formant |
|--------|----------------------|---------------|---------|
| 定位 | Kubernetes 原生云机器人平台 | 端到端托管云机器人服务 | 机器人数据与运维平台 |
| 开放性 | 核心开源 | 部分服务逐步迁移/开源 | 商业 SaaS |
| AI 集成 | Vertex AI / Gemini | SageMaker | 第三方集成 |
| 编排 | Kubernetes 联邦 | AWS 托管服务 | 平台内置 |
| 目标用户 | 有 DevOps 能力的企业 | 希望快速上云的开发者 | 运营型机器人客户 |

## 选购与部署建议

- 适合已有 Kubernetes/GKE 经验、希望深度定制云-边协同架构的团队。
- 开源 Cloud Robotics Core 可用于私有云或混合云部署，降低厂商锁定风险。
- 部署前需规划设备身份认证、网络策略、联邦资源配置以及与 Vertex AI 的数据流水线。

## 参考资料

1. [Google Cloud Robotics 官网](https://cloud.google.com/solutions/robotics)
2. [Cloud Robotics Core GitHub](https://github.com/googlecloudrobotics/core)
3. [Cloud Robotics Core 文档](https://googlecloudrobotics.github.io/core/)
4. [The Robot Report – Google Cloud Robotics Platform 报道](https://www.therobotreport.com/google-cloud-robotics-platform/)