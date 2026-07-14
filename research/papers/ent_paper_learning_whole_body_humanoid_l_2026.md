---
$id: ent_paper_learning_whole_body_humanoid_l_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking
  zh: 复杂地形里，参考动作要在线生成
  ko: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking
summary:
  en: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking is a knowledge node related to paper
    in the humanoid robot value chain.
  zh: Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need
    for real-time adaptation to various terrains using onboard perception. Directly applying reinforcement learning (RL) with
    reward shaping to humanoid locomotion often leads to lower-body-dominated behaviors, whereas imitation-based RL can learn
    more coordinated whole-body skills but is typically limited to replaying reference motions without a mechanism to adapt
    them online from perception for terrain-aware locomotion. To address this gap, we propose a whole-body humanoid locomotion
    framework that combines skills learned from reference motions with terrain-aware adaptation. We first train a diffusion
    model on retargeted human motions for real-time prediction of terrain-awar
  ko: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking is a knowledge node related to paper
    in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- task_interface
- visual_closed_loop
- vla
- whole_body_control
- world_model
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.17335v2.
sources:
- id: src_001
  type: paper
  title: Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking (arXiv)
  url: https://arxiv.org/abs/2604.17335
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 复杂地形里，参考动作要在线生成 project page
  url: https://wholebodylocomotion.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need for real-time adaptation to various terrains using onboard perception. Directly applying reinforcement learning (RL) with reward shaping to humanoid locomotion often leads to lower-body-dominated behaviors, whereas imitation-based RL can learn more coordinated whole-body skills but is typically limited to replaying reference motions without a mechanism to adapt them online from perception for terrain-aware locomotion. To address this gap, we propose a whole-body humanoid locomotion framework that combines skills learned from reference motions with terrain-aware adaptation. We first train a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions. Concurrently, we train a whole-body reference tracker with RL using this motion data. To improve robustness under imperfectly generated references, we further fine-tune the tracker with a frozen motion generator in a closed-loop setting. The resulting system supports directional goal-reaching control with terrain-aware whole-body adaptation, and can be deployed on a Unitree G1 humanoid robot with onboard perception and computation. The hardware experiments demonstrate successful traversal over boxes, hurdles, stairs, and mixed terrain combinations. Quantitative results further show the benefits of incorporating online motion generation and fine-tuning the motion tracker for improved generalization and robustness.

## 核心内容
Whole-body humanoid locomotion is challenging due to high-dimensional control, morphological instability, and the need for real-time adaptation to various terrains using onboard perception. Directly applying reinforcement learning (RL) with reward shaping to humanoid locomotion often leads to lower-body-dominated behaviors, whereas imitation-based RL can learn more coordinated whole-body skills but is typically limited to replaying reference motions without a mechanism to adapt them online from perception for terrain-aware locomotion. To address this gap, we propose a whole-body humanoid locomotion framework that combines skills learned from reference motions with terrain-aware adaptation. We first train a diffusion model on retargeted human motions for real-time prediction of terrain-aware reference motions. Concurrently, we train a whole-body reference tracker with RL using this motion data. To improve robustness under imperfectly generated references, we further fine-tune the tracker with a frozen motion generator in a closed-loop setting. The resulting system supports directional goal-reaching control with terrain-aware whole-body adaptation, and can be deployed on a Unitree G1 humanoid robot with onboard perception and computation. The hardware experiments demonstrate successful traversal over boxes, hurdles, stairs, and mixed terrain combinations. Quantitative results further show the benefits of incorporating online motion generation and fine-tuning the motion tracker for improved generalization and robustness.

## 参考
- http://arxiv.org/abs/2604.17335v2

