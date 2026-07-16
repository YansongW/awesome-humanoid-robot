---
$id: ent_paper_chen_combatvla_an_efficient_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games'
  zh: CombatVLA
  ko: 'CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games'
summary:
  en: 'CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games (CombatVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Alibaba Group.'
  zh: 'CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games (CombatVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Alibaba Group.'
  ko: 'CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games (CombatVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Alibaba Group.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- combatvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.09527v2.
sources:
- id: src_001
  type: paper
  title: 'CombatVLA: An Efficient Vision-Language-Action Model for Combat Tasks in 3D Action Role-Playing Games (arXiv)'
  url: https://arxiv.org/abs/2503.09527
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CombatVLA source
  url: https://doi.org/10.48550/arXiv.2503.09527
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in Vision-Language-Action models (VLAs) have expanded the capabilities of embodied intelligence. However, significant challenges remain in real-time decision-making in complex 3D environments, which demand second-level responses, high-resolution perception, and tactical reasoning under dynamic conditions. To advance the field, we introduce CombatVLA, an efficient VLA model optimized for combat tasks in 3D action role-playing games(ARPGs). Specifically, our CombatVLA is a 3B model trained on video-action pairs collected by an action tracker, where the data is formatted as action-of-thought (AoT) sequences. Thereafter, CombatVLA seamlessly integrates into an action execution framework, allowing efficient inference through our truncated AoT strategy. Experimental results demonstrate that CombatVLA not only outperforms all existing models on the combat understanding benchmark but also achieves a 50-fold acceleration in game combat. Moreover, it has a higher task success rate than human players. We will open-source all resources, including the action tracker, dataset, benchmark, model weights, training code, and the implementation of the framework at https://combatvla.github.io/.

## 核心内容
Recent advances in Vision-Language-Action models (VLAs) have expanded the capabilities of embodied intelligence. However, significant challenges remain in real-time decision-making in complex 3D environments, which demand second-level responses, high-resolution perception, and tactical reasoning under dynamic conditions. To advance the field, we introduce CombatVLA, an efficient VLA model optimized for combat tasks in 3D action role-playing games(ARPGs). Specifically, our CombatVLA is a 3B model trained on video-action pairs collected by an action tracker, where the data is formatted as action-of-thought (AoT) sequences. Thereafter, CombatVLA seamlessly integrates into an action execution framework, allowing efficient inference through our truncated AoT strategy. Experimental results demonstrate that CombatVLA not only outperforms all existing models on the combat understanding benchmark but also achieves a 50-fold acceleration in game combat. Moreover, it has a higher task success rate than human players. We will open-source all resources, including the action tracker, dataset, benchmark, model weights, training code, and the implementation of the framework at https://combatvla.github.io/.

## 参考
- http://arxiv.org/abs/2503.09527v2

## Overview
Recent advances in Vision-Language-Action models (VLAs) have expanded the capabilities of embodied intelligence. However, significant challenges remain in real-time decision-making in complex 3D environments, which demand second-level responses, high-resolution perception, and tactical reasoning under dynamic conditions. To advance the field, we introduce CombatVLA, an efficient VLA model optimized for combat tasks in 3D action role-playing games (ARPGs). Specifically, our CombatVLA is a 3B model trained on video-action pairs collected by an action tracker, where the data is formatted as action-of-thought (AoT) sequences. Thereafter, CombatVLA seamlessly integrates into an action execution framework, allowing efficient inference through our truncated AoT strategy. Experimental results demonstrate that CombatVLA not only outperforms all existing models on the combat understanding benchmark but also achieves a 50-fold acceleration in game combat. Moreover, it has a higher task success rate than human players. We will open-source all resources, including the action tracker, dataset, benchmark, model weights, training code, and the implementation of the framework at https://combatvla.github.io/.

## Content
Recent advances in Vision-Language-Action models (VLAs) have expanded the capabilities of embodied intelligence. However, significant challenges remain in real-time decision-making in complex 3D environments, which demand second-level responses, high-resolution perception, and tactical reasoning under dynamic conditions. To advance the field, we introduce CombatVLA, an efficient VLA model optimized for combat tasks in 3D action role-playing games (ARPGs). Specifically, our CombatVLA is a 3B model trained on video-action pairs collected by an action tracker, where the data is formatted as action-of-thought (AoT) sequences. Thereafter, CombatVLA seamlessly integrates into an action execution framework, allowing efficient inference through our truncated AoT strategy. Experimental results demonstrate that CombatVLA not only outperforms all existing models on the combat understanding benchmark but also achieves a 50-fold acceleration in game combat. Moreover, it has a higher task success rate than human players. We will open-source all resources, including the action tracker, dataset, benchmark, model weights, training code, and the implementation of the framework at https://combatvla.github.io/.

## 개요
최근 Vision-Language-Action 모델(VLA)의 발전은 구현된 지능의 능력을 확장시켰습니다. 그러나 복잡한 3D 환경에서의 실시간 의사 결정에는 여전히 상당한 과제가 남아 있으며, 이는 초 단위 응답, 고해상도 인식, 동적 조건에서의 전술적 추론을 요구합니다. 이 분야를 발전시키기 위해, 우리는 3D 액션 롤플레잉 게임(ARPG)의 전투 작업에 최적화된 효율적인 VLA 모델인 CombatVLA를 소개합니다. 구체적으로, CombatVLA는 액션 트래커에 의해 수집된 비디오-액션 쌍으로 훈련된 3B 모델이며, 데이터는 action-of-thought(AoT) 시퀀스로 형식화됩니다. 이후 CombatVLA는 액션 실행 프레임워크에 원활하게 통합되어, 우리의 truncated AoT 전략을 통해 효율적인 추론을 가능하게 합니다. 실험 결과는 CombatVLA가 전투 이해 벤치마크에서 모든 기존 모델을 능가할 뿐만 아니라 게임 전투에서 50배의 가속을 달성함을 보여줍니다. 또한, 인간 플레이어보다 높은 작업 성공률을 보입니다. 우리는 액션 트래커, 데이터셋, 벤치마크, 모델 가중치, 훈련 코드, 프레임워크 구현을 포함한 모든 리소스를 https://combatvla.github.io/에서 오픈소스로 공개할 예정입니다.

## 핵심 내용
최근 Vision-Language-Action 모델(VLA)의 발전은 구현된 지능의 능력을 확장시켰습니다. 그러나 복잡한 3D 환경에서의 실시간 의사 결정에는 여전히 상당한 과제가 남아 있으며, 이는 초 단위 응답, 고해상도 인식, 동적 조건에서의 전술적 추론을 요구합니다. 이 분야를 발전시키기 위해, 우리는 3D 액션 롤플레잉 게임(ARPG)의 전투 작업에 최적화된 효율적인 VLA 모델인 CombatVLA를 소개합니다. 구체적으로, CombatVLA는 액션 트래커에 의해 수집된 비디오-액션 쌍으로 훈련된 3B 모델이며, 데이터는 action-of-thought(AoT) 시퀀스로 형식화됩니다. 이후 CombatVLA는 액션 실행 프레임워크에 원활하게 통합되어, 우리의 truncated AoT 전략을 통해 효율적인 추론을 가능하게 합니다. 실험 결과는 CombatVLA가 전투 이해 벤치마크에서 모든 기존 모델을 능가할 뿐만 아니라 게임 전투에서 50배의 가속을 달성함을 보여줍니다. 또한, 인간 플레이어보다 높은 작업 성공률을 보입니다. 우리는 액션 트래커, 데이터셋, 벤치마크, 모델 가중치, 훈련 코드, 프레임워크 구현을 포함한 모든 리소스를 https://combatvla.github.io/에서 오픈소스로 공개할 예정입니다.
