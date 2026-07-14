---
$id: ent_paper_lu_human_in_the_loop_online_rejec_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation
  zh: Hi-ORS
  ko: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation
summary:
  en: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation (Hi-ORS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tencent Robotics X.
  zh: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation (Hi-ORS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tencent Robotics X.
  ko: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation (Hi-ORS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tencent Robotics X.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hi_ors
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26406v1.
sources:
- id: src_001
  type: paper
  title: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation (arXiv)
  url: https://arxiv.org/abs/2510.26406
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Hi-ORS source
  url: https://doi.org/10.48550/arXiv.2510.26406
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) is widely used to produce robust robotic manipulation policies, but fine-tuning vision-language-action (VLA) models with RL can be unstable due to inaccurate value estimates and sparse supervision at intermediate steps. In contrast, imitation learning (IL) is easy to train but often underperforms due to its offline nature. In this paper, we propose Hi-ORS, a simple yet effective post-training method that utilizes rejection sampling to achieve both training stability and high robustness. Hi-ORS stabilizes value estimation by filtering out negatively rewarded samples during online fine-tuning, and adopts a reward-weighted supervised training objective to provide dense intermediate-step supervision. For systematic study, we develop an asynchronous inference-training framework that supports flexible online human-in-the-loop corrections, which serve as explicit guidance for learning error-recovery behaviors. Across three real-world tasks and two embodiments, Hi-ORS fine-tunes a pi-base policy to master contact-rich manipulation in just 1.5 hours of real-world training, outperforming RL and IL baselines by a substantial margin in both effectiveness and efficiency. Notably, the fine-tuned policy exhibits strong test-time scalability by reliably executing complex error-recovery behaviors to achieve better performance.

## 核心内容
Reinforcement learning (RL) is widely used to produce robust robotic manipulation policies, but fine-tuning vision-language-action (VLA) models with RL can be unstable due to inaccurate value estimates and sparse supervision at intermediate steps. In contrast, imitation learning (IL) is easy to train but often underperforms due to its offline nature. In this paper, we propose Hi-ORS, a simple yet effective post-training method that utilizes rejection sampling to achieve both training stability and high robustness. Hi-ORS stabilizes value estimation by filtering out negatively rewarded samples during online fine-tuning, and adopts a reward-weighted supervised training objective to provide dense intermediate-step supervision. For systematic study, we develop an asynchronous inference-training framework that supports flexible online human-in-the-loop corrections, which serve as explicit guidance for learning error-recovery behaviors. Across three real-world tasks and two embodiments, Hi-ORS fine-tunes a pi-base policy to master contact-rich manipulation in just 1.5 hours of real-world training, outperforming RL and IL baselines by a substantial margin in both effectiveness and efficiency. Notably, the fine-tuned policy exhibits strong test-time scalability by reliably executing complex error-recovery behaviors to achieve better performance.

## 参考
- http://arxiv.org/abs/2510.26406v1

