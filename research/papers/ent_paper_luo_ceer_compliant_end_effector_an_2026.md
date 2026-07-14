---
$id: ent_paper_luo_ceer_compliant_end_effector_an_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation'
  zh: CEER：作为分层人形机器人移动操作统一接口的柔顺末端执行器与根控制
  ko: 'CEER: 계층형 휴머노이드 로코-매니퓰레이션을 위한 통합 인터페이스로서의 순응적 최종 효과기 및 루트 제어'
summary:
  en: CEER proposes a compliant end-effector and root (EE-root) control abstraction for humanoid loco-manipulation, training
    a low-level policy via teacher-student distillation from a whole-body motion tracker so that heterogeneous high-level
    planners can command the robot without retraining.
  zh: CEER提出了一种用于人形机器人移动操作的柔顺末端执行器-根（EE-root）控制抽象，通过教师-学生蒸馏从全身运动追踪器训练底层策略，使异构高层规划器无需重新训练即可控制机器人。
  ko: CEER는 휴머노이드 로코-매니퓰레이션을 위한 순응적 최종 효과기-루트(EE-root) 제어 추상화를 제안하며, 전신 동작 추적기로부터 교사-학생 증류를 통해 저수준 정책을 학습시켜 재학습 없이 이종 고수준
    플래너가 로봇을 명령할 수 있게 한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- whole_body_control
- end_effector_control
- loco_manipulation
- hierarchical_planning
- teacher_student_distillation
- compliant_control
- humanoid_robotics
- motion_tracking
- sim_to_real
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.19981v1.
sources:
- id: src_001
  type: paper
  title: 'CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2605.19981
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Humanoid robots have achieved impressive locomotion performance, yet contact-rich and long-horizon manipulation remains a major bottleneck. Manipulation is inherently contact-rich and demands compliant whole-body control for stable interaction, while its diversity and long-horizon nature favor modular, planner-compatible interfaces over joint-space tracking.   We propose CEER, a compliant end-effector-root (EE-root) control abstraction for modular humanoid loco-manipulation within a hierarchical planning framework. CEER enables compliance-aware whole-body control in an interpretable task space defined by root motion commands and end-effector pose targets, and supports plug-and-play integration with heterogeneous high-level planners. A teacher-student framework is adopted to distill a general motion-tracking controller into a low-level policy that consumes only EE-root commands.   We further construct a hierarchical system that integrates heterogeneous planners and task modules through the EE-root interface, enabling diverse manipulation tasks without retraining the underlying whole-body policy. Experiments in simulation and on hardware demonstrate 3.3 cm end-effector tracking accuracy with substantially reduced jerk compared to baselines, stable contact-rich manipulation under teleoperation, and up to 70% success in simulated single-object loco-manipulation tasks within a room-scale environment. These results indicate that compliant EE-root control provides a practical abstraction for humanoid loco-manipulation, enabling modular and scalable integration of diverse skills.

## 核心内容
Humanoid robots have achieved impressive locomotion performance, yet contact-rich and long-horizon manipulation remains a major bottleneck. Manipulation is inherently contact-rich and demands compliant whole-body control for stable interaction, while its diversity and long-horizon nature favor modular, planner-compatible interfaces over joint-space tracking.   We propose CEER, a compliant end-effector-root (EE-root) control abstraction for modular humanoid loco-manipulation within a hierarchical planning framework. CEER enables compliance-aware whole-body control in an interpretable task space defined by root motion commands and end-effector pose targets, and supports plug-and-play integration with heterogeneous high-level planners. A teacher-student framework is adopted to distill a general motion-tracking controller into a low-level policy that consumes only EE-root commands.   We further construct a hierarchical system that integrates heterogeneous planners and task modules through the EE-root interface, enabling diverse manipulation tasks without retraining the underlying whole-body policy. Experiments in simulation and on hardware demonstrate 3.3 cm end-effector tracking accuracy with substantially reduced jerk compared to baselines, stable contact-rich manipulation under teleoperation, and up to 70% success in simulated single-object loco-manipulation tasks within a room-scale environment. These results indicate that compliant EE-root control provides a practical abstraction for humanoid loco-manipulation, enabling modular and scalable integration of diverse skills.

## 参考
- http://arxiv.org/abs/2605.19981v1

