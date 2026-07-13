# Han's Robot Elfin 5 协作机器人

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [大族机器人 / Han's Robot](../companies/company_hans_robot.md) |
| **产品类别** | 协作机器人 |
| **发布时间** | 2018 年起持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.hansrobot.com](https://www.hansrobot.com) |

## 产品概述

Elfin 5 是大族机器人推出的 6 自由度协作机器人，负载 5 kg、臂展 950 mm，面向工业柔性制造与商业服务。

产品采用双关节模块化设计，继承了大族激光在精密制造领域的经验，强调易用性、安全性和开放生态，支持拖拽示教与图形化编程。

## 产品图片

> Elfin 5：请访问 [官方资料](https://www.hansrobot.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 6-DOF 协作机器人 | 大族机器人官网 |
| 自重 | 约 24 kg | 产品手册 |
| 负载 | 5 kg | 产品手册 |
| 臂展 | 950 mm | 产品手册 |
| 自由度 | 6 DOF | 公开规格 |
| 重复定位精度 | ±0.03 mm | 产品手册 |
| 最大末端速度 | 未公开 | - |
| 最大关节速度 | 未公开 | - |
| 防护等级 | IP54 | 产品手册 |
| 通信接口 | Ethernet / Modbus / ROS | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[大族机器人 / Han's Robot](../companies/company_hans_robot.md)
- **核心零部件/技术来源**：自研双关节模组、谐波减速器、伺服电机、控制器、编码器、结构件。
- **下游应用/客户**：3C 电子、汽车、新能源、医疗、食品、金属加工。

## 知识图谱节点与关系

- 产品实体：`ent_product_hans_elfin5`
- 制造商实体：`ent_company_hans_robot`
- 关键关系：
  - `rel_ent_company_hans_robot_manufactures_ent_product_hans_elfin5`（`ent_company_hans_robot` → `manufactures` → `ent_product_hans_elfin5`）

## 应用场景

- **3C 装配**：螺丝锁付、插件、检测、搬运。
- **汽车零部件上下料**：柔性产线中的小工件取放。
- **医疗样本处理**：实验室自动化、样本分拣。
- **食品包装**：分拣、装箱、码垛。

## 竞争对比

| 对比项 | Elfin 5 | 主要竞品 |
|--------|---------|----------|
| 定位 | 工业/商业协作机器人 | 节卡 Zu 5、遨博 i5、艾利特 EC66 |
| 核心优势 | 双关节模块化、大族制造体系 | 视具体型号而定 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 根据负载与臂展需求选择 Elfin 3 / 5 / 10 / 10L 系列。
- 确认末端执行器、视觉系统与大族控制器的接口兼容性。
- 建议通过大族机器人官方渠道获取最新固件与技术支持。

## 相关词条

- [制造商：大族机器人 / Han's Robot](../companies/company_hans_robot.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [大族机器人官网](https://www.hansrobot.com)
2. 大族机器人 Elfin 系列产品手册
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)