---
$id: ent_paper_zhang_grape_generalizing_robot_polic_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GRAPE: Generalizing Robot Policy via Preference Alignment'
  zh: GRAPE
  ko: 'GRAPE: Generalizing Robot Policy via Preference Alignment'
summary:
  en: 'GRAPE: Generalizing Robot Policy via Preference Alignment (GRAPE), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by University of Chicago.'
  zh: 'GRAPE: Generalizing Robot Policy via Preference Alignment (GRAPE), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by University of Chicago.'
  ko: 'GRAPE: Generalizing Robot Policy via Preference Alignment (GRAPE), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by University of Chicago.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- grape
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.19309v2.
sources:
- id: src_001
  type: paper
  title: 'GRAPE: Generalizing Robot Policy via Preference Alignment (arXiv)'
  url: https://arxiv.org/abs/2411.19309
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GRAPE source
  url: https://doi.org/10.48550/arXiv.2411.19309
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Despite the recent advancements of vision-language-action (VLA) models on a variety of robotics tasks, they suffer from critical issues such as poor generalizability to unseen tasks, due to their reliance on behavior cloning exclusively from successful rollouts. Furthermore, they are typically fine-tuned to replicate demonstrations collected by experts under different settings, thus introducing distribution bias and limiting their adaptability to diverse manipulation objectives, such as efficiency, safety, and task completion. To bridge this gap, we introduce GRAPE: Generalizing Robot Policy via Preference Alignment. Specifically, GRAPE aligns VLAs on a trajectory level and implicitly models reward from both successful and failure trials to boost generalizability to diverse tasks. Moreover, GRAPE breaks down complex manipulation tasks to independent stages and automatically guides preference modeling through customized spatiotemporal constraints with keypoints proposed by a large vision-language model. Notably, these constraints are flexible and can be customized to align the model with varying objectives, such as safety, efficiency, or task success. We evaluate GRAPE across a diverse array of tasks in both real-world and simulated environments. Experimental results demonstrate that GRAPE enhances the performance of state-of-the-art VLA models, increasing success rates on in-domain and unseen manipulation tasks by 51.79% and 58.20%, respectively. Additionally, GRAPE can be aligned with various objectives, such as safety and efficiency, reducing collision rates by 37.44% and rollout step-length by 11.15%, respectively. All code, models, and data are available at https://grape-vla.github.io/

## 核心内容
Despite the recent advancements of vision-language-action (VLA) models on a variety of robotics tasks, they suffer from critical issues such as poor generalizability to unseen tasks, due to their reliance on behavior cloning exclusively from successful rollouts. Furthermore, they are typically fine-tuned to replicate demonstrations collected by experts under different settings, thus introducing distribution bias and limiting their adaptability to diverse manipulation objectives, such as efficiency, safety, and task completion. To bridge this gap, we introduce GRAPE: Generalizing Robot Policy via Preference Alignment. Specifically, GRAPE aligns VLAs on a trajectory level and implicitly models reward from both successful and failure trials to boost generalizability to diverse tasks. Moreover, GRAPE breaks down complex manipulation tasks to independent stages and automatically guides preference modeling through customized spatiotemporal constraints with keypoints proposed by a large vision-language model. Notably, these constraints are flexible and can be customized to align the model with varying objectives, such as safety, efficiency, or task success. We evaluate GRAPE across a diverse array of tasks in both real-world and simulated environments. Experimental results demonstrate that GRAPE enhances the performance of state-of-the-art VLA models, increasing success rates on in-domain and unseen manipulation tasks by 51.79% and 58.20%, respectively. Additionally, GRAPE can be aligned with various objectives, such as safety and efficiency, reducing collision rates by 37.44% and rollout step-length by 11.15%, respectively. All code, models, and data are available at https://grape-vla.github.io/

## 参考
- http://arxiv.org/abs/2411.19309v2

## Overview
Despite the recent advancements of vision-language-action (VLA) models on a variety of robotics tasks, they suffer from critical issues such as poor generalizability to unseen tasks, due to their reliance on behavior cloning exclusively from successful rollouts. Furthermore, they are typically fine-tuned to replicate demonstrations collected by experts under different settings, thus introducing distribution bias and limiting their adaptability to diverse manipulation objectives, such as efficiency, safety, and task completion. To bridge this gap, we introduce GRAPE: Generalizing Robot Policy via Preference Alignment. Specifically, GRAPE aligns VLAs on a trajectory level and implicitly models reward from both successful and failure trials to boost generalizability to diverse tasks. Moreover, GRAPE breaks down complex manipulation tasks to independent stages and automatically guides preference modeling through customized spatiotemporal constraints with keypoints proposed by a large vision-language model. Notably, these constraints are flexible and can be customized to align the model with varying objectives, such as safety, efficiency, or task success. We evaluate GRAPE across a diverse array of tasks in both real-world and simulated environments. Experimental results demonstrate that GRAPE enhances the performance of state-of-the-art VLA models, increasing success rates on in-domain and unseen manipulation tasks by 51.79% and 58.20%, respectively. Additionally, GRAPE can be aligned with various objectives, such as safety and efficiency, reducing collision rates by 37.44% and rollout step-length by 11.15%, respectively. All code, models, and data are available at https://grape-vla.github.io/

## Content
Despite the recent advancements of vision-language-action (VLA) models on a variety of robotics tasks, they suffer from critical issues such as poor generalizability to unseen tasks, due to their reliance on behavior cloning exclusively from successful rollouts. Furthermore, they are typically fine-tuned to replicate demonstrations collected by experts under different settings, thus introducing distribution bias and limiting their adaptability to diverse manipulation objectives, such as efficiency, safety, and task completion. To bridge this gap, we introduce GRAPE: Generalizing Robot Policy via Preference Alignment. Specifically, GRAPE aligns VLAs on a trajectory level and implicitly models reward from both successful and failure trials to boost generalizability to diverse tasks. Moreover, GRAPE breaks down complex manipulation tasks to independent stages and automatically guides preference modeling through customized spatiotemporal constraints with keypoints proposed by a large vision-language model. Notably, these constraints are flexible and can be customized to align the model with varying objectives, such as safety, efficiency, or task success. We evaluate GRAPE across a diverse array of tasks in both real-world and simulated environments. Experimental results demonstrate that GRAPE enhances the performance of state-of-the-art VLA models, increasing success rates on in-domain and unseen manipulation tasks by 51.79% and 58.20%, respectively. Additionally, GRAPE can be aligned with various objectives, such as safety and efficiency, reducing collision rates by 37.44% and rollout step-length by 11.15%, respectively. All code, models, and data are available at https://grape-vla.github.io/

## 개요
최근 다양한 로봇 작업에서 시각-언어-행동(VLA) 모델의 발전이 이루어졌음에도 불구하고, 이들은 성공적인 롤아웃에서만 행동 복제에 의존하기 때문에 보지 못한 작업에 대한 일반화 능력이 부족하다는 심각한 문제를 겪고 있습니다. 또한, 일반적으로 다른 환경에서 전문가가 수집한 시연을 복제하도록 미세 조정되어 분포 편향을 초래하고 효율성, 안전성, 작업 완료와 같은 다양한 조작 목표에 대한 적응성을 제한합니다. 이러한 격차를 해소하기 위해 우리는 GRAPE: 선호도 정렬을 통한 로봇 정책 일반화를 소개합니다. 구체적으로, GRAPE는 궤적 수준에서 VLA를 정렬하고 성공 및 실패 시도 모두에서 보상을 암시적으로 모델링하여 다양한 작업에 대한 일반화 능력을 향상시킵니다. 또한, GRAPE는 복잡한 조작 작업을 독립적인 단계로 분해하고 대규모 시각-언어 모델이 제안한 키포인트를 사용자 정의 시공간 제약 조건을 통해 자동으로 선호도 모델링을 안내합니다. 특히, 이러한 제약 조건은 유연하며 안전성, 효율성 또는 작업 성공과 같은 다양한 목표에 맞게 모델을 정렬하도록 사용자 정의할 수 있습니다. 우리는 실제 환경과 시뮬레이션 환경 모두에서 다양한 작업에 걸쳐 GRAPE를 평가합니다. 실험 결과는 GRAPE가 최첨단 VLA 모델의 성능을 향상시켜 도메인 내 및 보지 못한 조작 작업에서 성공률을 각각 51.79% 및 58.20% 증가시킴을 보여줍니다. 또한, GRAPE는 안전성 및 효율성과 같은 다양한 목표에 정렬될 수 있어 충돌률을 37.44%, 롤아웃 단계 길이를 11.15% 각각 감소시킵니다. 모든 코드, 모델 및 데이터는 https://grape-vla.github.io/에서 확인할 수 있습니다.

## 핵심 내용
최근 다양한 로봇 작업에서 시각-언어-행동(VLA) 모델의 발전이 이루어졌음에도 불구하고, 이들은 성공적인 롤아웃에서만 행동 복제에 의존하기 때문에 보지 못한 작업에 대한 일반화 능력이 부족하다는 심각한 문제를 겪고 있습니다. 또한, 일반적으로 다른 환경에서 전문가가 수집한 시연을 복제하도록 미세 조정되어 분포 편향을 초래하고 효율성, 안전성, 작업 완료와 같은 다양한 조작 목표에 대한 적응성을 제한합니다. 이러한 격차를 해소하기 위해 우리는 GRAPE: 선호도 정렬을 통한 로봇 정책 일반화를 소개합니다. 구체적으로, GRAPE는 궤적 수준에서 VLA를 정렬하고 성공 및 실패 시도 모두에서 보상을 암시적으로 모델링하여 다양한 작업에 대한 일반화 능력을 향상시킵니다. 또한, GRAPE는 복잡한 조작 작업을 독립적인 단계로 분해하고 대규모 시각-언어 모델이 제안한 키포인트를 사용자 정의 시공간 제약 조건을 통해 자동으로 선호도 모델링을 안내합니다. 특히, 이러한 제약 조건은 유연하며 안전성, 효율성 또는 작업 성공과 같은 다양한 목표에 맞게 모델을 정렬하도록 사용자 정의할 수 있습니다. 우리는 실제 환경과 시뮬레이션 환경 모두에서 다양한 작업에 걸쳐 GRAPE를 평가합니다. 실험 결과는 GRAPE가 최첨단 VLA 모델의 성능을 향상시켜 도메인 내 및 보지 못한 조작 작업에서 성공률을 각각 51.79% 및 58.20% 증가시킴을 보여줍니다. 또한, GRAPE는 안전성 및 효율성과 같은 다양한 목표에 정렬될 수 있어 충돌률을 37.44%, 롤아웃 단계 길이를 11.15% 각각 감소시킵니다. 모든 코드, 모델 및 데이터는 https://grape-vla.github.io/에서 확인할 수 있습니다.
