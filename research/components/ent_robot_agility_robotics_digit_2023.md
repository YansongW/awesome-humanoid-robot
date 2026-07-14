---
$id: ent_robot_agility_robotics_digit_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Agility Robotics Digit
  zh: Agility Robotics Digit
  ko: Agility Robotics Digit
summary:
  en: Bipedal warehouse robot with humanoid torso and arms, designed for logistics workflows.
  zh: 面向物流工作流的双足仓库机器人，具有人形躯干和手臂。
  ko: 물류 워크플로우용 이족 보행 창고 로봇.
domains:
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- agility_robotics
- humanoid
- logistics
- robot_system
- warehouse
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_digit.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Agility Robotics Digit
  url: https://www.agilityrobotics.com/
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Agility Robotics Digit是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Agility Robotics Digit

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Agility Robotics](../companies/company_agility_robotics.md) |
| **产品类别** | 物流/仓储人形机器人 |
| **发布时间** | 2019 年首次发布；当前为量产迭代款 |
| **状态** | 量产/商业部署 |
| **官网/来源** | [Agility Robotics 官网](https://agilityrobotics.com/) |

### 产品概述

Agility Robotics Digit 是目前在仓储物流领域部署最广泛的人形机器人之一。其采用头部躯干一体化、反向膝关节设计，专为在狭窄通道、楼梯与斜坡等人类建筑环境中搬运周转箱（tote）而优化。Digit 的感知系统包括 4 颗 Intel RealSense 深度相机、LiDAR、IMU 与力传感器，可在无需外部基础设施的情况下自主导航。

Agility 在美国俄勒冈州 Salem 建有 RoboFab 人形机器人工厂，设计年产能达 10,000 台。Digit 已在 Amazon、GXO、Spanx 等客户的仓库中执行分拣与搬运任务，并通过 Robot-as-a-Service（RaaS）模式向企业客户提供服务，降低了初期采购门槛。

### 产品图片

> Agility Robotics Digit：请访问 [官方资料](https://agilityrobotics.com/) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 175 cm（高） | 公开规格 |
| 重量 | 约 63.5–65 kg | 公开规格 |
| 自由度（整机） | 16–28 DOF（不同来源） | 公开规格 |
| 关键性能指标 | 负载 16 kg；持续搬运 35 lb | 官方规格 |
| 行走速度 | 约 5.4 km/h | 公开规格 |
| 续航 | 约 4 小时（典型任务） | 官方规格 |
| 充电 | 自主对接充电 | Agility Robotics |
| 价格 | 未公开（行业估计约 250,000 USD 或 RaaS） | 第三方估计 |

### 供应链位置

- **制造商**：[Agility Robotics](../companies/company_agility_robotics.md)
- **核心零部件/技术来源**：Intel RealSense 深度相机、LiDAR、定制电驱执行器、Agility Arc 云端 fleet 管理平台。
- **下游应用/客户**：Amazon、GXO、Spanx、Toyota Canada 等仓储与制造客户。

### 知识图谱节点与关系

- 产品实体：`ent_product_agility_robotics_digit`
- 制造商实体：`ent_company_agility_robotics`
- 关键关系：
  - `rel_ent_company_agility_robotics_manufactures_ent_product_agility_robotics_digit`（`ent_company_agility_robotics` → `manufactures` → `ent_product_agility_robotics_digit`）

### 应用场景

- **电商仓储**：在 Amazon、GXO 等仓库执行周转箱（tote）搬运与分拣。
- **零售配送**：从货架到传送带的补货、退货整理与库存移位。
- **制造物流**：汽车与消费品工厂内的零部件配送与线边补料。

### 竞争对比

| 对比项 | Agility Digit | Tesla Optimus Gen 3 | Figure 02 |
|--------|---------------|---------------------|-----------|
| 定位 | 物流仓储人形 | 通用/工业人形 | 工业制造人形 |
| 手部 | 定制末端执行器 | 22×2 灵巧手 | 16 DOF 灵巧手 |
| 商业模式 | RaaS / 企业部署 | 目标零售 | 企业试点 |
| 核心优势 | 部署规模、续航、RoboFab 产能 | 成本与制造规模目标 | AI 模型与灵巧操作 |

### 选购与部署建议

- 企业客户可通过 Agility Robotics 商务团队评估 RaaS 或采购方案，通常需完成仓库现场勘察。
- 部署前需确认周转箱规格、地面条件、Wi-Fi 覆盖以及与 WMS 的数据接口。

### 参考资料

1. [Agility Robotics 官网](https://agilityrobotics.com/)
2. [Robozaps – Agility Robotics Digit Review](https://blog.robozaps.com/b/agility-robotics-digit-review)
3. [Humanoid.Guide – Digit](https://humanoid.guide/product/digit/)
4. [The Robot Report – Agility Digit Deployments](https://www.therobotreport.com)

## 参考
- [Agility Robotics Digit](https://www.agilityrobotics.com/)
- 项目 Wiki：appendix-d/products/product_digit.md

