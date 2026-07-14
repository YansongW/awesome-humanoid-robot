---
$id: ent_paper_yang_lohovla_a_unified_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks'
  zh: LoHoVLA
  ko: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks'
summary:
  en: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (LoHoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, ShanghaiTech University, Shanghai Jiao Tong University.'
  zh: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (LoHoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, ShanghaiTech University, Shanghai Jiao Tong University.'
  ko: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (LoHoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, ShanghaiTech University, Shanghai Jiao Tong University.'
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
- lohovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.00411v1.
sources:
- id: src_001
  type: paper
  title: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (arXiv)'
  url: https://arxiv.org/abs/2506.00411
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LoHoVLA source
  url: https://doi.org/10.48550/arXiv.2506.00411
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Real-world embodied agents face long-horizon tasks, characterized by high-level goals demanding multi-step solutions beyond single actions. Successfully navigating these requires both high-level task planning (i.e., decomposing goals into sub-tasks) and low-level motion control (i.e., generating precise robot actions). While existing vision language action (VLA) models and hierarchical architectures offer potential in embodied tasks, the former often falter in planning, and the latter can suffer from coordination issues, both hampering performance. We introduce a new unified VLA framework for long-horizon tasks, dubbed LoHoVLA, to overcome these limitations. LoHoVLA leverages a large pretrained vision language model (VLM) as the backbone to jointly generate language and action tokens for sub-task generation and robot action prediction, respectively. This shared representation promotes better generalization across tasks. Additionally, LoHoVLA embraces a hierarchical closed-loop control mechanism to mitigate errors originating from both high-level planning and low-level control. To train LoHoVLA, we introduce LoHoSet, a dataset built on the Ravens simulator, containing 20 long-horizon tasks, each with 1,000 expert demonstrations composed of visual observations, linguistic goals, sub-tasks, and robot actions. Experimental results show that LoHoVLA significantly surpasses both hierarchical and standard VLA approaches on long-horizon embodied tasks in the Ravens simulator. These findings underscore the promise of unified architectures for advancing generalizable embodied intelligence.

## 核心内容
Real-world embodied agents face long-horizon tasks, characterized by high-level goals demanding multi-step solutions beyond single actions. Successfully navigating these requires both high-level task planning (i.e., decomposing goals into sub-tasks) and low-level motion control (i.e., generating precise robot actions). While existing vision language action (VLA) models and hierarchical architectures offer potential in embodied tasks, the former often falter in planning, and the latter can suffer from coordination issues, both hampering performance. We introduce a new unified VLA framework for long-horizon tasks, dubbed LoHoVLA, to overcome these limitations. LoHoVLA leverages a large pretrained vision language model (VLM) as the backbone to jointly generate language and action tokens for sub-task generation and robot action prediction, respectively. This shared representation promotes better generalization across tasks. Additionally, LoHoVLA embraces a hierarchical closed-loop control mechanism to mitigate errors originating from both high-level planning and low-level control. To train LoHoVLA, we introduce LoHoSet, a dataset built on the Ravens simulator, containing 20 long-horizon tasks, each with 1,000 expert demonstrations composed of visual observations, linguistic goals, sub-tasks, and robot actions. Experimental results show that LoHoVLA significantly surpasses both hierarchical and standard VLA approaches on long-horizon embodied tasks in the Ravens simulator. These findings underscore the promise of unified architectures for advancing generalizable embodied intelligence.

## 参考
- http://arxiv.org/abs/2506.00411v1

