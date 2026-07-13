---
id: ent_component_hirose_df13
schema_version: 1
type: component
'title:': Hirose DF13 1.25 mm 线对板连接器
domain: 02_components
theoretical_depth: system
aliases:
- Hirose DF13 1.25 mm 线对板连接器
status: active
sources:
- id: src_component_hirose_df13_official
  type: website
  url: https://www.hirose.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Specifications from official catalog; missing values marked as 未公开.
---





# hirose_df13

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [广濑电机 / Hirose Electric](../../../appendices/appendix-d/companies/company_hirose.md) |
| **产品类别** | 1.25 mm 线对板连接器 |
| **发布时间** | 现役在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [Hirose Electric官网](https://www.hirose.com) |

## 产品概述

Hirose DF13 1.25 mm 线对板连接器 是 广濑电机 面向 小型伺服、编码器、工业相机、无人机 推出的 1.25 mm 线对板连接器。该产品以标准化接口、稳定接触与高可靠性的工业级设计，满足机器人系统对信号、电源或数据连接的长期稳定需求。

## 产品图片

> Hirose DF13 1.25 mm 线对板连接器：请访问 [官方资料](https://www.hirose.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 2 – 40（可选） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP20 | 产品资料 |
| 间距 | 1.25 mm | 官方 catalog |
| 应用场景 | 小型伺服、编码器、工业相机、无人机 | 产品资料 |
| 价格 | 未公开 | 未公开 |

## 供应链位置

- **制造商**：[广濑电机 / Hirose Electric](../../../appendices/appendix-d/companies/company_hirose.md)
- **核心零部件/技术来源**：磷青铜、高性能塑料、镀金/镀锡、线缆
- **下游应用/客户**：机器人关节编码器、摄像头模组、IMU、电池 BMS、小型执行器。

## 知识图谱节点与关系

- 产品实体：`ent_product_hirose_df13`
- 零部件实体：`ent_component_hirose_df13`
- 制造商实体：`ent_company_hirose`
- 关键关系：
  - `rel_ent_company_hirose_manufactures_ent_product_hirose_df13`（`ent_company_hirose` → `manufactures` → `ent_product_hirose_df13`）
  - `rel_ent_company_hirose_manufactures_ent_component_hirose_df13`（`ent_company_hirose` → `manufactures` → `ent_component_hirose_df13`）

## 应用场景

- **机器人关节编码器**：适配该场景的连接与布线需求。
- **摄像头模组**：适配该场景的连接与布线需求。
- **IMU**：适配该场景的连接与布线需求。
- **电池 BMS**：适配该场景的连接与布线需求。
- **小型执行器。**：适配该场景的连接与布线需求。

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

1. [Hirose Electric官网](https://www.hirose.com)
2. 产品 datasheet 与公开技术报道
3. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)