---
id: ent_product_inorbit_space_intelligence
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: InOrbit Space Intelligence
  en: InOrbit Space Intelligence
status: active
sources:
- id: src_ent_product_inorbit_space_intelligence_1
  type: website
  url: https://inorbitinc.mintlify.app/space-intelligence
- id: src_ent_product_inorbit_space_intelligence_2
  type: website
  url: https://www.automate.org/news/introducing-inorbit-space-intelligence-a-central-nervous-system-for-smarter-operations
- id: src_ent_product_inorbit_space_intelligence_3
  type: website
  url: https://www.robotics247.com/article/automate-2026-inorbit.ai-demonstrates-the-future-of-multi-vendor-robot-orchestration-and-physical-ai
- id: src_ent_product_inorbit_space_intelligence_4
  type: website
  url: https://www.prweb.com/releases/inorbitai-demonstrates-the-future-of-multi-vendor-robot-orchestration-and-physical-ai-302805136.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# InOrbit Space Intelligence

## 概述

InOrbit Space Intelligence 是 InOrbit.AI 推出的企业级物理世界编排平台，定位为“智能运营的中央神经系统”。它在 InOrbit RobOps 平台的基础上，进一步整合企业业务系统（WMS/ERP/MES）、机器人车队管理系统与空间计算能力，实现人、机器人、IoT 设备与非机器人资产在同一设施内的统一指挥、动态调度与持续优化。

## 工作原理 / 技术架构

Space Intelligence 采用“联邦式编排（federated orchestration）”架构：平台不替代各机器人厂商原生的车队管理系统，而是在其上构建统一的编排层，通过标准化接口与各厂商系统共存、协调与协同（3C：Co-existence、Coordination、Collaboration）。

核心模块包括：

- **Unified Command Center**：汇总所有机器人与 IoT 数据，提供跨品牌、跨地点的实时可视性与单一控制界面。
- **Business Execution System (BES)**：将来自 WMS/ERP/MES 的业务订单翻译为机器人任务，实现实时任务分配与调度。
- **RobOps Copilot**：基于 Agentic AI 的自然语言接口，支持语音或文本指令查询数据、派遣任务、生成报告。
- **AI-Powered Optimization**：利用物理 AI 与强化学习持续学习运营数据，动态优化路径、资源分配与作业顺序。

在技术接口层面，Space Intelligence 支持 InOrbit Agent、Robot SDK、VDA 5050、MassRobotics AMR Interoperability Standard 以及正在推进的 ISO/DIS 21423 标准，已认证接入 30 余家机器人品牌。

## 关键参数表

| 参数项 | 数值/描述 | 备注/来源 |
|--------|-----------|-----------|
| 部署形态 | 公有云 SaaS / 私有化部署 | InOrbit 文档 |
| 核心架构 | 联邦式编排，位于各厂商原生系统之上 | Robotics 247 / PRWeb |
| 支持机器人类型 | AMR、AGV、机械臂、服务机器人、人形机器人 | InOrbit 文档 |
| 互操作标准 | VDA 5050、MassRobotics AMR Interop、Open-RMF、ISO/DIS 21423 | 多源报道 |
| 认证机器人品牌 | 30+（InOrbit Connect 生态） | InOrbit 官方 |
| 企业系统集成 | WMS / WES / ERP / MES | InOrbit 文档 |
| 核心能力 | 实时空间感知、交通管控、任务消解、AI 优化 | A3 News |
| 关键功能 | RobOps Copilot、BES、Time Capsule、Adaptive Diagnostics | InOrbit 文档 |
| 定价 | 企业订阅，需询价 | 未公开 |

## 应用场景

- **多品牌 AMR 混合车队**：在 3PL 仓库与制造工厂中统一调度不同厂商的搬运机器人，避免交通冲突。
- **人机混行设施管理**：通过规则引擎为人员、叉车、机器人分配通行优先级与区域管控策略。
- **大规模仓储订单履约**：将 ERP/WMS 订单自动分解为机器人拣选、搬运、补货任务。
- **工业制造产线协同**：协调移动机器人与固定自动化设备完成物料配送与产线联动。

## 供应链关系

Space Intelligence 是 `ent_company_inorbit` 的核心软件产品之一，与 `ent_product_inorbit_robops_platform` 共同构成 InOrbit 的 RobOps 产品矩阵。上游依赖 AWS/Google Cloud 等云基础设施、ROS/ROS2、VDA 5050 / MassRobotics 等互操作标准以及 SICK Tag-LOC 等定位系统；下游客户包括 Colgate-Palmolive、Genentech/Roche、大型物流 3PL 与制造企业。知识图谱关系为：

- `ent_company_inorbit` -- `manufactures` --> `ent_product_inorbit_space_intelligence`
- `ent_product_inorbit_space_intelligence` -- `integrates_with` --> WMS/ERP/MES 等企业系统
- `ent_product_inorbit_space_intelligence` -- `orchestrates` --> 多品牌 AMR/AGV/机器人

## 来源与验证

- Space Intelligence 的产品定位与核心模块来自 InOrbit 官方文档与 A3 新闻稿。
- 联邦式编排、Automate 2026 八家机器人厂商现场演示及 ISO/DIS 21423 参考实现来自 Robotics 247、Industrial Sage 与 PRWeb 报道。
- 30+ 机器人品牌接入数据来自 InOrbit 官方新闻稿。