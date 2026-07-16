---
$id: ent_paper_chen_unified_diffusion_vla_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process'
  zh: UD-VLA
  ko: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process'
summary:
  en: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (UD-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Westlake University, Zhejiang University,
    Monash University.'
  zh: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (UD-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Westlake University, Zhejiang University,
    Monash University.'
  ko: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (UD-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Westlake University, Zhejiang University,
    Monash University.'
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
- ud_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01718v2.
sources:
- id: src_001
  type: paper
  title: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (arXiv)'
  url: https://arxiv.org/abs/2511.01718
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UD-VLA source
  url: https://doi.org/10.48550/arXiv.2511.01718
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models aim to understand natural language instructions and visual observations and to execute corresponding actions as an embodied agent. Recent work integrates future images into the understanding-acting loop, yielding unified VLAs that jointly understand, generate, and act -- reading text and images and producing future images and actions. However, these models either rely on external experts for modality unification or treat image generation and action prediction as separate processes, limiting the benefits of direct synergy between these tasks. Our core philosophy is to optimize generation and action jointly through a synchronous denoising process, where the iterative refinement enables actions to evolve from initialization, under constant and sufficient visual guidance. We ground this philosophy in our proposed Unified Diffusion VLA and Joint Discrete Denoising Diffusion Process (JD3P), which is a joint diffusion process that integrates multiple modalities into a single denoising trajectory to serve as the key mechanism enabling understanding, generation, and acting to be intrinsically synergistic. Our model and theory are built on a unified tokenized space of all modalities and a hybrid attention mechanism. We further propose a two-stage training pipeline and several inference-time techniques that optimize performance and efficiency. Our approach achieves state-of-the-art performance on benchmarks such as CALVIN, LIBERO, and SimplerEnv with 4$\times$ faster inference than autoregressive methods, and we demonstrate its effectiveness through in-depth analysis and real-world evaluations. Our project page is available at https://irpn-eai.github.io/UD-VLA.github.io/.

## 核心内容
Vision-language-action (VLA) models aim to understand natural language instructions and visual observations and to execute corresponding actions as an embodied agent. Recent work integrates future images into the understanding-acting loop, yielding unified VLAs that jointly understand, generate, and act -- reading text and images and producing future images and actions. However, these models either rely on external experts for modality unification or treat image generation and action prediction as separate processes, limiting the benefits of direct synergy between these tasks. Our core philosophy is to optimize generation and action jointly through a synchronous denoising process, where the iterative refinement enables actions to evolve from initialization, under constant and sufficient visual guidance. We ground this philosophy in our proposed Unified Diffusion VLA and Joint Discrete Denoising Diffusion Process (JD3P), which is a joint diffusion process that integrates multiple modalities into a single denoising trajectory to serve as the key mechanism enabling understanding, generation, and acting to be intrinsically synergistic. Our model and theory are built on a unified tokenized space of all modalities and a hybrid attention mechanism. We further propose a two-stage training pipeline and several inference-time techniques that optimize performance and efficiency. Our approach achieves state-of-the-art performance on benchmarks such as CALVIN, LIBERO, and SimplerEnv with 4$\times$ faster inference than autoregressive methods, and we demonstrate its effectiveness through in-depth analysis and real-world evaluations. Our project page is available at https://irpn-eai.github.io/UD-VLA.github.io/.

## 参考
- http://arxiv.org/abs/2511.01718v2

## Overview
Vision-language-action (VLA) models aim to understand natural language instructions and visual observations and to execute corresponding actions as an embodied agent. Recent work integrates future images into the understanding-acting loop, yielding unified VLAs that jointly understand, generate, and act -- reading text and images and producing future images and actions. However, these models either rely on external experts for modality unification or treat image generation and action prediction as separate processes, limiting the benefits of direct synergy between these tasks. Our core philosophy is to optimize generation and action jointly through a synchronous denoising process, where the iterative refinement enables actions to evolve from initialization, under constant and sufficient visual guidance. We ground this philosophy in our proposed Unified Diffusion VLA and Joint Discrete Denoising Diffusion Process (JD3P), which is a joint diffusion process that integrates multiple modalities into a single denoising trajectory to serve as the key mechanism enabling understanding, generation, and acting to be intrinsically synergistic. Our model and theory are built on a unified tokenized space of all modalities and a hybrid attention mechanism. We further propose a two-stage training pipeline and several inference-time techniques that optimize performance and efficiency. Our approach achieves state-of-the-art performance on benchmarks such as CALVIN, LIBERO, and SimplerEnv with 4$\times$ faster inference than autoregressive methods, and we demonstrate its effectiveness through in-depth analysis and real-world evaluations. Our project page is available at https://irpn-eai.github.io/UD-VLA.github.io/.

## Content
Vision-language-action (VLA) models aim to understand natural language instructions and visual observations and to execute corresponding actions as an embodied agent. Recent work integrates future images into the understanding-acting loop, yielding unified VLAs that jointly understand, generate, and act -- reading text and images and producing future images and actions. However, these models either rely on external experts for modality unification or treat image generation and action prediction as separate processes, limiting the benefits of direct synergy between these tasks. Our core philosophy is to optimize generation and action jointly through a synchronous denoising process, where the iterative refinement enables actions to evolve from initialization, under constant and sufficient visual guidance. We ground this philosophy in our proposed Unified Diffusion VLA and Joint Discrete Denoising Diffusion Process (JD3P), which is a joint diffusion process that integrates multiple modalities into a single denoising trajectory to serve as the key mechanism enabling understanding, generation, and acting to be intrinsically synergistic. Our model and theory are built on a unified tokenized space of all modalities and a hybrid attention mechanism. We further propose a two-stage training pipeline and several inference-time techniques that optimize performance and efficiency. Our approach achieves state-of-the-art performance on benchmarks such as CALVIN, LIBERO, and SimplerEnv with 4$\times$ faster inference than autoregressive methods, and we demonstrate its effectiveness through in-depth analysis and real-world evaluations. Our project page is available at https://irpn-eai.github.io/UD-VLA.github.io/.

## 개요
Vision-language-action (VLA) 모델은 자연어 명령과 시각적 관찰을 이해하고, 구현된 에이전트로서 해당 행동을 실행하는 것을 목표로 합니다. 최근 연구는 미래 이미지를 이해-행동 루프에 통합하여 텍스트와 이미지를 읽고 미래 이미지와 행동을 생성하는, 이해, 생성, 행동을 공동으로 수행하는 통합 VLA를 도출했습니다. 그러나 이러한 모델은 모달리티 통합을 위해 외부 전문가에 의존하거나 이미지 생성과 행동 예측을 별도의 프로세스로 처리하여, 이러한 작업 간의 직접적인 시너지 효과를 제한합니다. 우리의 핵심 철학은 동기식 잡음 제거 프로세스를 통해 생성과 행동을 공동으로 최적화하는 것이며, 반복적 정제를 통해 행동이 초기화 상태에서 지속적이고 충분한 시각적 안내 하에 진화할 수 있도록 하는 것입니다. 우리는 이 철학을 제안된 Unified Diffusion VLA 및 Joint Discrete Denoising Diffusion Process (JD3P)에 기반을 두고 있으며, 이는 여러 모달리티를 단일 잡음 제거 궤적으로 통합하여 이해, 생성, 행동이 본질적으로 시너지 효과를 발휘할 수 있도록 하는 핵심 메커니즘 역할을 합니다. 우리의 모델과 이론은 모든 모달리티의 통합 토큰화 공간과 하이브리드 어텐션 메커니즘을 기반으로 구축되었습니다. 또한 성능과 효율성을 최적화하는 2단계 훈련 파이프라인과 여러 추론 시간 기술을 제안합니다. 우리의 접근 방식은 CALVIN, LIBERO, SimplerEnv와 같은 벤치마크에서 최첨단 성능을 달성하며, 자기회귀 방법보다 4배 빠른 추론 속도를 보여주고, 심층 분석 및 실제 환경 평가를 통해 그 효과를 입증합니다. 프로젝트 페이지는 https://irpn-eai.github.io/UD-VLA.github.io/에서 확인할 수 있습니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 자연어 명령과 시각적 관찰을 이해하고, 구현된 에이전트로서 해당 행동을 실행하는 것을 목표로 합니다. 최근 연구는 미래 이미지를 이해-행동 루프에 통합하여 텍스트와 이미지를 읽고 미래 이미지와 행동을 생성하는, 이해, 생성, 행동을 공동으로 수행하는 통합 VLA를 도출했습니다. 그러나 이러한 모델은 모달리티 통합을 위해 외부 전문가에 의존하거나 이미지 생성과 행동 예측을 별도의 프로세스로 처리하여, 이러한 작업 간의 직접적인 시너지 효과를 제한합니다. 우리의 핵심 철학은 동기식 잡음 제거 프로세스를 통해 생성과 행동을 공동으로 최적화하는 것이며, 반복적 정제를 통해 행동이 초기화 상태에서 지속적이고 충분한 시각적 안내 하에 진화할 수 있도록 하는 것입니다. 우리는 이 철학을 제안된 Unified Diffusion VLA 및 Joint Discrete Denoising Diffusion Process (JD3P)에 기반을 두고 있으며, 이는 여러 모달리티를 단일 잡음 제거 궤적으로 통합하여 이해, 생성, 행동이 본질적으로 시너지 효과를 발휘할 수 있도록 하는 핵심 메커니즘 역할을 합니다. 우리의 모델과 이론은 모든 모달리티의 통합 토큰화 공간과 하이브리드 어텐션 메커니즘을 기반으로 구축되었습니다. 또한 성능과 효율성을 최적화하는 2단계 훈련 파이프라인과 여러 추론 시간 기술을 제안합니다. 우리의 접근 방식은 CALVIN, LIBERO, SimplerEnv와 같은 벤치마크에서 최첨단 성능을 달성하며, 자기회귀 방법보다 4배 빠른 추론 속도를 보여주고, 심층 분석 및 실제 환경 평가를 통해 그 효과를 입증합니다. 프로젝트 페이지는 https://irpn-eai.github.io/UD-VLA.github.io/에서 확인할 수 있습니다.
