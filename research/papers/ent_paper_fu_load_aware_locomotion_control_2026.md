---
$id: ent_paper_fu_load_aware_locomotion_control_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Load-Aware Locomotion Control for Humanoid Robots in Industrial Transportation
    Tasks
  zh: 面向工业搬运任务的人形机器人负载感知 locomotion 控制
  ko: 산업 운반 작업을 위한 휴머노이드 로봇의 부하 인식 보행 제어
summary:
  en: This paper presents a reinforcement-learning-based load-aware locomotion framework
    for full-size humanoid robots performing industrial load-carrying and box-handling
    tasks, using a decoupled loco-manipulation architecture with kinematic references,
    height-conditioned joint offsets, and history-based state estimation, trained
    entirely in simulation and deployed zero-shot on the Tiangong 2.0 Pro robot.
  zh: 本文提出了一种基于强化学习的负载感知 locomotion 框架，用于执行工业搬运与箱体操作任务的全尺寸人形机器人；该框架采用解耦的 loco-manipulation
    架构，结合运动学参考、基于高度的关节偏移与基于历史的状态估计，完全在仿真中训练并直接迁移到天工 2.0 Pro 机器人。
  ko: 본 논문은 산업용 운반 및 박스 취급 작업을 수행하는 실제 크기의 휴머노이드 로봇을 위한 강화학습 기반 부하 인식 보행 제어 프레임워크를
    제안한다. 이 프레임워크는 운동학적 기준, 높이 조건부 관절 오프셋, 그리고 이력 기반 상태 추정을 갖춘 분리된 loco-manipulation
    아키텍처를 사용하며, 전적으로 시뮬레이션에서 훈련된 후 Tiangong 2.0 Pro 로봇에 미세 조정 없이 배포되었다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
- 03_manufacturing_processes
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- load_aware_locomotion
- loco_manipulation
- reinforcement_learning
- sim_to_real
- industrial_transportation
- state_estimation
- residual_policy
- tiangong_2_pro
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text verification
    and human review required before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Load-Aware Locomotion Control for Humanoid Robots in Industrial Transportation
    Tasks
  url: https://arxiv.org/abs/2603.14308
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Industrial deployment of humanoid robots often requires them to carry payloads while walking and to coordinate lower-body locomotion with upper-body manipulation. This coupling between locomotion and manipulation introduces dynamic disturbances and partial observability that make stable gait generation difficult. The proposed framework addresses these challenges by decoupling the learning of lower-body locomotion from upper-body manipulation while preserving awareness of manipulation-induced disturbances through observation design.

The core of the approach is a reinforcement learning policy that outputs residual joint actions added to nominal joint configurations derived kinematically. A height-conditioned joint-space offset structures the residual policy and supports accurate height tracking. A history-based state estimator concurrently infers base linear velocity and base height, and compresses residual load and manipulation disturbances into a compact latent vector. The entire pipeline is trained in simulation with domain randomization and transferred to hardware without fine-tuning.

Experiments reported in the paper include simulation benchmarks and real-world trials on a full-size humanoid robot. The results highlight faster training convergence, improved height tracking, and stable locomotion while carrying loads and executing upper-body motions.

## Key Contributions

- A load-aware locomotion control framework that decouples lower-body locomotion learning from upper-body manipulation while maintaining dynamic coupling through observation design.
- A kinematics-based locomotion reference combined with a height-conditioned joint-space offset for structured residual reinforcement learning.
- A history-based state estimation scheme that infers base linear velocity and base height and learns a compact latent representation of load- and manipulation-induced disturbances.
- End-to-end training in simulation with domain randomization and zero-shot deployment on a full-size humanoid robot without real-world fine-tuning.

## Relevance to Humanoid Robotics

The work is directly relevant to the humanoid-robot knowledge base because it targets stable, load-aware locomotion for full-size humanoid robots in industrial logistics scenarios. By demonstrating sim-to-real transfer on the Tiangong 2.0 Pro platform, the paper provides a concrete method for bridging learning-based control and factory-floor applications such as box carrying and material transport.
