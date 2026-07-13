---
id: ent_component_ewellix_linear_actuator
schema_version: 1
type: component
'title:': Ewellix 电动缸
domain: 02_components
theoretical_depth: system
names:
  zh: Ewellix 电动缸
  en: Ewellix Electromechanical Cylinder
status: active
sources:
- id: src_ewellix_linear_actuator_official
  type: website
  url: https://www.ewellix.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Ewellix 电动缸 / Ewellix Electromechanical Cylinder

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Ewellix](../../../appendices/appendix-d/companies/company_ewellix.md) |
| **产品类别** | 线性驱动 / 电动缸 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [Ewellix 官网](https://www.ewellix.com) |

## 产品概述

Ewellix 电动缸继承 SKF 线性传动技术，提供从紧凑型小推力到工业级大推力的完整机电执行方案。CASM / LAMBDA 系列产品以模块化、高能效和智能控制为特点，可替代传统液压与气动缸。

Ewellix 于 2023 年被 Triton 收购后独立运营，持续服务工业自动化、医疗、机器人和移动机械市场。

## 产品图片

> Ewellix 电动缸：请访问 [官方资料](https://www.ewellix.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 推力范围 | 最高约 100 kN | 产品手册 |
| 行程 | 最大约 2,500 mm | 产品手册 |
| 速度 | 最高约 2,000 mm/s | 产品手册 |
| 重复定位精度 | ±0.01 mm | 产品手册 |
| 电机配置 | 伺服 / 步进可选 | 产品手册 |
| 防护等级 | IP54 / IP65 可选 | 产品手册 |
| 安装方式 | 前法兰 / 后法兰 / 耳轴 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[Ewellix](../../../appendices/appendix-d/companies/company_ewellix.md)
- **核心零部件/技术来源**：滚珠丝杠/滚柱丝杠、直线导轨、伺服电机、控制器、密封件。
- **下游应用/客户**：工业自动化、医疗设备、机器人 OEM、汽车、包装机械。

## 知识图谱节点与关系

- 零部件实体：`ent_component_ewellix_linear_actuator`
- 制造商实体：`ent_company_ewellix`
- 关键关系：
  - `rel_ent_company_ewellix_manufactures_ent_component_ewellix_linear_actuator`（`ent_company_ewellix` --> `manufactures` --> `ent_component_ewellix_linear_actuator`）

## 应用场景

- **工业自动化**：压装、搬运、包装、分拣执行机构。
- **人形机器人**：线性关节、躯干驱动、末端执行器。
- **医疗设备**：手术台、影像设备、康复机器人。
- **移动机械**：农机、工程机械电液替代方案。

## 竞争对比

| 对比项 | Ewellix 电动缸 | Bosch Rexroth | THK |
|--------|----------------|---------------|-----|
| 核心优势 | SKF 技术积淀、模块化 | 大功率、工业级 | 高精度导轨协同 |
| 交付周期 | 中等 | 中等 | 中等 |
| 服务响应 | 中等 | 中等 | 中等 |
| 价格水平 | 中高端 | 高端 | 高端 |

## 选购与部署建议

- 根据推力、速度、行程和精度要求选择 CASM 或 LAMBDA 系列，注意侧向载荷限制。
- 高速长行程应用建议校核丝杠临界转速，并配置导向机构分担侧向力。

## 参考资料

1. [Ewellix 官网](https://www.ewellix.com)
2. [Triton 收购公告](https://www.triton-partners.com)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)