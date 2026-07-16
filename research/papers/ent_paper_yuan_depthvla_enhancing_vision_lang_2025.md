---
$id: ent_paper_yuan_depthvla_enhancing_vision_lang_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning'
  zh: DepthVLA
  ko: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning'
summary:
  en: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (DepthVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Galaxea AI.'
  zh: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (DepthVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Galaxea AI.'
  ko: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (DepthVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Galaxea AI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- depthvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.13375v1.
sources:
- id: src_001
  type: paper
  title: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (arXiv)'
  url: https://arxiv.org/abs/2510.13375
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DepthVLA source
  url: https://doi.org/10.48550/arXiv.2510.13375
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently shown impressive generalization and language-guided manipulation capabilities. However, their performance degrades on tasks requiring precise spatial reasoning due to limited spatial reasoning inherited from Vision-Language Models (VLMs). Existing VLAs rely on extensive action-data pretraining to ground VLMs in 3D space, which reduces training efficiency and is still insufficient for accurate spatial understanding. In this work, we present DepthVLA, a simple yet effective VLA architecture that explicitly incorporates spatial awareness through a pretrained depth prediction module. DepthVLA adopts a mixture-of-transformers design that unifies a VLM, a depth transformer, and an action expert with fully shared attentions, forming an end-to-end model with enhanced spatial reasoning. Extensive evaluations in both real-world and simulated environments show that DepthVLA outperforms state-of-the-art approaches, achieving 78.5% vs. 65.0% progress in real-world tasks, 94.9% vs. 93.6% in the LIBERO simulator, and 74.8% vs. 58.8% in the Simpler simulator. Our code will be made publicly available.

## 核心内容
Vision-Language-Action (VLA) models have recently shown impressive generalization and language-guided manipulation capabilities. However, their performance degrades on tasks requiring precise spatial reasoning due to limited spatial reasoning inherited from Vision-Language Models (VLMs). Existing VLAs rely on extensive action-data pretraining to ground VLMs in 3D space, which reduces training efficiency and is still insufficient for accurate spatial understanding. In this work, we present DepthVLA, a simple yet effective VLA architecture that explicitly incorporates spatial awareness through a pretrained depth prediction module. DepthVLA adopts a mixture-of-transformers design that unifies a VLM, a depth transformer, and an action expert with fully shared attentions, forming an end-to-end model with enhanced spatial reasoning. Extensive evaluations in both real-world and simulated environments show that DepthVLA outperforms state-of-the-art approaches, achieving 78.5% vs. 65.0% progress in real-world tasks, 94.9% vs. 93.6% in the LIBERO simulator, and 74.8% vs. 58.8% in the Simpler simulator. Our code will be made publicly available.

## 参考
- http://arxiv.org/abs/2510.13375v1

## Overview
Vision-Language-Action (VLA) models have recently shown impressive generalization and language-guided manipulation capabilities. However, their performance degrades on tasks requiring precise spatial reasoning due to limited spatial reasoning inherited from Vision-Language Models (VLMs). Existing VLAs rely on extensive action-data pretraining to ground VLMs in 3D space, which reduces training efficiency and is still insufficient for accurate spatial understanding. In this work, we present DepthVLA, a simple yet effective VLA architecture that explicitly incorporates spatial awareness through a pretrained depth prediction module. DepthVLA adopts a mixture-of-transformers design that unifies a VLM, a depth transformer, and an action expert with fully shared attentions, forming an end-to-end model with enhanced spatial reasoning. Extensive evaluations in both real-world and simulated environments show that DepthVLA outperforms state-of-the-art approaches, achieving 78.5% vs. 65.0% progress in real-world tasks, 94.9% vs. 93.6% in the LIBERO simulator, and 74.8% vs. 58.8% in the Simpler simulator. Our code will be made publicly available.

## Content
Vision-Language-Action (VLA) models have recently shown impressive generalization and language-guided manipulation capabilities. However, their performance degrades on tasks requiring precise spatial reasoning due to limited spatial reasoning inherited from Vision-Language Models (VLMs). Existing VLAs rely on extensive action-data pretraining to ground VLMs in 3D space, which reduces training efficiency and is still insufficient for accurate spatial understanding. In this work, we present DepthVLA, a simple yet effective VLA architecture that explicitly incorporates spatial awareness through a pretrained depth prediction module. DepthVLA adopts a mixture-of-transformers design that unifies a VLM, a depth transformer, and an action expert with fully shared attentions, forming an end-to-end model with enhanced spatial reasoning. Extensive evaluations in both real-world and simulated environments show that DepthVLA outperforms state-of-the-art approaches, achieving 78.5% vs. 65.0% progress in real-world tasks, 94.9% vs. 93.6% in the LIBERO simulator, and 74.8% vs. 58.8% in the Simpler simulator. Our code will be made publicly available.

## 개요
Vision-Language-Action (VLA) 모델은 최근 인상적인 일반화 능력과 언어 기반 조작 능력을 보여주고 있습니다. 그러나 Vision-Language Models (VLM)로부터 물려받은 제한된 공간 추론 능력으로 인해 정밀한 공간 추론이 필요한 작업에서는 성능이 저하됩니다. 기존 VLA는 VLM을 3D 공간에 정착시키기 위해 방대한 행동 데이터 사전 학습에 의존하는데, 이는 훈련 효율성을 떨어뜨릴 뿐만 아니라 정확한 공간 이해에도 여전히 부족합니다. 본 연구에서는 사전 학습된 깊이 예측 모듈을 통해 공간 인식을 명시적으로 통합하는 간단하면서도 효과적인 VLA 아키텍처인 DepthVLA를 제시합니다. DepthVLA는 VLM, 깊이 트랜스포머, 행동 전문가를 완전히 공유된 어텐션으로 통합하는 mixture-of-transformers 설계를 채택하여 향상된 공간 추론 능력을 갖춘 종단간 모델을 형성합니다. 실제 환경과 시뮬레이션 환경 모두에서의 광범위한 평가 결과, DepthVLA는 최첨단 접근법을 능가하여 실제 작업에서 78.5% 대 65.0%, LIBERO 시뮬레이터에서 94.9% 대 93.6%, Simpler 시뮬레이터에서 74.8% 대 58.8%의 진전을 달성했습니다. 본 코드는 공개될 예정입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 최근 인상적인 일반화 능력과 언어 기반 조작 능력을 보여주고 있습니다. 그러나 Vision-Language Models (VLM)로부터 물려받은 제한된 공간 추론 능력으로 인해 정밀한 공간 추론이 필요한 작업에서는 성능이 저하됩니다. 기존 VLA는 VLM을 3D 공간에 정착시키기 위해 방대한 행동 데이터 사전 학습에 의존하는데, 이는 훈련 효율성을 떨어뜨릴 뿐만 아니라 정확한 공간 이해에도 여전히 부족합니다. 본 연구에서는 사전 학습된 깊이 예측 모듈을 통해 공간 인식을 명시적으로 통합하는 간단하면서도 효과적인 VLA 아키텍처인 DepthVLA를 제시합니다. DepthVLA는 VLM, 깊이 트랜스포머, 행동 전문가를 완전히 공유된 어텐션으로 통합하는 mixture-of-transformers 설계를 채택하여 향상된 공간 추론 능력을 갖춘 종단간 모델을 형성합니다. 실제 환경과 시뮬레이션 환경 모두에서의 광범위한 평가 결과, DepthVLA는 최첨단 접근법을 능가하여 실제 작업에서 78.5% 대 65.0%, LIBERO 시뮬레이터에서 94.9% 대 93.6%, Simpler 시뮬레이터에서 74.8% 대 58.8%의 진전을 달성했습니다. 본 코드는 공개될 예정입니다.
