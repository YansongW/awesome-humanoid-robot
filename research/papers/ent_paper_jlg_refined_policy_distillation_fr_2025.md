---
$id: ent_paper_jlg_refined_policy_distillation_fr_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Refined Policy Distillation: From VLA Generalists to RL Experts'
  zh: RPD
  ko: 'Refined Policy Distillation: From VLA Generalists to RL Experts'
summary:
  en: 'Refined Policy Distillation: From VLA Generalists to RL Experts (RPD), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Technology Nuremberg, and published at IROS25.'
  zh: 'Refined Policy Distillation: From VLA Generalists to RL Experts (RPD), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Technology Nuremberg, and published at IROS25.'
  ko: 'Refined Policy Distillation: From VLA Generalists to RL Experts (RPD), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Technology Nuremberg, and published at IROS25.'
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
- rpd
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.05833v2.
sources:
- id: src_001
  type: website
  title: RPD source
  url: https://doi.org/10.1109/IROS60139.2025.11246761
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action Models (VLAs) have demonstrated remarkable generalization capabilities in real-world experiments. However, their success rates are often not on par with expert policies, and they require fine-tuning when the setup changes. In this work, we introduce Refined Policy Distillation (RPD), a novel Reinforcement Learning (RL)-based policy refinement method that bridges this performance gap through a combination of on-policy RL with behavioral cloning. The core idea of RPD is to distill and refine VLAs into compact, high-performing expert policies by guiding the student policy during RL exploration using the actions of a teacher VLA, resulting in increased sample efficiency and faster convergence. We complement our method by fine-tuned versions of Octo and OpenVLA for ManiSkill3 to evaluate RPD in simulation. While this is a key requirement for applying RL, it also yields new insights beyond existing studies on VLA performance in real-world settings. Our experimental results across various manipulation tasks show that RPD enables the RL student to learn expert policies that outperform the VLA teacher in both dense and sparse reward settings, while also achieving faster convergence than the RL baseline. Our approach is even robust to changes in camera perspective and can generalize to task variations that the underlying VLA cannot solve. Our code, dataset, VLA checkpoints, and videos are available at https://refined-policy-distillation.github.io

## 核心内容
Vision-Language-Action Models (VLAs) have demonstrated remarkable generalization capabilities in real-world experiments. However, their success rates are often not on par with expert policies, and they require fine-tuning when the setup changes. In this work, we introduce Refined Policy Distillation (RPD), a novel Reinforcement Learning (RL)-based policy refinement method that bridges this performance gap through a combination of on-policy RL with behavioral cloning. The core idea of RPD is to distill and refine VLAs into compact, high-performing expert policies by guiding the student policy during RL exploration using the actions of a teacher VLA, resulting in increased sample efficiency and faster convergence. We complement our method by fine-tuned versions of Octo and OpenVLA for ManiSkill3 to evaluate RPD in simulation. While this is a key requirement for applying RL, it also yields new insights beyond existing studies on VLA performance in real-world settings. Our experimental results across various manipulation tasks show that RPD enables the RL student to learn expert policies that outperform the VLA teacher in both dense and sparse reward settings, while also achieving faster convergence than the RL baseline. Our approach is even robust to changes in camera perspective and can generalize to task variations that the underlying VLA cannot solve. Our code, dataset, VLA checkpoints, and videos are available at https://refined-policy-distillation.github.io

## 参考
- http://arxiv.org/abs/2503.05833v2

