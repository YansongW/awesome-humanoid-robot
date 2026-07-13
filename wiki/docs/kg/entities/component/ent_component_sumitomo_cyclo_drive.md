---
id: ent_component_sumitomo_cyclo_drive
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Cyclo 系列摆线减速机
  en: Sumitomo Cyclo Drive
status: active
sources:
- id: src_ent_component_sumitomo_cyclo_drive
  type: website
  url: ''
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Cyclo 系列摆线减速机 / Sumitomo Cyclo Drive

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [住友重工 / Sumitomo Heavy Industries](../../../appendices/appendix-d/companies/company_sumitomo.md) |
| **产品类别** | 摆线减速机 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [住友重工官网](https://www.shi.co.jp) |

## 产品概述

摆线针轮传动、多齿啮合、高刚性、耐冲击，适合重负载、高可靠性的工业场景。该系列产品由住友重工推出，主要面向减速机 / 重型机械 / 精密传动市场，具有6:1 – 658,503:1等核心参数，适用于工业机器人、工程机械及人形机器人场景。

作为住友重工的代表产品之一，Cyclo 系列摆线减速机在工业机器人底座、人形机器人躯干关节、矿山机械等领域具有广泛应用。产品采用成熟制造工艺，可根据客户需求提供定制化减速比、润滑方式与安装接口。

## 产品图片

> Cyclo 系列摆线减速机：请访问 [官方资料](https://www.shi.co.jp) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 40–400 mm 框号（系列范围） | 产品手册 |
| 减速比 | 6:1 – 658,503:1 | 产品手册 |
| 额定输出扭矩 | 20–1,200,000 N·m | 产品手册 |
| 传动效率 | ≥90% | 产品手册 |
| 冲击承载能力 | 额定扭矩 500% | 产品手册 |
| 输入转速 | 最高 3,000 rpm | 产品手册 |
| 润滑方式 | 油脂 / 油浴润滑 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[住友重工 / Sumitomo Heavy Industries](../../../appendices/appendix-d/companies/company_sumitomo.md)
- **核心零部件/技术来源**：特种合金钢、轴承、润滑剂、密封件、铸件、电机。
- **下游应用/客户**：工业机器人厂商、人形机器人整机厂、工程机械、矿业、能源。

## 知识图谱节点与关系

- 零部件实体：`ent_component_sumitomo_cyclo_drive`
- 制造商实体：`ent_company_sumitomo`
- 关键关系：
  - `rel_ent_company_sumitomo_manufactures_ent_component_sumitomo_cyclo_drive`（`ent_company_sumitomo` --> `manufactures` --> `ent_component_sumitomo_cyclo_drive`）

## 应用场景

- **机器人**：工业机器人底座与肩部、人形机器人躯干关节、焊接机器人。
- **工程机械**：挖掘机回转、起重机起升、港口设备。
- **矿山与能源**：破碎机、输送机、提升机。
- **工业自动化**：重载转台、旋转平台、自动化产线。

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 高扭矩、耐冲击、长寿命 | 高端可靠性 | 同区间性能竞争 |
| 交付周期 | 中等 | 较长 | 较短 |
| 服务响应 | 中等 | 中等 | 快速 |
| 价格水平 | 中高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载扭矩、减速比、冲击载荷与安装方式匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行润滑检查、刚性匹配与满载跑合测试，确保与整机系统兼容。

## 参考资料

1. [住友重工官网](https://www.shi.co.jp)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.shi.co.jp/products/)（请按实际产品型号核对）