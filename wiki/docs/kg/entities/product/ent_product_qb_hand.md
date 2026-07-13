---
id: ent_product_qb_hand
schema_version: 1
type: product
'title:': qb SoftHand 五指软体灵巧手
domain: 02_components
theoretical_depth: system
names:
  zh: qb SoftHand 五指软体灵巧手
  en: qb SoftHand 5-Finger Soft Robotic Hand
status: active
sources:
- id: src_qb_hand_official
  type: website
  url: https://qbrobotics.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# qb SoftHand 五指软体灵巧手 / qb SoftHand 5-Finger Soft Robotic Hand

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [qb Soft Robotics / qb Soft Robotics](../../../appendices/appendix-d/companies/company_qb_robotics.md) |
| **产品类别** | 软体灵巧手 / 末端执行器 |
| **发布时间** | 现役型号 |
| **状态** | 商用/科研 |
| **官网/来源** | [qb Soft Robotics官网](https://qbrobotics.com) |

## 产品概述

qb SoftHand 是 qbrobotics 推出的基于软体机器人技术的五指灵巧手，采用单电机腱驱动与 19 个软体关节协同，通过机械自适应性抓取不同形状物体，具有重量轻、负载自重比高、安全人机交互等特点。

## 产品图片

> qb SoftHand 五指软体灵巧手：请访问 [官方资料](https://qbrobotics.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 1:1 仿人手，具体未公开 | 公开资料 |
| 重量 | 500 g | 公开资料 |
| 手指数 | 5 | 公开资料 |
| 自由度 | 19 关节 / 1 主动协同（单电机） | 公开资料 |
| 指尖捏紧力 | 62 N | 公开资料 |
| 额定负载 | 1.7 kg（捏紧状态） | 公开资料 |
| 张手到握拳 | 1.1 s | 公开资料 |
| 通信接口 | USB / RS485 | 公开资料 |
| 兼容性 | ROS、UR+ 认证 | 公开资料 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[qb Soft Robotics / qb Soft Robotics](../../../appendices/appendix-d/companies/company_qb_robotics.md)
- **核心零部件/技术来源**：弹性体材料、肌腱/软驱动、电机、传感器、3D 打印结构件。
- **下游应用/客户**：高校、研究机构、协作机器人厂商、医疗康复、工业测试。

## 知识图谱节点与关系

- 零部件实体：`ent_product_qb_hand`
- 制造商实体：`ent_company_qb_robotics`
- 关键关系：
  - `rel_ent_company_qb_robotics_manufactures_ent_product_qb_hand`（`ent_company_qb_robotics` --> `manufactures` --> `ent_product_qb_hand`）

## 应用场景

- **科研**：软体抓取、协同控制、人机交互研究
- **教育**：机器人教学、演示与竞赛
- **协作机器人**：柔性末端执行器、安全共线作业
- **医疗康复**：假肢、康复辅具、人机交互

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 软体自适应、单电机易控、轻量高负载、安全 | 高端精度与可靠性 | 同区间性能竞争 |
| 交付周期 | 较短/按配置 | 较长 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 中高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载、行程、速度与精度要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行负载惯量辨识、刚性匹配与振动抑制调试，确保与整机系统兼容。

## 参考资料

1. [qb Soft Robotics官网](https://qbrobotics.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://qbrobotics.com)（请按实际产品型号核对）