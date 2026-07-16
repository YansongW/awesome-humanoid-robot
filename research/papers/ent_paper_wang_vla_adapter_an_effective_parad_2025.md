---
$id: ent_paper_wang_vla_adapter_an_effective_parad_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model'
  zh: VLA-Adapter
  ko: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model'
summary:
  en: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (VLA-Adapter), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications, Westlake University,
    Zhejiang University, OpenHelix Team, State Key Laboratory of Networking and Switching Technology, The Hong Kong University
    of Science and Technology (Guangzhou).'
  zh: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (VLA-Adapter), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications, Westlake University,
    Zhejiang University, OpenHelix Team, State Key Laboratory of Networking and Switching Technology, The Hong Kong University
    of Science and Technology (Guangzhou).'
  ko: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (VLA-Adapter), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications, Westlake University,
    Zhejiang University, OpenHelix Team, State Key Laboratory of Networking and Switching Technology, The Hong Kong University
    of Science and Technology (Guangzhou).'
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
- vision_language_action
- vla
- vla_adapter
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09372v2.
sources:
- id: src_001
  type: paper
  title: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2509.09372
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Adapter source
  url: https://doi.org/10.48550/arXiv.2509.09372
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models typically bridge the gap between perceptual and action spaces by pre-training a large-scale Vision-Language Model (VLM) on robotic data. While this approach greatly enhances performance, it also incurs significant training costs. In this paper, we investigate how to effectively bridge vision-language (VL) representations to action (A). We introduce VLA-Adapter, a novel paradigm designed to reduce the reliance of VLA models on large-scale VLMs and extensive pre-training. To this end, we first systematically analyze the effectiveness of various VL conditions and present key findings on which conditions are essential for bridging perception and action spaces. Based on these insights, we propose a lightweight Policy module with Bridge Attention, which autonomously injects the optimal condition into the action space. In this way, our method achieves high performance using only a 0.5B-parameter backbone, without any robotic data pre-training. Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that VLA-Adapter not only achieves state-of-the-art level performance, but also offers the fast inference speed reported to date. Furthermore, thanks to the proposed advanced bridging paradigm, VLA-Adapter enables the training of a powerful VLA model in just 8 hours on a single consumer-grade GPU, greatly lowering the barrier to deploying the VLA model. Project page: https://vla-adapter.github.io/.

## 核心内容
Vision-Language-Action (VLA) models typically bridge the gap between perceptual and action spaces by pre-training a large-scale Vision-Language Model (VLM) on robotic data. While this approach greatly enhances performance, it also incurs significant training costs. In this paper, we investigate how to effectively bridge vision-language (VL) representations to action (A). We introduce VLA-Adapter, a novel paradigm designed to reduce the reliance of VLA models on large-scale VLMs and extensive pre-training. To this end, we first systematically analyze the effectiveness of various VL conditions and present key findings on which conditions are essential for bridging perception and action spaces. Based on these insights, we propose a lightweight Policy module with Bridge Attention, which autonomously injects the optimal condition into the action space. In this way, our method achieves high performance using only a 0.5B-parameter backbone, without any robotic data pre-training. Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that VLA-Adapter not only achieves state-of-the-art level performance, but also offers the fast inference speed reported to date. Furthermore, thanks to the proposed advanced bridging paradigm, VLA-Adapter enables the training of a powerful VLA model in just 8 hours on a single consumer-grade GPU, greatly lowering the barrier to deploying the VLA model. Project page: https://vla-adapter.github.io/.

## 参考
- http://arxiv.org/abs/2509.09372v2

## Overview
Vision-Language-Action (VLA) models typically bridge the gap between perceptual and action spaces by pre-training a large-scale Vision-Language Model (VLM) on robotic data. While this approach greatly enhances performance, it also incurs significant training costs. In this paper, we investigate how to effectively bridge vision-language (VL) representations to action (A). We introduce VLA-Adapter, a novel paradigm designed to reduce the reliance of VLA models on large-scale VLMs and extensive pre-training. To this end, we first systematically analyze the effectiveness of various VL conditions and present key findings on which conditions are essential for bridging perception and action spaces. Based on these insights, we propose a lightweight Policy module with Bridge Attention, which autonomously injects the optimal condition into the action space. In this way, our method achieves high performance using only a 0.5B-parameter backbone, without any robotic data pre-training. Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that VLA-Adapter not only achieves state-of-the-art level performance, but also offers the fast inference speed reported to date. Furthermore, thanks to the proposed advanced bridging paradigm, VLA-Adapter enables the training of a powerful VLA model in just 8 hours on a single consumer-grade GPU, greatly lowering the barrier to deploying the VLA model. Project page: https://vla-adapter.github.io/.

## Content
Vision-Language-Action (VLA) models typically bridge the gap between perceptual and action spaces by pre-training a large-scale Vision-Language Model (VLM) on robotic data. While this approach greatly enhances performance, it also incurs significant training costs. In this paper, we investigate how to effectively bridge vision-language (VL) representations to action (A). We introduce VLA-Adapter, a novel paradigm designed to reduce the reliance of VLA models on large-scale VLMs and extensive pre-training. To this end, we first systematically analyze the effectiveness of various VL conditions and present key findings on which conditions are essential for bridging perception and action spaces. Based on these insights, we propose a lightweight Policy module with Bridge Attention, which autonomously injects the optimal condition into the action space. In this way, our method achieves high performance using only a 0.5B-parameter backbone, without any robotic data pre-training. Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that VLA-Adapter not only achieves state-of-the-art level performance, but also offers the fast inference speed reported to date. Furthermore, thanks to the proposed advanced bridging paradigm, VLA-Adapter enables the training of a powerful VLA model in just 8 hours on a single consumer-grade GPU, greatly lowering the barrier to deploying the VLA model. Project page: https://vla-adapter.github.io/.

## 개요
Vision-Language-Action (VLA) 모델은 일반적으로 로봇 데이터에 대해 대규모 Vision-Language Model (VLM)을 사전 학습하여 지각 공간과 행동 공간 간의 격차를 해소합니다. 이러한 접근 방식은 성능을 크게 향상시키지만, 상당한 학습 비용을 초래합니다. 본 논문에서는 시각-언어(VL) 표현을 행동(A)에 효과적으로 연결하는 방법을 연구합니다. 우리는 VLA 모델이 대규모 VLM 및 광범위한 사전 학습에 의존하는 것을 줄이기 위해 설계된 새로운 패러다임인 VLA-Adapter를 소개합니다. 이를 위해 먼저 다양한 VL 조건의 효과성을 체계적으로 분석하고, 지각 공간과 행동 공간을 연결하는 데 필수적인 조건에 대한 주요 결과를 제시합니다. 이러한 통찰을 바탕으로 Bridge Attention을 갖춘 경량 Policy 모듈을 제안하며, 이는 최적의 조건을 행동 공간에 자율적으로 주입합니다. 이 방식으로 우리의 방법은 0.5B 파라미터 백본만을 사용하여 로봇 데이터 사전 학습 없이도 높은 성능을 달성합니다. 시뮬레이션 및 실제 로봇 벤치마크에 대한 광범위한 실험은 VLA-Adapter가 최첨단 수준의 성능을 달성할 뿐만 아니라 현재까지 보고된 가장 빠른 추론 속도를 제공함을 보여줍니다. 또한, 제안된 고급 연결 패러다임 덕분에 VLA-Adapter는 단일 소비자용 GPU에서 단 8시간 만에 강력한 VLA 모델 학습을 가능하게 하여 VLA 모델 배포의 장벽을 크게 낮춥니다. 프로젝트 페이지: https://vla-adapter.github.io/.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 일반적으로 로봇 데이터에 대해 대규모 Vision-Language Model (VLM)을 사전 학습하여 지각 공간과 행동 공간 간의 격차를 해소합니다. 이러한 접근 방식은 성능을 크게 향상시키지만, 상당한 학습 비용을 초래합니다. 본 논문에서는 시각-언어(VL) 표현을 행동(A)에 효과적으로 연결하는 방법을 연구합니다. 우리는 VLA 모델이 대규모 VLM 및 광범위한 사전 학습에 의존하는 것을 줄이기 위해 설계된 새로운 패러다임인 VLA-Adapter를 소개합니다. 이를 위해 먼저 다양한 VL 조건의 효과성을 체계적으로 분석하고, 지각 공간과 행동 공간을 연결하는 데 필수적인 조건에 대한 주요 결과를 제시합니다. 이러한 통찰을 바탕으로 Bridge Attention을 갖춘 경량 Policy 모듈을 제안하며, 이는 최적의 조건을 행동 공간에 자율적으로 주입합니다. 이 방식으로 우리의 방법은 0.5B 파라미터 백본만을 사용하여 로봇 데이터 사전 학습 없이도 높은 성능을 달성합니다. 시뮬레이션 및 실제 로봇 벤치마크에 대한 광범위한 실험은 VLA-Adapter가 최첨단 수준의 성능을 달성할 뿐만 아니라 현재까지 보고된 가장 빠른 추론 속도를 제공함을 보여줍니다. 또한, 제안된 고급 연결 패러다임 덕분에 VLA-Adapter는 단일 소비자용 GPU에서 단 8시간 만에 강력한 VLA 모델 학습을 가능하게 하여 VLA 모델 배포의 장벽을 크게 낮춥니다. 프로젝트 페이지: https://vla-adapter.github.io/.
