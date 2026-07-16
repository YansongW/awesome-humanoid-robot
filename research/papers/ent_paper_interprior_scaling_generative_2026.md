---
$id: ent_paper_interprior_scaling_generative_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions'
  zh: 'InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions'
  ko: 'InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions'
summary:
  en: 'InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions is a 2026 work on physics-based
    character animation for humanoid robots.'
  zh: 'InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions is a 2026 work on physics-based
    character animation for humanoid robots.'
  ko: 'InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions is a 2026 work on physics-based
    character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- interprior
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06035v1.
sources:
- id: src_001
  type: paper
  title: 'InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions (arXiv)'
  url: https://arxiv.org/abs/2602.06035
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humans rarely plan whole-body interactions with objects at the level of explicit whole-body movements. High-level intentions, such as affordance, define the goal, while coordinated balance, contact, and manipulation can emerge naturally from underlying physical and motor priors. Scaling such priors is key to enabling humanoids to compose and generalize loco-manipulation skills across diverse contexts while maintaining physically coherent whole-body coordination. To this end, we introduce InterPrior, a scalable framework that learns a unified generative controller through large-scale imitation pretraining and post-training by reinforcement learning. InterPrior first distills a full-reference imitation expert into a versatile, goal-conditioned variational policy that reconstructs motion from multimodal observations and high-level intent. While the distilled policy reconstructs training behaviors, it does not generalize reliably due to the vast configuration space of large-scale human-object interactions. To address this, we apply data augmentation with physical perturbations, and then perform reinforcement learning finetuning to improve competence on unseen goals and initializations. Together, these steps consolidate the reconstructed latent skills into a valid manifold, yielding a motion prior that generalizes beyond the training data, e.g., it can incorporate new behaviors such as interactions with unseen objects. We further demonstrate its effectiveness for user-interactive control and its potential for real robot deployment.

## 核心内容
Humans rarely plan whole-body interactions with objects at the level of explicit whole-body movements. High-level intentions, such as affordance, define the goal, while coordinated balance, contact, and manipulation can emerge naturally from underlying physical and motor priors. Scaling such priors is key to enabling humanoids to compose and generalize loco-manipulation skills across diverse contexts while maintaining physically coherent whole-body coordination. To this end, we introduce InterPrior, a scalable framework that learns a unified generative controller through large-scale imitation pretraining and post-training by reinforcement learning. InterPrior first distills a full-reference imitation expert into a versatile, goal-conditioned variational policy that reconstructs motion from multimodal observations and high-level intent. While the distilled policy reconstructs training behaviors, it does not generalize reliably due to the vast configuration space of large-scale human-object interactions. To address this, we apply data augmentation with physical perturbations, and then perform reinforcement learning finetuning to improve competence on unseen goals and initializations. Together, these steps consolidate the reconstructed latent skills into a valid manifold, yielding a motion prior that generalizes beyond the training data, e.g., it can incorporate new behaviors such as interactions with unseen objects. We further demonstrate its effectiveness for user-interactive control and its potential for real robot deployment.

## 参考
- http://arxiv.org/abs/2602.06035v1

## Overview
Humans rarely plan whole-body interactions with objects at the level of explicit whole-body movements. High-level intentions, such as affordance, define the goal, while coordinated balance, contact, and manipulation can emerge naturally from underlying physical and motor priors. Scaling such priors is key to enabling humanoids to compose and generalize loco-manipulation skills across diverse contexts while maintaining physically coherent whole-body coordination. To this end, we introduce InterPrior, a scalable framework that learns a unified generative controller through large-scale imitation pretraining and post-training by reinforcement learning. InterPrior first distills a full-reference imitation expert into a versatile, goal-conditioned variational policy that reconstructs motion from multimodal observations and high-level intent. While the distilled policy reconstructs training behaviors, it does not generalize reliably due to the vast configuration space of large-scale human-object interactions. To address this, we apply data augmentation with physical perturbations, and then perform reinforcement learning finetuning to improve competence on unseen goals and initializations. Together, these steps consolidate the reconstructed latent skills into a valid manifold, yielding a motion prior that generalizes beyond the training data, e.g., it can incorporate new behaviors such as interactions with unseen objects. We further demonstrate its effectiveness for user-interactive control and its potential for real robot deployment.

## Content
Humans rarely plan whole-body interactions with objects at the level of explicit whole-body movements. High-level intentions, such as affordance, define the goal, while coordinated balance, contact, and manipulation can emerge naturally from underlying physical and motor priors. Scaling such priors is key to enabling humanoids to compose and generalize loco-manipulation skills across diverse contexts while maintaining physically coherent whole-body coordination. To this end, we introduce InterPrior, a scalable framework that learns a unified generative controller through large-scale imitation pretraining and post-training by reinforcement learning. InterPrior first distills a full-reference imitation expert into a versatile, goal-conditioned variational policy that reconstructs motion from multimodal observations and high-level intent. While the distilled policy reconstructs training behaviors, it does not generalize reliably due to the vast configuration space of large-scale human-object interactions. To address this, we apply data augmentation with physical perturbations, and then perform reinforcement learning finetuning to improve competence on unseen goals and initializations. Together, these steps consolidate the reconstructed latent skills into a valid manifold, yielding a motion prior that generalizes beyond the training data, e.g., it can incorporate new behaviors such as interactions with unseen objects. We further demonstrate its effectiveness for user-interactive control and its potential for real robot deployment.

## 개요
인간은 명시적인 전신 움직임 수준에서 물체와의 전신 상호작용을 계획하는 경우가 거의 없습니다. 어포던스(affordance)와 같은 고수준 의도는 목표를 정의하는 반면, 조정된 균형, 접촉 및 조작은 기본적인 물리적 및 운동 사전 지식(prior)에서 자연스럽게 발생할 수 있습니다. 이러한 사전 지식을 확장하는 것은 휴머노이드가 다양한 맥락에서 이동-조작(loco-manipulation) 기술을 구성하고 일반화하면서 물리적으로 일관된 전신 조정을 유지할 수 있도록 하는 핵심입니다. 이를 위해 우리는 InterPrior을 소개합니다. 이는 대규모 모방 사전 학습과 강화 학습을 통한 사후 학습을 통해 통합 생성 제어기를 학습하는 확장 가능한 프레임워크입니다. InterPrior은 먼저 전체 참조 모방 전문가를 다목적, 목표 조건부 변분 정책(variational policy)으로 증류(distill)하여 다중 모달 관찰과 고수준 의도로부터 동작을 재구성합니다. 증류된 정책은 훈련 행동을 재구성하지만, 대규모 인간-물체 상호작용의 방대한 구성 공간으로 인해 신뢰할 수 있게 일반화되지 않습니다. 이를 해결하기 위해 물리적 섭동을 포함한 데이터 증강을 적용한 후, 강화 학습 미세 조정을 수행하여 보지 못한 목표와 초기화에 대한 능력을 향상시킵니다. 이러한 단계들은 함께 재구성된 잠재 기술을 유효한 다양체(manifold)로 통합하여 훈련 데이터를 넘어 일반화되는 동작 사전 지식을 생성합니다. 예를 들어, 보지 못한 물체와의 상호작용과 같은 새로운 행동을 통합할 수 있습니다. 또한 사용자 상호작용 제어에 대한 효과성과 실제 로봇 배치 가능성을 입증합니다.

## 핵심 내용
인간은 명시적인 전신 움직임 수준에서 물체와의 전신 상호작용을 계획하는 경우가 거의 없습니다. 어포던스와 같은 고수준 의도는 목표를 정의하는 반면, 조정된 균형, 접촉 및 조작은 기본적인 물리적 및 운동 사전 지식에서 자연스럽게 발생할 수 있습니다. 이러한 사전 지식을 확장하는 것은 휴머노이드가 다양한 맥락에서 이동-조작 기술을 구성하고 일반화하면서 물리적으로 일관된 전신 조정을 유지할 수 있도록 하는 핵심입니다. 이를 위해 우리는 InterPrior을 소개합니다. 이는 대규모 모방 사전 학습과 강화 학습을 통한 사후 학습을 통해 통합 생성 제어기를 학습하는 확장 가능한 프레임워크입니다. InterPrior은 먼저 전체 참조 모방 전문가를 다목적, 목표 조건부 변분 정책으로 증류하여 다중 모달 관찰과 고수준 의도로부터 동작을 재구성합니다. 증류된 정책은 훈련 행동을 재구성하지만, 대규모 인간-물체 상호작용의 방대한 구성 공간으로 인해 신뢰할 수 있게 일반화되지 않습니다. 이를 해결하기 위해 물리적 섭동을 포함한 데이터 증강을 적용한 후, 강화 학습 미세 조정을 수행하여 보지 못한 목표와 초기화에 대한 능력을 향상시킵니다. 이러한 단계들은 함께 재구성된 잠재 기술을 유효한 다양체로 통합하여 훈련 데이터를 넘어 일반화되는 동작 사전 지식을 생성합니다. 예를 들어, 보지 못한 물체와의 상호작용과 같은 새로운 행동을 통합할 수 있습니다. 또한 사용자 상호작용 제어에 대한 효과성과 실제 로봇 배치 가능성을 입증합니다.
