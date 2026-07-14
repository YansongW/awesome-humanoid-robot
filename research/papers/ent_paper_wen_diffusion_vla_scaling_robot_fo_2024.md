---
$id: ent_paper_wen_diffusion_vla_scaling_robot_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression'
  zh: Diffusion-VLA
  ko: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression'
summary:
  en: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (Diffusion-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group,
    Shanghai University, and published at ICML25.'
  zh: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (Diffusion-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group,
    Shanghai University, and published at ICML25.'
  ko: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (Diffusion-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group,
    Shanghai University, and published at ICML25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.03293v3.
sources:
- id: src_001
  type: paper
  title: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (arXiv)'
  url: https://arxiv.org/abs/2412.03293
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Diffusion-VLA source
  url: https://doi.org/10.48550/arXiv.2412.03293
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we present DiffusionVLA, a novel framework that seamlessly combines the autoregression model with the diffusion model for learning visuomotor policy. Central to our approach is a next-token prediction objective, enabling the model to reason effectively over the user's query in the context of current observations. Subsequently, a diffusion model is attached to generate robust action outputs. To enhance policy learning through self-reasoning, we introduce a novel reasoning injection module that integrates reasoning phrases directly into the policy learning process. The whole framework is simple and flexible, making it easy to deploy and upgrade. We conduct extensive experiments using multiple real robots to validate the effectiveness of DiffusionVLA. Our tests include a challenging factory sorting task, where DiffusionVLA successfully categorizes objects, including those not seen during training. We observe that the reasoning module makes the model interpretable. It allows observers to understand the model thought process and identify potential causes of policy failures. Additionally, we test DiffusionVLA on a zero-shot bin-picking task, achieving 63.7\% accuracy on 102 previously unseen objects. Our method demonstrates robustness to visual changes, such as distractors and new backgrounds, and easily adapts to new embodiments. Furthermore, DiffusionVLA can follow novel instructions and retain conversational ability. Notably, DiffusionVLA is data-efficient and fast at inference; our smallest DiffusionVLA-2B runs 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for a complex task. Finally, we scale the model from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size.

## 核心内容
In this paper, we present DiffusionVLA, a novel framework that seamlessly combines the autoregression model with the diffusion model for learning visuomotor policy. Central to our approach is a next-token prediction objective, enabling the model to reason effectively over the user's query in the context of current observations. Subsequently, a diffusion model is attached to generate robust action outputs. To enhance policy learning through self-reasoning, we introduce a novel reasoning injection module that integrates reasoning phrases directly into the policy learning process. The whole framework is simple and flexible, making it easy to deploy and upgrade. We conduct extensive experiments using multiple real robots to validate the effectiveness of DiffusionVLA. Our tests include a challenging factory sorting task, where DiffusionVLA successfully categorizes objects, including those not seen during training. We observe that the reasoning module makes the model interpretable. It allows observers to understand the model thought process and identify potential causes of policy failures. Additionally, we test DiffusionVLA on a zero-shot bin-picking task, achieving 63.7\% accuracy on 102 previously unseen objects. Our method demonstrates robustness to visual changes, such as distractors and new backgrounds, and easily adapts to new embodiments. Furthermore, DiffusionVLA can follow novel instructions and retain conversational ability. Notably, DiffusionVLA is data-efficient and fast at inference; our smallest DiffusionVLA-2B runs 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for a complex task. Finally, we scale the model from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size.

## 参考
- http://arxiv.org/abs/2412.03293v3

