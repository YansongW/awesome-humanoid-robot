---
$id: ent_paper_residual_off_policy_rl_for_fin_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Residual Off-Policy RL for Finetuning Behavior Cloning Policies
  zh: Residual Off-Policy RL for Finetuning Behavior Cloning Policies
  ko: Residual Off-Policy RL for Finetuning Behavior Cloning Policies
summary:
  en: Residual Off-Policy RL for Finetuning Behavior Cloning Policies is a 2025 work on manipulation for humanoid robots.
  zh: Residual Off-Policy RL for Finetuning Behavior Cloning Policies is a 2025 work on manipulation for humanoid robots.
  ko: Residual Off-Policy RL for Finetuning Behavior Cloning Policies is a 2025 work on manipulation for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- manipulation
- residual_off_policy_rl_for_fin
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19301v2.
sources:
- id: src_001
  type: paper
  title: Residual Off-Policy RL for Finetuning Behavior Cloning Policies (arXiv)
  url: https://arxiv.org/abs/2509.19301
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in behavior cloning (BC) have enabled impressive visuomotor control policies. However, these approaches are limited by the quality of human demonstrations, the manual effort required for data collection, and the diminishing returns from offline data. In comparison, reinforcement learning (RL) trains an agent through autonomous interaction with the environment and has shown remarkable success in various domains. Still, training RL policies directly on real-world robots remains challenging due to sample inefficiency, safety concerns, and the difficulty of learning from sparse rewards for long-horizon tasks, especially for high-degree-of-freedom (DoF) systems.   We present a recipe that combines the benefits of BC and RL through a residual learning framework. Our approach leverages BC policies as black-box bases and learns lightweight per-step residual corrections via sample-efficient off-policy RL. We demonstrate that our method requires only sparse binary reward signals and can effectively improve manipulation policies on high-degree-of-freedom (DoF) systems in both simulation and the real world. In particular, we demonstrate, to the best of our knowledge, the first successful real-world RL training on a humanoid robot with dexterous hands. Our results demonstrate state-of-the-art performance in various vision-based tasks, pointing towards a practical pathway for deploying RL in the real world.

## 核心内容
Recent advances in behavior cloning (BC) have enabled impressive visuomotor control policies. However, these approaches are limited by the quality of human demonstrations, the manual effort required for data collection, and the diminishing returns from offline data. In comparison, reinforcement learning (RL) trains an agent through autonomous interaction with the environment and has shown remarkable success in various domains. Still, training RL policies directly on real-world robots remains challenging due to sample inefficiency, safety concerns, and the difficulty of learning from sparse rewards for long-horizon tasks, especially for high-degree-of-freedom (DoF) systems.   We present a recipe that combines the benefits of BC and RL through a residual learning framework. Our approach leverages BC policies as black-box bases and learns lightweight per-step residual corrections via sample-efficient off-policy RL. We demonstrate that our method requires only sparse binary reward signals and can effectively improve manipulation policies on high-degree-of-freedom (DoF) systems in both simulation and the real world. In particular, we demonstrate, to the best of our knowledge, the first successful real-world RL training on a humanoid robot with dexterous hands. Our results demonstrate state-of-the-art performance in various vision-based tasks, pointing towards a practical pathway for deploying RL in the real world.

## 参考
- http://arxiv.org/abs/2509.19301v2

## Overview
Recent advances in behavior cloning (BC) have enabled impressive visuomotor control policies. However, these approaches are limited by the quality of human demonstrations, the manual effort required for data collection, and the diminishing returns from offline data. In comparison, reinforcement learning (RL) trains an agent through autonomous interaction with the environment and has shown remarkable success in various domains. Still, training RL policies directly on real-world robots remains challenging due to sample inefficiency, safety concerns, and the difficulty of learning from sparse rewards for long-horizon tasks, especially for high-degree-of-freedom (DoF) systems. We present a recipe that combines the benefits of BC and RL through a residual learning framework. Our approach leverages BC policies as black-box bases and learns lightweight per-step residual corrections via sample-efficient off-policy RL. We demonstrate that our method requires only sparse binary reward signals and can effectively improve manipulation policies on high-degree-of-freedom (DoF) systems in both simulation and the real world. In particular, we demonstrate, to the best of our knowledge, the first successful real-world RL training on a humanoid robot with dexterous hands. Our results demonstrate state-of-the-art performance in various vision-based tasks, pointing towards a practical pathway for deploying RL in the real world.

## Content
Recent advances in behavior cloning (BC) have enabled impressive visuomotor control policies. However, these approaches are limited by the quality of human demonstrations, the manual effort required for data collection, and the diminishing returns from offline data. In comparison, reinforcement learning (RL) trains an agent through autonomous interaction with the environment and has shown remarkable success in various domains. Still, training RL policies directly on real-world robots remains challenging due to sample inefficiency, safety concerns, and the difficulty of learning from sparse rewards for long-horizon tasks, especially for high-degree-of-freedom (DoF) systems. We present a recipe that combines the benefits of BC and RL through a residual learning framework. Our approach leverages BC policies as black-box bases and learns lightweight per-step residual corrections via sample-efficient off-policy RL. We demonstrate that our method requires only sparse binary reward signals and can effectively improve manipulation policies on high-degree-of-freedom (DoF) systems in both simulation and the real world. In particular, we demonstrate, to the best of our knowledge, the first successful real-world RL training on a humanoid robot with dexterous hands. Our results demonstrate state-of-the-art performance in various vision-based tasks, pointing towards a practical pathway for deploying RL in the real world.

## 개요
최근 행동 복제(BC)의 발전은 인상적인 시각-운동 제어 정책을 가능하게 했습니다. 그러나 이러한 접근 방식은 인간 시연의 품질, 데이터 수집에 필요한 수동 노력, 그리고 오프라인 데이터의 수확 체감에 의해 제한됩니다. 이와 비교하여 강화 학습(RL)은 환경과의 자율적 상호작용을 통해 에이전트를 훈련시키며 다양한 분야에서 놀라운 성공을 거두었습니다. 그럼에도 불구하고, 실제 로봇에 RL 정책을 직접 훈련시키는 것은 샘플 비효율성, 안전 문제, 특히 고자유도(DoF) 시스템에서 장기 과제에 대한 희소 보상으로부터 학습의 어려움으로 인해 여전히 도전적입니다. 우리는 잔차 학습 프레임워크를 통해 BC와 RL의 이점을 결합한 방법을 제시합니다. 우리의 접근 방식은 BC 정책을 블랙박스 기반으로 활용하고, 샘플 효율적인 오프-폴리시 RL을 통해 가벼운 단계별 잔차 보정을 학습합니다. 우리의 방법은 희소 이진 보상 신호만 필요로 하며, 시뮬레이션과 실제 환경 모두에서 고자유도(DoF) 시스템의 조작 정책을 효과적으로 개선할 수 있음을 입증합니다. 특히, 우리가 아는 한, 우리는 손재주가 뛰어난 손을 가진 휴머노이드 로봇에서 최초로 성공적인 실제 RL 훈련을 시연합니다. 우리의 결과는 다양한 시각 기반 작업에서 최첨단 성능을 보여주며, 실제 환경에서 RL을 배포하기 위한 실용적인 경로를 제시합니다.

## 핵심 내용
최근 행동 복제(BC)의 발전은 인상적인 시각-운동 제어 정책을 가능하게 했습니다. 그러나 이러한 접근 방식은 인간 시연의 품질, 데이터 수집에 필요한 수동 노력, 그리고 오프라인 데이터의 수확 체감에 의해 제한됩니다. 이와 비교하여 강화 학습(RL)은 환경과의 자율적 상호작용을 통해 에이전트를 훈련시키며 다양한 분야에서 놀라운 성공을 거두었습니다. 그럼에도 불구하고, 실제 로봇에 RL 정책을 직접 훈련시키는 것은 샘플 비효율성, 안전 문제, 특히 고자유도(DoF) 시스템에서 장기 과제에 대한 희소 보상으로부터 학습의 어려움으로 인해 여전히 도전적입니다. 우리는 잔차 학습 프레임워크를 통해 BC와 RL의 이점을 결합한 방법을 제시합니다. 우리의 접근 방식은 BC 정책을 블랙박스 기반으로 활용하고, 샘플 효율적인 오프-폴리시 RL을 통해 가벼운 단계별 잔차 보정을 학습합니다. 우리의 방법은 희소 이진 보상 신호만 필요로 하며, 시뮬레이션과 실제 환경 모두에서 고자유도(DoF) 시스템의 조작 정책을 효과적으로 개선할 수 있음을 입증합니다. 특히, 우리가 아는 한, 우리는 손재주가 뛰어난 손을 가진 휴머노이드 로봇에서 최초로 성공적인 실제 RL 훈련을 시연합니다. 우리의 결과는 다양한 시각 기반 작업에서 최첨단 성능을 보여주며, 실제 환경에서 RL을 배포하기 위한 실용적인 경로를 제시합니다.
