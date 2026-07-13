---
id: ent_company_aws_robomaker
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: AWS RoboMaker
  en: AWS RoboMaker
status: active
sources:
- id: src_aws_robomaker_official
  type: website
  url: https://aws.amazon.com/robomaker
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---





# AWS RoboMaker / AWS RoboMaker

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 亚马逊云科技 RoboMaker |
| **英文名** | AWS RoboMaker |
| **总部** | 美国华盛顿州西雅图 |
| **成立时间** | 2018 年发布（2019 年正式商用） |
| **官网** | [https://aws.amazon.com/robomaker](https://aws.amazon.com/robomaker) |
| **供应链环节** | 云机器人平台、机器人仿真、车队管理 |
| **企业属性** | 公有云部门服务 |
| **母公司/所属集团** | Amazon Web Services（AWS）/ Amazon.com Inc. |
| **数据来源** | AWS 官网、AWS RoboMaker 产品页、AWS 博客与公告 |

## 公司简介

AWS RoboMaker 是 Amazon Web Services 推出的云机器人开发平台，旨在为机器人开发者提供基于云的仿真、机器学习、车队管理与持续集成/持续部署（CI/CD）能力。

平台原生集成 Robot Operating System（ROS/ROS2），开发者可在云端大规模运行 Gazebo 仿真，利用 Amazon SageMaker 训练模型，并通过 AWS IoT Greengrass 将模型部署到边缘机器人。RoboMaker 还提供了示例应用与世界文件（如 Small Warehouse World），加速 AMR、仓储机器人与户外移动机器人的原型验证。

2024 年起，AWS 逐步将 RoboMaker 的部分托管能力迁移至开源 ROS 生态与更广泛的 AWS 服务组合（如 IoT、SageMaker、SimSpace Weaver），建议新客户基于开源工具链与 AWS 服务自行搭建云机器人解决方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 云机器人开发平台 | 云端 ROS/ROS2 开发与仿真 | AWS RoboMaker | AMR、仓储、服务机器人 |
| 仿真与数字孪生 | 大规模并行物理仿真 | RoboMaker Simulation | 算法验证、场景回归测试 |
| 车队与边缘管理 | 机器人 OTA、监控、任务调度 | AWS IoT Greengrass + RoboMaker Fleet Management | 现场部署、远程运维 |
| 机器学习服务 | 云端模型训练与边缘推理 | Amazon SageMaker + RoboMaker ML | 感知、导航、操纵 |

## 代表产品

### AWS RoboMaker 云机器人平台

> AWS RoboMaker：请访问 [官方资料](https://aws.amazon.com/robomaker) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 部署形态 | 公有云 SaaS / PaaS | AWS 官网 |
| 支持中间件 | ROS 1 / ROS 2 | AWS RoboMaker 文档 |
| 仿真引擎 | Gazebo / Ignition | AWS 公开资料 |
| 最大并发仿真 | 按需扩展（AWS 计算资源） | AWS 官网 |
| 边缘部署 | AWS IoT Greengrass | AWS 文档 |
| ML 训练集成 | Amazon SageMaker | AWS 公开资料 |
| 数据存储 | Amazon S3、Amazon CloudWatch | AWS 文档 |
| 价格 | 按仿真小时、存储与数据传输计费 | AWS 定价页 |

**技术亮点**：云端 ROS 开发环境、大规模并行仿真、与 SageMaker 联动的模型训练、Greengrass 边缘部署、示例仓库世界与导航栈。

**应用场景**：AMR 导航算法验证、仓储机器人数字孪生、服务机器人远程监控、机器人模型 OTA 更新。

### AWS IoT Greengrass（机器人边缘部署）

> AWS IoT Greengrass：请访问 [官方资料](https://aws.amazon.com/robomaker) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 部署形态 | 边缘运行时 + 云端管理 | AWS 官网 |
| 支持协议 | MQTT、HTTP、本地 Lambda | AWS 文档 |
| 安全机制 | 设备证书、IAM、TLS 加密 | AWS 公开资料 |
| 离线运行 | 支持本地计算与消息队列 | AWS 文档 |
| 支持的硬件 | ARM / x86 边缘网关、NVIDIA Jetson 等 | AWS 公开资料 |
| 容器支持 | Docker 兼容 | AWS 文档 |
| 价格 | 按设备连接与消息计费 | AWS 定价页 |

**技术亮点**：边缘-云协同、本地 Lambda 计算、安全 OTA、设备影子与状态同步、与 RoboMaker 车队管理联动。

**应用场景**：机器人现场任务执行、离线/弱网环境下的本地决策、工厂产线边缘推理、车队级配置下发。

## 供应链位置

- **上游关键零部件/材料**：AWS 自研云基础设施、NVIDIA/Intel 边缘计算模块、ROS/ROS2 开源生态、Gazebo 仿真引擎。
- **下游客户/应用场景**：仓储物流 AMR、服务机器人厂商、自动驾驶研发、教育与研究机构。
- **主要竞争对手/对标**：Google Cloud Robotics、Microsoft Azure IoT + ROS、Formant、InOrbit、Freedom Robotics。

## 知识图谱节点与关系

- 公司实体：`ent_company_aws_robomaker`
- 产品/平台实体：`ent_product_aws_robomaker_cloud`、`ent_product_aws_iot_greengrass`
- 关键关系：
  - `rel_ent_company_aws_robomaker_manufactures_ent_product_aws_robomaker_cloud`（`ent_company_aws_robomaker` → `manufactures` → `ent_product_aws_robomaker_cloud`）
  - `rel_ent_company_aws_robomaker_manufactures_ent_product_aws_iot_greengrass`（`ent_company_aws_robomaker` → `manufactures` → `ent_product_aws_iot_greengrass`）

## 参考资料

1. [AWS RoboMaker 官网](https://aws.amazon.com/robomaker)
2. [AWS RoboMaker 文档](https://docs.aws.amazon.com/robomaker/)
3. [AWS IoT Greengrass 产品页](https://aws.amazon.com/greengrass/)
4. [AWS 博客 – RoboMaker 迁移公告](https://aws.amazon.com/blogs/robotics/)