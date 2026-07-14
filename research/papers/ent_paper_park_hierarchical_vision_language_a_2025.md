---
$id: ent_paper_park_hierarchical_vision_language_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations
  zh: VINE
  ko: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations
summary:
  en: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations (VINE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Korea University, KAIST, Seoul National University, NAVER AI Lab.
  zh: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations (VINE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Korea University, KAIST, Seoul National University, NAVER AI Lab.
  ko: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations (VINE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Korea University, KAIST, Seoul National University, NAVER AI Lab.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vine
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.03913v1.
sources:
- id: src_001
  type: paper
  title: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations (arXiv)
  url: https://arxiv.org/abs/2512.03913
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VINE source
  url: https://doi.org/10.48550/arXiv.2512.03913
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Prior Vision-Language-Action (VLA) models are typically trained on teleoperated successful demonstrations, while discarding numerous failed attempts that occur naturally during data collection. However, these failures encode where and how policies can be fragile, information that can be exploited to improve robustness. We address this problem by leveraging mixed-quality datasets to learn failure-aware reasoning at planning time. We introduce VINE, a hierarchical vision-language-action model that separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical reinforcement learning formalism, making failures usable as a structured learning signal rather than noisy supervision. System 2 performs feasibility-guided tree search over a 2D scene-graph abstraction: it proposes subgoal transitions, predicts success probabilities from both successes and failures, and prunes brittle branches before execution, effectively casting plan evaluation as feasibility scoring. The selected subgoal sequence is then passed to System 1, which executes low-level actions without modifying the agent's core skills. Trained entirely from offline teleoperation data, VINE integrates negative experience directly into the decision loop. Across challenging manipulation tasks, this approach consistently improves success rates and robustness, demonstrating that failure data is an essential resource for converting the broad competence of VLAs into robust execution.

## 核心内容
Prior Vision-Language-Action (VLA) models are typically trained on teleoperated successful demonstrations, while discarding numerous failed attempts that occur naturally during data collection. However, these failures encode where and how policies can be fragile, information that can be exploited to improve robustness. We address this problem by leveraging mixed-quality datasets to learn failure-aware reasoning at planning time. We introduce VINE, a hierarchical vision-language-action model that separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical reinforcement learning formalism, making failures usable as a structured learning signal rather than noisy supervision. System 2 performs feasibility-guided tree search over a 2D scene-graph abstraction: it proposes subgoal transitions, predicts success probabilities from both successes and failures, and prunes brittle branches before execution, effectively casting plan evaluation as feasibility scoring. The selected subgoal sequence is then passed to System 1, which executes low-level actions without modifying the agent's core skills. Trained entirely from offline teleoperation data, VINE integrates negative experience directly into the decision loop. Across challenging manipulation tasks, this approach consistently improves success rates and robustness, demonstrating that failure data is an essential resource for converting the broad competence of VLAs into robust execution.

## 参考
- http://arxiv.org/abs/2512.03913v1

