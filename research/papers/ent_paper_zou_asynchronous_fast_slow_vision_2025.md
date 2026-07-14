---
$id: ent_paper_zou_asynchronous_fast_slow_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation
  zh: DuoCore-FS
  ko: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation
summary:
  en: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation (DuoCore-FS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Astribot.
  zh: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation (DuoCore-FS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Astribot.
  ko: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation (DuoCore-FS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Astribot.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- duocore_fs
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20188v1.
sources:
- id: src_001
  type: paper
  title: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation (arXiv)
  url: https://arxiv.org/abs/2512.20188
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DuoCore-FS source
  url: https://doi.org/10.48550/arXiv.2512.20188
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Most Vision-Language-Action (VLA) systems integrate a Vision-Language Model (VLM) for semantic reasoning with an action expert generating continuous action signals, yet both typically run at a single unified frequency. As a result, policy performance is constrained by the low inference speed of large VLMs. This mandatory synchronous execution severely limits control stability and real-time performance in whole-body robotic manipulation, which involves more joints, larger motion spaces, and dynamically changing views. We introduce a truly asynchronous Fast-Slow VLA framework (DuoCore-FS), organizing the system into a fast pathway for high-frequency action generation and a slow pathway for rich VLM reasoning. The system is characterized by two key features. First, a latent representation buffer bridges the slow and fast systems. It stores instruction semantics and action-reasoning representation aligned with the scene-instruction context, providing high-level guidance to the fast pathway. Second, a whole-body action tokenizer provides a compact, unified representation of whole-body actions. Importantly, the VLM and action expert are still jointly trained end-to-end, preserving unified policy learning while enabling asynchronous execution. DuoCore-FS supports a 3B-parameter VLM while achieving 30 Hz whole-body action-chunk generation, approximately three times as fast as prior VLA models with comparable model sizes. Real-world whole-body manipulation experiments demonstrate improved task success rates and significantly enhanced responsiveness compared to synchronous Fast-Slow VLA baselines. The implementation of DuoCore-FS, including training, inference, and deployment, is provided to commercial users by Astribot as part of the Astribot robotic platform.

## 核心内容
Most Vision-Language-Action (VLA) systems integrate a Vision-Language Model (VLM) for semantic reasoning with an action expert generating continuous action signals, yet both typically run at a single unified frequency. As a result, policy performance is constrained by the low inference speed of large VLMs. This mandatory synchronous execution severely limits control stability and real-time performance in whole-body robotic manipulation, which involves more joints, larger motion spaces, and dynamically changing views. We introduce a truly asynchronous Fast-Slow VLA framework (DuoCore-FS), organizing the system into a fast pathway for high-frequency action generation and a slow pathway for rich VLM reasoning. The system is characterized by two key features. First, a latent representation buffer bridges the slow and fast systems. It stores instruction semantics and action-reasoning representation aligned with the scene-instruction context, providing high-level guidance to the fast pathway. Second, a whole-body action tokenizer provides a compact, unified representation of whole-body actions. Importantly, the VLM and action expert are still jointly trained end-to-end, preserving unified policy learning while enabling asynchronous execution. DuoCore-FS supports a 3B-parameter VLM while achieving 30 Hz whole-body action-chunk generation, approximately three times as fast as prior VLA models with comparable model sizes. Real-world whole-body manipulation experiments demonstrate improved task success rates and significantly enhanced responsiveness compared to synchronous Fast-Slow VLA baselines. The implementation of DuoCore-FS, including training, inference, and deployment, is provided to commercial users by Astribot as part of the Astribot robotic platform.

## 参考
- http://arxiv.org/abs/2512.20188v1

