---
id: ent_product_xpeng_iron
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Iron（第一代）
  en: Iron
status: active
sources:
- id: src_xpeng_iron_official
  type: website
  url: https://www.xiaopeng.com/airobot.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Iron（第一代） / Iron

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [小鹏机器人 / XPeng Robotics](../../../appendices/appendix-d/companies/company_xpeng_robotics.md) |
| **产品类别** | 通用人形机器人 |
| **发布时间** | 2024 年 11 月（第一代）；2025 年 11 月（第二代） |
| **状态** | 量产筹备 / 计划 2026 年底规模量产 |
| **官网/来源** | [https://www.xiaopeng.com/airobot.html](https://www.xiaopeng.com/airobot.html) |

## 产品概述

小鹏汽车广州工厂 P7 生产实训、拧螺丝、整理物料、看生产表单；未来面向门店导览与商业服务。

Iron（第一代） 是 小鹏机器人 的代表产品。自研图灵 AI 芯片（40 核、3000 T 算力）、720° 鹰眼视觉、天玑 AIOS、端到端大模型+强化学习。主要规格包括：178 cm（尺寸）、70 kg（重量）、62 个主动自由度（自由度）。

## 产品图片

![Iron（第一代）](https://xps01.xiaopeng.com/cms/content/pic/2026/02-28/23-34-440349-1822507725.png)


## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 178 cm | 公开报道 |
| 重量 | 70 kg | 公开报道 |
| 自由度 | 62 个主动自由度 | 公开报道 |
| 负载/扭矩 | 手部 15 个自由度，支持触觉反馈 | 公开报道 |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | 未公开 | - |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[小鹏机器人 / XPeng Robotics](../../../appendices/appendix-d/companies/company_xpeng_robotics.md)
- **核心零部件/技术来源**：自研图灵 AI 芯片、固态电池、谐波减速器、柔性皮肤与触觉传感器；复用小鹏汽车智驾与三电供应链。
- **下游应用/客户**：小鹏汽车广州工厂 P7 生产实训、拧螺丝、整理物料、看生产表单；未来面向门店导览与商业服务。

## 知识图谱节点与关系

- 产品实体：`ent_product_xpeng_iron`
- 制造商实体：`ent_company_xpeng_robotics`
- 关键关系：
  - `rel_ent_company_xpeng_robotics_manufactures_ent_product_xpeng_iron`（`ent_company_xpeng_robotics` → `manufactures` → `ent_product_xpeng_iron`）
  - `ent_product_xpeng_iron` -- `uses` --> `ent_component_xpeng_turing_chip`

## 应用场景

- **小鹏汽车广州工厂 P7 生产实训、拧螺丝、整理物料、看生产表单；未来面向门店导览与商业服务。**
- **科研教育**：作为机器人控制、AI 训练与具身智能研究的硬件平台。
- **商业服务**：用于导览、接待、展示与品牌互动。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 |
|--------|--------|----------|
| 定位 | 通用人形机器人 | 同类产品视具体场景而定 |
| 核心优势 | 自研图灵 AI 芯片（40 核、3000 T 算力）、720° 鹰眼视觉、天玑 AIOS、端到端大模型+强化学习 | 未公开 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [小鹏 AI 机器人官网](https://www.xiaopeng.com/airobot.html)
2. [小鹏机器人量产基地新闻](https://www.xiaopeng.com/news/company_news/5537.html)
3. [华金证券 – 汽车行业周报](https://pdf.dfcfw.com/pdf/H3_AP202511111779514833_1.pdf)