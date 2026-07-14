---
$id: ent_paper_bill_of_materials_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Bill of Materials
  zh: 物料清单
  ko: Bill of Materials
summary:
  en: Structured list of all parts, subassemblies, and raw materials required to build one humanoid robot unit.
  zh: 构建一台人形机器人所需的所有零件、子装配件和原材料的结构化清单。
  ko: 한 대의 휨로봇을 제작하는 데 필요한 모든 부품, 하위 조립품 및 원자재의 구조화된 목록.
domains:
- 03_manufacturing_processes
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- bom
- concept
- cost
- manufacturing
- supply_chain
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-07.md#7.2.1 物料清单（BOM）的结构 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Bill of Materials
  url: https://en.wikipedia.org/wiki/Bill_of_materials
  date: '2024'
  accessed_at: '2026-07-02'
---
## 概述
物料清单是人形机器人领域的重要concept。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
**物料清单（Bill of Materials, BOM）**是描述产品组成的最基础文件，列出制造一件产品所需的全部原材料、零部件、子装配件及其数量关系。BOM 不仅是成本核算起点，也是采购、计划、库存管理和供应商协同的核心数据结构。

!!! note "术语解释：BOM、EBOM、MBOM、Indented BOM、Phantom"
    - **BOM（Bill of Materials）**：产品结构表，记录组成产品的所有物料及其层级关系。
    - **EBOM（Engineering BOM）**：工程设计视图，按功能模块组织。
    - **MBOM（Manufacturing BOM）**：制造视图，按装配工艺和生产线组织。
    - **Indented BOM（缩进式物料清单）**：以父子层级缩进展示零件关系。
    - **Phantom（虚拟件）**：在 BOM 中作为逻辑子组件存在，但不单独入库的装配单元。

BOM 成本可直接按单位用量与单价滚动计算：

$$
C_{\text{BOM}} = \sum_{i} q_i \cdot p_i
$$

其中 \(q_i\) 为第 \(i\) 个零件的单位用量，\(p_i\) 为其采购单价或自制成本。对于多层级 BOM，需要自下向上递归汇总：

$$
C_{\text{parent}} = \sum_{j} q_j \cdot C_j + C_{\text{assembly},j}
$$

这里 \(C_j\) 既可以是子装配件的滚动成本，也可以是外购件单价。

## 参考
- [Bill of Materials](https://en.wikipedia.org/wiki/Bill_of_materials)
- 项目 Wiki：chapter-07.md#7.2.1 物料清单（BOM）的结构

