---
$id: ent_paper_shen_expertise_need_not_monopolize_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning'
  zh: AdaMoE
  ko: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning'
summary:
  en: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (AdaMoE),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tsinghua
    University, The University of Hong Kong, Tongji University, D-Robotics, Key Laboratory of System Control and Information
    Processing, Shanghai Key Laboratory of Integrated Administration Technologies for Information Security.'
  zh: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (AdaMoE),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tsinghua
    University, The University of Hong Kong, Tongji University, D-Robotics, Key Laboratory of System Control and Information
    Processing, Shanghai Key Laboratory of Integrated Administration Technologies for Information Security.'
  ko: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (AdaMoE),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tsinghua
    University, The University of Hong Kong, Tongji University, D-Robotics, Key Laboratory of System Control and Information
    Processing, Shanghai Key Laboratory of Integrated Administration Technologies for Information Security.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- adamoe
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14300v1.
sources:
- id: src_001
  type: paper
  title: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (arXiv)'
  url: https://arxiv.org/abs/2510.14300
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AdaMoE source
  url: https://doi.org/10.48550/arXiv.2510.14300
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models are experiencing rapid development and demonstrating promising capabilities in robotic manipulation tasks. However, scaling up VLA models presents several critical challenges: (1) Training new VLA models from scratch demands substantial computational resources and extensive datasets. Given the current scarcity of robot data, it becomes particularly valuable to fully leverage well-pretrained VLA model weights during the scaling process. (2) Real-time control requires carefully balancing model capacity with computational efficiency. To address these challenges, We propose AdaMoE, a Mixture-of-Experts (MoE) architecture that inherits pretrained weights from dense VLA models, and scales up the action expert by substituting the feedforward layers into sparsely activated MoE layers. AdaMoE employs a decoupling technique that decouples expert selection from expert weighting through an independent scale adapter working alongside the traditional router. This enables experts to be selected based on task relevance while contributing with independently controlled weights, allowing collaborative expert utilization rather than winner-takes-all dynamics. Our approach demonstrates that expertise need not monopolize. Instead, through collaborative expert utilization, we can achieve superior performance while maintaining computational efficiency. AdaMoE consistently outperforms the baseline model across key benchmarks, delivering performance gains of 1.8% on LIBERO and 9.3% on RoboTwin. Most importantly, a substantial 21.5% improvement in real-world experiments validates its practical effectiveness for robotic manipulation tasks.

## 核心内容
Vision-Language-Action (VLA) models are experiencing rapid development and demonstrating promising capabilities in robotic manipulation tasks. However, scaling up VLA models presents several critical challenges: (1) Training new VLA models from scratch demands substantial computational resources and extensive datasets. Given the current scarcity of robot data, it becomes particularly valuable to fully leverage well-pretrained VLA model weights during the scaling process. (2) Real-time control requires carefully balancing model capacity with computational efficiency. To address these challenges, We propose AdaMoE, a Mixture-of-Experts (MoE) architecture that inherits pretrained weights from dense VLA models, and scales up the action expert by substituting the feedforward layers into sparsely activated MoE layers. AdaMoE employs a decoupling technique that decouples expert selection from expert weighting through an independent scale adapter working alongside the traditional router. This enables experts to be selected based on task relevance while contributing with independently controlled weights, allowing collaborative expert utilization rather than winner-takes-all dynamics. Our approach demonstrates that expertise need not monopolize. Instead, through collaborative expert utilization, we can achieve superior performance while maintaining computational efficiency. AdaMoE consistently outperforms the baseline model across key benchmarks, delivering performance gains of 1.8% on LIBERO and 9.3% on RoboTwin. Most importantly, a substantial 21.5% improvement in real-world experiments validates its practical effectiveness for robotic manipulation tasks.

## 参考
- http://arxiv.org/abs/2510.14300v1

## Overview
Vision-Language-Action (VLA) models are experiencing rapid development and demonstrating promising capabilities in robotic manipulation tasks. However, scaling up VLA models presents several critical challenges: (1) Training new VLA models from scratch demands substantial computational resources and extensive datasets. Given the current scarcity of robot data, it becomes particularly valuable to fully leverage well-pretrained VLA model weights during the scaling process. (2) Real-time control requires carefully balancing model capacity with computational efficiency. To address these challenges, We propose AdaMoE, a Mixture-of-Experts (MoE) architecture that inherits pretrained weights from dense VLA models, and scales up the action expert by substituting the feedforward layers into sparsely activated MoE layers. AdaMoE employs a decoupling technique that decouples expert selection from expert weighting through an independent scale adapter working alongside the traditional router. This enables experts to be selected based on task relevance while contributing with independently controlled weights, allowing collaborative expert utilization rather than winner-takes-all dynamics. Our approach demonstrates that expertise need not monopolize. Instead, through collaborative expert utilization, we can achieve superior performance while maintaining computational efficiency. AdaMoE consistently outperforms the baseline model across key benchmarks, delivering performance gains of 1.8% on LIBERO and 9.3% on RoboTwin. Most importantly, a substantial 21.5% improvement in real-world experiments validates its practical effectiveness for robotic manipulation tasks.

## Content
Vision-Language-Action (VLA) models are experiencing rapid development and demonstrating promising capabilities in robotic manipulation tasks. However, scaling up VLA models presents several critical challenges: (1) Training new VLA models from scratch demands substantial computational resources and extensive datasets. Given the current scarcity of robot data, it becomes particularly valuable to fully leverage well-pretrained VLA model weights during the scaling process. (2) Real-time control requires carefully balancing model capacity with computational efficiency. To address these challenges, We propose AdaMoE, a Mixture-of-Experts (MoE) architecture that inherits pretrained weights from dense VLA models, and scales up the action expert by substituting the feedforward layers into sparsely activated MoE layers. AdaMoE employs a decoupling technique that decouples expert selection from expert weighting through an independent scale adapter working alongside the traditional router. This enables experts to be selected based on task relevance while contributing with independently controlled weights, allowing collaborative expert utilization rather than winner-takes-all dynamics. Our approach demonstrates that expertise need not monopolize. Instead, through collaborative expert utilization, we can achieve superior performance while maintaining computational efficiency. AdaMoE consistently outperforms the baseline model across key benchmarks, delivering performance gains of 1.8% on LIBERO and 9.3% on RoboTwin. Most importantly, a substantial 21.5% improvement in real-world experiments validates its practical effectiveness for robotic manipulation tasks.

## 개요
Vision-Language-Action (VLA) 모델은 빠르게 발전하며 로봇 조작 작업에서 유망한 성능을 보여주고 있습니다. 그러나 VLA 모델의 확장은 몇 가지 중요한 도전 과제를 제기합니다: (1) 새로운 VLA 모델을 처음부터 훈련하려면 상당한 계산 자원과 방대한 데이터셋이 필요합니다. 현재 로봇 데이터가 부족한 상황에서, 확장 과정에서 잘 사전 훈련된 VLA 모델 가중치를 완전히 활용하는 것이 특히 중요합니다. (2) 실시간 제어는 모델 용량과 계산 효율성 사이의 신중한 균형을 요구합니다. 이러한 도전 과제를 해결하기 위해, 우리는 AdaMoE를 제안합니다. 이는 밀집 VLA 모델의 사전 훈련 가중치를 상속받고, 피드포워드 레이어를 희소 활성화된 MoE 레이어로 대체하여 액션 전문가를 확장하는 Mixture-of-Experts (MoE) 아키텍처입니다. AdaMoE는 전통적인 라우터와 함께 작동하는 독립적인 스케일 어댑터를 통해 전문가 선택과 전문가 가중치를 분리하는 분리 기술을 사용합니다. 이를 통해 작업 관련성에 따라 전문가를 선택하면서 독립적으로 제어된 가중치로 기여할 수 있어, 승자 독식 동역학이 아닌 협력적 전문가 활용이 가능합니다. 우리의 접근 방식은 전문성이 독점될 필요가 없음을 보여줍니다. 대신, 협력적 전문가 활용을 통해 계산 효율성을 유지하면서 우수한 성능을 달성할 수 있습니다. AdaMoE는 주요 벤치마크에서 기준 모델을 일관되게 능가하며, LIBERO에서 1.8%, RoboTwin에서 9.3%의 성능 향상을 제공합니다. 가장 중요한 것은 실제 실험에서 21.5%의 상당한 개선이 로봇 조작 작업에 대한 실용적 효과를 입증한다는 점입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 빠르게 발전하며 로봇 조작 작업에서 유망한 성능을 보여주고 있습니다. 그러나 VLA 모델의 확장은 몇 가지 중요한 도전 과제를 제기합니다: (1) 새로운 VLA 모델을 처음부터 훈련하려면 상당한 계산 자원과 방대한 데이터셋이 필요합니다. 현재 로봇 데이터가 부족한 상황에서, 확장 과정에서 잘 사전 훈련된 VLA 모델 가중치를 완전히 활용하는 것이 특히 중요합니다. (2) 실시간 제어는 모델 용량과 계산 효율성 사이의 신중한 균형을 요구합니다. 이러한 도전 과제를 해결하기 위해, 우리는 AdaMoE를 제안합니다. 이는 밀집 VLA 모델의 사전 훈련 가중치를 상속받고, 피드포워드 레이어를 희소 활성화된 MoE 레이어로 대체하여 액션 전문가를 확장하는 Mixture-of-Experts (MoE) 아키텍처입니다. AdaMoE는 전통적인 라우터와 함께 작동하는 독립적인 스케일 어댑터를 통해 전문가 선택과 전문가 가중치를 분리하는 분리 기술을 사용합니다. 이를 통해 작업 관련성에 따라 전문가를 선택하면서 독립적으로 제어된 가중치로 기여할 수 있어, 승자 독식 동역학이 아닌 협력적 전문가 활용이 가능합니다. 우리의 접근 방식은 전문성이 독점될 필요가 없음을 보여줍니다. 대신, 협력적 전문가 활용을 통해 계산 효율성을 유지하면서 우수한 성능을 달성할 수 있습니다. AdaMoE는 주요 벤치마크에서 기준 모델을 일관되게 능가하며, LIBERO에서 1.8%, RoboTwin에서 9.3%의 성능 향상을 제공합니다. 가장 중요한 것은 실제 실험에서 21.5%의 상당한 개선이 로봇 조작 작업에 대한 실용적 효과를 입증한다는 점입니다.
