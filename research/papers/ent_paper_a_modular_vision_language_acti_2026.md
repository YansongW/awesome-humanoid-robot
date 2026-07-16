---
$id: ent_paper_a_modular_vision_language_acti_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Modular Vision-Language-Action Robotics Framework for Indoor Environments
  zh: A Modular Vision-Language-Action Robotics Framework for Indoor Environments
  ko: A Modular Vision-Language-Action Robotics Framework for Indoor Environments
summary:
  en: 'arXiv:2606.31144v1 Announce Type: new Abstract: This paper presents an integrated system for the CMU Vision-Language-Action
    (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions.
    Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation.
    The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time
    camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model.
    The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached.
    The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for
    the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language
    and robotic action.'
  zh: 'arXiv:2606.31144v1 Announce Type: new Abstract: This paper presents an integrated system for the CMU Vision-Language-Action
    (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions.
    Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation.
    The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time
    camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model.
    The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached.
    The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for
    the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language
    and robotic action.'
  ko: 'arXiv:2606.31144v1 Announce Type: new Abstract: This paper presents an integrated system for the CMU Vision-Language-Action
    (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions.
    Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation.
    The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time
    camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model.
    The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached.
    The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for
    the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language
    and robotic action.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_modular_vision_language_acti
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31144v1.
sources:
- id: src_001
  type: paper
  title: A Modular Vision-Language-Action Robotics Framework for Indoor Environments
  url: https://arxiv.org/abs/2606.31144
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents an integrated system for the CMU Vision-Language-Action (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions. Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation. The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model. The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached. The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language and robotic action.

## 核心内容
This paper presents an integrated system for the CMU Vision-Language-Action (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions. Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation. The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model. The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached. The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language and robotic action.

## 参考
- http://arxiv.org/abs/2606.31144v1

