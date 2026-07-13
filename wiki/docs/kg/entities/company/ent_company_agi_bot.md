---
id: ent_company_agi_bot
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 智元机器人
  en: AgiBot
status: active
sources:
- id: src_agi_bot_official
  type: website
  url: https://www.zhiyuan-robot.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 智元机器人 / AgiBot

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 智元机器人（智元创新） |
| **英文名** | AgiBot |
| **总部** | 中国上海 |
| **成立时间** | 2023 年 |
| **官网** | [https://www.zhiyuan-robot.com](https://www.zhiyuan-robot.com) |
| **供应链环节** | 整机 OEM / 通用人形机器人 |
| **企业属性** | 初创独角兽、具身智能赛道头部 |
| **母公司/所属集团** | 无 |
| **数据来源** | 智元官网、IT之家、Robothub、公开报道 |

## 公司简介

智元机器人由“稚晖君”彭志辉等人创立，定位为“以智能机器创造无限生产力”的具身智能公司。

公司快速迭代远征（Expedition）系列人形机器人，强调多模态交互、企业知识库与规模化商用，并在 2025 年宣布远征 A2 成为全球首个同时获得中、美、欧四项认证的人形机器人。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 交互服务 | 展厅讲解、迎宾、商演 | 远征 A2 / A2 青春版 | 展厅、商超、演艺 |
| 柔性智造 | 轮式移动操作 | 远征 A2-W | 工厂搬运、装配 |
| 重载特种 | 高负载工业场景 | 远征 A2-Max | 重载物流 |

## 代表产品

### 远征 A2

> 智元 远征 A2：请访问 [官方资料](https://www.zhiyuan-robot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 169–170 cm | 多家媒体报道 |
| 重量 | 约 69 kg | IT之家 |
| 自由度 | 40+ DOF | 官方宣传 |
| 负载/扭矩 | 单臂最大负载 5 kg | 官网参数页 |
| 速度/转速 | 最大行走 1.2 m/s（V1.3 OTA 后） | IT之家 |
| 续航 | 约 2 h（700 Wh 电池） | 公开报道 |
| 接口/通信 | 未公开 | - |
| 价格 | 未公开 | 需询价 |

**技术亮点**：具身智脑 EI-Brain、端侧多模态大模型、PLd 级安全防护、中美欧四项认证。

**应用场景**：汽车展厅销售顾问、商超导览、晚会商演、前台接待。

### 远征 A2 青春版

> 智元 远征 A2 青春版：请访问 [官方资料](https://www.zhiyuan-robot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 169 cm | Robothub |
| 重量 | 64 kg | Robothub |
| 自由度 | 23 DOF | Robothub |
| 负载/扭矩 | 双臂负载 4 kg | Robothub |
| 速度/转速 | 2.88 km/h | Robothub |
| 续航 | 4.5 h | Robothub |
| 接口/通信 | 未公开 | - |
| 价格 | 约 19.8 万元 | Robothub |

**技术亮点**：面向文娱商演的全尺寸演绎平台，支持群控、VR 遥操与二次创作。

**应用场景**：商业演出、活动引流、IP 定制。

## 供应链位置

- **上游关键零部件/材料**：自研关节与灵巧手，外购电机、减速器、电池、激光雷达、摄像头。
- **下游客户/应用场景**：汽车主机厂、商超、文旅、智能制造工厂。
- **主要竞争对手/对标**：优必选 Walker A2、傅利叶 GR-3、银河通用 Galbot。

## 知识图谱节点与关系

- 公司实体：`ent_company_agi_bot`
- 产品实体：`ent_product_agi_bot_a2`、`ent_product_agi_bot_a2_lite`
- 关键关系：
  - `ent_company_agi_bot` -- `manufactures` --> `ent_product_agi_bot_a2`
  - `ent_company_agi_bot` -- `manufactures` --> `ent_product_agi_bot_a2_lite`
  - `ent_product_agi_bot_a2` -- `uses` --> `ent_component_lidar`

## 参考资料

1. [智元机器人官网](https://www.zhiyuan-robot.com)
2. [IT之家 – 远征 A2 发布与 OTA 报道](https://www.ithome.com/0/788/620.htm)
3. [Robothub – 远征 A2 青春版](https://www.robothub.app/zh/robots/expedition-a2-lite)
4. [知乎 – 远征 A2 中美欧认证](https://zhuanlan.zhihu.com/p/1911481259995168918)
5. [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)