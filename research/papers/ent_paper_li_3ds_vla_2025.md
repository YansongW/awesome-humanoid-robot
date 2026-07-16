---
$id: ent_paper_li_3ds_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 3DS-VLA
  zh: 3DS-VLA
  ko: 3DS-VLA
summary:
  en: 3DS-VLA (3DS-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by CFCS, School
    of Computer Science, Peking University, PKU-Agibot Lab, State Key Laboratory of Multimedia Information Processing, School
    of Computer Science, Peking University, CUHK, and published at CoRL25.
  zh: 3DS-VLA (3DS-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by CFCS, School
    of Computer Science, Peking University, PKU-Agibot Lab, State Key Laboratory of Multimedia Information Processing, School
    of Computer Science, Peking University, CUHK, and published at CoRL25.
  ko: 3DS-VLA (3DS-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by CFCS, School
    of Computer Science, Peking University, PKU-Agibot Lab, State Key Laboratory of Multimedia Information Processing, School
    of Computer Science, Peking University, CUHK, and published at CoRL25.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 3ds_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.09631v1.
sources:
- id: src_001
  type: paper
  title: 3DS-VLA source
  url: https://proceedings.mlr.press/v305/li25g.html
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent vision-language-action (VLA) models rely on 2D inputs, lacking integration with the broader realm of the 3D physical world. Furthermore, they perform action prediction by learning a direct mapping from perception to action, neglecting the vast dynamics of the world and the relations between actions and dynamics. In contrast, human beings are endowed with world models that depict imagination about future scenarios to plan actions accordingly. To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a generative world model. Specifically, 3D-VLA is built on top of a 3D-based large language model (LLM), and a set of interaction tokens is introduced to engage with the embodied environment. Furthermore, to inject generation abilities into the model, we train a series of embodied diffusion models and align them into the LLM for predicting the goal images and point clouds. To train our 3D-VLA, we curate a large-scale 3D embodied instruction dataset by extracting vast 3D-related information from existing robotics datasets. Our experiments on held-in datasets demonstrate that 3D-VLA significantly improves the reasoning, multimodal generation, and planning capabilities in embodied environments, showcasing its potential in real-world applications.

## 核心内容
Recent vision-language-action (VLA) models rely on 2D inputs, lacking integration with the broader realm of the 3D physical world. Furthermore, they perform action prediction by learning a direct mapping from perception to action, neglecting the vast dynamics of the world and the relations between actions and dynamics. In contrast, human beings are endowed with world models that depict imagination about future scenarios to plan actions accordingly. To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a generative world model. Specifically, 3D-VLA is built on top of a 3D-based large language model (LLM), and a set of interaction tokens is introduced to engage with the embodied environment. Furthermore, to inject generation abilities into the model, we train a series of embodied diffusion models and align them into the LLM for predicting the goal images and point clouds. To train our 3D-VLA, we curate a large-scale 3D embodied instruction dataset by extracting vast 3D-related information from existing robotics datasets. Our experiments on held-in datasets demonstrate that 3D-VLA significantly improves the reasoning, multimodal generation, and planning capabilities in embodied environments, showcasing its potential in real-world applications.

## 参考
- http://arxiv.org/abs/2403.09631v1

## Overview
Recent vision-language-action (VLA) models rely on 2D inputs, lacking integration with the broader realm of the 3D physical world. Furthermore, they perform action prediction by learning a direct mapping from perception to action, neglecting the vast dynamics of the world and the relations between actions and dynamics. In contrast, human beings are endowed with world models that depict imagination about future scenarios to plan actions accordingly. To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a generative world model. Specifically, 3D-VLA is built on top of a 3D-based large language model (LLM), and a set of interaction tokens is introduced to engage with the embodied environment. Furthermore, to inject generation abilities into the model, we train a series of embodied diffusion models and align them into the LLM for predicting the goal images and point clouds. To train our 3D-VLA, we curate a large-scale 3D embodied instruction dataset by extracting vast 3D-related information from existing robotics datasets. Our experiments on held-in datasets demonstrate that 3D-VLA significantly improves the reasoning, multimodal generation, and planning capabilities in embodied environments, showcasing its potential in real-world applications.

## Content
Recent vision-language-action (VLA) models rely on 2D inputs, lacking integration with the broader realm of the 3D physical world. Furthermore, they perform action prediction by learning a direct mapping from perception to action, neglecting the vast dynamics of the world and the relations between actions and dynamics. In contrast, human beings are endowed with world models that depict imagination about future scenarios to plan actions accordingly. To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a generative world model. Specifically, 3D-VLA is built on top of a 3D-based large language model (LLM), and a set of interaction tokens is introduced to engage with the embodied environment. Furthermore, to inject generation abilities into the model, we train a series of embodied diffusion models and align them into the LLM for predicting the goal images and point clouds. To train our 3D-VLA, we curate a large-scale 3D embodied instruction dataset by extracting vast 3D-related information from existing robotics datasets. Our experiments on held-in datasets demonstrate that 3D-VLA significantly improves the reasoning, multimodal generation, and planning capabilities in embodied environments, showcasing its potential in real-world applications.

## 개요
최근의 VLA(Vision-Language-Action) 모델은 2D 입력에 의존하여 3D 물리적 세계의 광범위한 영역과의 통합이 부족합니다. 또한, 지각에서 행동으로의 직접적인 매핑을 학습하여 행동 예측을 수행하지만, 세계의 방대한 역학과 행동과 역학 간의 관계를 무시합니다. 이와 대조적으로, 인간은 미래 시나리오에 대한 상상을 묘사하는 세계 모델을 부여받아 그에 따라 행동을 계획합니다. 이를 위해, 우리는 생성적 세계 모델을 통해 3D 지각, 추론 및 행동을 원활하게 연결하는 새로운 체화된 기초 모델군을 도입하여 3D-VLA를 제안합니다. 구체적으로, 3D-VLA는 3D 기반 대규모 언어 모델(LLM) 위에 구축되며, 체화된 환경과 상호작용하기 위해 일련의 상호작용 토큰이 도입됩니다. 또한, 모델에 생성 능력을 주입하기 위해 일련의 체화된 확산 모델을 훈련하고 이를 LLM에 정렬하여 목표 이미지와 포인트 클라우드를 예측합니다. 3D-VLA를 훈련하기 위해, 기존 로봇공학 데이터셋에서 방대한 3D 관련 정보를 추출하여 대규모 3D 체화된 명령 데이터셋을 구성합니다. 보유 데이터셋에 대한 실험은 3D-VLA가 체화된 환경에서 추론, 다중 모드 생성 및 계획 능력을 크게 향상시켜 실제 응용에서의 잠재력을 보여줍니다.

## 핵심 내용
최근의 VLA(Vision-Language-Action) 모델은 2D 입력에 의존하여 3D 물리적 세계의 광범위한 영역과의 통합이 부족합니다. 또한, 지각에서 행동으로의 직접적인 매핑을 학습하여 행동 예측을 수행하지만, 세계의 방대한 역학과 행동과 역학 간의 관계를 무시합니다. 이와 대조적으로, 인간은 미래 시나리오에 대한 상상을 묘사하는 세계 모델을 부여받아 그에 따라 행동을 계획합니다. 이를 위해, 우리는 생성적 세계 모델을 통해 3D 지각, 추론 및 행동을 원활하게 연결하는 새로운 체화된 기초 모델군을 도입하여 3D-VLA를 제안합니다. 구체적으로, 3D-VLA는 3D 기반 대규모 언어 모델(LLM) 위에 구축되며, 체화된 환경과 상호작용하기 위해 일련의 상호작용 토큰이 도입됩니다. 또한, 모델에 생성 능력을 주입하기 위해 일련의 체화된 확산 모델을 훈련하고 이를 LLM에 정렬하여 목표 이미지와 포인트 클라우드를 예측합니다. 3D-VLA를 훈련하기 위해, 기존 로봇공학 데이터셋에서 방대한 3D 관련 정보를 추출하여 대규모 3D 체화된 명령 데이터셋을 구성합니다. 보유 데이터셋에 대한 실험은 3D-VLA가 체화된 환경에서 추론, 다중 모드 생성 및 계획 능력을 크게 향상시켜 실제 응용에서의 잠재력을 보여줍니다.
