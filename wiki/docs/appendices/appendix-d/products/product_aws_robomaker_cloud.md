# AWS RoboMaker 云机器人平台 / AWS RoboMaker Cloud Robotics Platform

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [AWS RoboMaker](../companies/company_aws_robomaker.md) |
| **产品类别** | 云机器人开发 / 仿真 / 车队管理平台 |
| **发布时间** | 2018 年发布，2019 年正式商用 |
| **状态** | 逐步迁移至开源与 AWS 服务组合 |
| **官网/来源** | [AWS RoboMaker 官网](https://aws.amazon.com/robomaker) |

## 产品概述

AWS RoboMaker 是 Amazon Web Services 推出的端到端云机器人平台，帮助开发者在云端开发、仿真、测试和部署机器人应用。平台原生集成 ROS/ROS2，并深度连接 AWS IoT Greengrass、Amazon SageMaker、Amazon S3、Amazon CloudWatch 等 AWS 服务。

RoboMaker 的核心价值在于将传统本地机器人开发环境迁移到可扩展的云端：开发者可在并行仿真中运行数千次场景回归测试，通过 SageMaker 训练感知与导航模型，再借助 Greengrass 将模型安全推送到边缘机器人。平台还提供 Small Warehouse World 等示例场景，方便 AMR 与仓储机器人快速原型验证。

2024 年起，AWS 建议新用户基于开源 ROS 工具链结合 AWS 服务构建云机器人解决方案，RoboMaker 的部分托管能力已迁移或开源。

## 产品图片

> AWS RoboMaker Cloud：请访问 [官方资料](https://aws.amazon.com/robomaker) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 部署形态 | 公有云 SaaS / PaaS | AWS 官网 |
| 支持中间件 | ROS 1 / ROS 2 | AWS 文档 |
| 仿真引擎 | Gazebo / Ignition | AWS 公开资料 |
| 并发仿真 | 按需扩展（EC2/SimSpace Weaver） | AWS 文档 |
| 边缘部署 | AWS IoT Greengrass | AWS 文档 |
| ML 训练 | Amazon SageMaker | AWS 公开资料 |
| 数据存储 | Amazon S3、CloudWatch Logs | AWS 文档 |
| 网络 | VPC、IAM、TLS 加密 | AWS 文档 |
| 价格 | 按仿真小时、存储与流量计费 | AWS 定价页 |

## 供应链位置

- **制造商**：[AWS RoboMaker](../companies/company_aws_robomaker.md)
- **核心零部件/技术来源**：AWS 云基础设施、NVIDIA/Intel 边缘计算平台、ROS/ROS2 开源生态、Gazebo 仿真引擎、SageMaker ML 框架。
- **下游应用/客户**：AMR 厂商、仓储物流机器人、服务机器人、自动驾驶研发、高校与研究机构。

## 知识图谱节点与关系

- 产品实体：`ent_product_aws_robomaker_cloud`
- 制造商实体：`ent_company_aws_robomaker`
- 关键关系：
  - `rel_ent_company_aws_robomaker_manufactures_ent_product_aws_robomaker_cloud`（`ent_company_aws_robomaker` → `manufactures` → `ent_product_aws_robomaker_cloud`）

## 应用场景

- **AMR 导航算法验证**：在 Small Warehouse World 等仿真环境中测试 SLAM、路径规划与避障。
- **数字孪生与场景回归**：并行运行数千次仿真，验证软件更新对机器人行为的影响。
- **云端模型训练**：利用 SageMaker 训练目标检测、语义分割或强化学习策略模型。
- **边缘 OTA 部署**：通过 Greengrass 将更新后的模型与软件安全下发到物理机器人。

## 竞争对比

| 对比项 | AWS RoboMaker | Google Cloud Robotics | Microsoft Azure IoT + ROS |
|--------|---------------|----------------------|---------------------------|
| 定位 | 端到端云机器人平台 | Kubernetes 原生云机器人框架 | 企业物联网与 ROS 集成 |
| 仿真 | Gazebo 托管仿真 | 自研/第三方仿真集成 | 第三方仿真集成 |
| 中间件 | ROS/ROS2 | ROS/ROS2 | ROS/ROS2 |
| 边缘 | AWS IoT Greengrass | Cloud Robotics Core | Azure IoT Edge |
| 商业模式 | 按使用量计费 | 开源 + 云资源计费 | 按云资源计费 |

## 选购与部署建议

- 新用户应评估是否直接使用开源 ROS + AWS 服务组合，以降低对单一托管服务的依赖。
- 大规模仿真需求可结合 SimSpace Weaver 或自管 EC2 集群以优化成本。
- 部署前需规划 VPC、IAM 权限、Greengrass 设备证书与 OTA 流水线。

## 参考资料

1. [AWS RoboMaker 官网](https://aws.amazon.com/robomaker)
2. [AWS RoboMaker 开发者指南](https://docs.aws.amazon.com/robomaker/)
3. [AWS IoT Greengrass 产品页](https://aws.amazon.com/greengrass/)
4. [AWS 机器人博客](https://aws.amazon.com/blogs/robotics/)