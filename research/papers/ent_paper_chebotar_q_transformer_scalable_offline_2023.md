---
$id: ent_paper_chebotar_q_transformer_scalable_offline_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions'
  zh: Q-Transformer
  ko: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions'
summary:
  en: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions (Q-Transformer), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
  zh: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions (Q-Transformer), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
  ko: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions (Q-Transformer), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- q_transformer
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.10150v2.
sources:
- id: src_001
  type: paper
  title: Q-Transformer source
  url: https://proceedings.mlr.press/v229/chebotar23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and autonomously collected data. Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups. We therefore refer to the method as Q-Transformer. By discretizing each action dimension and representing the Q-value of each action dimension as separate tokens, we can apply effective high-capacity sequence modeling techniques for Q-learning. We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a large diverse real-world robotic manipulation task suite. The project's website and videos can be found at https://qtransformer.github.io

## 核心内容
In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and autonomously collected data. Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups. We therefore refer to the method as Q-Transformer. By discretizing each action dimension and representing the Q-value of each action dimension as separate tokens, we can apply effective high-capacity sequence modeling techniques for Q-learning. We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a large diverse real-world robotic manipulation task suite. The project's website and videos can be found at https://qtransformer.github.io

## 参考
- http://arxiv.org/abs/2309.10150v2

## Overview
In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and autonomously collected data. Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups. We therefore refer to the method as Q-Transformer. By discretizing each action dimension and representing the Q-value of each action dimension as separate tokens, we can apply effective high-capacity sequence modeling techniques for Q-learning. We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a large diverse real-world robotic manipulation task suite. The project's website and videos can be found at https://qtransformer.github.io

## Content
In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and autonomously collected data. Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups. We therefore refer to the method as Q-Transformer. By discretizing each action dimension and representing the Q-value of each action dimension as separate tokens, we can apply effective high-capacity sequence modeling techniques for Q-learning. We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a large diverse real-world robotic manipulation task suite. The project's website and videos can be found at https://qtransformer.github.io

## 개요
본 연구에서는 대규모 오프라인 데이터셋으로부터 인간의 시연과 자율적으로 수집된 데이터를 모두 활용할 수 있는 다중 작업 정책을 훈련하기 위한 확장 가능한 강화 학습 방법을 제시합니다. 우리의 방법은 오프라인 시간차 백업을 통해 훈련된 Q-함수에 대해 확장 가능한 표현을 제공하기 위해 Transformer를 사용합니다. 따라서 이 방법을 Q-Transformer라고 명명합니다. 각 행동 차원을 이산화하고 각 행동 차원의 Q-값을 개별 토큰으로 표현함으로써, Q-러닝에 효과적인 고용량 시퀀스 모델링 기법을 적용할 수 있습니다. 우리는 오프라인 RL 훈련에서 우수한 성능을 가능하게 하는 여러 설계 결정을 제시하며, Q-Transformer가 다양하고 실제적인 로봇 조작 작업 모음에서 기존의 오프라인 RL 알고리즘과 모방 학습 기법보다 뛰어난 성능을 보임을 입증합니다. 프로젝트 웹사이트와 비디오는 https://qtransformer.github.io 에서 확인할 수 있습니다.

## 핵심 내용
본 연구에서는 대규모 오프라인 데이터셋으로부터 인간의 시연과 자율적으로 수집된 데이터를 모두 활용할 수 있는 다중 작업 정책을 훈련하기 위한 확장 가능한 강화 학습 방법을 제시합니다. 우리의 방법은 오프라인 시간차 백업을 통해 훈련된 Q-함수에 대해 확장 가능한 표현을 제공하기 위해 Transformer를 사용합니다. 따라서 이 방법을 Q-Transformer라고 명명합니다. 각 행동 차원을 이산화하고 각 행동 차원의 Q-값을 개별 토큰으로 표현함으로써, Q-러닝에 효과적인 고용량 시퀀스 모델링 기법을 적용할 수 있습니다. 우리는 오프라인 RL 훈련에서 우수한 성능을 가능하게 하는 여러 설계 결정을 제시하며, Q-Transformer가 다양하고 실제적인 로봇 조작 작업 모음에서 기존의 오프라인 RL 알고리즘과 모방 학습 기법보다 뛰어난 성능을 보임을 입증합니다. 프로젝트 웹사이트와 비디오는 https://qtransformer.github.io 에서 확인할 수 있습니다.
