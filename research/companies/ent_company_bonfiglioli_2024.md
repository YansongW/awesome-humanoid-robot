---
$id: ent_company_bonfiglioli_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Bonfiglioli
  zh: 邦飞利
  ko: Bonfiglioli
summary:
  en: Italian manufacturer of gearboxes and drive systems used in industrial and mobile robotics.
  zh: 用于工业和移动机器人的齿轮箱和驱动系统意大利制造商。
  ko: 산업 및 모바일 로보틱스에 사용되는 기어박스 및 드라이브 시스템 이탈리아 제조업체.
domains:
- 02_components
- 03_manufacturing_processes
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- bonfiglioli
- component_manufactur
- component_manufacturer
- drive_system
- gearbox
- italy
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_bonfiglioli.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Bonfiglioli
  url: https://www.bonfiglioli.com/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
邦飞利是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Bonfiglioli / 邦飞利

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 邦飞利 |
| **英文名** | Bonfiglioli |
| **总部** | 意大利博洛尼亚（Bologna） |
| **成立时间** | 1956 |
| **官网** | [https://www.bonfiglioli.com](https://www.bonfiglioli.com) |
| **供应链环节** | 减速机 / 驱动系统 / 移动机械 |
| **企业属性** | 家族企业、国际工业传动品牌 |
| **母公司/所属集团** | Bonfiglioli 家族（独立） |
| **数据来源** | 官网、产品样本、WAIC 2026 报道 |

### 公司简介

Bonfiglioli 是意大利知名的工业传动与驱动技术供应商，产品涵盖行星减速机、斜齿/伞齿减速电机、变频器及移动机械驱动方案。其 300M 系列行星减速机以高扭矩密度和模块化著称。

公司产品广泛应用于风力发电、物料搬运、工程机械、食品与饮料以及机器人领域，通过全球分销网络提供本地化支持。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 行星减速机 | 重载/高扭矩密度 | 300M 系列 | 风电、矿山、机器人 |
| 斜齿/伞齿减速电机 | 工业齿轮电机 | F / K / A 系列 | 自动化、输送 |
| 变频器与电机 | 运动控制/高效电机 | Active Cube 8 / BN-BE | 产线、物流 |

### 代表产品

#### 300M 系列行星减速机

> 300M 系列行星减速机：请访问 [官方资料](https://www.bonfiglioli.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 减速比 | 3.4:1 – 5,000:1 | 产品手册 |
| 输出扭矩 | 1,000 – 450,000 N·m（系列范围） | 产品手册 |
| 框号尺寸 | 20 种 finely spaced 尺寸 | 产品手册 |
| 安装型式 | 底脚 / 法兰 / 空心轴 / 实心键轴 | 产品手册 |
| 输入方式 | IEC/NEMA 电机适配、液压马达、实心轴 | 产品手册 |
| 防护/选项 | IP65、ATEX、独立冷却、Taconite 密封 | 产品手册 |
| 传动级数 | 1–4 级（含直角/组合） | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：模块化设计、高扭矩密度、直角与同轴版本可选、内置冷却与多重密封、适配多种电机。

**应用场景**：风电变桨、矿山机械、工业机器人底座、人形机器人躯干关节、输送与起重设备。

#### 其他代表产品

F 系列斜齿减速电机扭矩可达数万 N·m；Active Cube 8 变频器支持多轴伺服控制；移动机械轮边驱动用于 AGV/叉车。

### 供应链位置

- **上游关键零部件/材料**：球墨铸铁箱体、合金钢齿轮、轴承、密封件、电机、制动器、冷却系统
- **下游客户/应用场景**：风电主机厂、工程机械、机器人 OEM、物料搬运、食品包装
- **主要竞争对手/对标**：SEW-Eurodrive、Lenze、Siemens、STOBER

### 知识图谱节点与关系

- 公司实体：`ent_company_bonfiglioli`
- 零部件实体：`ent_component_bonfiglioli_300m`
- 关键关系：
  - `ent_company_bonfiglioli` -- `manufactures` --> `ent_component_bonfiglioli_300m`

### 参考资料

1. [邦飞利 官网](https://www.bonfiglioli.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [Bonfiglioli 300M 技术概览](https://www.bonfiglioli.com/en/products/gear-motors-and-gear-units)

## 参考
- [Bonfiglioli](https://www.bonfiglioli.com/)
- 项目 Wiki：appendix-d/companies/company_bonfiglioli.md

