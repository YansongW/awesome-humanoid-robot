---
$id: ent_paper_li_llara_supercharging_robot_lear_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LLaRA: Supercharging Robot Learning Data for Vision-Language Policy'
  zh: LLaRA
  ko: 'LLaRA: Supercharging Robot Learning Data for Vision-Language Policy'
summary:
  en: 'LLaRA: Supercharging Robot Learning Data for Vision-Language Policy (LLaRA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Stony Brook University, University of Wisconsin-Madison, and published at
    ICLR 2024.'
  zh: 'LLaRA: Supercharging Robot Learning Data for Vision-Language Policy (LLaRA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Stony Brook University, University of Wisconsin-Madison, and published at
    ICLR 2024.'
  ko: 'LLaRA: Supercharging Robot Learning Data for Vision-Language Policy (LLaRA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Stony Brook University, University of Wisconsin-Madison, and published at
    ICLR 2024.'
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
- llara
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.20095v3.
sources:
- id: src_001
  type: paper
  title: LLaRA source
  url: https://openreview.net/forum?id=iVxxgZlXh6
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision Language Models (VLMs) have recently been leveraged to generate robotic actions, forming Vision-Language-Action (VLA) models. However, directly adapting a pretrained VLM for robotic control remains challenging, particularly when constrained by a limited number of robot demonstrations. In this work, we introduce LLaRA: Large Language and Robotics Assistant, a framework that formulates robot action policy as visuo-textual conversations and enables an efficient transfer of a pretrained VLM into a powerful VLA, motivated by the success of visual instruction tuning in Computer Vision. First, we present an automated pipeline to generate conversation-style instruction tuning data for robots from existing behavior cloning datasets, aligning robotic actions with image pixel coordinates. Further, we enhance this dataset in a self-supervised manner by defining six auxiliary tasks, without requiring any additional action annotations. We show that a VLM finetuned with a limited amount of such datasets can produce meaningful action decisions for robotic control. Through experiments across multiple simulated and real-world tasks, we demonstrate that LLaRA achieves state-of-the-art performance while preserving the generalization capabilities of large language models. The code, datasets, and pretrained models are available at https://github.com/LostXine/LLaRA.

## 核心内容
Vision Language Models (VLMs) have recently been leveraged to generate robotic actions, forming Vision-Language-Action (VLA) models. However, directly adapting a pretrained VLM for robotic control remains challenging, particularly when constrained by a limited number of robot demonstrations. In this work, we introduce LLaRA: Large Language and Robotics Assistant, a framework that formulates robot action policy as visuo-textual conversations and enables an efficient transfer of a pretrained VLM into a powerful VLA, motivated by the success of visual instruction tuning in Computer Vision. First, we present an automated pipeline to generate conversation-style instruction tuning data for robots from existing behavior cloning datasets, aligning robotic actions with image pixel coordinates. Further, we enhance this dataset in a self-supervised manner by defining six auxiliary tasks, without requiring any additional action annotations. We show that a VLM finetuned with a limited amount of such datasets can produce meaningful action decisions for robotic control. Through experiments across multiple simulated and real-world tasks, we demonstrate that LLaRA achieves state-of-the-art performance while preserving the generalization capabilities of large language models. The code, datasets, and pretrained models are available at https://github.com/LostXine/LLaRA.

## 参考
- http://arxiv.org/abs/2406.20095v3

## Overview
Vision Language Models (VLMs) have recently been leveraged to generate robotic actions, forming Vision-Language-Action (VLA) models. However, directly adapting a pretrained VLM for robotic control remains challenging, particularly when constrained by a limited number of robot demonstrations. In this work, we introduce LLaRA: Large Language and Robotics Assistant, a framework that formulates robot action policy as visuo-textual conversations and enables an efficient transfer of a pretrained VLM into a powerful VLA, motivated by the success of visual instruction tuning in Computer Vision. First, we present an automated pipeline to generate conversation-style instruction tuning data for robots from existing behavior cloning datasets, aligning robotic actions with image pixel coordinates. Further, we enhance this dataset in a self-supervised manner by defining six auxiliary tasks, without requiring any additional action annotations. We show that a VLM finetuned with a limited amount of such datasets can produce meaningful action decisions for robotic control. Through experiments across multiple simulated and real-world tasks, we demonstrate that LLaRA achieves state-of-the-art performance while preserving the generalization capabilities of large language models. The code, datasets, and pretrained models are available at https://github.com/LostXine/LLaRA.

## Content
Vision Language Models (VLMs) have recently been leveraged to generate robotic actions, forming Vision-Language-Action (VLA) models. However, directly adapting a pretrained VLM for robotic control remains challenging, particularly when constrained by a limited number of robot demonstrations. In this work, we introduce LLaRA: Large Language and Robotics Assistant, a framework that formulates robot action policy as visuo-textual conversations and enables an efficient transfer of a pretrained VLM into a powerful VLA, motivated by the success of visual instruction tuning in Computer Vision. First, we present an automated pipeline to generate conversation-style instruction tuning data for robots from existing behavior cloning datasets, aligning robotic actions with image pixel coordinates. Further, we enhance this dataset in a self-supervised manner by defining six auxiliary tasks, without requiring any additional action annotations. We show that a VLM finetuned with a limited amount of such datasets can produce meaningful action decisions for robotic control. Through experiments across multiple simulated and real-world tasks, we demonstrate that LLaRA achieves state-of-the-art performance while preserving the generalization capabilities of large language models. The code, datasets, and pretrained models are available at https://github.com/LostXine/LLaRA.

## 개요
최근 Vision Language Models(VLM)이 로봇 동작을 생성하는 데 활용되면서 Vision-Language-Action(VLA) 모델이 형성되었습니다. 그러나 사전 학습된 VLM을 로봇 제어에 직접 적용하는 것은 여전히 어려운 과제이며, 특히 제한된 수의 로봇 시연 데이터로 제약될 때 더욱 그렇습니다. 본 연구에서는 컴퓨터 비전에서의 시각 명령 튜닝(visual instruction tuning)의 성공에 영감을 받아, 로봇 행동 정책을 시각-텍스트 대화로 공식화하고 사전 학습된 VLM을 강력한 VLA로 효율적으로 전이할 수 있는 프레임워크인 LLaRA: Large Language and Robotics Assistant를 소개합니다. 먼저, 기존의 행동 복제 데이터셋에서 로봇을 위한 대화 스타일의 명령 튜닝 데이터를 생성하고, 로봇 동작을 이미지 픽셀 좌표와 정렬하는 자동화된 파이프라인을 제시합니다. 또한, 추가적인 동작 주석 없이 6개의 보조 작업을 정의하여 자가 지도 방식으로 이 데이터셋을 향상시킵니다. 제한된 양의 이러한 데이터셋으로 미세 조정된 VLM이 로봇 제어를 위한 의미 있는 행동 결정을 생성할 수 있음을 보여줍니다. 여러 시뮬레이션 및 실제 환경 작업에 걸친 실험을 통해 LLaRA가 대규모 언어 모델의 일반화 능력을 유지하면서 최첨단 성능을 달성함을 입증합니다. 코드, 데이터셋 및 사전 학습된 모델은 https://github.com/LostXine/LLaRA에서 확인할 수 있습니다.

## 핵심 내용
최근 Vision Language Models(VLM)이 로봇 동작을 생성하는 데 활용되면서 Vision-Language-Action(VLA) 모델이 형성되었습니다. 그러나 사전 학습된 VLM을 로봇 제어에 직접 적용하는 것은 여전히 어려운 과제이며, 특히 제한된 수의 로봇 시연 데이터로 제약될 때 더욱 그렇습니다. 본 연구에서는 컴퓨터 비전에서의 시각 명령 튜닝(visual instruction tuning)의 성공에 영감을 받아, 로봇 행동 정책을 시각-텍스트 대화로 공식화하고 사전 학습된 VLM을 강력한 VLA로 효율적으로 전이할 수 있는 프레임워크인 LLaRA: Large Language and Robotics Assistant를 소개합니다. 먼저, 기존의 행동 복제 데이터셋에서 로봇을 위한 대화 스타일의 명령 튜닝 데이터를 생성하고, 로봇 동작을 이미지 픽셀 좌표와 정렬하는 자동화된 파이프라인을 제시합니다. 또한, 추가적인 동작 주석 없이 6개의 보조 작업을 정의하여 자가 지도 방식으로 이 데이터셋을 향상시킵니다. 제한된 양의 이러한 데이터셋으로 미세 조정된 VLM이 로봇 제어를 위한 의미 있는 행동 결정을 생성할 수 있음을 보여줍니다. 여러 시뮬레이션 및 실제 환경 작업에 걸친 실험을 통해 LLaRA가 대규모 언어 모델의 일반화 능력을 유지하면서 최첨단 성능을 달성함을 입증합니다. 코드, 데이터셋 및 사전 학습된 모델은 https://github.com/LostXine/LLaRA에서 확인할 수 있습니다.
