---
id: ent_component_shimpo_vrsf_gearbox
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: VRSF 系列行星减速器
  en: Nidec-Shimpo VRSF Planetary Gearbox
status: active
sources:
- id: src_ent_component_shimpo_vrsf_gearbox
  type: website
  url: ''
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# VRSF 系列行星减速器 / Nidec-Shimpo VRSF Planetary Gearbox

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [日本新宝 / Nidec-Shimpo](../../../appendices/appendix-d/companies/company_shimpo.md) |
| **产品类别** | 行星减速器 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [Nidec-Shimpo 官网](https://www.nidec-shimpo.com) |

## 产品概述

斜齿行星结构、低背隙、高刚性，适合高动态、高精度定位的机器人关节与伺服系统。该系列产品由日本新宝推出，主要面向减速器 / 传动部件 / 电机模组市场，具有3:1 – 100:1等核心参数，适用于工业机器人、协作机器人及人形机器人场景。

作为日本新宝的代表产品之一，VRSF 系列行星减速器在工业机器人关节、半导体设备、数控机床等领域具有广泛应用。产品采用成熟制造工艺，可根据客户需求提供定制化法兰、输出轴、润滑与密封配置。

## 产品图片

> VRSF 系列行星减速器：请访问 [官方资料](https://www.nidec-shimpo.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 40–200 mm 框号（系列范围） | 产品手册 |
| 减速比 | 3:1 – 100:1 | 产品手册 |
| 额定输出扭矩 | 5–3,000 N·m | 产品手册 |
| 背隙 | ≤ 3 arcmin（标准）/ ≤ 1 arcmin（精密型） | 产品手册 |
| 传动效率 | ≥90% | 产品手册 |
| 输入转速 | 最高 6,000 rpm | 产品手册 |
| 防护等级 | IP54–IP65 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[日本新宝 / Nidec-Shimpo](../../../appendices/appendix-d/companies/company_shimpo.md)
- **核心零部件/技术来源**：轴承、齿轮钢、润滑剂、密封件、电机（集团内供应）。
- **下游应用/客户**：工业机器人厂商、人形机器人整机厂、半导体设备商、机床厂。

## 知识图谱节点与关系

- 零部件实体：`ent_component_shimpo_vrsf_gearbox`
- 制造商实体：`ent_company_shimpo`
- 关键关系：
  - `rel_ent_company_shimpo_manufactures_ent_component_shimpo_vrsf_gearbox`（`ent_company_shimpo` --> `manufactures` --> `ent_component_shimpo_vrsf_gearbox`）

## 应用场景

- **机器人**：人形机器人关节、协作机器人、SCARA 机器人。
- **工业自动化**：数控机床进给轴、自动化产线、包装设备。
- **半导体与电子**：晶圆搬运、贴片机、检测设备。
- **新能源与汽车**：电动执行器、测试台架、智能座舱部件。

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 低背隙、高刚性、Nidec 集团协同 | 高端精度 | 同区间性能竞争 |
| 交付周期 | 中等 | 较长 | 较短 |
| 服务响应 | 中等 | 中等 | 快速 |
| 价格水平 | 中高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载扭矩、减速比、背隙与安装方式匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行刚性匹配、润滑检查与背隙测试，确保与整机系统兼容。

## 参考资料

1. [Nidec-Shimpo 官网](https://www.nidec-shimpo.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.nidec-shimpo.com/products/)（请按实际产品型号核对）