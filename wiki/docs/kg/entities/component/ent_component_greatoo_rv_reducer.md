---
id: ent_component_greatoo_rv_reducer
schema_version: 1
type: component
'title:': RV 减速器
domain: 02_components
theoretical_depth: system
names:
  zh: RV 减速器
  en: Greatoo RV Reducer
status: active
sources:
- id: src_greatoo_rv_reducer_official
  type: website
  url: http://www.greatoo.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# RV 减速器 / Greatoo RV Reducer

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [巨轮智能 / Greatoo Intelligent Equipment](../../../appendices/appendix-d/companies/company_greatoo.md) |
| **产品类别** | RV 减速器 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [巨轮智能官网](http://www.greatoo.com) |

## 产品概述

自主齿形与轴承设计、高刚性、长寿命，适配重载工业机器人与人形机器人大扭矩关节。该系列产品由巨轮智能推出，主要面向RV 减速器 / 轮胎模具 / 工业机器人 / 精密机械市场，具有30–200:1等核心参数，适用于机器人、自动化设备及精密传动场景。

作为巨轮智能的代表产品之一，RV 减速器在工业机器人、人形机器人等领域具有广泛应用。产品采用成熟制造工艺，可根据客户需求提供定制化接口、出线方式与控制协议。

## 产品图片

> RV 减速器：请访问 [官方资料](http://www.greatoo.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 外径 110–400 mm（系列范围） | 产品手册 |
| 重量 | 2–60 kg | 产品手册 |
| 减速比 | 30–200:1 | 产品手册 |
| 额定扭矩 | 50–5,000 N·m | 产品手册 |
| 扭转刚度 | 未公开 | 产品手册 |
| 背隙 | ≤ 1 arc-min | 产品手册 |
| 传动精度 | ≤ 1 arc-min | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[巨轮智能 / Greatoo Intelligent Equipment](../../../appendices/appendix-d/companies/company_greatoo.md)
- **核心零部件/技术来源**：合金钢、轴承、润滑油、铸件、电机、驱动器。
- **下游应用/客户**：汽车轮胎厂、工业机器人集成商、人形机器人 OEM、金属加工。

## 知识图谱节点与关系

- 零部件实体：`ent_component_greatoo_rv_reducer`
- 制造商实体：`ent_company_greatoo`
- 关键关系：
  - `rel_ent_company_greatoo_manufactures_ent_component_greatoo_rv_reducer`（`ent_company_greatoo` --> `manufactures` --> `ent_component_greatoo_rv_reducer`）

## 应用场景

- **机器人**：工业机器人基座/肩部/肘部、人形机器人髋/腰/膝关节、重型转台。
- **工业自动化**：精密定位、传动与控制执行机构。
- **医疗与消费电子**：便携式设备、医疗器械驱动单元。
- **新能源与汽车**：电动执行器、热管理与智能座舱部件。

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 本土化供应、性价比、定制化 | 高端精度与可靠性 | 同区间性能竞争 |
| 交付周期 | 较短 | 较长 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 中低端至中高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载、行程、速度与精度要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行负载惯量辨识、刚性匹配与振动抑制调试，确保与整机系统兼容。

## 参考资料

1. [巨轮智能官网](http://www.greatoo.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）