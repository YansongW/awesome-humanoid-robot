---
id: ent_product_aws_iot_greengrass
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: AWS IoT Greengrass 边缘运行时
  en: AWS IoT Greengrass Edge Runtime
status: active
sources:
- id: src_aws_greengrass
  type: website
  url: https://aws.amazon.com/greengrass/
- id: src_aws_greengrass_docs
  type: website
  url: https://docs.aws.amazon.com/greengrass/v2/developerguide/
- id: src_aws_robomaker
  type: website
  url: https://aws.amazon.com/robomaker/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# AWS IoT Greengrass 边缘运行时

## 概述

AWS IoT Greengrass 是 Amazon Web Services 推出的开源物联网边缘运行时与云服务，帮助用户在边缘设备上构建、部署和管理 IoT 应用。Greengrass v2 采用基于组件（component）的模块化架构，支持在本地运行 AWS Lambda 函数、Docker 容器、自定义进程及机器学习推理，并可在弱网或离线条件下持续工作，待连接恢复后与 AWS 云端同步数据与状态。

## 工作原理 / 技术架构

Greengrass v2 的核心是 **Greengrass Nucleus**，负责组件生命周期管理、本地进程间通信（IPC）、设备影子同步、OTA 更新与安全凭证管理。每个功能单元（如 MQTT 代理、日志管理、机器学习运行时、自定义业务逻辑）都以独立组件形式部署，可独立版本化与升级。

核心交互流程为：

1. 云端通过 AWS IoT Core 向核心设备或事物组下发部署（Deployment）。
2. Nucleus 拉取组件配方（recipe）与构件（artifact），在本地完成安装与启动。
3. 组件通过本地 IPC（Pub/Sub）交换消息，减少云端往返延迟。
4. 设备影子与遥测数据在本地缓存，网络恢复后同步到 AWS IoT Core / S3 / CloudWatch。

安全机制基于 X.509 设备证书、IAM 角色别名（Token Exchange Service）与 TLS 加密，实现云端到边缘的零信任访问控制。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 开发商 | Amazon Web Services |
| 产品形态 | 边缘运行时 + 云端管理服务 |
| 主要版本 | AWS IoT Greengrass v2 |
| 开源性 | Nucleus 及核心组件开源 |
| 支持操作系统 | Linux（Amazon Linux 2、Ubuntu、Raspberry Pi OS 等）、Windows（x86_64，部分功能受限） |
| 支持架构 | ARMv7l、ARMv8（AArch64）、x86_64 |
| 最低内存要求 | 96 MB RAM（分配给 Greengrass Core） |
| 最低磁盘要求 | 256 MB |
| 运行环境依赖 | Java 8 或更高版本 |
| 通信协议 | MQTT、HTTP、本地 IPC |
| 容器支持 | Docker 兼容 |
| 离线运行 | 支持本地计算与消息队列 |
| 安全机制 | 设备证书、IAM、TLS 加密、设备影子 |
| 定价 | 按设备连接与消息量计费 |

## 应用场景

- **机器人车队管理**：通过 RoboMaker Fleet Management 对 AMR、服务机器人进行远程监控、配置下发与 OTA 更新。
- **边缘 AI 推理**：将 SageMaker 训练的模型部署到边缘网关或机器人本体，实现低延迟视觉检测与决策。
- **工厂产线边缘计算**：本地采集 PLC、传感器数据，过滤聚合后上传云端。
- **离线/弱网环境**：矿井、船舶、野外机器人等场景下的本地任务执行与数据缓存。

## 供应链关系

在公司—产品—零部件网络中，AWS IoT Greengrass 处于**云-边协同软件平台层**：

- **上游**：AWS 云基础设施（IoT Core、S3、SageMaker、CloudWatch）、NVIDIA/Intel 边缘计算硬件、ROS/ROS2 开源生态。
- **自身位置**：`ent_company_aws_robomaker -- manufactures --> ent_product_aws_iot_greengrass`；Greengrass 常与 `ent_product_aws_robomaker_cloud` 协同，形成“云端开发/仿真 + 边缘部署/运维”闭环。
- **下游**：AMR 厂商、仓储物流机器人、服务机器人、工业物联网集成商及自动驾驶研发。

## 来源与验证

- AWS IoT Greengrass 产品页：https://aws.amazon.com/greengrass/
- AWS IoT Greengrass V2 开发者指南：https://docs.aws.amazon.com/greengrass/v2/developerguide/
- AWS RoboMaker 产品页：https://aws.amazon.com/robomaker/

版本、系统要求、架构支持与组件化架构均来自 AWS 官方文档；具体部署成本需参考 AWS 定价页。