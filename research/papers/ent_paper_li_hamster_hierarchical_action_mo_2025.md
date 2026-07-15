---
$id: ent_paper_li_hamster_hierarchical_action_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation'
  zh: HAMSTER
  ko: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation'
summary:
  en: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation (HAMSTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT CSAIL, Nvidia, and published at ICLR25.'
  zh: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation (HAMSTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT CSAIL, Nvidia, and published at ICLR25.'
  ko: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation (HAMSTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT CSAIL, Nvidia, and published at ICLR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hamster
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05485v4.
sources:
- id: src_001
  type: paper
  title: HAMSTER source
  url: https://openreview.net/forum?id=h7aQxzKbq6
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved in robotics. One fundamental challenge is the lack of robotic data, which are typically obtained through expensive on-robot operation. A promising remedy is to leverage cheaper, off-domain data such as action-free videos, hand-drawn sketches or simulation data. In this work, we posit that hierarchical vision-language-action (VLA) models can be more effective in utilizing off-domain data than standard monolithic VLA models that directly finetune vision-language models (VLMs) to predict actions. In particular, we study a class of hierarchical VLA models, where the high-level VLM is finetuned to produce a coarse 2D path indicating the desired robot end-effector trajectory given an RGB image and a task description. The intermediate 2D path prediction is then served as guidance to the low-level, 3D-aware control policy capable of precise manipulation. Doing so alleviates the high-level VLM from fine-grained action prediction, while reducing the low-level policy's burden on complex task-level reasoning. We show that, with the hierarchical design, the high-level VLM can transfer across significant domain gaps between the off-domain finetuning data and real-robot testing scenarios, including differences on embodiments, dynamics, visual appearances and task semantics, etc. In the real-robot experiments, we observe an average of 20% improvement in success rate across seven different axes of generalization over OpenVLA, representing a 50% relative gain. Visual results, code, and dataset are provided at: https://hamster-robot.github.io/

## 核心内容
Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved in robotics. One fundamental challenge is the lack of robotic data, which are typically obtained through expensive on-robot operation. A promising remedy is to leverage cheaper, off-domain data such as action-free videos, hand-drawn sketches or simulation data. In this work, we posit that hierarchical vision-language-action (VLA) models can be more effective in utilizing off-domain data than standard monolithic VLA models that directly finetune vision-language models (VLMs) to predict actions. In particular, we study a class of hierarchical VLA models, where the high-level VLM is finetuned to produce a coarse 2D path indicating the desired robot end-effector trajectory given an RGB image and a task description. The intermediate 2D path prediction is then served as guidance to the low-level, 3D-aware control policy capable of precise manipulation. Doing so alleviates the high-level VLM from fine-grained action prediction, while reducing the low-level policy's burden on complex task-level reasoning. We show that, with the hierarchical design, the high-level VLM can transfer across significant domain gaps between the off-domain finetuning data and real-robot testing scenarios, including differences on embodiments, dynamics, visual appearances and task semantics, etc. In the real-robot experiments, we observe an average of 20% improvement in success rate across seven different axes of generalization over OpenVLA, representing a 50% relative gain. Visual results, code, and dataset are provided at: https://hamster-robot.github.io/

## 参考
- http://arxiv.org/abs/2502.05485v4

