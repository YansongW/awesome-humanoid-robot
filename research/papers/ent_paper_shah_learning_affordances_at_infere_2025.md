---
$id: ent_paper_shah_learning_affordances_at_infere_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Affordances at Inference-Time for Vision-Language-Action Models
  zh: LITEN
  ko: Learning Affordances at Inference-Time for Vision-Language-Action Models
summary:
  en: Learning Affordances at Inference-Time for Vision-Language-Action Models (LITEN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Physical Intelligence.
  zh: Learning Affordances at Inference-Time for Vision-Language-Action Models (LITEN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Physical Intelligence.
  ko: Learning Affordances at Inference-Time for Vision-Language-Action Models (LITEN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Physical Intelligence.
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
- liten
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.19752v1.
sources:
- id: src_001
  type: paper
  title: Learning Affordances at Inference-Time for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2510.19752
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LITEN source
  url: https://doi.org/10.48550/arXiv.2510.19752
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Solving complex real-world control tasks often takes multiple tries: if we fail at first, we reflect on what went wrong, and change our strategy accordingly to avoid making the same mistake. In robotics, Vision-Language-Action models (VLAs) offer a promising path towards solving complex control tasks, but lack the ability to contextually and dynamically readjust behavior when they fail to accomplish a task. In this work, we introduce Learning from Inference-Time Execution (LITEN), which connects a VLA low-level policy to a high-level VLM that conditions on past experiences by including them in-context, allowing it to learn the affordances and capabilities of the low-level VLA. Our approach iterates between a reasoning phase that generates and executes plans for the low-level VLA, and an assessment phase that reflects on the resulting execution and draws useful conclusions to be included in future reasoning contexts. Unlike similar approaches to self-refinement in non-robotics domains, LITEN must reflect on unstructured real-world robot trajectories (e.g., raw videos), which requires structured guiderails during assessment. Our experimental results demonstrate LITEN is able to effectively learn from past experience to generate plans that use high-affordance instructions to accomplish long-horizon tasks.

## 核心内容
Solving complex real-world control tasks often takes multiple tries: if we fail at first, we reflect on what went wrong, and change our strategy accordingly to avoid making the same mistake. In robotics, Vision-Language-Action models (VLAs) offer a promising path towards solving complex control tasks, but lack the ability to contextually and dynamically readjust behavior when they fail to accomplish a task. In this work, we introduce Learning from Inference-Time Execution (LITEN), which connects a VLA low-level policy to a high-level VLM that conditions on past experiences by including them in-context, allowing it to learn the affordances and capabilities of the low-level VLA. Our approach iterates between a reasoning phase that generates and executes plans for the low-level VLA, and an assessment phase that reflects on the resulting execution and draws useful conclusions to be included in future reasoning contexts. Unlike similar approaches to self-refinement in non-robotics domains, LITEN must reflect on unstructured real-world robot trajectories (e.g., raw videos), which requires structured guiderails during assessment. Our experimental results demonstrate LITEN is able to effectively learn from past experience to generate plans that use high-affordance instructions to accomplish long-horizon tasks.

## 参考
- http://arxiv.org/abs/2510.19752v1

## Overview
Solving complex real-world control tasks often takes multiple tries: if we fail at first, we reflect on what went wrong, and change our strategy accordingly to avoid making the same mistake. In robotics, Vision-Language-Action models (VLAs) offer a promising path towards solving complex control tasks, but lack the ability to contextually and dynamically readjust behavior when they fail to accomplish a task. In this work, we introduce Learning from Inference-Time Execution (LITEN), which connects a VLA low-level policy to a high-level VLM that conditions on past experiences by including them in-context, allowing it to learn the affordances and capabilities of the low-level VLA. Our approach iterates between a reasoning phase that generates and executes plans for the low-level VLA, and an assessment phase that reflects on the resulting execution and draws useful conclusions to be included in future reasoning contexts. Unlike similar approaches to self-refinement in non-robotics domains, LITEN must reflect on unstructured real-world robot trajectories (e.g., raw videos), which requires structured guiderails during assessment. Our experimental results demonstrate LITEN is able to effectively learn from past experience to generate plans that use high-affordance instructions to accomplish long-horizon tasks.

## Content
Solving complex real-world control tasks often takes multiple tries: if we fail at first, we reflect on what went wrong, and change our strategy accordingly to avoid making the same mistake. In robotics, Vision-Language-Action models (VLAs) offer a promising path towards solving complex control tasks, but lack the ability to contextually and dynamically readjust behavior when they fail to accomplish a task. In this work, we introduce Learning from Inference-Time Execution (LITEN), which connects a VLA low-level policy to a high-level VLM that conditions on past experiences by including them in-context, allowing it to learn the affordances and capabilities of the low-level VLA. Our approach iterates between a reasoning phase that generates and executes plans for the low-level VLA, and an assessment phase that reflects on the resulting execution and draws useful conclusions to be included in future reasoning contexts. Unlike similar approaches to self-refinement in non-robotics domains, LITEN must reflect on unstructured real-world robot trajectories (e.g., raw videos), which requires structured guiderails during assessment. Our experimental results demonstrate LITEN is able to effectively learn from past experience to generate plans that use high-affordance instructions to accomplish long-horizon tasks.

## 개요
복잡한 실제 제어 작업을 해결하려면 여러 번의 시도가 필요한 경우가 많습니다. 처음에 실패하면 무엇이 잘못되었는지 반성하고, 같은 실수를 반복하지 않도록 전략을 변경합니다. 로봇 공학에서 VLA(Vision-Language-Action) 모델은 복잡한 제어 작업을 해결하는 유망한 경로를 제공하지만, 작업을 완료하지 못했을 때 상황에 맞게 동적으로 행동을 재조정하는 능력이 부족합니다. 본 연구에서는 LITEN(Learning from Inference-Time Execution)을 소개합니다. 이는 VLA 저수준 정책을 고수준 VLM과 연결하며, 과거 경험을 맥락에 포함시켜 조건화함으로써 저수준 VLA의 어포던스와 능력을 학습할 수 있게 합니다. 우리의 접근 방식은 저수준 VLA를 위한 계획을 생성하고 실행하는 추론 단계와, 결과 실행을 반성하고 향후 추론 맥락에 포함될 유용한 결론을 도출하는 평가 단계를 반복합니다. 비로봇 공학 분야의 유사한 자기 개선 접근 방식과 달리, LITEN은 구조화되지 않은 실제 로봇 궤적(예: 원시 비디오)을 반성해야 하며, 평가 중 구조화된 가이드레일이 필요합니다. 실험 결과는 LITEN이 과거 경험으로부터 효과적으로 학습하여 높은 어포던스 명령을 사용해 장기 작업을 완료하는 계획을 생성할 수 있음을 보여줍니다.

## 핵심 내용
복잡한 실제 제어 작업을 해결하려면 여러 번의 시도가 필요한 경우가 많습니다. 처음에 실패하면 무엇이 잘못되었는지 반성하고, 같은 실수를 반복하지 않도록 전략을 변경합니다. 로봇 공학에서 VLA(Vision-Language-Action) 모델은 복잡한 제어 작업을 해결하는 유망한 경로를 제공하지만, 작업을 완료하지 못했을 때 상황에 맞게 동적으로 행동을 재조정하는 능력이 부족합니다. 본 연구에서는 LITEN(Learning from Inference-Time Execution)을 소개합니다. 이는 VLA 저수준 정책을 고수준 VLM과 연결하며, 과거 경험을 맥락에 포함시켜 조건화함으로써 저수준 VLA의 어포던스와 능력을 학습할 수 있게 합니다. 우리의 접근 방식은 저수준 VLA를 위한 계획을 생성하고 실행하는 추론 단계와, 결과 실행을 반성하고 향후 추론 맥락에 포함될 유용한 결론을 도출하는 평가 단계를 반복합니다. 비로봇 공학 분야의 유사한 자기 개선 접근 방식과 달리, LITEN은 구조화되지 않은 실제 로봇 궤적(예: 원시 비디오)을 반성해야 하며, 평가 중 구조화된 가이드레일이 필요합니다. 실험 결과는 LITEN이 과거 경험으로부터 효과적으로 학습하여 높은 어포던스 명령을 사용해 장기 작업을 완료하는 계획을 생성할 수 있음을 보여줍니다.
