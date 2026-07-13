---
id: ent_company_bmw
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 宝马集团
  en: BMW Group
status: active
sources:
- id: src_bmw_group
  type: website
  url: https://www.bmwgroup.com
- id: src_bmw_virtual_factory
  type: website
  url: https://www.automotiveworld.com/news-releases/bmw-group-scales-virtual-factory/
- id: src_bmw_figure03
  type: website
  url: https://interestingengineering.com/ai-robotics/bmw-figure-03-humanoid-robot-smart-factory-us
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 宝马集团 / BMW Group

## 概述

宝马集团（BMW Group）是总部位于德国慕尼黑的跨国汽车制造商，旗下拥有 BMW、MINI 与 Rolls-Royce 品牌。集团在 31 个国家拥有约 31 家工厂，年销量约 250 万辆汽车，是全球工业机器人与人形机器人技术的重要终端用户之一，通过 iFACTORY 战略推进数字化、精益与绿色制造。

## 工作原理 / 技术架构

宝马集团的生产体系以 iFACTORY 为核心，强调“精益、绿色、数字化”。其 Virtual Factory 基于 NVIDIA Omniverse 构建全球 30 余家工厂的数字孪生，将建筑、设备、物流与车辆数据实时关联，实现产线布局、机器人运动与物流系统的虚拟优化。AIQX 平台利用摄像头、传感器与 AI 进行视觉/声学质检，实时反馈给产线工人。Physical AI 战略则引入 Figure 02/03、AEON 等人形机器人，辅助完成重复性、 ergonomically challenging 或安全关键的任务。

## 关键参数表

| 项目 | 数值 | 备注/来源 |
|------|------|-----------|
| 总部 | 德国慕尼黑 | BMW Group |
| 成立 | 1916 年（BMW AG）/ 1928 年开始汽车制造 | BMW Group |
| 年销量 | 约 250 万辆汽车（集团） | Device Chronicle |
| 日产量 | 约 10,000 辆 | Device Chronicle |
| 车型数量 | 约 40 款，平均 100 项选装配置 | Device Chronicle |
| 全球工厂 | 31 家 | Device Chronicle |
| 供应商 | 约 1,800 家 | Device Chronicle |
| 零件号数量 | 230,000 个 | Device Chronicle |
| 生产节拍 | 约每 56 秒一辆车 | Device Chronicle |
| 生产战略 | iFACTORY（精益、绿色、数字化） | BMW Group |
| Virtual Factory | 30+ 工厂数字孪生；规划成本预计降低 30% | BMW Group |
| 人形机器人试点 | Figure 02/03（美国 Spartanburg）、AEON（德国 Leipzig） | 新闻报道 |

## 应用场景

- 汽车整车冲压、焊装、涂装、总装
- 生产物流排序与物料搬运
- AI 驱动的视觉/声学质量检测
- 人机协作装配与人形机器人试点

## 供应链关系

宝马集团作为整车 OEM 处于汽车与机器人产业链的终端应用层。上游包括动力总成、底盘、电子电气、机器人本体及视觉/控制零部件供应商；下游为经销商网络与终端消费者。在人形机器人/具身智能领域，宝马集团是机器人技术的采购方与场景验证方，与 Figure AI、Hexagon 等人形机器人厂商合作。在知识图谱中，`ent_company_bmw` 作为公司节点，通过 `uses`/`purchases` 等关系与机器人零部件及整机实体相连。

## 来源与验证

- [BMW Group Official](https://www.bmwgroup.com)
- [BMW Group Virtual Factory](https://www.automotiveworld.com/news-releases/bmw-group-scales-virtual-factory/)
- [BMW deploys Figure 03 humanoid robot](https://interestingengineering.com/ai-robotics/bmw-figure-03-humanoid-robot-smart-factory-us)