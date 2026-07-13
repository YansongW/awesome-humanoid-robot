# InOrbit / InOrbit.AI

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | InOrbit |
| **英文名** | InOrbit.AI |
| **总部** | 美国加利福尼亚州山景城 |
| **成立时间** | 2017 年 |
| **官网** | [https://inorbit.ai](https://inorbit.ai) |
| **供应链环节** | 机器人运营（RobOps）、车队编排、远程运维 |
| **企业属性** | 初创公司 |
| **母公司/所属集团** | 无 |
| **数据来源** | InOrbit 官网、Automate.org、Gartner Cool Vendor 报道 |

## 公司简介

InOrbit 是一家专注于机器人运营（RobOps）与车队编排的云计算公司，致力于让人类、机器人与 AI 在真实生产环境中高效协同。

平台以“四个 O”——Observability（可观测性）、Operations（操作）、Optimization（优化）、Orchestration（编排）——为核心，提供机器人无关的 Agent、自适应诊断（Adaptive Diagnostics™）、实时地图追踪、一键事件响应、远程遥操作以及跨品牌车队编排。InOrbit Connect 认证计划支持 VDA 5050、MassRobotics AMR 互操作标准等多种接入方式，帮助企业整合不同厂商的机器人。

2024 年，InOrbit 入选 Google for Startups Latino Founders Fund；2025 年完成 1,000 万美元 A 轮融资，由 L'Attitude Ventures 与 Globant Ventures 联合领投。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 机器人运营平台 | 可观测、诊断、遥控 | InOrbit Control | 物流、制造、零售 |
| 车队编排平台 | 多品牌机器人协同 | InOrbit Space Intelligence | 大规模混合车队 |
| 开发者平台 | API、SDK、白标应用 | InOrbit Developer Edition | 系统集成商、机器人 OEM |
| 互操作认证 | 机器人接入标准 | InOrbit Connect | 多厂商生态 |

## 代表产品

### InOrbit RobOps 平台

> InOrbit RobOps：请访问 [官方资料](https://inorbit.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 部署形态 | 公有云 SaaS / 私有化部署 | InOrbit 官网 |
| 接入方式 | InOrbit Agent / Robot SDK / VDA 5050 | InOrbit 文档 |
| 支持机器人类型 | AMR、AGV、机械臂、服务机器人 | 公开资料 |
| 实时监控 | 遥测、地图位置、告警 | InOrbit 文档 |
| 自适应诊断 | Adaptive Diagnostics™ | 官方资料 |
| 时间胶囊 | Time Capsule™ 历史数据回放 | InOrbit 新闻 |
| 免费版 | 无限机器人免费版 | Automate.org |
| 价格 | Free / Standard / Developer 订阅 | InOrbit 官网 |

**技术亮点**：机器人无关的可观测层、跨品牌混合车队编排、AI 驱动的自适应诊断、Time Capsule 历史回溯、与 SICK Tag-LOC 等定位系统深度集成。

**应用场景**：3PL 仓库多品牌 AMR 协同、制造工厂人机混行交通管理、零售与服务机器人规模化运营、医院物流机器人调度。

### InOrbit Space Intelligence

> InOrbit Space Intelligence：请访问 [官方资料](https://inorbit.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 定位 | 物理世界编排层 | InOrbit 新闻 |
| 核心能力 | 共存、协调、协同（3C） | 公开资料 |
| 集成系统 | WMS / ERP / MES | InOrbit 文档 |
| 定位技术 | 支持 UWB、Tag-LOC、SLAM | InOrbit 与 SICK 合作新闻 |
| 自动化规则 | 交通优先级、充电调度、区域管控 | 公开资料 |
| 价格 | 企业订阅 | 官方询价 |

**技术亮点**：软件定义的物理运营、统一的人-机器人-车辆编排、与企业业务系统打通、规则引擎驱动的动态调度。

**应用场景**：大型仓库人机混行、多品牌 AMR 统一调度、工厂产线物料配送、机场/医院等大型设施的机器人编排。

## 供应链位置

- **上游关键零部件/材料**：AWS/Google Cloud 云基础设施、SICK 等定位传感器、ROS/ROS2、VDA 5050 / MassRobotics 互操作标准。
- **下游客户/应用场景**：Colgate-Palmolive、Genentech/Roche、物流 3PL、制造与零售企业。
- **主要竞争对手/对标**：Formant、Freedom Robotics、AW RoboMaker、Google Cloud Robotics、Locus Robotics 车队管理。

## 知识图谱节点与关系

- 公司实体：`ent_company_inorbit`
- 产品/平台实体：`ent_product_inorbit_robops_platform`、`ent_product_inorbit_space_intelligence`
- 关键关系：
  - `rel_ent_company_inorbit_manufactures_ent_product_inorbit_robops_platform`（`ent_company_inorbit` → `manufactures` → `ent_product_inorbit_robops_platform`）
  - `rel_ent_company_inorbit_manufactures_ent_product_inorbit_space_intelligence`（`ent_company_inorbit` → `manufactures` → `ent_product_inorbit_space_intelligence`）

## 参考资料

1. [InOrbit 官网](https://inorbit.ai)
2. [Automate.org – InOrbit Free Edition 发布](https://www.automate.org/news/inorbit-launches-free-edition-to-democratize-robot-operations)
3. [Automate.org – SICK 与 InOrbit 合作](https://www.automate.org/news/sick-and-inorbit-ai-achieve-groundbreaking-advances-in-robot-and-facility-operations)
4. [Robotics 247 – InOrbit A 轮融资](https://www.robotics247.com/article/inorbit.ai_closes_series_a_funding_round_to_scale_robot_orchestration_platform/designer)