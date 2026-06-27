---
$id: ent_paper_li_reinforcement_learning_for_rob_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning for Robust Parameterized Locomotion Control of Bipedal
    Robots
  zh: 用于双足机器人鲁棒参数化运动控制的强化学习
  ko: 이족 보행 로봇의 강건한 매개변수화 보행 제어를 위한 강화학습
summary:
  en: Presents a model-free reinforcement learning framework that combines an HZD
    gait library with PPO and curriculum-based dynamics randomization to train robust
    sim-to-real locomotion policies for the Cassie bipedal robot, enabling tracking
    of target walking velocity, height, and yaw without residual control.
  zh: 提出一种无模型强化学习框架，将混合零动态（HZD）步态库与PPO及课程式动力学随机化结合，在仿真中训练可迁移到真实Cassie双足机器人的鲁棒运动策略，实现无需残差控制的目标行走速度、高度与偏航跟踪。
  ko: HZD 보행 라이브러리와 PPO 및 커리큘럼 기반 동역학 랜덤화를 결합한 모델-프리 강화학습 프레임워크를 제안하여, Cassie 실제 이족
    로봇으로 시뮬레이션-투-리얼 전이가 가능한 강건한 보행 정책을 학습하고 잔차 제어 없이 목표 보행 속도·높이·선회를 추적한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- bipedal_locomotion
- sim_to_real
- domain_randomization
- proximal_policy_optimization
- hybrid_zero_dynamics
- cassie
- locomotion_control
- robot_locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the paper metadata and abstract; full-text verification
    needed before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Reinforcement Learning for Robust Parameterized Locomotion Control of Bipedal
    Robots
  url: https://arxiv.org/abs/2103.14295
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Bipedal walking remains difficult for classical model-based controllers because they rely on accurate models and are easily destabilized by modeling errors or environmental variations. This paper proposes a model-free reinforcement learning framework that learns robust parameterized locomotion policies entirely in simulation and transfers them to the real Cassie robot. The approach combines a diverse Hybrid Zero Dynamics (HZD) gait library with Proximal Policy Optimization (PPO), using a curriculum-based dynamics randomization schedule to improve both learning efficiency and robustness. The resulting policies can track commanded forward/lateral walking speed, walking height, and turning yaw rate without resorting to residual control, and they are shown to outperform traditional controllers and prior learning-based methods on a physical platform.

## Key Contributions

- End-to-end versatile walking policy that tracks frontal/lateral walking speeds, walking height, and turning yaw rate without residual control.
- Integration of a diverse HZD-based gait library with deep RL to expand the feasible command set and safe set over prior model-based controllers.
- Curriculum-based dynamics randomization that gradually increases simulation uncertainty to improve learning speed and robustness.
- Sim-to-real transfer validated on a real Cassie robot, demonstrating robustness to modeling errors, motor malfunctions, perturbations, friction changes, and unknown loads.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid robotics because it develops a scalable, model-free method for producing robust, versatile bipedal locomotion on a person-sized robot. Its command tracking of velocity, height, and yaw provides the kind of agile, tunable gait behavior required for humanoid platforms operating in unstructured indoor and outdoor environments. The sim-to-real pipeline also reduces the need for extensive per-robot manual tuning, a major bottleneck for deploying humanoid systems.
