---
$id: ent_paper_fang_dualvla_building_a_generalizab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action'
  zh: DualVLA
  ko: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action'
summary:
  en: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (DualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by MoE Key Laboratory of Brain-inspired Intelligent
    Perception and Cognition, University of Science and Technology of China, State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, CUHK.'
  zh: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (DualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by MoE Key Laboratory of Brain-inspired Intelligent
    Perception and Cognition, University of Science and Technology of China, State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, CUHK.'
  ko: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (DualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by MoE Key Laboratory of Brain-inspired Intelligent
    Perception and Cognition, University of Science and Technology of China, State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, CUHK.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dualvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22134v1.
sources:
- id: src_001
  type: paper
  title: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (arXiv)'
  url: https://arxiv.org/abs/2511.22134
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DualVLA source
  url: https://doi.org/10.48550/arXiv.2511.22134
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To build a generalizable Vision-Language-Action (VLA) model with strong reasoning ability, a common strategy is to first train a specialist VLA on robot demonstrations to acquire reliable manipulation skills, and then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. However, we observe that the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon we refer to as action degeneration. To address this issue, we propose DualVLA, which enhances action performance through carefully designed post-training while still preserving reasoning capability. We first introduce a dual-layer data pruning method that removes redundant embodied reasoning, preventing it from adversely influencing action learning. To further strengthen action generation, we design a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains while maintaining reasoning ability. To fill the evaluation gap for generalist VLAs, we also propose VLA Score, which decouples VLA capability into reasoning, intention, action, and alignment dimensions for a more fine-grained assessment. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks, demonstrating a stronger balance between precise action execution and multimodal understanding. Project Website: https://costaliya.github.io/DualVLA/.

## 核心内容
To build a generalizable Vision-Language-Action (VLA) model with strong reasoning ability, a common strategy is to first train a specialist VLA on robot demonstrations to acquire reliable manipulation skills, and then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. However, we observe that the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon we refer to as action degeneration. To address this issue, we propose DualVLA, which enhances action performance through carefully designed post-training while still preserving reasoning capability. We first introduce a dual-layer data pruning method that removes redundant embodied reasoning, preventing it from adversely influencing action learning. To further strengthen action generation, we design a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains while maintaining reasoning ability. To fill the evaluation gap for generalist VLAs, we also propose VLA Score, which decouples VLA capability into reasoning, intention, action, and alignment dimensions for a more fine-grained assessment. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks, demonstrating a stronger balance between precise action execution and multimodal understanding. Project Website: https://costaliya.github.io/DualVLA/.

## 参考
- http://arxiv.org/abs/2511.22134v1

