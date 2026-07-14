---
$id: ent_paper_hierarchical_vision_language_p_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
  zh: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
  ko: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
summary:
  en: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation is a 2025 work on manipulation for humanoid
    robots.
  zh: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation is a 2025 work on manipulation for humanoid
    robots.
  ko: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation is a 2025 work on manipulation for humanoid
    robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hierarchical_vision_language_p
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.22827v3.
sources:
- id: src_001
  type: paper
  title: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation (arXiv)
  url: https://arxiv.org/abs/2506.22827
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Enabling humanoid robots to reliably execute complex multi-step manipulation tasks is crucial for their effective deployment in industrial and household environments. This paper presents a hierarchical planning and control framework designed to achieve reliable multi-step humanoid manipulation. The proposed system comprises three layers: (1) a low-level RL-based controller responsible for tracking whole-body motion targets; (2) a mid-level set of skill policies trained via imitation learning that produce motion targets for different steps of a task; and (3) a high-level vision-language planning module that determines which skills should be executed and also monitors their completion in real-time using pretrained vision-language models (VLMs). Experimental validation is performed on a Unitree G1 humanoid robot executing a non-prehensile pick-and-place task. Over 40 real-world trials, the hierarchical system achieved a 73% success rate in completing the full manipulation sequence. These experiments confirm the feasibility of the proposed hierarchical system, highlighting the benefits of VLM-based skill planning and monitoring for multi-step manipulation scenarios. See https://vlp-humanoid.github.io/ for video demonstrations of the policy rollout.

## 核心内容
Enabling humanoid robots to reliably execute complex multi-step manipulation tasks is crucial for their effective deployment in industrial and household environments. This paper presents a hierarchical planning and control framework designed to achieve reliable multi-step humanoid manipulation. The proposed system comprises three layers: (1) a low-level RL-based controller responsible for tracking whole-body motion targets; (2) a mid-level set of skill policies trained via imitation learning that produce motion targets for different steps of a task; and (3) a high-level vision-language planning module that determines which skills should be executed and also monitors their completion in real-time using pretrained vision-language models (VLMs). Experimental validation is performed on a Unitree G1 humanoid robot executing a non-prehensile pick-and-place task. Over 40 real-world trials, the hierarchical system achieved a 73% success rate in completing the full manipulation sequence. These experiments confirm the feasibility of the proposed hierarchical system, highlighting the benefits of VLM-based skill planning and monitoring for multi-step manipulation scenarios. See https://vlp-humanoid.github.io/ for video demonstrations of the policy rollout.

## 参考
- http://arxiv.org/abs/2506.22827v3

