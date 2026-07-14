---
$id: ent_paper_li_cogact_a_foundational_vision_l_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation'
  zh: CogACT
  ko: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation'
summary:
  en: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation (CogACT),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Microsoft Research
    Asia, USTC, Institute of Microelectronics, CAS.'
  zh: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation (CogACT),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Microsoft Research
    Asia, USTC, Institute of Microelectronics, CAS.'
  ko: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation (CogACT),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Microsoft Research
    Asia, USTC, Institute of Microelectronics, CAS.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cogact
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.19650v1.
sources:
- id: src_001
  type: paper
  title: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation
    (arXiv)'
  url: https://arxiv.org/abs/2411.19650
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CogACT source
  url: https://doi.org/10.48550/arXiv.2411.19650
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
The advancement of large Vision-Language-Action (VLA) models has significantly improved robotic manipulation in terms of language-guided task execution and generalization to unseen scenarios. While existing VLAs adapted from pretrained large Vision-Language-Models (VLM) have demonstrated promising generalizability, their task performance is still unsatisfactory as indicated by the low tasks success rates in different environments. In this paper, we present a new advanced VLA architecture derived from VLM. Unlike previous works that directly repurpose VLM for action prediction by simple action quantization, we propose a omponentized VLA architecture that has a specialized action module conditioned on VLM output. We systematically study the design of the action module and demonstrates the strong performance enhancement with diffusion action transformers for action sequence modeling, as well as their favorable scaling behaviors. We also conduct comprehensive experiments and ablation studies to evaluate the efficacy of our models with varied designs. The evaluation on 5 robot embodiments in simulation and real work shows that our model not only significantly surpasses existing VLAs in task performance and but also exhibits remarkable adaptation to new robots and generalization to unseen objects and backgrounds. It exceeds the average success rates of OpenVLA which has similar model size (7B) with ours by over 35% in simulated evaluation and 55% in real robot experiments. It also outperforms the large RT-2-X model (55B) by 18% absolute success rates in simulation. Code and models can be found on our project page (https://cogact.github.io/).

## 核心内容
The advancement of large Vision-Language-Action (VLA) models has significantly improved robotic manipulation in terms of language-guided task execution and generalization to unseen scenarios. While existing VLAs adapted from pretrained large Vision-Language-Models (VLM) have demonstrated promising generalizability, their task performance is still unsatisfactory as indicated by the low tasks success rates in different environments. In this paper, we present a new advanced VLA architecture derived from VLM. Unlike previous works that directly repurpose VLM for action prediction by simple action quantization, we propose a omponentized VLA architecture that has a specialized action module conditioned on VLM output. We systematically study the design of the action module and demonstrates the strong performance enhancement with diffusion action transformers for action sequence modeling, as well as their favorable scaling behaviors. We also conduct comprehensive experiments and ablation studies to evaluate the efficacy of our models with varied designs. The evaluation on 5 robot embodiments in simulation and real work shows that our model not only significantly surpasses existing VLAs in task performance and but also exhibits remarkable adaptation to new robots and generalization to unseen objects and backgrounds. It exceeds the average success rates of OpenVLA which has similar model size (7B) with ours by over 35% in simulated evaluation and 55% in real robot experiments. It also outperforms the large RT-2-X model (55B) by 18% absolute success rates in simulation. Code and models can be found on our project page (https://cogact.github.io/).

## 参考
- http://arxiv.org/abs/2411.19650v1

