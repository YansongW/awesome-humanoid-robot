---
$id: ent_paper_pan_agility_meets_stability_versat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Agility Meets Stability: Versatile Humanoid Control with Heterogeneous Data'
  zh: 敏捷与稳定兼得：基于异构数据的多用途人形机器人控制
  ko: '민첩성과 안정성의 결합: 이종 데이터를 활용한 다목적 휴머노이드 제어'
summary:
  en: AMS trains a single humanoid control policy on heterogeneous data—human motion
    capture plus controllable synthetic balance motions—using a hybrid reward scheme
    and adaptive learning to unify agile dynamic skills with extreme balance maintenance.
  zh: AMS通过异构数据（人体动作捕捉与可控合成平衡动作）、混合奖励机制与自适应学习训练单一控制策略，将敏捷动态技能与极限平衡能力统一于人形机器人控制中。
  ko: AMS는 인체 동작 캡처와 제어 가능한 합성 균형 동작으로 구성된 이종 데이터, 하이브리드 보상 체계 및 적응형 학습을 통해 단일 정책을
    훈련시켜 민첩한 동적 기술과 극한 균형 유지를 통합한다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- whole_body_control
- motion_tracking
- balance_control
- humanoid_locomotion
- teacher_student_rl
- sim_to_real
- unitree_g1
- amass
- lafan1
- isaacgym
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from abstract and metadata; full-text verification needed for
    exact section citations and relationship evidence.
sources:
- id: src_001
  type: paper
  title: 'Agility Meets Stability: Versatile Humanoid Control with Heterogeneous Data'
  url: https://arxiv.org/abs/2511.17373
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Existing humanoid controllers excel at either agile dynamic motions or stability-critical behaviors, but rarely both. AMS addresses this specialization gap by training a single policy on heterogeneous data that combines human motion capture datasets with physically constrained synthetic balance motions. The framework uses a teacher-student reinforcement learning pipeline in which a teacher policy is trained on privileged state information and distilled into a student policy for deployment.

To reconcile the divergent optimization goals of agility and stability, AMS employs a hybrid reward scheme: general tracking objectives are applied across all data sources, while balance-specific priors are injected only into synthetic balance motions. An adaptive learning strategy further adjusts data sampling and reward shaping based on training performance, enabling efficient learning across diverse motion distributions. The approach is validated extensively in simulation and on a real Unitree G1 humanoid, where a single policy executes both dancing and running, as well as zero-shot extreme balance motions such as Ip Man's Squat.

The work also explores interactive teleoperation as an application, using RGB-based pose estimation to drive the policy on real hardware. However, the authors note limitations in precise end-effector control and noise in global motion estimation from RGB teleoperation.

## Key Contributions

- Introduced AMS, the first framework to unify dynamic motion tracking and extreme balance maintenance in a single policy.
- Developed a heterogeneous-data learning approach combining human MoCap (AMASS, LAFAN1) and controllable synthetic balance motions with hybrid rewards and adaptive learning.
- Demonstrated real-world execution of both agile dynamic motions and zero-shot extreme balance control on a Unitree G1 humanoid, enabling interactive teleoperation.

## Relevance to Humanoid Robotics

AMS advances versatile whole-body control for humanoid robots by showing that a single policy can span both agility-demanding skills and stability-critical postures. This capability is essential for real-world deployment in human-centered environments, where controllers must switch between dynamic locomotion and contact-rich, balance-sensitive tasks. The sim-to-real transfer on a commercially relevant platform (Unitree G1) further strengthens its practical relevance for the humanoid robotics industry.
