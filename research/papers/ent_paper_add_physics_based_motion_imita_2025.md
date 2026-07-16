---
$id: ent_paper_add_physics_based_motion_imita_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators'
  zh: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators'
  ko: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators'
summary:
  en: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators is a 2025 work on physics-based character
    animation for humanoid robots.'
  zh: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators is a 2025 work on physics-based character
    animation for humanoid robots.'
  ko: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators is a 2025 work on physics-based character
    animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- add
- character_animation
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.04961v2.
sources:
- id: src_001
  type: paper
  title: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators (arXiv)'
  url: https://arxiv.org/abs/2505.04961v1
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Multi-objective optimization problems, which require the simultaneous optimization of multiple objectives, are prevalent across numerous applications. Existing multi-objective optimization methods often rely on manually-tuned aggregation functions to formulate a joint optimization objective. The performance of such hand-tuned methods is heavily dependent on careful weight selection, a time-consuming and laborious process. These limitations also arise in the setting of reinforcement-learning-based motion tracking methods for physically simulated characters, where intricately crafted reward functions are typically used to achieve high-fidelity results. Such solutions not only require domain expertise and significant manual tuning, but also limit the applicability of the resulting reward function across diverse skills. To bridge this gap, we present a novel adversarial multi-objective optimization technique that is broadly applicable to a range of multi-objective reinforcement-learning tasks, including motion tracking. Our proposed Adversarial Differential Discriminator (ADD) receives a single positive sample, yet is still effective at guiding the optimization process. We demonstrate that our technique can enable characters to closely replicate a variety of acrobatic and agile behaviors, achieving comparable quality to state-of-the-art motion-tracking methods, without relying on manually-designed reward functions. Code and results are available at https://add-moo.github.io/.

## 核心内容
Multi-objective optimization problems, which require the simultaneous optimization of multiple objectives, are prevalent across numerous applications. Existing multi-objective optimization methods often rely on manually-tuned aggregation functions to formulate a joint optimization objective. The performance of such hand-tuned methods is heavily dependent on careful weight selection, a time-consuming and laborious process. These limitations also arise in the setting of reinforcement-learning-based motion tracking methods for physically simulated characters, where intricately crafted reward functions are typically used to achieve high-fidelity results. Such solutions not only require domain expertise and significant manual tuning, but also limit the applicability of the resulting reward function across diverse skills. To bridge this gap, we present a novel adversarial multi-objective optimization technique that is broadly applicable to a range of multi-objective reinforcement-learning tasks, including motion tracking. Our proposed Adversarial Differential Discriminator (ADD) receives a single positive sample, yet is still effective at guiding the optimization process. We demonstrate that our technique can enable characters to closely replicate a variety of acrobatic and agile behaviors, achieving comparable quality to state-of-the-art motion-tracking methods, without relying on manually-designed reward functions. Code and results are available at https://add-moo.github.io/.

## 参考
- http://arxiv.org/abs/2505.04961v2

## Overview
Multi-objective optimization problems, which require the simultaneous optimization of multiple objectives, are prevalent across numerous applications. Existing multi-objective optimization methods often rely on manually-tuned aggregation functions to formulate a joint optimization objective. The performance of such hand-tuned methods is heavily dependent on careful weight selection, a time-consuming and laborious process. These limitations also arise in the setting of reinforcement-learning-based motion tracking methods for physically simulated characters, where intricately crafted reward functions are typically used to achieve high-fidelity results. Such solutions not only require domain expertise and significant manual tuning, but also limit the applicability of the resulting reward function across diverse skills. To bridge this gap, we present a novel adversarial multi-objective optimization technique that is broadly applicable to a range of multi-objective reinforcement-learning tasks, including motion tracking. Our proposed Adversarial Differential Discriminator (ADD) receives a single positive sample, yet is still effective at guiding the optimization process. We demonstrate that our technique can enable characters to closely replicate a variety of acrobatic and agile behaviors, achieving comparable quality to state-of-the-art motion-tracking methods, without relying on manually-designed reward functions. Code and results are available at https://add-moo.github.io/.

## Content
Multi-objective optimization problems, which require the simultaneous optimization of multiple objectives, are prevalent across numerous applications. Existing multi-objective optimization methods often rely on manually-tuned aggregation functions to formulate a joint optimization objective. The performance of such hand-tuned methods is heavily dependent on careful weight selection, a time-consuming and laborious process. These limitations also arise in the setting of reinforcement-learning-based motion tracking methods for physically simulated characters, where intricately crafted reward functions are typically used to achieve high-fidelity results. Such solutions not only require domain expertise and significant manual tuning, but also limit the applicability of the resulting reward function across diverse skills. To bridge this gap, we present a novel adversarial multi-objective optimization technique that is broadly applicable to a range of multi-objective reinforcement-learning tasks, including motion tracking. Our proposed Adversarial Differential Discriminator (ADD) receives a single positive sample, yet is still effective at guiding the optimization process. We demonstrate that our technique can enable characters to closely replicate a variety of acrobatic and agile behaviors, achieving comparable quality to state-of-the-art motion-tracking methods, without relying on manually-designed reward functions. Code and results are available at https://add-moo.github.io/.

## 개요
다중 목표 최적화 문제는 여러 목표를 동시에 최적화해야 하며, 다양한 응용 분야에서 널리 발생합니다. 기존의 다중 목표 최적화 방법은 종종 수동으로 조정된 집계 함수를 사용하여 공동 최적화 목표를 구성합니다. 이러한 수동 조정 방법의 성능은 시간이 많이 소요되고 노동 집약적인 과정인 신중한 가중치 선택에 크게 의존합니다. 이러한 한계는 물리적으로 시뮬레이션된 캐릭터를 위한 강화 학습 기반 모션 추적 방법에서도 발생하며, 일반적으로 정교하게 설계된 보상 함수를 사용하여 높은 충실도의 결과를 얻습니다. 이러한 솔루션은 도메인 전문 지식과 상당한 수동 조정이 필요할 뿐만 아니라, 결과 보상 함수의 다양한 기술에 대한 적용 가능성을 제한합니다. 이러한 격차를 해소하기 위해, 우리는 모션 추적을 포함한 다양한 다중 목표 강화 학습 작업에 광범위하게 적용 가능한 새로운 적대적 다중 목표 최적화 기술을 제시합니다. 제안된 Adversarial Differential Discriminator (ADD)는 단일 양성 샘플을 받지만, 최적화 과정을 안내하는 데 여전히 효과적입니다. 우리의 기술을 통해 캐릭터가 다양한 곡예 및 민첩한 행동을 밀접하게 재현할 수 있으며, 수동으로 설계된 보상 함수에 의존하지 않고 최첨단 모션 추적 방법과 비교할 수 있는 품질을 달성할 수 있음을 입증합니다. 코드와 결과는 https://add-moo.github.io/에서 확인할 수 있습니다.

## 핵심 내용
다중 목표 최적화 문제는 여러 목표를 동시에 최적화해야 하며, 다양한 응용 분야에서 널리 발생합니다. 기존의 다중 목표 최적화 방법은 종종 수동으로 조정된 집계 함수를 사용하여 공동 최적화 목표를 구성합니다. 이러한 수동 조정 방법의 성능은 시간이 많이 소요되고 노동 집약적인 과정인 신중한 가중치 선택에 크게 의존합니다. 이러한 한계는 물리적으로 시뮬레이션된 캐릭터를 위한 강화 학습 기반 모션 추적 방법에서도 발생하며, 일반적으로 정교하게 설계된 보상 함수를 사용하여 높은 충실도의 결과를 얻습니다. 이러한 솔루션은 도메인 전문 지식과 상당한 수동 조정이 필요할 뿐만 아니라, 결과 보상 함수의 다양한 기술에 대한 적용 가능성을 제한합니다. 이러한 격차를 해소하기 위해, 우리는 모션 추적을 포함한 다양한 다중 목표 강화 학습 작업에 광범위하게 적용 가능한 새로운 적대적 다중 목표 최적화 기술을 제시합니다. 제안된 Adversarial Differential Discriminator (ADD)는 단일 양성 샘플을 받지만, 최적화 과정을 안내하는 데 여전히 효과적입니다. 우리의 기술을 통해 캐릭터가 다양한 곡예 및 민첩한 행동을 밀접하게 재현할 수 있으며, 수동으로 설계된 보상 함수에 의존하지 않고 최첨단 모션 추적 방법과 비교할 수 있는 품질을 달성할 수 있음을 입증합니다. 코드와 결과는 https://add-moo.github.io/에서 확인할 수 있습니다.
