---
$id: ent_concept_seven_transitions
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Seven Transitions from 0 to 1
  zh: 从0到1的七个跃迁
  ko: 0에서 1로의 7가지 전환
summary:
  en: A framework describing seven critical transitions—technology, system, supply chain, manufacturing, cost, validation,
    and market—required to move a humanoid robot from prototype to product.
  zh: 将人形机器人从样机推向产品所需的技术、系统、供应链、制造、成本、验证与市场七大关键跃迁框架。
  ko: 휴로봇을 시제품에서 제품으로 전환하는 데 필요한 기술·시스템·공급망·제조·비용·검증·시장의 7대 전환 프레임워크.
domains:
- 11_applications_markets
- 12_policy_regulation_ethics
layers:
- validation_markets
functional_roles:
- knowledge
tags:
- concept
- chapter_1
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
  confidence: high
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; pending human review and translation
    to en/ko.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 1.5 从 0 到 1 的七个跃迁

将人形机器人从概念变为可规模化的产品，需要经历七个递进的跃迁阶段。下图展示了这一过程的宏观流程：

```mermaid
flowchart LR
    A[实验室样机] --> B[工程样机]
    B --> C[小批量验证]
    C --> D[量产准备]
    D --> E[场景部署]
    E --> F[运营维护]
    F --> G[规模化复制]
```
