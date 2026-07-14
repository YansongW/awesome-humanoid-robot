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
  en: This paper presents a practical recipe using FastSAC and FastTD3 with massively parallel simulation to train robust
    full-body humanoid locomotion policies on a single RTX 4090 GPU in 15 minutes, and demonstrates sim-to-real deployment
    on Unitree G1 and Booster T1 robots.
  zh: 本文提出了一种基于 FastSAC 和 FastTD3 的实用方案，结合大规模并行仿真，在单张 RTX 4090 GPU 上仅用 15 分钟即可训练出鲁棒的全尺寸人形机器人运动策略，并在 Unitree G1 与 Booster T1
    机器人上实现了 sim-to-real 部署。
  ko: 본 논문은 대규모 병렬 시뮬레이션과 FastSAC 및 FastTD3를 활용한 실용적인 방법론을 제안하여 단일 RTX 4090 GPU에서 15분 만에 강건한 전신 휴머노이드 보행 정책을 학습하고, Unitree
    G1과 Booster T1 로봇에서 sim-to-real 전개를 입증한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01996v1.
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
## 概述
Massively parallel simulation has reduced reinforcement learning (RL) training time for robots from days to minutes. However, achieving fast and reliable sim-to-real RL for humanoid control remains difficult due to the challenges introduced by factors such as high dimensionality and domain randomization. In this work, we introduce a simple and practical recipe based on off-policy RL algorithms, i.e., FastSAC and FastTD3, that enables rapid training of humanoid locomotion policies in just 15 minutes with a single RTX 4090 GPU. Our simple recipe stabilizes off-policy RL algorithms at massive scale with thousands of parallel environments through carefully tuned design choices and minimalist reward functions. We demonstrate rapid end-to-end learning of humanoid locomotion controllers on Unitree G1 and Booster T1 robots under strong domain randomization, e.g., randomized dynamics, rough terrain, and push perturbations, as well as fast training of whole-body human-motion tracking policies. We provide videos and open-source implementation at: https://younggyo.me/fastsac-humanoid.

## 核心内容
Massively parallel simulation has reduced reinforcement learning (RL) training time for robots from days to minutes. However, achieving fast and reliable sim-to-real RL for humanoid control remains difficult due to the challenges introduced by factors such as high dimensionality and domain randomization. In this work, we introduce a simple and practical recipe based on off-policy RL algorithms, i.e., FastSAC and FastTD3, that enables rapid training of humanoid locomotion policies in just 15 minutes with a single RTX 4090 GPU. Our simple recipe stabilizes off-policy RL algorithms at massive scale with thousands of parallel environments through carefully tuned design choices and minimalist reward functions. We demonstrate rapid end-to-end learning of humanoid locomotion controllers on Unitree G1 and Booster T1 robots under strong domain randomization, e.g., randomized dynamics, rough terrain, and push perturbations, as well as fast training of whole-body human-motion tracking policies. We provide videos and open-source implementation at: https://younggyo.me/fastsac-humanoid.

## 参考
- http://arxiv.org/abs/2512.01996v1

