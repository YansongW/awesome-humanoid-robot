---
$id: ent_paper_sridhar_ricl_adding_in_context_adaptab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models'
  zh: RICL
  ko: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models'
summary:
  en: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (RICL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pennsylvania, and published at CoRL25.'
  zh: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (RICL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pennsylvania, and published at CoRL25.'
  ko: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (RICL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pennsylvania, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- ricl
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.02062v1.
sources:
- id: src_001
  type: paper
  title: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2508.02062
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RICL source
  url: https://doi.org/10.48550/arXiv.2508.02062
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Multi-task ``vision-language-action'' (VLA) models have recently demonstrated increasing promise as generalist foundation models for robotics, achieving non-trivial performance out of the box on new tasks in new environments. However, for such models to be truly useful, an end user must have easy means to teach them to improve. For language and vision models, the emergent ability to perform in-context learning (ICL) has proven to be a versatile and highly useful interface to easily teach new tasks with no parameter finetuning. Unfortunately, VLAs pre-trained with imitation learning objectives do not naturally acquire ICL abilities. In this paper, we demonstrate that, with the right finetuning recipe and a small robot demonstration dataset, it is possible to inject in-context adaptability post hoc into such a VLA. After retraining for in-context learning (RICL), our system permits an end user to provide a small number (10-20) of demonstrations for a new task. RICL then fetches the most relevant portions of those demonstrations into the VLA context to exploit ICL, performing the new task and boosting task performance. We apply RICL to inject ICL into the $π_{0}$-FAST VLA, and show that it permits large in-context improvements for a variety of new manipulation tasks with only 20 demonstrations per task, without any parameter updates. When parameter updates on the target task demonstrations is possible, RICL finetuning further boosts performance. We release code and model weights for RICL-$π_{0}$-FAST alongside the paper to enable, for the first time, a simple in-context learning interface for new manipulation tasks. Website: https://ricl-vla.github.io.

## 核心内容
Multi-task ``vision-language-action'' (VLA) models have recently demonstrated increasing promise as generalist foundation models for robotics, achieving non-trivial performance out of the box on new tasks in new environments. However, for such models to be truly useful, an end user must have easy means to teach them to improve. For language and vision models, the emergent ability to perform in-context learning (ICL) has proven to be a versatile and highly useful interface to easily teach new tasks with no parameter finetuning. Unfortunately, VLAs pre-trained with imitation learning objectives do not naturally acquire ICL abilities. In this paper, we demonstrate that, with the right finetuning recipe and a small robot demonstration dataset, it is possible to inject in-context adaptability post hoc into such a VLA. After retraining for in-context learning (RICL), our system permits an end user to provide a small number (10-20) of demonstrations for a new task. RICL then fetches the most relevant portions of those demonstrations into the VLA context to exploit ICL, performing the new task and boosting task performance. We apply RICL to inject ICL into the $π_{0}$-FAST VLA, and show that it permits large in-context improvements for a variety of new manipulation tasks with only 20 demonstrations per task, without any parameter updates. When parameter updates on the target task demonstrations is possible, RICL finetuning further boosts performance. We release code and model weights for RICL-$π_{0}$-FAST alongside the paper to enable, for the first time, a simple in-context learning interface for new manipulation tasks. Website: https://ricl-vla.github.io.

## 参考
- http://arxiv.org/abs/2508.02062v1

## Overview
Multi-task ``vision-language-action'' (VLA) models have recently demonstrated increasing promise as generalist foundation models for robotics, achieving non-trivial performance out of the box on new tasks in new environments. However, for such models to be truly useful, an end user must have easy means to teach them to improve. For language and vision models, the emergent ability to perform in-context learning (ICL) has proven to be a versatile and highly useful interface to easily teach new tasks with no parameter finetuning. Unfortunately, VLAs pre-trained with imitation learning objectives do not naturally acquire ICL abilities. In this paper, we demonstrate that, with the right finetuning recipe and a small robot demonstration dataset, it is possible to inject in-context adaptability post hoc into such a VLA. After retraining for in-context learning (RICL), our system permits an end user to provide a small number (10-20) of demonstrations for a new task. RICL then fetches the most relevant portions of those demonstrations into the VLA context to exploit ICL, performing the new task and boosting task performance. We apply RICL to inject ICL into the $π_{0}$-FAST VLA, and show that it permits large in-context improvements for a variety of new manipulation tasks with only 20 demonstrations per task, without any parameter updates. When parameter updates on the target task demonstrations is possible, RICL finetuning further boosts performance. We release code and model weights for RICL-$π_{0}$-FAST alongside the paper to enable, for the first time, a simple in-context learning interface for new manipulation tasks. Website: https://ricl-vla.github.io.

## Content
Multi-task ``vision-language-action'' (VLA) models have recently demonstrated increasing promise as generalist foundation models for robotics, achieving non-trivial performance out of the box on new tasks in new environments. However, for such models to be truly useful, an end user must have easy means to teach them to improve. For language and vision models, the emergent ability to perform in-context learning (ICL) has proven to be a versatile and highly useful interface to easily teach new tasks with no parameter finetuning. Unfortunately, VLAs pre-trained with imitation learning objectives do not naturally acquire ICL abilities. In this paper, we demonstrate that, with the right finetuning recipe and a small robot demonstration dataset, it is possible to inject in-context adaptability post hoc into such a VLA. After retraining for in-context learning (RICL), our system permits an end user to provide a small number (10-20) of demonstrations for a new task. RICL then fetches the most relevant portions of those demonstrations into the VLA context to exploit ICL, performing the new task and boosting task performance. We apply RICL to inject ICL into the $π_{0}$-FAST VLA, and show that it permits large in-context improvements for a variety of new manipulation tasks with only 20 demonstrations per task, without any parameter updates. When parameter updates on the target task demonstrations is possible, RICL finetuning further boosts performance. We release code and model weights for RICL-$π_{0}$-FAST alongside the paper to enable, for the first time, a simple in-context learning interface for new manipulation tasks. Website: https://ricl-vla.github.io.

## 개요
멀티태스크 '비전-언어-행동'(VLA) 모델은 최근 로봇 공학을 위한 범용 기반 모델로서 점점 더 유망함을 보여주며, 새로운 환경에서 새로운 작업에 대해 즉시 상당한 성능을 달성하고 있습니다. 그러나 이러한 모델이 진정으로 유용하려면 최종 사용자가 쉽게 개선할 수 있는 방법을 갖추어야 합니다. 언어 및 비전 모델의 경우, 문맥 내 학습(ICL) 능력이 등장하여 매개변수 미세 조정 없이도 새로운 작업을 쉽게 가르칠 수 있는 다재다능하고 매우 유용한 인터페이스로 입증되었습니다. 불행히도, 모방 학습 목표로 사전 훈련된 VLA는 자연스럽게 ICL 능력을 획득하지 못합니다. 본 논문에서는 올바른 미세 조정 방법과 소규모 로봇 시연 데이터셋을 사용하여 사후에 이러한 VLA에 문맥 내 적응성을 주입할 수 있음을 보여줍니다. 문맥 내 학습을 위한 재훈련(RICL) 후, 우리 시스템은 최종 사용자가 새로운 작업에 대해 소량(10-20개)의 시연을 제공할 수 있게 합니다. 그런 다음 RICL은 해당 시연의 가장 관련성 높은 부분을 VLA 문맥으로 가져와 ICL을 활용하여 새로운 작업을 수행하고 작업 성능을 향상시킵니다. 우리는 RICL을 적용하여 $π_{0}$-FAST VLA에 ICL을 주입했으며, 매개변수 업데이트 없이 작업당 20개의 시연만으로 다양한 새로운 조작 작업에서 큰 문맥 내 개선이 가능함을 보여줍니다. 대상 작업 시연에 대한 매개변수 업데이트가 가능한 경우, RICL 미세 조정은 성능을 더욱 향상시킵니다. 우리는 논문과 함께 RICL-$π_{0}$-FAST의 코드와 모델 가중치를 공개하여, 처음으로 새로운 조작 작업을 위한 간단한 문맥 내 학습 인터페이스를 제공합니다. 웹사이트: https://ricl-vla.github.io.

## 핵심 내용
멀티태스크 '비전-언어-행동'(VLA) 모델은 최근 로봇 공학을 위한 범용 기반 모델로서 점점 더 유망함을 보여주며, 새로운 환경에서 새로운 작업에 대해 즉시 상당한 성능을 달성하고 있습니다. 그러나 이러한 모델이 진정으로 유용하려면 최종 사용자가 쉽게 개선할 수 있는 방법을 갖추어야 합니다. 언어 및 비전 모델의 경우, 문맥 내 학습(ICL) 능력이 등장하여 매개변수 미세 조정 없이도 새로운 작업을 쉽게 가르칠 수 있는 다재다능하고 매우 유용한 인터페이스로 입증되었습니다. 불행히도, 모방 학습 목표로 사전 훈련된 VLA는 자연스럽게 ICL 능력을 획득하지 못합니다. 본 논문에서는 올바른 미세 조정 방법과 소규모 로봇 시연 데이터셋을 사용하여 사후에 이러한 VLA에 문맥 내 적응성을 주입할 수 있음을 보여줍니다. 문맥 내 학습을 위한 재훈련(RICL) 후, 우리 시스템은 최종 사용자가 새로운 작업에 대해 소량(10-20개)의 시연을 제공할 수 있게 합니다. 그런 다음 RICL은 해당 시연의 가장 관련성 높은 부분을 VLA 문맥으로 가져와 ICL을 활용하여 새로운 작업을 수행하고 작업 성능을 향상시킵니다. 우리는 RICL을 적용하여 $π_{0}$-FAST VLA에 ICL을 주입했으며, 매개변수 업데이트 없이 작업당 20개의 시연만으로 다양한 새로운 조작 작업에서 큰 문맥 내 개선이 가능함을 보여줍니다. 대상 작업 시연에 대한 매개변수 업데이트가 가능한 경우, RICL 미세 조정은 성능을 더욱 향상시킵니다. 우리는 논문과 함께 RICL-$π_{0}$-FAST의 코드와 모델 가중치를 공개하여, 처음으로 새로운 조작 작업을 위한 간단한 문맥 내 학습 인터페이스를 제공합니다. 웹사이트: https://ricl-vla.github.io.
