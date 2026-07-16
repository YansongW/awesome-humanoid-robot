---
$id: ent_paper_fu_load_aware_locomotion_control_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Load-Aware Locomotion Control for Humanoid Robots in Industrial Transportation Tasks
  zh: 面向工业搬运任务的人形机器人负载感知 locomotion 控制
  ko: 산업 운반 작업을 위한 휴머노이드 로봇의 부하 인식 보행 제어
summary:
  en: This paper presents a reinforcement-learning-based load-aware locomotion framework for full-size humanoid robots performing
    industrial load-carrying and box-handling tasks, using a decoupled loco-manipulation architecture with kinematic references,
    height-conditioned joint offsets, and history-based state estimation, trained entirely in simulation and deployed zero-shot
    on the Tiangong 2.0 Pro robot.
  zh: 本文提出了一种基于强化学习的负载感知 locomotion 框架，用于执行工业搬运与箱体操作任务的全尺寸人形机器人；该框架采用解耦的 loco-manipulation 架构，结合运动学参考、基于高度的关节偏移与基于历史的状态估计，完全在仿真中训练并直接迁移到天工
    2.0 Pro 机器人。
  ko: 본 논문은 산업용 운반 및 박스 취급 작업을 수행하는 실제 크기의 휴머노이드 로봇을 위한 강화학습 기반 부하 인식 보행 제어 프레임워크를 제안한다. 이 프레임워크는 운동학적 기준, 높이 조건부 관절 오프셋,
    그리고 이력 기반 상태 추정을 갖춘 분리된 loco-manipulation 아키텍처를 사용하며, 전적으로 시뮬레이션에서 훈련된 후 Tiangong 2.0 Pro 로봇에 미세 조정 없이 배포되었다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.14308v1.
sources:
- id: src_001
  type: paper
  title: Load-Aware Locomotion Control for Humanoid Robots in Industrial Transportation Tasks
  url: https://arxiv.org/abs/2603.14308
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Humanoid robots deployed in industrial environments are required to perform load-carrying transportation tasks that tightly couple locomotion and manipulation. However, achieving stable and robust locomotion under varying payloads and upper-body motions is challenging due to dynamic coupling and partial observability. This paper presents a load-aware locomotion framework for industrial humanoids based on a decoupled yet coordinated loco-manipulation architecture. Lower-body locomotion is controlled via a reinforcement learning policy producing residual joint actions on kinematically derived nominal configurations. A kinematics-based locomotion reference with a height-conditioned joint-space offset guides learning, while a history-based state estimator infers base linear velocity and height and encodes residual load- and manipulation-induced disturbances in a compact latent representation. The framework is trained entirely in simulation and deployed on a full-size humanoid robot without fine-tuning. Simulation and real-world experiments demonstrate faster training, accurate height tracking, and stable loco-manipulation. Project page: https://lequn-f.github.io/LALO/

## 核心内容
Humanoid robots deployed in industrial environments are required to perform load-carrying transportation tasks that tightly couple locomotion and manipulation. However, achieving stable and robust locomotion under varying payloads and upper-body motions is challenging due to dynamic coupling and partial observability. This paper presents a load-aware locomotion framework for industrial humanoids based on a decoupled yet coordinated loco-manipulation architecture. Lower-body locomotion is controlled via a reinforcement learning policy producing residual joint actions on kinematically derived nominal configurations. A kinematics-based locomotion reference with a height-conditioned joint-space offset guides learning, while a history-based state estimator infers base linear velocity and height and encodes residual load- and manipulation-induced disturbances in a compact latent representation. The framework is trained entirely in simulation and deployed on a full-size humanoid robot without fine-tuning. Simulation and real-world experiments demonstrate faster training, accurate height tracking, and stable loco-manipulation. Project page: https://lequn-f.github.io/LALO/

## 参考
- http://arxiv.org/abs/2603.14308v1

## Overview
Humanoid robots deployed in industrial environments are required to perform load-carrying transportation tasks that tightly couple locomotion and manipulation. However, achieving stable and robust locomotion under varying payloads and upper-body motions is challenging due to dynamic coupling and partial observability. This paper presents a load-aware locomotion framework for industrial humanoids based on a decoupled yet coordinated loco-manipulation architecture. Lower-body locomotion is controlled via a reinforcement learning policy producing residual joint actions on kinematically derived nominal configurations. A kinematics-based locomotion reference with a height-conditioned joint-space offset guides learning, while a history-based state estimator infers base linear velocity and height and encodes residual load- and manipulation-induced disturbances in a compact latent representation. The framework is trained entirely in simulation and deployed on a full-size humanoid robot without fine-tuning. Simulation and real-world experiments demonstrate faster training, accurate height tracking, and stable loco-manipulation. Project page: https://lequn-f.github.io/LALO/

## Content
Humanoid robots deployed in industrial environments are required to perform load-carrying transportation tasks that tightly couple locomotion and manipulation. However, achieving stable and robust locomotion under varying payloads and upper-body motions is challenging due to dynamic coupling and partial observability. This paper presents a load-aware locomotion framework for industrial humanoids based on a decoupled yet coordinated loco-manipulation architecture. Lower-body locomotion is controlled via a reinforcement learning policy producing residual joint actions on kinematically derived nominal configurations. A kinematics-based locomotion reference with a height-conditioned joint-space offset guides learning, while a history-based state estimator infers base linear velocity and height and encodes residual load- and manipulation-induced disturbances in a compact latent representation. The framework is trained entirely in simulation and deployed on a full-size humanoid robot without fine-tuning. Simulation and real-world experiments demonstrate faster training, accurate height tracking, and stable loco-manipulation. Project page: https://lequn-f.github.io/LALO/

## 개요
산업 환경에 배치된 휴머노이드 로봇은 보행과 조작이 밀접하게 결합된 하중 운반 작업을 수행해야 합니다. 그러나 동적 결합과 부분 관측 가능성으로 인해 다양한 하중과 상체 움직임 하에서 안정적이고 강건한 보행을 달성하는 것은 어렵습니다. 본 논문은 분리되었지만 조정된 보행-조작 아키텍처를 기반으로 한 산업용 휴머노이드를 위한 하중 인식 보행 프레임워크를 제시합니다. 하체 보행은 운동학적으로 도출된 공칭 구성에 잔여 관절 동작을 생성하는 강화 학습 정책을 통해 제어됩니다. 높이 조건이 적용된 관절 공간 오프셋을 갖는 운동학 기반 보행 참조가 학습을 안내하며, 히스토리 기반 상태 추정기가 베이스 선형 속도와 높이를 추론하고 잔여 하중 및 조작 유발 교란을 압축된 잠재 표현으로 인코딩합니다. 프레임워크는 전적으로 시뮬레이션에서 훈련되고 미세 조정 없이 실제 크기 휴머노이드 로봇에 배치됩니다. 시뮬레이션 및 실제 실험은 더 빠른 훈련, 정확한 높이 추적, 안정적인 보행-조작을 입증합니다. 프로젝트 페이지: https://lequn-f.github.io/LALO/

## 핵심 내용
산업 환경에 배치된 휴머노이드 로봇은 보행과 조작이 밀접하게 결합된 하중 운반 작업을 수행해야 합니다. 그러나 동적 결합과 부분 관측 가능성으로 인해 다양한 하중과 상체 움직임 하에서 안정적이고 강건한 보행을 달성하는 것은 어렵습니다. 본 논문은 분리되었지만 조정된 보행-조작 아키텍처를 기반으로 한 산업용 휴머노이드를 위한 하중 인식 보행 프레임워크를 제시합니다. 하체 보행은 운동학적으로 도출된 공칭 구성에 잔여 관절 동작을 생성하는 강화 학습 정책을 통해 제어됩니다. 높이 조건이 적용된 관절 공간 오프셋을 갖는 운동학 기반 보행 참조가 학습을 안내하며, 히스토리 기반 상태 추정기가 베이스 선형 속도와 높이를 추론하고 잔여 하중 및 조작 유발 교란을 압축된 잠재 표현으로 인코딩합니다. 프레임워크는 전적으로 시뮬레이션에서 훈련되고 미세 조정 없이 실제 크기 휴머노이드 로봇에 배치됩니다. 시뮬레이션 및 실제 실험은 더 빠른 훈련, 정확한 높이 추적, 안정적인 보행-조작을 입증합니다. 프로젝트 페이지: https://lequn-f.github.io/LALO/
