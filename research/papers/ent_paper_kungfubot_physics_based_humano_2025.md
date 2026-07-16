---
$id: ent_paper_kungfubot_physics_based_humano_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills'
  zh: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills'
  ko: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills'
summary:
  en: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- kungfubot
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.12851v3.
sources:
- id: src_001
  type: paper
  title: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills (arXiv)'
  url: https://arxiv.org/abs/2506.12851
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots are promising to acquire various skills by imitating human behaviors. However, existing algorithms are only capable of tracking smooth, low-speed human motions, even with delicate reward and curriculum design. This paper presents a physics-based humanoid control framework, aiming to master highly-dynamic human behaviors such as Kungfu and dancing through multi-steps motion processing and adaptive motion tracking. For motion processing, we design a pipeline to extract, filter out, correct, and retarget motions, while ensuring compliance with physical constraints to the maximum extent. For motion imitation, we formulate a bi-level optimization problem to dynamically adjust the tracking accuracy tolerance based on the current tracking error, creating an adaptive curriculum mechanism. We further construct an asymmetric actor-critic framework for policy training. In experiments, we train whole-body control policies to imitate a set of highly-dynamic motions. Our method achieves significantly lower tracking errors than existing approaches and is successfully deployed on the Unitree G1 robot, demonstrating stable and expressive behaviors. The project page is https://kungfubot.github.io.

## 核心内容
Humanoid robots are promising to acquire various skills by imitating human behaviors. However, existing algorithms are only capable of tracking smooth, low-speed human motions, even with delicate reward and curriculum design. This paper presents a physics-based humanoid control framework, aiming to master highly-dynamic human behaviors such as Kungfu and dancing through multi-steps motion processing and adaptive motion tracking. For motion processing, we design a pipeline to extract, filter out, correct, and retarget motions, while ensuring compliance with physical constraints to the maximum extent. For motion imitation, we formulate a bi-level optimization problem to dynamically adjust the tracking accuracy tolerance based on the current tracking error, creating an adaptive curriculum mechanism. We further construct an asymmetric actor-critic framework for policy training. In experiments, we train whole-body control policies to imitate a set of highly-dynamic motions. Our method achieves significantly lower tracking errors than existing approaches and is successfully deployed on the Unitree G1 robot, demonstrating stable and expressive behaviors. The project page is https://kungfubot.github.io.

## 参考
- http://arxiv.org/abs/2506.12851v3

## Overview
Humanoid robots are promising to acquire various skills by imitating human behaviors. However, existing algorithms are only capable of tracking smooth, low-speed human motions, even with delicate reward and curriculum design. This paper presents a physics-based humanoid control framework, aiming to master highly-dynamic human behaviors such as Kungfu and dancing through multi-steps motion processing and adaptive motion tracking. For motion processing, we design a pipeline to extract, filter out, correct, and retarget motions, while ensuring compliance with physical constraints to the maximum extent. For motion imitation, we formulate a bi-level optimization problem to dynamically adjust the tracking accuracy tolerance based on the current tracking error, creating an adaptive curriculum mechanism. We further construct an asymmetric actor-critic framework for policy training. In experiments, we train whole-body control policies to imitate a set of highly-dynamic motions. Our method achieves significantly lower tracking errors than existing approaches and is successfully deployed on the Unitree G1 robot, demonstrating stable and expressive behaviors. The project page is https://kungfubot.github.io.

## Content
Humanoid robots are promising to acquire various skills by imitating human behaviors. However, existing algorithms are only capable of tracking smooth, low-speed human motions, even with delicate reward and curriculum design. This paper presents a physics-based humanoid control framework, aiming to master highly-dynamic human behaviors such as Kungfu and dancing through multi-steps motion processing and adaptive motion tracking. For motion processing, we design a pipeline to extract, filter out, correct, and retarget motions, while ensuring compliance with physical constraints to the maximum extent. For motion imitation, we formulate a bi-level optimization problem to dynamically adjust the tracking accuracy tolerance based on the current tracking error, creating an adaptive curriculum mechanism. We further construct an asymmetric actor-critic framework for policy training. In experiments, we train whole-body control policies to imitate a set of highly-dynamic motions. Our method achieves significantly lower tracking errors than existing approaches and is successfully deployed on the Unitree G1 robot, demonstrating stable and expressive behaviors. The project page is https://kungfubot.github.io.

## 개요
휴머노이드 로봇은 인간의 행동을 모방하여 다양한 기술을 습득할 수 있는 가능성을 지니고 있습니다. 그러나 기존 알고리즘은 정교한 보상 및 커리큘럼 설계에도 불구하고 부드럽고 저속인 인간 동작만을 추적할 수 있습니다. 본 논문은 물리 기반 휴머노이드 제어 프레임워크를 제시하며, 쿵푸와 춤과 같은 고역학적 인간 행동을 다단계 동작 처리 및 적응형 동작 추적을 통해 마스터하는 것을 목표로 합니다. 동작 처리를 위해, 물리적 제약 조건을 최대한 준수하면서 동작을 추출, 필터링, 보정 및 리타겟팅하는 파이프라인을 설계합니다. 동작 모방을 위해, 현재 추적 오류에 기반하여 추적 정확도 허용 오차를 동적으로 조정하는 이중 수준 최적화 문제를 공식화하여 적응형 커리큘럼 메커니즘을 생성합니다. 또한 정책 훈련을 위한 비대칭 행위자-비평가 프레임워크를 구축합니다. 실험에서, 우리는 고역학적 동작 세트를 모방하기 위해 전신 제어 정책을 훈련합니다. 우리의 방법은 기존 접근 방식보다 현저히 낮은 추적 오류를 달성하며, Unitree G1 로봇에 성공적으로 배포되어 안정적이고 표현력 있는 행동을 보여줍니다. 프로젝트 페이지는 https://kungfubot.github.io입니다.

## 핵심 내용
휴머노이드 로봇은 인간의 행동을 모방하여 다양한 기술을 습득할 수 있는 가능성을 지니고 있습니다. 그러나 기존 알고리즘은 정교한 보상 및 커리큘럼 설계에도 불구하고 부드럽고 저속인 인간 동작만을 추적할 수 있습니다. 본 논문은 물리 기반 휴머노이드 제어 프레임워크를 제시하며, 쿵푸와 춤과 같은 고역학적 인간 행동을 다단계 동작 처리 및 적응형 동작 추적을 통해 마스터하는 것을 목표로 합니다. 동작 처리를 위해, 물리적 제약 조건을 최대한 준수하면서 동작을 추출, 필터링, 보정 및 리타겟팅하는 파이프라인을 설계합니다. 동작 모방을 위해, 현재 추적 오류에 기반하여 추적 정확도 허용 오차를 동적으로 조정하는 이중 수준 최적화 문제를 공식화하여 적응형 커리큘럼 메커니즘을 생성합니다. 또한 정책 훈련을 위한 비대칭 행위자-비평가 프레임워크를 구축합니다. 실험에서, 우리는 고역학적 동작 세트를 모방하기 위해 전신 제어 정책을 훈련합니다. 우리의 방법은 기존 접근 방식보다 현저히 낮은 추적 오류를 달성하며, Unitree G1 로봇에 성공적으로 배포되어 안정적이고 표현력 있는 행동을 보여줍니다. 프로젝트 페이지는 https://kungfubot.github.io입니다.
