# InOrbit 机器人运营平台 / InOrbit RobOps Platform

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [InOrbit](../companies/company_inorbit.md) |
| **产品类别** | 机器人运营（RobOps）/ 车队编排平台 |
| **发布时间** | 2017 年起持续迭代 |
| **状态** | 商用 / 免费版 + 企业版 |
| **官网/来源** | [InOrbit 官网](https://inorbit.ai) |

## 产品概述

InOrbit 机器人运营平台是业界领先的 RobOps 解决方案，帮助机器人开发商与企业在 heterogeneous（异构）机器人车队中实现可观测性、远程操作、优化与编排。平台以“四个 O”为理念：Observability（可观测）、Operations（操作）、Optimization（优化）、Orchestration（编排）。

InOrbit 提供机器人无关的 Agent、自适应诊断（Adaptive Diagnostics™）、实时地图追踪、一键事件响应、Time Capsule™ 历史数据回放，以及支持 VDA 5050、MassRobotics AMR 互操作标准的 InOrbit Connect 认证计划。2025 年，InOrbit 进一步推出 Space Intelligence，将编排能力从机器人扩展到人、手动车辆与固定设施。

InOrbit 被 Gartner 评为 2024 年物流与机器人技术 Cool Vendor，客户包括 Colgate-Palmolive、Genentech/Roche 等大型企业。

## 产品图片

> InOrbit RobOps Platform：请访问 [官方资料](https://inorbit.ai) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 部署形态 | 公有云 SaaS / 私有化部署 | InOrbit 官网 |
| 接入方式 | InOrbit Agent / Robot SDK / VDA 5050 | InOrbit 文档 |
| 支持机器人类型 | AMR、AGV、机械臂、服务机器人 | 公开资料 |
| 可观测能力 | 遥测、地图位置、告警、诊断 | InOrbit 文档 |
| 自适应诊断 | Adaptive Diagnostics™ | 官方资料 |
| 历史回放 | Time Capsule™ | InOrbit 新闻 |
| 互操作标准 | VDA 5050、MassRobotics AMR | InOrbit 文档 |
| 免费版 | 无限机器人 Free Edition | Automate.org |
| 价格 | Free / Standard / Developer / Enterprise | InOrbit 官网 |

## 供应链位置

- **制造商**：[InOrbit](../companies/company_inorbit.md)
- **核心零部件/技术来源**：AWS/Google Cloud 云基础设施、ROS/ROS2、SICK Tag-LOC 等定位系统、VDA 5050 / MassRobotics 互操作标准。
- **下游应用/客户**：Colgate-Palmolive、Genentech/Roche、物流 3PL、制造与零售企业。

## 知识图谱节点与关系

- 产品实体：`ent_product_inorbit_robops_platform`
- 制造商实体：`ent_company_inorbit`
- 关键关系：
  - `rel_ent_company_inorbit_manufactures_ent_product_inorbit_robops_platform`（`ent_company_inorbit` → `manufactures` → `ent_product_inorbit_robops_platform`）

## 应用场景

- **多品牌 AMR 混合车队**：统一编排来自不同厂商的 AMR/AGV，避免交通冲突。
- **仓库人机混行管理**：通过规则引擎为人员、叉车、机器人分配通行优先级。
- **机器人异常响应**：自适应诊断自动分类故障，一键接管或触发工单。
- **生产设施机器人编排**：与 WMS/ERP/MES 集成，实现物料配送与产线协同。

## 竞争对比

| 对比项 | InOrbit | Formant | Freedom Robotics |
|--------|---------|---------|------------------|
| 定位 | RobOps 与车队编排 | 数据与操作平台 | 远程控制与车队管理 |
| 核心优势 | 编排、互操作标准、免费版 | 数据可视化、遥操作 | 快速接入、开发友好 |
| 互操作认证 | InOrbit Connect | 较灵活 | 较灵活 |
| 企业集成 | WMS/ERP/MES | 第三方集成 | 第三方集成 |
| 目标客户 | 大型企业混合车队 | 机器人厂商 + 终端企业 | 初创机器人公司 |

## 选购与部署建议

- 适合拥有多品牌、多场景机器人车队、需要统一编排与企业系统集成的大型企业。
- 免费版可用于小规模试点，验证 Agent 稳定性与数据可视化效果。
- 部署前需梳理现有机器人接口标准，优先选择支持 VDA 5050 或 InOrbit Robot SDK 的设备。

## 参考资料

1. [InOrbit 官网](https://inorbit.ai)
2. [Automate.org – InOrbit Free Edition 发布](https://www.automate.org/news/inorbit-launches-free-edition-to-democratize-robot-operations)
3. [Automate.org – SICK 与 InOrbit 合作](https://www.automate.org/news/sick-and-inorbit-ai-achieve-groundbreaking-advances-in-robot-and-facility-operations)
4. [Robotics 247 – InOrbit A 轮融资](https://www.robotics247.com/article/inorbit.ai_closes_series_a_funding_round_to_scale_robot_orchestration_platform/designer)