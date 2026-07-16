---
$id: ent_paper_gu_usim_and_u0_a_vision_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots'
  zh: USIM & U0
  ko: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots'
summary:
  en: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (USIM & U0), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences,
    Key Laboratory of Cognition and Decision Intelligence for Complex Systems.'
  zh: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (USIM & U0), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences,
    Key Laboratory of Cognition and Decision Intelligence for Complex Systems.'
  ko: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (USIM & U0), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences,
    Key Laboratory of Cognition and Decision Intelligence for Complex Systems.'
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
- usim_u0
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07869v4.
sources:
- id: src_001
  type: paper
  title: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (arXiv)'
  url: https://arxiv.org/abs/2510.07869
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: USIM & U0 source
  url: https://doi.org/10.48550/arXiv.2510.07869
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Underwater environments pose unique challenges for robotic navigation and manipulation. While existing research has primarily focused on task-specific methods, studies on general-purpose intelligence for multi-task execution remain scarce. To address this gap, we propose a unified framework for general-purpose underwater robots that integrates perception and action driven by language instructions. First, we develop a data synthesis pipeline to construct USIM, a simulation-based dataset which comprises over 905K frames from 2275 trajectories, totaling approximately 25 hours of BlueROV2 interactions. Furthermore, we propose U0, a vision-language-action (VLA) model capable of executing various tasks from obstacle-avoidance navigation to three-dimensional mobile manipulation. The model features a convolution-attention-based perception (CAP) module, which incorporates target pose estimation as an auxiliary task to explicitly bolster the model's spatial awareness. For evaluation, we establish a systematic assessment framework and an automated pipeline encompassing both offline metrics and online task execution. Experimental results demonstrate that the USIM dataset significantly empowers existing VLA models to adapt to underwater scenarios. Notably, our U0 model achieves state-of-the-art performance: it reduces the offline mean action prediction error to 0.0359 and achieves an overall online success rate of 43.1%, marking a 5.5% improvement over existing competitive baselines (below 37.6%), with navigation tasks reaching as high as 87.5%. These results validate the feasibility of general-purpose intelligence in underwater robotics, providing a foundation for scalable dataset synthesis and aquatic embodied agents.

## 核心内容
Underwater environments pose unique challenges for robotic navigation and manipulation. While existing research has primarily focused on task-specific methods, studies on general-purpose intelligence for multi-task execution remain scarce. To address this gap, we propose a unified framework for general-purpose underwater robots that integrates perception and action driven by language instructions. First, we develop a data synthesis pipeline to construct USIM, a simulation-based dataset which comprises over 905K frames from 2275 trajectories, totaling approximately 25 hours of BlueROV2 interactions. Furthermore, we propose U0, a vision-language-action (VLA) model capable of executing various tasks from obstacle-avoidance navigation to three-dimensional mobile manipulation. The model features a convolution-attention-based perception (CAP) module, which incorporates target pose estimation as an auxiliary task to explicitly bolster the model's spatial awareness. For evaluation, we establish a systematic assessment framework and an automated pipeline encompassing both offline metrics and online task execution. Experimental results demonstrate that the USIM dataset significantly empowers existing VLA models to adapt to underwater scenarios. Notably, our U0 model achieves state-of-the-art performance: it reduces the offline mean action prediction error to 0.0359 and achieves an overall online success rate of 43.1%, marking a 5.5% improvement over existing competitive baselines (below 37.6%), with navigation tasks reaching as high as 87.5%. These results validate the feasibility of general-purpose intelligence in underwater robotics, providing a foundation for scalable dataset synthesis and aquatic embodied agents.

## 参考
- http://arxiv.org/abs/2510.07869v4

## Overview
Underwater environments pose unique challenges for robotic navigation and manipulation. While existing research has primarily focused on task-specific methods, studies on general-purpose intelligence for multi-task execution remain scarce. To address this gap, we propose a unified framework for general-purpose underwater robots that integrates perception and action driven by language instructions. First, we develop a data synthesis pipeline to construct USIM, a simulation-based dataset which comprises over 905K frames from 2275 trajectories, totaling approximately 25 hours of BlueROV2 interactions. Furthermore, we propose U0, a vision-language-action (VLA) model capable of executing various tasks from obstacle-avoidance navigation to three-dimensional mobile manipulation. The model features a convolution-attention-based perception (CAP) module, which incorporates target pose estimation as an auxiliary task to explicitly bolster the model's spatial awareness. For evaluation, we establish a systematic assessment framework and an automated pipeline encompassing both offline metrics and online task execution. Experimental results demonstrate that the USIM dataset significantly empowers existing VLA models to adapt to underwater scenarios. Notably, our U0 model achieves state-of-the-art performance: it reduces the offline mean action prediction error to 0.0359 and achieves an overall online success rate of 43.1%, marking a 5.5% improvement over existing competitive baselines (below 37.6%), with navigation tasks reaching as high as 87.5%. These results validate the feasibility of general-purpose intelligence in underwater robotics, providing a foundation for scalable dataset synthesis and aquatic embodied agents.

## Content
Underwater environments pose unique challenges for robotic navigation and manipulation. While existing research has primarily focused on task-specific methods, studies on general-purpose intelligence for multi-task execution remain scarce. To address this gap, we propose a unified framework for general-purpose underwater robots that integrates perception and action driven by language instructions. First, we develop a data synthesis pipeline to construct USIM, a simulation-based dataset which comprises over 905K frames from 2275 trajectories, totaling approximately 25 hours of BlueROV2 interactions. Furthermore, we propose U0, a vision-language-action (VLA) model capable of executing various tasks from obstacle-avoidance navigation to three-dimensional mobile manipulation. The model features a convolution-attention-based perception (CAP) module, which incorporates target pose estimation as an auxiliary task to explicitly bolster the model's spatial awareness. For evaluation, we establish a systematic assessment framework and an automated pipeline encompassing both offline metrics and online task execution. Experimental results demonstrate that the USIM dataset significantly empowers existing VLA models to adapt to underwater scenarios. Notably, our U0 model achieves state-of-the-art performance: it reduces the offline mean action prediction error to 0.0359 and achieves an overall online success rate of 43.1%, marking a 5.5% improvement over existing competitive baselines (below 37.6%), with navigation tasks reaching as high as 87.5%. These results validate the feasibility of general-purpose intelligence in underwater robotics, providing a foundation for scalable dataset synthesis and aquatic embodied agents.

## 개요
수중 환경은 로봇 항법 및 조작에 독특한 도전 과제를 제시합니다. 기존 연구는 주로 작업별 방법에 초점을 맞춰 왔지만, 다중 작업 실행을 위한 범용 지능에 대한 연구는 여전히 부족합니다. 이러한 격차를 해소하기 위해, 우리는 언어 명령에 의해 구동되는 인식과 행동을 통합하는 범용 수중 로봇을 위한 통합 프레임워크를 제안합니다. 먼저, 우리는 데이터 합성 파이프라인을 개발하여 시뮬레이션 기반 데이터셋인 USIM을 구축했습니다. 이 데이터셋은 2275개의 궤적으로부터 905K 프레임 이상을 포함하며, 총 약 25시간의 BlueROV2 상호작용으로 구성됩니다. 또한, 우리는 장애물 회피 항법부터 3차원 이동 조작까지 다양한 작업을 실행할 수 있는 시각-언어-행동(VLA) 모델인 U0을 제안합니다. 이 모델은 합성곱-어텐션 기반 인식(CAP) 모듈을 특징으로 하며, 대상 자세 추정을 보조 작업으로 통합하여 모델의 공간 인식을 명시적으로 강화합니다. 평가를 위해, 우리는 오프라인 지표와 온라인 작업 실행을 모두 포함하는 체계적인 평가 프레임워크와 자동화된 파이프라인을 구축했습니다. 실험 결과는 USIM 데이터셋이 기존 VLA 모델이 수중 시나리오에 적응할 수 있도록 크게 지원함을 보여줍니다. 특히, 우리의 U0 모델은 최첨단 성능을 달성합니다: 오프라인 평균 행동 예측 오차를 0.0359로 줄이고, 전체 온라인 성공률 43.1%를 달성하여 기존 경쟁 기준선(37.6% 미만) 대비 5.5% 향상되었으며, 항법 작업은 최대 87.5%에 이릅니다. 이러한 결과는 수중 로봇 공학에서 범용 지능의 실현 가능성을 검증하며, 확장 가능한 데이터셋 합성 및 수중 임베디드 에이전트를 위한 기반을 제공합니다.

## 핵심 내용
수중 환경은 로봇 항법 및 조작에 독특한 도전 과제를 제시합니다. 기존 연구는 주로 작업별 방법에 초점을 맞춰 왔지만, 다중 작업 실행을 위한 범용 지능에 대한 연구는 여전히 부족합니다. 이러한 격차를 해소하기 위해, 우리는 언어 명령에 의해 구동되는 인식과 행동을 통합하는 범용 수중 로봇을 위한 통합 프레임워크를 제안합니다. 먼저, 우리는 데이터 합성 파이프라인을 개발하여 시뮬레이션 기반 데이터셋인 USIM을 구축했습니다. 이 데이터셋은 2275개의 궤적으로부터 905K 프레임 이상을 포함하며, 총 약 25시간의 BlueROV2 상호작용으로 구성됩니다. 또한, 우리는 장애물 회피 항법부터 3차원 이동 조작까지 다양한 작업을 실행할 수 있는 시각-언어-행동(VLA) 모델인 U0을 제안합니다. 이 모델은 합성곱-어텐션 기반 인식(CAP) 모듈을 특징으로 하며, 대상 자세 추정을 보조 작업으로 통합하여 모델의 공간 인식을 명시적으로 강화합니다. 평가를 위해, 우리는 오프라인 지표와 온라인 작업 실행을 모두 포함하는 체계적인 평가 프레임워크와 자동화된 파이프라인을 구축했습니다. 실험 결과는 USIM 데이터셋이 기존 VLA 모델이 수중 시나리오에 적응할 수 있도록 크게 지원함을 보여줍니다. 특히, 우리의 U0 모델은 최첨단 성능을 달성합니다: 오프라인 평균 행동 예측 오차를 0.0359로 줄이고, 전체 온라인 성공률 43.1%를 달성하여 기존 경쟁 기준선(37.6% 미만) 대비 5.5% 향상되었으며, 항법 작업은 최대 87.5%에 이릅니다. 이러한 결과는 수중 로봇 공학에서 범용 지능의 실현 가능성을 검증하며, 확장 가능한 데이터셋 합성 및 수중 임베디드 에이전트를 위한 기반을 제공합니다.
