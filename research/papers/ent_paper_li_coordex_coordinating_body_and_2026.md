---
$id: ent_paper_li_coordex_coordinating_body_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid
    Loco-Manipulation'
  zh: CoorDex：协调身体与手部先验的连续灵巧人形移动操作
  ko: 'CoorDex: 지속적 영리한 휴머노이드 이동-조작을 위한 몸과 손의 사전 지식 조율'
summary:
  en: CoorDex is a learning pipeline that distills separate whole-body and wrist-stabilized
    hand motion priors into latent action spaces and trains a coordinated residual
    PPO policy, enabling a Unitree G1 with a 20-DoF WUJI hand to perform dexterous
    manipulation while walking.
  zh: CoorDex 是一种学习流程，它将独立的全身运动和腕部稳定的灵巧手部运动先验蒸馏为隐式动作空间，并训练一个协调的残差 PPO 策略，使配备 20 自由度
    WUJI 手的 Unitree G1 能够在行走的同时完成灵巧操作。
  ko: CoorDex는 개별적인 전신 동작과 손목 고정형 영리한 손 동작의 사전 지식을 잠재 동작 공간으로 증류하고, 조화로운 잔차 PPO 정책을
    학습하여 20-DoF WUJI 손이 장착된 Unitree G1이 걸으면서 영리한 조작을 수행할 수 있게 한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from abstract and provided metadata; full-text verification
    is required before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid
    Loco-Manipulation'
  url: https://arxiv.org/abs/2606.23680
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_component_unitree_dex3_1_hand
  relationship: uses
  description:
    en: The paper mentions the Unitree Dex3-1 dexterous hand as part of the hardware
      context.
    zh: 该论文将 Unitree Dex3-1 灵巧手作为硬件背景的一部分提及。
    ko: 해당 논문은 Unitree Dex3-1 영리한 손을 하드웨어 맥락의 일부로 언급한다.
---

## Overview

Existing humanoid loco-manipulation systems typically treat manipulation and locomotion as sequential stop-and-go phases, and they often rely on low-degree-of-freedom (DoF) grippers that only provide open-close grasp primitives. This simplification limits the robot's ability to interact continuously and dexterously with objects while moving, which is essential for real-world tasks such as opening doors, grasping bottles, or repositioning objects without halting locomotion.

CoorDex addresses this limitation through a staged learning pipeline. Starting from simulated whole-body and wrist-stabilized hand demonstrations, it first trains privileged motion-tracking teachers for the humanoid body and the dexterous hand. These teachers are then distilled into proprioception-conditioned latent priors, which are frozen and used as the action space for downstream residual reinforcement learning. A coordinated latent residual policy shares task context between body and hand while predicting separate latent corrections through dedicated residual heads, preserving natural whole-body motion and improving finger-level contact reliability.

The authors evaluate CoorDex on a Unitree G1 humanoid equipped with a 20-DoF WUJI hand. The system executes non-stop bottle grasping and carrying, fridge door opening while walking, and a cube pick-and-turn task. Ablations on the walk-grasp-carry task show that joint-space PPO, joint-space hand control, and monolithic latent prediction fail under the same reward budget, whereas the latent-prior interface and coordinated residual structure make high-dimensional contact-rich loco-manipulation trainable.

## Key Contributions

- A complete Isaac Lab learning pipeline for high-DoF dexterous humanoid loco-manipulation, covering demonstration collection, tracking teachers, prior distillation, and residual RL.
- Asymmetric body-hand prior composition that separates whole-body wrist placement from reusable finger coordination via a wrist-stabilized hand prior.
- Coordinated latent residual policy with shared task context and separate body-hand residual heads for structured high-dimensional control.
- Empirical ablations showing that joint-space PPO, joint-space hand control, and monolithic latent prediction fail under the same reward budget, validating the latent-prior interface and coordination structure.

## Relevance to Humanoid Robotics

CoorDex directly targets a mass-production and deployment capability gap for humanoid robots: the ability to manipulate objects dexterously while continuously locomoting. By enabling a commercial Unitree G1 with a high-DoF WUJI hand to perform non-stop grasping, door opening, and pick-and-turn behaviors, the work moves beyond stop-and-go or low-DoF manipulation paradigms that dominate current systems.

The hardware-software combination demonstrated in the paper—a commercial humanoid platform, a dexterous multi-finger hand, and a learned latent residual controller—also illustrates a pathway toward more flexible industrial and service applications where robots must coordinate whole-body posture with fine finger contacts without interrupting their motion.
