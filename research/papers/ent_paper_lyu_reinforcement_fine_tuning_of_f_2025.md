---
$id: ent_paper_lyu_reinforcement_fine_tuning_of_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models
  zh: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models
  ko: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models
summary:
  en: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models (Reinforcement Fine-Tuning of
    Flow-Matching Policies for Vision-Language-Action Models), is a 2025 large vision-language-action model for robotic manipulation.
  zh: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models (Reinforcement Fine-Tuning of
    Flow-Matching Policies for Vision-Language-Action Models), is a 2025 large vision-language-action model for robotic manipulation.
  ko: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models (Reinforcement Fine-Tuning of
    Flow-Matching Policies for Vision-Language-Action Models), is a 2025 large vision-language-action model for robotic manipulation.
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
- reinforcement_fine_tuning_of_f
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.09976v2.
sources:
- id: src_001
  type: paper
  title: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2510.09976
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models source
  url: https://doi.org/10.48550/arXiv.2510.09976
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models such as OpenVLA, Octo, and $π_0$ have shown strong generalization by leveraging large-scale demonstrations, yet their performance is still fundamentally constrained by the quality and coverage of supervised data. Reinforcement learning (RL) provides a promising path for improving and fine-tuning VLAs through online interaction. However, conventional policy gradient methods are computationally infeasible in the context of flow-matching based models due to the intractability of the importance sampling process, which requires explicit computation of policy ratios. To overcome this limitation, we propose Flow Policy Optimization (FPO) algorithm, which reformulates importance sampling by leveraging per-sample changes in the conditional flow-matching objective. Furthermore, FPO achieves stable and scalable online reinforcement fine-tuning of the $π_0$ model by integrating structure-aware credit assignment to enhance gradient efficiency, clipped surrogate objectives to stabilize optimization, multi-step latent exploration to encourage diverse policy updates, and a Q-ensemble mechanism to provide robust value estimation. We evaluate FPO on the LIBERO benchmark and the ALOHA simulation task against supervised, preference-aligned, diffusion-based, autoregressive online RL, and $π_0$-FAST baselines, observing consistent improvements over the imitation prior and strong alternatives with stable learning under sparse rewards. In addition, ablation studies and analyses of the latent space dynamics further highlight the contributions of individual components within FPO, validating the effectiveness of the proposed computational modules and the stable convergence of the conditional flow-matching objective during online RL.

## 核心内容
Vision-Language-Action (VLA) models such as OpenVLA, Octo, and $π_0$ have shown strong generalization by leveraging large-scale demonstrations, yet their performance is still fundamentally constrained by the quality and coverage of supervised data. Reinforcement learning (RL) provides a promising path for improving and fine-tuning VLAs through online interaction. However, conventional policy gradient methods are computationally infeasible in the context of flow-matching based models due to the intractability of the importance sampling process, which requires explicit computation of policy ratios. To overcome this limitation, we propose Flow Policy Optimization (FPO) algorithm, which reformulates importance sampling by leveraging per-sample changes in the conditional flow-matching objective. Furthermore, FPO achieves stable and scalable online reinforcement fine-tuning of the $π_0$ model by integrating structure-aware credit assignment to enhance gradient efficiency, clipped surrogate objectives to stabilize optimization, multi-step latent exploration to encourage diverse policy updates, and a Q-ensemble mechanism to provide robust value estimation. We evaluate FPO on the LIBERO benchmark and the ALOHA simulation task against supervised, preference-aligned, diffusion-based, autoregressive online RL, and $π_0$-FAST baselines, observing consistent improvements over the imitation prior and strong alternatives with stable learning under sparse rewards. In addition, ablation studies and analyses of the latent space dynamics further highlight the contributions of individual components within FPO, validating the effectiveness of the proposed computational modules and the stable convergence of the conditional flow-matching objective during online RL.

## 参考
- http://arxiv.org/abs/2510.09976v2

## Overview
Vision-Language-Action (VLA) models such as OpenVLA, Octo, and \(π_0\) have shown strong generalization by leveraging large-scale demonstrations, yet their performance is still fundamentally constrained by the quality and coverage of supervised data. Reinforcement learning (RL) provides a promising path for improving and fine-tuning VLAs through online interaction. However, conventional policy gradient methods are computationally infeasible in the context of flow-matching based models due to the intractability of the importance sampling process, which requires explicit computation of policy ratios. To overcome this limitation, we propose Flow Policy Optimization (FPO) algorithm, which reformulates importance sampling by leveraging per-sample changes in the conditional flow-matching objective. Furthermore, FPO achieves stable and scalable online reinforcement fine-tuning of the \(π_0\) model by integrating structure-aware credit assignment to enhance gradient efficiency, clipped surrogate objectives to stabilize optimization, multi-step latent exploration to encourage diverse policy updates, and a Q-ensemble mechanism to provide robust value estimation. We evaluate FPO on the LIBERO benchmark and the ALOHA simulation task against supervised, preference-aligned, diffusion-based, autoregressive online RL, and \(π_0\)-FAST baselines, observing consistent improvements over the imitation prior and strong alternatives with stable learning under sparse rewards. In addition, ablation studies and analyses of the latent space dynamics further highlight the contributions of individual components within FPO, validating the effectiveness of the proposed computational modules and the stable convergence of the conditional flow-matching objective during online RL.

## Content
Vision-Language-Action (VLA) models such as OpenVLA, Octo, and \(π_0\) have shown strong generalization by leveraging large-scale demonstrations, yet their performance is still fundamentally constrained by the quality and coverage of supervised data. Reinforcement learning (RL) provides a promising path for improving and fine-tuning VLAs through online interaction. However, conventional policy gradient methods are computationally infeasible in the context of flow-matching based models due to the intractability of the importance sampling process, which requires explicit computation of policy ratios. To overcome this limitation, we propose Flow Policy Optimization (FPO) algorithm, which reformulates importance sampling by leveraging per-sample changes in the conditional flow-matching objective. Furthermore, FPO achieves stable and scalable online reinforcement fine-tuning of the \(π_0\) model by integrating structure-aware credit assignment to enhance gradient efficiency, clipped surrogate objectives to stabilize optimization, multi-step latent exploration to encourage diverse policy updates, and a Q-ensemble mechanism to provide robust value estimation. We evaluate FPO on the LIBERO benchmark and the ALOHA simulation task against supervised, preference-aligned, diffusion-based, autoregressive online RL, and \(π_0\)-FAST baselines, observing consistent improvements over the imitation prior and strong alternatives with stable learning under sparse rewards. In addition, ablation studies and analyses of the latent space dynamics further highlight the contributions of individual components within FPO, validating the effectiveness of the proposed computational modules and the stable convergence of the conditional flow-matching objective during online RL.

## 개요
OpenVLA, Octo, $π_0$와 같은 Vision-Language-Action (VLA) 모델은 대규모 시연 데이터를 활용하여 강력한 일반화 성능을 보여주었지만, 그 성능은 여전히 지도 학습 데이터의 품질과 범위에 근본적으로 제약을 받습니다. 강화 학습(RL)은 온라인 상호작용을 통해 VLA를 개선하고 미세 조정할 수 있는 유망한 경로를 제공합니다. 그러나 기존의 정책 경사 방법은 중요도 샘플링 과정이 다루기 어려워 유동 매칭 기반 모델의 맥락에서 계산적으로 실행 불가능합니다. 이는 정책 비율의 명시적 계산을 필요로 하기 때문입니다. 이러한 한계를 극복하기 위해, 우리는 조건부 유동 매칭 목적 함수에서 샘플별 변화를 활용하여 중요도 샘플링을 재구성하는 Flow Policy Optimization (FPO) 알고리즘을 제안합니다. 또한, FPO는 구조 인식 크레딧 할당을 통합하여 그래디언트 효율성을 높이고, 클리핑된 대리 목적 함수로 최적화를 안정화하며, 다단계 잠재 탐색으로 다양한 정책 업데이트를 장려하고, Q-앙상블 메커니즘으로 강건한 가치 추정을 제공함으로써 $π_0$ 모델의 안정적이고 확장 가능한 온라인 강화 미세 조정을 달성합니다. 우리는 FPO를 LIBERO 벤치마크와 ALOHA 시뮬레이션 작업에서 지도 학습, 선호 정렬, 확산 기반, 자기회귀 온라인 RL, $π_0$-FAST 기준선과 비교 평가하여, 모방 사전 및 강력한 대안에 비해 일관된 개선과 희소 보상 하에서의 안정적인 학습을 관찰했습니다. 또한, 절제 연구와 잠재 공간 역학 분석을 통해 FPO 내 개별 구성 요소의 기여를 더욱 강조하여, 제안된 계산 모듈의 효과성과 온라인 RL 중 조건부 유동 매칭 목적 함수의 안정적인 수렴을 검증했습니다.

## 핵심 내용
OpenVLA, Octo, $π_0$와 같은 Vision-Language-Action (VLA) 모델은 대규모 시연 데이터를 활용하여 강력한 일반화 성능을 보여주었지만, 그 성능은 여전히 지도 학습 데이터의 품질과 범위에 근본적으로 제약을 받습니다. 강화 학습(RL)은 온라인 상호작용을 통해 VLA를 개선하고 미세 조정할 수 있는 유망한 경로를 제공합니다. 그러나 기존의 정책 경사 방법은 중요도 샘플링 과정이 다루기 어려워 유동 매칭 기반 모델의 맥락에서 계산적으로 실행 불가능합니다. 이는 정책 비율의 명시적 계산을 필요로 하기 때문입니다. 이러한 한계를 극복하기 위해, 우리는 조건부 유동 매칭 목적 함수에서 샘플별 변화를 활용하여 중요도 샘플링을 재구성하는 Flow Policy Optimization (FPO) 알고리즘을 제안합니다. 또한, FPO는 구조 인식 크레딧 할당을 통합하여 그래디언트 효율성을 높이고, 클리핑된 대리 목적 함수로 최적화를 안정화하며, 다단계 잠재 탐색으로 다양한 정책 업데이트를 장려하고, Q-앙상블 메커니즘으로 강건한 가치 추정을 제공함으로써 $π_0$ 모델의 안정적이고 확장 가능한 온라인 강화 미세 조정을 달성합니다. 우리는 FPO를 LIBERO 벤치마크와 ALOHA 시뮬레이션 작업에서 지도 학습, 선호 정렬, 확산 기반, 자기회귀 온라인 RL, $π_0$-FAST 기준선과 비교 평가하여, 모방 사전 및 강력한 대안에 비해 일관된 개선과 희소 보상 하에서의 안정적인 학습을 관찰했습니다. 또한, 절제 연구와 잠재 공간 역학 분석을 통해 FPO 내 개별 구성 요소의 기여를 더욱 강조하여, 제안된 계산 모듈의 효과성과 온라인 RL 중 조건부 유동 매칭 목적 함수의 안정적인 수렴을 검증했습니다.
