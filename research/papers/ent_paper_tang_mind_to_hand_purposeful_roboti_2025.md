---
$id: ent_paper_tang_mind_to_hand_purposeful_roboti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning'
  zh: Mind to Hand
  ko: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning'
summary:
  en: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning (Mind to Hand), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Astribot.'
  zh: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning (Mind to Hand), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Astribot.'
  ko: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning (Mind to Hand), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Astribot.'
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
- mind_to_hand
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08580v2.
sources:
- id: src_001
  type: paper
  title: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning (arXiv)'
  url: https://arxiv.org/abs/2512.08580
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Mind to Hand source
  url: https://doi.org/10.48550/arXiv.2512.08580
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans act with context and intention, with reasoning playing a central role. While internet-scale data has enabled broad reasoning capabilities in AI systems, grounding these abilities in physical action remains a major challenge. We introduce Lumo-1, a generalist vision-language-action (VLA) model that unifies robot reasoning ("mind") with robot action ("hand"). Our approach builds upon the general multi-modal reasoning capabilities of pre-trained vision-language models (VLMs), progressively extending them to embodied reasoning and action prediction, and ultimately towards structured reasoning and reasoning-action alignment. This results in a three-stage pre-training pipeline: (1) Continued VLM pre-training on curated vision-language data to enhance embodied reasoning skills such as planning, spatial understanding, and trajectory prediction; (2) Co-training on cross-embodiment robot data alongside vision-language data; and (3) Action training with reasoning process on trajectories collected on Astribot S1, a bimanual mobile manipulator with human-like dexterity and agility. Finally, we integrate reinforcement learning to further refine reasoning-action consistency and close the loop between semantic inference and motor control. Extensive experiments demonstrate that Lumo-1 achieves significant performance improvements in embodied vision-language reasoning, a critical component for generalist robotic control. Real-world evaluations further show that Lumo-1 surpasses strong baselines across a wide range of challenging robotic tasks, with strong generalization to novel objects and environments, excelling particularly in long-horizon tasks and responding to human-natural instructions that require reasoning over strategy, concepts and space.

## 核心内容
Humans act with context and intention, with reasoning playing a central role. While internet-scale data has enabled broad reasoning capabilities in AI systems, grounding these abilities in physical action remains a major challenge. We introduce Lumo-1, a generalist vision-language-action (VLA) model that unifies robot reasoning ("mind") with robot action ("hand"). Our approach builds upon the general multi-modal reasoning capabilities of pre-trained vision-language models (VLMs), progressively extending them to embodied reasoning and action prediction, and ultimately towards structured reasoning and reasoning-action alignment. This results in a three-stage pre-training pipeline: (1) Continued VLM pre-training on curated vision-language data to enhance embodied reasoning skills such as planning, spatial understanding, and trajectory prediction; (2) Co-training on cross-embodiment robot data alongside vision-language data; and (3) Action training with reasoning process on trajectories collected on Astribot S1, a bimanual mobile manipulator with human-like dexterity and agility. Finally, we integrate reinforcement learning to further refine reasoning-action consistency and close the loop between semantic inference and motor control. Extensive experiments demonstrate that Lumo-1 achieves significant performance improvements in embodied vision-language reasoning, a critical component for generalist robotic control. Real-world evaluations further show that Lumo-1 surpasses strong baselines across a wide range of challenging robotic tasks, with strong generalization to novel objects and environments, excelling particularly in long-horizon tasks and responding to human-natural instructions that require reasoning over strategy, concepts and space.

## 参考
- http://arxiv.org/abs/2512.08580v2

