---
$id: ent_paper_zheng_leveraging_os_level_primitives_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Leveraging OS-Level Primitives for Robotic Action Management
  zh: AMS
  ko: Leveraging OS-Level Primitives for Robotic Action Management
summary:
  en: Leveraging OS-Level Primitives for Robotic Action Management (AMS), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai Jiao Tong University, Southern University of Science and Technology.
  zh: Leveraging OS-Level Primitives for Robotic Action Management (AMS), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai Jiao Tong University, Southern University of Science and Technology.
  ko: Leveraging OS-Level Primitives for Robotic Action Management (AMS), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai Jiao Tong University, Southern University of Science and Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ams
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.10259v1.
sources:
- id: src_001
  type: paper
  title: Leveraging OS-Level Primitives for Robotic Action Management (arXiv)
  url: https://arxiv.org/abs/2508.10259
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AMS source
  url: https://doi.org/10.48550/arXiv.2508.10259
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
End-to-end imitation learning frameworks (e.g., VLA) are increasingly prominent in robotics, as they enable rapid task transfer by learning directly from perception to control, eliminating the need for complex hand-crafted features. However, even when employing SOTA VLA-based models, they still exhibit limited generalization capabilities and suboptimal action efficiency, due to the constraints imposed by insufficient robotic training datasets. In addition to addressing this problem using model-based approaches, we observe that robotic action slices, which consist of contiguous action steps, exhibit strong analogies to the time slices of threads in traditional operating systems. This insight presents a novel opportunity to tackle the problem at the system level.   In this paper, we propose AMS, a robot action management system enhanced with OS-level primitives like exception, context switch and record-and-replay, that improves both execution efficiency and success rates of robotic tasks. AMS first introduces action exception, which facilitates the immediate interruption of robotic actions to prevent error propagation. Secondly, AMS proposes action context, which eliminates redundant computations for VLA-based models, thereby accelerating execution efficiency in robotic actions. Finally, AMS leverages action replay to facilitate repetitive or similar robotic tasks without the need for re-training efforts. We implement AMS in both an emulated environment and on a real robot platform. The evaluation results demonstrate that AMS significantly enhances the model's generalization ability and action efficiency, achieving task success rate improvements ranging from 7x to 24x and saving end-to-end execution time ranging from 29% to 74% compared to existing robotic system without AMS support.

## 核心内容
End-to-end imitation learning frameworks (e.g., VLA) are increasingly prominent in robotics, as they enable rapid task transfer by learning directly from perception to control, eliminating the need for complex hand-crafted features. However, even when employing SOTA VLA-based models, they still exhibit limited generalization capabilities and suboptimal action efficiency, due to the constraints imposed by insufficient robotic training datasets. In addition to addressing this problem using model-based approaches, we observe that robotic action slices, which consist of contiguous action steps, exhibit strong analogies to the time slices of threads in traditional operating systems. This insight presents a novel opportunity to tackle the problem at the system level.   In this paper, we propose AMS, a robot action management system enhanced with OS-level primitives like exception, context switch and record-and-replay, that improves both execution efficiency and success rates of robotic tasks. AMS first introduces action exception, which facilitates the immediate interruption of robotic actions to prevent error propagation. Secondly, AMS proposes action context, which eliminates redundant computations for VLA-based models, thereby accelerating execution efficiency in robotic actions. Finally, AMS leverages action replay to facilitate repetitive or similar robotic tasks without the need for re-training efforts. We implement AMS in both an emulated environment and on a real robot platform. The evaluation results demonstrate that AMS significantly enhances the model's generalization ability and action efficiency, achieving task success rate improvements ranging from 7x to 24x and saving end-to-end execution time ranging from 29% to 74% compared to existing robotic system without AMS support.

## 参考
- http://arxiv.org/abs/2508.10259v1

## Overview
End-to-end imitation learning frameworks (e.g., VLA) are increasingly prominent in robotics, as they enable rapid task transfer by learning directly from perception to control, eliminating the need for complex hand-crafted features. However, even when employing SOTA VLA-based models, they still exhibit limited generalization capabilities and suboptimal action efficiency, due to the constraints imposed by insufficient robotic training datasets. In addition to addressing this problem using model-based approaches, we observe that robotic action slices, which consist of contiguous action steps, exhibit strong analogies to the time slices of threads in traditional operating systems. This insight presents a novel opportunity to tackle the problem at the system level. In this paper, we propose AMS, a robot action management system enhanced with OS-level primitives like exception, context switch and record-and-replay, that improves both execution efficiency and success rates of robotic tasks. AMS first introduces action exception, which facilitates the immediate interruption of robotic actions to prevent error propagation. Secondly, AMS proposes action context, which eliminates redundant computations for VLA-based models, thereby accelerating execution efficiency in robotic actions. Finally, AMS leverages action replay to facilitate repetitive or similar robotic tasks without the need for re-training efforts. We implement AMS in both an emulated environment and on a real robot platform. The evaluation results demonstrate that AMS significantly enhances the model's generalization ability and action efficiency, achieving task success rate improvements ranging from 7x to 24x and saving end-to-end execution time ranging from 29% to 74% compared to existing robotic system without AMS support.

## Content
End-to-end imitation learning frameworks (e.g., VLA) are increasingly prominent in robotics, as they enable rapid task transfer by learning directly from perception to control, eliminating the need for complex hand-crafted features. However, even when employing SOTA VLA-based models, they still exhibit limited generalization capabilities and suboptimal action efficiency, due to the constraints imposed by insufficient robotic training datasets. In addition to addressing this problem using model-based approaches, we observe that robotic action slices, which consist of contiguous action steps, exhibit strong analogies to the time slices of threads in traditional operating systems. This insight presents a novel opportunity to tackle the problem at the system level. In this paper, we propose AMS, a robot action management system enhanced with OS-level primitives like exception, context switch and record-and-replay, that improves both execution efficiency and success rates of robotic tasks. AMS first introduces action exception, which facilitates the immediate interruption of robotic actions to prevent error propagation. Secondly, AMS proposes action context, which eliminates redundant computations for VLA-based models, thereby accelerating execution efficiency in robotic actions. Finally, AMS leverages action replay to facilitate repetitive or similar robotic tasks without the need for re-training efforts. We implement AMS in both an emulated environment and on a real robot platform. The evaluation results demonstrate that AMS significantly enhances the model's generalization ability and action efficiency, achieving task success rate improvements ranging from 7x to 24x and saving end-to-end execution time ranging from 29% to 74% compared to existing robotic system without AMS support.

## 개요
엔드투엔드 모방 학습 프레임워크(예: VLA)는 로봇공학에서 점점 더 중요해지고 있습니다. 이는 인식에서 제어로 직접 학습하여 복잡한 수작업 특징이 필요 없이 빠른 작업 전환을 가능하게 하기 때문입니다. 그러나 최첨단 VLA 기반 모델을 사용하더라도 로봇 훈련 데이터셋의 부족으로 인해 일반화 능력이 제한적이고 행동 효율성이 최적화되지 못합니다. 모델 기반 접근법으로 이 문제를 해결하는 것 외에도, 연속된 행동 단계로 구성된 로봇 행동 조각이 전통적인 운영체제의 스레드 시간 조각과 강한 유사성을 가진다는 점을 관찰했습니다. 이 통찰은 시스템 수준에서 문제를 해결할 새로운 기회를 제공합니다. 본 논문에서는 예외, 컨텍스트 스위치, 기록 및 재생과 같은 OS 수준 프리미티브로 강화된 로봇 행동 관리 시스템 AMS를 제안하여 로봇 작업의 실행 효율성과 성공률을 모두 향상시킵니다. AMS는 먼저 행동 예외를 도입하여 로봇 행동을 즉시 중단시켜 오류 전파를 방지합니다. 둘째, AMS는 행동 컨텍스트를 제안하여 VLA 기반 모델의 중복 계산을 제거함으로써 로봇 행동의 실행 효율성을 가속화합니다. 마지막으로, AMS는 행동 재생을 활용하여 재훈련 없이 반복적이거나 유사한 로봇 작업을 수행할 수 있도록 합니다. 우리는 AMS를 에뮬레이션 환경과 실제 로봇 플랫폼에서 구현했습니다. 평가 결과는 AMS가 모델의 일반화 능력과 행동 효율성을 크게 향상시켜, AMS 지원이 없는 기존 로봇 시스템과 비교하여 작업 성공률을 7배에서 24배까지 개선하고 엔드투엔드 실행 시간을 29%에서 74%까지 절약함을 보여줍니다.

## 핵심 내용
엔드투엔드 모방 학습 프레임워크(예: VLA)는 로봇공학에서 점점 더 중요해지고 있습니다. 이는 인식에서 제어로 직접 학습하여 복잡한 수작업 특징이 필요 없이 빠른 작업 전환을 가능하게 하기 때문입니다. 그러나 최첨단 VLA 기반 모델을 사용하더라도 로봇 훈련 데이터셋의 부족으로 인해 일반화 능력이 제한적이고 행동 효율성이 최적화되지 못합니다. 모델 기반 접근법으로 이 문제를 해결하는 것 외에도, 연속된 행동 단계로 구성된 로봇 행동 조각이 전통적인 운영체제의 스레드 시간 조각과 강한 유사성을 가진다는 점을 관찰했습니다. 이 통찰은 시스템 수준에서 문제를 해결할 새로운 기회를 제공합니다. 본 논문에서는 예외, 컨텍스트 스위치, 기록 및 재생과 같은 OS 수준 프리미티브로 강화된 로봇 행동 관리 시스템 AMS를 제안하여 로봇 작업의 실행 효율성과 성공률을 모두 향상시킵니다. AMS는 먼저 행동 예외를 도입하여 로봇 행동을 즉시 중단시켜 오류 전파를 방지합니다. 둘째, AMS는 행동 컨텍스트를 제안하여 VLA 기반 모델의 중복 계산을 제거함으로써 로봇 행동의 실행 효율성을 가속화합니다. 마지막으로, AMS는 행동 재생을 활용하여 재훈련 없이 반복적이거나 유사한 로봇 작업을 수행할 수 있도록 합니다. 우리는 AMS를 에뮬레이션 환경과 실제 로봇 플랫폼에서 구현했습니다. 평가 결과는 AMS가 모델의 일반화 능력과 행동 효율성을 크게 향상시켜, AMS 지원이 없는 기존 로봇 시스템과 비교하여 작업 성공률을 7배에서 24배까지 개선하고 엔드투엔드 실행 시간을 29%에서 74%까지 절약함을 보여줍니다.
