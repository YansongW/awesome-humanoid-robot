---
id: ent_component_leoni_dacar_302
schema_version: 1
type: component
'title:': LEONI Dacar® 302 汽车以太网电缆
domain: 02_components
theoretical_depth: system
aliases:
- LEONI Dacar® 302 汽车以太网电缆
status: active
sources:
- id: src_component_leoni_dacar_302_official
  type: website
  url: https://www.leoni.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Specifications from official catalog; missing values marked as 未公开.
---





# leoni_dacar_302

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [莱尼 / LEONI](../../../appendices/appendix-d/companies/company_leoni.md) |
| **产品类别** | 单对以太网数据电缆 |
| **发布时间** | 现役在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [LEONI官网](https://www.leoni.com) |

## 产品概述

LEONI Dacar® 302 汽车以太网电缆 是 莱尼 面向 车载/机器人传感器网络、摄像头、LiDAR 推出的 单对以太网数据电缆。该产品以标准化接口、稳定接触与高可靠性的工业级设计，满足机器人系统对信号、电源或数据连接的长期稳定需求。

## 产品图片

> LEONI Dacar® 302 汽车以太网电缆：请访问 [官方资料](https://www.leoni.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 芯线数 | 1 对（2 芯） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 传输速率 | 100 Mbps（100BASE-T1） | 官方 catalog |
| 耐温范围 | -40°C ~ +105°C | 官方 catalog |
| 屏蔽 | 整体屏蔽 | 产品资料 |
| 应用场景 | 车载/机器人传感器网络、摄像头、LiDAR | 产品资料 |
| 价格 | 未公开 | 未公开 |

## 供应链位置

- **制造商**：[莱尼 / LEONI](../../../appendices/appendix-d/companies/company_leoni.md)
- **核心零部件/技术来源**：铜杆、PVC/TPE/PUR 绝缘材料、铝箔/编织屏蔽、连接器
- **下游应用/客户**：自动驾驶/机器人传感器总线、工业相机、LiDAR、域控制器互联。

## 知识图谱节点与关系

- 产品实体：`ent_product_leoni_dacar_302`
- 零部件实体：`ent_component_leoni_dacar_302`
- 制造商实体：`ent_company_leoni`
- 关键关系：
  - `rel_ent_company_leoni_manufactures_ent_product_leoni_dacar_302`（`ent_company_leoni` → `manufactures` → `ent_product_leoni_dacar_302`）
  - `rel_ent_company_leoni_manufactures_ent_component_leoni_dacar_302`（`ent_company_leoni` → `manufactures` → `ent_component_leoni_dacar_302`）

## 应用场景

- **自动驾驶/机器人传感器总线**：适配该场景的连接与布线需求。
- **工业相机**：适配该场景的连接与布线需求。
- **LiDAR**：适配该场景的连接与布线需求。
- **域控制器互联。**：适配该场景的连接与布线需求。

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

1. [LEONI官网](https://www.leoni.com)
2. 产品 datasheet 与公开技术报道
3. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)