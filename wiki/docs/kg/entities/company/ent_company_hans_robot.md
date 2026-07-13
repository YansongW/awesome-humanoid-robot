---
id: ent_company_hans_robot
schema_version: 1
type: company
'title:': Han's Robot
domain: 04_assembly_integration_testing
theoretical_depth: system
names:
  zh: 大族机器人
  en: Han's Robot
status: active
sources:
- id: src_hans_robot_official
  type: website
  url: https://www.hansrobot.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 大族机器人 / Han's Robot

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 大族机器人 |
| **英文名** | Han's Robot |
| **总部** | 中国广东深圳 |
| **成立时间** | 2017 年（源自大族电机机器人事业部） |
| **官网** | [https://www.hansrobot.com](https://www.hansrobot.com) |
| **供应链环节** | 整机 OEM / 协作机器人 / 人形机器人部件 |
| **企业属性** | 国产品牌、大族激光系、协作机器人核心厂商 |
| **母公司/所属集团** | 大族激光科技产业集团股份有限公司（002008.SZ） |
| **数据来源** | 大族机器人官网、产品手册、WAIC 2026 报道、公开新闻稿 |

## 公司简介

大族机器人由大族激光内部孵化，专注于智能协作机器人研发与产业化，以 Elfin 系列协作臂为核心产品。

公司继承了母公司在精密制造与运动控制领域的能力，产品覆盖 3–20 kg 负载，强调易用性、安全性和开放生态。大族机器人同时布局复合移动机器人、力控打磨与医疗康复机器人，并积极参与人形机器人核心零部件研发。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 协作机器人 | 工业/商业/科研 | Elfin 3 / Elfin 5 / Elfin 10 | 3C、汽车、医疗、食品 |
| 复合机器人 | 移动协作 | Han's AMR + Elfin | 物流、柔性产线 |
| 智能应用 | 力控打磨、焊接、上下料 | 行业解决方案 | 金属加工、汽车 |

## 代表产品

### Elfin 5 协作机器人

> Elfin 5：请访问 [官方资料](https://www.hansrobot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 6-DOF 协作机器人 | 大族机器人官网 |
| 自重 | 约 24 kg | 产品手册 |
| 负载 | 5 kg | 产品手册 |
| 臂展 | 950 mm | 产品手册 |
| 自由度 | 6 DOF | 公开规格 |
| 重复定位精度 | ±0.03 mm | 产品手册 |
| 最大末端速度 | 未公开 | - |
| 防护等级 | IP54 | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：双关节模块化设计、拖拽示教、图形化编程、碰撞检测、开放的 ROS/ROS2 接口。

**应用场景**：3C 装配、汽车零部件上下料、医疗样本处理、食品包装、力控打磨。

### Elfin 10 协作机器人

> Elfin 10：请访问 [官方资料](https://www.hansrobot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 6-DOF 协作机器人 | 大族机器人官网 |
| 自重 | 约 38 kg | 产品手册 |
| 负载 | 10 kg | 产品手册 |
| 臂展 | 1300 mm | 产品手册 |
| 自由度 | 6 DOF | 公开规格 |
| 重复定位精度 | ±0.05 mm | 产品手册 |
| 防护等级 | IP54 | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：大负载长臂展，适合搬运、码垛、上下料等重载协作场景。

**应用场景**：汽车装配、物流搬运、金属加工、食品饮料、新能源电池产线。

## 供应链位置

- **上游关键零部件/材料**：谐波减速器、伺服电机、编码器、控制器、结构件、线缆、传感器。
- **下游客户/应用场景**：3C 电子、汽车、新能源、医疗、食品、金属加工。
- **主要竞争对手/对标**：节卡、遨博、越疆、优傲 UR、珞石。

## 知识图谱节点与关系

- 公司实体：`ent_company_hans_robot`
- 产品实体：`ent_product_hans_elfin5`、`ent_product_hans_elfin10`
- 关键关系：
  - `ent_company_hans_robot` -- `manufactures` --> `ent_product_hans_elfin5`
  - `ent_company_hans_robot` -- `manufactures` --> `ent_product_hans_elfin10`

## 参考资料

1. [大族机器人官网](https://www.hansrobot.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. 大族机器人产品手册与公开新闻稿