---
$id: ent_paper_hou_robust_fall_recovery_for_armle_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust Fall Recovery for Armless Bipedal-Wheeled Robots via Force-Guided Learning
  zh: 基于力引导学习的无臂双轮足机器人鲁棒跌倒恢复
  ko: 힘-유도 학습을 통한 무팔 이족-바퀴 로봇의 강건한 낙상 복귀
summary:
  en: This paper proposes FTSR, a force-guided teacher-student reinforcement-learning
    framework that formulates height-correlated external auxiliary forces as optimizable
    constraints and uses height-progressive stage-wise rewards to train armless bipedal-wheeled
    robots to recover from falls, with sim-to-real deployment on the JiaRan robot
    and generalization to a 23-DOF Unitree humanoid.
  zh: 本文提出FTSR框架，将高度相关的外部辅助力构建为可优化约束，并采用高度递进的分阶段奖励训练无臂双轮足机器人实现跌倒恢复，在JiaRan机器人上完成仿真到现实部署，并泛化至23自由度Unitree人形机器人。
  ko: 본 논문은 높이에 연동된 외부 보조력을 최적화 가능한 제약으로 공식화하고 높이 기반 단계적 보상을 사용하여 무팔 이족-바퀴 로봇의 낙상
    복귀를 학습하는 FTSR 프레임워크를 제안하며, JiaRan 로봇에 대한 시뮬레이션-현실 전개 및 23-DOF Unitree 휴머노이드로의
    일반화를 보여준다.
domains:
- 07_ai_models_algorithms
- 02_components
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- fall_recovery
- reinforcement_learning
- force_guided_learning
- teacher_student_distillation
- constrained_rl
- bipedal_wheeled_robot
- sim_to_real
- jiaran_robot
- unitree_humanoid
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text review is required
    before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Robust Fall Recovery for Armless Bipedal-Wheeled Robots via Force-Guided
    Learning
  url: https://arxiv.org/abs/2606.14270
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Falls are inevitable for legged robots operating in unstructured environments, and recovery without external assistance is essential for autonomy. For robots that lack arms or additional legs, such as armless bipedal-wheeled platforms, conventional reinforcement-learning (RL) fall-recovery policies often collapse into dead points because no extra end effectors can generate support forces. This paper presents FTSR (Force-guided Teacher-student framework with Stage-wise Rewards), which addresses the problem by adding height-correlated external auxiliary forces during simulation and treating them as optimizable constraints inside constrained policy optimization. The dependence on these forces is progressively reduced so that the policy learns internal recovery strategies using only leg actuation.

FTSR combines three design elements: a force-guided constrained-RL objective, height-progressive stage-wise rewards that automatically transition the task from upper-body erection through standing up to walking, and a teacher-student architecture that distills privileged knowledge about force effects and recovery dynamics into a proprioceptive-only student policy. After training in simulation, the policy is deployed on the physical JiaRan robot. The authors report robust and reliable recovery from multiple randomized initial postures and on diverse terrains, while preserving full post-recovery locomotion capability. The same framework is also applied to a 23-DOF Unitree humanoid, demonstrating cross-platform generalization.

The experiments are conducted primarily on the authors' self-developed JiaRan armless bipedal-wheeled robot. Results are presented for both simulated and real-world scenarios, including challenging conditions that test environmental adaptability and motion robustness. The work therefore spans algorithm design, sim-to-real transfer, and validation on two distinct legged platforms.

## Key Contributions

- Force-guided learning that constructs height-correlated external auxiliary forces as optimizable constraints to avoid dead-point convergence in armless bipedal-wheeled robots.
- Height-progressive stage-wise rewards that auto-transition from upper-body erection through standing-up to walking based on batch height statistics.
- Teacher-student architecture that distills privileged knowledge of force effects and recovery dynamics for proprioceptive-only deployment.
- First real-world fall recovery of an armless bipedal-wheeled robot from multiple randomized postures and diverse terrains, with generalization shown on a 23-DOF Unitree humanoid.

## Relevance to Humanoid Robotics

Although the primary platform is an armless bipedal-wheeled robot, the paper explicitly transfers the learned policy to a 23-DOF Unitree humanoid and shows that it can stand up from arbitrary poses. This direct generalization makes the contribution relevant to humanoid deployment, where reliable fall recovery is a prerequisite for long-term autonomous operation and mass production. The force-guided constrained-RL formulation and stage-wise reward design are not tied to wheels and can in principle be applied to pure bipedal humanoids that also lack arm support.

From an industry-chain perspective, the work sits in AI models and algorithms, but it touches components (actuator-limited leg designs), mass production (robust recovery reduces field failures), and applications/markets (deployment readiness). By demonstrating sim-to-real transfer and cross-platform generalization, the paper advances the state of practical humanoid locomotion control beyond simulation-only methods.
