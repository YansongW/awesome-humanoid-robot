---
$id: ent_paper_cen_worldvla_towards_autoregressiv_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WorldVLA: Towards Autoregressive Action World Model'
  zh: WorldVLA
  ko: 'WorldVLA: Towards Autoregressive Action World Model'
summary:
  en: 'WorldVLA: Towards Autoregressive Action World Model (WorldVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by DAMO Academy, Alibaba Group, Hupan Lab, Zhejiang University.'
  zh: 'WorldVLA: Towards Autoregressive Action World Model (WorldVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by DAMO Academy, Alibaba Group, Hupan Lab, Zhejiang University.'
  ko: 'WorldVLA: Towards Autoregressive Action World Model (WorldVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by DAMO Academy, Alibaba Group, Hupan Lab, Zhejiang University.'
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
- worldvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.21539v1.
sources:
- id: src_001
  type: paper
  title: 'WorldVLA: Towards Autoregressive Action World Model (arXiv)'
  url: https://arxiv.org/abs/2506.21539
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: WorldVLA source
  url: https://doi.org/10.48550/arXiv.2506.21539
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present WorldVLA, an autoregressive action world model that unifies action and image understanding and generation. Our WorldVLA intergrates Vision-Language-Action (VLA) model and world model in one single framework. The world model predicts future images by leveraging both action and image understanding, with the purpose of learning the underlying physics of the environment to improve action generation. Meanwhile, the action model generates the subsequent actions based on image observations, aiding in visual understanding and in turn helps visual generation of the world model. We demonstrate that WorldVLA outperforms standalone action and world models, highlighting the mutual enhancement between the world model and the action model. In addition, we find that the performance of the action model deteriorates when generating sequences of actions in an autoregressive manner. This phenomenon can be attributed to the model's limited generalization capability for action prediction, leading to the propagation of errors from earlier actions to subsequent ones. To address this issue, we propose an attention mask strategy that selectively masks prior actions during the generation of the current action, which shows significant performance improvement in the action chunk generation task.

## 核心内容
We present WorldVLA, an autoregressive action world model that unifies action and image understanding and generation. Our WorldVLA intergrates Vision-Language-Action (VLA) model and world model in one single framework. The world model predicts future images by leveraging both action and image understanding, with the purpose of learning the underlying physics of the environment to improve action generation. Meanwhile, the action model generates the subsequent actions based on image observations, aiding in visual understanding and in turn helps visual generation of the world model. We demonstrate that WorldVLA outperforms standalone action and world models, highlighting the mutual enhancement between the world model and the action model. In addition, we find that the performance of the action model deteriorates when generating sequences of actions in an autoregressive manner. This phenomenon can be attributed to the model's limited generalization capability for action prediction, leading to the propagation of errors from earlier actions to subsequent ones. To address this issue, we propose an attention mask strategy that selectively masks prior actions during the generation of the current action, which shows significant performance improvement in the action chunk generation task.

## 参考
- http://arxiv.org/abs/2506.21539v1

## Overview
We present WorldVLA, an autoregressive action world model that unifies action and image understanding and generation. Our WorldVLA integrates Vision-Language-Action (VLA) model and world model in one single framework. The world model predicts future images by leveraging both action and image understanding, with the purpose of learning the underlying physics of the environment to improve action generation. Meanwhile, the action model generates the subsequent actions based on image observations, aiding in visual understanding and in turn helps visual generation of the world model. We demonstrate that WorldVLA outperforms standalone action and world models, highlighting the mutual enhancement between the world model and the action model. In addition, we find that the performance of the action model deteriorates when generating sequences of actions in an autoregressive manner. This phenomenon can be attributed to the model's limited generalization capability for action prediction, leading to the propagation of errors from earlier actions to subsequent ones. To address this issue, we propose an attention mask strategy that selectively masks prior actions during the generation of the current action, which shows significant performance improvement in the action chunk generation task.

## Content
We present WorldVLA, an autoregressive action world model that unifies action and image understanding and generation. Our WorldVLA integrates Vision-Language-Action (VLA) model and world model in one single framework. The world model predicts future images by leveraging both action and image understanding, with the purpose of learning the underlying physics of the environment to improve action generation. Meanwhile, the action model generates the subsequent actions based on image observations, aiding in visual understanding and in turn helps visual generation of the world model. We demonstrate that WorldVLA outperforms standalone action and world models, highlighting the mutual enhancement between the world model and the action model. In addition, we find that the performance of the action model deteriorates when generating sequences of actions in an autoregressive manner. This phenomenon can be attributed to the model's limited generalization capability for action prediction, leading to the propagation of errors from earlier actions to subsequent ones. To address this issue, we propose an attention mask strategy that selectively masks prior actions during the generation of the current action, which shows significant performance improvement in the action chunk generation task.

## 개요
본 논문에서는 행동과 이미지 이해 및 생성을 통합하는 자기회귀적 행동 세계 모델인 WorldVLA를 제시합니다. WorldVLA는 비전-언어-행동(VLA) 모델과 세계 모델을 하나의 프레임워크로 통합합니다. 세계 모델은 행동과 이미지 이해를 모두 활용하여 미래 이미지를 예측하며, 환경의 물리적 원리를 학습하여 행동 생성을 개선하는 것을 목표로 합니다. 동시에 행동 모델은 이미지 관찰을 기반으로 후속 행동을 생성하여 시각적 이해를 돕고, 이는 다시 세계 모델의 시각적 생성을 지원합니다. 우리는 WorldVLA가 독립적인 행동 모델과 세계 모델보다 우수한 성능을 보임을 입증하며, 세계 모델과 행동 모델 간의 상호 강화 효과를 강조합니다. 또한, 자기회귀적 방식으로 행동 시퀀스를 생성할 때 행동 모델의 성능이 저하되는 현상을 발견했습니다. 이 현상은 행동 예측에 대한 모델의 제한된 일반화 능력으로 인해 초기 행동의 오류가 후속 행동으로 전파되기 때문입니다. 이 문제를 해결하기 위해 현재 행동 생성 중 이전 행동을 선택적으로 마스킹하는 어텐션 마스크 전략을 제안하며, 이는 행동 청크 생성 작업에서 상당한 성능 향상을 보여줍니다.

## 핵심 내용
본 논문에서는 행동과 이미지 이해 및 생성을 통합하는 자기회귀적 행동 세계 모델인 WorldVLA를 제시합니다. WorldVLA는 비전-언어-행동(VLA) 모델과 세계 모델을 하나의 프레임워크로 통합합니다. 세계 모델은 행동과 이미지 이해를 모두 활용하여 미래 이미지를 예측하며, 환경의 물리적 원리를 학습하여 행동 생성을 개선하는 것을 목표로 합니다. 동시에 행동 모델은 이미지 관찰을 기반으로 후속 행동을 생성하여 시각적 이해를 돕고, 이는 다시 세계 모델의 시각적 생성을 지원합니다. 우리는 WorldVLA가 독립적인 행동 모델과 세계 모델보다 우수한 성능을 보임을 입증하며, 세계 모델과 행동 모델 간의 상호 강화 효과를 강조합니다. 또한, 자기회귀적 방식으로 행동 시퀀스를 생성할 때 행동 모델의 성능이 저하되는 현상을 발견했습니다. 이 현상은 행동 예측에 대한 모델의 제한된 일반화 능력으로 인해 초기 행동의 오류가 후속 행동으로 전파되기 때문입니다. 이 문제를 해결하기 위해 현재 행동 생성 중 이전 행동을 선택적으로 마스킹하는 어텐션 마스크 전략을 제안하며, 이는 행동 청크 생성 작업에서 상당한 성능 향상을 보여줍니다.
