---
$id: ent_paper_chen_conrft_a_reinforced_fine_tunin_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy'
  zh: ConRFT
  ko: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy'
summary:
  en: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (ConRFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by SKL-MAIS, Institute of Automation, Chinese Academy of Sciences, School of
    Artificial Intelligence, University of Chinese Academy of Sciences, and published at RSS25.'
  zh: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (ConRFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by SKL-MAIS, Institute of Automation, Chinese Academy of Sciences, School of
    Artificial Intelligence, University of Chinese Academy of Sciences, and published at RSS25.'
  ko: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (ConRFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by SKL-MAIS, Institute of Automation, Chinese Academy of Sciences, School of
    Artificial Intelligence, University of Chinese Academy of Sciences, and published at RSS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- conrft
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05450v2.
sources:
- id: src_001
  type: paper
  title: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (arXiv)'
  url: https://arxiv.org/abs/2502.05450
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ConRFT source
  url: https://doi.org/10.48550/arXiv.2502.05450
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown substantial potential in real-world robotic manipulation. However, fine-tuning these models through supervised learning struggles to achieve robust performance due to limited, inconsistent demonstrations, especially in contact-rich environments. In this paper, we propose a reinforced fine-tuning approach for VLA models, named ConRFT, which consists of offline and online fine-tuning with a unified consistency-based training objective, to address these challenges. In the offline stage, our method integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating. In the online stage, the VLA model is further fine-tuned via consistency policy, with human interventions to ensure safe exploration and high sample efficiency. We evaluate our approach on eight diverse real-world manipulation tasks. It achieves an average success rate of 96.3% within 45-90 minutes of online fine-tuning, outperforming prior supervised methods with a 144% improvement in success rate and 1.9x shorter episode length. This work highlights the potential of integrating reinforcement learning to enhance the performance of VLA models for real-world robotic applications. Videos and code are available at our project website https://cccedric.github.io/conrft/.

## 核心内容
Vision-Language-Action (VLA) models have shown substantial potential in real-world robotic manipulation. However, fine-tuning these models through supervised learning struggles to achieve robust performance due to limited, inconsistent demonstrations, especially in contact-rich environments. In this paper, we propose a reinforced fine-tuning approach for VLA models, named ConRFT, which consists of offline and online fine-tuning with a unified consistency-based training objective, to address these challenges. In the offline stage, our method integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating. In the online stage, the VLA model is further fine-tuned via consistency policy, with human interventions to ensure safe exploration and high sample efficiency. We evaluate our approach on eight diverse real-world manipulation tasks. It achieves an average success rate of 96.3% within 45-90 minutes of online fine-tuning, outperforming prior supervised methods with a 144% improvement in success rate and 1.9x shorter episode length. This work highlights the potential of integrating reinforcement learning to enhance the performance of VLA models for real-world robotic applications. Videos and code are available at our project website https://cccedric.github.io/conrft/.

## 参考
- http://arxiv.org/abs/2502.05450v2

## Overview
Vision-Language-Action (VLA) models have shown substantial potential in real-world robotic manipulation. However, fine-tuning these models through supervised learning struggles to achieve robust performance due to limited, inconsistent demonstrations, especially in contact-rich environments. In this paper, we propose a reinforced fine-tuning approach for VLA models, named ConRFT, which consists of offline and online fine-tuning with a unified consistency-based training objective, to address these challenges. In the offline stage, our method integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating. In the online stage, the VLA model is further fine-tuned via consistency policy, with human interventions to ensure safe exploration and high sample efficiency. We evaluate our approach on eight diverse real-world manipulation tasks. It achieves an average success rate of 96.3% within 45-90 minutes of online fine-tuning, outperforming prior supervised methods with a 144% improvement in success rate and 1.9x shorter episode length. This work highlights the potential of integrating reinforcement learning to enhance the performance of VLA models for real-world robotic applications. Videos and code are available at our project website https://cccedric.github.io/conrft/.

## Content
Vision-Language-Action (VLA) models have shown substantial potential in real-world robotic manipulation. However, fine-tuning these models through supervised learning struggles to achieve robust performance due to limited, inconsistent demonstrations, especially in contact-rich environments. In this paper, we propose a reinforced fine-tuning approach for VLA models, named ConRFT, which consists of offline and online fine-tuning with a unified consistency-based training objective, to address these challenges. In the offline stage, our method integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating. In the online stage, the VLA model is further fine-tuned via consistency policy, with human interventions to ensure safe exploration and high sample efficiency. We evaluate our approach on eight diverse real-world manipulation tasks. It achieves an average success rate of 96.3% within 45-90 minutes of online fine-tuning, outperforming prior supervised methods with a 144% improvement in success rate and 1.9x shorter episode length. This work highlights the potential of integrating reinforcement learning to enhance the performance of VLA models for real-world robotic applications. Videos and code are available at our project website https://cccedric.github.io/conrft/.

## 개요
Vision-Language-Action (VLA) 모델은 실제 로봇 조작 분야에서 상당한 잠재력을 보여주고 있습니다. 그러나 제한적이고 일관되지 않은 시연 데이터, 특히 접촉이 많은 환경에서 지도 학습을 통한 미세 조정은 강력한 성능을 달성하는 데 어려움을 겪습니다. 본 논문에서는 이러한 문제를 해결하기 위해 일관성 기반의 통합 훈련 목표를 갖춘 오프라인 및 온라인 미세 조정으로 구성된 VLA 모델을 위한 강화 미세 조정 접근법인 ConRFT를 제안합니다. 오프라인 단계에서 우리의 방법은 행동 복제와 Q-러닝을 통합하여 소규모 시연 데이터에서 효과적으로 정책을 추출하고 가치 추정을 안정화합니다. 온라인 단계에서는 일관성 정책을 통해 VLA 모델을 추가로 미세 조정하며, 인간의 개입을 통해 안전한 탐색과 높은 샘플 효율성을 보장합니다. 우리는 8가지 다양한 실제 조작 작업에서 접근법을 평가했습니다. 45-90분의 온라인 미세 조정 내에 평균 성공률 96.3%를 달성하여, 이전의 지도 학습 방법보다 성공률에서 144% 향상, 에피소드 길이에서 1.9배 단축된 성과를 보였습니다. 이 연구는 강화 학습을 통합하여 실제 로봇 응용을 위한 VLA 모델의 성능을 향상시킬 수 있는 잠재력을 강조합니다. 비디오와 코드는 프로젝트 웹사이트 https://cccedric.github.io/conrft/에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 실제 로봇 조작 분야에서 상당한 잠재력을 보여주고 있습니다. 그러나 제한적이고 일관되지 않은 시연 데이터, 특히 접촉이 많은 환경에서 지도 학습을 통한 미세 조정은 강력한 성능을 달성하는 데 어려움을 겪습니다. 본 논문에서는 이러한 문제를 해결하기 위해 일관성 기반의 통합 훈련 목표를 갖춘 오프라인 및 온라인 미세 조정으로 구성된 VLA 모델을 위한 강화 미세 조정 접근법인 ConRFT를 제안합니다. 오프라인 단계에서 우리의 방법은 행동 복제와 Q-러닝을 통합하여 소규모 시연 데이터에서 효과적으로 정책을 추출하고 가치 추정을 안정화합니다. 온라인 단계에서는 일관성 정책을 통해 VLA 모델을 추가로 미세 조정하며, 인간의 개입을 통해 안전한 탐색과 높은 샘플 효율성을 보장합니다. 우리는 8가지 다양한 실제 조작 작업에서 접근법을 평가했습니다. 45-90분의 온라인 미세 조정 내에 평균 성공률 96.3%를 달성하여, 이전의 지도 학습 방법보다 성공률에서 144% 향상, 에피소드 길이에서 1.9배 단축된 성과를 보였습니다. 이 연구는 강화 학습을 통합하여 실제 로봇 응용을 위한 VLA 모델의 성능을 향상시킬 수 있는 잠재력을 강조합니다. 비디오와 코드는 프로젝트 웹사이트 https://cccedric.github.io/conrft/에서 확인할 수 있습니다.
