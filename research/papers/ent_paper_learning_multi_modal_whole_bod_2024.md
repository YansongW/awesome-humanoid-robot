---
$id: ent_paper_learning_multi_modal_whole_bod_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots
  zh: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots
  ko: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots
summary:
  en: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
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
- learning_multi_modal_whole_bod
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.07295v4.
sources:
- id: src_001
  type: paper
  title: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2408.07295
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots project page
  url: https://masked-humanoid.github.io/mhc/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
A major challenge in humanoid robotics is designing a unified interface for commanding diverse whole-body behaviors, from precise footstep sequences to partial-body mimicry and joystick teleoperation. We introduce the Masked Humanoid Controller (MHC), a learned whole-body controller that exposes a simple yet expressive interface: the specification of masked target trajectories over selected subsets of the robot's state variables. This unified abstraction allows high-level systems to issue commands in a flexible format that accommodates multi-modal inputs such as optimized trajectories, motion capture clips, re-targeted video, and real-time joystick signals. The MHC is trained in simulation using a curriculum that spans this full range of modalities, enabling robust execution of partially specified behaviors while maintaining balance and disturbance rejection. We demonstrate the MHC both in simulation and on the real-world Digit V3 humanoid, showing that a single learned controller is capable of executing such diverse whole-body commands in the real world through a common representational interface.

## 核心内容
A major challenge in humanoid robotics is designing a unified interface for commanding diverse whole-body behaviors, from precise footstep sequences to partial-body mimicry and joystick teleoperation. We introduce the Masked Humanoid Controller (MHC), a learned whole-body controller that exposes a simple yet expressive interface: the specification of masked target trajectories over selected subsets of the robot's state variables. This unified abstraction allows high-level systems to issue commands in a flexible format that accommodates multi-modal inputs such as optimized trajectories, motion capture clips, re-targeted video, and real-time joystick signals. The MHC is trained in simulation using a curriculum that spans this full range of modalities, enabling robust execution of partially specified behaviors while maintaining balance and disturbance rejection. We demonstrate the MHC both in simulation and on the real-world Digit V3 humanoid, showing that a single learned controller is capable of executing such diverse whole-body commands in the real world through a common representational interface.

## 参考
- http://arxiv.org/abs/2408.07295v4

## Overview
A major challenge in humanoid robotics is designing a unified interface for commanding diverse whole-body behaviors, from precise footstep sequences to partial-body mimicry and joystick teleoperation. We introduce the Masked Humanoid Controller (MHC), a learned whole-body controller that exposes a simple yet expressive interface: the specification of masked target trajectories over selected subsets of the robot's state variables. This unified abstraction allows high-level systems to issue commands in a flexible format that accommodates multi-modal inputs such as optimized trajectories, motion capture clips, re-targeted video, and real-time joystick signals. The MHC is trained in simulation using a curriculum that spans this full range of modalities, enabling robust execution of partially specified behaviors while maintaining balance and disturbance rejection. We demonstrate the MHC both in simulation and on the real-world Digit V3 humanoid, showing that a single learned controller is capable of executing such diverse whole-body commands in the real world through a common representational interface.

## Content
A major challenge in humanoid robotics is designing a unified interface for commanding diverse whole-body behaviors, from precise footstep sequences to partial-body mimicry and joystick teleoperation. We introduce the Masked Humanoid Controller (MHC), a learned whole-body controller that exposes a simple yet expressive interface: the specification of masked target trajectories over selected subsets of the robot's state variables. This unified abstraction allows high-level systems to issue commands in a flexible format that accommodates multi-modal inputs such as optimized trajectories, motion capture clips, re-targeted video, and real-time joystick signals. The MHC is trained in simulation using a curriculum that spans this full range of modalities, enabling robust execution of partially specified behaviors while maintaining balance and disturbance rejection. We demonstrate the MHC both in simulation and on the real-world Digit V3 humanoid, showing that a single learned controller is capable of executing such diverse whole-body commands in the real world through a common representational interface.

## 개요
휴머노이드 로보틱스의 주요 과제는 정밀한 보폭 시퀀스부터 부분 신체 모방 및 조이스틱 원격 조작에 이르기까지 다양한 전신 동작을 명령하기 위한 통합 인터페이스를 설계하는 것입니다. 우리는 마스크드 휴머노이드 컨트롤러(MHC)를 소개합니다. 이는 학습 기반 전신 컨트롤러로, 로봇 상태 변수의 선택된 하위 집합에 대한 마스킹된 목표 궤적을 지정하는 간단하면서도 표현력 있는 인터페이스를 제공합니다. 이 통합 추상화는 고수준 시스템이 최적화된 궤적, 모션 캡처 클립, 재타겟팅된 비디오, 실시간 조이스틱 신호와 같은 다중 모드 입력을 수용하는 유연한 형식으로 명령을 내릴 수 있게 합니다. MHC는 이러한 모든 모드 범위를 포괄하는 커리큘럼을 사용하여 시뮬레이션에서 훈련되며, 균형 유지 및 외란 제거를 유지하면서 부분적으로 지정된 동작을 강건하게 실행할 수 있습니다. 우리는 시뮬레이션과 실제 Digit V3 휴머노이드에서 MHC를 시연하여, 단일 학습 컨트롤러가 공통 표현 인터페이스를 통해 실제 세계에서 이러한 다양한 전신 명령을 실행할 수 있음을 보여줍니다.

## 핵심 내용
휴머노이드 로보틱스의 주요 과제는 정밀한 보폭 시퀀스부터 부분 신체 모방 및 조이스틱 원격 조작에 이르기까지 다양한 전신 동작을 명령하기 위한 통합 인터페이스를 설계하는 것입니다. 우리는 마스크드 휴머노이드 컨트롤러(MHC)를 소개합니다. 이는 학습 기반 전신 컨트롤러로, 로봇 상태 변수의 선택된 하위 집합에 대한 마스킹된 목표 궤적을 지정하는 간단하면서도 표현력 있는 인터페이스를 제공합니다. 이 통합 추상화는 고수준 시스템이 최적화된 궤적, 모션 캡처 클립, 재타겟팅된 비디오, 실시간 조이스틱 신호와 같은 다중 모드 입력을 수용하는 유연한 형식으로 명령을 내릴 수 있게 합니다. MHC는 이러한 모든 모드 범위를 포괄하는 커리큘럼을 사용하여 시뮬레이션에서 훈련되며, 균형 유지 및 외란 제거를 유지하면서 부분적으로 지정된 동작을 강건하게 실행할 수 있습니다. 우리는 시뮬레이션과 실제 Digit V3 휴머노이드에서 MHC를 시연하여, 단일 학습 컨트롤러가 공통 표현 인터페이스를 통해 실제 세계에서 이러한 다양한 전신 명령을 실행할 수 있음을 보여줍니다.
