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

