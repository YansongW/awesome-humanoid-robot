# Agility Robotics / Agility Robotics

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Agility Robotics |
| **英文名** | Agility Robotics |
| **总部** | 美国俄勒冈州塞勒姆（RoboFab 所在地） |
| **成立时间** | 2015 |
| **官网** | [https://agilityrobotics.com](https://agilityrobotics.com) |
| **供应链环节** | 物流人形机器人整机厂、RaaS |
| **企业属性** | 初创公司 |
| **母公司/所属集团** | 无 |
| **数据来源** | Agility Robotics 官网、Digit 产品页、公开部署报道 |

## 公司简介

Agility Robotics 是商业化部署人形机器人的先行者，Digit 已在亚马逊、GXO 等仓库执行真实搬运任务。

Digit 专为物流场景设计，采用反向膝关节优化行走与搬运效率；配套 Agility Arc 云平台实现远程监控与车队管理。公司在塞勒姆建有 RoboFab 人形机器人制造工厂。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Digit 人形机器人 | 物流仓储人形 | Digit 当前代 / 下一代 | 仓库分拣、搬运、卡车装卸 |
| Agility Arc | 云端机器人管理平台 | Agility Arc | 车队监控、任务调度、数据分析 |

## 代表产品

### Agility Robotics Digit（当前代）

> Agility Robotics Digit（当前代）：请访问 [官方资料](https://agilityrobotics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 175 cm（高） | 公开资料 |
| 重量 | 约 63–65 kg | 公开资料 |
| 自由度 | 全身 28；手臂/手部为物流定制夹具 | 公开资料 |
| 负载/扭矩 | 约 16 kg | 公开资料 |
| 速度/转速 | 约 5.4 km/h | 公开资料 |
| 续航 | 约 4 小时（任务相关） | 公开资料 |
| 接口/通信 | LiDAR、Intel RealSense 深度相机、IMU、Agility Arc | 官方披露 |
| 价格 | RaaS 租赁 / 约 250,000 USD 起 | 第三方报价 |

**技术亮点**：反向膝关节优化行走、专为 tote/纸箱搬运设计、LiDAR + 深度相机 360° 感知、已在亚马逊/GXO 仓库部署。

**应用场景**：仓库货物搬运、卡车装卸、重复性物流作业。


### Agility Robotics Digit（下一代）

> Agility Robotics Digit（下一代）：请访问 [官方资料](https://agilityrobotics.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 175 cm（高） | 公开报道 |
| 重量 | 约 63.5 kg | 公开报道 |
| 自由度 | 30+ | 公开报道 |
| 负载/扭矩 | 约 22.6 kg（50 lbs） | 公开报道 |
| 速度/转速 | 未公开 | - |
| 续航 | 改进中（未公开具体数值） | - |
| 接口/通信 | Agility Arc | - |
| 价格 | 未公开 | - |

**技术亮点**：在现有 Digit 基础上提升负载与上肢灵活性，继续面向物流规模化部署。

**应用场景**：高负载仓储搬运、更复杂的物流任务。


## 供应链位置

- **上游关键零部件/材料**：Intel RealSense 深度相机、电机/驱动、结构件、电池与计算模块。
- **下游客户/应用场景**：Amazon、GXO Logistics、Mercado Libre 等物流与零售企业。
- **主要竞争对手/对标**：Tesla Optimus、Apptronik Apollo、Boston Dynamics Stretch。

## 知识图谱节点与关系

- 公司实体：`ent_company_agility_robotics`
- 产品/平台实体：`ent_product_agility_robotics_digit`、`ent_product_agility_robotics_digit_next_gen`
- 关键关系：
  - `rel_ent_company_agility_robotics_manufactures_ent_product_agility_robotics_digit`（`ent_company_agility_robotics` → `manufactures` → `ent_product_agility_robotics_digit`）
  - `rel_ent_company_agility_robotics_manufactures_ent_product_agility_robotics_digit_next_gen`（`ent_company_agility_robotics` → `manufactures` → `ent_product_agility_robotics_digit_next_gen`）

## 参考资料

1. [Agility Robotics 官网](https://agilityrobotics.com)
2. [RoboZaps Agility Digit Review](https://blog.robozaps.com/b/agility-robotics-digit-review)
3. [Humanoid.guide Digit 规格](https://humanoid.guide/product/digit/)