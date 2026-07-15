---
$id: ent_company_maxon_group_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Maxon Group
  zh: Maxon
  ko: Maxon Group
summary:
  en: Swiss manufacturer of high-precision brushless DC motors, gearheads and controllers for robotics.
  zh: Maxon是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。
  ko: 로보틱스용 고정밀 브러시리스 DC 모터, 기어헤드 및 컨트롤러 제조업체.
domains:
- 02_components
- 03_manufacturing_processes
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component_manufactur
- component_manufacturer
- controller
- gearhead
- maxon
- motor
- switzerland
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_maxon.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Maxon Group
  url: https://www.maxongroup.com/
  date: '2024'
  accessed_at: '2026-07-01'
---


## 概述
Maxon是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Maxon Motor / Maxon Motor

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Maxon Motor |
| **英文名** | Maxon Motor |
| **总部** | 瑞士 Sachseln |
| **成立时间** | 1961 |
| **官网** | [https://www.maxongroup.com](https://www.maxongroup.com) |
| **供应链环节** | 电机 / 驱动 / 精密运动控制 |
| **企业属性** | 外资品牌、瑞士上市 |
| **母公司/所属集团** | maxon Group |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

### 公司简介

全球领先的精密直流电机与驱动系统供应商，以高扭矩密度、低齿槽转矩的 brushless DC 电机著称。

Maxon Motor 提供 brushed/brushless DC 电机、齿轮箱、编码器和控制器，产品广泛应用于医疗、航天、机器人和工业自动化。其 EC-i 系列铁芯无刷电机因高动态响应和紧凑设计，常被用于协作机器人和人形机器人关节驱动。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| EC-i / EC 无刷电机 | 高扭矩密度伺服电机 | EC-i 40 / EC 40 | 机器人关节、AGV、医疗设备 |
| ECX SPEED / ESK 电机 | 超高速无刷电机 | ECX SPEED 16 | 手术工具、航空作动器 |

### 代表产品

#### EC-i 40 无刷直流电机 / EC-i 40 Brushless DC Motor

> EC-i 40 无刷直流电机：请访问 [官方资料](https://www.maxongroup.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø40 × 52 mm（参考） | maxon 产品页 |
| 重量 | 390 g | maxon 产品页 488607 |
| 额定功率 | 100 W | maxon 产品页 |
| 额定扭矩 | 224 mNm | maxon 产品页 |
| 堵转扭矩 | 2080 mNm | maxon 产品页 |
| 额定转速 | 4390 rpm | maxon 产品页 |
| 最高转速 | 8000 rpm | maxon 产品页 |
| 效率 | 89% | maxon 产品页 |
| 编码器 | Hall 传感器，可配编码器 | maxon 产品页 |

**技术亮点**：铁芯绕组、高扭矩密度、低齿槽转矩，适合机器人关节紧凑集成。

**应用场景**：协作机器人关节、外骨骼、AGV 驱动轮、精密自动化设备。

#### EC 40 无刷直流电机 / EC 40 Brushless DC Motor

> EC 40 无刷直流电机：请访问 [官方资料](https://www.maxongroup.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø40 mm | TraceParts |
| 重量 | 390 g | TraceParts |
| 额定功率 | 120 W | TraceParts 118896 |
| 额定扭矩 | 124 mNm | TraceParts |
| 堵转扭矩 | 1280 mNm | TraceParts |
| 额定转速 | 9280 rpm | TraceParts |
| 最高转速 | 18000 rpm | TraceParts |
| 效率 | 84% | TraceParts |
| 工作温度 | -20 ~ +125 °C | TraceParts |

**技术亮点**：高速型无刷电机，适合需要高转速与小体积的精密传动场景。

**应用场景**：医疗手持工具、光学平台、小型无人机、机器人末端执行器。

### 供应链位置

- **上游关键零部件/材料**：稀土永磁体（钕铁硼）、铜线、硅钢片、轴承、铝外壳
- **下游客户/应用场景**：协作机器人、人形机器人 OEM、医疗器械、航空航天厂商
- **主要竞争对手/对标**：Kollmorgen、汇川技术、禾川科技、鸣志电器

### 知识图谱节点与关系

- 公司实体：`ent_company_maxon`
- 产品实体：`ent_component_maxon_ec_i_40`、`ent_component_maxon_ec_40`
- 关键关系：
  - `ent_company_maxon` -- `manufactures` --> `ent_component_maxon_ec_i_40`
  - `ent_company_maxon` -- `manufactures` --> `ent_component_maxon_ec_40`

### 参考资料

1. [官网](https://www.maxongroup.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）

## 参考
- [Maxon Group](https://www.maxongroup.com/)
- 项目 Wiki：appendix-d/companies/company_maxon.md



