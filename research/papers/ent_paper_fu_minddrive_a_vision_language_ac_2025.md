---
$id: ent_paper_fu_minddrive_a_vision_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning'
  zh: MindDrive
  ko: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning'
summary:
  en: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning (MindDrive), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Xiaomi EV.'
  zh: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning (MindDrive), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Xiaomi EV.'
  ko: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning (MindDrive), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Xiaomi EV.'
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
- minddrive
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13636v3.
sources:
- id: src_001
  type: paper
  title: 'MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2512.13636
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MindDrive source
  url: https://doi.org/10.48550/arXiv.2512.13636
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Current Vision-Language-Action (VLA) paradigms in autonomous driving primarily rely on Imitation Learning (IL), which introduces inherent challenges such as distribution shift and causal confusion. Online Reinforcement Learning offers a promising pathway to address these issues through trial-and-error learning. However, applying online reinforcement learning to VLA models in autonomous driving is hindered by inefficient exploration in continuous action spaces. To overcome this limitation, we propose MindDrive, a VLA framework comprising a large language model (LLM) with two distinct sets of LoRA parameters. The one LLM serves as a Decision Expert for scenario reasoning and driving decision-making, while the other acts as an Action Expert that dynamically maps linguistic decisions into feasible trajectories. By feeding trajectory-level rewards back into the reasoning space, MindDrive enables trial-and-error learning over a finite set of discrete linguistic driving decisions, instead of operating directly in a continuous action space. This approach effectively balances optimal decision-making in complex scenarios, human-like driving behavior, and efficient exploration in online reinforcement learning. Using the lightweight Qwen-0.5B LLM, MindDrive achieves Driving Score (DS) of 78.04 and Success Rate (SR) of 55.09% on the challenging Bench2Drive benchmark. To the best of our knowledge, this is the first work to demonstrate the effectiveness of online reinforcement learning for the VLA model in autonomous driving.

## 核心内容
Current Vision-Language-Action (VLA) paradigms in autonomous driving primarily rely on Imitation Learning (IL), which introduces inherent challenges such as distribution shift and causal confusion. Online Reinforcement Learning offers a promising pathway to address these issues through trial-and-error learning. However, applying online reinforcement learning to VLA models in autonomous driving is hindered by inefficient exploration in continuous action spaces. To overcome this limitation, we propose MindDrive, a VLA framework comprising a large language model (LLM) with two distinct sets of LoRA parameters. The one LLM serves as a Decision Expert for scenario reasoning and driving decision-making, while the other acts as an Action Expert that dynamically maps linguistic decisions into feasible trajectories. By feeding trajectory-level rewards back into the reasoning space, MindDrive enables trial-and-error learning over a finite set of discrete linguistic driving decisions, instead of operating directly in a continuous action space. This approach effectively balances optimal decision-making in complex scenarios, human-like driving behavior, and efficient exploration in online reinforcement learning. Using the lightweight Qwen-0.5B LLM, MindDrive achieves Driving Score (DS) of 78.04 and Success Rate (SR) of 55.09% on the challenging Bench2Drive benchmark. To the best of our knowledge, this is the first work to demonstrate the effectiveness of online reinforcement learning for the VLA model in autonomous driving.

## 参考
- http://arxiv.org/abs/2512.13636v3

## Overview
Current Vision-Language-Action (VLA) paradigms in autonomous driving primarily rely on Imitation Learning (IL), which introduces inherent challenges such as distribution shift and causal confusion. Online Reinforcement Learning offers a promising pathway to address these issues through trial-and-error learning. However, applying online reinforcement learning to VLA models in autonomous driving is hindered by inefficient exploration in continuous action spaces. To overcome this limitation, we propose MindDrive, a VLA framework comprising a large language model (LLM) with two distinct sets of LoRA parameters. The one LLM serves as a Decision Expert for scenario reasoning and driving decision-making, while the other acts as an Action Expert that dynamically maps linguistic decisions into feasible trajectories. By feeding trajectory-level rewards back into the reasoning space, MindDrive enables trial-and-error learning over a finite set of discrete linguistic driving decisions, instead of operating directly in a continuous action space. This approach effectively balances optimal decision-making in complex scenarios, human-like driving behavior, and efficient exploration in online reinforcement learning. Using the lightweight Qwen-0.5B LLM, MindDrive achieves Driving Score (DS) of 78.04 and Success Rate (SR) of 55.09% on the challenging Bench2Drive benchmark. To the best of our knowledge, this is the first work to demonstrate the effectiveness of online reinforcement learning for the VLA model in autonomous driving.

## Content
Current Vision-Language-Action (VLA) paradigms in autonomous driving primarily rely on Imitation Learning (IL), which introduces inherent challenges such as distribution shift and causal confusion. Online Reinforcement Learning offers a promising pathway to address these issues through trial-and-error learning. However, applying online reinforcement learning to VLA models in autonomous driving is hindered by inefficient exploration in continuous action spaces. To overcome this limitation, we propose MindDrive, a VLA framework comprising a large language model (LLM) with two distinct sets of LoRA parameters. The one LLM serves as a Decision Expert for scenario reasoning and driving decision-making, while the other acts as an Action Expert that dynamically maps linguistic decisions into feasible trajectories. By feeding trajectory-level rewards back into the reasoning space, MindDrive enables trial-and-error learning over a finite set of discrete linguistic driving decisions, instead of operating directly in a continuous action space. This approach effectively balances optimal decision-making in complex scenarios, human-like driving behavior, and efficient exploration in online reinforcement learning. Using the lightweight Qwen-0.5B LLM, MindDrive achieves Driving Score (DS) of 78.04 and Success Rate (SR) of 55.09% on the challenging Bench2Drive benchmark. To the best of our knowledge, this is the first work to demonstrate the effectiveness of online reinforcement learning for the VLA model in autonomous driving.

## 개요
현재 자율주행 분야의 Vision-Language-Action (VLA) 패러다임은 주로 모방 학습(IL)에 의존하며, 이는 분포 변화(distribution shift)와 인과 혼란(causal confusion)과 같은 본질적인 문제를 야기합니다. 온라인 강화 학습(Online Reinforcement Learning)은 시행착오 학습을 통해 이러한 문제를 해결할 유망한 접근법을 제공합니다. 그러나 자율주행에서 VLA 모델에 온라인 강화 학습을 적용하는 것은 연속적인 행동 공간에서의 비효율적인 탐색으로 인해 어려움을 겪습니다. 이러한 한계를 극복하기 위해, 우리는 두 개의 서로 다른 LoRA 파라미터 세트를 가진 대규모 언어 모델(LLM)로 구성된 VLA 프레임워크인 MindDrive를 제안합니다. 하나의 LLM은 시나리오 추론 및 주행 의사 결정을 위한 Decision Expert 역할을 하고, 다른 하나는 언어적 결정을 실행 가능한 궤적으로 동적으로 매핑하는 Action Expert 역할을 합니다. 궤적 수준의 보상을 추론 공간에 피드백함으로써, MindDrive는 연속적인 행동 공간에서 직접 작동하는 대신 유한한 이산적 언어 주행 결정 집합에 대해 시행착오 학습을 가능하게 합니다. 이 접근법은 복잡한 시나리오에서의 최적 의사 결정, 인간과 유사한 주행 행동, 그리고 온라인 강화 학습에서의 효율적인 탐색을 효과적으로 균형 있게 조정합니다. 경량화된 Qwen-0.5B LLM을 사용하여, MindDrive는 까다로운 Bench2Drive 벤치마크에서 주행 점수(DS) 78.04와 성공률(SR) 55.09%를 달성했습니다. 우리가 아는 한, 이는 자율주행에서 VLA 모델에 대한 온라인 강화 학습의 효과를 입증한 최초의 연구입니다.

## 핵심 내용
현재 자율주행 분야의 Vision-Language-Action (VLA) 패러다임은 주로 모방 학습(IL)에 의존하며, 이는 분포 변화(distribution shift)와 인과 혼란(causal confusion)과 같은 본질적인 문제를 야기합니다. 온라인 강화 학습(Online Reinforcement Learning)은 시행착오 학습을 통해 이러한 문제를 해결할 유망한 접근법을 제공합니다. 그러나 자율주행에서 VLA 모델에 온라인 강화 학습을 적용하는 것은 연속적인 행동 공간에서의 비효율적인 탐색으로 인해 어려움을 겪습니다. 이러한 한계를 극복하기 위해, 우리는 두 개의 서로 다른 LoRA 파라미터 세트를 가진 대규모 언어 모델(LLM)로 구성된 VLA 프레임워크인 MindDrive를 제안합니다. 하나의 LLM은 시나리오 추론 및 주행 의사 결정을 위한 Decision Expert 역할을 하고, 다른 하나는 언어적 결정을 실행 가능한 궤적으로 동적으로 매핑하는 Action Expert 역할을 합니다. 궤적 수준의 보상을 추론 공간에 피드백함으로써, MindDrive는 연속적인 행동 공간에서 직접 작동하는 대신 유한한 이산적 언어 주행 결정 집합에 대해 시행착오 학습을 가능하게 합니다. 이 접근법은 복잡한 시나리오에서의 최적 의사 결정, 인간과 유사한 주행 행동, 그리고 온라인 강화 학습에서의 효율적인 탐색을 효과적으로 균형 있게 조정합니다. 경량화된 Qwen-0.5B LLM을 사용하여, MindDrive는 까다로운 Bench2Drive 벤치마크에서 주행 점수(DS) 78.04와 성공률(SR) 55.09%를 달성했습니다. 우리가 아는 한, 이는 자율주행에서 VLA 모델에 대한 온라인 강화 학습의 효과를 입증한 최초의 연구입니다.
