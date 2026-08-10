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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18477v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (772 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.18477v1

## 개요
STORM 프레임워크는 기존 VLA 모델이 추상적 잠재 역학 또는 언어 추론에 의존하는 한계를突破하여, 확산 정책을 통해 다양한 후보 행동을 생성하고, 생성형 비디오 세계 모델이 그 시각적 결과와 보상 신호를 시뮬레이션하며, 마지막으로 MCTS를 이용한 전향적 평가와 계획 최적화를 수행합니다. 이 방법은 SimplerEnv 조작 벤치마크에서 51.0%의 평균 성공률로 CogACT 등 강력한 베이스라인을 능가하며, 보상 강화 비디오 예측은 시공간 충실도와 작업 관련성을 크게 향상시킵니다. 또한 STORM은 강력한 재계획 및 장애 복구 능력을 보여주며, 검색 기반 생성 세계 모델이 장시간 로봇 조작에서의 우위를 검증합니다.

## 핵심 내용
### 방법 아키텍처
STORM은 세 가지 핵심 모듈로 구성됩니다:
- **확산형 VLA 정책**: 확산 모델을 기반으로 다양한 후보 행동 시퀀스를 생성하여 단일 행동의 지역 최적 함정을 피합니다.
- **생성형 비디오 세계 모델**: 조건부 비디오 예측 방식으로 각 후보 행동의 시각적 결과와 보상 신호를 시뮬레이션하여 계획 과정을 픽셀 공간에서 명시적으로 만듭니다.
- **MCTS 플래너**: 트리 검색을 통해 후보 행동을 전향적으로 평가하고 선택적으로 계획을 최적화하여 해석 가능한 결정 추적을 구현합니다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: 다양한 장시간 조작 작업을 포함하는 SimplerEnv 조작 벤치마크에서 평가되었습니다.
- **성능 비교**: STORM은 51.0%의 평균 성공률로 CogACT 등 베이스라인을 능가하며 새로운 SOTA가 되었습니다.
- **비디오 예측 품질**: 보상 강화 비디오 예측은 Frechet Video Distance(FVD)를 75% 이상 낮추어 시공간 일관성을 크게 향상시킵니다.
- **강건성**: 모델은 실패 시나리오에서 자동으로 재계획을 트리거하여 순수 피드포워드 정책보다 우수한 장애 복구 능력을 보여줍니다.

### 결론
STORM은 검색 기반 생성 세계 모델과 확산 행동 생성을 결합하여 로봇 조작을 위한 해석 가능하고 추적 가능한 계획 프레임워크를 제공합니다. 명시적 시각적 추론 메커니즘은 작업 성공률을 향상시킬 뿐만 아니라 MCTS의 반복 최적화를 통해 장시간 작업에 대한 적응성을 구현하며, 미래 임베디드 지능 시스템의 결정 투명성을 위한 새로운 방향을 제시합니다.
