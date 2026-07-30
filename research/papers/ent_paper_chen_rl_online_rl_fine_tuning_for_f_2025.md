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
  zh: πRL（π_RL）是由清华大学、北京大学、中国科学院自动化研究所、卡内基梅隆大学、Infinigence AI及中关村实验室联合提出的2025年大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过两种技术方案（Flow-Noise和Flow-SDE）解决了流匹配模型在强化学习微调中动作对数似然难以计算的问题，并在分布内与分布外场景中均取得显著性能提升。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25889v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
πRL针对现有流匹配型视觉-语言-动作模型（如π₀、π₀.₅）在强化学习微调时面临的挑战——流匹配导致动作对数似然难以计算——提出了两种创新方法。Flow-Noise将去噪过程建模为离散时间马尔可夫决策过程，并引入可学习噪声网络以实现精确的对数似然计算；Flow-SDE则通过ODE到SDE的转换，将去噪与智能体-环境交互整合为双层马尔可夫决策过程，从而支持高效的强化学习探索。实验表明，该方法在多个基准测试中均能显著提升模型在分布内与分布外场景下的表现。

## 核心内容
### 背景与挑战
- 视觉-语言-动作模型（VLA）使机器人能够基于多模态输入理解并执行复杂任务。
- 近期研究尝试使用强化学习（RL）替代人工数据收集以扩展监督微调（SFT），但将RL应用于大规模流匹配型VLA（如π₀、π₀.₅）时，因流匹配产生的动作对数似然难以计算而面临困难。

### 方法架构
#### Flow-Noise
- 将去噪过程建模为**离散时间马尔可夫决策过程（MDP）**。
- 引入**可学习噪声网络**，用于精确计算动作的对数似然，从而支持RL训练。

#### Flow-SDE
- 将去噪过程与智能体-环境交互整合为**双层马尔可夫决策过程**。
- 通过**ODE到SDE的转换**，在保持生成质量的同时引入随机性，以支持高效的RL探索。

### 实验设置与结果
- 在多个机器人操作基准上进行评估，涵盖**分布内（in-distribution）**与**分布外（out-of-distribution）**场景。
- 实验结果显示，RL微调在两种场景下均带来**显著的性能提升**，验证了πRL方法的有效性。

## Overview
Vision-Language-Action (VLA) models enable robots to understand and perform complex tasks from multimodal input. Although recent work explores using reinforcement learning (RL) to automate the laborious data collection process in scaling supervised fine-tuning (SFT), applying RL to large-scale flow-based VLAs (\eg, $π_0$, $π_{0.5}$) remains challenging due to intractable action log-likelihoods raised from flow matching. We address this challenge with $π_{\texttt{RL}}$, featuring two technical approaches: (1) \textbf{Flow-Noise} models the denoising process as a discrete-time MDP with a learnable noise network for exact log-likelihood computation. (2) \textbf{Flow-SDE} integrates denoising with agent-environment interaction, formulating a two-layer MDP that employs ODE-to-SDE conversion for efficient RL exploration. We evaluate $π_{\texttt{RL}}$ across various benchmarks, with experiments demonstrating that RL yields significant performance improvements in both in-distribution and out-of-distribution settings.

## 개요
Vision-Language-Action (VLA) 모델은 로봇이 멀티모달 입력을 통해 복잡한 작업을 이해하고 수행할 수 있도록 합니다. 최근 연구에서는 강화 학습(RL)을 활용하여 지도 미세 조정(SFT) 확장 과정에서의 번거로운 데이터 수집을 자동화하려는 시도가 있었지만, 대규모 플로우 기반 VLA(예: $π_0$, $π_{0.5}$)에 RL을 적용하는 것은 플로우 매칭에서 발생하는 다루기 어려운 행동 로그 우도(log-likelihood)로 인해 여전히 어려움이 있습니다. 우리는 이 문제를 $π_{\texttt{RL}}$로 해결하며, 두 가지 기술적 접근법을 제시합니다: (1) **Flow-Noise**는 잡음 제거 과정을 이산 시간 MDP로 모델링하고, 학습 가능한 잡음 네트워크를 통해 정확한 로그 우도를 계산합니다. (2) **Flow-SDE**는 잡음 제거를 에이전트-환경 상호작용과 통합하여, ODE-to-SDE 변환을 활용한 효율적인 RL 탐색을 위해 이중 계층 MDP를 구성합니다. 우리는 다양한 벤치마크에서 $π_{\texttt{RL}}$을 평가했으며, 실험 결과 RL이 분포 내 및 분포 외 설정 모두에서 상당한 성능 향상을 가져옴을 입증했습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇이 멀티모달 입력을 통해 복잡한 작업을 이해하고 수행할 수 있도록 합니다. 최근 연구에서는 강화 학습(RL)을 활용하여 지도 미세 조정(SFT) 확장 과정에서의 번거로운 데이터 수집을 자동화하려는 시도가 있었지만, 대규모 플로우 기반 VLA(예: $π_0$, $π_{0.5}$)에 RL을 적용하는 것은 플로우 매칭에서 발생하는 다루기 어려운 행동 로그 우도(log-likelihood)로 인해 여전히 어려움이 있습니다. 우리는 이 문제를 $π_{\texttt{RL}}$로 해결하며, 두 가지 기술적 접근법을 제시합니다: (1) **Flow-Noise**는 잡음 제거 과정을 이산 시간 MDP로 모델링하고, 학습 가능한 잡음 네트워크를 통해 정확한 로그 우도를 계산합니다. (2) **Flow-SDE**는 잡음 제거를 에이전트-환경 상호작용과 통합하여, ODE-to-SDE 변환을 활용한 효율적인 RL 탐색을 위해 이중 계층 MDP를 구성합니다. 우리는 다양한 벤치마크에서 $π_{\texttt{RL}}$을 평가했으며, 실험 결과 RL이 분포 내 및 분포 외 설정 모두에서 상당한 성능 향상을 가져옴을 입증했습니다.

## 参考
- http://arxiv.org/abs/2510.25889v3
