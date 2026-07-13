---
id: ent_company_tesla
schema_version: 1
type: company
'title:': Tesla, Inc.
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 特斯拉
  en: Tesla, Inc.
aliases:
- 特斯拉
- Tesla, Inc.
status: active
sources:
- id: src_tesla_official
  type: website
  url: https://www.tesla.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# 特斯拉 / Tesla, Inc.

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 特斯拉 |
| **英文名** | Tesla, Inc. |
| **总部** | 美国德克萨斯州奥斯汀 |
| **成立时间** | 2003 |
| **官网** | [https://www.tesla.com](https://www.tesla.com) |
| **供应链环节** | 整车/OEM、人形机器人整机厂、核心零部件自研 |
| **企业属性** | 上市公司（NASDAQ: TSLA） |
| **母公司/所属集团** | 无（Tesla, Inc. 为上市主体） |
| **数据来源** | Tesla 官网、AI Day 公开演示、第三方技术汇编 |

## 公司简介

特斯拉是全球知名的电动汽车与清洁能源公司，正通过 Optimus 人形机器人将其垂直整合的制造与 AI 能力延伸至通用机器人领域。

2021 年 Tesla AI Day 首次发布 Tesla Bot（后命名为 Optimus），目标先在特斯拉工厂内部署，再逐步面向企业级与消费级市场。Optimus 依托特斯拉自研执行器、电池包、FSD 视觉感知与车载级计算平台，强调规模化制造与成本控制。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Optimus 人形机器人 | 通用/工业人形 | Optimus Gen 2 / Gen 1 | 工厂搬运、分拣、未来家庭服务 |
| 自动驾驶与机器人 AI | 感知/决策软件栈 | FSD / Dojo | 车辆自动驾驶、机器人任务规划 |

## 代表产品

### Tesla Optimus Gen 2

> Tesla Optimus Gen 2：请访问 [官方资料](https://www.tesla.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 173 cm（高） | Tesla AI Day / 公开资料 |
| 重量 | 约 57 kg | Tesla 官方披露 |
| 自由度 | 躯干 28+；手部 11×2（Gen 2），Gen 3 手部升级为 22×2 | 公开资料 |
| 负载/扭矩 | 双手搬运约 20 kg | 公开演示 |
| 速度/转速 | 步行最高约 8 km/h | 第三方评测 |
| 续航 | 约 2–4 小时（视任务） | 未官方确认 |
| 接口/通信 | 专有接口，FSD 计算平台 | 官方披露 |
| 价格 | 目标零售价 20,000–30,000 USD | Musk 公开表态 |

**技术亮点**：轻量化机身、特斯拉自研线性/旋转执行器、躯干集成电池、FSD 衍生神经网络、类人双手与触觉反馈。

**应用场景**：汽车工厂电池/物料分拣、一般工业搬运、未来家庭与个人服务。


### Tesla Optimus Gen 1

> Tesla Optimus Gen 1：请访问 [官方资料](https://www.tesla.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 173 cm（高） | Tesla AI Day 2022 |
| 重量 | 约 73 kg | 公开资料 |
| 自由度 | 躯干约 28；手部 11×2 | 公开资料 |
| 负载/扭矩 | 双手搬运约 20 kg；硬拉约 68 kg | 公开演示 |
| 速度/转速 | 步行 < 2 km/h | 原型演示 |
| 续航 | 未公开 | - |
| 接口/通信 | 专有接口 | - |
| 价格 | 未公开 | - |

**技术亮点**：第一代公开原型，验证电驱关节、基础双足行走与躯干集成计算架构。

**应用场景**：实验室验证、公开演示与后续迭代基础。


## 供应链位置

- **上游关键零部件/材料**：自研执行器、电池电芯与电源管理、视觉传感器、计算芯片；部分结构件与原材料外协。
- **下游客户/应用场景**：特斯拉自有工厂、未来潜在车企/物流企业及消费级市场。
- **主要竞争对手/对标**：Figure AI、Boston Dynamics、Apptronik、1X Technologies、Agility Robotics。

## 知识图谱节点与关系

- 公司实体：`ent_company_tesla`
- 产品/平台实体：`ent_product_tesla_optimus_gen2`、`ent_product_tesla_optimus_gen1`
- 关键关系：
  - `rel_ent_company_tesla_manufactures_ent_product_tesla_optimus_gen2`（`ent_company_tesla` → `manufactures` → `ent_product_tesla_optimus_gen2`）
  - `rel_ent_company_tesla_manufactures_ent_product_tesla_optimus_gen1`（`ent_company_tesla` → `manufactures` → `ent_product_tesla_optimus_gen1`）

## 参考资料

1. [Tesla 官网](https://www.tesla.com)
2. [Tesla AI Day 2022 公开演示](https://www.tesla.com/AI)
3. [Robohuman Tesla Optimus 规格汇总](https://robohuman.org/product/tesla-optimus)