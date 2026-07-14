---
$id: ent_method_design_for_manufacturing
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Design for Manufacturing (DFM)
  zh: 可制造性设计（DFM）
  ko: 제조 용이성 설계(DFM)
summary:
  en: An engineering practice of designing parts and assemblies so that they are easy, repeatable, and cost-effective to manufacture
    at scale.
  zh: 使零部件与总成易于、可重复且经济地实现规模化制造的工程设计方法。
  ko: 부품과 조립체를 쉽고 재현 가능하며 비용 효율적으로 대량 생산할 수 있도록 설계하는 공학 방법론.
domains:
- 03_manufacturing_processes
layers:
- upstream
functional_roles:
- knowledge
tags:
- method
- chapter_10
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body populated from chapter-08.md section "8.6.1 DFM、DFA 与 DFS" by scripts/backfill_method_bodies_from_wiki.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
8.6.1 DFM、DFA 与 DFS相关内容如下。

### 8.6.1 DFM、DFA 与 DFS
面向制造的设计（Design for Manufacturing, DFM）、面向装配的设计（Design for Assembly, DFA）与面向维护/服务的设计（Design for Serviceability, DFS）是降低全生命周期成本的关键方法。

!!! note "术语解释：DFM、DFA、DFS、面向成本的设计、生命周期成本"
    - **DFM（Design for Manufacturing）**：在产品设计阶段考虑制造工艺约束，降低制造难度与成本。
    - **DFA（Design for Assembly）**：简化装配过程，减少零件数量与装配时间。
    - **DFS（Design for Serviceability）**：便于维护、检修、更换与升级的设计。
    - **生命周期成本（LCC）**：产品从概念到报废全过程的总成本。

DFM 原则包括：
1. 减少零件数量与定制件比例。
2. 采用标准材料、标准件与标准工艺。
3. 避免无法加工或检测的几何特征。
4. 考虑公差累积与装配调整。

DFA 原则包括：
1. 设计自定位、自锁紧特征。
2. 减少紧固件种类与数量。
3. 保证装配方向单一、操作空间充足。
4. 采用模块化、子装配先调后装。

DFS 原则包括：
1. 高故障率部件（电池、风扇、线缆）易于更换。
2. 关键关节可在不解体整机的情况下拆装。
3. 提供维护窗口、诊断接口与状态监测。

```mermaid
flowchart TD
    A["设计阶段"] --> B["DFM"]
    A --> C["DFA"]
    A --> D["DFS"]
    B --> E["可制造性"]
    C --> F["可装配性"]
    D --> G["可维护性"]
    E --> H["降低 LCC"]
    F --> H
    G --> H
```

## 参考
- 详见 chapter-08.md。

