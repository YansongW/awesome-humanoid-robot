---
$id: ent_paper_reinforcement_learning_for_ver_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control
  zh: Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control
  ko: Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control
summary:
  en: Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control is a 2024 work on locomotion for
    humanoid robots.
  zh: Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control is a 2024 work on locomotion for
    humanoid robots.
  ko: Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control is a 2024 work on locomotion for
    humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- reinforcement_learning_for_ver
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.16889v2.
sources:
- id: src_001
  type: paper
  title: Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control (arXiv)
  url: https://arxiv.org/abs/2401.16889
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents a comprehensive study on using deep reinforcement learning (RL) to create dynamic locomotion controllers for bipedal robots. Going beyond focusing on a single locomotion skill, we develop a general control solution that can be used for a range of dynamic bipedal skills, from periodic walking and running to aperiodic jumping and standing. Our RL-based controller incorporates a novel dual-history architecture, utilizing both a long-term and short-term input/output (I/O) history of the robot. This control architecture, when trained through the proposed end-to-end RL approach, consistently outperforms other methods across a diverse range of skills in both simulation and the real world. The study also delves into the adaptivity and robustness introduced by the proposed RL system in developing locomotion controllers. We demonstrate that the proposed architecture can adapt to both time-invariant dynamics shifts and time-variant changes, such as contact events, by effectively using the robot's I/O history. Additionally, we identify task randomization as another key source of robustness, fostering better task generalization and compliance to disturbances. The resulting control policies can be successfully deployed on Cassie, a torque-controlled human-sized bipedal robot. This work pushes the limits of agility for bipedal robots through extensive real-world experiments. We demonstrate a diverse range of locomotion skills, including: robust standing, versatile walking, fast running with a demonstration of a 400-meter dash, and a diverse set of jumping skills, such as standing long jumps and high jumps.

## 核心内容
This paper presents a comprehensive study on using deep reinforcement learning (RL) to create dynamic locomotion controllers for bipedal robots. Going beyond focusing on a single locomotion skill, we develop a general control solution that can be used for a range of dynamic bipedal skills, from periodic walking and running to aperiodic jumping and standing. Our RL-based controller incorporates a novel dual-history architecture, utilizing both a long-term and short-term input/output (I/O) history of the robot. This control architecture, when trained through the proposed end-to-end RL approach, consistently outperforms other methods across a diverse range of skills in both simulation and the real world. The study also delves into the adaptivity and robustness introduced by the proposed RL system in developing locomotion controllers. We demonstrate that the proposed architecture can adapt to both time-invariant dynamics shifts and time-variant changes, such as contact events, by effectively using the robot's I/O history. Additionally, we identify task randomization as another key source of robustness, fostering better task generalization and compliance to disturbances. The resulting control policies can be successfully deployed on Cassie, a torque-controlled human-sized bipedal robot. This work pushes the limits of agility for bipedal robots through extensive real-world experiments. We demonstrate a diverse range of locomotion skills, including: robust standing, versatile walking, fast running with a demonstration of a 400-meter dash, and a diverse set of jumping skills, such as standing long jumps and high jumps.

## 参考
- http://arxiv.org/abs/2401.16889v2

## Overview
This paper presents a comprehensive study on using deep reinforcement learning (RL) to create dynamic locomotion controllers for bipedal robots. Going beyond focusing on a single locomotion skill, we develop a general control solution that can be used for a range of dynamic bipedal skills, from periodic walking and running to aperiodic jumping and standing. Our RL-based controller incorporates a novel dual-history architecture, utilizing both a long-term and short-term input/output (I/O) history of the robot. This control architecture, when trained through the proposed end-to-end RL approach, consistently outperforms other methods across a diverse range of skills in both simulation and the real world. The study also delves into the adaptivity and robustness introduced by the proposed RL system in developing locomotion controllers. We demonstrate that the proposed architecture can adapt to both time-invariant dynamics shifts and time-variant changes, such as contact events, by effectively using the robot's I/O history. Additionally, we identify task randomization as another key source of robustness, fostering better task generalization and compliance to disturbances. The resulting control policies can be successfully deployed on Cassie, a torque-controlled human-sized bipedal robot. This work pushes the limits of agility for bipedal robots through extensive real-world experiments. We demonstrate a diverse range of locomotion skills, including: robust standing, versatile walking, fast running with a demonstration of a 400-meter dash, and a diverse set of jumping skills, such as standing long jumps and high jumps.

## Content
This paper presents a comprehensive study on using deep reinforcement learning (RL) to create dynamic locomotion controllers for bipedal robots. Going beyond focusing on a single locomotion skill, we develop a general control solution that can be used for a range of dynamic bipedal skills, from periodic walking and running to aperiodic jumping and standing. Our RL-based controller incorporates a novel dual-history architecture, utilizing both a long-term and short-term input/output (I/O) history of the robot. This control architecture, when trained through the proposed end-to-end RL approach, consistently outperforms other methods across a diverse range of skills in both simulation and the real world. The study also delves into the adaptivity and robustness introduced by the proposed RL system in developing locomotion controllers. We demonstrate that the proposed architecture can adapt to both time-invariant dynamics shifts and time-variant changes, such as contact events, by effectively using the robot's I/O history. Additionally, we identify task randomization as another key source of robustness, fostering better task generalization and compliance to disturbances. The resulting control policies can be successfully deployed on Cassie, a torque-controlled human-sized bipedal robot. This work pushes the limits of agility for bipedal robots through extensive real-world experiments. We demonstrate a diverse range of locomotion skills, including: robust standing, versatile walking, fast running with a demonstration of a 400-meter dash, and a diverse set of jumping skills, such as standing long jumps and high jumps.

## 개요
본 논문은 이족 보행 로봇의 동적 보행 제어기를 생성하기 위해 심층 강화 학습(RL)을 사용하는 포괄적인 연구를 제시합니다. 단일 보행 기술에 초점을 맞추는 것을 넘어, 주기적인 걷기와 달리기부터 비주기적인 점프와 서기까지 다양한 동적 이족 보행 기술에 사용할 수 있는 일반 제어 솔루션을 개발합니다. RL 기반 제어기는 로봇의 장기 및 단기 입출력(I/O) 이력을 모두 활용하는 새로운 이중 이력 아키텍처를 통합합니다. 제안된 종단 간 RL 접근법을 통해 훈련된 이 제어 아키텍처는 시뮬레이션과 실제 환경 모두에서 다양한 기술에 걸쳐 다른 방법보다 일관되게 우수한 성능을 보입니다. 또한 본 연구는 보행 제어기 개발에서 제안된 RL 시스템이 도입하는 적응성과 견고성을 탐구합니다. 제안된 아키텍처는 로봇의 I/O 이력을 효과적으로 사용하여 시간 불변 동적 변화와 접촉 이벤트와 같은 시간 가변 변화 모두에 적응할 수 있음을 입증합니다. 추가적으로, 작업 무작위화를 견고성의 또 다른 핵심 원천으로 식별하여 더 나은 작업 일반화와 외란에 대한 순응을 촉진합니다. 결과 제어 정책은 토크 제어 인간 크기 이족 보행 로봇인 Cassie에 성공적으로 배포될 수 있습니다. 이 연구는 광범위한 실제 실험을 통해 이족 보행 로봇의 민첩성 한계를 확장합니다. 견고한 서기, 다용도 걷기, 400미터 달리기 시연을 포함한 빠른 달리기, 그리고 제자리 멀리뛰기와 높이뛰기와 같은 다양한 점프 기술을 포함한 다양한 보행 기술을 시연합니다.

## 핵심 내용
본 논문은 이족 보행 로봇의 동적 보행 제어기를 생성하기 위해 심층 강화 학습(RL)을 사용하는 포괄적인 연구를 제시합니다. 단일 보행 기술에 초점을 맞추는 것을 넘어, 주기적인 걷기와 달리기부터 비주기적인 점프와 서기까지 다양한 동적 이족 보행 기술에 사용할 수 있는 일반 제어 솔루션을 개발합니다. RL 기반 제어기는 로봇의 장기 및 단기 입출력(I/O) 이력을 모두 활용하는 새로운 이중 이력 아키텍처를 통합합니다. 제안된 종단 간 RL 접근법을 통해 훈련된 이 제어 아키텍처는 시뮬레이션과 실제 환경 모두에서 다양한 기술에 걸쳐 다른 방법보다 일관되게 우수한 성능을 보입니다. 또한 본 연구는 보행 제어기 개발에서 제안된 RL 시스템이 도입하는 적응성과 견고성을 탐구합니다. 제안된 아키텍처는 로봇의 I/O 이력을 효과적으로 사용하여 시간 불변 동적 변화와 접촉 이벤트와 같은 시간 가변 변화 모두에 적응할 수 있음을 입증합니다. 추가적으로, 작업 무작위화를 견고성의 또 다른 핵심 원천으로 식별하여 더 나은 작업 일반화와 외란에 대한 순응을 촉진합니다. 결과 제어 정책은 토크 제어 인간 크기 이족 보행 로봇인 Cassie에 성공적으로 배포될 수 있습니다. 이 연구는 광범위한 실제 실험을 통해 이족 보행 로봇의 민첩성 한계를 확장합니다. 견고한 서기, 다용도 걷기, 400미터 달리기 시연을 포함한 빠른 달리기, 그리고 제자리 멀리뛰기와 높이뛰기와 같은 다양한 점프 기술을 포함한 다양한 보행 기술을 시연합니다.
