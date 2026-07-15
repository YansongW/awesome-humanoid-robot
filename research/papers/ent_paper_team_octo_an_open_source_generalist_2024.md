---
$id: ent_paper_team_octo_an_open_source_generalist_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Octo: An Open-Source Generalist Robot Policy'
  zh: Octo
  ko: 'Octo: An Open-Source Generalist Robot Policy'
summary:
  en: 'Octo: An Open-Source Generalist Robot Policy (Octo), is a 2024 generalized vision-language-action model for robotic
    manipulation, introduced by UC Berkeley, Stanford, Carnegie Mellon University, and published at Robotics - Science and
    Systems 2024.'
  zh: 'Octo: An Open-Source Generalist Robot Policy (Octo), is a 2024 generalized vision-language-action model for robotic
    manipulation, introduced by UC Berkeley, Stanford, Carnegie Mellon University, and published at Robotics - Science and
    Systems 2024.'
  ko: 'Octo: An Open-Source Generalist Robot Policy (Octo), is a 2024 generalized vision-language-action model for robotic
    manipulation, introduced by UC Berkeley, Stanford, Carnegie Mellon University, and published at Robotics - Science and
    Systems 2024.'
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
- octo
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.12213v2.
sources:
- id: src_001
  type: website
  title: Octo source
  url: https://doi.org/10.15607/RSS.2024.XX.090
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies may be finetuned with only a little in-domain data, yet generalize broadly. However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, accommodate a variety of commonly used robotic platforms, and finetune readily and efficiently to new domains. In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation. As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date. It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs. In experiments across 9 robotic platforms, we demonstrate that Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces. We also perform detailed ablations of design decisions for the Octo model, from architecture to training data, to guide future research on building generalist robot models.

## 核心内容
Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies may be finetuned with only a little in-domain data, yet generalize broadly. However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, accommodate a variety of commonly used robotic platforms, and finetune readily and efficiently to new domains. In this work, we aim to lay the groundwork for developing open-source, widely applicable, generalist policies for robotic manipulation. As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date. It can be instructed via language commands or goal images and can be effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs. In experiments across 9 robotic platforms, we demonstrate that Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces. We also perform detailed ablations of design decisions for the Octo model, from architecture to training data, to guide future research on building generalist robot models.

## 参考
- http://arxiv.org/abs/2405.12213v2

