---
$id: ent_paper_keep_on_going_learning_robust_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training'
  zh: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training'
  ko: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training'
summary:
  en: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- keep_on_going
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.08303v3.
sources:
- id: src_001
  type: paper
  title: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training (arXiv)'
  url: https://arxiv.org/abs/2507.08303
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots are expected to operate reliably over long horizons while executing versatile whole-body skills. Yet Reinforcement Learning (RL) motion policies typically lose stability under prolonged operation, sensor/actuator noise, and real world disturbances. In this work, we propose a Selective Adversarial Attack for Robust Training (SA2RT) to enhance the robustness of motion skills. The adversary is learned to identify and sparsely perturb the most vulnerable states and actions under an attack-budget constraint, thereby exposing true weakness without inducing conservative overfitting. The resulting non-zero sum, alternating optimization continually strengthens the motion policy against the strongest discovered attacks. We validate our approach on the Unitree G1 humanoid robot across perceptive locomotion and whole-body control tasks. Experimental results show that adversarially trained policies improve the terrain traversal success rate by 40%, reduce the trajectory tracking error by 32%, and maintain long horizon mobility and tracking performance. Together, these results demonstrate that selective adversarial attacks are an effective driver for learning robust, long horizon humanoid motion skills.

## 核心内容
Humanoid robots are expected to operate reliably over long horizons while executing versatile whole-body skills. Yet Reinforcement Learning (RL) motion policies typically lose stability under prolonged operation, sensor/actuator noise, and real world disturbances. In this work, we propose a Selective Adversarial Attack for Robust Training (SA2RT) to enhance the robustness of motion skills. The adversary is learned to identify and sparsely perturb the most vulnerable states and actions under an attack-budget constraint, thereby exposing true weakness without inducing conservative overfitting. The resulting non-zero sum, alternating optimization continually strengthens the motion policy against the strongest discovered attacks. We validate our approach on the Unitree G1 humanoid robot across perceptive locomotion and whole-body control tasks. Experimental results show that adversarially trained policies improve the terrain traversal success rate by 40%, reduce the trajectory tracking error by 32%, and maintain long horizon mobility and tracking performance. Together, these results demonstrate that selective adversarial attacks are an effective driver for learning robust, long horizon humanoid motion skills.

## 参考
- http://arxiv.org/abs/2507.08303v3

