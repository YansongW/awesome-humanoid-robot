---
$id: ent_paper_yadav_robust_finetuning_of_vision_la_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging
  zh: RETAIN
  ko: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging
summary:
  en: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging (RETAIN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.
  zh: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging (RETAIN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.
  ko: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging (RETAIN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.
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
- retain
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08333v3.
sources:
- id: src_001
  type: paper
  title: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging (arXiv)
  url: https://arxiv.org/abs/2512.08333
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RETAIN source
  url: https://doi.org/10.48550/arXiv.2512.08333
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generalist robot policies, trained on large and diverse datasets, have demonstrated the ability to generalize across a wide spectrum of behaviors, enabling a single policy to act in varied real-world environments. However, they still fall short on new tasks not covered in the training data. When finetuned on limited demonstrations of a new task, these policies often overfit to the specific demonstrations--not only losing their prior abilities to solve a wide variety of generalist tasks but also failing to generalize within the new task itself. In this work, we aim to develop a method that preserves the generalization capabilities of the generalist policy during finetuning, allowing a single policy to robustly incorporate a new skill into its repertoire. Our goal is a single policy that both learns to generalize to variations of the new task and retains the broad competencies gained from pretraining. We show that this can be achieved through a simple yet effective strategy: interpolating the weights of a finetuned model with that of the pretrained model. We show, across extensive simulated and real-world experiments, that such model merging produces a single model that inherits the generalist abilities of the base model and learns to solve the new task robustly, outperforming both the pretrained and finetuned model on out-of-distribution variations of the new task. Moreover, we show that model merging performance scales with the amount of pretraining data, and enables continual acquisition of new skills in a lifelong learning setting, without sacrificing previously learned generalist abilities.

## 核心内容
Generalist robot policies, trained on large and diverse datasets, have demonstrated the ability to generalize across a wide spectrum of behaviors, enabling a single policy to act in varied real-world environments. However, they still fall short on new tasks not covered in the training data. When finetuned on limited demonstrations of a new task, these policies often overfit to the specific demonstrations--not only losing their prior abilities to solve a wide variety of generalist tasks but also failing to generalize within the new task itself. In this work, we aim to develop a method that preserves the generalization capabilities of the generalist policy during finetuning, allowing a single policy to robustly incorporate a new skill into its repertoire. Our goal is a single policy that both learns to generalize to variations of the new task and retains the broad competencies gained from pretraining. We show that this can be achieved through a simple yet effective strategy: interpolating the weights of a finetuned model with that of the pretrained model. We show, across extensive simulated and real-world experiments, that such model merging produces a single model that inherits the generalist abilities of the base model and learns to solve the new task robustly, outperforming both the pretrained and finetuned model on out-of-distribution variations of the new task. Moreover, we show that model merging performance scales with the amount of pretraining data, and enables continual acquisition of new skills in a lifelong learning setting, without sacrificing previously learned generalist abilities.

## 参考
- http://arxiv.org/abs/2512.08333v3

