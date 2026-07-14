---
$id: ent_paper_gao_diffvla_bridging_cognitive_rea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment'
  zh: DiffVLA
  ko: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment'
summary:
  en: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment (DiffVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by RIX, Bosch, AIR, Tsinghua University, Shanghai
    Jiao Tong University.'
  zh: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment (DiffVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by RIX, Bosch, AIR, Tsinghua University, Shanghai
    Jiao Tong University.'
  ko: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment (DiffVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by RIX, Bosch, AIR, Tsinghua University, Shanghai
    Jiao Tong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffvla
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17148v4.
sources:
- id: src_001
  type: paper
  title: 'DiffVLA++: Bridging Cognitive Reasoning and End-to-End Driving through Metric-Guided Alignment (arXiv)'
  url: https://arxiv.org/abs/2510.17148
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DiffVLA source
  url: https://doi.org/10.48550/arXiv.2510.17148
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Conventional end-to-end (E2E) driving models are effective at generating physically plausible trajectories, but often fail to generalize to long-tail scenarios due to the lack of essential world knowledge to understand and reason about surrounding environments. In contrast, Vision-Language-Action (VLA) models leverage world knowledge to handle challenging cases, but their limited 3D reasoning capability can lead to physically infeasible actions. In this work we introduce DiffVLA++, an enhanced autonomous driving framework that explicitly bridges cognitive reasoning and E2E planning through metric-guided alignment. First, we build a VLA module directly generating semantically grounded driving trajectories. Second, we design an E2E module with a dense trajectory vocabulary that ensures physical feasibility. Third, and most critically, we introduce a metric-guided trajectory scorer that guides and aligns the outputs of the VLA and E2E modules, thereby integrating their complementary strengths. The experiment on the ICCV 2025 Autonomous Grand Challenge leaderboard shows that DiffVLA++ achieves EPDMS of 49.12.

## 核心内容
Conventional end-to-end (E2E) driving models are effective at generating physically plausible trajectories, but often fail to generalize to long-tail scenarios due to the lack of essential world knowledge to understand and reason about surrounding environments. In contrast, Vision-Language-Action (VLA) models leverage world knowledge to handle challenging cases, but their limited 3D reasoning capability can lead to physically infeasible actions. In this work we introduce DiffVLA++, an enhanced autonomous driving framework that explicitly bridges cognitive reasoning and E2E planning through metric-guided alignment. First, we build a VLA module directly generating semantically grounded driving trajectories. Second, we design an E2E module with a dense trajectory vocabulary that ensures physical feasibility. Third, and most critically, we introduce a metric-guided trajectory scorer that guides and aligns the outputs of the VLA and E2E modules, thereby integrating their complementary strengths. The experiment on the ICCV 2025 Autonomous Grand Challenge leaderboard shows that DiffVLA++ achieves EPDMS of 49.12.

## 参考
- http://arxiv.org/abs/2510.17148v4

