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
  zh: 'STORM: Search-Guided Generative World Models for Robotic Manipulation (STORM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18477v1.
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
We present STORM (Search-Guided Generative World Models), a novel framework for spatio-temporal reasoning in robotic manipulation that unifies diffusion-based action generation, conditional video prediction, and search-based planning. Unlike prior Vision-Language-Action (VLA) models that rely on abstract latent dynamics or delegate reasoning to language components, STORM grounds planning in explicit visual rollouts, enabling interpretable and foresight-driven decision-making. A diffusion-based VLA policy proposes diverse candidate actions, a generative video world model simulates their visual and reward outcomes, and Monte Carlo Tree Search (MCTS) selectively refines plans through lookahead evaluation. Experiments on the SimplerEnv manipulation benchmark demonstrate that STORM achieves a new state-of-the-art average success rate of 51.0 percent, outperforming strong baselines such as CogACT. Reward-augmented video prediction substantially improves spatio-temporal fidelity and task relevance, reducing Frechet Video Distance by over 75 percent. Moreover, STORM exhibits robust re-planning and failure recovery behavior, highlighting the advantages of search-guided generative world models for long-horizon robotic manipulation.

## 核心内容
We present STORM (Search-Guided Generative World Models), a novel framework for spatio-temporal reasoning in robotic manipulation that unifies diffusion-based action generation, conditional video prediction, and search-based planning. Unlike prior Vision-Language-Action (VLA) models that rely on abstract latent dynamics or delegate reasoning to language components, STORM grounds planning in explicit visual rollouts, enabling interpretable and foresight-driven decision-making. A diffusion-based VLA policy proposes diverse candidate actions, a generative video world model simulates their visual and reward outcomes, and Monte Carlo Tree Search (MCTS) selectively refines plans through lookahead evaluation. Experiments on the SimplerEnv manipulation benchmark demonstrate that STORM achieves a new state-of-the-art average success rate of 51.0 percent, outperforming strong baselines such as CogACT. Reward-augmented video prediction substantially improves spatio-temporal fidelity and task relevance, reducing Frechet Video Distance by over 75 percent. Moreover, STORM exhibits robust re-planning and failure recovery behavior, highlighting the advantages of search-guided generative world models for long-horizon robotic manipulation.

## 参考
- http://arxiv.org/abs/2512.18477v1

## Overview
We present STORM (Search-Guided Generative World Models), a novel framework for spatio-temporal reasoning in robotic manipulation that unifies diffusion-based action generation, conditional video prediction, and search-based planning. Unlike prior Vision-Language-Action (VLA) models that rely on abstract latent dynamics or delegate reasoning to language components, STORM grounds planning in explicit visual rollouts, enabling interpretable and foresight-driven decision-making. A diffusion-based VLA policy proposes diverse candidate actions, a generative video world model simulates their visual and reward outcomes, and Monte Carlo Tree Search (MCTS) selectively refines plans through lookahead evaluation. Experiments on the SimplerEnv manipulation benchmark demonstrate that STORM achieves a new state-of-the-art average success rate of 51.0 percent, outperforming strong baselines such as CogACT. Reward-augmented video prediction substantially improves spatio-temporal fidelity and task relevance, reducing Frechet Video Distance by over 75 percent. Moreover, STORM exhibits robust re-planning and failure recovery behavior, highlighting the advantages of search-guided generative world models for long-horizon robotic manipulation.

## Content
We present STORM (Search-Guided Generative World Models), a novel framework for spatio-temporal reasoning in robotic manipulation that unifies diffusion-based action generation, conditional video prediction, and search-based planning. Unlike prior Vision-Language-Action (VLA) models that rely on abstract latent dynamics or delegate reasoning to language components, STORM grounds planning in explicit visual rollouts, enabling interpretable and foresight-driven decision-making. A diffusion-based VLA policy proposes diverse candidate actions, a generative video world model simulates their visual and reward outcomes, and Monte Carlo Tree Search (MCTS) selectively refines plans through lookahead evaluation. Experiments on the SimplerEnv manipulation benchmark demonstrate that STORM achieves a new state-of-the-art average success rate of 51.0 percent, outperforming strong baselines such as CogACT. Reward-augmented video prediction substantially improves spatio-temporal fidelity and task relevance, reducing Frechet Video Distance by over 75 percent. Moreover, STORM exhibits robust re-planning and failure recovery behavior, highlighting the advantages of search-guided generative world models for long-horizon robotic manipulation.

## 개요
본 논문에서는 로봇 조작 작업에서 시공간 추론을 위한 새로운 프레임워크인 STORM(Search-Guided Generative World Models)을 제시합니다. STORM은 확산 기반 행동 생성, 조건부 비디오 예측, 탐색 기반 계획을 통합합니다. 추상적인 잠재 역학에 의존하거나 추론을 언어 구성 요소에 위임하는 기존의 VLA(Vision-Language-Action) 모델과 달리, STORM은 명시적인 시각적 롤아웃에 계획을 기반으로 하여 해석 가능하고 예측 기반의 의사 결정을 가능하게 합니다. 확산 기반 VLA 정책은 다양한 후보 행동을 제안하고, 생성형 비디오 월드 모델은 해당 행동의 시각적 결과와 보상 결과를 시뮬레이션하며, MCTS(Monte Carlo Tree Search)는 예측 평가를 통해 계획을 선택적으로 개선합니다. SimplerEnv 조작 벤치마크 실험에서 STORM은 51.0%의 새로운 최고 평균 성공률을 달성하여 CogACT와 같은 강력한 기준 모델을 능가했습니다. 보상 강화 비디오 예측은 시공간 충실도와 작업 관련성을 크게 개선하여 Frechet Video Distance를 75% 이상 감소시켰습니다. 또한 STORM은 강력한 재계획 및 실패 복구 동작을 보여주며, 장기 로봇 조작을 위한 탐색 유도 생성형 월드 모델의 장점을 강조합니다.

## 핵심 내용
본 논문에서는 로봇 조작 작업에서 시공간 추론을 위한 새로운 프레임워크인 STORM(Search-Guided Generative World Models)을 제시합니다. STORM은 확산 기반 행동 생성, 조건부 비디오 예측, 탐색 기반 계획을 통합합니다. 추상적인 잠재 역학에 의존하거나 추론을 언어 구성 요소에 위임하는 기존의 VLA(Vision-Language-Action) 모델과 달리, STORM은 명시적인 시각적 롤아웃에 계획을 기반으로 하여 해석 가능하고 예측 기반의 의사 결정을 가능하게 합니다. 확산 기반 VLA 정책은 다양한 후보 행동을 제안하고, 생성형 비디오 월드 모델은 해당 행동의 시각적 결과와 보상 결과를 시뮬레이션하며, MCTS(Monte Carlo Tree Search)는 예측 평가를 통해 계획을 선택적으로 개선합니다. SimplerEnv 조작 벤치마크 실험에서 STORM은 51.0%의 새로운 최고 평균 성공률을 달성하여 CogACT와 같은 강력한 기준 모델을 능가했습니다. 보상 강화 비디오 예측은 시공간 충실도와 작업 관련성을 크게 개선하여 Frechet Video Distance를 75% 이상 감소시켰습니다. 또한 STORM은 강력한 재계획 및 실패 복구 동작을 보여주며, 장기 로봇 조작을 위한 탐색 유도 생성형 월드 모델의 장점을 강조합니다.
