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

## Overview
Humanoid robots are envisioned to perform a wide range of tasks in human-centered environments, requiring controllers that combine agility with robust balance. Recent advances in locomotion and whole-body tracking have enabled impressive progress in either agile dynamic skills or stability-critical behaviors, but existing methods remain specialized, focusing on one capability while compromising the other. In this work, we introduce AMS (Agility Meets Stability), the first framework that unifies both dynamic motion tracking and extreme balance maintenance in a single policy. Our key insight is to leverage heterogeneous data sources: human motion capture datasets that provide rich, agile behaviors, and physically constrained synthetic balance motions that capture stability configurations. To reconcile the divergent optimization goals of agility and stability, we design a hybrid reward scheme that applies general tracking objectives across all data while injecting balance-specific priors only into synthetic motions. Further, an adaptive learning strategy with performance-driven sampling and motion-specific reward shaping enables efficient training across diverse motion distributions. We validate AMS extensively in simulation and on a real Unitree G1 humanoid. Experiments demonstrate that a single policy can execute agile skills such as dancing and running, while also performing zero-shot extreme balance motions like Ip Man's Squat, highlighting AMS as a versatile control paradigm for future humanoid applications.

## Content
Humanoid robots are envisioned to perform a wide range of tasks in human-centered environments, requiring controllers that combine agility with robust balance. Recent advances in locomotion and whole-body tracking have enabled impressive progress in either agile dynamic skills or stability-critical behaviors, but existing methods remain specialized, focusing on one capability while compromising the other. In this work, we introduce AMS (Agility Meets Stability), the first framework that unifies both dynamic motion tracking and extreme balance maintenance in a single policy. Our key insight is to leverage heterogeneous data sources: human motion capture datasets that provide rich, agile behaviors, and physically constrained synthetic balance motions that capture stability configurations. To reconcile the divergent optimization goals of agility and stability, we design a hybrid reward scheme that applies general tracking objectives across all data while injecting balance-specific priors only into synthetic motions. Further, an adaptive learning strategy with performance-driven sampling and motion-specific reward shaping enables efficient training across diverse motion distributions. We validate AMS extensively in simulation and on a real Unitree G1 humanoid. Experiments demonstrate that a single policy can execute agile skills such as dancing and running, while also performing zero-shot extreme balance motions like Ip Man's Squat, highlighting AMS as a versatile control paradigm for future humanoid applications.

## 개요
휴머노이드 로봇은 인간 중심 환경에서 다양한 작업을 수행할 것으로 예상되며, 민첩성과 강력한 균형을 결합한 제어기가 필요합니다. 최근 보행 및 전신 추적의 발전으로 민첩한 동적 기술이나 안정성이 중요한 행동에서 인상적인 진전이 이루어졌지만, 기존 방법은 한 가지 능력에 집중하고 다른 능력을 희생하는 특화된 방식에 머물러 있습니다. 본 연구에서는 동적 동작 추적과 극한 균형 유지를 단일 정책으로 통합한 최초의 프레임워크인 AMS(Agility Meets Stability)를 소개합니다. 핵심 통찰은 다양한 데이터 소스를 활용하는 데 있습니다: 풍부하고 민첩한 행동을 제공하는 인간 모션 캡처 데이터셋과 안정성 구성을 포착하는 물리적 제약이 있는 합성 균형 동작입니다. 민첩성과 안정성이라는 상이한 최적화 목표를 조화시키기 위해, 모든 데이터에 일반적인 추적 목표를 적용하면서 합성 동작에만 균형 특화 사전 지식을 주입하는 하이브리드 보상 체계를 설계했습니다. 또한, 성능 기반 샘플링과 동작 특화 보상 형성을 통한 적응형 학습 전략으로 다양한 동작 분포에서 효율적인 훈련이 가능합니다. 시뮬레이션과 실제 Unitree G1 휴머노이드에서 AMS를 광범위하게 검증했습니다. 실험 결과, 단일 정책으로 춤과 달리기 같은 민첩한 기술을 실행하면서, 이소룡 스쿼트와 같은 제로샷 극한 균형 동작도 수행할 수 있음을 보여주며, AMS가 미래 휴머노이드 응용을 위한 다목적 제어 패러다임임을 강조합니다.

## 핵심 내용
휴머노이드 로봇은 인간 중심 환경에서 다양한 작업을 수행할 것으로 예상되며, 민첩성과 강력한 균형을 결합한 제어기가 필요합니다. 최근 보행 및 전신 추적의 발전으로 민첩한 동적 기술이나 안정성이 중요한 행동에서 인상적인 진전이 이루어졌지만, 기존 방법은 한 가지 능력에 집중하고 다른 능력을 희생하는 특화된 방식에 머물러 있습니다. 본 연구에서는 동적 동작 추적과 극한 균형 유지를 단일 정책으로 통합한 최초의 프레임워크인 AMS(Agility Meets Stability)를 소개합니다. 핵심 통찰은 다양한 데이터 소스를 활용하는 데 있습니다: 풍부하고 민첩한 행동을 제공하는 인간 모션 캡처 데이터셋과 안정성 구성을 포착하는 물리적 제약이 있는 합성 균형 동작입니다. 민첩성과 안정성이라는 상이한 최적화 목표를 조화시키기 위해, 모든 데이터에 일반적인 추적 목표를 적용하면서 합성 동작에만 균형 특화 사전 지식을 주입하는 하이브리드 보상 체계를 설계했습니다. 또한, 성능 기반 샘플링과 동작 특화 보상 형성을 통한 적응형 학습 전략으로 다양한 동작 분포에서 효율적인 훈련이 가능합니다. 시뮬레이션과 실제 Unitree G1 휴머노이드에서 AMS를 광범위하게 검증했습니다. 실험 결과, 단일 정책으로 춤과 달리기 같은 민첩한 기술을 실행하면서, 이소룡 스쿼트와 같은 제로샷 극한 균형 동작도 수행할 수 있음을 보여주며, AMS가 미래 휴머노이드 응용을 위한 다목적 제어 패러다임임을 강조합니다.
