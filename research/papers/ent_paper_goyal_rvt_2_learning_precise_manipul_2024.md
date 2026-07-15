---
$id: ent_paper_goyal_rvt_2_learning_precise_manipul_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RVT-2: Learning Precise Manipulation from Few Demonstrations'
  zh: RVT-2
  ko: 'RVT-2: Learning Precise Manipulation from Few Demonstrations'
summary:
  en: 'RVT-2: Learning Precise Manipulation from Few Demonstrations (RVT-2), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, and published at Robotics - Science and Systems 2024.'
  zh: 'RVT-2: Learning Precise Manipulation from Few Demonstrations (RVT-2), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, and published at Robotics - Science and Systems 2024.'
  ko: 'RVT-2: Learning Precise Manipulation from Few Demonstrations (RVT-2), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, and published at Robotics - Science and Systems 2024.'
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
- rvt_2
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.08545v1.
sources:
- id: src_001
  type: website
  title: RVT-2 source
  url: https://doi.org/10.15607/RSS.2024.XX.055
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
In this work, we study how to build a robotic system that can solve multiple 3D manipulation tasks given language instructions. To be useful in industrial and household domains, such a system should be capable of learning new tasks with few demonstrations and solving them precisely. Prior works, like PerAct and RVT, have studied this problem, however, they often struggle with tasks requiring high precision. We study how to make them more effective, precise, and fast. Using a combination of architectural and system-level improvements, we propose RVT-2, a multitask 3D manipulation model that is 6X faster in training and 2X faster in inference than its predecessor RVT. RVT-2 achieves a new state-of-the-art on RLBench, improving the success rate from 65% to 82%. RVT-2 is also effective in the real world, where it can learn tasks requiring high precision, like picking up and inserting plugs, with just 10 demonstrations. Visual results, code, and trained model are provided at: https://robotic-view-transformer-2.github.io/.

## 核心内容
In this work, we study how to build a robotic system that can solve multiple 3D manipulation tasks given language instructions. To be useful in industrial and household domains, such a system should be capable of learning new tasks with few demonstrations and solving them precisely. Prior works, like PerAct and RVT, have studied this problem, however, they often struggle with tasks requiring high precision. We study how to make them more effective, precise, and fast. Using a combination of architectural and system-level improvements, we propose RVT-2, a multitask 3D manipulation model that is 6X faster in training and 2X faster in inference than its predecessor RVT. RVT-2 achieves a new state-of-the-art on RLBench, improving the success rate from 65% to 82%. RVT-2 is also effective in the real world, where it can learn tasks requiring high precision, like picking up and inserting plugs, with just 10 demonstrations. Visual results, code, and trained model are provided at: https://robotic-view-transformer-2.github.io/.

## 参考
- http://arxiv.org/abs/2406.08545v1

