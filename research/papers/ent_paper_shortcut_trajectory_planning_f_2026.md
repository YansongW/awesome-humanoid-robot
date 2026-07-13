---
$id: ent_paper_shortcut_trajectory_planning_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning
  zh: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning
  ko: ''
summary:
  en: "arXiv:2607.09336v1 Announce Type: cross \nAbstract: Diffusion-based trajectory\
    \ planners have shown strong performance in offline reinforcement learning, but\
    \ their iterative denoising process often incurs high inference cost. Consistency-based\
    \ planners reduce the number of sampling steps, yet they typically rely on a two-stage\
    \ teacher--student distillation pipeline that increases training cost and may\
    \ introduce instability. We propose Shortcut Trajectory Planning (STP), an offline\
    \ model-based reinforcement learning framework that incorporates shortcut models\
    \ as efficient trajectory generators. STP trains a conditional shortcut trajectory\
    \ model in a single stage, supports adjustable one-step and few-step inference\
    \ through step-size conditioning, and selects candidate plans using a critic augmented\
    \ with feasibility-aware correction. Across standard D4RL benchmarks, including\
    \ locomotion, navigation, manipulation, and dexterous control tasks, STP achieves\
    \ strong performance while simplifying the training pipeline for fast generative\
    \ planning."
  zh: "arXiv:2607.09336v1 Announce Type: cross \nAbstract: Diffusion-based trajectory\
    \ planners have shown strong performance in offline reinforcement learning, but\
    \ their iterative denoising process often incurs high inference cost. Consistency-based\
    \ planners reduce the number of sampling steps, yet they typically rely on a two-stage\
    \ teacher--student distillation pipeline that increases training cost and may\
    \ introduce instability. We propose Shortcut Trajectory Planning (STP), an offline\
    \ model-based reinforcement learning framework that incorporates shortcut models\
    \ as efficient trajectory generators. STP trains a conditional shortcut trajectory\
    \ model in a single stage, supports adjustable one-step and few-step inference\
    \ through step-size conditioning, and selects candidate plans using a critic augmented\
    \ with feasibility-aware correction. Across standard D4RL benchmarks, including\
    \ locomotion, navigation, manipulation, and dexterous control tasks, STP achieves\
    \ strong performance while simplifying the training pipeline for fast generative\
    \ planning."
  ko: ''
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- shortcut_trajectory_planning_f
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-13'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning
    (arXiv)
  url: https://arxiv.org/abs/2607.09336
  date: '2026'
  accessed_at: '2026-07-13'
---

arXiv:2607.09336v1 Announce Type: cross 
Abstract: Diffusion-based trajectory planners have shown strong performance in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction. Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves strong performance while simplifying the training pipeline for fast generative planning.
