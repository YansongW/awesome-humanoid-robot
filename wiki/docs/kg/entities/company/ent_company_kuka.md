---
id: ent_company_kuka
type: company
'title:': KUKA Robotics / 库卡机器人
domain: 04_assembly_integration_testing
theoretical_depth: system
aliases:
- 库卡机器人
- KUKA
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: kuka_official
  type: website
  url: https://www.kuka.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
---





# kuka

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 库卡机器人 |
| **英文名** | KUKA Robotics |
| **总部** | 德国奥格斯堡（Augsburg） |
| **成立时间** | 1898 年 |
| **官网** | [https://www.kuka.com](https://www.kuka.com) |
| **供应链环节** | 工业机器人、协作机器人、移动机器人、自动化系统集成 |
| **企业属性** | 上市公司（原法兰克福证券交易所），现为美的集团子公司 |
| **母公司/所属集团** | 美的集团（Midea Group，2017 年收购） |
| **数据来源** | KUKA 官网、KUKA 年报、公开新闻资料 |

## 公司简介

KUKA 是全球领先的工业机器人与自动化解决方案供应商，以 orange 色六轴工业机器人、协作机器人 LBR iiwa 以及移动机器人平台著称。

KUKA 的产品覆盖汽车、电子、金属加工、物流与医疗等行业，其机器人控制器、伺服驱动与离线编程软件构成完整的自动化生态。在人形机器人产业链中，KUKA 的精密装配机器人、协作臂与数字化产线方案可为关节模组组装、整机标定与批量测试提供核心装备。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 工业机器人 | 高负载、高精度六轴机器人 | KR QUANTEC / KR AGILUS / KR CYBERTECH | 汽车、电子、金属加工 |
| 协作机器人 | 人机协作、力控安全 | LBR iiwa / iiQKA | 装配、检测、医疗 |
| 移动机器人 | 工厂物流 AMR/AGV | KMP 系列 / KMR iiwa | 仓储、半导体、汽车 |

## 代表产品

### KUKA LBR iiwa 协作机器人

> LBR iiwa：请访问 [官方资料](https://www.kuka.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 轴数 | 7 | KUKA 官网 |
| 最大负载 | 14 kg（iiwa 14）/ 7 kg（iiwa 7） | KUKA 官网 |
| 最大工作半径 | 820 mm / 1260 mm | KUKA 官网 |
| 重复定位精度 | ± 0.1 mm | KUKA 官网 |
| 机械单元重量 | 未公开 | KUKA 官网 |
| 防护等级 | IP54 | KUKA 官网 |
| 安装方式 | 地面 / 天花板 / 墙面 | KUKA 官网 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：内置关节力矩传感器，可实现顺应性控制与人机安全协作；开放式 Java 接口与 iiQKA 操作系统支持快速部署。

**应用场景**：精密装配、螺丝拧紧、抛光打磨、人形机器人零部件柔性装配与测试。

## 与人形机器人的关联

- 库卡机器人 在 工业机器人、协作机器人、移动机器人、自动化系统集成 等领域的能力，可为人形机器人零部件加工、整机装配与测试提供关键装备或基础零部件。
- 高精度运动控制、力控与自主导航技术是类人运动与操作的核心支撑。
- 该公司在 汽车 OEM 等场景的落地经验，可为人形机器人未来应用提供商业化参考。

## 供应链位置

- **上游关键零部件/材料**：伺服电机、减速器、控制器、结构件、传感器、线缆。
- **下游客户/应用场景**：汽车 OEM、电子制造商、物流仓储、医疗手术设备、自动化集成商。
- **主要竞争对手/对标**：FANUC、ABB、Yaskawa、MOTOMAN。

## 知识图谱节点与关系

- 公司实体：`ent_company_kuka`
- 产品实体：`ent_product_kuka_iiwa`
- 关键关系：
  - `ent_company_kuka` -- `manufactures` --> `ent_product_kuka_iiwa`

## 参考资料

1. [库卡机器人 官网](https://www.kuka.com)
2. [LBR iiwa 产品页](https://www.kuka.com/en-us/products/robotics-systems/industrial-robots/lbr-iiwa)
3. [公开资料与行业研报](https://www.kuka.com)