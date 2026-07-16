---
$id: ent_component_linear_actuator_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Linear Actuator
  zh: 线性执行器
  ko: Linear Actuator
summary:
  en: Actuator producing linear motion, typically composed of frameless torque motor, planetary roller screw, encoder and
    force sensor.
  zh: 滚珠/梯形丝杠线性执行器 / Dingzhi Lead Screw / Ball Screw Actuator
  ko: 선형 운 동을 생성하는 액추에이터, 일반적으로 프레임리스 토크 모터, 행성 롤러 스크류, 인코더 및 힘 센서로 구성.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- linear_actuator
- linear_motion
- planetary_roller_screw
- torque_motor
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_dingzhi_lead_screw.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Linear Actuator
  url: https://en.wikipedia.org/wiki/Linear_actuator
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
线性执行器是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 滚珠/梯形丝杠线性执行器 / Dingzhi Lead Screw / Ball Screw Actuator

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [鼎智科技 / Dingzhi Technology](../companies/company_dingzhi.md) |
| **产品类别** | 步进电机 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [鼎智科技官网](https://www.dingzhimotion.com) |

### 产品概述

一体化步进/伺服电机+丝杠，结构紧凑、自锁性好，适合机器人线性关节与精密推杆。该系列产品由鼎智科技推出，主要面向步进电机 / 线性执行器 / 丝杠 / 关节模组市场，具有10–300 mm（依定制）等核心参数，适用于机器人、自动化设备及精密传动场景。

作为鼎智科技的代表产品之一，滚珠/梯形丝杠线性执行器在医疗、3D 打印、机器人等领域具有广泛应用。产品采用成熟制造工艺，可根据客户需求提供定制化接口、出线方式与控制协议。

### 产品图片

> 滚珠/梯形丝杠线性执行器：请访问 [官方资料](https://www.dingzhimotion.com) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 丝杠直径 | Ø3–Ø12 mm | 产品手册 |
| 导程 | 1–20 mm | 产品手册 |
| 行程 | 10–300 mm（依定制） | 产品手册 |
| 最大负载 | 500 N | 产品手册 |
| 定位精度 | ±0.02 mm | 产品手册 |
| 重复定位精度 | ±0.01 mm | 产品手册 |
| 传动方式 | 梯形丝杠 / 滚珠丝杠 | 产品手册 |
| 价格 | 未公开 | - |

### 供应链位置

- **制造商**：[鼎智科技 / Dingzhi Technology](../companies/company_dingzhi.md)
- **核心零部件/技术来源**：硅钢片、铜线、磁材、轴承、丝杠钢材、塑料粒子、电子元器件。
- **下游应用/客户**：医疗器械、3D 打印、人形机器人、工业自动化、汽车电子。

### 知识图谱节点与关系

- 零部件实体：`ent_component_dingzhi_lead_screw`
- 制造商实体：`ent_company_dingzhi`
- 关键关系：
  - `rel_ent_company_dingzhi_manufactures_ent_component_dingzhi_lead_screw`（`ent_company_dingzhi` --> `manufactures` --> `ent_component_dingzhi_lead_screw`）

### 应用场景

- **机器人**：人形机器人线性关节、灵巧手驱动、医疗床/注射泵、3D 打印机、光学平台。
- **工业自动化**：精密定位、传动与控制执行机构。
- **医疗与消费电子**：便携式设备、医疗器械驱动单元。
- **新能源与汽车**：电动执行器、热管理与智能座舱部件。

### 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 本土化供应、性价比、定制化 | 高端精度与可靠性 | 同区间性能竞争 |
| 交付周期 | 较短 | 较长 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 中低端至中高端 | 高端 | 中低端 |

### 选购与部署建议

- 选型时应根据负载、行程、速度与精度要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行负载惯量辨识、刚性匹配与振动抑制调试，确保与整机系统兼容。

### 参考资料

1. [鼎智科技官网](https://www.dingzhimotion.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）

## 参考
- [Linear Actuator](https://en.wikipedia.org/wiki/Linear_actuator)
- 项目 Wiki：appendix-d/products/product_dingzhi_lead_screw.md


