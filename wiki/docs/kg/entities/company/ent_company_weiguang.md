---
id: ent_company_weiguang
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 微光股份
  en: 微光股份
status: active
sources:
- id: src_weiguang_official
  type: website
  url: https://www.weiguang.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 微光股份 / 微光股份

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 微光股份 |
| **英文名** | Hangzhou Weiguang Electronic Co., Ltd. |
| **总部** | 中国杭州 |
| **成立时间** | 1986 |
| **官网** | [https://www.weiguang.com](https://www.weiguang.com) |
| **供应链环节** | 电机 / 风机 / 驱动控制 |
| **企业属性** | 上市公司（SZ.002801）、国内品牌 |
| **母公司/所属集团** | 杭州微光电子股份有限公司 |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

## 公司简介

国内冷链电机与风机龙头企业，外转子电机与 EC 风机技术积累深厚。

微光股份专注于制冷电机、冷柜电机、外转子风机与 EC 风机的研发制造，产品广泛应用于冷链物流、 HVAC、通信、电力与新能源汽车。公司在高效电机设计、电子控制与系统集成方面具备优势，其产品可为机器人整机提供热管理、散热与通风解决方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 外转子电机 | 高效异步/永磁电机 | YZF 系列 | 冷柜、冰箱、机器人热管理 |
| EC 风机 | 直流无刷高效风机 | EC 系列 | 冷链、数据中心、新能源 |
| 驱动控制器 | 电机控制与电源 | 未公开 | 风机、泵、自动化设备 |

## 代表产品

### 外转子电机 / Weiguang External Rotor Motor

> 外转子电机：请访问 [官方资料](https://www.weiguang.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø48–Ø120 mm（系列范围） | 产品手册 |
| 额定功率 | 5–200 W | 产品手册 |
| 额定转速 | 1,300–2,600 rpm | 产品手册 |
| 额定电压 | 110–240 VAC / 12–48 VDC | 产品手册 |
| 效率 | ≥70% | 产品手册 |
| 绝缘等级 | B / F 级 | 产品手册 |
| 防护等级 | IP44–IP54 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：外转子结构紧凑、惯量大、运行平稳，适合风机直驱与空间受限的热管理应用。

**应用场景**：冷链设备风机、机器人热管理、通信设备散热、新能源电池热管理。

### EC 外转子风机 / Weiguang EC External Rotor Fan

> EC 外转子风机：请访问 [官方资料](https://www.weiguang.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 叶轮直径 | 154–400 mm（系列范围） | 产品手册 |
| 风量 | 200–4,500 m³/h | 产品手册 |
| 静压 | 30–1,200 Pa | 产品手册 |
| 额定功率 | 20–600 W | 产品手册 |
| 供电电压 | 24–380 VAC / VDC | 产品手册 |
| 噪音水平 | ≤ 68 dB(A) | 产品手册 |
| 调速接口 | 0–10 V / PWM | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：集成 EC 无刷电机与控制器，高效率、低噪音、调速范围宽，支持智能控制。

**应用场景**：数据中心散热、新能源储能热管理、机器人整机散热、冷链物流。

## 供应链位置

- **上游关键零部件/材料**：硅钢片、铜线、铝材、磁材、电子元器件、塑料粒子
- **下游客户/应用场景**：冷链设备商、家电品牌、数据中心、新能源车企、机器人整机厂
- **主要竞争对手/对标**：ebm-papst、祥明智能、泛仕达、朗伟股份

## 知识图谱节点与关系

- 公司实体：`ent_company_weiguang`
- 产品/零部件实体：`ent_component_weiguang_external_rotor_motor`, `ent_component_weiguang_ec_fan`
- 关键关系：
  - `ent_company_weiguang` -- `manufactures` --> `ent_component_weiguang_external_rotor_motor`
  - `ent_company_weiguang` -- `manufactures` --> `ent_component_weiguang_ec_fan`

## 参考资料

1. [官网](https://www.weiguang.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.weiguang.com/product)（请按实际产品型号核对）