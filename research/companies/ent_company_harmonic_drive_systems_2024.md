---
$id: ent_company_harmonic_drive_systems_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Harmonic Drive Systems
  zh: 哈默纳科
  ko: Harmonic Drive Systems
summary:
  en: Leading Japanese manufacturer of harmonic/strain-wave gearboxes for robot joints.
  zh: '## 概述 哈默纳科是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。'
  ko: 로봇 관절용 하모닉/스트레인 웨이브 기어박스의 선도적인 일본 제조업체.
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
- gearbox
- harmonic_drive
- japan
- reducer
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_harmonic_drive.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Harmonic Drive Systems
  url: https://www.harmonicdrive.net/
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
哈默纳科是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Harmonic Drive Systems / Harmonic Drive Systems

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Harmonic Drive Systems |
| **英文名** | Harmonic Drive Systems |
| **总部** | 日本长野县安昙野市 |
| **成立时间** | 1970 |
| **官网** | [https://www.harmonicdrive.net](https://www.harmonicdrive.net) |
| **供应链环节** | 谐波减速器 / 精密减速器 / 旋转执行器 |
| **企业属性** | 外资品牌、日本上市公司 |
| **母公司/所属集团** | Harmonic Drive Systems Inc. |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

### 公司简介

全球谐波减速器发明者与领导者，产品以零背隙、高扭矩密度和长寿命著称。

Harmonic Drive Systems 提供 CSF/CSG、SHF/SHG 系列谐波减速器以及 FHA-C 一体化旋转执行器，是工业机器人、半导体设备和人形机器人关节的核心传动部件供应商。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| CSF/CSG 组件型 | 标准/高扭矩谐波减速器 | CSF-32 / CSG-32 | 机器人关节、转台 |
| SHF/SHG 中空型 | 中空结构谐波减速器 | SHF-32 / SHG-32 | 协作机器人、人形机器人 |

### 代表产品

#### CSF-32-50-2A-GR 谐波减速器 / CSF-32-50-2A-GR Harmonic Drive

> CSF-32-50-2A-GR 谐波减速器：请访问 [官方资料](https://www.harmonicdrive.net) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 外径 | 110 mm | Electromate |
| 长度 | 44 mm | Electromate |
| 重量 | 0.89 kg | Electromate |
| 减速比 | 50:1 | Electromate |
| 最大连续扭矩 | 76 N·m | Electromate |
| 最高输入转速 | 7000 rpm | Electromate |
| 背隙 | ≤ 1 arc-min | Electromate |
| 安装方式 | 法兰输出 / 组件型 | Electromate |

**技术亮点**：S 齿形、零背隙、组件型设计，便于直接集成到机器人关节。

**应用场景**：工业机器人腕部、人形机器人小臂/腕部、半导体转台。

#### SHF-32-120 谐波减速器 / SHF-32-120 Harmonic Drive

> SHF-32-120 谐波减速器：请访问 [官方资料](https://www.harmonicdrive.net) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 外径 | 147 mm | Amazon 产品页 |
| 厚度 | 65.5 mm | Amazon 产品页 |
| 重量 | 1.665 kg | Amazon 产品页 |
| 减速比 | 50/80/100/120:1 | Amazon 产品页 |
| 额定扭矩（2000rpm） | 72/112/130/130 N·m | Amazon 产品页 |
| 瞬时最大扭矩 | 363/540/635/652 N·m | Amazon 产品页 |
| 最高输入转速 | 4500 rpm | Amazon 产品页 |
| 背隙 | 10–20 arcsec | Amazon 产品页 |

**技术亮点**：大中空结构，方便线缆穿过，适合协作机器人和人形机器人关节。

**应用场景**：协作机器人肩部/肘部、人形机器人腰/髋部、医疗机器人。

### 供应链位置

- **上游关键零部件/材料**：合金钢（柔轮/刚轮）、交叉滚子轴承、润滑脂、铝壳
- **下游客户/应用场景**：工业机器人、人形机器人、半导体设备、医疗机器人 OEM
- **主要竞争对手/对标**：绿的谐波、来福谐波、Nabtesco、新宝

### 知识图谱节点与关系

- 公司实体：`ent_company_harmonic_drive`
- 产品实体：`ent_component_harmonic_csf_32_50`、`ent_component_harmonic_shf_32_120`
- 关键关系：
  - `ent_company_harmonic_drive` -- `manufactures` --> `ent_component_harmonic_csf_32_50`
  - `ent_company_harmonic_drive` -- `manufactures` --> `ent_component_harmonic_shf_32_120`

### 参考资料

1. [官网](https://www.harmonicdrive.net)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）

## 参考
- [Harmonic Drive Systems](https://www.harmonicdrive.net/)
- 项目 Wiki：appendix-d/companies/company_harmonic_drive.md


