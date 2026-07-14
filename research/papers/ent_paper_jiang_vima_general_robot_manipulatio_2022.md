---
$id: ent_paper_jiang_vima_general_robot_manipulatio_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VIMA: General Robot Manipulation with Multimodal Prompts'
  zh: VIMA
  ko: 'VIMA: General Robot Manipulation with Multimodal Prompts'
summary:
  en: 'VIMA: General Robot Manipulation with Multimodal Prompts (VIMA), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, Stanford, Macalester College, Caltech, Tsinghua, UT Austin.'
  zh: 'VIMA: General Robot Manipulation with Multimodal Prompts (VIMA), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, Stanford, Macalester College, Caltech, Tsinghua, UT Austin.'
  ko: 'VIMA: General Robot Manipulation with Multimodal Prompts (VIMA), is a 2022 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, Stanford, Macalester College, Caltech, Tsinghua, UT Austin.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- vima
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.03094v2.
sources:
- id: src_001
  type: paper
  title: 'VIMA: General Robot Manipulation with Multimodal Prompts (arXiv)'
  url: https://arxiv.org/abs/2210.03094
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VIMA source
  url: https://doi.org/10.48550/arXiv.2210.03094
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
Prompt-based learning has emerged as a successful paradigm in natural language processing, where a single general-purpose language model can be instructed to perform any task specified by input prompts. Yet task specification in robotics comes in various forms, such as imitating one-shot demonstrations, following language instructions, and reaching visual goals. They are often considered different tasks and tackled by specialized models. We show that a wide spectrum of robot manipulation tasks can be expressed with multimodal prompts, interleaving textual and visual tokens. Accordingly, we develop a new simulation benchmark that consists of thousands of procedurally-generated tabletop tasks with multimodal prompts, 600K+ expert trajectories for imitation learning, and a four-level evaluation protocol for systematic generalization. We design a transformer-based robot agent, VIMA, that processes these prompts and outputs motor actions autoregressively. VIMA features a recipe that achieves strong model scalability and data efficiency. It outperforms alternative designs in the hardest zero-shot generalization setting by up to $2.9\times$ task success rate given the same training data. With $10\times$ less training data, VIMA still performs $2.7\times$ better than the best competing variant. Code and video demos are available at https://vimalabs.github.io/

## 核心内容
Prompt-based learning has emerged as a successful paradigm in natural language processing, where a single general-purpose language model can be instructed to perform any task specified by input prompts. Yet task specification in robotics comes in various forms, such as imitating one-shot demonstrations, following language instructions, and reaching visual goals. They are often considered different tasks and tackled by specialized models. We show that a wide spectrum of robot manipulation tasks can be expressed with multimodal prompts, interleaving textual and visual tokens. Accordingly, we develop a new simulation benchmark that consists of thousands of procedurally-generated tabletop tasks with multimodal prompts, 600K+ expert trajectories for imitation learning, and a four-level evaluation protocol for systematic generalization. We design a transformer-based robot agent, VIMA, that processes these prompts and outputs motor actions autoregressively. VIMA features a recipe that achieves strong model scalability and data efficiency. It outperforms alternative designs in the hardest zero-shot generalization setting by up to $2.9\times$ task success rate given the same training data. With $10\times$ less training data, VIMA still performs $2.7\times$ better than the best competing variant. Code and video demos are available at https://vimalabs.github.io/

## 参考
- http://arxiv.org/abs/2210.03094v2

