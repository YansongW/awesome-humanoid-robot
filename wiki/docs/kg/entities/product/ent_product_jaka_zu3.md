---
id: ent_product_jaka_zu3
schema_version: 1
type: product
'title:': Jaka Zu 3 协作机器人
domain: 04_assembly_integration_testing
theoretical_depth: system
names:
  zh: Jaka Zu 3 协作机器人
  en: Jaka Zu 3 Collaborative Robot
status: active
sources:
- id: src_jaka_zu3_official
  type: website
  url: https://www.jaka.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Jaka Zu 3 协作机器人 / Jaka Zu 3 Collaborative Robot

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [节卡机器人 / Jaka](../../../appendices/appendix-d/companies/company_jaka.md) |
| **产品类别** | 协作机器人 |
| **发布时间** | 2017 年起持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.jaka.com](https://www.jaka.com) |

## 产品概述

Jaka Zu 3 是节卡机器人推出的桌面型 6 自由度协作机器人，面向 3C、汽车、食品、医疗等柔性制造场景。

产品以无线示教、图形化编程、IP54 防护和±0.02 mm 重复定位精度为核心卖点，适合人机共线与小批量多品种生产。

## 产品图片

> Jaka Zu 3：请访问 [官方资料](https://www.jaka.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 6-DOF 桌面型协作机器人 | 节卡官网 |
| 自重 | 约 12 kg | 产品手册 |
| 负载 | 3 kg | 产品手册 |
| 臂展 | 626 mm | 产品手册 |
| 自由度 | 6 DOF | 公开规格 |
| 重复定位精度 | ±0.02 mm | 产品手册 |
| 最大末端速度 | 2.3 m/s | 产品手册 |
| 最大关节速度 | 180°/s（参考） | 产品手册 |
| 防护等级 | IP54 | 产品手册 |
| 通信接口 | Ethernet / Modbus / ROS | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[节卡机器人 / Jaka](../../../appendices/appendix-d/companies/company_jaka.md)
- **核心零部件/技术来源**：自研关节模组、谐波减速器、伺服电机、控制器、编码器、结构件。
- **下游应用/客户**：3C 电子、汽车零部件、食品医疗、科研教育、人形机器人整机厂。

## 知识图谱节点与关系

- 产品实体：`ent_product_jaka_zu3`
- 制造商实体：`ent_company_jaka`
- 关键关系：
  - `rel_ent_company_jaka_manufactures_ent_product_jaka_zu3`（`ent_company_jaka` → `manufactures` → `ent_product_jaka_zu3`）
  - `ent_product_jaka_k1` -- `uses` --> `ent_product_jaka_zu3`

## 应用场景

- **3C 装配**：螺丝锁付、插件、检测、贴标。
- **汽车零部件**：小型工件上下料、精密检测。
- **食品医疗**：包装、分拣、样本处理。
- **科研教育**：机器人编程实训、人机协作研究。

## 竞争对比

| 对比项 | Jaka Zu 3 | 主要竞品 |
|--------|-----------|----------|
| 定位 | 桌面级协作机器人 | 同类产品视场景而定 |
| 核心优势 | 无线示教、图形化编程、IP54 | 遨博 i3、大族 Elfin 3 等 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 根据负载与臂展需求选择 Zu 3 / Zu 5 / Zu 7 / Zu 12 / Zu 18 系列。
- 确认末端执行器、视觉系统与节卡控制器的接口兼容性。
- 建议通过官方渠道获取最新示教器固件与 SDK 文档。

## 相关词条

- [制造商：节卡机器人 / Jaka](../../../appendices/appendix-d/companies/company_jaka.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [节卡机器人官网](https://www.jaka.com)
2. 节卡 Zu 系列产品手册
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)