---
$id: ent_paper_general_humanoid_whole_body_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation
  zh: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation
  ko: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation
summary:
  en: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- general_humanoid_whole_body_co
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11929v1.
sources:
- id: src_001
  type: paper
  title: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation (arXiv)
  url: https://arxiv.org/abs/2602.11929
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Learning a general whole-body controller for humanoid robots remains challenging due to the diversity of motion distributions, the difficulty of fast adaptation, and the need for robust balance in high-dynamic scenarios. Existing approaches often require task-specific training or suffer from performance degradation when adapting to new motions. In this paper, we present FAST, a general humanoid whole-body control framework that enables Fast Adaptation and Stable Motion Tracking. FAST introduces Parseval-Guided Residual Policy Adaptation, which learns a lightweight delta action policy under orthogonality and KL constraints, enabling efficient adaptation to out-of-distribution motions while mitigating catastrophic forgetting. To further improve physical robustness, we propose Center-of-Mass-Aware Control, which incorporates CoM-related observations and objectives to enhance balance when tracking challenging reference motions. Extensive experiments in simulation and real-world deployment demonstrate that FAST consistently outperforms state-of-the-art baselines in robustness, adaptation efficiency, and generalization.

## 核心内容
Learning a general whole-body controller for humanoid robots remains challenging due to the diversity of motion distributions, the difficulty of fast adaptation, and the need for robust balance in high-dynamic scenarios. Existing approaches often require task-specific training or suffer from performance degradation when adapting to new motions. In this paper, we present FAST, a general humanoid whole-body control framework that enables Fast Adaptation and Stable Motion Tracking. FAST introduces Parseval-Guided Residual Policy Adaptation, which learns a lightweight delta action policy under orthogonality and KL constraints, enabling efficient adaptation to out-of-distribution motions while mitigating catastrophic forgetting. To further improve physical robustness, we propose Center-of-Mass-Aware Control, which incorporates CoM-related observations and objectives to enhance balance when tracking challenging reference motions. Extensive experiments in simulation and real-world deployment demonstrate that FAST consistently outperforms state-of-the-art baselines in robustness, adaptation efficiency, and generalization.

## 参考
- http://arxiv.org/abs/2602.11929v1

