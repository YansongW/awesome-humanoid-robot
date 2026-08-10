---
$id: ent_paper_li_simplevla_rl_scaling_vla_train_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning'
  zh: SimpleVLA-RL
  ko: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning'
summary:
  en: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (SimpleVLA-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Tsinghua University.'
  zh: SimpleVLA-RL 是由北京大学和清华大学提出的一个高效强化学习框架，旨在提升视觉-语言-动作（VLA）模型的机器人操作能力。其核心贡献在于通过引入轨迹采样、并行化、多环境渲染和优化损失计算等 VLA 特定技术，在 LIBERO
    和 RoboTwin 基准上取得了最先进性能，并显著减少了大规模数据依赖。
  ko: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (SimpleVLA-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Tsinghua University.'
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
- simplevla_rl
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09674v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (959 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2509.09674
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SimpleVLA-RL source
  url: https://doi.org/10.48550/arXiv.2509.09674
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
SimpleVLA-RL 针对当前 VLA 模型在监督微调（SFT）中面临的数据稀缺和泛化能力不足问题，提出了一种基于强化学习（RL）的解决方案。该框架构建于 veRL 之上，通过 VLA 特定的轨迹采样、可扩展并行化、多环境渲染和优化损失计算，有效提升了模型的长程动作规划能力。实验表明，SimpleVLA-RL 在 LIBERO 基准上达到最先进水平，并在 RoboTwin 1.0 和 2.0 上超越了 π₀ 模型，同时在实际任务中展现出优于 SFT 的泛化性能。

## 核心内容
### 方法
SimpleVLA-RL 的核心是一个为 VLA 模型量身定制的强化学习框架，基于 veRL 构建。其关键创新包括：
- **VLA 特定轨迹采样**：针对机器人操作任务的长程特性，设计了专门的采样策略以高效利用经验。
- **可扩展并行化**：支持多环境并行渲染和训练，大幅提升训练效率。
- **优化损失计算**：调整 RL 损失函数以适配 VLA 模型的输出结构，确保稳定训练。

### 实验设置
- **基础模型**：采用 OpenVLA-OFT 作为预训练 VLA 模型。
- **基准测试**：在 LIBERO 和 RoboTwin 1.0/2.0 上进行评估。
- **对比方法**：与 SFT 训练的 VLA 模型及 π₀ 模型进行对比。

### 关键结果
- **性能提升**：SimpleVLA-RL 在 LIBERO 上达到最先进水平（SoTA），并在 RoboTwin 1.0 和 2.0 上超越 π₀ 模型。
- **数据效率**：显著降低了对大规模人类操作轨迹的依赖，仅需少量数据即可实现鲁棒泛化。
- **真实世界任务**：在实际机器人操作任务中，RL 训练的效果明显优于 SFT。
- **新发现**：在 RL 训练过程中，观察到一种名为“pushcut”的新现象，即策略能够发现训练数据中从未出现过的动作模式，表明 RL 能激发模型的探索能力。

### 结论
SimpleVLA-RL 证明了强化学习可以有效提升 VLA 模型的长程动作规划能力，减少对大规模数据的依赖，并增强泛化性能。该框架为未来 VLA 模型的训练提供了新范式，其代码已开源在 GitHub。

## Overview
Vision-Language-Action (VLA) models have recently emerged as a powerful paradigm for robotic manipulation. Despite substantial progress enabled by large-scale pretraining and supervised fine-tuning (SFT), these models face two fundamental challenges: (i) the scarcity and high cost of large-scale human-operated robotic trajectories required for SFT scaling, and (ii) limited generalization to tasks involving distribution shift. Recent breakthroughs in Large Reasoning Models (LRMs) demonstrate that reinforcement learning (RL) can dramatically enhance step-by-step reasoning capabilities, raising a natural question: Can RL similarly improve the long-horizon step-by-step action planning of VLA? In this work, we introduce SimpleVLA-RL, an efficient RL framework tailored for VLA models. Building upon veRL, we introduce VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, and optimized loss computation. When applied to OpenVLA-OFT, SimpleVLA-RL achieves SoTA performance on LIBERO and even outperforms $π_0$ on RoboTwin 1.0\&2.0 with the exploration-enhancing strategies we introduce. SimpleVLA-RL not only reduces dependence on large-scale data and enables robust generalization, but also remarkably surpasses SFT in real-world tasks. Moreover, we identify a novel phenomenon ``pushcut'' during RL training, wherein the policy discovers previously unseen patterns beyond those seen in the previous training process. Github: https://github.com/PRIME-RL/SimpleVLA-RL

## 参考
- http://arxiv.org/abs/2509.09674v1

## 개요
SimpleVLA-RL은 현재 VLA 모델이 지도 미세 조정(SFT)에서 직면하는 데이터 부족 및 일반화 능력 부족 문제를 해결하기 위해 강화 학습(RL) 기반 솔루션을 제안합니다. 이 프레임워크는 veRL 위에 구축되었으며, VLA 특화 궤적 샘플링, 확장 가능한 병렬화, 다중 환경 렌더링 및 최적화된 손실 계산을 통해 모델의 장기 동작 계획 능력을 효과적으로 향상시킵니다. 실험 결과, SimpleVLA-RL은 LIBERO 벤치마크에서 최첨단 수준에 도달했으며, RoboTwin 1.0 및 2.0에서 π₀ 모델을 능가했고, 실제 작업에서 SFT보다 우수한 일반화 성능을 보여주었습니다.

## 핵심 내용
### 방법
SimpleVLA-RL의 핵심은 veRL 기반으로 구축된 VLA 모델에 맞춤화된 강화 학습 프레임워크입니다. 주요 혁신은 다음과 같습니다:
- **VLA 특화 궤적 샘플링**: 로봇 조작 작업의 장기적 특성을 고려하여 경험을 효율적으로 활용하기 위한 전용 샘플링 전략을 설계했습니다.
- **확장 가능한 병렬화**: 다중 환경 병렬 렌더링 및 훈련을 지원하여 훈련 효율성을 크게 향상시킵니다.
- **최적화된 손실 계산**: RL 손실 함수를 VLA 모델의 출력 구조에 맞게 조정하여 안정적인 훈련을 보장합니다.

### 실험 설정
- **기본 모델**: OpenVLA-OFT를 사전 훈련된 VLA 모델로 사용합니다.
- **벤치마크 테스트**: LIBERO 및 RoboTwin 1.0/2.0에서 평가합니다.
- **비교 방법**: SFT로 훈련된 VLA 모델 및 π₀ 모델과 비교합니다.

### 주요 결과
- **성능 향상**: SimpleVLA-RL은 LIBERO에서 최첨단 수준(SoTA)에 도달했으며, RoboTwin 1.0 및 2.0에서 π₀ 모델을 능가했습니다.
- **데이터 효율성**: 대규모 인간 조작 궤적에 대한 의존도를 크게 줄였으며, 소량의 데이터만으로도 강력한 일반화를 달성합니다.
- **실제 세계 작업**: 실제 로봇 조작 작업에서 RL 훈련 효과가 SFT보다 명확히 우수합니다.
- **새로운 발견**: RL 훈련 과정에서 "pushcut"이라는 새로운 현상이 관찰되었으며, 이는 정책이 훈련 데이터에 전혀 등장하지 않은 동작 패턴을 발견할 수 있음을 의미합니다. 이는 RL이 모델의 탐색 능력을 자극할 수 있음을 보여줍니다.

### 결론
SimpleVLA-RL은 강화 학습이 VLA 모델의 장기 동작 계획 능력을 효과적으로 향상시키고, 대규모 데이터 의존성을 줄이며, 일반화 성능을 강화할 수 있음을 입증했습니다. 이 프레임워크는 향후 VLA 모델 훈련을 위한 새로운 패러다임을 제공하며, 코드는 GitHub에 오픈소스로 공개되어 있습니다.
