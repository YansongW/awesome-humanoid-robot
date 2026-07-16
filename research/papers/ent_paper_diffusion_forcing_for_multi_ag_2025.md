---
$id: ent_paper_diffusion_forcing_for_multi_ag_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
  zh: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
  ko: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
summary:
  en: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
  zh: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
  ko: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_forcing_for_multi_ag
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.17900v2.
sources:
- id: src_001
  type: paper
  title: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling (arXiv)
  url: https://arxiv.org/abs/2512.17900
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Understanding and generating multi-person interactions is a fundamental challenge with broad implications for robotics and social computing. While humans naturally coordinate in groups, modeling such interactions remains difficult due to long temporal horizons, strong inter-agent dependencies, and variable group sizes. Existing motion generation methods are largely task-specific and do not generalize to flexible multi-agent generation. We introduce MAGNet (Multi-Agent Generative Network), a unified autoregressive diffusion framework for multi-agent motion generation that supports a wide range of interaction tasks through flexible conditioning and sampling. MAGNet performs dyadic and polyadic prediction, partner inpainting, partner prediction, and agentic generation all within a single model, and can autoregressively generate ultra-long sequences spanning hundreds of motion steps. We explicitly model inter-agent coupling during autoregressive denoising, enabling coherent coordination across agents. As a result, MAGNet captures both tightly synchronized activities (e.g., dancing, boxing) and loosely structured social interactions. Our approach performs on par with specialized methods on dyadic benchmarks while naturally extending to polyadic scenarios involving three or more interacting people. Please watch the supplemental video, where the temporal dynamics and spatial coordination of generated interactions are best appreciated. Project page: https://von31.github.io/MAGNet/

## 核心内容
Understanding and generating multi-person interactions is a fundamental challenge with broad implications for robotics and social computing. While humans naturally coordinate in groups, modeling such interactions remains difficult due to long temporal horizons, strong inter-agent dependencies, and variable group sizes. Existing motion generation methods are largely task-specific and do not generalize to flexible multi-agent generation. We introduce MAGNet (Multi-Agent Generative Network), a unified autoregressive diffusion framework for multi-agent motion generation that supports a wide range of interaction tasks through flexible conditioning and sampling. MAGNet performs dyadic and polyadic prediction, partner inpainting, partner prediction, and agentic generation all within a single model, and can autoregressively generate ultra-long sequences spanning hundreds of motion steps. We explicitly model inter-agent coupling during autoregressive denoising, enabling coherent coordination across agents. As a result, MAGNet captures both tightly synchronized activities (e.g., dancing, boxing) and loosely structured social interactions. Our approach performs on par with specialized methods on dyadic benchmarks while naturally extending to polyadic scenarios involving three or more interacting people. Please watch the supplemental video, where the temporal dynamics and spatial coordination of generated interactions are best appreciated. Project page: https://von31.github.io/MAGNet/

## 参考
- http://arxiv.org/abs/2512.17900v2

## Overview
Understanding and generating multi-person interactions is a fundamental challenge with broad implications for robotics and social computing. While humans naturally coordinate in groups, modeling such interactions remains difficult due to long temporal horizons, strong inter-agent dependencies, and variable group sizes. Existing motion generation methods are largely task-specific and do not generalize to flexible multi-agent generation. We introduce MAGNet (Multi-Agent Generative Network), a unified autoregressive diffusion framework for multi-agent motion generation that supports a wide range of interaction tasks through flexible conditioning and sampling. MAGNet performs dyadic and polyadic prediction, partner inpainting, partner prediction, and agentic generation all within a single model, and can autoregressively generate ultra-long sequences spanning hundreds of motion steps. We explicitly model inter-agent coupling during autoregressive denoising, enabling coherent coordination across agents. As a result, MAGNet captures both tightly synchronized activities (e.g., dancing, boxing) and loosely structured social interactions. Our approach performs on par with specialized methods on dyadic benchmarks while naturally extending to polyadic scenarios involving three or more interacting people. Please watch the supplemental video, where the temporal dynamics and spatial coordination of generated interactions are best appreciated. Project page: https://von31.github.io/MAGNet/

## Content
Understanding and generating multi-person interactions is a fundamental challenge with broad implications for robotics and social computing. While humans naturally coordinate in groups, modeling such interactions remains difficult due to long temporal horizons, strong inter-agent dependencies, and variable group sizes. Existing motion generation methods are largely task-specific and do not generalize to flexible multi-agent generation. We introduce MAGNet (Multi-Agent Generative Network), a unified autoregressive diffusion framework for multi-agent motion generation that supports a wide range of interaction tasks through flexible conditioning and sampling. MAGNet performs dyadic and polyadic prediction, partner inpainting, partner prediction, and agentic generation all within a single model, and can autoregressively generate ultra-long sequences spanning hundreds of motion steps. We explicitly model inter-agent coupling during autoregressive denoising, enabling coherent coordination across agents. As a result, MAGNet captures both tightly synchronized activities (e.g., dancing, boxing) and loosely structured social interactions. Our approach performs on par with specialized methods on dyadic benchmarks while naturally extending to polyadic scenarios involving three or more interacting people. Please watch the supplemental video, where the temporal dynamics and spatial coordination of generated interactions are best appreciated. Project page: https://von31.github.io/MAGNet/

## 개요
다중 인물 상호작용을 이해하고 생성하는 것은 로보틱스와 사회 컴퓨팅에 광범위한 영향을 미치는 근본적인 도전 과제입니다. 인간은 자연스럽게 그룹으로 협력하지만, 긴 시간적 범위, 강한 에이전트 간 의존성, 그리고 다양한 그룹 크기로 인해 이러한 상호작용을 모델링하는 것은 여전히 어렵습니다. 기존의 모션 생성 방법은 대부분 작업별로 특화되어 있으며 유연한 다중 에이전트 생성으로 일반화되지 않습니다. 우리는 MAGNet(Multi-Agent Generative Network)을 소개합니다. 이는 통합된 자기회귀 확산 프레임워크로, 유연한 조건화와 샘플링을 통해 다양한 상호작용 작업을 지원합니다. MAGNet은 단일 모델 내에서 이인칭 및 다인칭 예측, 파트너 인페인팅, 파트너 예측, 에이전트 생성을 모두 수행하며, 수백 개의 모션 단계에 걸친 초장기 시퀀스를 자기회귀적으로 생성할 수 있습니다. 우리는 자기회귀 잡음 제거 과정에서 에이전트 간 결합을 명시적으로 모델링하여 에이전트 간의 일관된 조정을 가능하게 합니다. 그 결과, MAGNet은 긴밀하게 동기화된 활동(예: 춤, 복싱)과 느슨하게 구조화된 사회적 상호작용을 모두 포착합니다. 우리의 접근 방식은 이인칭 벤치마크에서 특화된 방법과 동등한 성능을 보이면서도 세 명 이상의 상호작용하는 사람들이 포함된 다인칭 시나리오로 자연스럽게 확장됩니다. 생성된 상호작용의 시간적 역학과 공간적 조정이 가장 잘 드러나는 보충 비디오를 시청해 주시기 바랍니다. 프로젝트 페이지: https://von31.github.io/MAGNet/

## 핵심 내용
다중 인물 상호작용을 이해하고 생성하는 것은 로보틱스와 사회 컴퓨팅에 광범위한 영향을 미치는 근본적인 도전 과제입니다. 인간은 자연스럽게 그룹으로 협력하지만, 긴 시간적 범위, 강한 에이전트 간 의존성, 그리고 다양한 그룹 크기로 인해 이러한 상호작용을 모델링하는 것은 여전히 어렵습니다. 기존의 모션 생성 방법은 대부분 작업별로 특화되어 있으며 유연한 다중 에이전트 생성으로 일반화되지 않습니다. 우리는 MAGNet(Multi-Agent Generative Network)을 소개합니다. 이는 통합된 자기회귀 확산 프레임워크로, 유연한 조건화와 샘플링을 통해 다양한 상호작용 작업을 지원합니다. MAGNet은 단일 모델 내에서 이인칭 및 다인칭 예측, 파트너 인페인팅, 파트너 예측, 에이전트 생성을 모두 수행하며, 수백 개의 모션 단계에 걸친 초장기 시퀀스를 자기회귀적으로 생성할 수 있습니다. 우리는 자기회귀 잡음 제거 과정에서 에이전트 간 결합을 명시적으로 모델링하여 에이전트 간의 일관된 조정을 가능하게 합니다. 그 결과, MAGNet은 긴밀하게 동기화된 활동(예: 춤, 복싱)과 느슨하게 구조화된 사회적 상호작용을 모두 포착합니다. 우리의 접근 방식은 이인칭 벤치마크에서 특화된 방법과 동등한 성능을 보이면서도 세 명 이상의 상호작용하는 사람들이 포함된 다인칭 시나리오로 자연스럽게 확장됩니다. 생성된 상호작용의 시간적 역학과 공간적 조정이 가장 잘 드러나는 보충 비디오를 시청해 주시기 바랍니다. 프로젝트 페이지: https://von31.github.io/MAGNet/
