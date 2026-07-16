---
$id: ent_paper_haic_humanoid_agile_object_int_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model'
  zh: 对象也有自己的动力学
  ko: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model'
summary:
  en: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model is a knowledge node related to paper
    in the humanoid robot value chain.'
  zh: Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction
    (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated
    objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces
    and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external
    state estimation. Our key contribution is a dynamics predictor that estimates high-order object states (velocity, acceleration)
    solely from proprioceptive history. These predictions are projected onto static geometric priors to form a spatially grounded
    dynamic occupancy map, enabling the policy to infer collision
  ko: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model is a knowledge node related to paper
    in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- compliance
- contact_rich
- fall_recovery
- load_carrying
- safety
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11758v2.
sources:
- id: src_001
  type: paper
  title: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model (arXiv)'
  url: https://arxiv.org/abs/2602.11758
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 对象也有自己的动力学 project page
  url: https://haic-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external state estimation. Our key contribution is a dynamics predictor that estimates high-order object states (velocity, acceleration) solely from proprioceptive history. These predictions are projected onto static geometric priors to form a spatially grounded dynamic occupancy map, enabling the policy to infer collision boundaries and contact affordances in blind spots. We use asymmetric fine-tuning, where a world model continuously adapts to the student policy's exploration, ensuring robust state estimation under distribution shifts. Experiments on a humanoid robot show HAIC achieves high success rates in agile tasks (skateboarding, cart pushing/pulling under various loads) by proactively compensating for inertial perturbations, and also masters multi-object long-horizon tasks like carrying a box across varied terrain by predicting the dynamics of multiple objects.

## 核心内容
Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external state estimation. Our key contribution is a dynamics predictor that estimates high-order object states (velocity, acceleration) solely from proprioceptive history. These predictions are projected onto static geometric priors to form a spatially grounded dynamic occupancy map, enabling the policy to infer collision boundaries and contact affordances in blind spots. We use asymmetric fine-tuning, where a world model continuously adapts to the student policy's exploration, ensuring robust state estimation under distribution shifts. Experiments on a humanoid robot show HAIC achieves high success rates in agile tasks (skateboarding, cart pushing/pulling under various loads) by proactively compensating for inertial perturbations, and also masters multi-object long-horizon tasks like carrying a box across varied terrain by predicting the dynamics of multiple objects.

## 参考
- http://arxiv.org/abs/2602.11758v2

## Overview
Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external state estimation. Our key contribution is a dynamics predictor that estimates high-order object states (velocity, acceleration) solely from proprioceptive history. These predictions are projected onto static geometric priors to form a spatially grounded dynamic occupancy map, enabling the policy to infer collision boundaries and contact affordances in blind spots. We use asymmetric fine-tuning, where a world model continuously adapts to the student policy's exploration, ensuring robust state estimation under distribution shifts. Experiments on a humanoid robot show HAIC achieves high success rates in agile tasks (skateboarding, cart pushing/pulling under various loads) by proactively compensating for inertial perturbations, and also masters multi-object long-horizon tasks like carrying a box across varied terrain by predicting the dynamics of multiple objects.

## Content
Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external state estimation. Our key contribution is a dynamics predictor that estimates high-order object states (velocity, acceleration) solely from proprioceptive history. These predictions are projected onto static geometric priors to form a spatially grounded dynamic occupancy map, enabling the policy to infer collision boundaries and contact affordances in blind spots. We use asymmetric fine-tuning, where a world model continuously adapts to the student policy's exploration, ensuring robust state estimation under distribution shifts. Experiments on a humanoid robot show HAIC achieves high success rates in agile tasks (skateboarding, cart pushing/pulling under various loads) by proactively compensating for inertial perturbations, and also masters multi-object long-horizon tasks like carrying a box across varied terrain by predicting the dynamics of multiple objects.

## 개요
휴머노이드 로봇은 비정형 환경에서 복잡한 전신 작업을 수행할 가능성을 보여줍니다. 인간-객체 상호작용(HOI)이 발전했지만, 대부분의 방법은 로봇에 강체로 결합된 완전 구동 객체에 초점을 맞추며, 독립적인 동역학과 비홀로노믹 제약을 가진 저구동 객체는 무시합니다. 이러한 객체는 결합력과 폐색으로 인한 제어 문제를 야기합니다. 우리는 외부 상태 추정 없이 다양한 객체 동역학에 걸쳐 강건한 상호작용을 위한 통합 프레임워크인 HAIC를 제시합니다. 핵심 기여는 고유수용성 히스토리만으로 고차 객체 상태(속도, 가속도)를 추정하는 동역학 예측기입니다. 이러한 예측은 정적 기하학적 사전 정보에 투영되어 공간적으로 기반한 동적 점유 맵을 형성하며, 이를 통해 정책이 사각지대에서 충돌 경계와 접촉 가능성을 추론할 수 있습니다. 우리는 비대칭 미세 조정을 사용하여 세계 모델이 학생 정책의 탐색에 지속적으로 적응하도록 하여 분포 변화 하에서도 강건한 상태 추정을 보장합니다. 휴머노이드 로봇 실험에서 HAIC는 관성 섭동을 능동적으로 보상함으로써 민첩한 작업(스케이트보드, 다양한 하중에서 카트 밀기/끌기)에서 높은 성공률을 달성하고, 여러 객체의 동역학을 예측하여 다양한 지형에서 상자를 운반하는 다중 객체 장기 작업도 마스터함을 보여줍니다.

## 핵심 내용
휴머노이드 로봇은 비정형 환경에서 복잡한 전신 작업을 수행할 가능성을 보여줍니다. 인간-객체 상호작용(HOI)이 발전했지만, 대부분의 방법은 로봇에 강체로 결합된 완전 구동 객체에 초점을 맞추며, 독립적인 동역학과 비홀로노믹 제약을 가진 저구동 객체는 무시합니다. 이러한 객체는 결합력과 폐색으로 인한 제어 문제를 야기합니다. 우리는 외부 상태 추정 없이 다양한 객체 동역학에 걸쳐 강건한 상호작용을 위한 통합 프레임워크인 HAIC를 제시합니다. 핵심 기여는 고유수용성 히스토리만으로 고차 객체 상태(속도, 가속도)를 추정하는 동역학 예측기입니다. 이러한 예측은 정적 기하학적 사전 정보에 투영되어 공간적으로 기반한 동적 점유 맵을 형성하며, 이를 통해 정책이 사각지대에서 충돌 경계와 접촉 가능성을 추론할 수 있습니다. 우리는 비대칭 미세 조정을 사용하여 세계 모델이 학생 정책의 탐색에 지속적으로 적응하도록 하여 분포 변화 하에서도 강건한 상태 추정을 보장합니다. 휴머노이드 로봇 실험에서 HAIC는 관성 섭동을 능동적으로 보상함으로써 민첩한 작업(스케이트보드, 다양한 하중에서 카트 밀기/끌기)에서 높은 성공률을 달성하고, 여러 객체의 동역학을 예측하여 다양한 지형에서 상자를 운반하는 다중 객체 장기 작업도 마스터함을 보여줍니다.
