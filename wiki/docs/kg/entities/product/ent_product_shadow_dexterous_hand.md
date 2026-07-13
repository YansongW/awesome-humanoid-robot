---
id: ent_product_shadow_dexterous_hand
schema_version: 1
type: product
'title:': Shadow Dexterous Hand
domain: 02_components
theoretical_depth: system
names:
  zh: Shadow Dexterous Hand
  en: Shadow Dexterous Hand
status: active
sources:
- id: src_shadow_dexterous_hand_official
  type: website
  url: https://www.shadowrobot.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Shadow Dexterous Hand / Shadow Dexterous Hand

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Shadow Robot Company / Shadow Robot Company](../../../appendices/appendix-d/companies/company_shadow_robot.md) |
| **产品类别** | 灵巧手 / 末端执行器 |
| **发布时间** | 现役主力型号 |
| **状态** | 商用/科研 |
| **官网/来源** | [Shadow Robot Company官网](https://www.shadowrobot.com) |

## 产品概述

Shadow Dexterous Hand 是 Shadow Robot Company 推出的高度仿人五指灵巧手，拥有与人类手部相近的运动学与尺寸，支持位置、力、扭矩多模式控制，是全球科研与高端遥操作领域最具影响力的灵巧手平台之一。

## 产品图片

> Shadow Dexterous Hand：请访问 [官方资料](https://www.shadowrobot.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 仿人成年男性手尺寸 | 官方规格书 |
| 重量 | 4.3 kg（含前臂） | 官方规格书 |
| 自由度 | 20 主动 + 4 被动 / 24 关节 | 官方规格书 |
| 负载 | 强力抓握 4–5 kg | 官方规格书 / 公开报道 |
| 运动速度 | 典型关节 1.0 Hz | 官方规格书 |
| 通信接口 | EtherCAT | 官方规格书 |
| 控制频率 | 位置环 1 kHz / 力矩环 5 kHz | 官方规格书 |
| 供电电压 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[Shadow Robot Company / Shadow Robot Company](../../../appendices/appendix-d/companies/company_shadow_robot.md)
- **核心零部件/技术来源**：微型电机、腱绳、力/触觉传感器、铝合金/工程塑料、EtherCAT 控制板。
- **下游应用/客户**：高校与研究机构、医疗手术、核工业、遥操作、人形机器人。

## 知识图谱节点与关系

- 零部件实体：`ent_product_shadow_dexterous_hand`
- 制造商实体：`ent_company_shadow_robot`
- 关键关系：
  - `rel_ent_company_shadow_robot_manufactures_ent_product_shadow_dexterous_hand`（`ent_company_shadow_robot` --> `manufactures` --> `ent_product_shadow_dexterous_hand`）

## 应用场景

- **科研**：抓取策略、灵巧操作、AI 算法验证
- **医疗**：手术训练、康复机器人、远程手术
- **核工业**：危险环境遥操作与维护
- **人形机器人**：高端人形平台末端执行器

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 极高自由度、成熟 ROS/EtherCAT 生态、科研标杆 | 高端精度与可靠性 | 同区间性能竞争 |
| 交付周期 | 较短/按配置 | 较长 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 极高 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载、行程、速度与精度要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行负载惯量辨识、刚性匹配与振动抑制调试，确保与整机系统兼容。

## 参考资料

1. [Shadow Robot Company官网](https://www.shadowrobot.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.shadowrobot.com)（请按实际产品型号核对）