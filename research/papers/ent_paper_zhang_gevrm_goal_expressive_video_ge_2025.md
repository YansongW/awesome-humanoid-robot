---
$id: ent_paper_zhang_gevrm_goal_expressive_video_ge_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation'
  zh: GEVRM
  ko: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation'
summary:
  en: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation (GEVRM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Westlake University, and published at ICLR25.'
  zh: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation (GEVRM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Westlake University, and published at ICLR25.'
  ko: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation (GEVRM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Westlake University, and published at ICLR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gevrm
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.09268v2.
sources:
- id: src_001
  type: paper
  title: GEVRM source
  url: https://openreview.net/forum?id=hPWWXpCaJ7
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
With the rapid development of embodied artificial intelligence, significant progress has been made in vision-language-action (VLA) models for general robot decision-making. However, the majority of existing VLAs fail to account for the inevitable external perturbations encountered during deployment. These perturbations introduce unforeseen state information to the VLA, resulting in inaccurate actions and consequently, a significant decline in generalization performance. The classic internal model control (IMC) principle demonstrates that a closed-loop system with an internal model that includes external input signals can accurately track the reference input and effectively offset the disturbance. We propose a novel closed-loop VLA method GEVRM that integrates the IMC principle to enhance the robustness of robot visual manipulation. The text-guided video generation model in GEVRM can generate highly expressive future visual planning goals. Simultaneously, we evaluate perturbations by simulating responses, which are called internal embeddings and optimized through prototype contrastive learning. This allows the model to implicitly infer and distinguish perturbations from the external environment. The proposed GEVRM achieves state-of-the-art performance on both standard and perturbed CALVIN benchmarks and shows significant improvements in realistic robot tasks.

## 核心内容
With the rapid development of embodied artificial intelligence, significant progress has been made in vision-language-action (VLA) models for general robot decision-making. However, the majority of existing VLAs fail to account for the inevitable external perturbations encountered during deployment. These perturbations introduce unforeseen state information to the VLA, resulting in inaccurate actions and consequently, a significant decline in generalization performance. The classic internal model control (IMC) principle demonstrates that a closed-loop system with an internal model that includes external input signals can accurately track the reference input and effectively offset the disturbance. We propose a novel closed-loop VLA method GEVRM that integrates the IMC principle to enhance the robustness of robot visual manipulation. The text-guided video generation model in GEVRM can generate highly expressive future visual planning goals. Simultaneously, we evaluate perturbations by simulating responses, which are called internal embeddings and optimized through prototype contrastive learning. This allows the model to implicitly infer and distinguish perturbations from the external environment. The proposed GEVRM achieves state-of-the-art performance on both standard and perturbed CALVIN benchmarks and shows significant improvements in realistic robot tasks.

## 参考
- http://arxiv.org/abs/2502.09268v2

