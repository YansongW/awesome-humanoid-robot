# 艾利特 EC66 协作机器人

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [艾利特机器人 / Elite Robot](../companies/company_elite_robot.md) |
| **产品类别** | 协作机器人 |
| **发布时间** | 2018 年起持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.elite-robot.com](https://www.elite-robot.com) |

## 产品概述

EC66 是艾利特机器人推出的 6 自由度协作机器人，负载 6 kg、臂展 914 mm，面向工业柔性制造与科研教育。

产品采用平台化控制架构，支持拖拽示教、图形化编程、碰撞检测与开放的 ROS/ROS2 接口，强调快速二次开发与行业定制能力。

## 产品图片

> EC66：请访问 [官方资料](https://www.elite-robot.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 6-DOF 协作机器人 | 艾利特官网 |
| 自重 | 约 17.5 kg | 产品手册 |
| 负载 | 6 kg | 产品手册 |
| 臂展 | 914 mm | 产品手册 |
| 自由度 | 6 DOF | 公开规格 |
| 重复定位精度 | ±0.03 mm | 产品手册 |
| 最大末端速度 | 2.8 m/s | 产品手册 |
| 最大关节速度 | 未公开 | - |
| 防护等级 | IP54 | 产品手册 |
| 通信接口 | Ethernet / Modbus / ROS | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[艾利特机器人 / Elite Robot](../companies/company_elite_robot.md)
- **核心零部件/技术来源**：自研关节模组、谐波减速器、伺服电机、控制器、编码器、结构件。
- **下游应用/客户**：3C 电子、汽车、新能源、医疗、食品、教育科研。

## 知识图谱节点与关系

- 产品实体：`ent_product_elite_ec66`
- 制造商实体：`ent_company_elite_robot`
- 关键关系：
  - `rel_ent_company_elite_robot_manufactures_ent_product_elite_ec66`（`ent_company_elite_robot` → `manufactures` → `ent_product_elite_ec66`）

## 应用场景

- **3C 装配**：螺丝锁付、插件、检测、搬运。
- **汽车零部件检测**：柔性产线中的在线检测。
- **医疗辅具**：康复训练、手术辅助、样本处理。
- **科研教育**：机器人编程实训、人机协作研究。

## 竞争对比

| 对比项 | EC66 | 主要竞品 |
|--------|------|----------|
| 定位 | 工业/科研协作机器人 | 节卡 Zu 5、遨博 i5、大族 Elfin 5 |
| 核心优势 | 平台化架构、开放 SDK、快速定制 | 视具体型号而定 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 根据负载与臂展需求选择 EC63 / EC66 / EC75 / EC612 系列。
- 二次开发用户应优先评估 SDK、ROS 接口与社区支持。
- 建议通过艾利特官方渠道获取最新控制器固件与认证配件。

## 相关词条

- [制造商：艾利特机器人 / Elite Robot](../companies/company_elite_robot.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [艾利特机器人官网](https://www.elite-robot.com)
2. 艾利特 EC 系列产品手册
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)