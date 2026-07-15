---
$id: ent_paper_xu_humanvla_towards_vision_langua_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid'
  zh: HumanVLA
  ko: 'HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid'
summary:
  en: 'HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid (HumanVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tencent Robotics X, and published at NIPS
    2024.'
  zh: 'HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid (HumanVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tencent Robotics X, and published at NIPS
    2024.'
  ko: 'HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid (HumanVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tencent Robotics X, and published at NIPS
    2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.19972v2.
sources:
- id: src_001
  type: website
  title: HumanVLA source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/215aeb07b5996c969c0123c3c6ee8f54-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Physical Human-Scene Interaction (HSI) plays a crucial role in numerous applications.   However, existing HSI techniques are limited to specific object dynamics and privileged information, which prevents the development of more comprehensive applications.   To address this limitation, we introduce HumanVLA for general object rearrangement directed by practical vision and language.   A teacher-student framework is utilized to develop HumanVLA.   A state-based teacher policy is trained first using goal-conditioned reinforcement learning and adversarial motion prior.   Then, it is distilled into a vision-language-action model via behavior cloning.   We propose several key insights to facilitate the large-scale learning process.   To support general object rearrangement by physical humanoid, we introduce a novel Human-in-the-Room dataset encompassing various rearrangement tasks.   Through extensive experiments and analysis, we demonstrate the effectiveness of the proposed approach.

## 核心内容
Physical Human-Scene Interaction (HSI) plays a crucial role in numerous applications.   However, existing HSI techniques are limited to specific object dynamics and privileged information, which prevents the development of more comprehensive applications.   To address this limitation, we introduce HumanVLA for general object rearrangement directed by practical vision and language.   A teacher-student framework is utilized to develop HumanVLA.   A state-based teacher policy is trained first using goal-conditioned reinforcement learning and adversarial motion prior.   Then, it is distilled into a vision-language-action model via behavior cloning.   We propose several key insights to facilitate the large-scale learning process.   To support general object rearrangement by physical humanoid, we introduce a novel Human-in-the-Room dataset encompassing various rearrangement tasks.   Through extensive experiments and analysis, we demonstrate the effectiveness of the proposed approach.

## 参考
- http://arxiv.org/abs/2406.19972v2

