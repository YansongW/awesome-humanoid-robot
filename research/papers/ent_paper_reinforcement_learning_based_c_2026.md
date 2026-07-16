---
$id: ent_paper_reinforcement_learning_based_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
  zh: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
  ko: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
summary:
  en: 'arXiv:2606.31807v1 Announce Type: new Abstract: As humanoid robots become increasingly dynamic, coupling them with
    reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating.
    Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility
    of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we
    train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot
    modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots
    or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion
    strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation
    learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts
    by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a
    custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to
    a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers
    zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject
    active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can
    be found at https://www.youtube.com/watch?v=-_APcOS7uFo.'
  zh: 'arXiv:2606.31807v1 Announce Type: new Abstract: As humanoid robots become increasingly dynamic, coupling them with
    reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating.
    Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility
    of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we
    train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot
    modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots
    or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion
    strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation
    learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts
    by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a
    custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to
    a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers
    zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject
    active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can
    be found at https://www.youtube.com/watch?v=-_APcOS7uFo.'
  ko: 'arXiv:2606.31807v1 Announce Type: new Abstract: As humanoid robots become increasingly dynamic, coupling them with
    reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating.
    Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility
    of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we
    train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot
    modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots
    or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion
    strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation
    learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts
    by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a
    custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to
    a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers
    zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject
    active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can
    be found at https://www.youtube.com/watch?v=-_APcOS7uFo.'
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
- reinforcement_learning_based_c
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31807v1.
sources:
- id: src_001
  type: paper
  title: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
  url: https://arxiv.org/abs/2606.31807
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
As humanoid robots become increasingly dynamic, coupling them with reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo.

## 核心内容
As humanoid robots become increasingly dynamic, coupling them with reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo.

## 参考
- http://arxiv.org/abs/2606.31807v1

## Overview
As humanoid robots become increasingly dynamic, coupling them with reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo.

## Content
As humanoid robots become increasingly dynamic, coupling them with reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo.

## 개요
휴머노이드 로봇이 점점 더 동적으로 발전함에 따라, 이를 강화 학습과 결합하는 것은 수동 인라인 스케이팅의 복잡하고 저구동된 역학을 해결하는 유망한 접근법을 제공합니다. 휴머노이드 로봇에 수동 인라인 스케이팅 바퀴를 장착하면 휴머노이드의 다재다능한 민첩성과 인간 스케이터가 사용하는 고속, 에너지 효율적인 이동 전략을 결합할 수 있는 기회가 생깁니다. 본 논문에서는 기존 발 대신 소비자용 인라인 스케이트를 장착하도록 개조된 휴머노이드 로봇을 위해 새로운 이동 전략을 가능하게 하는 강화 학습 제어 정책을 훈련하고 배포합니다. 사족 로봇이나 능동 구동 바퀴에 국한된 이전 연구와 달리, 우리 시스템은 스케이트의 정밀한 6자유도 제어를 통해 동적이고 에지 기반의 추진 전략을 실행할 수 있습니다. 우리의 스케이팅 전략은 인간 동작 데이터, 모방 학습 또는 운동학적 사전 지식에 의존하지 않고 보상 구조에서 완전히 창발합니다. 우리는 훈련 및 검증 중에 다양한 기하학적 바퀴 모델(구형 및 타원체)과 맞춤형 성공 기반 명령 커리큘럼 및 특수 구름 보상을 활용하여 수동 바퀴의 본질적인 불안정성과 시뮬레이션 접촉 인공물을 극복합니다. 결과적으로, 우리의 정책은 표준 보행 걸음걸이에 비해 최대 50%의 수송 비용(CoT) 감소를 보여줍니다. 결과 정책은 물리적 Booster T1 하드웨어에 제로샷으로 성공적으로 전이됩니다. 실제 배포에서는 동적 균형, 능동적 물리적 교란을 거부하는 능력, 속도에서 회전이 가능한 민첩한 이동 전략을 입증합니다. 결과 비디오는 https://www.youtube.com/watch?v=-_APcOS7uFo에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇이 점점 더 동적으로 발전함에 따라, 이를 강화 학습과 결합하는 것은 수동 인라인 스케이팅의 복잡하고 저구동된 역학을 해결하는 유망한 접근법을 제공합니다. 휴머노이드 로봇에 수동 인라인 스케이팅 바퀴를 장착하면 휴머노이드의 다재다능한 민첩성과 인간 스케이터가 사용하는 고속, 에너지 효율적인 이동 전략을 결합할 수 있는 기회가 생깁니다. 본 논문에서는 기존 발 대신 소비자용 인라인 스케이트를 장착하도록 개조된 휴머노이드 로봇을 위해 새로운 이동 전략을 가능하게 하는 강화 학습 제어 정책을 훈련하고 배포합니다. 사족 로봇이나 능동 구동 바퀴에 국한된 이전 연구와 달리, 우리 시스템은 스케이트의 정밀한 6자유도 제어를 통해 동적이고 에지 기반의 추진 전략을 실행할 수 있습니다. 우리의 스케이팅 전략은 인간 동작 데이터, 모방 학습 또는 운동학적 사전 지식에 의존하지 않고 보상 구조에서 완전히 창발합니다. 우리는 훈련 및 검증 중에 다양한 기하학적 바퀴 모델(구형 및 타원체)과 맞춤형 성공 기반 명령 커리큘럼 및 특수 구름 보상을 활용하여 수동 바퀴의 본질적인 불안정성과 시뮬레이션 접촉 인공물을 극복합니다. 결과적으로, 우리의 정책은 표준 보행 걸음걸이에 비해 최대 50%의 수송 비용(CoT) 감소를 보여줍니다. 결과 정책은 물리적 Booster T1 하드웨어에 제로샷으로 성공적으로 전이됩니다. 실제 배포에서는 동적 균형, 능동적 물리적 교란을 거부하는 능력, 속도에서 회전이 가능한 민첩한 이동 전략을 입증합니다. 결과 비디오는 https://www.youtube.com/watch?v=-_APcOS7uFo에서 확인할 수 있습니다.
