---
$id: ent_paper_li_gr_rl_going_dexterous_and_prec_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation'
  zh: GR-RL
  ko: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation'
summary:
  en: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (GR-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ByteDance Seed.'
  zh: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (GR-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ByteDance Seed.'
  ko: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (GR-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ByteDance Seed.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gr_rl
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01801v3.
sources:
- id: src_001
  type: paper
  title: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.01801
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GR-RL source
  url: https://doi.org/10.48550/arXiv.2512.01801
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present GR-RL, a robotic learning framework that turns a generalist vision-language-action (VLA) policy into a highly capable specialist for long-horizon dexterous manipulation. Assuming the optimality of human demonstrations is core to existing VLA policies. However, we claim that in highly dexterous and precise manipulation tasks, human demonstrations are noisy and suboptimal. GR-RL proposes a multi-stage training pipeline that filters, augments, and reinforces the demonstrations by reinforcement learning. First, GR-RL learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress. Specifically, we show that by directly applying offline RL with sparse reward, the resulting $Q$-values can be treated as a robust progress function. Next, we introduce morphological symmetry augmentation that greatly improves the generalization and performance of GR-RL. Lastly, to better align the VLA policy with its deployment behaviors for high-precision control, we perform online RL by learning a latent space noise predictor. With this pipeline, GR-RL is, to our knowledge, the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets with an 83.3% success rate, a task requiring long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction. We hope GR-RL provides a step toward enabling generalist robot foundation models to specialize into reliable real-world experts.

## 核心内容
We present GR-RL, a robotic learning framework that turns a generalist vision-language-action (VLA) policy into a highly capable specialist for long-horizon dexterous manipulation. Assuming the optimality of human demonstrations is core to existing VLA policies. However, we claim that in highly dexterous and precise manipulation tasks, human demonstrations are noisy and suboptimal. GR-RL proposes a multi-stage training pipeline that filters, augments, and reinforces the demonstrations by reinforcement learning. First, GR-RL learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress. Specifically, we show that by directly applying offline RL with sparse reward, the resulting $Q$-values can be treated as a robust progress function. Next, we introduce morphological symmetry augmentation that greatly improves the generalization and performance of GR-RL. Lastly, to better align the VLA policy with its deployment behaviors for high-precision control, we perform online RL by learning a latent space noise predictor. With this pipeline, GR-RL is, to our knowledge, the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets with an 83.3% success rate, a task requiring long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction. We hope GR-RL provides a step toward enabling generalist robot foundation models to specialize into reliable real-world experts.

## 参考
- http://arxiv.org/abs/2512.01801v3

