---
id: ent_component_kaidi_linear_drive
schema_version: 1
type: component
'title:': 凯迪线性驱动器
domain: 02_components
theoretical_depth: system
names:
  zh: 凯迪线性驱动器
  en: Kaidi Linear Drive
status: active
sources:
- id: src_kaidi_linear_drive_official
  type: website
  url: https://www.kaidi-electric.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 凯迪线性驱动器 / Kaidi Linear Drive

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [凯迪股份 / Kaidi](../../../appendices/appendix-d/companies/company_kaidi.md) |
| **产品类别** | 线性驱动系统 / 电动推杆 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [凯迪股份官网](https://www.kaidi-electric.com) |

## 产品概述

凯迪股份线性驱动器是以永磁直流/无刷电机为核心、配合丝杠或齿轮传动实现直线运动的机电产品。产品具有低噪音、模块化、易集成的特点，广泛应用于智能家居、医疗康复、汽车座椅及人形机器人线性关节。

凯迪凭借规模化制造与成本控制能力，成为国内线性驱动领域主要出口企业之一，并积极向高推力密度、智能化的机器人执行器方向升级。

## 产品图片

> 凯迪线性驱动器：请访问 [官方资料](https://www.kaidi-electric.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 推拉力 | 最大约 8,000 N | 产品手册 |
| 行程 | 50–1,000 mm | 产品手册 |
| 速度 | 最高约 80 mm/s | 产品手册 |
| 电压 | 24 / 29 / 36 V DC | 产品手册 |
| 防护等级 | IP42 / IP54 可选 | 产品手册 |
| 噪音 | ≤ 48 dB | 产品手册 |
| 重复定位精度 | ±0.5 mm | 产品手册 |
| 材质 | 铝合金 / 钢 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[凯迪股份 / Kaidi](../../../appendices/appendix-d/companies/company_kaidi.md)
- **核心零部件/技术来源**：永磁电机、丝杠/齿轮、控制器、铝合金型材、塑料件。
- **下游应用/客户**：智能家居、医疗康复设备、汽车座椅、人形机器人 OEM。

## 知识图谱节点与关系

- 零部件实体：`ent_component_kaidi_linear_drive`
- 制造商实体：`ent_company_kaidi`
- 关键关系：
  - `rel_ent_company_kaidi_manufactures_ent_component_kaidi_linear_drive`（`ent_company_kaidi` --> `manufactures` --> `ent_component_kaidi_linear_drive`）

## 应用场景

- **智能家居**：智能升降桌、电动沙发、可调节床架。
- **医疗康复**：护理床、轮椅升降、康复训练设备。
- **汽车**：座椅调节、尾门启闭、方向盘调节。
- **人形机器人**：低负载线性关节、躯干伸缩机构。

## 竞争对比

| 对比项 | 凯迪线性驱动器 | Linak | 捷昌驱动 |
|--------|----------------|-------|----------|
| 核心优势 | 规模化、性价比、出口经验 | 品牌、可靠性、医疗认证 | 国内龙头、快速交付 |
| 交付周期 | 较短 | 中等 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 中低端 | 高端 | 中端 |

## 选购与部署建议

- 选型时根据负载、速度、行程与安装空间匹配电机规格，注意空载与满载速度差异。
- 医疗或户外应用需确认防护等级、EMC 认证及噪音要求，必要时选择带霍尔反馈型号。

## 参考资料

1. [凯迪股份官网](https://www.kaidi-electric.com)
2. [上交所公告/年报](http://www.sse.com.cn)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)