---
id: ent_component_jae_il_wx
schema_version: 1
type: component
'title:': JAE IL-WX 1.25 mm 线对板连接器
domain: 02_components
theoretical_depth: system
aliases:
- JAE IL-WX 1.25 mm 线对板连接器
status: active
sources:
- id: src_component_jae_il_wx_official
  type: website
  url: https://www.jae.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Specifications from official catalog; missing values marked as 未公开.
---





# jae_il_wx

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [日本航空电子 / JAE](../../../appendices/appendix-d/companies/company_jae.md) |
| **产品类别** | 1.25 mm 线对板连接器 |
| **发布时间** | 现役在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [JAE官网](https://www.jae.com) |

## 产品概述

JAE IL-WX 1.25 mm 线对板连接器 是 日本航空电子 面向 工业控制器、机器人内部接线、相机模块 推出的 1.25 mm 线对板连接器。该产品以标准化接口、稳定接触与高可靠性的工业级设计，满足机器人系统对信号、电源或数据连接的长期稳定需求。

## 产品图片

> JAE IL-WX 1.25 mm 线对板连接器：请访问 [官方资料](https://www.jae.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 2 – 30（可选） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP20 | 产品资料 |
| 间距 | 1.25 mm | 官方 catalog |
| 应用场景 | 工业控制器、机器人内部接线、相机模块 | 产品资料 |
| 价格 | 未公开 | 未公开 |

## 供应链位置

- **制造商**：[日本航空电子 / JAE](../../../appendices/appendix-d/companies/company_jae.md)
- **核心零部件/技术来源**：铜合金、工程塑料、电镀材料、线缆、航空级材料
- **下游应用/客户**：机器人控制板、工业相机、LiDAR 接口、编码器、通信模块。

## 知识图谱节点与关系

- 产品实体：`ent_product_jae_il_wx`
- 零部件实体：`ent_component_jae_il_wx`
- 制造商实体：`ent_company_jae`
- 关键关系：
  - `rel_ent_company_jae_manufactures_ent_product_jae_il_wx`（`ent_company_jae` → `manufactures` → `ent_product_jae_il_wx`）
  - `rel_ent_company_jae_manufactures_ent_component_jae_il_wx`（`ent_company_jae` → `manufactures` → `ent_component_jae_il_wx`）

## 应用场景

- **机器人控制板**：适配该场景的连接与布线需求。
- **工业相机**：适配该场景的连接与布线需求。
- **LiDAR 接口**：适配该场景的连接与布线需求。
- **编码器**：适配该场景的连接与布线需求。
- **通信模块。**：适配该场景的连接与布线需求。

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 品质稳定、规格齐全、全球供应 | 高端可靠 | 成本与交期优势 |
| 交付周期 | 按配置/稳定 | 中等 | 较短 |
| 服务响应 | 全球分销网络 | 中等 | 快速 |
| 价格水平 | 中高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型前确认引脚数、电流、电压、防护等级及安装空间，必要时索取官方 datasheet 与样品。
- 机器人应用需重点评估耐振动、耐弯曲、耐油及 EMC 屏蔽需求，建议进行样机验证。
- 大批量采购建议通过授权代理商或原厂确认交期、MOQ 与 RoHS/REACH 合规证明。

## 参考资料

1. [JAE官网](https://www.jae.com)
2. 产品 datasheet 与公开技术报道
3. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)