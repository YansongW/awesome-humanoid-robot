---
$id: ent_paper_jabbour_dont_run_with_scissors_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dont Run with Scissors
  zh: GLUESTICK
  ko: Dont Run with Scissors
summary:
  en: Dont Run with Scissors (GLUESTICK), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by FieldAI, Harvard University.
  zh: Dont Run with Scissors (GLUESTICK), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by FieldAI, Harvard University.
  ko: Dont Run with Scissors (GLUESTICK), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by FieldAI, Harvard University.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gluestick
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.08464v1.
sources:
- id: src_001
  type: paper
  title: Dont Run with Scissors (arXiv)
  url: https://arxiv.org/abs/2510.08464
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have advanced robotic capabilities but remain challenging to deploy on resource-limited hardware. Pruning has enabled efficient compression of large language models (LLMs), yet it is largely understudied in robotics. Surprisingly, we observe that pruning VLA models leads to drastic degradation and increased safety violations. We introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits. Our method performs a one-time interpolation between the dense and pruned models in weight-space to compute a corrective term. This correction is used during inference by each pruned layer to recover lost capabilities with minimal overhead. GLUESTICK requires no additional training, is agnostic to the pruning algorithm, and introduces a single hyperparameter that controls the tradeoff between efficiency and accuracy. Across diverse VLA architectures and tasks in manipulation and navigation, GLUESTICK achieves competitive memory efficiency while substantially recovering success rates and reducing safety violations. Additional material can be found at: https://gluestick-vla.github.io/.

## 核心内容
Vision-Language-Action (VLA) models have advanced robotic capabilities but remain challenging to deploy on resource-limited hardware. Pruning has enabled efficient compression of large language models (LLMs), yet it is largely understudied in robotics. Surprisingly, we observe that pruning VLA models leads to drastic degradation and increased safety violations. We introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits. Our method performs a one-time interpolation between the dense and pruned models in weight-space to compute a corrective term. This correction is used during inference by each pruned layer to recover lost capabilities with minimal overhead. GLUESTICK requires no additional training, is agnostic to the pruning algorithm, and introduces a single hyperparameter that controls the tradeoff between efficiency and accuracy. Across diverse VLA architectures and tasks in manipulation and navigation, GLUESTICK achieves competitive memory efficiency while substantially recovering success rates and reducing safety violations. Additional material can be found at: https://gluestick-vla.github.io/.

## 参考
- http://arxiv.org/abs/2510.08464v1

## Overview
Vision-Language-Action (VLA) models have advanced robotic capabilities but remain challenging to deploy on resource-limited hardware. Pruning has enabled efficient compression of large language models (LLMs), yet it is largely understudied in robotics. Surprisingly, we observe that pruning VLA models leads to drastic degradation and increased safety violations. We introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits. Our method performs a one-time interpolation between the dense and pruned models in weight-space to compute a corrective term. This correction is used during inference by each pruned layer to recover lost capabilities with minimal overhead. GLUESTICK requires no additional training, is agnostic to the pruning algorithm, and introduces a single hyperparameter that controls the tradeoff between efficiency and accuracy. Across diverse VLA architectures and tasks in manipulation and navigation, GLUESTICK achieves competitive memory efficiency while substantially recovering success rates and reducing safety violations. Additional material can be found at: https://gluestick-vla.github.io/.

## Content
Vision-Language-Action (VLA) models have advanced robotic capabilities but remain challenging to deploy on resource-limited hardware. Pruning has enabled efficient compression of large language models (LLMs), yet it is largely understudied in robotics. Surprisingly, we observe that pruning VLA models leads to drastic degradation and increased safety violations. We introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits. Our method performs a one-time interpolation between the dense and pruned models in weight-space to compute a corrective term. This correction is used during inference by each pruned layer to recover lost capabilities with minimal overhead. GLUESTICK requires no additional training, is agnostic to the pruning algorithm, and introduces a single hyperparameter that controls the tradeoff between efficiency and accuracy. Across diverse VLA architectures and tasks in manipulation and navigation, GLUESTICK achieves competitive memory efficiency while substantially recovering success rates and reducing safety violations. Additional material can be found at: https://gluestick-vla.github.io/.

## 개요
Vision-Language-Action (VLA) 모델은 로봇의 성능을 향상시켰지만, 자원이 제한된 하드웨어에 배포하는 것은 여전히 어려운 과제입니다. Pruning(가지치기)은 대규모 언어 모델(LLM)의 효율적인 압축을 가능하게 했지만, 로봇 공학 분야에서는 거의 연구되지 않았습니다. 놀랍게도, VLA 모델을 가지치기하면 성능이 급격히 저하되고 안전 위반이 증가하는 것을 관찰했습니다. 우리는 GLUESTICK을 소개합니다. 이는 가지치기 후 복구 방법으로, 희소성(sparsity)의 이점을 유지하면서 원래 모델의 기능 대부분을 복원합니다. 이 방법은 밀집(dense) 모델과 가지치기된 모델 간의 가중치 공간에서 일회성 보간(interpolation)을 수행하여 보정 항(corrective term)을 계산합니다. 이 보정은 추론 중 각 가지치기된 레이어에서 최소한의 오버헤드로 손실된 기능을 복구하는 데 사용됩니다. GLUESTICK은 추가 학습이 필요 없고, 가지치기 알고리즘에 구애받지 않으며, 효율성과 정확성 간의 균형을 제어하는 단일 하이퍼파라미터를 도입합니다. 조작 및 탐색 작업에서 다양한 VLA 아키텍처와 작업에 걸쳐 GLUESTICK은 경쟁력 있는 메모리 효율성을 달성하면서 성공률을 크게 회복하고 안전 위반을 줄입니다. 추가 자료는 https://gluestick-vla.github.io/에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇의 성능을 향상시켰지만, 자원이 제한된 하드웨어에 배포하는 것은 여전히 어려운 과제입니다. Pruning(가지치기)은 대규모 언어 모델(LLM)의 효율적인 압축을 가능하게 했지만, 로봇 공학 분야에서는 거의 연구되지 않았습니다. 놀랍게도, VLA 모델을 가지치기하면 성능이 급격히 저하되고 안전 위반이 증가하는 것을 관찰했습니다. 우리는 GLUESTICK을 소개합니다. 이는 가지치기 후 복구 방법으로, 희소성(sparsity)의 이점을 유지하면서 원래 모델의 기능 대부분을 복원합니다. 이 방법은 밀집(dense) 모델과 가지치기된 모델 간의 가중치 공간에서 일회성 보간(interpolation)을 수행하여 보정 항(corrective term)을 계산합니다. 이 보정은 추론 중 각 가지치기된 레이어에서 최소한의 오버헤드로 손실된 기능을 복구하는 데 사용됩니다. GLUESTICK은 추가 학습이 필요 없고, 가지치기 알고리즘에 구애받지 않으며, 효율성과 정확성 간의 균형을 제어하는 단일 하이퍼파라미터를 도입합니다. 조작 및 탐색 작업에서 다양한 VLA 아키텍처와 작업에 걸쳐 GLUESTICK은 경쟁력 있는 메모리 효율성을 달성하면서 성공률을 크게 회복하고 안전 위반을 줄입니다. 추가 자료는 https://gluestick-vla.github.io/에서 확인할 수 있습니다.
