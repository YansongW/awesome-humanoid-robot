---
$id: ent_paper_seo_learning_sim_to_real_humanoid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Sim-to-Real Humanoid Locomotion in 15 Minutes
  zh: 在15分钟内学习从仿真到现实的人形机器人运动
  ko: 15분 만에 학습하는 시뮬레이션-현실 간 휴머노이드 보행
summary:
  en: This paper presents a practical recipe using FastSAC and FastTD3 with massively
    parallel simulation to train robust full-body humanoid locomotion policies on
    a single RTX 4090 GPU in 15 minutes, and demonstrates sim-to-real deployment on
    Unitree G1 and Booster T1 robots.
  zh: 本文提出了一种基于 FastSAC 和 FastTD3 的实用方案，结合大规模并行仿真，在单张 RTX 4090 GPU 上仅用 15 分钟即可训练出鲁棒的全尺寸人形机器人运动策略，并在
    Unitree G1 与 Booster T1 机器人上实现了 sim-to-real 部署。
  ko: 본 논문은 대규모 병렬 시뮬레이션과 FastSAC 및 FastTD3를 활용한 실용적인 방법론을 제안하여 단일 RTX 4090 GPU에서
    15분 만에 강건한 전신 휴머노이드 보행 정책을 학습하고, Unitree G1과 Booster T1 로봇에서 sim-to-real 전개를 입증한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 06_design_engineering
layers:
- intelligence
- midstream
- upstream
functional_roles:
- intelligence
- knowledge
tags:
- sim_to_real
- reinforcement_learning
- off_policy_rl
- fastsac
- fasttd3
- humanoid_locomotion
- whole_body_motion_tracking
- domain_randomization
- unitree_g1
- booster_t1
- rtx_4090
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the arXiv abstract and supplied metadata; full-text verification
    and human review are still required.
sources:
- id: src_001
  type: paper
  title: Learning Sim-to-Real Humanoid Locomotion in 15 Minutes
  url: https://arxiv.org/abs/2512.01996
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Training sim-to-real reinforcement-learning controllers for full-body humanoids has remained slow and brittle because of high-dimensional state/action spaces and the need for strong domain randomization. This paper introduces a streamlined recipe built on off-policy RL algorithms—FastSAC and FastTD3—running with thousands of parallel simulated environments. The authors report that careful implementation choices, including joint-limit-aware action bounds, observation and layer normalization, distributional critics, and minimalist reward functions, are sufficient to stabilize learning at massive scale.

Using a single NVIDIA RTX 4090 GPU, the authors train locomotion policies end-to-end in roughly 15 minutes. They transfer the resulting policies to physical Unitree G1 and Booster T1 humanoids and show robustness under randomized dynamics, rough terrain, and external pushes. The work also extends the same pipeline to whole-body human-motion tracking tasks on the G1 hardware, demonstrating that the approach can support both locomotion and tracking behaviors.

## Key Contributions

- Stabilizes FastSAC and FastTD3 for full-body humanoid control under strong domain randomization.
- Trains robust humanoid locomotion policies end-to-end in 15 minutes on a single RTX 4090 GPU.
- Demonstrates sim-to-real deployment on Unitree G1 and Booster T1 robots.
- Shows fast training of whole-body human-motion tracking policies on real G1 hardware.
- Provides an open-source implementation to support reproducibility.

## Relevance to Humanoid Robotics

The work directly reduces the sim-to-real iteration loop for full-body humanoid locomotion from hours or days to minutes, lowering a major barrier in developing controllable humanoid hardware. By demonstrating reliable deployment on two distinct commercial humanoid platforms and extending to whole-body motion tracking, it provides a practical training methodology that can accelerate algorithm-hardware co-development for humanoid robots.
