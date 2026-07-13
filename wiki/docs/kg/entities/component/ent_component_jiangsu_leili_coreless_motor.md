---
id: ent_component_jiangsu_leili_coreless_motor
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 空心杯无刷直流电机
  en: Jiangsu Leili Coreless BLDC Motor
status: active
sources:
- id: src_ent_component_jiangsu_leili_coreless_motor
  type: website
  url: ''
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 空心杯无刷直流电机 / Jiangsu Leili Coreless BLDC Motor

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [江苏雷利 / Jiangsu Leili](../../../appendices/appendix-d/companies/company_jiangsu_leili.md) |
| **产品类别** | 空心杯电机 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [江苏雷利官网](https://www.leiligroup.com) |

## 产品概述

无槽空心杯结构、低惯量、高动态响应，适合机器人灵巧手、医疗精密器械等场景。该系列产品由江苏雷利推出，主要面向电机 / 驱动 / 精密组件市场，具有12–48 VDC等核心参数，适用于机器人、医疗及自动化设备场景。

作为江苏雷利的代表产品之一，空心杯无刷直流电机在人形机器人手指、医疗手持器械、无人机云台等领域具有广泛应用。产品采用成熟制造工艺，可根据客户需求提供定制化接口、出线方式与控制协议。

## 产品图片

> 空心杯无刷直流电机：请访问 [官方资料](https://www.leiligroup.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø13–Ø30 mm（系列范围） | 产品手册 |
| 重量 | 10–80 g（依型号） | 产品手册 |
| 额定电压 | 12–48 VDC | 产品手册 |
| 额定转速 | 5,000–18,000 rpm | 产品手册 |
| 额定扭矩 | 1–40 mNm | 产品手册 |
| 效率 | ≥85% | 产品手册 |
| 通信接口 | Hall / 编码器可选 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[江苏雷利 / Jiangsu Leili](../../../appendices/appendix-d/companies/company_jiangsu_leili.md)
- **核心零部件/技术来源**：稀土永磁体、铜线、硅钢片、轴承、驱动 IC、塑料粒子。
- **下游应用/客户**：家电品牌、汽车 Tier 1、医疗器械、人形机器人整机厂、3C 自动化。

## 知识图谱节点与关系

- 零部件实体：`ent_component_jiangsu_leili_coreless_motor`
- 制造商实体：`ent_company_jiangsu_leili`
- 关键关系：
  - `rel_ent_company_jiangsu_leili_manufactures_ent_component_jiangsu_leili_coreless_motor`（`ent_company_jiangsu_leili` --> `manufactures` --> `ent_component_jiangsu_leili_coreless_motor`）

## 应用场景

- **机器人**：人形机器人灵巧手、无人机云台、小型机械臂。
- **医疗与消费电子**：医疗手持器械、便携式设备、精密光学调焦。
- **汽车电子**：电动执行器、热管理与智能座舱部件。
- **工业自动化**：精密定位、传动与控制执行机构。

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 本土化供应、性价比、快速响应 | 高端精度与可靠性 | 同区间性能竞争 |
| 交付周期 | 较短 | 较长 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 中低端至中高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载、行程、速度与精度要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行负载惯量辨识、刚性匹配与振动抑制调试，确保与整机系统兼容。

## 参考资料

1. [江苏雷利官网](https://www.leiligroup.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.leiligroup.com/product)（请按实际产品型号核对）