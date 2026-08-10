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
  zh: COLA 是一个基于本体感知的强化学习框架，由研究团队提出，用于实现人形机器人与人类协作搬运物体。其核心贡献在于将领导者和跟随者行为统一在一个策略中，通过闭环训练隐式预测物体运动模式和人类意图，无需外部传感器。实验表明，该方法在模拟中减少人类
    24.7% 的体力消耗，在真实场景中用户满意度提升 27.4%。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14293v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (762 chars, DeepSeek).'
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
COLA 针对人形机器人全身动力学复杂、难以实现柔顺协作的挑战，提出了一种仅依赖本体感知的强化学习方法。该方法在闭环模拟器中训练一个基于特权物体状态的教师策略，并通过知识蒸馏得到学生策略，用于真实世界部署。模型通过动态物体交互隐式学习人类意图和物体运动模式，实现负载平衡的协调轨迹规划。在多种地形和物体（如箱子、桌子、担架）上的实验验证了其有效性和泛化能力，且无需外部传感器。

## 核心内容
### 方法架构
- **框架设计**：COLA 采用强化学习框架，将领导者和跟随者行为统一在一个策略中。训练时使用闭环模拟器，动态模拟物体与机器人的交互。
- **教师-学生蒸馏**：教师策略在模拟器中利用特权物体状态（如物体位置、速度、人类施加的力）进行训练；学生策略仅依赖本体感知（关节角度、角速度、IMU 数据）进行蒸馏，实现真实世界部署。
- **隐式建模**：模型通过预测物体运动模式和人类意图，实现柔顺协作，无需显式交互模型或外部传感器。

### 实验设置
- **模拟实验**：在多种地形（直线、转弯、斜坡）和物体类型（箱子、桌子、担架）上测试。与基线方法相比，COLA 将人类体力消耗降低 24.7%，同时保持物体稳定性。
- **真实世界实验**：使用 23 名参与者进行用户研究，评估协作搬运任务。结果显示，COLA 在用户满意度上平均提升 27.4%，优于基线模型。
- **鲁棒性测试**：模型在不同物体重量、尺寸和运动模式下均表现稳定，无需重新训练。

### 关键结论
- COLA 实现了人形机器人与人类的柔顺协作搬运，无需外部传感器或复杂交互模型。
- 模拟和真实实验均验证了模型的有效性、泛化能力和鲁棒性。
- 该方法为实际部署提供了实用解决方案，适用于医疗、家庭和制造等场景。

## Overview
Human-humanoid collaboration shows significant promise for applications in healthcare, domestic assistance, and manufacturing. While compliant robot-human collaboration has been extensively developed for robotic arms, enabling compliant human-humanoid collaboration remains largely unexplored due to humanoids' complex whole-body dynamics. In this paper, we propose a proprioception-only reinforcement learning approach, COLA, that combines leader and follower behaviors within a single policy. The model is trained in a closed-loop environment with dynamic object interactions to predict object motion patterns and human intentions implicitly, enabling compliant collaboration to maintain load balance through coordinated trajectory planning. We evaluate our approach through comprehensive simulator and real-world experiments on collaborative carrying tasks, demonstrating the effectiveness, generalization, and robustness of our model across various terrains and objects. Simulation experiments demonstrate that our model reduces human effort by 24.7%. compared to baseline approaches while maintaining object stability. Real-world experiments validate robust collaborative carrying across different object types (boxes, desks, stretchers, etc.) and movement patterns (straight-line, turning, slope climbing). Human user studies with 23 participants confirm an average improvement of 27.4% compared to baseline models. Our method enables compliant human-humanoid collaborative carrying without requiring external sensors or complex interaction models, offering a practical solution for real-world deployment.

## Overview
Human-humanoid collaboration shows significant promise for applications in healthcare, domestic assistance, and manufacturing. While compliant robot-human collaboration has been extensively developed for robotic arms, enabling compliant human-humanoid collaboration remains largely unexplored due to humanoids' complex whole-body dynamics. In this paper, we propose a proprioception-only reinforcement learning approach, COLA, that combines leader and follower behaviors within a single policy. The model is trained in a closed-loop environment with dynamic object interactions to predict object motion patterns and human intentions implicitly, enabling compliant collaboration to maintain load balance through coordinated trajectory planning. We evaluate our approach through comprehensive simulator and real-world experiments on collaborative carrying tasks, demonstrating the effectiveness, generalization, and robustness of our model across various terrains and objects. Simulation experiments demonstrate that our model reduces human effort by 24.7% compared to baseline approaches while maintaining object stability. Real-world experiments validate robust collaborative carrying across different object types (boxes, desks, stretchers, etc.) and movement patterns (straight-line, turning, slope climbing). Human user studies with 23 participants confirm an average improvement of 27.4% compared to baseline models. Our method enables compliant human-humanoid collaborative carrying without requiring external sensors or complex interaction models, offering a practical solution for real-world deployment.

## Content
Human-humanoid collaboration shows significant promise for applications in healthcare, domestic assistance, and manufacturing. While compliant robot-human collaboration has been extensively developed for robotic arms, enabling compliant human-humanoid collaboration remains largely unexplored due to humanoids' complex whole-body dynamics. In this paper, we propose a proprioception-only reinforcement learning approach, COLA, that combines leader and follower behaviors within a single policy. The model is trained in a closed-loop environment with dynamic object interactions to predict object motion patterns and human intentions implicitly, enabling compliant collaboration to maintain load balance through coordinated trajectory planning. We evaluate our approach through comprehensive simulator and real-world experiments on collaborative carrying tasks, demonstrating the effectiveness, generalization, and robustness of our model across various terrains and objects. Simulation experiments demonstrate that our model reduces human effort by 24.7% compared to baseline approaches while maintaining object stability. Real-world experiments validate robust collaborative carrying across different object types (boxes, desks, stretchers, etc.) and movement patterns (straight-line, turning, slope climbing). Human user studies with 23 participants confirm an average improvement of 27.4% compared to baseline models. Our method enables compliant human-humanoid collaborative carrying without requiring external sensors or complex interaction models, offering a practical solution for real-world deployment.

## 参考
- http://arxiv.org/abs/2510.14293v1

## 개요
COLA는 인간형 로봇의 전신 역학이 복잡하고 유연한 협력이 어렵다는 과제에 대응하여, 고유 감각(자기수용감각)만을 활용하는 강화 학습 방법을 제안한다. 이 방법은 폐루프 시뮬레이터에서 특권 객체 상태를 기반으로 한 교사 정책을 훈련하고, 지식 증류를 통해 학생 정책을 얻어 실제 세계에 배포한다. 모델은 동적 객체 상호작용을 통해 인간의 의도와 객체 운동 패턴을 암묵적으로 학습하며, 부하 균형을 고려한 조화로운 궤적 계획을 구현한다. 다양한 지형과 객체(상자, 테이블, 들것)에서의 실험을 통해 유효성과 일반화 능력을 검증했으며, 외부 센서가 필요 없다.

## 핵심 내용
### 방법 아키텍처
- **프레임워크 설계**: COLA는 강화 학습 프레임워크를 채택하여 리더와 팔로워 행동을 하나의 정책으로 통합한다. 훈련 시 폐루프 시뮬레이터를 사용하여 객체와 로봇 간의 상호작용을 동적으로 시뮬레이션한다.
- **교사-학생 증류**: 교사 정책은 시뮬레이터에서 특권 객체 상태(예: 객체 위치, 속도, 인간이 가하는 힘)를 활용하여 훈련된다. 학생 정책은 고유 감각(관절 각도, 각속도, IMU 데이터)만을 기반으로 증류되어 실제 세계 배포를 가능하게 한다.
- **암묵적 모델링**: 모델은 객체 운동 패턴과 인간 의도를 예측하여 유연한 협력을 구현하며, 명시적 상호작용 모델이나 외부 센서가 필요 없다.

### 실험 설정
- **시뮬레이션 실험**: 다양한 지형(직선, 곡선, 경사로)과 객체 유형(상자, 테이블, 들것)에서 테스트했다. 기준 방법과 비교하여 COLA는 인간의 체력 소모를 24.7% 줄이면서 객체 안정성을 유지했다.
- **실제 세계 실험**: 23명의 참가자를 대상으로 사용자 연구를 수행하여 협력 운반 작업을 평가했다. 결과에 따르면 COLA는 사용자 만족도에서 평균 27.4% 향상되어 기준 모델보다 우수했다.
- **강건성 테스트**: 모델은 다양한 객체 무게, 크기, 운동 패턴에서도 재훈련 없이 안정적인 성능을 보였다.

### 핵심 결론
- COLA는 외부 센서나 복잡한 상호작용 모델 없이 인간형 로봇과 인간의 유연한 협력 운반을 구현했다.
- 시뮬레이션과 실제 실험 모두에서 모델의 유효성, 일반화 능력, 강건성을 검증했다.
- 이 방법은 의료, 가정, 제조 등 다양한 시나리오에 적용 가능한 실용적인 배포 솔루션을 제공한다.
