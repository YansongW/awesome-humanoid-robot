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

