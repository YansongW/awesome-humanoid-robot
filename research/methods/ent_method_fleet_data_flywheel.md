---
$id: ent_method_fleet_data_flywheel
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Fleet Data Flywheel
  zh: 车队数据飞轮
  ko: 플릿 데이터 플라이휠
summary:
  en: A closed-loop system where data from deployed robot fleets continuously improves models, which in turn improve fleet
    performance and generate more data.
  zh: 部署机器人车队产生的数据持续改进模型，模型反过来提升车队性能并产生更多数据的闭环系统。
  ko: 배포된 로봇 플릿의 데이터가 지속적으로 모델을 개선하고, 이 모델이 다시 플릿 성능을 높여 더 많은 데이터를 생성하는 폐쇄 루프 시스템.
domains:
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
tags:
- method
- chapter_21
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-01.md#1.14.3 数据飞轮与规模化学习 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
车队数据飞轮是人形机器人领域的重要method。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
人形机器人的 AI 能力提升依赖于数据飞轮：

```mermaid
graph LR
    A[部署机器人] --> B[采集真实数据]
    B --> C[数据清洗与标注]
    C --> D[模型训练]
    D --> E[模型部署]
    E --> A

    D --> F[仿真生成数据]
    F --> C
```

真实数据包括遥操作演示、人类动作捕捉、自主运行记录和失败案例。仿真数据可以快速生成大量多样场景，但存在 reality gap。成功的数据策略通常是真实数据与仿真数据的结合。

!!! note "术语解释：数据飞轮（Data Flywheel）"
    数据飞轮是指产品使用越多，产生的数据越多，模型越好，产品体验越好，从而吸引更多使用的正反馈循环。在人形机器人中，数据飞轮是实现泛化能力和持续改进的关键机制。

---

## 参考
- Wiki extraction
- 项目 Wiki：chapter-01.md#1.14.3 数据飞轮与规模化学习

