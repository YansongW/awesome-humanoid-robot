---
$id: ent_paper_fang_robotic_vla_benefits_from_join_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion
  zh: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion
  ko: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion
summary:
  en: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (Robotic VLA Benefits from Joint Learning with
    Motion Image Diffusion), is a 2025 large vision-language-action model for robotic manipulation, introduced by Salesforce,
    Stanford University.
  zh: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (Robotic VLA Benefits from Joint Learning with
    Motion Image Diffusion), is a 2025 large vision-language-action model for robotic manipulation, introduced by Salesforce,
    Stanford University.
  ko: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (Robotic VLA Benefits from Joint Learning with
    Motion Image Diffusion), is a 2025 large vision-language-action model for robotic manipulation, introduced by Salesforce,
    Stanford University.
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
- robotic_vla_benefits_from_join
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18007v1.
sources:
- id: src_001
  type: paper
  title: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (arXiv)
  url: https://arxiv.org/abs/2512.18007
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion source
  url: https://doi.org/10.48550/arXiv.2512.18007
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have achieved remarkable progress in robotic manipulation by mapping multimodal observations and instructions directly to actions. However, they typically mimic expert trajectories without predictive motion reasoning, which limits their ability to reason about what actions to take. To address this limitation, we propose joint learning with motion image diffusion, a novel strategy that enhances VLA models with motion reasoning capabilities. Our method extends the VLA architecture with a dual-head design: while the action head predicts action chunks as in vanilla VLAs, an additional motion head, implemented as a Diffusion Transformer (DiT), predicts optical-flow-based motion images that capture future dynamics. The two heads are trained jointly, enabling the shared VLM backbone to learn representations that couple robot control with motion knowledge. This joint learning builds temporally coherent and physically grounded representations without modifying the inference pathway of standard VLAs, thereby maintaining test-time latency. Experiments in both simulation and real-world environments demonstrate that joint learning with motion image diffusion improves the success rate of pi-series VLAs to 97.5% on the LIBERO benchmark and 58.0% on the RoboTwin benchmark, yielding a 23% improvement in real-world performance and validating its effectiveness in enhancing the motion reasoning capability of large-scale VLAs.

## 核心内容
Vision-Language-Action (VLA) models have achieved remarkable progress in robotic manipulation by mapping multimodal observations and instructions directly to actions. However, they typically mimic expert trajectories without predictive motion reasoning, which limits their ability to reason about what actions to take. To address this limitation, we propose joint learning with motion image diffusion, a novel strategy that enhances VLA models with motion reasoning capabilities. Our method extends the VLA architecture with a dual-head design: while the action head predicts action chunks as in vanilla VLAs, an additional motion head, implemented as a Diffusion Transformer (DiT), predicts optical-flow-based motion images that capture future dynamics. The two heads are trained jointly, enabling the shared VLM backbone to learn representations that couple robot control with motion knowledge. This joint learning builds temporally coherent and physically grounded representations without modifying the inference pathway of standard VLAs, thereby maintaining test-time latency. Experiments in both simulation and real-world environments demonstrate that joint learning with motion image diffusion improves the success rate of pi-series VLAs to 97.5% on the LIBERO benchmark and 58.0% on the RoboTwin benchmark, yielding a 23% improvement in real-world performance and validating its effectiveness in enhancing the motion reasoning capability of large-scale VLAs.

## 参考
- http://arxiv.org/abs/2512.18007v1

## Overview
Vision-Language-Action (VLA) models have achieved remarkable progress in robotic manipulation by mapping multimodal observations and instructions directly to actions. However, they typically mimic expert trajectories without predictive motion reasoning, which limits their ability to reason about what actions to take. To address this limitation, we propose joint learning with motion image diffusion, a novel strategy that enhances VLA models with motion reasoning capabilities. Our method extends the VLA architecture with a dual-head design: while the action head predicts action chunks as in vanilla VLAs, an additional motion head, implemented as a Diffusion Transformer (DiT), predicts optical-flow-based motion images that capture future dynamics. The two heads are trained jointly, enabling the shared VLM backbone to learn representations that couple robot control with motion knowledge. This joint learning builds temporally coherent and physically grounded representations without modifying the inference pathway of standard VLAs, thereby maintaining test-time latency. Experiments in both simulation and real-world environments demonstrate that joint learning with motion image diffusion improves the success rate of pi-series VLAs to 97.5% on the LIBERO benchmark and 58.0% on the RoboTwin benchmark, yielding a 23% improvement in real-world performance and validating its effectiveness in enhancing the motion reasoning capability of large-scale VLAs.

## Content
Vision-Language-Action (VLA) models have achieved remarkable progress in robotic manipulation by mapping multimodal observations and instructions directly to actions. However, they typically mimic expert trajectories without predictive motion reasoning, which limits their ability to reason about what actions to take. To address this limitation, we propose joint learning with motion image diffusion, a novel strategy that enhances VLA models with motion reasoning capabilities. Our method extends the VLA architecture with a dual-head design: while the action head predicts action chunks as in vanilla VLAs, an additional motion head, implemented as a Diffusion Transformer (DiT), predicts optical-flow-based motion images that capture future dynamics. The two heads are trained jointly, enabling the shared VLM backbone to learn representations that couple robot control with motion knowledge. This joint learning builds temporally coherent and physically grounded representations without modifying the inference pathway of standard VLAs, thereby maintaining test-time latency. Experiments in both simulation and real-world environments demonstrate that joint learning with motion image diffusion improves the success rate of pi-series VLAs to 97.5% on the LIBERO benchmark and 58.0% on the RoboTwin benchmark, yielding a 23% improvement in real-world performance and validating its effectiveness in enhancing the motion reasoning capability of large-scale VLAs.

## 개요
Vision-Language-Action (VLA) 모델은 다중 모달 관찰과 명령을 직접 행동으로 매핑하여 로봇 조작 분야에서 놀라운 진전을 이루었습니다. 그러나 이러한 모델은 일반적으로 예측적 움직임 추론 없이 전문가 궤적을 모방하므로, 어떤 행동을 취해야 하는지 추론하는 능력이 제한됩니다. 이러한 한계를 해결하기 위해, 우리는 움직임 이미지 확산을 통한 공동 학습(joint learning with motion image diffusion)이라는 새로운 전략을 제안하며, 이는 VLA 모델에 움직임 추론 능력을 부여합니다. 우리의 방법은 이중 헤드(dual-head) 설계로 VLA 아키텍처를 확장합니다: 액션 헤드는 기본 VLA와 같이 행동 청크(action chunks)를 예측하는 반면, 확산 트랜스포머(Diffusion Transformer, DiT)로 구현된 추가적인 움직임 헤드는 미래 역학을 포착하는 광학 흐름 기반 움직임 이미지를 예측합니다. 두 헤드는 공동으로 훈련되어, 공유된 VLM 백본이 로봇 제어와 움직임 지식을 결합한 표현을 학습할 수 있게 합니다. 이 공동 학습은 표준 VLA의 추론 경로를 수정하지 않고 시간적으로 일관되고 물리적으로 기반을 둔 표현을 구축하여, 테스트 시 지연 시간을 유지합니다. 시뮬레이션 및 실제 환경 모두에서의 실험은 움직임 이미지 확산을 통한 공동 학습이 pi-시리즈 VLA의 성공률을 LIBERO 벤치마크에서 97.5%, RoboTwin 벤치마크에서 58.0%로 향상시키며, 실제 환경 성능에서 23%의 개선을 가져와 대규모 VLA의 움직임 추론 능력을 향상시키는 효과를 입증합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 다중 모달 관찰과 명령을 직접 행동으로 매핑하여 로봇 조작 분야에서 놀라운 진전을 이루었습니다. 그러나 이러한 모델은 일반적으로 예측적 움직임 추론 없이 전문가 궤적을 모방하므로, 어떤 행동을 취해야 하는지 추론하는 능력이 제한됩니다. 이러한 한계를 해결하기 위해, 우리는 움직임 이미지 확산을 통한 공동 학습(joint learning with motion image diffusion)이라는 새로운 전략을 제안하며, 이는 VLA 모델에 움직임 추론 능력을 부여합니다. 우리의 방법은 이중 헤드(dual-head) 설계로 VLA 아키텍처를 확장합니다: 액션 헤드는 기본 VLA와 같이 행동 청크(action chunks)를 예측하는 반면, 확산 트랜스포머(Diffusion Transformer, DiT)로 구현된 추가적인 움직임 헤드는 미래 역학을 포착하는 광학 흐름 기반 움직임 이미지를 예측합니다. 두 헤드는 공동으로 훈련되어, 공유된 VLM 백본이 로봇 제어와 움직임 지식을 결합한 표현을 학습할 수 있게 합니다. 이 공동 학습은 표준 VLA의 추론 경로를 수정하지 않고 시간적으로 일관되고 물리적으로 기반을 둔 표현을 구축하여, 테스트 시 지연 시간을 유지합니다. 시뮬레이션 및 실제 환경 모두에서의 실험은 움직임 이미지 확산을 통한 공동 학습이 pi-시리즈 VLA의 성공률을 LIBERO 벤치마크에서 97.5%, RoboTwin 벤치마크에서 58.0%로 향상시키며, 실제 환경 성능에서 23%의 개선을 가져와 대규모 VLA의 움직임 추론 능력을 향상시키는 효과를 입증합니다.
