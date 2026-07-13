---
id: ent_company_fanuc
type: company
'title:': FANUC Corporation / 发那科
domain: 04_assembly_integration_testing
theoretical_depth: system
aliases:
- 发那科
- FANUC
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: fanuc_official
  type: website
  url: https://www.fanuc.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
---





# fanuc

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 发那科株式会社 |
| **英文名** | FANUC Corporation |
| **总部** | 日本山梨县忍野村 |
| **成立时间** | 1972 年（从富士通数控部门拆分） |
| **官网** | [https://www.fanuc.com](https://www.fanuc.com) |
| **供应链环节** | 工业机器人、CNC 数控系统、伺服电机、工厂自动化 |
| **企业属性** | 上市公司（东京证券交易所：6954） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | FANUC 官网、FANUC America 产品页、公开规格 |

## 公司简介

FANUC 是全球最大的工业机器人制造商之一，以高可靠性、高精度和高速度著称，业务涵盖工业机器人、CNC 数控系统和工厂自动化解决方案。

FANUC 机器人广泛应用于汽车、电子、金属加工和食品行业。其伺服控制与运动控制技术是机器人关节驱动与整机装配线自动化的核心能力，可为人形机器人量产阶段的机加工、装配与测试提供关键装备。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 工业机器人 | 多关节搬运/装配机器人 | M-20iD / R-2000iC / LR Mate | 汽车、电子、物流 |
| 协作机器人 | 人机协作 | CRX 系列 | 装配、检测 |
| CNC 与伺服 | 数控系统与伺服驱动 | FANUC CNC / SERVO | 机床、自动化 |

## 代表产品

### FANUC M-20iD/35 工业机器人

![M-20iD/35](https://www.fanucamerica.com/products/robot/m-20id-35)


| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 轴数 | 6 | FANUC America |
| 最大负载 | 35 kg | FANUC America |
| 最大工作半径 | 1831 mm | FANUC America |
| 重复定位精度 | ± 0.03 mm | FANUC America |
| 机械单元重量 | 250 kg | FANUC America |
| 防护等级 | IP54（标准） | FANUC America |
| 安装方式 | 地面 / 倾斜 / 倒挂 | FANUC America |
| 价格 | 未公开 | 未公开 |

**技术亮点**：中空手臂与手腕设计，内置电缆走线，减少干涉；高轴速与高重复精度，适合紧凑单元中的搬运与装配。

**应用场景**：机床上下料、汽车零部件装配、人形机器人零部件加工与组装产线。

## 与人形机器人的关联

- 电池、功率半导体与先进材料是人形机器人实现长续航、高动态与轻量化的共性基础。
- 工业机器人与自动化产线为人形机器人整机装配、测试与量产提供可复用的制造能力。

## 供应链位置

- **上游关键零部件/材料**：伺服电机、减速器、控制器、结构件、传感器。
- **下游客户/应用场景**：汽车 OEM、电子制造商、机床厂、自动化集成商。
- **主要竞争对手/对标**：ABB、KUKA、Yaskawa、MOTOMAN。

## 知识图谱节点与关系

- 公司实体：`ent_company_fanuc`
- 产品实体：`ent_product_fanuc_m20id_35`
- 关键关系：
  - `ent_company_fanuc` -- `manufactures` --> `ent_product_fanuc_m20id_35`

## 参考资料

1. [FANUC 官网](https://www.fanuc.com)
2. [FANUC America M-20iD/35 产品页](https://www.fanucamerica.com/products/robot/m-20id-35)
3. [FANUC M-20iD/25 规格书](https://www.robots.com/images/robots/Fanuc/M-Series/Fanuc_M-120iD_25_Datasheet.pdf)