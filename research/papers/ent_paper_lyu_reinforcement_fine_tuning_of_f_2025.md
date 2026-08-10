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
  zh: 本文提出Flow Policy Optimization (FPO)算法，用于对基于流匹配的视觉-语言-动作模型（如$π_0$）进行强化微调。FPO通过重新定义重要性采样过程，解决了传统策略梯度方法在流匹配模型中的计算不可行问题，并在LIBERO基准和ALOHA仿真任务上取得了优于多种基线方法的性能。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.09976v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (889 chars, DeepSeek).'
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
视觉-语言-动作模型（如OpenVLA、Octo和$π_0$）虽通过大规模演示数据展现出强大泛化能力，但其性能仍受限于监督数据的质量与覆盖范围。强化学习为在线微调VLA模型提供了可行路径，但传统策略梯度方法因需要显式计算策略比率，在流匹配模型背景下存在计算不可行性。为此，本文提出Flow Policy Optimization算法，通过利用条件流匹配目标中每个样本的变化来重新定义重要性采样。FPO还整合了结构感知信用分配、裁剪替代目标、多步潜在探索和Q-ensemble机制，实现了对$π_0$模型的稳定可扩展在线强化微调。

## 核心内容
### 方法架构
- **Flow Policy Optimization (FPO) 算法**：核心创新在于重新定义重要性采样过程，通过利用条件流匹配目标中每个样本的变化来避免传统策略比率的显式计算，从而解决流匹配模型中的计算不可行问题。
- **结构感知信用分配**：增强梯度效率，使模型能更有效地从稀疏奖励中学习。
- **裁剪替代目标**：稳定优化过程，防止策略更新过大导致训练不稳定。
- **多步潜在探索**：鼓励多样化的策略更新，提升探索效率。
- **Q-ensemble机制**：提供鲁棒的价值估计，减少价值函数估计的方差。

### 实验设置
- **基准测试**：在LIBERO基准和ALOHA仿真任务上进行评估。
- **基线方法**：与监督学习、偏好对齐、扩散模型、自回归在线RL以及$π_0$-FAST等方法进行对比。
- **训练细节**：在稀疏奖励设置下进行在线强化微调，评估稳定学习能力。

### 关键结果
- **性能提升**：FPO在所有评估任务上均一致优于模仿学习先验和强基线方法，展现出稳定的学习过程。
- **消融研究**：通过消融实验验证了FPO各组件（结构感知信用分配、裁剪目标、多步探索、Q-ensemble）的贡献，确认了每个计算模块的有效性。
- **潜在空间动力学**：分析表明，在在线RL过程中，条件流匹配目标实现了稳定收敛，进一步验证了FPO算法的有效性。

## Overview
Vision-Language-Action (VLA) models such as OpenVLA, Octo, and $π_0$ have shown strong generalization by leveraging large-scale demonstrations, yet their performance is still fundamentally constrained by the quality and coverage of supervised data. Reinforcement learning (RL) provides a promising path for improving and fine-tuning VLAs through online interaction. However, conventional policy gradient methods are computationally infeasible in the context of flow-matching based models due to the intractability of the importance sampling process, which requires explicit computation of policy ratios. To overcome this limitation, we propose Flow Policy Optimization (FPO) algorithm, which reformulates importance sampling by leveraging per-sample changes in the conditional flow-matching objective. Furthermore, FPO achieves stable and scalable online reinforcement fine-tuning of the $π_0$ model by integrating structure-aware credit assignment to enhance gradient efficiency, clipped surrogate objectives to stabilize optimization, multi-step latent exploration to encourage diverse policy updates, and a Q-ensemble mechanism to provide robust value estimation. We evaluate FPO on the LIBERO benchmark and the ALOHA simulation task against supervised, preference-aligned, diffusion-based, autoregressive online RL, and $π_0$-FAST baselines, observing consistent improvements over the imitation prior and strong alternatives with stable learning under sparse rewards. In addition, ablation studies and analyses of the latent space dynamics further highlight the contributions of individual components within FPO, validating the effectiveness of the proposed computational modules and the stable convergence of the conditional flow-matching objective during online RL.

## Overview
Vision-Language-Action (VLA) models such as OpenVLA, Octo, and \(π_0\) have shown strong generalization by leveraging large-scale demonstrations, yet their performance is still fundamentally constrained by the quality and coverage of supervised data. Reinforcement learning (RL) provides a promising path for improving and fine-tuning VLAs through online interaction. However, conventional policy gradient methods are computationally infeasible in the context of flow-matching based models due to the intractability of the importance sampling process, which requires explicit computation of policy ratios. To overcome this limitation, we propose Flow Policy Optimization (FPO) algorithm, which reformulates importance sampling by leveraging per-sample changes in the conditional flow-matching objective. Furthermore, FPO achieves stable and scalable online reinforcement fine-tuning of the \(π_0\) model by integrating structure-aware credit assignment to enhance gradient efficiency, clipped surrogate objectives to stabilize optimization, multi-step latent exploration to encourage diverse policy updates, and a Q-ensemble mechanism to provide robust value estimation. We evaluate FPO on the LIBERO benchmark and the ALOHA simulation task against supervised, preference-aligned, diffusion-based, autoregressive online RL, and \(π_0\)-FAST baselines, observing consistent improvements over the imitation prior and strong alternatives with stable learning under sparse rewards. In addition, ablation studies and analyses of the latent space dynamics further highlight the contributions of individual components within FPO, validating the effectiveness of the proposed computational modules and the stable convergence of the conditional flow-matching objective during online RL.

## Content
Vision-Language-Action (VLA) models such as OpenVLA, Octo, and \(π_0\) have shown strong generalization by leveraging large-scale demonstrations, yet their performance is still fundamentally constrained by the quality and coverage of supervised data. Reinforcement learning (RL) provides a promising path for improving and fine-tuning VLAs through online interaction. However, conventional policy gradient methods are computationally infeasible in the context of flow-matching based models due to the intractability of the importance sampling process, which requires explicit computation of policy ratios. To overcome this limitation, we propose Flow Policy Optimization (FPO) algorithm, which reformulates importance sampling by leveraging per-sample changes in the conditional flow-matching objective. Furthermore, FPO achieves stable and scalable online reinforcement fine-tuning of the \(π_0\) model by integrating structure-aware credit assignment to enhance gradient efficiency, clipped surrogate objectives to stabilize optimization, multi-step latent exploration to encourage diverse policy updates, and a Q-ensemble mechanism to provide robust value estimation. We evaluate FPO on the LIBERO benchmark and the ALOHA simulation task against supervised, preference-aligned, diffusion-based, autoregressive online RL, and \(π_0\)-FAST baselines, observing consistent improvements over the imitation prior and strong alternatives with stable learning under sparse rewards. In addition, ablation studies and analyses of the latent space dynamics further highlight the contributions of individual components within FPO, validating the effectiveness of the proposed computational modules and the stable convergence of the conditional flow-matching objective during online RL.

## 参考
- http://arxiv.org/abs/2510.09976v2

## 개요
시각-언어-행동 모델(OpenVLA, Octo, $π_0$ 등)은 대규모 시연 데이터를 통해 강력한 일반화 능력을 보여주지만, 그 성능은 여전히 감독 데이터의 품질과 범위에 제한을 받습니다. 강화 학습은 VLA 모델의 온라인 미세 조정을 위한 실현 가능한 경로를 제공하지만, 전통적인 정책 경사 방법은 정책 비율의 명시적 계산을 요구하기 때문에 흐름 매칭 모델 맥락에서 계산상 비실현 가능성이 존재합니다. 이를 해결하기 위해, 본 논문은 조건부 흐름 매칭 목표에서 각 샘플의 변화를 활용하여 중요도 샘플링을 재정의하는 Flow Policy Optimization 알고리즘을 제안합니다. FPO는 또한 구조 인식 신용 할당, 클리핑 대체 목표, 다단계 잠재 탐색 및 Q-ensemble 메커니즘을 통합하여 $π_0$ 모델의 안정적이고 확장 가능한 온라인 강화 미세 조정을 구현합니다.

## 핵심 내용
### 방법 아키텍처
- **Flow Policy Optimization (FPO) 알고리즘**: 핵심 혁신은 중요도 샘플링 과정을 재정의하여 조건부 흐름 매칭 목표에서 각 샘플의 변화를 활용함으로써 전통적인 정책 비율의 명시적 계산을 피하고, 흐름 매칭 모델의 계산상 비실현 가능성 문제를 해결하는 것입니다.
- **구조 인식 신용 할당**: 기울기 효율성을 향상시켜 모델이 희소 보상에서 더 효과적으로 학습할 수 있게 합니다.
- **클리핑 대체 목표**: 최적화 과정을 안정화하여 정책 업데이트가 과도하게 커져 훈련이 불안정해지는 것을 방지합니다.
- **다단계 잠재 탐색**: 다양한 정책 업데이트를 장려하여 탐색 효율성을 높입니다.
- **Q-ensemble 메커니즘**: 견고한 가치 추정을 제공하여 가치 함수 추정의 분산을 줄입니다.

### 실험 설정
- **벤치마크 테스트**: LIBERO 벤치마크 및 ALOHA 시뮬레이션 작업에서 평가를 수행합니다.
- **기준 방법**: 감독 학습, 선호도 정렬, 확산 모델, 자기회귀 온라인 RL 및 $π_0$-FAST 등의 방법과 비교합니다.
- **훈련 세부 사항**: 희소 보상 설정에서 온라인 강화 미세 조정을 수행하여 안정적인 학습 능력을 평가합니다.

### 주요 결과
- **성능 향상**: FPO는 모든 평가 작업에서 모방 학습 사전 및 강력한 기준 방법보다 일관되게 우수한 성능을 보이며, 안정적인 학습 과정을 입증합니다.
- **소거 연구**: 소거 실험을 통해 FPO의 각 구성 요소(구조 인식 신용 할당, 클리핑 목표, 다단계 탐색, Q-ensemble)의 기여를 검증하고, 각 계산 모듈의 효과를 확인합니다.
- **잠재 공간 역학**: 분석 결과, 온라인 RL 과정에서 조건부 흐름 매칭 목표가 안정적으로 수렴하여 FPO 알고리즘의 효과를 추가로 검증합니다.
