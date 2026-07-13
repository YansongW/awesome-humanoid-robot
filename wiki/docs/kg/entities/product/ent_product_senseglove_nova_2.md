---
id: ent_product_senseglove_nova_2
schema_version: 1
type: product
domain: 02_components
theoretical_depth: system
names:
  zh: SenseGlove Nova 2 力反馈手套
  en: SenseGlove Nova 2 Haptic Force-Feedback Glove
status: active
sources:
- id: src_ent_product_senseglove_nova_2_official
  type: website
  url: https://senseglove.com/products/nova-2/
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# SenseGlove Nova 2 力反馈手套 / SenseGlove Nova 2 Haptic Force-Feedback Glove

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [SenseGlove](../../../appendices/appendix-d/companies/company_senseglove.md) |
| **产品类别** | 无线力反馈/触觉反馈手套 |
| **发布时间** | Nova 系列持续在售，Nova 2 为新一代 |
| **状态** | 量产/商用 |
| **官网/来源** | [SenseGlove Nova 2 产品页](https://senseglove.com/products/nova-2/) |

## 产品概述

SenseGlove Nova 2 是一款面向虚拟现实、遥操作机器人与工业培训的无线力反馈手套。它在手指关键部位配置主动阻力执行器与振动触觉模块，可模拟抓取、按压、摩擦等力觉，配合主流 VR 头显与追踪方案，实现沉浸式的远程操控与训练体验。Nova 2 广泛应用于人形机器人遥操作、手术机器人训练、航空维修模拟等场景。

## 产品图片

> SenseGlove Nova 2：请访问 [官方资料](https://senseglove.com/products/nova-2/) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 无线力反馈手套 | 官网 |
| 反馈执行器 | 4 路主动阻力（拇指、食指、中指、无名指） | 产品页 |
| 触觉反馈 | 振动触觉反馈模块 | 产品页 |
| 手指追踪 | 5 手指追踪（依赖外置追踪器） | 产品页 |
| 无线连接 | 蓝牙 / 2.4 GHz 专有协议 | 产品页 |
| 兼容平台 | Meta Quest 2/3/Pro、SteamVR、PC VR | 产品页 |
| 电池续航 | 约 2–3 小时 | 产品页 |
| 单只重量 | 约 320 g（未公开精确值） | 公开资料 |
| 软件开发 | Unity、Unreal Engine、C++ SDK | 官网 |
| 价格 | 未公开 | 商务报价 |

## 供应链位置

- **制造商**：[SenseGlove](../../../appendices/appendix-d/companies/company_senseglove.md)
- **核心零部件/技术来源**：微型力反馈执行器、柔性传动、惯性/弯曲传感器、蓝牙无线模块、电池、手套织物、追踪器适配
- **下游应用/客户**：机器人遥操作开发商、医疗手术训练、VR 培训集成商、汽车/航空仿真、科研院所

## 知识图谱节点与关系

- 产品实体：`ent_product_senseglove_nova_2`
- 零部件实体：`ent_component_senseglove_nova_2_core`
- 制造商实体：`ent_company_senseglove`
- 关键关系：
  - `rel_ent_company_senseglove_manufactures_ent_product_senseglove_nova_2`（`ent_company_senseglove` → `manufactures` → `ent_product_senseglove_nova_2`）
  - `rel_ent_company_senseglove_manufactures_ent_component_senseglove_nova_2_core`（`ent_company_senseglove` → `manufactures` → `ent_component_senseglove_nova_2_core`）
  - `rel_ent_product_senseglove_nova_2_uses_ent_component_senseglove_nova_2_core`（`ent_product_senseglove_nova_2` → `uses` → `ent_component_senseglove_nova_2_core`）

## 应用场景

- **人形机器人遥操作**：操作员通过手套远程控制人形机器人手部抓取与操作。
- **手术机器人训练**：模拟组织阻力与器械触感，提高训练真实度。
- **VR 工业维修培训**：在虚拟环境中感知螺栓拧紧、部件拆装力。
- **康复评估**：记录手部运动与力反馈数据，用于手功能康复训练。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 无线力反馈手套 | HaptX Gloves G1 | Manus VR Haptic Glove |
| 反馈 | 主动阻力 + 振动触觉 | 气动高保真力反馈 | 振动触觉为主 |
| 无线 | 是 | 需外接气源/缆线 | 是 |
| 价格区间 | 未公开 | 高端 | 中高端 |

## 选购与部署建议

- 确认目标平台追踪方案（Quest / SteamVR / 光学追踪）与 SDK 支持。
- 根据训练场景选择单只或成对手套，并预留力校准与内容适配时间。
- 建议从官方或授权代理商采购以获取最新固件与技术支持。

## 相关词条

- [制造商：SenseGlove](../../../appendices/appendix-d/companies/company_senseglove.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [SenseGlove 官网](https://senseglove.com)
2. [SenseGlove Nova 2 产品页](https://senseglove.com/products/nova-2/)
3. 公开产品评测与技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)