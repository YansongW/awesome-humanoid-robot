---
$id: ent_paper_human_humanoid_robots_cross_em_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
  zh: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
  ko: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
summary:
  en: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
    is a 2024 work on loco-manipulation and whole-body-control for humanoid robots.
  zh: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
    is a 2024 work on loco-manipulation and whole-body-control for humanoid robots.
  ko: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
    is a 2024 work on loco-manipulation and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_humanoid_robots_cross_em
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.15166v1.
sources:
- id: src_001
  type: paper
  title: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
    (arXiv)
  url: https://arxiv.org/abs/2412.15166
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots are envisioned as embodied intelligent agents capable of performing a wide range of human-level loco-manipulation tasks, particularly in scenarios requiring strenuous and repetitive labor. However, learning these skills is challenging due to the high degrees of freedom of humanoid robots, and collecting sufficient training data for humanoid is a laborious process. Given the rapid introduction of new humanoid platforms, a cross-embodiment framework that allows generalizable skill transfer is becoming increasingly critical. To address this, we propose a transferable framework that reduces the data bottleneck by using a unified digital human model as a common prototype and bypassing the need for re-training on every new robot platform. The model learns behavior primitives from human demonstrations through adversarial imitation, and the complex robot structures are decomposed into functional components, each trained independently and dynamically coordinated. Task generalization is achieved through a human-object interaction graph, and skills are transferred to different robots via embodiment-specific kinematic motion retargeting and dynamic fine-tuning. Our framework is validated on five humanoid robots with diverse configurations, demonstrating stable loco-manipulation and highlighting its effectiveness in reducing data requirements and increasing the efficiency of skill transfer across platforms.

## 核心内容
Humanoid robots are envisioned as embodied intelligent agents capable of performing a wide range of human-level loco-manipulation tasks, particularly in scenarios requiring strenuous and repetitive labor. However, learning these skills is challenging due to the high degrees of freedom of humanoid robots, and collecting sufficient training data for humanoid is a laborious process. Given the rapid introduction of new humanoid platforms, a cross-embodiment framework that allows generalizable skill transfer is becoming increasingly critical. To address this, we propose a transferable framework that reduces the data bottleneck by using a unified digital human model as a common prototype and bypassing the need for re-training on every new robot platform. The model learns behavior primitives from human demonstrations through adversarial imitation, and the complex robot structures are decomposed into functional components, each trained independently and dynamically coordinated. Task generalization is achieved through a human-object interaction graph, and skills are transferred to different robots via embodiment-specific kinematic motion retargeting and dynamic fine-tuning. Our framework is validated on five humanoid robots with diverse configurations, demonstrating stable loco-manipulation and highlighting its effectiveness in reducing data requirements and increasing the efficiency of skill transfer across platforms.

## 参考
- http://arxiv.org/abs/2412.15166v1

## Overview
Humanoid robots are envisioned as embodied intelligent agents capable of performing a wide range of human-level loco-manipulation tasks, particularly in scenarios requiring strenuous and repetitive labor. However, learning these skills is challenging due to the high degrees of freedom of humanoid robots, and collecting sufficient training data for humanoid is a laborious process. Given the rapid introduction of new humanoid platforms, a cross-embodiment framework that allows generalizable skill transfer is becoming increasingly critical. To address this, we propose a transferable framework that reduces the data bottleneck by using a unified digital human model as a common prototype and bypassing the need for re-training on every new robot platform. The model learns behavior primitives from human demonstrations through adversarial imitation, and the complex robot structures are decomposed into functional components, each trained independently and dynamically coordinated. Task generalization is achieved through a human-object interaction graph, and skills are transferred to different robots via embodiment-specific kinematic motion retargeting and dynamic fine-tuning. Our framework is validated on five humanoid robots with diverse configurations, demonstrating stable loco-manipulation and highlighting its effectiveness in reducing data requirements and increasing the efficiency of skill transfer across platforms.

## Content
Humanoid robots are envisioned as embodied intelligent agents capable of performing a wide range of human-level loco-manipulation tasks, particularly in scenarios requiring strenuous and repetitive labor. However, learning these skills is challenging due to the high degrees of freedom of humanoid robots, and collecting sufficient training data for humanoid is a laborious process. Given the rapid introduction of new humanoid platforms, a cross-embodiment framework that allows generalizable skill transfer is becoming increasingly critical. To address this, we propose a transferable framework that reduces the data bottleneck by using a unified digital human model as a common prototype and bypassing the need for re-training on every new robot platform. The model learns behavior primitives from human demonstrations through adversarial imitation, and the complex robot structures are decomposed into functional components, each trained independently and dynamically coordinated. Task generalization is achieved through a human-object interaction graph, and skills are transferred to different robots via embodiment-specific kinematic motion retargeting and dynamic fine-tuning. Our framework is validated on five humanoid robots with diverse configurations, demonstrating stable loco-manipulation and highlighting its effectiveness in reducing data requirements and increasing the efficiency of skill transfer across platforms.

## 개요
휴머노이드 로봇은 특히 힘들고 반복적인 노동이 필요한 상황에서 다양한 인간 수준의 이동-조작 작업을 수행할 수 있는 구현된 지능형 에이전트로 구상됩니다. 그러나 휴머노이드 로봇의 높은 자유도로 인해 이러한 기술을 학습하는 것은 어려우며, 휴머노이드를 위한 충분한 훈련 데이터를 수집하는 것은 힘든 과정입니다. 새로운 휴머노이드 플랫폼이 빠르게 도입됨에 따라, 일반화 가능한 기술 전이를 가능하게 하는 교차 구현 프레임워크가 점점 더 중요해지고 있습니다. 이를 해결하기 위해, 우리는 통합된 디지털 휴먼 모델을 공통 프로토타입으로 사용하여 데이터 병목 현상을 줄이고, 새로운 로봇 플랫폼마다 재훈련할 필요를 없애는 전이 가능한 프레임워크를 제안합니다. 이 모델은 적대적 모방을 통해 인간 시연으로부터 행동 프리미티브를 학습하며, 복잡한 로봇 구조는 기능적 구성 요소로 분해되어 각각 독립적으로 훈련되고 동적으로 조정됩니다. 작업 일반화는 인간-객체 상호작용 그래프를 통해 달성되며, 기술은 구현별 운동학적 동작 리타겟팅과 동적 미세 조정을 통해 다른 로봇으로 전이됩니다. 우리의 프레임워크는 다양한 구성을 가진 다섯 대의 휴머노이드 로봇에서 검증되어 안정적인 이동-조작을 입증하고, 데이터 요구량을 줄이고 플랫폼 간 기술 전이 효율성을 높이는 데 효과적임을 강조합니다.

## 핵심 내용
휴머노이드 로봇은 특히 힘들고 반복적인 노동이 필요한 상황에서 다양한 인간 수준의 이동-조작 작업을 수행할 수 있는 구현된 지능형 에이전트로 구상됩니다. 그러나 휴머노이드 로봇의 높은 자유도로 인해 이러한 기술을 학습하는 것은 어려우며, 휴머노이드를 위한 충분한 훈련 데이터를 수집하는 것은 힘든 과정입니다. 새로운 휴머노이드 플랫폼이 빠르게 도입됨에 따라, 일반화 가능한 기술 전이를 가능하게 하는 교차 구현 프레임워크가 점점 더 중요해지고 있습니다. 이를 해결하기 위해, 우리는 통합된 디지털 휴먼 모델을 공통 프로토타입으로 사용하여 데이터 병목 현상을 줄이고, 새로운 로봇 플랫폼마다 재훈련할 필요를 없애는 전이 가능한 프레임워크를 제안합니다. 이 모델은 적대적 모방을 통해 인간 시연으로부터 행동 프리미티브를 학습하며, 복잡한 로봇 구조는 기능적 구성 요소로 분해되어 각각 독립적으로 훈련되고 동적으로 조정됩니다. 작업 일반화는 인간-객체 상호작용 그래프를 통해 달성되며, 기술은 구현별 운동학적 동작 리타겟팅과 동적 미세 조정을 통해 다른 로봇으로 전이됩니다. 우리의 프레임워크는 다양한 구성을 가진 다섯 대의 휴머노이드 로봇에서 검증되어 안정적인 이동-조작을 입증하고, 데이터 요구량을 줄이고 플랫폼 간 기술 전이 효율성을 높이는 데 효과적임을 강조합니다.
