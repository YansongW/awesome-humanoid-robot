---
$id: ent_concept_product_liability
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Product Liability
  zh: 产品责任
  ko: 제품 책임
summary:
  en: The legal responsibility of manufacturers and sellers for injuries or damages caused by defective or unsafe products,
    directly applicable to humanoid robots.
  zh: 制造商与销售商因缺陷或不安全产品造成人身伤害或财产损失的法律责任，直接适用于人形机器人。
  ko: 결함이나 불안전한 제품으로 인한 상해·손해에 대해 제조업체와 판매자가 지는 법적 책임.
domains:
- 12_policy_regulation_ethics
layers:
- validation_markets
functional_roles:
- knowledge
tags:
- concept
- chapter_29
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-07.md#7.8.3 冲突矿产与负责任采购 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
产品责任是人形机器人领域的重要concept。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
钽、锡、钨、金（3TG）以及钴等矿产在部分冲突地区和高风险地区开采，可能涉及强迫劳动、童工和环境破坏。**冲突矿产（conflict minerals）**法规要求企业进行来源调查与披露。

!!! note "术语解释：冲突矿产、3TG、负责任采购、冶炼厂审计、RMI"
    - **冲突矿产**：在冲突地区开采并可能资助武装团体的矿产。
    - **3TG**：钽（Tantalum）、锡（Tin）、钨（Tungsten）、金（Gold）。
    - **负责任采购（responsible sourcing）**：在采购中考虑人权和环境影响的实践。
    - **冶炼厂审计（smelter audit）**：对矿产冶炼厂进行第三方审核，确认来源合规。
    - **RMI（Responsible Minerals Initiative）**：负责任矿产倡议，提供冶炼厂清单与审计标准。

```mermaid
flowchart TD
    A["人形机器人 ESG 管理"] --> B["环境"]
    A --> C["社会"]
    A --> D["治理"]
    B --> B1["LCA 与范围 3 碳排"]
    B --> B2["电池回收与梯次利用"]
    B --> B3["绿色材料替代"]
    C --> C1["冲突矿产尽职调查"]
    C --> C2["供应商劳工标准"]
    C --> C3["社区影响"]
    D --> D1["反贿赂/反腐败"]
    D --> D2["供应链透明披露"]
    D --> D3["董事会 ESG 监督"]
```

---

## 参考
- Wiki extraction
- 项目 Wiki：chapter-07.md#7.8.3 冲突矿产与负责任采购

