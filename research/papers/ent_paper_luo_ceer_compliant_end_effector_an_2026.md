---
$id: ent_paper_luo_ceer_compliant_end_effector_an_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical
    Humanoid Loco-Manipulation'
  zh: CEER：作为分层人形机器人移动操作统一接口的柔顺末端执行器与根控制
  ko: 'CEER: 계층형 휴머노이드 로코-매니퓰레이션을 위한 통합 인터페이스로서의 순응적 최종 효과기 및 루트 제어'
summary:
  en: CEER proposes a compliant end-effector and root (EE-root) control abstraction
    for humanoid loco-manipulation, training a low-level policy via teacher-student
    distillation from a whole-body motion tracker so that heterogeneous high-level
    planners can command the robot without retraining.
  zh: CEER提出了一种用于人形机器人移动操作的柔顺末端执行器-根（EE-root）控制抽象，通过教师-学生蒸馏从全身运动追踪器训练底层策略，使异构高层规划器无需重新训练即可控制机器人。
  ko: CEER는 휴머노이드 로코-매니퓰레이션을 위한 순응적 최종 효과기-루트(EE-root) 제어 추상화를 제안하며, 전신 동작 추적기로부터
    교사-학생 증류를 통해 저수준 정책을 학습시켜 재학습 없이 이종 고수준 플래너가 로봇을 명령할 수 있게 한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text review is needed
    before marking verified.
sources:
- id: src_001
  type: paper
  title: 'CEER: Compliant End-Effector and Root Control as a Unified Interface for
    Hierarchical Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2605.19981
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

CEER formulates humanoid loco-manipulation as compliant end-effector and root (EE-root) control. It defines an interpretable task space using root motion commands and end-effector pose targets, and distills a general whole-body motion tracker into a low-level policy that consumes only EE-root commands. This design decouples high-level task planning from morphology-specific joint-space tracking and allows plug-and-play integration with heterogeneous planners.

The system is organized into three hierarchical layers. A high-level task manager (e.g., an LLM-based planner) selects skills and goals; mid-level planners generate EE-root trajectories for each skill; and the low-level policy executes compliant whole-body control. The low-level policy is trained with a teacher-student framework, where the teacher is a whole-body motion tracker trained on AMASS and the student is conditioned only on EE-root commands and proprioception.

Experiments are conducted in simulation and on a real Unitree G1 robot equipped with a RealSense D435 camera and custom end-effector tools. The system achieves 3.3 cm end-effector tracking accuracy with substantially reduced jerk compared to baselines, stable contact-rich manipulation under teleoperation, and up to 70% success in simulated room-scale single-object loco-manipulation tasks.

## Key Contributions

- Proposes CEER, a compliant EE-root control abstraction that unifies task-level execution for humanoid loco-manipulation independent of morphology-specific joint targets.
- Designs a three-layer hierarchical framework that decouples high-level planning from low-level control via a planner-compatible EE-root interface.
- Demonstrates plug-and-play integration of heterogeneous mid-level planners and skills without retraining the low-level whole-body policy.
- Achieves 3.3 cm end-effector tracking accuracy with substantially reduced jerk and stable real-world contact-rich teleoperated manipulation.
- Shows up to 70% success on simulated room-scale single-object loco-manipulation tasks through an LLM-based task manager.

## Relevance to Humanoid Robotics

CEER addresses a key bottleneck in humanoid deployment: contact-rich, long-horizon manipulation. By providing a planner-agnostic EE-root interface, it enables scalable integration of diverse skills and automated perception-planning-execution pipelines. The compliant whole-body control abstraction is particularly relevant for industrial and service applications where robots must interact safely and stably with unstructured environments while retaining modularity across different embodiments.
