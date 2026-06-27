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
  en: Proposes Adaptive Motion Optimization (AMO), a framework that combines sim-to-real
    reinforcement learning with trajectory optimization to enable real-time, hyper-dexterous
    whole-body control on a 29-DoF Unitree G1 humanoid robot, validated on tasks such
    as picking objects from the ground.
  zh: 提出自适应运动优化（AMO）框架，将sim-to-real强化学习与轨迹优化相结合，使29自由度Unitree G1人形机器人实现实时、超灵巧的全身控制，并在拾取地面物体等任务中得到验证。
  ko: sim-to-real 강화학습과 궤적 최적화를 결합하여 29-DoF Unitree G1 인간형 로봇에서 실시간 초민첩 전신 제어를 가능하게
    하는 AMO(Adaptive Motion Optimization) 프레임워크를 제안하고, 지면에서 물체를 집는 작업 등으로 검증함.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full paper before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body
    Control'
  url: https://arxiv.org/abs/2505.03738
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Humanoid robots can achieve a large operational workspace through hyper-dexterous whole-body movements, but realizing these capabilities on real hardware is difficult because of high degrees of freedom and nonlinear dynamics. This paper presents Adaptive Motion Optimization (AMO), a framework that integrates sim-to-real reinforcement learning with trajectory optimization to produce real-time, adaptive whole-body control. To reduce the distribution bias common in motion-imitation reinforcement learning, the authors construct a hybrid AMO dataset and train a network that can robustly adapt to potentially out-of-distribution commands on demand.

The proposed pipeline fuses motion-capture arm trajectories with sampled torso commands, then uses trajectory optimization to generate dynamically feasible whole-body references. A neural network trained with supervised learning, together with an RL policy, maps sparse torso and height commands to lower-body joint references in real time. The system is evaluated both in simulation and on a 29-DoF Unitree G1 humanoid robot equipped with Dex3-1 dexterous hands, an active head, a ZED Mini stereo camera, a Jetson Orin NX, and an RTX 4090 GPU.

The experiments demonstrate improved stability and an expanded workspace compared with strong baselines. The authors further show that AMO's consistent performance enables autonomous task execution through imitation learning, illustrating the system's potential for practical loco-manipulation tasks.

## Key Contributions

- Adaptive Motion Optimization (AMO) framework that expands humanoid workspace and supports real-time, sparse task-space control.
- Hybrid AMO dataset combining MoCap upper-body data with dynamics-aware trajectory optimization to mitigate kinematic bias.
- Network architecture that generalizes to out-of-distribution torso and height commands beyond the training distribution.
- Real-world validation on a 29-DoF Unitree G1 for teleoperation and autonomous loco-manipulation tasks.

## Relevance to Humanoid Robotics

AMO directly advances real-world humanoid deployment by enabling real-time, hyper-dexterous whole-body control on a high-DoF platform. By addressing the distribution bias that limits existing motion-imitation methods, it enlarges the reachable workspace and improves robustness for tasks such as ground-object retrieval. The integration of trajectory optimization with sim-to-real reinforcement learning offers a concrete methodology for transferring dynamic whole-body skills to physical humanoids, which is a key step toward autonomous loco-manipulation in unstructured environments.
