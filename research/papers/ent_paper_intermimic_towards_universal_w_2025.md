---
$id: ent_paper_intermimic_towards_universal_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions'
  zh: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions'
  ko: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions'
summary:
  en: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions is a 2025 work on physics-based
    character animation for humanoid robots, with open-source code available.'
  zh: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions is a 2025 work on physics-based
    character animation for humanoid robots, with open-source code available.'
  ko: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions is a 2025 work on physics-based
    character animation for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- intermimic
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.20390v2.
sources:
- id: src_001
  type: paper
  title: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions (arXiv)'
  url: https://arxiv.org/abs/2502.20390
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions project page'
  url: https://sirui-xu.github.io/InterMimic/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving realistic simulations of humans interacting with a wide range of objects has long been a fundamental goal. Extending physics-based motion imitation to complex human-object interactions (HOIs) is challenging due to intricate human-object coupling, variability in object geometries, and artifacts in motion capture data, such as inaccurate contacts and limited hand detail. We introduce InterMimic, a framework that enables a single policy to robustly learn from hours of imperfect MoCap data covering diverse full-body interactions with dynamic and varied objects. Our key insight is to employ a curriculum strategy -- perfect first, then scale up. We first train subject-specific teacher policies to mimic, retarget, and refine motion capture data. Next, we distill these teachers into a student policy, with the teachers acting as online experts providing direct supervision, as well as high-quality references. Notably, we incorporate RL fine-tuning on the student policy to surpass mere demonstration replication and achieve higher-quality solutions. Our experiments demonstrate that InterMimic produces realistic and diverse interactions across multiple HOI datasets. The learned policy generalizes in a zero-shot manner and seamlessly integrates with kinematic generators, elevating the framework from mere imitation to generative modeling of complex human-object interactions.

## 核心内容
Achieving realistic simulations of humans interacting with a wide range of objects has long been a fundamental goal. Extending physics-based motion imitation to complex human-object interactions (HOIs) is challenging due to intricate human-object coupling, variability in object geometries, and artifacts in motion capture data, such as inaccurate contacts and limited hand detail. We introduce InterMimic, a framework that enables a single policy to robustly learn from hours of imperfect MoCap data covering diverse full-body interactions with dynamic and varied objects. Our key insight is to employ a curriculum strategy -- perfect first, then scale up. We first train subject-specific teacher policies to mimic, retarget, and refine motion capture data. Next, we distill these teachers into a student policy, with the teachers acting as online experts providing direct supervision, as well as high-quality references. Notably, we incorporate RL fine-tuning on the student policy to surpass mere demonstration replication and achieve higher-quality solutions. Our experiments demonstrate that InterMimic produces realistic and diverse interactions across multiple HOI datasets. The learned policy generalizes in a zero-shot manner and seamlessly integrates with kinematic generators, elevating the framework from mere imitation to generative modeling of complex human-object interactions.

## 参考
- http://arxiv.org/abs/2502.20390v2

## Overview
Achieving realistic simulations of humans interacting with a wide range of objects has long been a fundamental goal. Extending physics-based motion imitation to complex human-object interactions (HOIs) is challenging due to intricate human-object coupling, variability in object geometries, and artifacts in motion capture data, such as inaccurate contacts and limited hand detail. We introduce InterMimic, a framework that enables a single policy to robustly learn from hours of imperfect MoCap data covering diverse full-body interactions with dynamic and varied objects. Our key insight is to employ a curriculum strategy -- perfect first, then scale up. We first train subject-specific teacher policies to mimic, retarget, and refine motion capture data. Next, we distill these teachers into a student policy, with the teachers acting as online experts providing direct supervision, as well as high-quality references. Notably, we incorporate RL fine-tuning on the student policy to surpass mere demonstration replication and achieve higher-quality solutions. Our experiments demonstrate that InterMimic produces realistic and diverse interactions across multiple HOI datasets. The learned policy generalizes in a zero-shot manner and seamlessly integrates with kinematic generators, elevating the framework from mere imitation to generative modeling of complex human-object interactions.

## Content
Achieving realistic simulations of humans interacting with a wide range of objects has long been a fundamental goal. Extending physics-based motion imitation to complex human-object interactions (HOIs) is challenging due to intricate human-object coupling, variability in object geometries, and artifacts in motion capture data, such as inaccurate contacts and limited hand detail. We introduce InterMimic, a framework that enables a single policy to robustly learn from hours of imperfect MoCap data covering diverse full-body interactions with dynamic and varied objects. Our key insight is to employ a curriculum strategy -- perfect first, then scale up. We first train subject-specific teacher policies to mimic, retarget, and refine motion capture data. Next, we distill these teachers into a student policy, with the teachers acting as online experts providing direct supervision, as well as high-quality references. Notably, we incorporate RL fine-tuning on the student policy to surpass mere demonstration replication and achieve higher-quality solutions. Our experiments demonstrate that InterMimic produces realistic and diverse interactions across multiple HOI datasets. The learned policy generalizes in a zero-shot manner and seamlessly integrates with kinematic generators, elevating the framework from mere imitation to generative modeling of complex human-object interactions.

## 개요
다양한 객체와 상호작용하는 인간의 현실적인 시뮬레이션을 구현하는 것은 오랫동안 근본적인 목표였습니다. 물리 기반 동작 모방을 복잡한 인간-객체 상호작용(HOI)으로 확장하는 것은 복잡한 인간-객체 결합, 객체 형상의 다양성, 그리고 부정확한 접촉 및 제한된 손 디테일과 같은 모션 캡처 데이터의 아티팩트로 인해 어렵습니다. 우리는 동적이고 다양한 객체와의 전신 상호작용을 포괄하는 수 시간의 불완전한 MoCap 데이터를 단일 정책이 강건하게 학습할 수 있는 프레임워크인 InterMimic을 소개합니다. 우리의 핵심 통찰은 커리큘럼 전략, 즉 먼저 완벽하게 한 다음 확장하는 것을 사용하는 것입니다. 먼저 피험자별 교사 정책을 훈련하여 모션 캡처 데이터를 모방, 리타겟팅 및 정제합니다. 다음으로, 이 교사들을 학생 정책으로 증류하며, 교사들은 직접적인 감독과 고품질 참조를 제공하는 온라인 전문가 역할을 합니다. 특히, 우리는 학생 정책에 RL 미세 조정을 통합하여 단순한 시연 복제를 넘어 더 높은 품질의 솔루션을 달성합니다. 우리의 실험은 InterMimic이 여러 HOI 데이터셋에서 현실적이고 다양한 상호작용을 생성함을 보여줍니다. 학습된 정책은 제로샷 방식으로 일반화되며 운동학적 생성기와 원활하게 통합되어, 프레임워크를 단순한 모방에서 복잡한 인간-객체 상호작용의 생성 모델링으로 끌어올립니다.

## 핵심 내용
다양한 객체와 상호작용하는 인간의 현실적인 시뮬레이션을 구현하는 것은 오랫동안 근본적인 목표였습니다. 물리 기반 동작 모방을 복잡한 인간-객체 상호작용(HOI)으로 확장하는 것은 복잡한 인간-객체 결합, 객체 형상의 다양성, 그리고 부정확한 접촉 및 제한된 손 디테일과 같은 모션 캡처 데이터의 아티팩트로 인해 어렵습니다. 우리는 동적이고 다양한 객체와의 전신 상호작용을 포괄하는 수 시간의 불완전한 MoCap 데이터를 단일 정책이 강건하게 학습할 수 있는 프레임워크인 InterMimic을 소개합니다. 우리의 핵심 통찰은 커리큘럼 전략, 즉 먼저 완벽하게 한 다음 확장하는 것을 사용하는 것입니다. 먼저 피험자별 교사 정책을 훈련하여 모션 캡처 데이터를 모방, 리타겟팅 및 정제합니다. 다음으로, 이 교사들을 학생 정책으로 증류하며, 교사들은 직접적인 감독과 고품질 참조를 제공하는 온라인 전문가 역할을 합니다. 특히, 우리는 학생 정책에 RL 미세 조정을 통합하여 단순한 시연 복제를 넘어 더 높은 품질의 솔루션을 달성합니다. 우리의 실험은 InterMimic이 여러 HOI 데이터셋에서 현실적이고 다양한 상호작용을 생성함을 보여줍니다. 학습된 정책은 제로샷 방식으로 일반화되며 운동학적 생성기와 원활하게 통합되어, 프레임워크를 단순한 모방에서 복잡한 인간-객체 상호작용의 생성 모델링으로 끌어올립니다.
