---
$id: ent_paper_ma_running_vlas_at_real_time_spee_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Running VLAs at Real-time Speed
  zh: Running VLAs at Real-time Speed
  ko: Running VLAs at Real-time Speed
summary:
  en: Running VLAs at Real-time Speed (Running VLAs at Real-time Speed), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Dexmal, StepFun.
  zh: Running VLAs at Real-time Speed (Running VLAs at Real-time Speed), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Dexmal, StepFun.
  ko: Running VLAs at Real-time Speed (Running VLAs at Real-time Speed), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Dexmal, StepFun.
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
- robotic_manipulation
- running_vlas_at_real_time_spee
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26742v1.
sources:
- id: src_001
  type: paper
  title: Running VLAs at Real-time Speed (arXiv)
  url: https://arxiv.org/abs/2510.26742
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Running VLAs at Real-time Speed source
  url: https://doi.org/10.48550/arXiv.2510.26742
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we show how to run pi0-level multi-view VLA at 30Hz frame rate and at most 480Hz trajectory frequency using a single consumer GPU. This enables dynamic and real-time tasks that were previously believed to be unattainable by large VLA models. To achieve it, we introduce a bag of strategies to eliminate the overheads in model inference. The real-world experiment shows that the pi0 policy with our strategy achieves a 100% success rate in grasping a falling pen task. Based on the results, we further propose a full streaming inference framework for real-time robot control of VLA. Code is available at https://github.com/Dexmal/realtime-vla.

## 核心内容
In this paper, we show how to run pi0-level multi-view VLA at 30Hz frame rate and at most 480Hz trajectory frequency using a single consumer GPU. This enables dynamic and real-time tasks that were previously believed to be unattainable by large VLA models. To achieve it, we introduce a bag of strategies to eliminate the overheads in model inference. The real-world experiment shows that the pi0 policy with our strategy achieves a 100% success rate in grasping a falling pen task. Based on the results, we further propose a full streaming inference framework for real-time robot control of VLA. Code is available at https://github.com/Dexmal/realtime-vla.

## 参考
- http://arxiv.org/abs/2510.26742v1

## Overview
In this paper, we show how to run pi0-level multi-view VLA at 30Hz frame rate and at most 480Hz trajectory frequency using a single consumer GPU. This enables dynamic and real-time tasks that were previously believed to be unattainable by large VLA models. To achieve it, we introduce a bag of strategies to eliminate the overheads in model inference. The real-world experiment shows that the pi0 policy with our strategy achieves a 100% success rate in grasping a falling pen task. Based on the results, we further propose a full streaming inference framework for real-time robot control of VLA. Code is available at https://github.com/Dexmal/realtime-vla.

## Content
In this paper, we show how to run pi0-level multi-view VLA at 30Hz frame rate and at most 480Hz trajectory frequency using a single consumer GPU. This enables dynamic and real-time tasks that were previously believed to be unattainable by large VLA models. To achieve it, we introduce a bag of strategies to eliminate the overheads in model inference. The real-world experiment shows that the pi0 policy with our strategy achieves a 100% success rate in grasping a falling pen task. Based on the results, we further propose a full streaming inference framework for real-time robot control of VLA. Code is available at https://github.com/Dexmal/realtime-vla.

## 개요
본 논문에서는 단일 소비자 GPU를 사용하여 pi0 수준의 다중 뷰 VLA를 30Hz 프레임 속도와 최대 480Hz 궤적 주파수로 실행하는 방법을 보여줍니다. 이를 통해 대규모 VLA 모델로는 이전에 달성할 수 없다고 여겨졌던 동적이고 실시간 작업이 가능해집니다. 이를 달성하기 위해 모델 추론의 오버헤드를 제거하는 전략 모음을 소개합니다. 실제 실험 결과, 당사의 전략을 적용한 pi0 정책은 떨어지는 펜 잡기 작업에서 100% 성공률을 달성했습니다. 이러한 결과를 바탕으로 VLA의 실시간 로봇 제어를 위한 완전한 스트리밍 추론 프레임워크를 추가로 제안합니다. 코드는 https://github.com/Dexmal/realtime-vla에서 확인할 수 있습니다.

## 핵심 내용
본 논문에서는 단일 소비자 GPU를 사용하여 pi0 수준의 다중 뷰 VLA를 30Hz 프레임 속도와 최대 480Hz 궤적 주파수로 실행하는 방법을 보여줍니다. 이를 통해 대규모 VLA 모델로는 이전에 달성할 수 없다고 여겨졌던 동적이고 실시간 작업이 가능해집니다. 이를 달성하기 위해 모델 추론의 오버헤드를 제거하는 전략 모음을 소개합니다. 실제 실험 결과, 당사의 전략을 적용한 pi0 정책은 떨어지는 펜 잡기 작업에서 100% 성공률을 달성했습니다. 이러한 결과를 바탕으로 VLA의 실시간 로봇 제어를 위한 완전한 스트리밍 추론 프레임워크를 추가로 제안합니다. 코드는 https://github.com/Dexmal/realtime-vla에서 확인할 수 있습니다.
