---
$id: ent_paper_ke_3d_diffuser_actor_policy_diffu_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations'
  zh: 3D Diffuser Actor
  ko: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations'
summary:
  en: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations (3D Diffuser Actor), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2024.'
  zh: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations (3D Diffuser Actor), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2024.'
  ko: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations (3D Diffuser Actor), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 3d_diffuser_actor
- generalist_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.10885v3.
sources:
- id: src_001
  type: paper
  title: 3D Diffuser Actor source
  url: https://proceedings.mlr.press/v270/ke25a.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Diffusion policies are conditional diffusion models that learn robot action distributions conditioned on the robot and environment state. They have recently shown to outperform both deterministic and alternative action distribution learning formulations. 3D robot policies use 3D scene feature representations aggregated from a single or multiple camera views using sensed depth. They have shown to generalize better than their 2D counterparts across camera viewpoints. We unify these two lines of work and present 3D Diffuser Actor, a neural policy equipped with a novel 3D denoising transformer that fuses information from the 3D visual scene, a language instruction and proprioception to predict the noise in noised 3D robot pose trajectories. 3D Diffuser Actor sets a new state-of-the-art on RLBench with an absolute performance gain of 18.1% over the current SOTA on a multi-view setup and an absolute gain of 13.1% on a single-view setup. On the CALVIN benchmark, it improves over the current SOTA by a 9% relative increase. It also learns to control a robot manipulator in the real world from a handful of demonstrations. Through thorough comparisons with the current SOTA policies and ablations of our model, we show 3D Diffuser Actor's design choices dramatically outperform 2D representations, regression and classification objectives, absolute attentions, and holistic non-tokenized 3D scene embeddings.

## 核心内容
Diffusion policies are conditional diffusion models that learn robot action distributions conditioned on the robot and environment state. They have recently shown to outperform both deterministic and alternative action distribution learning formulations. 3D robot policies use 3D scene feature representations aggregated from a single or multiple camera views using sensed depth. They have shown to generalize better than their 2D counterparts across camera viewpoints. We unify these two lines of work and present 3D Diffuser Actor, a neural policy equipped with a novel 3D denoising transformer that fuses information from the 3D visual scene, a language instruction and proprioception to predict the noise in noised 3D robot pose trajectories. 3D Diffuser Actor sets a new state-of-the-art on RLBench with an absolute performance gain of 18.1% over the current SOTA on a multi-view setup and an absolute gain of 13.1% on a single-view setup. On the CALVIN benchmark, it improves over the current SOTA by a 9% relative increase. It also learns to control a robot manipulator in the real world from a handful of demonstrations. Through thorough comparisons with the current SOTA policies and ablations of our model, we show 3D Diffuser Actor's design choices dramatically outperform 2D representations, regression and classification objectives, absolute attentions, and holistic non-tokenized 3D scene embeddings.

## 参考
- http://arxiv.org/abs/2402.10885v3

## Overview
Diffusion policies are conditional diffusion models that learn robot action distributions conditioned on the robot and environment state. They have recently shown to outperform both deterministic and alternative action distribution learning formulations. 3D robot policies use 3D scene feature representations aggregated from a single or multiple camera views using sensed depth. They have shown to generalize better than their 2D counterparts across camera viewpoints. We unify these two lines of work and present 3D Diffuser Actor, a neural policy equipped with a novel 3D denoising transformer that fuses information from the 3D visual scene, a language instruction and proprioception to predict the noise in noised 3D robot pose trajectories. 3D Diffuser Actor sets a new state-of-the-art on RLBench with an absolute performance gain of 18.1% over the current SOTA on a multi-view setup and an absolute gain of 13.1% on a single-view setup. On the CALVIN benchmark, it improves over the current SOTA by a 9% relative increase. It also learns to control a robot manipulator in the real world from a handful of demonstrations. Through thorough comparisons with the current SOTA policies and ablations of our model, we show 3D Diffuser Actor's design choices dramatically outperform 2D representations, regression and classification objectives, absolute attentions, and holistic non-tokenized 3D scene embeddings.

## Content
Diffusion policies are conditional diffusion models that learn robot action distributions conditioned on the robot and environment state. They have recently shown to outperform both deterministic and alternative action distribution learning formulations. 3D robot policies use 3D scene feature representations aggregated from a single or multiple camera views using sensed depth. They have shown to generalize better than their 2D counterparts across camera viewpoints. We unify these two lines of work and present 3D Diffuser Actor, a neural policy equipped with a novel 3D denoising transformer that fuses information from the 3D visual scene, a language instruction and proprioception to predict the noise in noised 3D robot pose trajectories. 3D Diffuser Actor sets a new state-of-the-art on RLBench with an absolute performance gain of 18.1% over the current SOTA on a multi-view setup and an absolute gain of 13.1% on a single-view setup. On the CALVIN benchmark, it improves over the current SOTA by a 9% relative increase. It also learns to control a robot manipulator in the real world from a handful of demonstrations. Through thorough comparisons with the current SOTA policies and ablations of our model, we show 3D Diffuser Actor's design choices dramatically outperform 2D representations, regression and classification objectives, absolute attentions, and holistic non-tokenized 3D scene embeddings.

## 개요
Diffusion policies는 로봇과 환경 상태에 조건화된 로봇 행동 분포를 학습하는 조건부 확산 모델입니다. 최근 이들은 결정론적 및 대안적 행동 분포 학습 방식보다 뛰어난 성능을 보여주고 있습니다. 3D 로봇 정책은 감지된 깊이를 사용하여 단일 또는 다중 카메라 뷰에서 집계된 3D 장면 특징 표현을 활용합니다. 이들은 카메라 시점에 걸쳐 2D 기반 정책보다 더 나은 일반화 성능을 보여주었습니다. 우리는 이 두 연구 흐름을 통합하여 3D Diffuser Actor를 제시합니다. 이는 새로운 3D 노이즈 제거 트랜스포머를 갖춘 신경 정책으로, 3D 시각 장면, 언어 명령 및 고유 감각 정보를 융합하여 노이즈가 포함된 3D 로봇 포즈 궤적의 노이즈를 예측합니다. 3D Diffuser Actor는 RLBench에서 다중 뷰 설정에서 현재 SOTA 대비 18.1%의 절대 성능 향상, 단일 뷰 설정에서 13.1%의 절대 향상으로 새로운 최고 성능을 기록했습니다. CALVIN 벤치마크에서는 현재 SOTA 대비 9%의 상대적 개선을 이루었습니다. 또한 소수의 시연만으로 실제 세계에서 로봇 매니퓰레이터를 제어하는 방법을 학습합니다. 현재 SOTA 정책과의 철저한 비교 및 모델의 절제 연구를 통해, 3D Diffuser Actor의 설계 선택이 2D 표현, 회귀 및 분류 목표, 절대적 주의 메커니즘, 전체적 비토큰화 3D 장면 임베딩보다 훨씬 뛰어난 성능을 발휘함을 보여줍니다.

## 핵심 내용
Diffusion policies는 로봇과 환경 상태에 조건화된 로봇 행동 분포를 학습하는 조건부 확산 모델입니다. 최근 이들은 결정론적 및 대안적 행동 분포 학습 방식보다 뛰어난 성능을 보여주고 있습니다. 3D 로봇 정책은 감지된 깊이를 사용하여 단일 또는 다중 카메라 뷰에서 집계된 3D 장면 특징 표현을 활용합니다. 이들은 카메라 시점에 걸쳐 2D 기반 정책보다 더 나은 일반화 성능을 보여주었습니다. 우리는 이 두 연구 흐름을 통합하여 3D Diffuser Actor를 제시합니다. 이는 새로운 3D 노이즈 제거 트랜스포머를 갖춘 신경 정책으로, 3D 시각 장면, 언어 명령 및 고유 감각 정보를 융합하여 노이즈가 포함된 3D 로봇 포즈 궤적의 노이즈를 예측합니다. 3D Diffuser Actor는 RLBench에서 다중 뷰 설정에서 현재 SOTA 대비 18.1%의 절대 성능 향상, 단일 뷰 설정에서 13.1%의 절대 향상으로 새로운 최고 성능을 기록했습니다. CALVIN 벤치마크에서는 현재 SOTA 대비 9%의 상대적 개선을 이루었습니다. 또한 소수의 시연만으로 실제 세계에서 로봇 매니퓰레이터를 제어하는 방법을 학습합니다. 현재 SOTA 정책과의 철저한 비교 및 모델의 절제 연구를 통해, 3D Diffuser Actor의 설계 선택이 2D 표현, 회귀 및 분류 목표, 절대적 주의 메커니즘, 전체적 비토큰화 3D 장면 임베딩보다 훨씬 뛰어난 성능을 발휘함을 보여줍니다.
