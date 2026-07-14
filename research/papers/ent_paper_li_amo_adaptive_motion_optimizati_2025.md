---
$id: ent_paper_li_amo_adaptive_motion_optimizati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
  zh: AMO：面向超灵巧人形机器人全身控制的自适应运动优化
  ko: 'AMO: 초민첩한 인간형 로봇 전신 제어를 위한 적응형 동작 최적화'
summary:
  en: Proposes Adaptive Motion Optimization (AMO), a framework that combines sim-to-real reinforcement learning with trajectory
    optimization to enable real-time, hyper-dexterous whole-body control on a 29-DoF Unitree G1 humanoid robot, validated
    on tasks such as picking objects from the ground.
  zh: 提出自适应运动优化（AMO）框架，将sim-to-real强化学习与轨迹优化相结合，使29自由度Unitree G1人形机器人实现实时、超灵巧的全身控制，并在拾取地面物体等任务中得到验证。
  ko: sim-to-real 강화학습과 궤적 최적화를 결합하여 29-DoF Unitree G1 인간형 로봇에서 실시간 초민첩 전신 제어를 가능하게 하는 AMO(Adaptive Motion Optimization) 프레임워크를
    제안하고, 지면에서 물체를 집는 작업 등으로 검증함.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- whole_body_control
- sim_to_real
- reinforcement_learning
- trajectory_optimization
- motion_imitation
- loco_manipulation
- unitree_g1
- humanoid_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03738v1.
sources:
- id: src_001
  type: paper
  title: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
  url: https://arxiv.org/abs/2505.03738
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Humanoid robots derive much of their dexterity from hyper-dexterous whole-body movements, enabling tasks that require a large operational workspace: such as picking objects off the ground. However, achieving these capabilities on real humanoids remains challenging due to their high degrees of freedom (DoF) and nonlinear dynamics. We propose Adaptive Motion Optimization (AMO), a framework that integrates sim-to-real reinforcement learning (RL) with trajectory optimization for real-time, adaptive whole-body control. To mitigate distribution bias in motion imitation RL, we construct a hybrid AMO dataset and train a network capable of robust, on-demand adaptation to potentially O.O.D. commands. We validate AMO in simulation and on a 29-DoF Unitree G1 humanoid robot, demonstrating superior stability and an expanded workspace compared to strong baselines. Finally, we show that AMO's consistent performance supports autonomous task execution via imitation learning, underscoring the system's versatility and robustness.

## 核心内容
Humanoid robots derive much of their dexterity from hyper-dexterous whole-body movements, enabling tasks that require a large operational workspace: such as picking objects off the ground. However, achieving these capabilities on real humanoids remains challenging due to their high degrees of freedom (DoF) and nonlinear dynamics. We propose Adaptive Motion Optimization (AMO), a framework that integrates sim-to-real reinforcement learning (RL) with trajectory optimization for real-time, adaptive whole-body control. To mitigate distribution bias in motion imitation RL, we construct a hybrid AMO dataset and train a network capable of robust, on-demand adaptation to potentially O.O.D. commands. We validate AMO in simulation and on a 29-DoF Unitree G1 humanoid robot, demonstrating superior stability and an expanded workspace compared to strong baselines. Finally, we show that AMO's consistent performance supports autonomous task execution via imitation learning, underscoring the system's versatility and robustness.

## 参考
- http://arxiv.org/abs/2505.03738v1

