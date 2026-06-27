---
$id: ent_paper_du_cola_learning_human_humanoid_c_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'COLA: Learning Human-Humanoid Coordination for Collaborative Object Carrying'
  zh: COLA：学习人机协调以协作搬运物体
  ko: 'COLA: 협업적 물체 운반을 위한 인간-휴머노이드 협응 학습'
summary:
  en: COLA presents a proprioception-only reinforcement-learning framework that unifies
    leader and follower behaviors in one policy for whole-body human-humanoid collaborative
    carrying. It trains a residual teacher policy on privileged object states in a
    closed-loop simulator and distills it into a student policy for real-world deployment.
  zh: COLA 提出了一种仅依赖本体感知的强化学习框架，将领导者与跟随者行为统一于单一策略中，实现全身人机协作搬运。该框架在闭环仿真器中基于特权物体状态训练残差教师策略，并通过行为克隆蒸馏为可实际部署的学生策略。
  ko: COLA는 단일 정책 내에서 리더와 팔로워 행동을 통합하여 전신 인간-휴머노이드 협업 운반을 수행하는 본체감각 전용 강화학습 프레임워크를
    제안한다. 폐쇄루프 시뮬레이터에서 특권적 물체 상태를 기반으로 잔차 교사 정책을 학습하고, 행동 복제를 통해 실제 배포용 학생 정책으로 증류한다.
domains:
- 11_applications_markets
- 07_ai_models_algorithms
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- whole_body_control
- human_robot_collaboration
- human_humanoid_collaboration
- proprioception
- teacher_student_distillation
- collaborative_carrying
- compliant_control
- object_transport
- residual_policy
- unitree_g1
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from abstract and provided metadata; requires human review before
    promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'COLA: Learning Human-Humanoid Coordination for Collaborative Object Carrying'
  url: https://arxiv.org/abs/2510.14293
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: uses
  description:
    en: The paper evaluates COLA on the Unitree G1 humanoid robot in real-world collaborative
      carrying experiments.
    zh: 该论文在现实世界协作搬运实验中于 Unitree G1 人形机器人上评估了 COLA。
    ko: 해당 논문은 실제 협업 운반 실험에서 Unitree G1 휴머노이드 로봇에 COLA를 평가한다.
---

## Overview

Human-humanoid collaboration holds substantial promise for healthcare, domestic assistance, and manufacturing, yet compliant whole-body coordination for collaborative object carrying remains underexplored because of complex humanoid dynamics, diverse human behaviors, and the need for adaptive leader/follower allocation. COLA addresses this gap through a proprioception-only reinforcement-learning framework that combines leader and follower behaviors within a single residual policy. The system is trained in a closed-loop simulated environment that explicitly models humanoid-object-human interactions, enabling the policy to implicitly predict object motion patterns and human intentions from physical interaction.

The training pipeline consists of three stages. First, a whole-body controller provides stable locomotion primitives. Second, a residual teacher policy is trained with privileged object-state information to produce compliant collaborative behaviors. Third, the teacher is distilled into a proprioception-only student policy via behavioral cloning so the method can be deployed without external sensors or explicit force sensing. This design keeps the real-world sensing minimal while preserving coordination capabilities across varied terrains, object geometries, and movement patterns.

Empirical evaluation spans simulation and real-world experiments. In simulation, COLA reduces human effort by 24.7% compared with baselines while maintaining object stability. Real-world trials cover boxes, desks, stretchers, and other objects with straight-line, turning, and slope-climbing motions. A user study with 23 participants reports an average improvement of 27.4% over baseline models, supporting the method's effectiveness, generalization, and robustness.

## Key Contributions

- A unified residual policy that uses only proprioception for whole-body collaborative carrying across diverse movement patterns.
- A three-step training framework with a closed-loop environment explicitly modeling humanoid-object-human interactions.
- Implicit learning of object dynamics and human intention through physical interaction, without requiring external sensors or explicit force sensing.
- Empirical validation in simulation and the real world, including a user study with 23 participants showing reduced human effort and improved compliance.

## Relevance to Humanoid Robotics

The work directly advances practical deployment of humanoid robots by targeting collaborative object transport in logistics, healthcare, and manufacturing. By enabling compliant, sensor-minimal, whole-body coordination, COLA reduces the deployment burden for humanoid systems that must physically collaborate with humans in unstructured environments. This is particularly relevant for applications such as patient handling, warehouse transport, and assembly assistance, where load sharing and balance maintenance are critical.

The paper also contributes to the algorithm layer of the humanoid value chain: its teacher-student residual reinforcement-learning pipeline demonstrates how privileged-information training in simulation can be distilled into policies that rely only on onboard proprioception. This aligns with broader industry needs for low-cost, robust control methods that can generalize across robot embodiments and real-world conditions without expensive multi-modal sensing suites.
