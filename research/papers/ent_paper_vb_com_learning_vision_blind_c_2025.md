---
$id: ent_paper_vb_com_learning_vision_blind_c_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception'
  zh: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception'
  ko: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception'
summary:
  en: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception is a 2025 work on locomotion
    for humanoid robots.'
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
- vb_com
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.14814v2.
sources:
- id: src_001
  type: paper
  title: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception (arXiv)'
  url: https://arxiv.org/abs/2502.14814
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'VB-Com: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception project page'
  url: https://renjunli99.github.io/vbcom.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The performance of legged locomotion is closely tied to the accuracy and comprehensiveness of state observations. Blind policies, which rely solely on proprioception, are considered highly robust due to the reliability of proprioceptive observations. However, these policies significantly limit locomotion speed and often require collisions with the terrain to adapt. In contrast, Vision policies allows the robot to plan motions in advance and respond proactively to unstructured terrains with an online perception module. However, perception is often compromised by noisy real-world environments, potential sensor failures, and the limitations of current simulations in presenting dynamic or deformable terrains. Humanoid robots, with high degrees of freedom and inherently unstable morphology, are particularly susceptible to misguidance from deficient perception, which can result in falls or termination on challenging dynamic terrains. To leverage the advantages of both vision and blind policies, we propose VB-Com, a composite framework that enables humanoid robots to determine when to rely on the vision policy and when to switch to the blind policy under perceptual deficiency. We demonstrate that VB-Com effectively enables humanoid robots to traverse challenging terrains and obstacles despite perception deficiencies caused by dynamic terrains or perceptual noise.

## 核心内容
The performance of legged locomotion is closely tied to the accuracy and comprehensiveness of state observations. Blind policies, which rely solely on proprioception, are considered highly robust due to the reliability of proprioceptive observations. However, these policies significantly limit locomotion speed and often require collisions with the terrain to adapt. In contrast, Vision policies allows the robot to plan motions in advance and respond proactively to unstructured terrains with an online perception module. However, perception is often compromised by noisy real-world environments, potential sensor failures, and the limitations of current simulations in presenting dynamic or deformable terrains. Humanoid robots, with high degrees of freedom and inherently unstable morphology, are particularly susceptible to misguidance from deficient perception, which can result in falls or termination on challenging dynamic terrains. To leverage the advantages of both vision and blind policies, we propose VB-Com, a composite framework that enables humanoid robots to determine when to rely on the vision policy and when to switch to the blind policy under perceptual deficiency. We demonstrate that VB-Com effectively enables humanoid robots to traverse challenging terrains and obstacles despite perception deficiencies caused by dynamic terrains or perceptual noise.

## 参考
- http://arxiv.org/abs/2502.14814v2

## Overview
The performance of legged locomotion is closely tied to the accuracy and comprehensiveness of state observations. Blind policies, which rely solely on proprioception, are considered highly robust due to the reliability of proprioceptive observations. However, these policies significantly limit locomotion speed and often require collisions with the terrain to adapt. In contrast, Vision policies allows the robot to plan motions in advance and respond proactively to unstructured terrains with an online perception module. However, perception is often compromised by noisy real-world environments, potential sensor failures, and the limitations of current simulations in presenting dynamic or deformable terrains. Humanoid robots, with high degrees of freedom and inherently unstable morphology, are particularly susceptible to misguidance from deficient perception, which can result in falls or termination on challenging dynamic terrains. To leverage the advantages of both vision and blind policies, we propose VB-Com, a composite framework that enables humanoid robots to determine when to rely on the vision policy and when to switch to the blind policy under perceptual deficiency. We demonstrate that VB-Com effectively enables humanoid robots to traverse challenging terrains and obstacles despite perception deficiencies caused by dynamic terrains or perceptual noise.

## Content
The performance of legged locomotion is closely tied to the accuracy and comprehensiveness of state observations. Blind policies, which rely solely on proprioception, are considered highly robust due to the reliability of proprioceptive observations. However, these policies significantly limit locomotion speed and often require collisions with the terrain to adapt. In contrast, Vision policies allows the robot to plan motions in advance and respond proactively to unstructured terrains with an online perception module. However, perception is often compromised by noisy real-world environments, potential sensor failures, and the limitations of current simulations in presenting dynamic or deformable terrains. Humanoid robots, with high degrees of freedom and inherently unstable morphology, are particularly susceptible to misguidance from deficient perception, which can result in falls or termination on challenging dynamic terrains. To leverage the advantages of both vision and blind policies, we propose VB-Com, a composite framework that enables humanoid robots to determine when to rely on the vision policy and when to switch to the blind policy under perceptual deficiency. We demonstrate that VB-Com effectively enables humanoid robots to traverse challenging terrains and obstacles despite perception deficiencies caused by dynamic terrains or perceptual noise.

## 개요
보행 이동의 성능은 상태 관측의 정확성과 포괄성에 밀접하게 연관됩니다. 고유 수용 감각(proprioception)에만 의존하는 블라인드 정책(Blind policies)은 고유 수용 관측의 신뢰성 덕분에 매우 강건한 것으로 간주됩니다. 그러나 이러한 정책은 이동 속도를 크게 제한하며, 종종 지형에 적응하기 위해 충돌이 필요합니다. 반면, 비전 정책(Vision policies)은 로봇이 사전에 동작을 계획하고 온라인 인식 모듈을 통해 비정형 지형에 능동적으로 대응할 수 있게 합니다. 그러나 인식은 잡음이 많은 실제 환경, 잠재적인 센서 고장, 그리고 동적 또는 변형 가능한 지형을 표현하는 현재 시뮬레이션의 한계로 인해 종종 손상됩니다. 높은 자유도와 본질적으로 불안정한 형태를 가진 휴머노이드 로봇은 결함 있는 인식으로 인한 잘못된 안내에 특히 취약하며, 이는 도전적인 동적 지형에서 넘어지거나 종료로 이어질 수 있습니다. 비전 정책과 블라인드 정책의 장점을 활용하기 위해, 우리는 VB-Com을 제안합니다. 이는 휴머노이드 로봇이 인식 결함 상황에서 언제 비전 정책에 의존하고 언제 블라인드 정책으로 전환할지 결정할 수 있게 하는 복합 프레임워크입니다. 우리는 VB-Com이 동적 지형이나 인식 잡음으로 인한 인식 결함에도 불구하고 휴머노이드 로봇이 도전적인 지형과 장애물을 효과적으로 통과할 수 있게 함을 입증합니다.

## 핵심 내용
보행 이동의 성능은 상태 관측의 정확성과 포괄성에 밀접하게 연관됩니다. 고유 수용 감각에만 의존하는 블라인드 정책은 고유 수용 관측의 신뢰성 덕분에 매우 강건한 것으로 간주됩니다. 그러나 이러한 정책은 이동 속도를 크게 제한하며, 종종 지형에 적응하기 위해 충돌이 필요합니다. 반면, 비전 정책은 로봇이 사전에 동작을 계획하고 온라인 인식 모듈을 통해 비정형 지형에 능동적으로 대응할 수 있게 합니다. 그러나 인식은 잡음이 많은 실제 환경, 잠재적인 센서 고장, 그리고 동적 또는 변형 가능한 지형을 표현하는 현재 시뮬레이션의 한계로 인해 종종 손상됩니다. 높은 자유도와 본질적으로 불안정한 형태를 가진 휴머노이드 로봇은 결함 있는 인식으로 인한 잘못된 안내에 특히 취약하며, 이는 도전적인 동적 지형에서 넘어지거나 종료로 이어질 수 있습니다. 비전 정책과 블라인드 정책의 장점을 활용하기 위해, 우리는 VB-Com을 제안합니다. 이는 휴머노이드 로봇이 인식 결함 상황에서 언제 비전 정책에 의존하고 언제 블라인드 정책으로 전환할지 결정할 수 있게 하는 복합 프레임워크입니다. 우리는 VB-Com이 동적 지형이나 인식 잡음으로 인한 인식 결함에도 불구하고 휴머노이드 로봇이 도전적인 지형과 장애물을 효과적으로 통과할 수 있게 함을 입증합니다.
