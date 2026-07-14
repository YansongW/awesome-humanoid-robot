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

