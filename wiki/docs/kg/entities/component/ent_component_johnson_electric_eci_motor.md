---
id: ent_component_johnson_electric_eci_motor
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: ECI 系列无刷直流电机
  en: Johnson Electric ECI BLDC Motor
status: active
sources:
- id: src_ent_component_johnson_electric_eci_motor
  type: website
  url: ''
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# ECI 系列无刷直流电机 / Johnson Electric ECI BLDC Motor

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [德昌电机 / Johnson Electric](../../../appendices/appendix-d/companies/company_johnson_electric.md) |
| **产品类别** | 无刷直流电机 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [德昌电器官网](https://www.johnsonelectric.com) |

## 产品概述

无刷设计、长寿命、低 EMI，适合需要高可靠性与低维护的机器人关节与执行器。该系列产品由德昌电机推出，主要面向微型电机 / 执行器 / 驱动模块市场，具有12–48 VDC等核心参数，适用于机器人、汽车电子及自动化设备场景。

作为德昌电机的代表产品之一，ECI 系列无刷直流电机在汽车执行器、医疗呼吸机、小型机器人关节等领域具有广泛应用。产品采用成熟制造工艺，可根据客户需求提供定制化轴伸、连接器与控制协议。

## 产品图片

> ECI 系列无刷直流电机：请访问 [官方资料](https://www.johnsonelectric.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø22–Ø62 mm（系列范围） | 产品手册 |
| 重量 | 50–400 g（依型号） | 产品手册 |
| 额定电压 | 12–48 VDC | 产品手册 |
| 额定转速 | 2,000–10,000 rpm | 产品手册 |
| 额定扭矩 | 5–200 mNm | 产品手册 |
| 效率 | ≥80% | 产品手册 |
| 防护等级 | IP40–IP54 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[德昌电机 / Johnson Electric](../../../appendices/appendix-d/companies/company_johnson_electric.md)
- **核心零部件/技术来源**：磁材、铜线、硅钢片、轴承、电子元器件、塑料粒子。
- **下游应用/客户**：汽车 OEM、机器人整机厂、医疗设备商、消费电子品牌。

## 知识图谱节点与关系

- 零部件实体：`ent_component_johnson_electric_eci_motor`
- 制造商实体：`ent_company_johnson_electric`
- 关键关系：
  - `rel_ent_company_johnson_electric_manufactures_ent_component_johnson_electric_eci_motor`（`ent_company_johnson_electric` --> `manufactures` --> `ent_component_johnson_electric_eci_motor`）

## 应用场景

- **机器人**：人形机器人关节、协作机器人、小型执行机构。
- **汽车**：座椅调节、后视镜、天窗、热管理执行器。
- **医疗与消费电子**：呼吸机、输液泵、手持器械、智能家居。
- **工业自动化**：小型输送、阀门控制、精密定位。

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 大规模制造、汽车级可靠性、全球交付 | 高端精度 | 同区间性能竞争 |
| 交付周期 | 中等 | 较长 | 较短 |
| 服务响应 | 中等 | 中等 | 快速 |
| 价格水平 | 中高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载、转速、扭矩与防护要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行驱动器匹配、EMC 测试与热管理验证，确保与整机系统兼容。

## 参考资料

1. [德昌电器官网](https://www.johnsonelectric.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.johnsonelectric.com/en/products)（请按实际产品型号核对）