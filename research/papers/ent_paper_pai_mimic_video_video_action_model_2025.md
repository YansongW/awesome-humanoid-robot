---
$id: ent_paper_pai_mimic_video_video_action_model_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs'
  zh: VAM
  ko: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs'
summary:
  en: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (VAM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by mimic robotics, Microsoft Zurich, ETH Zurich, ETH AI Center, UC Berkeley.'
  zh: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (VAM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by mimic robotics, Microsoft Zurich, ETH Zurich, ETH AI Center, UC Berkeley.'
  ko: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (VAM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by mimic robotics, Microsoft Zurich, ETH Zurich, ETH AI Center, UC Berkeley.'
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
- vam
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15692v2.
sources:
- id: src_001
  type: paper
  title: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (arXiv)'
  url: https://arxiv.org/abs/2512.15692
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VAM source
  url: https://doi.org/10.48550/arXiv.2512.15692
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Prevailing Vision-Language-Action Models (VLAs) for robotic manipulation are built upon vision-language backbones pretrained on large-scale, but disconnected static web data. As a result, despite improved semantic generalization, the policy must implicitly infer complex physical dynamics and temporal dependencies solely from robot trajectories. This reliance creates an unsustainable data burden, necessitating continuous, large-scale expert data collection to compensate for the lack of innate physical understanding. We contend that while vision-language pretraining effectively captures semantic priors, it remains blind to physical causality. A more effective paradigm leverages video to jointly capture semantics and visual dynamics during pretraining, thereby isolating the remaining task of low-level control. To this end, we introduce mimic-video, a novel Video-Action Model (VAM) that pairs a pretrained Internet-scale video model with a flow matching-based action decoder conditioned on its latent representations. The decoder serves as an Inverse Dynamics Model (IDM), generating low-level robot actions from the latent representation of video-space action plans. Our extensive evaluation shows that our approach achieves state-of-the-art performance on simulated and real-world robotic manipulation tasks, improving sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures.

## 核心内容
Prevailing Vision-Language-Action Models (VLAs) for robotic manipulation are built upon vision-language backbones pretrained on large-scale, but disconnected static web data. As a result, despite improved semantic generalization, the policy must implicitly infer complex physical dynamics and temporal dependencies solely from robot trajectories. This reliance creates an unsustainable data burden, necessitating continuous, large-scale expert data collection to compensate for the lack of innate physical understanding. We contend that while vision-language pretraining effectively captures semantic priors, it remains blind to physical causality. A more effective paradigm leverages video to jointly capture semantics and visual dynamics during pretraining, thereby isolating the remaining task of low-level control. To this end, we introduce mimic-video, a novel Video-Action Model (VAM) that pairs a pretrained Internet-scale video model with a flow matching-based action decoder conditioned on its latent representations. The decoder serves as an Inverse Dynamics Model (IDM), generating low-level robot actions from the latent representation of video-space action plans. Our extensive evaluation shows that our approach achieves state-of-the-art performance on simulated and real-world robotic manipulation tasks, improving sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures.

## 参考
- http://arxiv.org/abs/2512.15692v2

## Overview
Prevailing Vision-Language-Action Models (VLAs) for robotic manipulation are built upon vision-language backbones pretrained on large-scale, but disconnected static web data. As a result, despite improved semantic generalization, the policy must implicitly infer complex physical dynamics and temporal dependencies solely from robot trajectories. This reliance creates an unsustainable data burden, necessitating continuous, large-scale expert data collection to compensate for the lack of innate physical understanding. We contend that while vision-language pretraining effectively captures semantic priors, it remains blind to physical causality. A more effective paradigm leverages video to jointly capture semantics and visual dynamics during pretraining, thereby isolating the remaining task of low-level control. To this end, we introduce mimic-video, a novel Video-Action Model (VAM) that pairs a pretrained Internet-scale video model with a flow matching-based action decoder conditioned on its latent representations. The decoder serves as an Inverse Dynamics Model (IDM), generating low-level robot actions from the latent representation of video-space action plans. Our extensive evaluation shows that our approach achieves state-of-the-art performance on simulated and real-world robotic manipulation tasks, improving sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures.

## Content
Prevailing Vision-Language-Action Models (VLAs) for robotic manipulation are built upon vision-language backbones pretrained on large-scale, but disconnected static web data. As a result, despite improved semantic generalization, the policy must implicitly infer complex physical dynamics and temporal dependencies solely from robot trajectories. This reliance creates an unsustainable data burden, necessitating continuous, large-scale expert data collection to compensate for the lack of innate physical understanding. We contend that while vision-language pretraining effectively captures semantic priors, it remains blind to physical causality. A more effective paradigm leverages video to jointly capture semantics and visual dynamics during pretraining, thereby isolating the remaining task of low-level control. To this end, we introduce mimic-video, a novel Video-Action Model (VAM) that pairs a pretrained Internet-scale video model with a flow matching-based action decoder conditioned on its latent representations. The decoder serves as an Inverse Dynamics Model (IDM), generating low-level robot actions from the latent representation of video-space action plans. Our extensive evaluation shows that our approach achieves state-of-the-art performance on simulated and real-world robotic manipulation tasks, improving sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures.

## 개요
로봇 조작을 위한 기존의 Vision-Language-Action Models (VLA)는 대규모이지만 단절된 정적 웹 데이터로 사전 학습된 비전-언어 백본을 기반으로 구축됩니다. 그 결과, 의미적 일반화가 향상되었음에도 불구하고, 정책은 로봇 궤적으로부터만 복잡한 물리적 역학과 시간적 의존성을 암시적으로 추론해야 합니다. 이러한 의존성은 지속 불가능한 데이터 부담을 초래하여, 타고난 물리적 이해의 부족을 보완하기 위해 지속적이고 대규모의 전문가 데이터 수집을 필요로 합니다. 우리는 비전-언어 사전 학습이 의미적 사전 지식을 효과적으로 포착하지만, 물리적 인과관계에는 여전히 무지하다고 주장합니다. 더 효과적인 패러다임은 사전 학습 중에 비디오를 활용하여 의미와 시각적 역학을 동시에 포착함으로써, 남은 저수준 제어 작업을 분리하는 것입니다. 이를 위해, 우리는 사전 학습된 인터넷 규모의 비디오 모델과 잠재 표현에 조건화된 흐름 매칭 기반 행동 디코더를 결합한 새로운 Video-Action Model (VAM)인 mimic-video를 소개합니다. 디코더는 역동역학 모델 (IDM) 역할을 하여, 비디오 공간 행동 계획의 잠재 표현으로부터 저수준 로봇 행동을 생성합니다. 우리의 광범위한 평가는 우리의 접근 방식이 시뮬레이션 및 실제 로봇 조작 작업에서 최첨단 성능을 달성하며, 기존 VLA 아키텍처에 비해 샘플 효율성을 10배, 수렴 속도를 2배 향상시킴을 보여줍니다.

## 핵심 내용
로봇 조작을 위한 기존의 Vision-Language-Action Models (VLA)는 대규모이지만 단절된 정적 웹 데이터로 사전 학습된 비전-언어 백본을 기반으로 구축됩니다. 그 결과, 의미적 일반화가 향상되었음에도 불구하고, 정책은 로봇 궤적으로부터만 복잡한 물리적 역학과 시간적 의존성을 암시적으로 추론해야 합니다. 이러한 의존성은 지속 불가능한 데이터 부담을 초래하여, 타고난 물리적 이해의 부족을 보완하기 위해 지속적이고 대규모의 전문가 데이터 수집을 필요로 합니다. 우리는 비전-언어 사전 학습이 의미적 사전 지식을 효과적으로 포착하지만, 물리적 인과관계에는 여전히 무지하다고 주장합니다. 더 효과적인 패러다임은 사전 학습 중에 비디오를 활용하여 의미와 시각적 역학을 동시에 포착함으로써, 남은 저수준 제어 작업을 분리하는 것입니다. 이를 위해, 우리는 사전 학습된 인터넷 규모의 비디오 모델과 잠재 표현에 조건화된 흐름 매칭 기반 행동 디코더를 결합한 새로운 Video-Action Model (VAM)인 mimic-video를 소개합니다. 디코더는 역동역학 모델 (IDM) 역할을 하여, 비디오 공간 행동 계획의 잠재 표현으로부터 저수준 로봇 행동을 생성합니다. 우리의 광범위한 평가는 우리의 접근 방식이 시뮬레이션 및 실제 로봇 조작 작업에서 최첨단 성능을 달성하며, 기존 VLA 아키텍처에 비해 샘플 효율성을 10배, 수렴 속도를 2배 향상시킴을 보여줍니다.
