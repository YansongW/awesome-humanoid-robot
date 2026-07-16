---
$id: ent_paper_kungfubot_2_learning_versatile_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control'
  zh: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control'
  ko: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control'
summary:
  en: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
  zh: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
  ko: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- kungfubot_2
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.16638v1.
sources:
- id: src_001
  type: paper
  title: 'KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control (arXiv)'
  url: https://arxiv.org/abs/2509.16638
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning versatile whole-body skills by tracking various human motions is a fundamental step toward general-purpose humanoid robots. This task is particularly challenging because a single policy must master a broad repertoire of motion skills while ensuring stability over long-horizon sequences. To this end, we present VMS, a unified whole-body controller that enables humanoid robots to learn diverse and dynamic behaviors within a single policy. Our framework integrates a hybrid tracking objective that balances local motion fidelity with global trajectory consistency, and an Orthogonal Mixture-of-Experts (OMoE) architecture that encourages skill specialization while enhancing generalization across motions. A segment-level tracking reward is further introduced to relax rigid step-wise matching, enhancing robustness when handling global displacements and transient inaccuracies. We validate VMS extensively in both simulation and real-world experiments, demonstrating accurate imitation of dynamic skills, stable performance over minute-long sequences, and strong generalization to unseen motions. These results highlight the potential of VMS as a scalable foundation for versatile humanoid whole-body control. The project page is available at https://kungfubot2-humanoid.github.io.

## 核心内容
Learning versatile whole-body skills by tracking various human motions is a fundamental step toward general-purpose humanoid robots. This task is particularly challenging because a single policy must master a broad repertoire of motion skills while ensuring stability over long-horizon sequences. To this end, we present VMS, a unified whole-body controller that enables humanoid robots to learn diverse and dynamic behaviors within a single policy. Our framework integrates a hybrid tracking objective that balances local motion fidelity with global trajectory consistency, and an Orthogonal Mixture-of-Experts (OMoE) architecture that encourages skill specialization while enhancing generalization across motions. A segment-level tracking reward is further introduced to relax rigid step-wise matching, enhancing robustness when handling global displacements and transient inaccuracies. We validate VMS extensively in both simulation and real-world experiments, demonstrating accurate imitation of dynamic skills, stable performance over minute-long sequences, and strong generalization to unseen motions. These results highlight the potential of VMS as a scalable foundation for versatile humanoid whole-body control. The project page is available at https://kungfubot2-humanoid.github.io.

## 参考
- http://arxiv.org/abs/2509.16638v1

## Overview
Learning versatile whole-body skills by tracking various human motions is a fundamental step toward general-purpose humanoid robots. This task is particularly challenging because a single policy must master a broad repertoire of motion skills while ensuring stability over long-horizon sequences. To this end, we present VMS, a unified whole-body controller that enables humanoid robots to learn diverse and dynamic behaviors within a single policy. Our framework integrates a hybrid tracking objective that balances local motion fidelity with global trajectory consistency, and an Orthogonal Mixture-of-Experts (OMoE) architecture that encourages skill specialization while enhancing generalization across motions. A segment-level tracking reward is further introduced to relax rigid step-wise matching, enhancing robustness when handling global displacements and transient inaccuracies. We validate VMS extensively in both simulation and real-world experiments, demonstrating accurate imitation of dynamic skills, stable performance over minute-long sequences, and strong generalization to unseen motions. These results highlight the potential of VMS as a scalable foundation for versatile humanoid whole-body control. The project page is available at https://kungfubot2-humanoid.github.io.

## Content
Learning versatile whole-body skills by tracking various human motions is a fundamental step toward general-purpose humanoid robots. This task is particularly challenging because a single policy must master a broad repertoire of motion skills while ensuring stability over long-horizon sequences. To this end, we present VMS, a unified whole-body controller that enables humanoid robots to learn diverse and dynamic behaviors within a single policy. Our framework integrates a hybrid tracking objective that balances local motion fidelity with global trajectory consistency, and an Orthogonal Mixture-of-Experts (OMoE) architecture that encourages skill specialization while enhancing generalization across motions. A segment-level tracking reward is further introduced to relax rigid step-wise matching, enhancing robustness when handling global displacements and transient inaccuracies. We validate VMS extensively in both simulation and real-world experiments, demonstrating accurate imitation of dynamic skills, stable performance over minute-long sequences, and strong generalization to unseen motions. These results highlight the potential of VMS as a scalable foundation for versatile humanoid whole-body control. The project page is available at https://kungfubot2-humanoid.github.io.

## 개요
다양한 인간 동작을 추적하여 다재다능한 전신 기술을 학습하는 것은 범용 휴머노이드 로봇을 향한 기본 단계입니다. 이 작업은 단일 정책이 광범위한 동작 기술을 숙달하면서도 장기 시퀀스에서 안정성을 보장해야 하기 때문에 특히 어렵습니다. 이를 위해 우리는 VMS를 제안합니다. VMS는 휴머노이드 로봇이 단일 정책 내에서 다양하고 역동적인 행동을 학습할 수 있도록 하는 통합 전신 제어기입니다. 우리의 프레임워크는 국소 동작 충실도와 전역 궤적 일관성의 균형을 맞추는 하이브리드 추적 목표와, 동작 전반의 일반화를 향상시키면서 기술 전문화를 장려하는 직교 혼합 전문가(OMoE) 아키텍처를 통합합니다. 또한 세그먼트 수준 추적 보상을 도입하여 엄격한 단계별 매칭을 완화하고, 전역 변위 및 일시적 부정확성을 처리할 때 강건성을 향상시킵니다. 우리는 시뮬레이션과 실제 실험에서 VMS를 광범위하게 검증하여, 역동적 기술의 정확한 모방, 1분 이상의 시퀀스에서의 안정적 성능, 그리고 보지 못한 동작에 대한 강력한 일반화를 입증했습니다. 이러한 결과는 VMS가 다재다능한 휴머노이드 전신 제어를 위한 확장 가능한 기반으로서의 잠재력을 강조합니다. 프로젝트 페이지는 https://kungfubot2-humanoid.github.io 에서 확인할 수 있습니다.

## 핵심 내용
다양한 인간 동작을 추적하여 다재다능한 전신 기술을 학습하는 것은 범용 휴머노이드 로봇을 향한 기본 단계입니다. 이 작업은 단일 정책이 광범위한 동작 기술을 숙달하면서도 장기 시퀀스에서 안정성을 보장해야 하기 때문에 특히 어렵습니다. 이를 위해 우리는 VMS를 제안합니다. VMS는 휴머노이드 로봇이 단일 정책 내에서 다양하고 역동적인 행동을 학습할 수 있도록 하는 통합 전신 제어기입니다. 우리의 프레임워크는 국소 동작 충실도와 전역 궤적 일관성의 균형을 맞추는 하이브리드 추적 목표와, 동작 전반의 일반화를 향상시키면서 기술 전문화를 장려하는 직교 혼합 전문가(OMoE) 아키텍처를 통합합니다. 또한 세그먼트 수준 추적 보상을 도입하여 엄격한 단계별 매칭을 완화하고, 전역 변위 및 일시적 부정확성을 처리할 때 강건성을 향상시킵니다. 우리는 시뮬레이션과 실제 실험에서 VMS를 광범위하게 검증하여, 역동적 기술의 정확한 모방, 1분 이상의 시퀀스에서의 안정적 성능, 그리고 보지 못한 동작에 대한 강력한 일반화를 입증했습니다. 이러한 결과는 VMS가 다재다능한 휴머노이드 전신 제어를 위한 확장 가능한 기반으로서의 잠재력을 강조합니다. 프로젝트 페이지는 https://kungfubot2-humanoid.github.io 에서 확인할 수 있습니다.
