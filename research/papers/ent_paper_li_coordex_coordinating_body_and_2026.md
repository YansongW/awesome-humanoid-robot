---
$id: ent_paper_li_coordex_coordinating_body_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation'
  zh: CoorDex：协调身体与手部先验的连续灵巧人形移动操作
  ko: 'CoorDex: 지속적 영리한 휴머노이드 이동-조작을 위한 몸과 손의 사전 지식 조율'
summary:
  en: CoorDex is a learning pipeline that distills separate whole-body and wrist-stabilized hand motion priors into latent
    action spaces and trains a coordinated residual PPO policy, enabling a Unitree G1 with a 20-DoF WUJI hand to perform dexterous
    manipulation while walking.
  zh: CoorDex 是一种学习流程，它将独立的全身运动和腕部稳定的灵巧手部运动先验蒸馏为隐式动作空间，并训练一个协调的残差 PPO 策略，使配备 20 自由度 WUJI 手的 Unitree G1 能够在行走的同时完成灵巧操作。
  ko: CoorDex는 개별적인 전신 동작과 손목 고정형 영리한 손 동작의 사전 지식을 잠재 동작 공간으로 증류하고, 조화로운 잔차 PPO 정책을 학습하여 20-DoF WUJI 손이 장착된 Unitree G1이 걸으면서
    영리한 조작을 수행할 수 있게 한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- coor_dex
- dexterous_manipulation
- loco_manipulation
- continuous_manipulation
- latent_priors
- residual_reinforcement_learning
- motion_tracking
- whole_body_control
- unitree_g1
- wuji_hand
- isaac_lab
- ppo
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.23680v1.
sources:
- id: src_001
  type: paper
  title: 'CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2606.23680
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_component_unitree_dex3_1_hand
  relationship: uses
  description:
    en: The paper mentions the Unitree Dex3-1 dexterous hand as part of the hardware context.
    zh: 该论文将 Unitree Dex3-1 灵巧手作为硬件背景的一部分提及。
    ko: 해당 논문은 Unitree Dex3-1 영리한 손을 하드웨어 맥락의 일부로 언급한다.
---
## 概述
Humanoid loco-manipulation is often simplified into a stop-and-go process: walking to an object, stopping to manipulate it, and then resuming locomotion. It also commonly relies on low degree-of-freedom (DoF) end effectors that behave like an open-close grasp primitive. We introduce CoorDex, a learning pipeline that converts high-dimensional body and dexterous hand control into coordinated latent residual control, enabling high-DoF dexterous loco-manipulation on the move. Starting from simulated whole-body and hand demonstrations, CoorDex trains privileged motion tracking teachers for the humanoid body and dexterous hand, distills them into proprioception-conditioned latent priors, and uses the frozen priors as the action space for downstream residual reinforcement learning. A coordinated latent residual policy composes these priors through shared task context and separate body-hand residual heads, preserving natural whole-body motion while improving finger-level contact reliability. CoorDex enables a Unitree G1 humanoid with a 20-DoF WUJI hand to execute dexterous manipulation while in motion, including non-stop bottle grasping and carrying, fridge door opening on the move, and cube pick-and-turn. Ablations on the walk-grasp-carry task show that joint-space PPO, joint-space hand control, and monolithic latent prediction all fail under the same reward budget, while the latent-prior interface and coordinated residual structure make high-dimensional contact-rich loco-manipulation trainable. Project Page: https://skevinci.github.io/coordex/

## 核心内容
Humanoid loco-manipulation is often simplified into a stop-and-go process: walking to an object, stopping to manipulate it, and then resuming locomotion. It also commonly relies on low degree-of-freedom (DoF) end effectors that behave like an open-close grasp primitive. We introduce CoorDex, a learning pipeline that converts high-dimensional body and dexterous hand control into coordinated latent residual control, enabling high-DoF dexterous loco-manipulation on the move. Starting from simulated whole-body and hand demonstrations, CoorDex trains privileged motion tracking teachers for the humanoid body and dexterous hand, distills them into proprioception-conditioned latent priors, and uses the frozen priors as the action space for downstream residual reinforcement learning. A coordinated latent residual policy composes these priors through shared task context and separate body-hand residual heads, preserving natural whole-body motion while improving finger-level contact reliability. CoorDex enables a Unitree G1 humanoid with a 20-DoF WUJI hand to execute dexterous manipulation while in motion, including non-stop bottle grasping and carrying, fridge door opening on the move, and cube pick-and-turn. Ablations on the walk-grasp-carry task show that joint-space PPO, joint-space hand control, and monolithic latent prediction all fail under the same reward budget, while the latent-prior interface and coordinated residual structure make high-dimensional contact-rich loco-manipulation trainable. Project Page: https://skevinci.github.io/coordex/

## 参考
- http://arxiv.org/abs/2606.23680v1

## Overview
Humanoid loco-manipulation is often simplified into a stop-and-go process: walking to an object, stopping to manipulate it, and then resuming locomotion. It also commonly relies on low degree-of-freedom (DoF) end effectors that behave like an open-close grasp primitive. We introduce CoorDex, a learning pipeline that converts high-dimensional body and dexterous hand control into coordinated latent residual control, enabling high-DoF dexterous loco-manipulation on the move. Starting from simulated whole-body and hand demonstrations, CoorDex trains privileged motion tracking teachers for the humanoid body and dexterous hand, distills them into proprioception-conditioned latent priors, and uses the frozen priors as the action space for downstream residual reinforcement learning. A coordinated latent residual policy composes these priors through shared task context and separate body-hand residual heads, preserving natural whole-body motion while improving finger-level contact reliability. CoorDex enables a Unitree G1 humanoid with a 20-DoF WUJI hand to execute dexterous manipulation while in motion, including non-stop bottle grasping and carrying, fridge door opening on the move, and cube pick-and-turn. Ablations on the walk-grasp-carry task show that joint-space PPO, joint-space hand control, and monolithic latent prediction all fail under the same reward budget, while the latent-prior interface and coordinated residual structure make high-dimensional contact-rich loco-manipulation trainable. Project Page: https://skevinci.github.io/coordex/

## Content
Humanoid loco-manipulation is often simplified into a stop-and-go process: walking to an object, stopping to manipulate it, and then resuming locomotion. It also commonly relies on low degree-of-freedom (DoF) end effectors that behave like an open-close grasp primitive. We introduce CoorDex, a learning pipeline that converts high-dimensional body and dexterous hand control into coordinated latent residual control, enabling high-DoF dexterous loco-manipulation on the move. Starting from simulated whole-body and hand demonstrations, CoorDex trains privileged motion tracking teachers for the humanoid body and dexterous hand, distills them into proprioception-conditioned latent priors, and uses the frozen priors as the action space for downstream residual reinforcement learning. A coordinated latent residual policy composes these priors through shared task context and separate body-hand residual heads, preserving natural whole-body motion while improving finger-level contact reliability. CoorDex enables a Unitree G1 humanoid with a 20-DoF WUJI hand to execute dexterous manipulation while in motion, including non-stop bottle grasping and carrying, fridge door opening on the move, and cube pick-and-turn. Ablations on the walk-grasp-carry task show that joint-space PPO, joint-space hand control, and monolithic latent prediction all fail under the same reward budget, while the latent-prior interface and coordinated residual structure make high-dimensional contact-rich loco-manipulation trainable. Project Page: https://skevinci.github.io/coordex/

## 개요
휴머노이드의 이동-조작(loco-manipulation)은 종종 멈춤-이동 과정으로 단순화됩니다. 즉, 물체로 걸어가서 멈추고 조작한 후 다시 이동을 재개하는 방식입니다. 또한 일반적으로 개폐식 파악 원시 동작처럼 작동하는 저자유도(DoF) 말단 효과기에 의존합니다. 본 논문에서는 CoorDex를 소개합니다. 이는 고차원의 신체 및 정교한 손 제어를 조정된 잠재 잔차 제어로 변환하여 이동 중에도 고자유도 정교한 이동-조작을 가능하게 하는 학습 파이프라인입니다. 시뮬레이션된 전신 및 손 시연에서 시작하여, CoorDex는 휴머노이드 신체와 정교한 손을 위한 특권적 동작 추적 교사를 훈련하고, 이를 고유수용감각 조건화된 잠재 사전 지식으로 증류한 후, 동결된 사전 지식을 하류 잔차 강화 학습의 행동 공간으로 사용합니다. 조정된 잠재 잔차 정책은 공유된 작업 컨텍스트와 분리된 신체-손 잔차 헤드를 통해 이러한 사전 지식을 구성하여, 자연스러운 전신 동작을 유지하면서 손가락 수준의 접촉 신뢰성을 향상시킵니다. CoorDex는 20-DoF WUJI 손을 장착한 Unitree G1 휴머노이드가 이동 중에도 정교한 조작을 수행할 수 있게 합니다. 여기에는 멈추지 않는 병 잡기 및 운반, 이동 중 냉장고 문 열기, 큐브 집기 및 돌리기가 포함됩니다. 걷기-잡기-운반 작업에 대한 절제 연구는 동일한 보상 예산 하에서 관절 공간 PPO, 관절 공간 손 제어, 단일 잠재 예측이 모두 실패하는 반면, 잠재 사전 지식 인터페이스와 조정된 잔차 구조가 고차원 접촉이 풍부한 이동-조작을 훈련 가능하게 만든다는 것을 보여줍니다. 프로젝트 페이지: https://skevinci.github.io/coordex/

## 핵심 내용
휴머노이드의 이동-조작(loco-manipulation)은 종종 멈춤-이동 과정으로 단순화됩니다. 즉, 물체로 걸어가서 멈추고 조작한 후 다시 이동을 재개하는 방식입니다. 또한 일반적으로 개폐식 파악 원시 동작처럼 작동하는 저자유도(DoF) 말단 효과기에 의존합니다. 본 논문에서는 CoorDex를 소개합니다. 이는 고차원의 신체 및 정교한 손 제어를 조정된 잠재 잔차 제어로 변환하여 이동 중에도 고자유도 정교한 이동-조작을 가능하게 하는 학습 파이프라인입니다. 시뮬레이션된 전신 및 손 시연에서 시작하여, CoorDex는 휴머노이드 신체와 정교한 손을 위한 특권적 동작 추적 교사를 훈련하고, 이를 고유수용감각 조건화된 잠재 사전 지식으로 증류한 후, 동결된 사전 지식을 하류 잔차 강화 학습의 행동 공간으로 사용합니다. 조정된 잠재 잔차 정책은 공유된 작업 컨텍스트와 분리된 신체-손 잔차 헤드를 통해 이러한 사전 지식을 구성하여, 자연스러운 전신 동작을 유지하면서 손가락 수준의 접촉 신뢰성을 향상시킵니다. CoorDex는 20-DoF WUJI 손을 장착한 Unitree G1 휴머노이드가 이동 중에도 정교한 조작을 수행할 수 있게 합니다. 여기에는 멈추지 않는 병 잡기 및 운반, 이동 중 냉장고 문 열기, 큐브 집기 및 돌리기가 포함됩니다. 걷기-잡기-운반 작업에 대한 절제 연구는 동일한 보상 예산 하에서 관절 공간 PPO, 관절 공간 손 제어, 단일 잠재 예측이 모두 실패하는 반면, 잠재 사전 지식 인터페이스와 조정된 잔차 구조가 고차원 접촉이 풍부한 이동-조작을 훈련 가능하게 만든다는 것을 보여줍니다. 프로젝트 페이지: https://skevinci.github.io/coordex/
