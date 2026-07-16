---
$id: ent_paper_neary_improving_pre_trained_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search
  zh: VLAPS
  ko: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search
summary:
  en: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search (VLAPS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mila — Quebec AI Institute, Universit´e de Montr´eal, The University of
    British Columbia.
  zh: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search (VLAPS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mila — Quebec AI Institute, Universit´e de Montr´eal, The University of
    British Columbia.
  ko: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search (VLAPS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mila — Quebec AI Institute, Universit´e de Montr´eal, The University of
    British Columbia.
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
- vision_language_action
- vla
- vlaps
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.12211v2.
sources:
- id: src_001
  type: paper
  title: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search (arXiv)
  url: https://arxiv.org/abs/2508.12211
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLAPS source
  url: https://doi.org/10.48550/arXiv.2508.12211
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Pre-trained vision-language-action (VLA) models offer a promising foundation for generalist robot policies, but often produce brittle behaviors or unsafe failures when deployed zero-shot in out-of-distribution scenarios. We present Vision-Language-Action Planning & Search (VLAPS) -- a novel framework and accompanying algorithms that embed model-based search into the inference procedure of pre-trained VLA policies to improve their performance on robotic tasks. Specifically, our method biases a modified Monte Carlo Tree Search (MCTS) algorithm -- run using a model of the target environment -- using action priors defined by the VLA policy. By using VLA-derived abstractions and priors in model-based search, VLAPS efficiently explores language-conditioned robotics tasks whose search spaces would otherwise be intractably large. Conversely, by integrating model-based search with the VLA policy's inference procedure, VLAPS yields behaviors that are more performant than those obtained by directly following the VLA policy's action predictions. VLAPS offers a principled framework to: i) control test-time compute in VLA models, ii) leverage a priori knowledge of the robotic environment, and iii) integrate established planning and reinforcement learning techniques into the VLA inference process. Across all experiments, VLAPS significantly outperforms VLA-only baselines on language-specified tasks that would otherwise be intractable for uninformed search algorithms, increasing success rates by as much as 67 percentage points.

## 核心内容
Pre-trained vision-language-action (VLA) models offer a promising foundation for generalist robot policies, but often produce brittle behaviors or unsafe failures when deployed zero-shot in out-of-distribution scenarios. We present Vision-Language-Action Planning & Search (VLAPS) -- a novel framework and accompanying algorithms that embed model-based search into the inference procedure of pre-trained VLA policies to improve their performance on robotic tasks. Specifically, our method biases a modified Monte Carlo Tree Search (MCTS) algorithm -- run using a model of the target environment -- using action priors defined by the VLA policy. By using VLA-derived abstractions and priors in model-based search, VLAPS efficiently explores language-conditioned robotics tasks whose search spaces would otherwise be intractably large. Conversely, by integrating model-based search with the VLA policy's inference procedure, VLAPS yields behaviors that are more performant than those obtained by directly following the VLA policy's action predictions. VLAPS offers a principled framework to: i) control test-time compute in VLA models, ii) leverage a priori knowledge of the robotic environment, and iii) integrate established planning and reinforcement learning techniques into the VLA inference process. Across all experiments, VLAPS significantly outperforms VLA-only baselines on language-specified tasks that would otherwise be intractable for uninformed search algorithms, increasing success rates by as much as 67 percentage points.

## 参考
- http://arxiv.org/abs/2508.12211v2

## Overview
Pre-trained vision-language-action (VLA) models offer a promising foundation for generalist robot policies, but often produce brittle behaviors or unsafe failures when deployed zero-shot in out-of-distribution scenarios. We present Vision-Language-Action Planning & Search (VLAPS) -- a novel framework and accompanying algorithms that embed model-based search into the inference procedure of pre-trained VLA policies to improve their performance on robotic tasks. Specifically, our method biases a modified Monte Carlo Tree Search (MCTS) algorithm -- run using a model of the target environment -- using action priors defined by the VLA policy. By using VLA-derived abstractions and priors in model-based search, VLAPS efficiently explores language-conditioned robotics tasks whose search spaces would otherwise be intractably large. Conversely, by integrating model-based search with the VLA policy's inference procedure, VLAPS yields behaviors that are more performant than those obtained by directly following the VLA policy's action predictions. VLAPS offers a principled framework to: i) control test-time compute in VLA models, ii) leverage a priori knowledge of the robotic environment, and iii) integrate established planning and reinforcement learning techniques into the VLA inference process. Across all experiments, VLAPS significantly outperforms VLA-only baselines on language-specified tasks that would otherwise be intractable for uninformed search algorithms, increasing success rates by as much as 67 percentage points.

## Content
Pre-trained vision-language-action (VLA) models offer a promising foundation for generalist robot policies, but often produce brittle behaviors or unsafe failures when deployed zero-shot in out-of-distribution scenarios. We present Vision-Language-Action Planning & Search (VLAPS) -- a novel framework and accompanying algorithms that embed model-based search into the inference procedure of pre-trained VLA policies to improve their performance on robotic tasks. Specifically, our method biases a modified Monte Carlo Tree Search (MCTS) algorithm -- run using a model of the target environment -- using action priors defined by the VLA policy. By using VLA-derived abstractions and priors in model-based search, VLAPS efficiently explores language-conditioned robotics tasks whose search spaces would otherwise be intractably large. Conversely, by integrating model-based search with the VLA policy's inference procedure, VLAPS yields behaviors that are more performant than those obtained by directly following the VLA policy's action predictions. VLAPS offers a principled framework to: i) control test-time compute in VLA models, ii) leverage a priori knowledge of the robotic environment, and iii) integrate established planning and reinforcement learning techniques into the VLA inference process. Across all experiments, VLAPS significantly outperforms VLA-only baselines on language-specified tasks that would otherwise be intractable for uninformed search algorithms, increasing success rates by as much as 67 percentage points.

## 개요
사전 훈련된 시각-언어-행동(VLA) 모델은 범용 로봇 정책을 위한 유망한 기반을 제공하지만, 분포 외 시나리오에서 제로샷으로 배치될 때 취약한 행동이나 안전하지 않은 실패를 자주 초래합니다. 본 논문에서는 사전 훈련된 VLA 정책의 추론 과정에 모델 기반 탐색을 내장하여 로봇 작업 성능을 향상시키는 새로운 프레임워크이자 알고리즘인 VLAPS(Vision-Language-Action Planning & Search)를 제시합니다. 구체적으로, 우리 방법은 VLA 정책이 정의한 행동 사전 확률을 사용하여 대상 환경의 모델을 기반으로 실행되는 수정된 몬테카를로 트리 탐색(MCTS) 알고리즘에 편향을 부여합니다. VLA에서 파생된 추상화와 사전 확률을 모델 기반 탐색에 활용함으로써, VLAPS는 그렇지 않으면 다루기 힘들 정도로 큰 탐색 공간을 가진 언어 조건부 로봇 작업을 효율적으로 탐색합니다. 반대로, 모델 기반 탐색을 VLA 정책의 추론 과정과 통합함으로써, VLAPS는 VLA 정책의 행동 예측을 직접 따를 때보다 더 우수한 성능의 행동을 생성합니다. VLAPS는 다음과 같은 원칙적인 프레임워크를 제공합니다: i) VLA 모델의 테스트 시간 계산 제어, ii) 로봇 환경에 대한 사전 지식 활용, iii) 기존의 계획 및 강화 학습 기술을 VLA 추론 과정에 통합. 모든 실험에서 VLAPS는 정보 없는 탐색 알고리즘으로는 다루기 힘든 언어 지정 작업에서 VLA 전용 기준선을 크게 능가하며, 성공률을 최대 67% 포인트까지 향상시킵니다.

## 핵심 내용
사전 훈련된 시각-언어-행동(VLA) 모델은 범용 로봇 정책을 위한 유망한 기반을 제공하지만, 분포 외 시나리오에서 제로샷으로 배치될 때 취약한 행동이나 안전하지 않은 실패를 자주 초래합니다. 본 논문에서는 사전 훈련된 VLA 정책의 추론 과정에 모델 기반 탐색을 내장하여 로봇 작업 성능을 향상시키는 새로운 프레임워크이자 알고리즘인 VLAPS(Vision-Language-Action Planning & Search)를 제시합니다. 구체적으로, 우리 방법은 VLA 정책이 정의한 행동 사전 확률을 사용하여 대상 환경의 모델을 기반으로 실행되는 수정된 몬테카를로 트리 탐색(MCTS) 알고리즘에 편향을 부여합니다. VLA에서 파생된 추상화와 사전 확률을 모델 기반 탐색에 활용함으로써, VLAPS는 그렇지 않으면 다루기 힘들 정도로 큰 탐색 공간을 가진 언어 조건부 로봇 작업을 효율적으로 탐색합니다. 반대로, 모델 기반 탐색을 VLA 정책의 추론 과정과 통합함으로써, VLAPS는 VLA 정책의 행동 예측을 직접 따를 때보다 더 우수한 성능의 행동을 생성합니다. VLAPS는 다음과 같은 원칙적인 프레임워크를 제공합니다: i) VLA 모델의 테스트 시간 계산 제어, ii) 로봇 환경에 대한 사전 지식 활용, iii) 기존의 계획 및 강화 학습 기술을 VLA 추론 과정에 통합. 모든 실험에서 VLAPS는 정보 없는 탐색 알고리즘으로는 다루기 힘든 언어 지정 작업에서 VLA 전용 기준선을 크게 능가하며, 성공률을 최대 67% 포인트까지 향상시킵니다.
