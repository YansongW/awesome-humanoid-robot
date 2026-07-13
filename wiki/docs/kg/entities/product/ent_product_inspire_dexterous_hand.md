---
id: ent_product_inspire_dexterous_hand
schema_version: 1
type: product
'title:': RH56DFX 系列灵巧手
domain: 02_components
theoretical_depth: system
names:
  zh: RH56DFX 系列灵巧手
  en: Inspire RH56DFX Dexterous Hand
status: active
sources:
- id: src_inspire_rh56dfx_dexterous_hand_official
  type: website
  url: https://www.inspiterobots.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# RH56DFX 系列灵巧手 / Inspire RH56DFX Dexterous Hand

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [因时机器人 / Inspire Robots](../../../appendices/appendix-d/companies/company_inspire_robots.md) |
| **产品类别** | 灵巧手 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [因时机器人官网](https://www.inspiterobots.com) |

## 产品概述

高自由度、一体化微型驱动单元、可扩展触觉与力控，适配人形机器人精细操作。该系列产品由因时机器人推出，主要面向灵巧手 / 微型线性执行器 / 关节模组市场，具有6 主动 + 6 被动 / 11 主动（可选）等核心参数，适用于机器人、自动化设备及精密传动场景。

作为因时机器人的代表产品之一，RH56DFX 系列灵巧手在人形机器人、假肢等领域具有广泛应用。产品采用成熟制造工艺，可根据客户需求提供定制化接口、出线方式与控制协议。

## 产品图片

> RH56DFX 系列灵巧手：请访问 [官方资料](https://www.inspiterobots.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 230×85×35 mm（手掌） | 产品手册 |
| 重量 | 约 480 g | 产品手册 |
| 自由度 | 6 主动 + 6 被动 / 11 主动（可选） | 产品手册 |
| 负载 | 单指 1.5 kg（指尖） | 产品手册 |
| 运动速度 | 关节 180°/s | 产品手册 |
| 供电电压 | DC 24 V | 产品手册 |
| 通信接口 | CAN / RS485 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[因时机器人 / Inspire Robots](../../../appendices/appendix-d/companies/company_inspire_robots.md)
- **核心零部件/技术来源**：微型电机、滚珠丝杠、轴承、驱动 IC、触觉传感器、结构件。
- **下游应用/客户**：人形机器人整机厂、假肢厂商、服务机器人公司、科研机构。

## 知识图谱节点与关系

- 零部件实体：`ent_product_inspire_dexterous_hand`
- 制造商实体：`ent_company_inspire_robots`
- 关键关系：
  - `rel_ent_company_inspire_robots_manufactures_ent_product_inspire_dexterous_hand`（`ent_company_inspire_robots` --> `manufactures` --> `ent_product_inspire_dexterous_hand`）

## 应用场景

- **机器人**：人形机器人操作、假肢、服务机器人抓取、工业质检。
- **工业自动化**：精密定位、传动与控制执行机构。
- **医疗与消费电子**：便携式设备、医疗器械驱动单元。
- **新能源与汽车**：电动执行器、热管理与智能座舱部件。

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 本土化供应、性价比、定制化 | 高端精度与可靠性 | 同区间性能竞争 |
| 交付周期 | 较短 | 较长 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 中低端至中高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载、行程、速度与精度要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行负载惯量辨识、刚性匹配与振动抑制调试，确保与整机系统兼容。

## 参考资料

1. [因时机器人官网](https://www.inspiterobots.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）