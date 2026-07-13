---
id: ent_product_engineai_pm01
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: EngineAI PM01
  en: EngineAI PM01
status: active
sources:
- id: src_engineai_pm01_official
  type: website
  url: https://www.engineai.com.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# EngineAI PM01 / EngineAI PM01

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [众擎机器人 / EngineAI](../../../appendices/appendix-d/companies/company_engineai.md) |
| **产品类别** | 通用人形机器人 |
| **发布时间** | 2024 年底 / 2025 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.engineai.com.cn](https://www.engineai.com.cn) |

## 产品概述

科研教育算法验证、工业制造二次开发、商业展示与舞蹈表演。

EngineAI PM01 是 众擎机器人 的代表产品。全栈自研一体化关节、腰部 ＞300° 旋转、开源训练/部署代码、手持遥控、交互屏。主要规格包括：站立 1400(H)×535.55(W)×252.66(D) mm（尺寸）、商业版约 42 kg；教育版约 43 kg（重量）、商业版 23 DOF；教育版 24 DOF（自由度）。

## 产品图片

![EngineAI PM01](https://cn-engineai-1304599088.cos.ap-guangzhou.myqcloud.com/uploads/upload/images/20251029/668bd44456c24b778a8c7d824e42d858.png)


## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 站立 1400(H)×535.55(W)×252.66(D) mm | EngineAI 官网 |
| 重量 | 商业版约 42 kg；教育版约 43 kg | EngineAI 官网 |
| 自由度 | 商业版 23 DOF；教育版 24 DOF | EngineAI 官网 |
| 负载/扭矩 | 膝关节峰值扭矩 145 N·m（Q90H 电机） | EngineAI 官网 |
| 速度/转速 | 移动速度 ＞2 m/s（硬件支持） | EngineAI 官网 |
| 续航 | 约 2 小时（10000 mAh 快拆电池） | EngineAI 官网 |
| 接口/通信 | 教育版支持二次开发，搭载 NVIDIA Jetson Orin NX (16G) | EngineAI 官网 |
| 价格 | 商用版 8.8 万元（含税） | 官方 FAQ |

## 供应链位置

- **制造商**：[众擎机器人 / EngineAI](../../../appendices/appendix-d/companies/company_engineai.md)
- **核心零部件/技术来源**：自研 Q90H/Q25H 一体化关节电机、行星/谐波减速器、电机；Intel RealSense、NVIDIA Jetson、电池。
- **下游应用/客户**：科研教育算法验证、工业制造二次开发、商业展示与舞蹈表演。

## 知识图谱节点与关系

- 产品实体：`ent_product_engineai_pm01`
- 制造商实体：`ent_company_engineai`
- 关键关系：
  - `rel_ent_company_engineai_manufactures_ent_product_engineai_pm01`（`ent_company_engineai` → `manufactures` → `ent_product_engineai_pm01`）
  - `ent_product_engineai_pm01` -- `uses` --> `ent_component_engineai_q90h`

## 应用场景

- **科研教育算法验证、工业制造二次开发、商业展示与舞蹈表演。**
- **工业制造**：在柔性产线执行搬运、装配、检测等任务。
- **商业服务**：用于导览、接待、展示与品牌互动。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 |
|--------|--------|----------|
| 定位 | 通用人形机器人 | 同类产品视具体场景而定 |
| 核心优势 | 全栈自研一体化关节、腰部 ＞300° 旋转、开源训练/部署代码、手持遥控、交互屏 | 未公开 |
| 价格 | 商用版 8.8 万元（含税） | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [EngineAI PM01 产品页](https://www.engineai.com.cn/product-pm01.html)
2. [EngineAI SE01 产品页](https://en.engineai.com.cn/product-se01)
3. [众擎机器人 FAQ](https://www.engineai.com.cn/about-news-media/23.html)