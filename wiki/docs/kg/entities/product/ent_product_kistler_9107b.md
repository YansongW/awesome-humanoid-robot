---
id: ent_product_kistler_9107b
schema_version: 1
type: product
domain: 02_components
theoretical_depth: system
names:
  zh: Kistler 9107B 三分量力传感器
  en: Kistler 9107B 3-Component Force Sensor
status: active
sources:
- id: src_ent_product_kistler_9107b_official
  type: website
  url: https://www.kistler.com/en/products/force-sensors/9107b
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# Kistler 9107B 三分量力传感器 / Kistler 9107B 3-Component Force Sensor

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [奇石乐（Kistler） / Kistler](../../../appendices/appendix-d/companies/company_kistler.md) |
| **产品类别** | 压电式三分量力传感器 |
| **发布时间** | 持续在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [Kistler 9107B 三分量力传感器 产品/资料页](https://www.kistler.com/en/products/force-sensors/9107b) |

## 产品概述

9107B 是 Kistler 推出的紧凑型压电式三分量力传感器，可同时测量 Fx、Fy 与 Fz 三个正交方向的动态力。其高刚度、高固有频率与极低串扰使其适用于机加工切削力监测、机器人末端力控及结构测试。

## 产品图片

> Kistler 9107B 三分量力传感器：请访问 [官方资料](https://www.kistler.com/en/products/force-sensors/9107b) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 压电式三分量力传感器 | 官网 |
| 测量方向 | Fx / Fy / Fz | 官网/datasheet |
| 力测量范围（Fx/Fy） | 未公开 | - |
| 力测量范围（Fz） | 未公开 | - |
| 灵敏度 | 未公开 | - |
| 刚度 | 高刚度设计 | 官网/datasheet |
| 固有频率 | 未公开 | - |
| 串扰 | < ±1%（典型） | 官网/datasheet |
| 工作温度 | 未公开 | - |
| 防护等级 | 未公开 | - |
| 输出接口 | 压电电荷输出 + 配套电荷放大器 | 官网/datasheet |
| 尺寸 | 紧凑型法兰安装 | 官网/datasheet |
| 重量 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[奇石乐（Kistler） / Kistler](../../../appendices/appendix-d/companies/company_kistler.md)
- **核心零部件/技术来源**：压电石英晶体传感元件、预载机构、不锈钢外壳、屏蔽线缆、电荷放大器。
- **下游应用/客户**：机床与刀具厂商、汽车测试实验室、机器人 OEM、航空航天研究机构、人形机器人整机厂。

## 知识图谱节点与关系

- 产品实体：`ent_product_kistler_9107b`
- 零部件实体：`ent_component_kistler_9107b_sensor`
- 制造商实体：`ent_company_kistler`
- 关键关系：
  - `rel_ent_company_kistler_manufactures_ent_product_kistler_9107b`（`ent_company_kistler` → `manufactures` → `ent_product_kistler_9107b`）
  - `rel_ent_company_kistler_manufactures_ent_component_kistler_9107b_sensor`（`ent_company_kistler` → `manufactures` → `ent_component_kistler_9107b_sensor`）
  - `rel_ent_product_kistler_9107b_uses_ent_component_kistler_9107b_sensor`（`ent_product_kistler_9107b` → `uses` → `ent_component_kistler_9107b_sensor`）

## 应用场景

- **机加工切削力监测**：实时三向切削力分析，优化刀具寿命与加工质量。
- **机器人末端力控**：装配、压装与研磨过程中的动态力反馈。
- **结构动态测试**：高刚度传感器捕获瞬态冲击与振动载荷。
- **人形机器人足端**：行走与平衡控制中的地面反作用力测量。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 压电三分量力传感器 | ATI Mini 系列 | Kunwei KWR36 |
| 技术原理 | 压电石英 | 硅应变计 | 金属应变计 |
| 适用频段 | 高频动态 | 中低频力控 | 中低频力控 |
| 核心优势 | 高频动态、低串扰 | 机器人集成成熟 | 微型高精度 |

## 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：奇石乐（Kistler） / Kistler](../../../appendices/appendix-d/companies/company_kistler.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [Kistler 官网](https://www.kistler.com)
2. [Kistler 9107B 三分量力传感器 产品/资料页](https://www.kistler.com/en/products/force-sensors/9107b)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)