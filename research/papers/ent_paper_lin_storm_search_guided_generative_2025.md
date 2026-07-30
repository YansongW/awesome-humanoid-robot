---
$id: ent_paper_lin_storm_search_guided_generative_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'STORM: Search-Guided Generative World Models for Robotic Manipulation'
  zh: STORM
  ko: 'STORM: Search-Guided Generative World Models for Robotic Manipulation'
summary:
  en: 'STORM: Search-Guided Generative World Models for Robotic Manipulation (STORM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University.'
  zh: STORM（Search-Guided Generative World Models）是中山大学于2025年提出的大型视觉-语言-动作模型，用于机器人操作中的时空推理。其核心贡献在于将扩散动作生成、条件视频预测与蒙特卡洛树搜索（MCTS）规划统一，通过显式视觉推演实现可解释的预见性决策。在SimplerEnv基准上，STORM以51.0%的平均成功率刷新了SOTA，并将Frechet
    Video Distance降低超过75%。
  ko: 'STORM: Search-Guided Generative World Models for Robotic Manipulation (STORM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University.'
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
- storm
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18477v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'STORM: Search-Guided Generative World Models for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.18477
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: STORM source
  url: https://doi.org/10.48550/arXiv.2512.18477
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
STORM框架突破了传统VLA模型依赖抽象潜在动力学或语言推理的局限，通过扩散策略生成多样候选动作，再由生成式视频世界模型模拟其视觉结果与奖励信号，最后利用MCTS进行前瞻性评估与计划优化。该方法在SimplerEnv操作基准上以51.0%的平均成功率超越CogACT等强基线，同时奖励增强的视频预测显著提升了时空保真度与任务相关性。此外，STORM展现出强大的重规划与故障恢复能力，验证了搜索引导生成世界模型在长时域机器人操作中的优势。

## 核心内容
### 方法架构
STORM由三个核心模块组成：
- **扩散式VLA策略**：基于扩散模型生成多样化的候选动作序列，避免单一动作的局部最优陷阱。
- **生成式视频世界模型**：以条件视频预测方式模拟每个候选动作的视觉结果与奖励信号，将规划过程显式化于像素空间。
- **MCTS规划器**：通过树搜索对候选动作进行前瞻性评估，选择性优化计划，实现可解释的决策回溯。

### 实验设置与关键结果
- **基准测试**：在SimplerEnv操作基准上评估，该基准包含多种长时域操作任务。
- **性能对比**：STORM以51.0%的平均成功率超越CogACT等基线，成为新SOTA。
- **视频预测质量**：奖励增强的视频预测将Frechet Video Distance（FVD）降低超过75%，显著提升时空一致性。
- **鲁棒性**：模型在失败场景中能自动触发重规划，展现出优于纯前馈策略的故障恢复能力。

### 结论
STORM通过将搜索引导的生成世界模型与扩散动作生成结合，为机器人操作提供了可解释、可回溯的规划框架。其显式视觉推演机制不仅提升了任务成功率，还通过MCTS的迭代优化实现了对长时域任务的适应性，为未来具身智能系统的决策透明化提供了新方向。

## Overview
We present STORM (Search-Guided Generative World Models), a novel framework for spatio-temporal reasoning in robotic manipulation that unifies diffusion-based action generation, conditional video prediction, and search-based planning. Unlike prior Vision-Language-Action (VLA) models that rely on abstract latent dynamics or delegate reasoning to language components, STORM grounds planning in explicit visual rollouts, enabling interpretable and foresight-driven decision-making. A diffusion-based VLA policy proposes diverse candidate actions, a generative video world model simulates their visual and reward outcomes, and Monte Carlo Tree Search (MCTS) selectively refines plans through lookahead evaluation. Experiments on the SimplerEnv manipulation benchmark demonstrate that STORM achieves a new state-of-the-art average success rate of 51.0 percent, outperforming strong baselines such as CogACT. Reward-augmented video prediction substantially improves spatio-temporal fidelity and task relevance, reducing Frechet Video Distance by over 75 percent. Moreover, STORM exhibits robust re-planning and failure recovery behavior, highlighting the advantages of search-guided generative world models for long-horizon robotic manipulation.

## 개요
본 논문에서는 로봇 조작 작업에서 시공간 추론을 위한 새로운 프레임워크인 STORM(Search-Guided Generative World Models)을 제시합니다. STORM은 확산 기반 행동 생성, 조건부 비디오 예측, 탐색 기반 계획을 통합합니다. 추상적인 잠재 역학에 의존하거나 추론을 언어 구성 요소에 위임하는 기존의 VLA(Vision-Language-Action) 모델과 달리, STORM은 명시적인 시각적 롤아웃에 계획을 기반으로 하여 해석 가능하고 예측 기반의 의사 결정을 가능하게 합니다. 확산 기반 VLA 정책은 다양한 후보 행동을 제안하고, 생성형 비디오 월드 모델은 해당 행동의 시각적 결과와 보상 결과를 시뮬레이션하며, MCTS(Monte Carlo Tree Search)는 예측 평가를 통해 계획을 선택적으로 개선합니다. SimplerEnv 조작 벤치마크 실험에서 STORM은 51.0%의 새로운 최고 평균 성공률을 달성하여 CogACT와 같은 강력한 기준 모델을 능가했습니다. 보상 강화 비디오 예측은 시공간 충실도와 작업 관련성을 크게 개선하여 Frechet Video Distance를 75% 이상 감소시켰습니다. 또한 STORM은 강력한 재계획 및 실패 복구 동작을 보여주며, 장기 로봇 조작을 위한 탐색 유도 생성형 월드 모델의 장점을 강조합니다.

## 핵심 내용
본 논문에서는 로봇 조작 작업에서 시공간 추론을 위한 새로운 프레임워크인 STORM(Search-Guided Generative World Models)을 제시합니다. STORM은 확산 기반 행동 생성, 조건부 비디오 예측, 탐색 기반 계획을 통합합니다. 추상적인 잠재 역학에 의존하거나 추론을 언어 구성 요소에 위임하는 기존의 VLA(Vision-Language-Action) 모델과 달리, STORM은 명시적인 시각적 롤아웃에 계획을 기반으로 하여 해석 가능하고 예측 기반의 의사 결정을 가능하게 합니다. 확산 기반 VLA 정책은 다양한 후보 행동을 제안하고, 생성형 비디오 월드 모델은 해당 행동의 시각적 결과와 보상 결과를 시뮬레이션하며, MCTS(Monte Carlo Tree Search)는 예측 평가를 통해 계획을 선택적으로 개선합니다. SimplerEnv 조작 벤치마크 실험에서 STORM은 51.0%의 새로운 최고 평균 성공률을 달성하여 CogACT와 같은 강력한 기준 모델을 능가했습니다. 보상 강화 비디오 예측은 시공간 충실도와 작업 관련성을 크게 개선하여 Frechet Video Distance를 75% 이상 감소시켰습니다. 또한 STORM은 강력한 재계획 및 실패 복구 동작을 보여주며, 장기 로봇 조작을 위한 탐색 유도 생성형 월드 모델의 장점을 강조합니다.

## 参考
- http://arxiv.org/abs/2512.18477v1
