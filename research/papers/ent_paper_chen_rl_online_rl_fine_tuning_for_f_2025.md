---
$id: ent_paper_chen_rl_online_rl_fine_tuning_for_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models'
  zh: π_RL
  ko: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models'
summary:
  en: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models (π_RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Peking University, Institute of Automation, Chinese
    Academy of Sciences, Carnegie Mellon University, Infinigence AI, Zhongguancun Academy.'
  zh: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models (π_RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Peking University, Institute of Automation, Chinese
    Academy of Sciences, Carnegie Mellon University, Infinigence AI, Zhongguancun Academy.'
  ko: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models (π_RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Peking University, Institute of Automation, Chinese
    Academy of Sciences, Carnegie Mellon University, Infinigence AI, Zhongguancun Academy.'
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
- rl
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25889v3.
sources:
- id: src_001
  type: paper
  title: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.25889
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: π_RL source
  url: https://doi.org/10.48550/arXiv.2510.25889
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models enable robots to understand and perform complex tasks from multimodal input. Although recent work explores using reinforcement learning (RL) to automate the laborious data collection process in scaling supervised fine-tuning (SFT), applying RL to large-scale flow-based VLAs (\eg, $π_0$, $π_{0.5}$) remains challenging due to intractable action log-likelihoods raised from flow matching. We address this challenge with $π_{\texttt{RL}}$, featuring two technical approaches: (1) \textbf{Flow-Noise} models the denoising process as a discrete-time MDP with a learnable noise network for exact log-likelihood computation. (2) \textbf{Flow-SDE} integrates denoising with agent-environment interaction, formulating a two-layer MDP that employs ODE-to-SDE conversion for efficient RL exploration. We evaluate $π_{\texttt{RL}}$ across various benchmarks, with experiments demonstrating that RL yields significant performance improvements in both in-distribution and out-of-distribution settings.

## 核心内容
Vision-Language-Action (VLA) models enable robots to understand and perform complex tasks from multimodal input. Although recent work explores using reinforcement learning (RL) to automate the laborious data collection process in scaling supervised fine-tuning (SFT), applying RL to large-scale flow-based VLAs (\eg, $π_0$, $π_{0.5}$) remains challenging due to intractable action log-likelihoods raised from flow matching. We address this challenge with $π_{\texttt{RL}}$, featuring two technical approaches: (1) \textbf{Flow-Noise} models the denoising process as a discrete-time MDP with a learnable noise network for exact log-likelihood computation. (2) \textbf{Flow-SDE} integrates denoising with agent-environment interaction, formulating a two-layer MDP that employs ODE-to-SDE conversion for efficient RL exploration. We evaluate $π_{\texttt{RL}}$ across various benchmarks, with experiments demonstrating that RL yields significant performance improvements in both in-distribution and out-of-distribution settings.

## 参考
- http://arxiv.org/abs/2510.25889v3

## Overview
Vision-Language-Action (VLA) models enable robots to understand and perform complex tasks from multimodal input. Although recent work explores using reinforcement learning (RL) to automate the laborious data collection process in scaling supervised fine-tuning (SFT), applying RL to large-scale flow-based VLAs (\eg, $π_0$, $π_{0.5}$) remains challenging due to intractable action log-likelihoods raised from flow matching. We address this challenge with $π_{\texttt{RL}}$, featuring two technical approaches: (1) \textbf{Flow-Noise} models the denoising process as a discrete-time MDP with a learnable noise network for exact log-likelihood computation. (2) \textbf{Flow-SDE} integrates denoising with agent-environment interaction, formulating a two-layer MDP that employs ODE-to-SDE conversion for efficient RL exploration. We evaluate $π_{\texttt{RL}}$ across various benchmarks, with experiments demonstrating that RL yields significant performance improvements in both in-distribution and out-of-distribution settings.

## Content
Vision-Language-Action (VLA) models enable robots to understand and perform complex tasks from multimodal input. Although recent work explores using reinforcement learning (RL) to automate the laborious data collection process in scaling supervised fine-tuning (SFT), applying RL to large-scale flow-based VLAs (\eg, $π_0$, $π_{0.5}$) remains challenging due to intractable action log-likelihoods raised from flow matching. We address this challenge with $π_{\texttt{RL}}$, featuring two technical approaches: (1) \textbf{Flow-Noise} models the denoising process as a discrete-time MDP with a learnable noise network for exact log-likelihood computation. (2) \textbf{Flow-SDE} integrates denoising with agent-environment interaction, formulating a two-layer MDP that employs ODE-to-SDE conversion for efficient RL exploration. We evaluate $π_{\texttt{RL}}$ across various benchmarks, with experiments demonstrating that RL yields significant performance improvements in both in-distribution and out-of-distribution settings.

## 개요
Vision-Language-Action (VLA) 모델은 로봇이 멀티모달 입력을 통해 복잡한 작업을 이해하고 수행할 수 있도록 합니다. 최근 연구에서는 강화 학습(RL)을 활용하여 지도 미세 조정(SFT) 확장 과정에서의 번거로운 데이터 수집을 자동화하려는 시도가 있었지만, 대규모 플로우 기반 VLA(예: $π_0$, $π_{0.5}$)에 RL을 적용하는 것은 플로우 매칭에서 발생하는 다루기 어려운 행동 로그 우도(log-likelihood)로 인해 여전히 어려움이 있습니다. 우리는 이 문제를 $π_{\texttt{RL}}$로 해결하며, 두 가지 기술적 접근법을 제시합니다: (1) **Flow-Noise**는 잡음 제거 과정을 이산 시간 MDP로 모델링하고, 학습 가능한 잡음 네트워크를 통해 정확한 로그 우도를 계산합니다. (2) **Flow-SDE**는 잡음 제거를 에이전트-환경 상호작용과 통합하여, ODE-to-SDE 변환을 활용한 효율적인 RL 탐색을 위해 이중 계층 MDP를 구성합니다. 우리는 다양한 벤치마크에서 $π_{\texttt{RL}}$을 평가했으며, 실험 결과 RL이 분포 내 및 분포 외 설정 모두에서 상당한 성능 향상을 가져옴을 입증했습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇이 멀티모달 입력을 통해 복잡한 작업을 이해하고 수행할 수 있도록 합니다. 최근 연구에서는 강화 학습(RL)을 활용하여 지도 미세 조정(SFT) 확장 과정에서의 번거로운 데이터 수집을 자동화하려는 시도가 있었지만, 대규모 플로우 기반 VLA(예: $π_0$, $π_{0.5}$)에 RL을 적용하는 것은 플로우 매칭에서 발생하는 다루기 어려운 행동 로그 우도(log-likelihood)로 인해 여전히 어려움이 있습니다. 우리는 이 문제를 $π_{\texttt{RL}}$로 해결하며, 두 가지 기술적 접근법을 제시합니다: (1) **Flow-Noise**는 잡음 제거 과정을 이산 시간 MDP로 모델링하고, 학습 가능한 잡음 네트워크를 통해 정확한 로그 우도를 계산합니다. (2) **Flow-SDE**는 잡음 제거를 에이전트-환경 상호작용과 통합하여, ODE-to-SDE 변환을 활용한 효율적인 RL 탐색을 위해 이중 계층 MDP를 구성합니다. 우리는 다양한 벤치마크에서 $π_{\texttt{RL}}$을 평가했으며, 실험 결과 RL이 분포 내 및 분포 외 설정 모두에서 상당한 성능 향상을 가져옴을 입증했습니다.
