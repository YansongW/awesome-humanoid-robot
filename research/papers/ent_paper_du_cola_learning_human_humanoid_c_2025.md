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
  en: COLA presents a proprioception-only reinforcement-learning framework that unifies leader and follower behaviors in one
    policy for whole-body human-humanoid collaborative carrying. It trains a residual teacher policy on privileged object
    states in a closed-loop simulator and distills it into a student policy for real-world deployment.
  zh: COLA 提出了一种仅依赖本体感知的强化学习框架，将领导者与跟随者行为统一于单一策略中，实现全身人机协作搬运。该框架在闭环仿真器中基于特权物体状态训练残差教师策略，并通过行为克隆蒸馏为可实际部署的学生策略。
  ko: COLA는 단일 정책 내에서 리더와 팔로워 행동을 통합하여 전신 인간-휴머노이드 협업 운반을 수행하는 본체감각 전용 강화학습 프레임워크를 제안한다. 폐쇄루프 시뮬레이터에서 특권적 물체 상태를 기반으로 잔차 교사
    정책을 학습하고, 행동 복제를 통해 실제 배포용 학생 정책으로 증류한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14293v1.
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
    en: The paper evaluates COLA on the Unitree G1 humanoid robot in real-world collaborative carrying experiments.
    zh: 该论文在现实世界协作搬运实验中于 Unitree G1 人形机器人上评估了 COLA。
    ko: 해당 논문은 실제 협업 운반 실험에서 Unitree G1 휴머노이드 로봇에 COLA를 평가한다.
---
## 概述
Human-humanoid collaboration shows significant promise for applications in healthcare, domestic assistance, and manufacturing. While compliant robot-human collaboration has been extensively developed for robotic arms, enabling compliant human-humanoid collaboration remains largely unexplored due to humanoids' complex whole-body dynamics. In this paper, we propose a proprioception-only reinforcement learning approach, COLA, that combines leader and follower behaviors within a single policy. The model is trained in a closed-loop environment with dynamic object interactions to predict object motion patterns and human intentions implicitly, enabling compliant collaboration to maintain load balance through coordinated trajectory planning. We evaluate our approach through comprehensive simulator and real-world experiments on collaborative carrying tasks, demonstrating the effectiveness, generalization, and robustness of our model across various terrains and objects. Simulation experiments demonstrate that our model reduces human effort by 24.7%. compared to baseline approaches while maintaining object stability. Real-world experiments validate robust collaborative carrying across different object types (boxes, desks, stretchers, etc.) and movement patterns (straight-line, turning, slope climbing). Human user studies with 23 participants confirm an average improvement of 27.4% compared to baseline models. Our method enables compliant human-humanoid collaborative carrying without requiring external sensors or complex interaction models, offering a practical solution for real-world deployment.

## 核心内容
Human-humanoid collaboration shows significant promise for applications in healthcare, domestic assistance, and manufacturing. While compliant robot-human collaboration has been extensively developed for robotic arms, enabling compliant human-humanoid collaboration remains largely unexplored due to humanoids' complex whole-body dynamics. In this paper, we propose a proprioception-only reinforcement learning approach, COLA, that combines leader and follower behaviors within a single policy. The model is trained in a closed-loop environment with dynamic object interactions to predict object motion patterns and human intentions implicitly, enabling compliant collaboration to maintain load balance through coordinated trajectory planning. We evaluate our approach through comprehensive simulator and real-world experiments on collaborative carrying tasks, demonstrating the effectiveness, generalization, and robustness of our model across various terrains and objects. Simulation experiments demonstrate that our model reduces human effort by 24.7%. compared to baseline approaches while maintaining object stability. Real-world experiments validate robust collaborative carrying across different object types (boxes, desks, stretchers, etc.) and movement patterns (straight-line, turning, slope climbing). Human user studies with 23 participants confirm an average improvement of 27.4% compared to baseline models. Our method enables compliant human-humanoid collaborative carrying without requiring external sensors or complex interaction models, offering a practical solution for real-world deployment.

## 参考
- http://arxiv.org/abs/2510.14293v1

## Overview
Human-humanoid collaboration shows significant promise for applications in healthcare, domestic assistance, and manufacturing. While compliant robot-human collaboration has been extensively developed for robotic arms, enabling compliant human-humanoid collaboration remains largely unexplored due to humanoids' complex whole-body dynamics. In this paper, we propose a proprioception-only reinforcement learning approach, COLA, that combines leader and follower behaviors within a single policy. The model is trained in a closed-loop environment with dynamic object interactions to predict object motion patterns and human intentions implicitly, enabling compliant collaboration to maintain load balance through coordinated trajectory planning. We evaluate our approach through comprehensive simulator and real-world experiments on collaborative carrying tasks, demonstrating the effectiveness, generalization, and robustness of our model across various terrains and objects. Simulation experiments demonstrate that our model reduces human effort by 24.7% compared to baseline approaches while maintaining object stability. Real-world experiments validate robust collaborative carrying across different object types (boxes, desks, stretchers, etc.) and movement patterns (straight-line, turning, slope climbing). Human user studies with 23 participants confirm an average improvement of 27.4% compared to baseline models. Our method enables compliant human-humanoid collaborative carrying without requiring external sensors or complex interaction models, offering a practical solution for real-world deployment.

## Content
Human-humanoid collaboration shows significant promise for applications in healthcare, domestic assistance, and manufacturing. While compliant robot-human collaboration has been extensively developed for robotic arms, enabling compliant human-humanoid collaboration remains largely unexplored due to humanoids' complex whole-body dynamics. In this paper, we propose a proprioception-only reinforcement learning approach, COLA, that combines leader and follower behaviors within a single policy. The model is trained in a closed-loop environment with dynamic object interactions to predict object motion patterns and human intentions implicitly, enabling compliant collaboration to maintain load balance through coordinated trajectory planning. We evaluate our approach through comprehensive simulator and real-world experiments on collaborative carrying tasks, demonstrating the effectiveness, generalization, and robustness of our model across various terrains and objects. Simulation experiments demonstrate that our model reduces human effort by 24.7% compared to baseline approaches while maintaining object stability. Real-world experiments validate robust collaborative carrying across different object types (boxes, desks, stretchers, etc.) and movement patterns (straight-line, turning, slope climbing). Human user studies with 23 participants confirm an average improvement of 27.4% compared to baseline models. Our method enables compliant human-humanoid collaborative carrying without requiring external sensors or complex interaction models, offering a practical solution for real-world deployment.

## 개요
인간-휴머노이드 협업은 의료, 가사 지원, 제조 분야에서 큰 잠재력을 보여주고 있습니다. 로봇 팔의 경우 순응적 로봇-인간 협업이 광범위하게 개발되었지만, 휴머노이드의 복잡한 전신 역학으로 인해 순응적 인간-휴머노이드 협업은 아직 거의 탐구되지 않았습니다. 본 논문에서는 단일 정책 내에서 리더와 팔로워 행동을 결합한 고유 감각 기반 강화 학습 접근법인 COLA를 제안합니다. 이 모델은 동적 객체 상호작용이 있는 폐루프 환경에서 훈련되어 객체 운동 패턴과 인간 의도를 암시적으로 예측하며, 조정된 궤적 계획을 통해 부하 균형을 유지하는 순응적 협업을 가능하게 합니다. 우리는 협력 운반 작업에 대한 포괄적인 시뮬레이터 및 실제 실험을 통해 접근법을 평가하며, 다양한 지형과 객체에서 모델의 효과성, 일반화 및 견고성을 입증합니다. 시뮬레이션 실험은 우리 모델이 객체 안정성을 유지하면서 기준 접근법 대비 인간의 노력을 24.7% 감소시킴을 보여줍니다. 실제 실험은 다양한 객체 유형(상자, 책상, 들것 등)과 이동 패턴(직선, 회전, 경사 오르기)에서 견고한 협력 운반을 검증합니다. 23명의 참가자를 대상으로 한 인간 사용자 연구는 기준 모델 대비 평균 27.4%의 개선을 확인했습니다. 우리 방법은 외부 센서나 복잡한 상호작용 모델 없이 순응적 인간-휴머노이드 협력 운반을 가능하게 하여 실제 배포를 위한 실용적인 솔루션을 제공합니다.

## 핵심 내용
인간-휴머노이드 협업은 의료, 가사 지원, 제조 분야에서 큰 잠재력을 보여주고 있습니다. 로봇 팔의 경우 순응적 로봇-인간 협업이 광범위하게 개발되었지만, 휴머노이드의 복잡한 전신 역학으로 인해 순응적 인간-휴머노이드 협업은 아직 거의 탐구되지 않았습니다. 본 논문에서는 단일 정책 내에서 리더와 팔로워 행동을 결합한 고유 감각 기반 강화 학습 접근법인 COLA를 제안합니다. 이 모델은 동적 객체 상호작용이 있는 폐루프 환경에서 훈련되어 객체 운동 패턴과 인간 의도를 암시적으로 예측하며, 조정된 궤적 계획을 통해 부하 균형을 유지하는 순응적 협업을 가능하게 합니다. 우리는 협력 운반 작업에 대한 포괄적인 시뮬레이터 및 실제 실험을 통해 접근법을 평가하며, 다양한 지형과 객체에서 모델의 효과성, 일반화 및 견고성을 입증합니다. 시뮬레이션 실험은 우리 모델이 객체 안정성을 유지하면서 기준 접근법 대비 인간의 노력을 24.7% 감소시킴을 보여줍니다. 실제 실험은 다양한 객체 유형(상자, 책상, 들것 등)과 이동 패턴(직선, 회전, 경사 오르기)에서 견고한 협력 운반을 검증합니다. 23명의 참가자를 대상으로 한 인간 사용자 연구는 기준 모델 대비 평균 27.4%의 개선을 확인했습니다. 우리 방법은 외부 센서나 복잡한 상호작용 모델 없이 순응적 인간-휴머노이드 협력 운반을 가능하게 하여 실제 배포를 위한 실용적인 솔루션을 제공합니다.
