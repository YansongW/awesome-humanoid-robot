---
$id: ent_paper_fu_minddrive_a_vision_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning'
  zh: MindDrive
  ko: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning'
summary:
  en: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning (MindDrive), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Xiaomi EV.'
  zh: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning (MindDrive), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Xiaomi EV.'
  ko: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning (MindDrive), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Xiaomi EV.'
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
- minddrive
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13636v3.
sources:
- id: src_001
  type: paper
  title: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2512.13636
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MindDrive source
  url: https://doi.org/10.48550/arXiv.2512.13636
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Current Vision-Language-Action (VLA) paradigms in autonomous driving primarily rely on Imitation Learning (IL), which introduces inherent challenges such as distribution shift and causal confusion. Online Reinforcement Learning offers a promising pathway to address these issues through trial-and-error learning. However, applying online reinforcement learning to VLA models in autonomous driving is hindered by inefficient exploration in continuous action spaces. To overcome this limitation, we propose MindDrive, a VLA framework comprising a large language model (LLM) with two distinct sets of LoRA parameters. The one LLM serves as a Decision Expert for scenario reasoning and driving decision-making, while the other acts as an Action Expert that dynamically maps linguistic decisions into feasible trajectories. By feeding trajectory-level rewards back into the reasoning space, MindDrive enables trial-and-error learning over a finite set of discrete linguistic driving decisions, instead of operating directly in a continuous action space. This approach effectively balances optimal decision-making in complex scenarios, human-like driving behavior, and efficient exploration in online reinforcement learning. Using the lightweight Qwen-0.5B LLM, MindDrive achieves Driving Score (DS) of 78.04 and Success Rate (SR) of 55.09% on the challenging Bench2Drive benchmark. To the best of our knowledge, this is the first work to demonstrate the effectiveness of online reinforcement learning for the VLA model in autonomous driving.

## 核心内容
Current Vision-Language-Action (VLA) paradigms in autonomous driving primarily rely on Imitation Learning (IL), which introduces inherent challenges such as distribution shift and causal confusion. Online Reinforcement Learning offers a promising pathway to address these issues through trial-and-error learning. However, applying online reinforcement learning to VLA models in autonomous driving is hindered by inefficient exploration in continuous action spaces. To overcome this limitation, we propose MindDrive, a VLA framework comprising a large language model (LLM) with two distinct sets of LoRA parameters. The one LLM serves as a Decision Expert for scenario reasoning and driving decision-making, while the other acts as an Action Expert that dynamically maps linguistic decisions into feasible trajectories. By feeding trajectory-level rewards back into the reasoning space, MindDrive enables trial-and-error learning over a finite set of discrete linguistic driving decisions, instead of operating directly in a continuous action space. This approach effectively balances optimal decision-making in complex scenarios, human-like driving behavior, and efficient exploration in online reinforcement learning. Using the lightweight Qwen-0.5B LLM, MindDrive achieves Driving Score (DS) of 78.04 and Success Rate (SR) of 55.09% on the challenging Bench2Drive benchmark. To the best of our knowledge, this is the first work to demonstrate the effectiveness of online reinforcement learning for the VLA model in autonomous driving.

## 参考
- http://arxiv.org/abs/2512.13636v3

