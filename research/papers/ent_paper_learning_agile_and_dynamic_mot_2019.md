---
$id: ent_paper_learning_agile_and_dynamic_mot_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Agile and Dynamic Motor Skills for Legged Robots
  zh: Learning Agile and Dynamic Motor Skills for Legged Robots
  ko: Learning Agile and Dynamic Motor Skills for Legged Robots
summary:
  en: Learning Agile and Dynamic Motor Skills for Legged Robots is a 2019 work on sim-to-real for humanoid robots.
  zh: Learning Agile and Dynamic Motor Skills for Legged Robots is a 2019 work on sim-to-real for humanoid robots.
  ko: Learning Agile and Dynamic Motor Skills for Legged Robots is a 2019 work on sim-to-real for humanoid robots.
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
- learning_agile_and_dynamic_mot
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1901.08652v1.
sources:
- id: src_001
  type: paper
  title: Learning Agile and Dynamic Motor Skills for Legged Robots (arXiv)
  url: https://arxiv.org/abs/1901.08652
  date: '2019'
  accessed_at: '2026-07-01'
---
## 概述
Legged robots pose one of the greatest challenges in robotics. Dynamic and agile maneuvers of animals cannot be imitated by existing methods that are crafted by humans. A compelling alternative is reinforcement learning, which requires minimal craftsmanship and promotes the natural evolution of a control policy. However, so far, reinforcement learning research for legged robots is mainly limited to simulation, and only few and comparably simple examples have been deployed on real systems. The primary reason is that training with real robots, particularly with dynamically balancing systems, is complicated and expensive. In the present work, we introduce a method for training a neural network policy in simulation and transferring it to a state-of-the-art legged system, thereby leveraging fast, automated, and cost-effective data generation schemes. The approach is applied to the ANYmal robot, a sophisticated medium-dog-sized quadrupedal system. Using policies trained in simulation, the quadrupedal machine achieves locomotion skills that go beyond what had been achieved with prior methods: ANYmal is capable of precisely and energy-efficiently following high-level body velocity commands, running faster than before, and recovering from falling even in complex configurations.

## 核心内容
Legged robots pose one of the greatest challenges in robotics. Dynamic and agile maneuvers of animals cannot be imitated by existing methods that are crafted by humans. A compelling alternative is reinforcement learning, which requires minimal craftsmanship and promotes the natural evolution of a control policy. However, so far, reinforcement learning research for legged robots is mainly limited to simulation, and only few and comparably simple examples have been deployed on real systems. The primary reason is that training with real robots, particularly with dynamically balancing systems, is complicated and expensive. In the present work, we introduce a method for training a neural network policy in simulation and transferring it to a state-of-the-art legged system, thereby leveraging fast, automated, and cost-effective data generation schemes. The approach is applied to the ANYmal robot, a sophisticated medium-dog-sized quadrupedal system. Using policies trained in simulation, the quadrupedal machine achieves locomotion skills that go beyond what had been achieved with prior methods: ANYmal is capable of precisely and energy-efficiently following high-level body velocity commands, running faster than before, and recovering from falling even in complex configurations.

## 参考
- http://arxiv.org/abs/1901.08652v1

## Overview
Legged robots pose one of the greatest challenges in robotics. Dynamic and agile maneuvers of animals cannot be imitated by existing methods that are crafted by humans. A compelling alternative is reinforcement learning, which requires minimal craftsmanship and promotes the natural evolution of a control policy. However, so far, reinforcement learning research for legged robots is mainly limited to simulation, and only few and comparably simple examples have been deployed on real systems. The primary reason is that training with real robots, particularly with dynamically balancing systems, is complicated and expensive. In the present work, we introduce a method for training a neural network policy in simulation and transferring it to a state-of-the-art legged system, thereby leveraging fast, automated, and cost-effective data generation schemes. The approach is applied to the ANYmal robot, a sophisticated medium-dog-sized quadrupedal system. Using policies trained in simulation, the quadrupedal machine achieves locomotion skills that go beyond what had been achieved with prior methods: ANYmal is capable of precisely and energy-efficiently following high-level body velocity commands, running faster than before, and recovering from falling even in complex configurations.

## Content
Legged robots pose one of the greatest challenges in robotics. Dynamic and agile maneuvers of animals cannot be imitated by existing methods that are crafted by humans. A compelling alternative is reinforcement learning, which requires minimal craftsmanship and promotes the natural evolution of a control policy. However, so far, reinforcement learning research for legged robots is mainly limited to simulation, and only few and comparably simple examples have been deployed on real systems. The primary reason is that training with real robots, particularly with dynamically balancing systems, is complicated and expensive. In the present work, we introduce a method for training a neural network policy in simulation and transferring it to a state-of-the-art legged system, thereby leveraging fast, automated, and cost-effective data generation schemes. The approach is applied to the ANYmal robot, a sophisticated medium-dog-sized quadrupedal system. Using policies trained in simulation, the quadrupedal machine achieves locomotion skills that go beyond what had been achieved with prior methods: ANYmal is capable of precisely and energy-efficiently following high-level body velocity commands, running faster than before, and recovering from falling even in complex configurations.

## 개요
보행 로봇은 로봇 공학에서 가장 큰 도전 과제 중 하나입니다. 동물의 역동적이고 민첩한 움직임은 인간이 고안한 기존 방법으로는 모방할 수 없습니다. 강력한 대안은 최소한의 수작업만 필요로 하며 제어 정책의 자연스러운 진화를 촉진하는 강화 학습입니다. 그러나 현재까지 보행 로봇을 위한 강화 학습 연구는 주로 시뮬레이션에 국한되어 있으며, 실제 시스템에 적용된 사례는 소수에 불과하고 비교적 단순한 예시에 그치고 있습니다. 주요 이유는 실제 로봇, 특히 동적 균형 시스템을 사용한 훈련이 복잡하고 비용이 많이 들기 때문입니다. 본 연구에서는 시뮬레이션에서 신경망 정책을 훈련하고 이를 최첨단 보행 시스템으로 전이하는 방법을 소개하여, 빠르고 자동화되며 비용 효율적인 데이터 생성 방식을 활용합니다. 이 접근법은 정교한 중형견 크기의 사족 보행 시스템인 ANYmal 로봇에 적용되었습니다. 시뮬레이션에서 훈련된 정책을 사용하여, 이 사족 보행 기계는 기존 방법으로는 달성하지 못한 보행 기술을 구현합니다: ANYmal은 높은 수준의 신체 속도 명령을 정밀하고 에너지 효율적으로 따르며, 이전보다 빠르게 달리고, 복잡한 자세에서도 넘어짐에서 회복할 수 있습니다.

## 핵심 내용
보행 로봇은 로봇 공학에서 가장 큰 도전 과제 중 하나입니다. 동물의 역동적이고 민첩한 움직임은 인간이 고안한 기존 방법으로는 모방할 수 없습니다. 강력한 대안은 최소한의 수작업만 필요로 하며 제어 정책의 자연스러운 진화를 촉진하는 강화 학습입니다. 그러나 현재까지 보행 로봇을 위한 강화 학습 연구는 주로 시뮬레이션에 국한되어 있으며, 실제 시스템에 적용된 사례는 소수에 불과하고 비교적 단순한 예시에 그치고 있습니다. 주요 이유는 실제 로봇, 특히 동적 균형 시스템을 사용한 훈련이 복잡하고 비용이 많이 들기 때문입니다. 본 연구에서는 시뮬레이션에서 신경망 정책을 훈련하고 이를 최첨단 보행 시스템으로 전이하는 방법을 소개하여, 빠르고 자동화되며 비용 효율적인 데이터 생성 방식을 활용합니다. 이 접근법은 정교한 중형견 크기의 사족 보행 시스템인 ANYmal 로봇에 적용되었습니다. 시뮬레이션에서 훈련된 정책을 사용하여, 이 사족 보행 기계는 기존 방법으로는 달성하지 못한 보행 기술을 구현합니다: ANYmal은 높은 수준의 신체 속도 명령을 정밀하고 에너지 효율적으로 따르며, 이전보다 빠르게 달리고, 복잡한 자세에서도 넘어짐에서 회복할 수 있습니다.
