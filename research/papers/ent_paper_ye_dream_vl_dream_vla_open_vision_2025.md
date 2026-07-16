---
$id: ent_paper_ye_dream_vl_dream_vla_open_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone'
  zh: Dream-VLA
  ko: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone'
summary:
  en: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone
    (Dream-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Hong
    Kong.'
  zh: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone
    (Dream-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Hong
    Kong.'
  ko: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone
    (Dream-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Hong
    Kong.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dream_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22615v2.
sources:
- id: src_001
  type: paper
  title: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone
    (arXiv)'
  url: https://arxiv.org/abs/2512.22615
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Dream-VLA source
  url: https://doi.org/10.48550/arXiv.2512.22615
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While autoregressive Large Vision-Language Models (VLMs) have achieved remarkable success, their sequential generation often limits their efficacy in complex visual planning and dynamic robotic control. In this work, we investigate the potential of constructing Vision-Language Models upon diffusion-based large language models (dLLMs) to overcome these limitations. We introduce Dream-VL, an open diffusion-based VLM (dVLM) that achieves state-of-the-art performance among previous dVLMs. Dream-VL is comparable to top-tier AR-based VLMs trained on open data on various benchmarks but exhibits superior potential when applied to visual planning tasks. Building upon Dream-VL, we introduce Dream-VLA, a dLLM-based Vision-Language-Action model (dVLA) developed through continuous pre-training on open robotic datasets. We demonstrate that the natively bidirectional nature of this diffusion backbone serves as a superior foundation for VLA tasks, inherently suited for action chunking and parallel generation, leading to significantly faster convergence in downstream fine-tuning. Dream-VLA achieves top-tier performance of 97.2% average success rate on LIBERO, 71.4% overall average on SimplerEnv-Bridge, and 60.5% overall average on SimplerEnv-Fractal, surpassing leading models such as $π_0$ and GR00T-N1. We also validate that dVLMs surpass AR baselines on downstream tasks across different training objectives. We release both Dream-VL and Dream-VLA to facilitate further research in the community.

## 核心内容
While autoregressive Large Vision-Language Models (VLMs) have achieved remarkable success, their sequential generation often limits their efficacy in complex visual planning and dynamic robotic control. In this work, we investigate the potential of constructing Vision-Language Models upon diffusion-based large language models (dLLMs) to overcome these limitations. We introduce Dream-VL, an open diffusion-based VLM (dVLM) that achieves state-of-the-art performance among previous dVLMs. Dream-VL is comparable to top-tier AR-based VLMs trained on open data on various benchmarks but exhibits superior potential when applied to visual planning tasks. Building upon Dream-VL, we introduce Dream-VLA, a dLLM-based Vision-Language-Action model (dVLA) developed through continuous pre-training on open robotic datasets. We demonstrate that the natively bidirectional nature of this diffusion backbone serves as a superior foundation for VLA tasks, inherently suited for action chunking and parallel generation, leading to significantly faster convergence in downstream fine-tuning. Dream-VLA achieves top-tier performance of 97.2% average success rate on LIBERO, 71.4% overall average on SimplerEnv-Bridge, and 60.5% overall average on SimplerEnv-Fractal, surpassing leading models such as $π_0$ and GR00T-N1. We also validate that dVLMs surpass AR baselines on downstream tasks across different training objectives. We release both Dream-VL and Dream-VLA to facilitate further research in the community.

## 参考
- http://arxiv.org/abs/2512.22615v2

## Overview
While autoregressive Large Vision-Language Models (VLMs) have achieved remarkable success, their sequential generation often limits their efficacy in complex visual planning and dynamic robotic control. In this work, we investigate the potential of constructing Vision-Language Models upon diffusion-based large language models (dLLMs) to overcome these limitations. We introduce Dream-VL, an open diffusion-based VLM (dVLM) that achieves state-of-the-art performance among previous dVLMs. Dream-VL is comparable to top-tier AR-based VLMs trained on open data on various benchmarks but exhibits superior potential when applied to visual planning tasks. Building upon Dream-VL, we introduce Dream-VLA, a dLLM-based Vision-Language-Action model (dVLA) developed through continuous pre-training on open robotic datasets. We demonstrate that the natively bidirectional nature of this diffusion backbone serves as a superior foundation for VLA tasks, inherently suited for action chunking and parallel generation, leading to significantly faster convergence in downstream fine-tuning. Dream-VLA achieves top-tier performance of 97.2% average success rate on LIBERO, 71.4% overall average on SimplerEnv-Bridge, and 60.5% overall average on SimplerEnv-Fractal, surpassing leading models such as $π_0$ and GR00T-N1. We also validate that dVLMs surpass AR baselines on downstream tasks across different training objectives. We release both Dream-VL and Dream-VLA to facilitate further research in the community.

## Content
While autoregressive Large Vision-Language Models (VLMs) have achieved remarkable success, their sequential generation often limits their efficacy in complex visual planning and dynamic robotic control. In this work, we investigate the potential of constructing Vision-Language Models upon diffusion-based large language models (dLLMs) to overcome these limitations. We introduce Dream-VL, an open diffusion-based VLM (dVLM) that achieves state-of-the-art performance among previous dVLMs. Dream-VL is comparable to top-tier AR-based VLMs trained on open data on various benchmarks but exhibits superior potential when applied to visual planning tasks. Building upon Dream-VL, we introduce Dream-VLA, a dLLM-based Vision-Language-Action model (dVLA) developed through continuous pre-training on open robotic datasets. We demonstrate that the natively bidirectional nature of this diffusion backbone serves as a superior foundation for VLA tasks, inherently suited for action chunking and parallel generation, leading to significantly faster convergence in downstream fine-tuning. Dream-VLA achieves top-tier performance of 97.2% average success rate on LIBERO, 71.4% overall average on SimplerEnv-Bridge, and 60.5% overall average on SimplerEnv-Fractal, surpassing leading models such as $π_0$ and GR00T-N1. We also validate that dVLMs surpass AR baselines on downstream tasks across different training objectives. We release both Dream-VL and Dream-VLA to facilitate further research in the community.

## 개요
자기회귀적 대규모 시각-언어 모델(VLM)은 놀라운 성공을 거두었지만, 순차적 생성 방식은 복잡한 시각적 계획 및 동적 로봇 제어에서 그 효용성을 종종 제한합니다. 본 연구에서는 이러한 한계를 극복하기 위해 확산 기반 대규모 언어 모델(dLLM) 위에 시각-언어 모델을 구축할 가능성을 탐구합니다. 우리는 이전 dVLM 중 최첨단 성능을 달성한 오픈 확산 기반 VLM(dVLM)인 Dream-VL을 소개합니다. Dream-VL은 공개 데이터로 학습된 최고 수준의 AR 기반 VLM과 다양한 벤치마크에서 견줄 만하지만, 시각적 계획 작업에 적용될 때 우수한 잠재력을 보여줍니다. Dream-VL을 기반으로, 우리는 공개 로봇 데이터셋에 대한 지속적인 사전 학습을 통해 개발된 dLLM 기반 시각-언어-행동 모델(dVLA)인 Dream-VLA를 소개합니다. 우리는 이 확산 백본의 본질적으로 양방향적인 특성이 VLA 작업에 탁월한 기반을 제공하며, 액션 청킹 및 병렬 생성에 본질적으로 적합하여 하위 작업 미세 조정에서 훨씬 빠른 수렴을 이끌어낸다는 것을 입증합니다. Dream-VLA는 LIBERO에서 97.2%의 평균 성공률, SimplerEnv-Bridge에서 71.4%의 전체 평균, SimplerEnv-Fractal에서 60.5%의 전체 평균을 달성하여 $π_0$ 및 GR00T-N1과 같은 선도 모델을 능가합니다. 또한 dVLM이 다양한 학습 목표에 걸쳐 하위 작업에서 AR 기준선을 능가한다는 것을 검증합니다. 우리는 커뮤니티의 추가 연구를 촉진하기 위해 Dream-VL과 Dream-VLA를 모두 공개합니다.

## 핵심 내용
자기회귀적 대규모 시각-언어 모델(VLM)은 놀라운 성공을 거두었지만, 순차적 생성 방식은 복잡한 시각적 계획 및 동적 로봇 제어에서 그 효용성을 종종 제한합니다. 본 연구에서는 이러한 한계를 극복하기 위해 확산 기반 대규모 언어 모델(dLLM) 위에 시각-언어 모델을 구축할 가능성을 탐구합니다. 우리는 이전 dVLM 중 최첨단 성능을 달성한 오픈 확산 기반 VLM(dVLM)인 Dream-VL을 소개합니다. Dream-VL은 공개 데이터로 학습된 최고 수준의 AR 기반 VLM과 다양한 벤치마크에서 견줄 만하지만, 시각적 계획 작업에 적용될 때 우수한 잠재력을 보여줍니다. Dream-VL을 기반으로, 우리는 공개 로봇 데이터셋에 대한 지속적인 사전 학습을 통해 개발된 dLLM 기반 시각-언어-행동 모델(dVLA)인 Dream-VLA를 소개합니다. 우리는 이 확산 백본의 본질적으로 양방향적인 특성이 VLA 작업에 탁월한 기반을 제공하며, 액션 청킹 및 병렬 생성에 본질적으로 적합하여 하위 작업 미세 조정에서 훨씬 빠른 수렴을 이끌어낸다는 것을 입증합니다. Dream-VLA는 LIBERO에서 97.2%의 평균 성공률, SimplerEnv-Bridge에서 71.4%의 전체 평균, SimplerEnv-Fractal에서 60.5%의 전체 평균을 달성하여 $π_0$ 및 GR00T-N1과 같은 선도 모델을 능가합니다. 또한 dVLM이 다양한 학습 목표에 걸쳐 하위 작업에서 AR 기준선을 능가한다는 것을 검증합니다. 우리는 커뮤니티의 추가 연구를 촉진하기 위해 Dream-VL과 Dream-VLA를 모두 공개합니다.
