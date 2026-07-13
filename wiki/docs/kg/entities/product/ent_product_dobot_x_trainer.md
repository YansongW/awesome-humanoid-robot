---
id: ent_product_dobot_x_trainer
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Dobot X-Trainer
  en: Dobot X-Trainer
status: active
sources:
- id: src_dobot_x_trainer_official
  type: website
  url: https://www.dobot.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Dobot X-Trainer / Dobot X-Trainer

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [越疆科技 / Dobot / Yuejiang Technology](../../../appendices/appendix-d/companies/company_dobot.md) |
| **产品类别** | 双臂遥操作 AI 训练平台 |
| **发布时间** | 2024 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.dobot.cn](https://www.dobot.cn) |

## 产品概述

具身智能数据采集、模仿学习、科研教育、AGI 场景仿真与竞赛。

Dobot X-Trainer 是 越疆科技 的代表产品。工业级 Nova 2 协作臂从手、±0.05 mm 重复定位精度、25 Hz 端到端运动接口、VR/手柄遥操作、数据采集 SDK。主要规格包括：底座 1400×1000 mm（轻量版，不含把手）（尺寸）、未公开（重量）、主手 6-DOF×2，从手 Nova 2 协作臂×2（自由度）。

## 产品图片

![Dobot X-Trainer](https://www.dobot-robots.com/media/upload/2024/x-trainer/tab.png)


## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 底座 1400×1000 mm（轻量版，不含把手） | Dobot X-Trainer 用户手册 |
| 重量 | 未公开 | - |
| 自由度 | 主手 6-DOF×2，从手 Nova 2 协作臂×2 | 用户手册 |
| 负载/扭矩 | 单臂可搬 2 kg，双臂 3 kg；夹爪最大行程 95 mm | 宣传册 |
| 速度/转速 | 末端最高速度 1.6 m/s | 宣传册 |
| 续航 | 市电供电 | - |
| 接口/通信 | 千兆网口、USB、WiFi（Nova 2 选配） | 用户手册 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[越疆科技 / Dobot / Yuejiang Technology](../../../appendices/appendix-d/companies/company_dobot.md)
- **核心零部件/技术来源**：自研协作机器人关节、电机、减速器、控制器；Intel RealSense D405 深度相机；NVIDIA Jetson 算力平台。
- **下游应用/客户**：具身智能数据采集、模仿学习、科研教育、AGI 场景仿真与竞赛。

## 知识图谱节点与关系

- 产品实体：`ent_product_dobot_x_trainer`
- 制造商实体：`ent_company_dobot`
- 关键关系：
  - `rel_ent_company_dobot_manufactures_ent_product_dobot_x_trainer`（`ent_company_dobot` → `manufactures` → `ent_product_dobot_x_trainer`）
  - `ent_product_dobot_x_trainer` -- `uses` --> `ent_component_dobot_nova2`

## 应用场景

- **具身智能数据采集、模仿学习、科研教育、AGI 场景仿真与竞赛。**

## 竞争对比

| 对比项 | 本产品 | 主要竞品 |
|--------|--------|----------|
| 定位 | 双臂遥操作 AI 训练平台 | 同类产品视具体场景而定 |
| 核心优势 | 工业级 Nova 2 协作臂从手、±0.05 mm 重复定位精度、25 Hz 端到端运动接口、VR/手柄遥操作、数据采集 SDK | 未公开 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [Dobot X-Trainer 产品页](https://www.dobot-robots.com/products/humanoid-robots/x-trainer.html)
2. [Dobot X-Trainer 宣传册](https://www.roscomponents.com/wp-content/uploads/2026/02/X-Trainer-leaflet-Lightweight-Base_Brochure.pdf)
3. [越疆科技官网](https://www.dobot.cn)