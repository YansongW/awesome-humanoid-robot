---
$id: ent_company_mingzhi_appliance_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Mingzhi Appliance
  zh: 鸣志电器
  ko: Mingzhi Appliance
summary:
  en: Chinese manufacturer of hollow-cup motors used in dexterous robot hands.
  zh: 概述 鸣志电器是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。
  ko: 로봇 능숙한 손에 사용되는 홀컵 모터 제조업체.
domains:
- 02_components
- 03_manufacturing_processes
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- china
- component_manufactur
- component_manufacturer
- dexterous_hand
- hollow_cup_motor
- mingzhi
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_moons.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Mingzhi Appliance
  url: http://www.moons.com.cn/
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
鸣志电器是人形机器人领域的重要零部件_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 鸣志电器 / MOONS' Electric

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 鸣志电器 |
| **英文名** | MOONS' Electric |
| **总部** | 中国上海 |
| **成立时间** | 1994 |
| **官网** | [https://www.moons.com.cn](https://www.moons.com.cn) |
| **供应链环节** | 电机 / 驱动 / 运动控制 |
| **企业属性** | 上市公司（SH.603728）、国内品牌 |
| **母公司/所属集团** | 鸣志电器股份有限公司 |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

### 公司简介

国内领先的控制电机及其驱动系统供应商，步进电机全球市占率前列。

鸣志电器专注于控制电机及其驱动系统，产品覆盖步进电机、无刷电机、伺服电机、精密减速器与运动控制器。公司在空心杯电机、无槽无刷电机等高端品类具备量产能力，为机器人、医疗、半导体设备提供核心运动部件。其人形机器人相关布局以微型化、高响应电机与一体化关节模组为主。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 步进电机 | 精密开环/闭环步进 | 57/86 系列、NEMA 系列 | 3C、半导体、医疗设备 |
| 无刷电机 | 高速无槽/空心杯电机 | ECU、DCU 系列 | 机器人关节、无人机、医疗 |
| 伺服系统 | 低压伺服与驱动 | M2AC、M3AC 系列 | AGV、协作机器人 |

### 代表产品

#### 空心杯无刷直流电机 / MOONS' Coreless Brushless DC Motor

> 空心杯无刷直流电机：请访问 [官方资料](https://www.moons.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø16–Ø40 mm（系列范围） | 产品手册 |
| 重量 | 20–150 g（依型号） | 产品手册 |
| 额定电压 | 12–48 VDC | 产品手册 |
| 额定转速 | 5,000–15,000 rpm | 产品手册 |
| 额定扭矩 | 3–50 mNm | 产品手册 |
| 效率 | ≥85% | 产品手册 |
| 通信接口 | Hall / 编码器可选 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：无槽空心杯绕组、低惯量、高动态响应，适合机器人手指、灵巧手等狭小空间驱动。

**应用场景**：人形机器人灵巧手、医疗手持器械、精密光学调焦、无人机云台。

#### 步进电机驱动器 / MOONS' Stepper Drive

> 步进电机驱动器：请访问 [官方资料](https://www.moons.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | 产品手册 |
| 重量 | 未公开 | 产品手册 |
| 额定电流 | 0.5–10 A | 产品手册 |
| 供电电压 | 12–80 VDC | 产品手册 |
| 控制方式 | 脉冲 / CANopen / Modbus | 产品手册 |
| 细分模式 | 最高 256 细分 | 产品手册 |
| 保护功能 | 过流、过压、过热 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：闭环步进控制、振动抑制、支持多种总线协议，适合精密定位与低成本自动化。

**应用场景**：3C 设备、半导体封装、医疗仪器、小型机器人关节。

### 供应链位置

- **上游关键零部件/材料**：稀土永磁体、硅钢片、铜线、轴承、驱动 IC、功率器件
- **下游客户/应用场景**：工业机器人、人形机器人、医疗设备、半导体设备、3C 自动化厂商
- **主要竞争对手/对标**：Maxon、Faulhaber、汇川技术、步科股份、禾川科技

### 知识图谱节点与关系

- 公司实体：`ent_company_moons`
- 产品/零部件实体：`ent_component_moons_brushless_motor`, `ent_component_moons_stepper_drive`
- 关键关系：
  - `ent_company_moons` -- `manufactures` --> `ent_component_moons_brushless_motor`
  - `ent_company_moons` -- `manufactures` --> `ent_component_moons_stepper_drive`

### 参考资料

1. [官网](https://www.moons.com.cn)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）

## 参考
- [Mingzhi Appliance](http://www.moons.com.cn/)
- 项目 Wiki：appendix-d/companies/company_moons.md


