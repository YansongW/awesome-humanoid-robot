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
  en: AMS trains a single humanoid control policy on heterogeneous data—human motion capture plus controllable synthetic balance
    motions—using a hybrid reward scheme and adaptive learning to unify agile dynamic skills with extreme balance maintenance.
  zh: Humanoid robots are envisioned to perform a wide range of tasks in human-centered environments, requiring controllers
    that combine agility with robust balance. Recent advances in locomotion and whole-body tracking have enabled impressive
    progress in either agile dynamic skills or stability-critical behaviors, but existing methods remain specialized, focusing
    on one capability while compromising the other. In this work, we introduce AMS (Agility Meets Stability), the first framework
    that unifies both dynamic motion tracking and extreme balance maintenance in a single policy. Our key insight is
  ko: AMS는 인체 동작 캡처와 제어 가능한 합성 균형 동작으로 구성된 이종 데이터, 하이브리드 보상 체계 및 적응형 학습을 통해 단일 정책을 훈련시켜 민첩한 동적 기술과 극한 균형 유지를 통합한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.17373v3.
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

## 概述
Humanoid robots are envisioned to perform a wide range of tasks in human-centered environments, requiring controllers that combine agility with robust balance. Recent advances in locomotion and whole-body tracking have enabled impressive progress in either agile dynamic skills or stability-critical behaviors, but existing methods remain specialized, focusing on one capability while compromising the other. In this work, we introduce AMS (Agility Meets Stability), the first framework that unifies both dynamic motion tracking and extreme balance maintenance in a single policy. Our key insight is to leverage heterogeneous data sources: human motion capture datasets that provide rich, agile behaviors, and physically constrained synthetic balance motions that capture stability configurations. To reconcile the divergent optimization goals of agility and stability, we design a hybrid reward scheme that applies general tracking objectives across all data while injecting balance-specific priors only into synthetic motions. Further, an adaptive learning strategy with performance-driven sampling and motion-specific reward shaping enables efficient training across diverse motion distributions. We validate AMS extensively in simulation and on a real Unitree G1 humanoid. Experiments demonstrate that a single policy can execute agile skills such as dancing and running, while also performing zero-shot extreme balance motions like Ip Man's Squat, highlighting AMS as a versatile control paradigm for future humanoid applications.

## 核心内容
Humanoid robots are envisioned to perform a wide range of tasks in human-centered environments, requiring controllers that combine agility with robust balance. Recent advances in locomotion and whole-body tracking have enabled impressive progress in either agile dynamic skills or stability-critical behaviors, but existing methods remain specialized, focusing on one capability while compromising the other. In this work, we introduce AMS (Agility Meets Stability), the first framework that unifies both dynamic motion tracking and extreme balance maintenance in a single policy. Our key insight is to leverage heterogeneous data sources: human motion capture datasets that provide rich, agile behaviors, and physically constrained synthetic balance motions that capture stability configurations. To reconcile the divergent optimization goals of agility and stability, we design a hybrid reward scheme that applies general tracking objectives across all data while injecting balance-specific priors only into synthetic motions. Further, an adaptive learning strategy with performance-driven sampling and motion-specific reward shaping enables efficient training across diverse motion distributions. We validate AMS extensively in simulation and on a real Unitree G1 humanoid. Experiments demonstrate that a single policy can execute agile skills such as dancing and running, while also performing zero-shot extreme balance motions like Ip Man's Squat, highlighting AMS as a versatile control paradigm for future humanoid applications.

## 参考
- http://arxiv.org/abs/2511.17373v3


