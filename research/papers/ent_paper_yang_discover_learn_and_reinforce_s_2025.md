---
$id: ent_paper_yang_discover_learn_and_reinforce_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories'
  zh: DLR
  ko: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories'
summary:
  en: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories (DLR),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science
    and Technology, Tsinghua University, Wuhan University, Central South University, Microsoft Research.'
  zh: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories (DLR),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science
    and Technology, Tsinghua University, Wuhan University, Central South University, Microsoft Research.'
  ko: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories (DLR),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science
    and Technology, Tsinghua University, Wuhan University, Central South University, Microsoft Research.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dlr
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19528v1.
sources:
- id: src_001
  type: paper
  title: 'Discover, Learn, and Reinforce: Scaling Vision-Language-Action Pretraining with Diverse RL-Generated Trajectories
    (arXiv)'
  url: https://arxiv.org/abs/2511.19528
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DLR source
  url: https://doi.org/10.48550/arXiv.2511.19528
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Scaling vision-language-action (VLA) model pre-training requires large volumes of diverse, high-quality manipulation trajectories. Most current data is obtained via human teleoperation, which is expensive and difficult to scale. Reinforcement learning (RL) methods learn useful skills through autonomous exploration, making them a viable approach for generating data. However, standard RL training collapses to a narrow execution pattern, limiting its utility for large-scale pre-training. We propose Discover, Lea rn and Reinforce (DLR), an information-theoretic pattern discovery framework that generates multiple distinct, high-success behavioral patterns for VLA pretraining. Empirically, DLR generates a markedly more diverse trajectory corpus on LIBERO. Specifically, it learns multiple distinct, high-success strategies for the same task where standard RL discovers only one, and hence it covers substantially broader regions of the state-action space. When adapted to unseen downstream task suites, VLA models pretrained on our diverse RL data surpass counterparts trained on equal-sized standard RL datasets. Moreover, DLR exhibits positive data-scaling behavior that single-pattern RL lacks. These results position multi-pattern RL as a practical, scalable data engine for embodied foundation models.

## 核心内容
Scaling vision-language-action (VLA) model pre-training requires large volumes of diverse, high-quality manipulation trajectories. Most current data is obtained via human teleoperation, which is expensive and difficult to scale. Reinforcement learning (RL) methods learn useful skills through autonomous exploration, making them a viable approach for generating data. However, standard RL training collapses to a narrow execution pattern, limiting its utility for large-scale pre-training. We propose Discover, Lea rn and Reinforce (DLR), an information-theoretic pattern discovery framework that generates multiple distinct, high-success behavioral patterns for VLA pretraining. Empirically, DLR generates a markedly more diverse trajectory corpus on LIBERO. Specifically, it learns multiple distinct, high-success strategies for the same task where standard RL discovers only one, and hence it covers substantially broader regions of the state-action space. When adapted to unseen downstream task suites, VLA models pretrained on our diverse RL data surpass counterparts trained on equal-sized standard RL datasets. Moreover, DLR exhibits positive data-scaling behavior that single-pattern RL lacks. These results position multi-pattern RL as a practical, scalable data engine for embodied foundation models.

## 参考
- http://arxiv.org/abs/2511.19528v1

## Overview
Scaling vision-language-action (VLA) model pre-training requires large volumes of diverse, high-quality manipulation trajectories. Most current data is obtained via human teleoperation, which is expensive and difficult to scale. Reinforcement learning (RL) methods learn useful skills through autonomous exploration, making them a viable approach for generating data. However, standard RL training collapses to a narrow execution pattern, limiting its utility for large-scale pre-training. We propose Discover, Learn and Reinforce (DLR), an information-theoretic pattern discovery framework that generates multiple distinct, high-success behavioral patterns for VLA pretraining. Empirically, DLR generates a markedly more diverse trajectory corpus on LIBERO. Specifically, it learns multiple distinct, high-success strategies for the same task where standard RL discovers only one, and hence it covers substantially broader regions of the state-action space. When adapted to unseen downstream task suites, VLA models pretrained on our diverse RL data surpass counterparts trained on equal-sized standard RL datasets. Moreover, DLR exhibits positive data-scaling behavior that single-pattern RL lacks. These results position multi-pattern RL as a practical, scalable data engine for embodied foundation models.

## Content
Scaling vision-language-action (VLA) model pre-training requires large volumes of diverse, high-quality manipulation trajectories. Most current data is obtained via human teleoperation, which is expensive and difficult to scale. Reinforcement learning (RL) methods learn useful skills through autonomous exploration, making them a viable approach for generating data. However, standard RL training collapses to a narrow execution pattern, limiting its utility for large-scale pre-training. We propose Discover, Learn and Reinforce (DLR), an information-theoretic pattern discovery framework that generates multiple distinct, high-success behavioral patterns for VLA pretraining. Empirically, DLR generates a markedly more diverse trajectory corpus on LIBERO. Specifically, it learns multiple distinct, high-success strategies for the same task where standard RL discovers only one, and hence it covers substantially broader regions of the state-action space. When adapted to unseen downstream task suites, VLA models pretrained on our diverse RL data surpass counterparts trained on equal-sized standard RL datasets. Moreover, DLR exhibits positive data-scaling behavior that single-pattern RL lacks. These results position multi-pattern RL as a practical, scalable data engine for embodied foundation models.

## 개요
비전-언어-행동(VLA) 모델 사전 학습을 확장하려면 다양하고 고품질의 조작 궤적 데이터가 대량으로 필요합니다. 현재 대부분의 데이터는 인간 원격 조작을 통해 얻어지며, 이는 비용이 많이 들고 확장이 어렵습니다. 강화 학습(RL) 방법은 자율 탐색을 통해 유용한 기술을 학습하므로 데이터 생성에 실용적인 접근 방식이 될 수 있습니다. 그러나 표준 RL 훈련은 좁은 실행 패턴으로 수렴되어 대규모 사전 학습에 유용성이 제한됩니다. 본 연구에서는 VLA 사전 학습을 위해 여러 개의 뚜렷하고 성공률이 높은 행동 패턴을 생성하는 정보 이론 기반 패턴 발견 프레임워크인 Discover, Learn and Reinforce(DLR)를 제안합니다. 실험적으로 DLR은 LIBERO에서 현저히 더 다양한 궤적 코퍼스를 생성합니다. 구체적으로, 표준 RL이 하나만 발견하는 동일한 작업에 대해 여러 개의 뚜렷하고 성공률이 높은 전략을 학습하여 상태-행동 공간의 훨씬 더 넓은 영역을 포괄합니다. 보지 못한 하위 작업 집합에 적용할 때, 다양한 RL 데이터로 사전 학습된 VLA 모델은 동일한 크기의 표준 RL 데이터셋으로 훈련된 모델보다 성능이 뛰어납니다. 또한 DLR은 단일 패턴 RL이 결여된 긍정적 데이터 확장 행동을 보여줍니다. 이러한 결과는 다중 패턴 RL을 체화된 기초 모델을 위한 실용적이고 확장 가능한 데이터 엔진으로 자리매김합니다.

## 핵심 내용
비전-언어-행동(VLA) 모델 사전 학습을 확장하려면 다양하고 고품질의 조작 궤적 데이터가 대량으로 필요합니다. 현재 대부분의 데이터는 인간 원격 조작을 통해 얻어지며, 이는 비용이 많이 들고 확장이 어렵습니다. 강화 학습(RL) 방법은 자율 탐색을 통해 유용한 기술을 학습하므로 데이터 생성에 실용적인 접근 방식이 될 수 있습니다. 그러나 표준 RL 훈련은 좁은 실행 패턴으로 수렴되어 대규모 사전 학습에 유용성이 제한됩니다. 본 연구에서는 VLA 사전 학습을 위해 여러 개의 뚜렷하고 성공률이 높은 행동 패턴을 생성하는 정보 이론 기반 패턴 발견 프레임워크인 Discover, Learn and Reinforce(DLR)를 제안합니다. 실험적으로 DLR은 LIBERO에서 현저히 더 다양한 궤적 코퍼스를 생성합니다. 구체적으로, 표준 RL이 하나만 발견하는 동일한 작업에 대해 여러 개의 뚜렷하고 성공률이 높은 전략을 학습하여 상태-행동 공간의 훨씬 더 넓은 영역을 포괄합니다. 보지 못한 하위 작업 집합에 적용할 때, 다양한 RL 데이터로 사전 학습된 VLA 모델은 동일한 크기의 표준 RL 데이터셋으로 훈련된 모델보다 성능이 뛰어납니다. 또한 DLR은 단일 패턴 RL이 결여된 긍정적 데이터 확장 행동을 보여줍니다. 이러한 결과는 다중 패턴 RL을 체화된 기초 모델을 위한 실용적이고 확장 가능한 데이터 엔진으로 자리매김합니다.
