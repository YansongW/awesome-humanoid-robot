# Entry Template (YAML frontmatter + Markdown)

> Copy this file for each new entity. Replace bracketed placeholders with real content.

```yaml
---
$id: "ent_<unique_snake_case_name>"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "<entity_type>"

names:
  en: "English name"
  zh: "中文名称"
  ko: "한국어 이름"

summary:
  en: "One-sentence summary in English."
  zh: "一句话中文摘要。"
  ko: "한국어 한 줄 요약."

domains:
  - "00_foundations"          # or the appropriate engineering domain

layers:
  - "foundations"             # or upstream / midstream / intelligence / validation_markets

functional_roles:
  - "knowledge"               # or material / component / system / intelligence / etc.

theoretical_depth:
  - "foundation"              # or principle / formalism / method / system

tags:
  - "example_tag"

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "Draft entity for demonstration; sources and relationships to be expanded."

sources:
  - id: "src_<id>"
    type: "paper"
    title: "Source title"
    url: "https://example.com/source"
    date: "2026-01-01"
    accessed_at: "2026-06-25"

related_entities:
  - id: "ent_<other>"
    relationship: "has_prerequisite"
    description:
      en: "Brief description of the relationship."
      zh: "关系简述。"
      ko: "관계에 대한 간단한 설명."

---

# English name / 中文名称 / 한국어 이름

## 抽象

> **生活实例**：用一句日常比喻说明这个实体。例如，KKT 条件可以比喻成“在商场里找最近出口，同时不能走进商店、必须站在过道中线上”。
>
> **自然语言逻辑**：用两三句话说明它解决什么问题、为什么长这样、每个符号/步骤在直觉上代表什么。读者读完这段后，应该能在不看公式的情况下理解这个知识点的核心思想。

## 形式化定义 / Formal Definition

在此处写出公式、定义、伪代码或严格表述。

例如：

$$
\min_{x} \; \frac{1}{2} x^{\top} H x + g^{\top} x
\quad \text{s.t.} \quad A x = b, \; C x \leq d
$$

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $x$ | 决策变量 | 我们要找的最优“位置” |
| $H$ | Hessian | 目标函数的曲率 |
| $g$ | Gradient | 目标函数的“坡度” |
| $A, b$ | 等式约束 | 必须精确满足的规则 |
| $C, d$ | 不等式约束 | 不能越过的边界 |

## 与其他知识点的关系

- `has_prerequisite` → [相关前置知识]
- `derived_from` → [推导来源]
- `instantiates` / `builds_on` → [具体实例或后续工作]

## 参考文献

1. Author et al., "Title", *Venue*, Year.
