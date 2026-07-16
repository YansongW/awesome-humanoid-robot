---
$id: ent_paper_zhang_iflybot_vla_technical_report_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: iFlyBot-VLA Technical Report
  zh: iFlyBot-VLA
  ko: iFlyBot-VLA Technical Report
summary:
  en: iFlyBot-VLA Technical Report (iFlyBot-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by iFlyTek Reasearch and Development Group, LindenBot.
  zh: iFlyBot-VLA Technical Report (iFlyBot-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by iFlyTek Reasearch and Development Group, LindenBot.
  ko: iFlyBot-VLA Technical Report (iFlyBot-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by iFlyTek Reasearch and Development Group, LindenBot.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- iflybot_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01914v1.
sources:
- id: src_001
  type: paper
  title: iFlyBot-VLA Technical Report (arXiv)
  url: https://arxiv.org/abs/2511.01914
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: iFlyBot-VLA source
  url: https://doi.org/10.48550/arXiv.2511.01914
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce iFlyBot-VLA, a large-scale Vision-Language-Action (VLA) model trained under a novel framework. The main contributions are listed as follows: (1) a latent action model thoroughly trained on large-scale human and robotic manipulation videos; (2) a dual-level action representation framework that jointly supervises both the Vision-Language Model (VLM) and the action expert during training; (3) a mixed training strategy that combines robot trajectory data with general QA and spatial QA datasets, effectively enhancing the 3D perceptual and reasoning capabilities of the VLM backbone. Specifically, the VLM is trained to predict two complementary forms of actions: latent actions, derived from our latent action model pretrained on cross-embodiment manipulation data, which capture implicit high-level intentions; and structured discrete action tokens, obtained through frequency-domain transformations of continuous control signals, which encode explicit low-level dynamics. This dual supervision aligns the representation spaces of language, vision, and action, enabling the VLM to directly contribute to action generation. Experimental results on the LIBERO Franka benchmark demonstrate the superiority of our frame-work, while real-world evaluations further show that iFlyBot-VLA achieves competitive success rates across diverse and challenging manipulation tasks. Furthermore, we plan to open-source a portion of our self-constructed dataset to support future research in the community

## 核心内容
We introduce iFlyBot-VLA, a large-scale Vision-Language-Action (VLA) model trained under a novel framework. The main contributions are listed as follows: (1) a latent action model thoroughly trained on large-scale human and robotic manipulation videos; (2) a dual-level action representation framework that jointly supervises both the Vision-Language Model (VLM) and the action expert during training; (3) a mixed training strategy that combines robot trajectory data with general QA and spatial QA datasets, effectively enhancing the 3D perceptual and reasoning capabilities of the VLM backbone. Specifically, the VLM is trained to predict two complementary forms of actions: latent actions, derived from our latent action model pretrained on cross-embodiment manipulation data, which capture implicit high-level intentions; and structured discrete action tokens, obtained through frequency-domain transformations of continuous control signals, which encode explicit low-level dynamics. This dual supervision aligns the representation spaces of language, vision, and action, enabling the VLM to directly contribute to action generation. Experimental results on the LIBERO Franka benchmark demonstrate the superiority of our frame-work, while real-world evaluations further show that iFlyBot-VLA achieves competitive success rates across diverse and challenging manipulation tasks. Furthermore, we plan to open-source a portion of our self-constructed dataset to support future research in the community

## 参考
- http://arxiv.org/abs/2511.01914v1

## Overview
We introduce iFlyBot-VLA, a large-scale Vision-Language-Action (VLA) model trained under a novel framework. The main contributions are listed as follows: (1) a latent action model thoroughly trained on large-scale human and robotic manipulation videos; (2) a dual-level action representation framework that jointly supervises both the Vision-Language Model (VLM) and the action expert during training; (3) a mixed training strategy that combines robot trajectory data with general QA and spatial QA datasets, effectively enhancing the 3D perceptual and reasoning capabilities of the VLM backbone. Specifically, the VLM is trained to predict two complementary forms of actions: latent actions, derived from our latent action model pretrained on cross-embodiment manipulation data, which capture implicit high-level intentions; and structured discrete action tokens, obtained through frequency-domain transformations of continuous control signals, which encode explicit low-level dynamics. This dual supervision aligns the representation spaces of language, vision, and action, enabling the VLM to directly contribute to action generation. Experimental results on the LIBERO Franka benchmark demonstrate the superiority of our framework, while real-world evaluations further show that iFlyBot-VLA achieves competitive success rates across diverse and challenging manipulation tasks. Furthermore, we plan to open-source a portion of our self-constructed dataset to support future research in the community.

## Content
We introduce iFlyBot-VLA, a large-scale Vision-Language-Action (VLA) model trained under a novel framework. The main contributions are listed as follows: (1) a latent action model thoroughly trained on large-scale human and robotic manipulation videos; (2) a dual-level action representation framework that jointly supervises both the Vision-Language Model (VLM) and the action expert during training; (3) a mixed training strategy that combines robot trajectory data with general QA and spatial QA datasets, effectively enhancing the 3D perceptual and reasoning capabilities of the VLM backbone. Specifically, the VLM is trained to predict two complementary forms of actions: latent actions, derived from our latent action model pretrained on cross-embodiment manipulation data, which capture implicit high-level intentions; and structured discrete action tokens, obtained through frequency-domain transformations of continuous control signals, which encode explicit low-level dynamics. This dual supervision aligns the representation spaces of language, vision, and action, enabling the VLM to directly contribute to action generation. Experimental results on the LIBERO Franka benchmark demonstrate the superiority of our framework, while real-world evaluations further show that iFlyBot-VLA achieves competitive success rates across diverse and challenging manipulation tasks. Furthermore, we plan to open-source a portion of our self-constructed dataset to support future research in the community.

## 개요
우리는 새로운 프레임워크 하에서 훈련된 대규모 Vision-Language-Action(VLA) 모델인 iFlyBot-VLA를 소개합니다. 주요 기여 사항은 다음과 같습니다: (1) 대규모 인간 및 로봇 조작 비디오를 통해 철저히 훈련된 잠재 행동 모델; (2) 훈련 중 Vision-Language Model(VLM)과 행동 전문가를 공동으로 감독하는 이중 수준 행동 표현 프레임워크; (3) 로봇 궤적 데이터를 일반 QA 및 공간 QA 데이터셋과 결합하여 VLM 백본의 3D 인식 및 추론 능력을 효과적으로 향상시키는 혼합 훈련 전략. 구체적으로, VLM은 두 가지 상호 보완적인 형태의 행동을 예측하도록 훈련됩니다: 교차 체현 조작 데이터에서 사전 훈련된 잠재 행동 모델에서 파생되어 암시적인 고수준 의도를 포착하는 잠재 행동; 그리고 연속 제어 신호의 주파수 영역 변환을 통해 얻어져 명시적인 저수준 역학을 인코딩하는 구조화된 이산 행동 토큰. 이 이중 감독은 언어, 시각 및 행동의 표현 공간을 정렬하여 VLM이 행동 생성에 직접 기여할 수 있게 합니다. LIBERO Franka 벤치마크에서의 실험 결과는 우리 프레임워크의 우수성을 입증하며, 실제 환경 평가는 iFlyBot-VLA가 다양하고 도전적인 조작 작업에서 경쟁력 있는 성공률을 달성함을 보여줍니다. 또한, 우리는 커뮤니티의 향후 연구를 지원하기 위해 자체 구축 데이터셋의 일부를 오픈소스로 공개할 계획입니다.

## 핵심 내용
우리는 새로운 프레임워크 하에서 훈련된 대규모 Vision-Language-Action(VLA) 모델인 iFlyBot-VLA를 소개합니다. 주요 기여 사항은 다음과 같습니다: (1) 대규모 인간 및 로봇 조작 비디오를 통해 철저히 훈련된 잠재 행동 모델; (2) 훈련 중 Vision-Language Model(VLM)과 행동 전문가를 공동으로 감독하는 이중 수준 행동 표현 프레임워크; (3) 로봇 궤적 데이터를 일반 QA 및 공간 QA 데이터셋과 결합하여 VLM 백본의 3D 인식 및 추론 능력을 효과적으로 향상시키는 혼합 훈련 전략. 구체적으로, VLM은 두 가지 상호 보완적인 형태의 행동을 예측하도록 훈련됩니다: 교차 체현 조작 데이터에서 사전 훈련된 잠재 행동 모델에서 파생되어 암시적인 고수준 의도를 포착하는 잠재 행동; 그리고 연속 제어 신호의 주파수 영역 변환을 통해 얻어져 명시적인 저수준 역학을 인코딩하는 구조화된 이산 행동 토큰. 이 이중 감독은 언어, 시각 및 행동의 표현 공간을 정렬하여 VLM이 행동 생성에 직접 기여할 수 있게 합니다. LIBERO Franka 벤치마크에서의 실험 결과는 우리 프레임워크의 우수성을 입증하며, 실제 환경 평가는 iFlyBot-VLA가 다양하고 도전적인 조작 작업에서 경쟁력 있는 성공률을 달성함을 보여줍니다. 또한, 우리는 커뮤니티의 향후 연구를 지원하기 위해 자체 구축 데이터셋의 일부를 오픈소스로 공개할 계획입니다.
