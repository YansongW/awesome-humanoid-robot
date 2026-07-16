---
$id: ent_paper_learning_symmetric_and_low_ene_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Symmetric and Low-energy Locomotion
  zh: Learning Symmetric and Low-energy Locomotion
  ko: Learning Symmetric and Low-energy Locomotion
summary:
  en: Learning Symmetric and Low-energy Locomotion is a 2018 work on physics-based character animation for humanoid robots.
  zh: Learning Symmetric and Low-energy Locomotion is a 2018 work on physics-based character animation for humanoid robots.
  ko: Learning Symmetric and Low-energy Locomotion is a 2018 work on physics-based character animation for humanoid robots.
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
- learning_symmetric_and_low_ene
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1801.08093v3.
sources:
- id: src_001
  type: paper
  title: Learning Symmetric and Low-energy Locomotion (arXiv)
  url: https://arxiv.org/abs/1801.08093
  date: '2018'
  accessed_at: '2026-07-01'
---
## 概述
Learning locomotion skills is a challenging problem. To generate realistic and smooth locomotion, existing methods use motion capture, finite state machines or morphology-specific knowledge to guide the motion generation algorithms. Deep reinforcement learning (DRL) is a promising approach for the automatic creation of locomotion control. Indeed, a standard benchmark for DRL is to automatically create a running controller for a biped character from a simple reward function. Although several different DRL algorithms can successfully create a running controller, the resulting motions usually look nothing like a real runner. This paper takes a minimalist learning approach to the locomotion problem, without the use of motion examples, finite state machines, or morphology-specific knowledge. We introduce two modifications to the DRL approach that, when used together, produce locomotion behaviors that are symmetric, low-energy, and much closer to that of a real person. First, we introduce a new term to the loss function (not the reward function) that encourages symmetric actions. Second, we introduce a new curriculum learning method that provides modulated physical assistance to help the character with left/right balance and forward movement. The algorithm automatically computes appropriate assistance to the character and gradually relaxes this assistance, so that eventually the character learns to move entirely without help. Because our method does not make use of motion capture data, it can be applied to a variety of character morphologies. We demonstrate locomotion controllers for the lower half of a biped, a full humanoid, a quadruped, and a hexapod. Our results show that learned policies are able to produce symmetric, low-energy gaits. In addition, speed-appropriate gait patterns emerge without any guidance from motion examples or contact planning.

## 核心内容
Learning locomotion skills is a challenging problem. To generate realistic and smooth locomotion, existing methods use motion capture, finite state machines or morphology-specific knowledge to guide the motion generation algorithms. Deep reinforcement learning (DRL) is a promising approach for the automatic creation of locomotion control. Indeed, a standard benchmark for DRL is to automatically create a running controller for a biped character from a simple reward function. Although several different DRL algorithms can successfully create a running controller, the resulting motions usually look nothing like a real runner. This paper takes a minimalist learning approach to the locomotion problem, without the use of motion examples, finite state machines, or morphology-specific knowledge. We introduce two modifications to the DRL approach that, when used together, produce locomotion behaviors that are symmetric, low-energy, and much closer to that of a real person. First, we introduce a new term to the loss function (not the reward function) that encourages symmetric actions. Second, we introduce a new curriculum learning method that provides modulated physical assistance to help the character with left/right balance and forward movement. The algorithm automatically computes appropriate assistance to the character and gradually relaxes this assistance, so that eventually the character learns to move entirely without help. Because our method does not make use of motion capture data, it can be applied to a variety of character morphologies. We demonstrate locomotion controllers for the lower half of a biped, a full humanoid, a quadruped, and a hexapod. Our results show that learned policies are able to produce symmetric, low-energy gaits. In addition, speed-appropriate gait patterns emerge without any guidance from motion examples or contact planning.

## 参考
- http://arxiv.org/abs/1801.08093v3

## Overview
Learning locomotion skills is a challenging problem. To generate realistic and smooth locomotion, existing methods use motion capture, finite state machines or morphology-specific knowledge to guide the motion generation algorithms. Deep reinforcement learning (DRL) is a promising approach for the automatic creation of locomotion control. Indeed, a standard benchmark for DRL is to automatically create a running controller for a biped character from a simple reward function. Although several different DRL algorithms can successfully create a running controller, the resulting motions usually look nothing like a real runner. This paper takes a minimalist learning approach to the locomotion problem, without the use of motion examples, finite state machines, or morphology-specific knowledge. We introduce two modifications to the DRL approach that, when used together, produce locomotion behaviors that are symmetric, low-energy, and much closer to that of a real person. First, we introduce a new term to the loss function (not the reward function) that encourages symmetric actions. Second, we introduce a new curriculum learning method that provides modulated physical assistance to help the character with left/right balance and forward movement. The algorithm automatically computes appropriate assistance to the character and gradually relaxes this assistance, so that eventually the character learns to move entirely without help. Because our method does not make use of motion capture data, it can be applied to a variety of character morphologies. We demonstrate locomotion controllers for the lower half of a biped, a full humanoid, a quadruped, and a hexapod. Our results show that learned policies are able to produce symmetric, low-energy gaits. In addition, speed-appropriate gait patterns emerge without any guidance from motion examples or contact planning.

## Content
Learning locomotion skills is a challenging problem. To generate realistic and smooth locomotion, existing methods use motion capture, finite state machines or morphology-specific knowledge to guide the motion generation algorithms. Deep reinforcement learning (DRL) is a promising approach for the automatic creation of locomotion control. Indeed, a standard benchmark for DRL is to automatically create a running controller for a biped character from a simple reward function. Although several different DRL algorithms can successfully create a running controller, the resulting motions usually look nothing like a real runner. This paper takes a minimalist learning approach to the locomotion problem, without the use of motion examples, finite state machines, or morphology-specific knowledge. We introduce two modifications to the DRL approach that, when used together, produce locomotion behaviors that are symmetric, low-energy, and much closer to that of a real person. First, we introduce a new term to the loss function (not the reward function) that encourages symmetric actions. Second, we introduce a new curriculum learning method that provides modulated physical assistance to help the character with left/right balance and forward movement. The algorithm automatically computes appropriate assistance to the character and gradually relaxes this assistance, so that eventually the character learns to move entirely without help. Because our method does not make use of motion capture data, it can be applied to a variety of character morphologies. We demonstrate locomotion controllers for the lower half of a biped, a full humanoid, a quadruped, and a hexapod. Our results show that learned policies are able to produce symmetric, low-energy gaits. In addition, speed-appropriate gait patterns emerge without any guidance from motion examples or contact planning.

## 개요
보행 기술을 학습하는 것은 도전적인 문제입니다. 현실적이고 부드러운 보행을 생성하기 위해 기존 방법들은 모션 캡처, 유한 상태 기계 또는 형태별 지식을 활용하여 동작 생성 알고리즘을 안내합니다. 심층 강화 학습(DRL)은 보행 제어를 자동으로 생성하기 위한 유망한 접근 방식입니다. 실제로 DRL의 표준 벤치마크 중 하나는 단순한 보상 함수로부터 이족 캐릭터의 달리기 제어기를 자동으로 생성하는 것입니다. 여러 DRL 알고리즘이 성공적으로 달리기 제어기를 생성할 수 있지만, 결과 동작은 일반적으로 실제 주자와 전혀 닮지 않습니다. 본 논문은 모션 예제, 유한 상태 기계 또는 형태별 지식을 사용하지 않고 보행 문제에 대한 미니멀리스트 학습 접근 방식을 취합니다. 우리는 DRL 접근 방식에 두 가지 수정을 도입하여, 함께 사용할 때 대칭적이고 저에너지이며 실제 사람의 보행에 훨씬 가까운 보행 행동을 생성합니다. 첫째, 대칭적 행동을 장려하는 손실 함수(보상 함수가 아님)에 새로운 항을 도입합니다. 둘째, 캐릭터의 좌/우 균형 및 전진 이동을 돕기 위해 조정된 물리적 지원을 제공하는 새로운 커리큘럼 학습 방법을 도입합니다. 알고리즘은 캐릭터에 적절한 지원을 자동으로 계산하고 이 지원을 점진적으로 완화하여, 결국 캐릭터가 완전히 도움 없이 움직이는 법을 학습합니다. 우리의 방법은 모션 캡처 데이터를 사용하지 않기 때문에 다양한 캐릭터 형태에 적용할 수 있습니다. 우리는 이족 보행체의 하반신, 완전한 휴머노이드, 사족 보행체, 그리고 육족 보행체에 대한 보행 제어기를 시연합니다. 결과는 학습된 정책이 대칭적이고 저에너지의 걸음걸이를 생성할 수 있음을 보여줍니다. 또한, 모션 예제나 접촉 계획의 안내 없이 속도에 적합한 걸음걸이 패턴이 나타납니다.

## 핵심 내용
보행 기술을 학습하는 것은 도전적인 문제입니다. 현실적이고 부드러운 보행을 생성하기 위해 기존 방법들은 모션 캡처, 유한 상태 기계 또는 형태별 지식을 활용하여 동작 생성 알고리즘을 안내합니다. 심층 강화 학습(DRL)은 보행 제어를 자동으로 생성하기 위한 유망한 접근 방식입니다. 실제로 DRL의 표준 벤치마크 중 하나는 단순한 보상 함수로부터 이족 캐릭터의 달리기 제어기를 자동으로 생성하는 것입니다. 여러 DRL 알고리즘이 성공적으로 달리기 제어기를 생성할 수 있지만, 결과 동작은 일반적으로 실제 주자와 전혀 닮지 않습니다. 본 논문은 모션 예제, 유한 상태 기계 또는 형태별 지식을 사용하지 않고 보행 문제에 대한 미니멀리스트 학습 접근 방식을 취합니다. 우리는 DRL 접근 방식에 두 가지 수정을 도입하여, 함께 사용할 때 대칭적이고 저에너지이며 실제 사람의 보행에 훨씬 가까운 보행 행동을 생성합니다. 첫째, 대칭적 행동을 장려하는 손실 함수(보상 함수가 아님)에 새로운 항을 도입합니다. 둘째, 캐릭터의 좌/우 균형 및 전진 이동을 돕기 위해 조정된 물리적 지원을 제공하는 새로운 커리큘럼 학습 방법을 도입합니다. 알고리즘은 캐릭터에 적절한 지원을 자동으로 계산하고 이 지원을 점진적으로 완화하여, 결국 캐릭터가 완전히 도움 없이 움직이는 법을 학습합니다. 우리의 방법은 모션 캡처 데이터를 사용하지 않기 때문에 다양한 캐릭터 형태에 적용할 수 있습니다. 우리는 이족 보행체의 하반신, 완전한 휴머노이드, 사족 보행체, 그리고 육족 보행체에 대한 보행 제어기를 시연합니다. 결과는 학습된 정책이 대칭적이고 저에너지의 걸음걸이를 생성할 수 있음을 보여줍니다. 또한, 모션 예제나 접촉 계획의 안내 없이 속도에 적합한 걸음걸이 패턴이 나타납니다.
