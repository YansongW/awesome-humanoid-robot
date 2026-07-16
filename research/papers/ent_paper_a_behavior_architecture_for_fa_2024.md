---
$id: ent_paper_a_behavior_architecture_for_fa_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Behavior Architecture for Fast Humanoid Robot Door Traversals
  zh: A Behavior Architecture for Fast Humanoid Robot Door Traversals
  ko: A Behavior Architecture for Fast Humanoid Robot Door Traversals
summary:
  en: A Behavior Architecture for Fast Humanoid Robot Door Traversals is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: A Behavior Architecture for Fast Humanoid Robot Door Traversals is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: A Behavior Architecture for Fast Humanoid Robot Door Traversals is a 2024 work on loco-manipulation and whole-body-control
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
- a_behavior_architecture_for_fa
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.03532v1.
sources:
- id: src_001
  type: paper
  title: A Behavior Architecture for Fast Humanoid Robot Door Traversals (arXiv)
  url: https://arxiv.org/abs/2411.03532
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: A Behavior Architecture for Fast Humanoid Robot Door Traversals project page
  url: https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Towards the role of humanoid robots as squad mates in urban operations and other domains, we identified doors as a major area lacking capability development. In this paper, we focus on the ability of humanoid robots to navigate and deal with doors. Human-sized doors are ubiquitous in many environment domains and the humanoid form factor is uniquely suited to operate and traverse them. We present an architecture which incorporates GPU accelerated perception and a tree based interactive behavior coordination system with a whole body motion and walking controller. Our system is capable of performing door traversals on a variety of door types. It supports rapid authoring of behaviors for unseen door types and techniques to achieve re-usability of those authored behaviors. The behaviors are modelled using trees and feature logical reactivity and action sequences that can be executed with layered concurrency to increase speed. Primitive actions are built on top of our existing whole body controller which supports manipulation while walking. We include a perception system using both neural networks and classical computer vision for door mechanism detection outside of the lab environment. We present operator-robot interdependence analysis charts to explore how human cognition is combined with artificial intelligence to produce complex robot behavior. Finally, we present and discuss real robot performances of fast door traversals on our Nadia humanoid robot. Videos online at https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy.

## 核心内容
Towards the role of humanoid robots as squad mates in urban operations and other domains, we identified doors as a major area lacking capability development. In this paper, we focus on the ability of humanoid robots to navigate and deal with doors. Human-sized doors are ubiquitous in many environment domains and the humanoid form factor is uniquely suited to operate and traverse them. We present an architecture which incorporates GPU accelerated perception and a tree based interactive behavior coordination system with a whole body motion and walking controller. Our system is capable of performing door traversals on a variety of door types. It supports rapid authoring of behaviors for unseen door types and techniques to achieve re-usability of those authored behaviors. The behaviors are modelled using trees and feature logical reactivity and action sequences that can be executed with layered concurrency to increase speed. Primitive actions are built on top of our existing whole body controller which supports manipulation while walking. We include a perception system using both neural networks and classical computer vision for door mechanism detection outside of the lab environment. We present operator-robot interdependence analysis charts to explore how human cognition is combined with artificial intelligence to produce complex robot behavior. Finally, we present and discuss real robot performances of fast door traversals on our Nadia humanoid robot. Videos online at https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy.

## 参考
- http://arxiv.org/abs/2411.03532v1

## Overview
Towards the role of humanoid robots as squad mates in urban operations and other domains, we identified doors as a major area lacking capability development. In this paper, we focus on the ability of humanoid robots to navigate and deal with doors. Human-sized doors are ubiquitous in many environment domains and the humanoid form factor is uniquely suited to operate and traverse them. We present an architecture which incorporates GPU accelerated perception and a tree based interactive behavior coordination system with a whole body motion and walking controller. Our system is capable of performing door traversals on a variety of door types. It supports rapid authoring of behaviors for unseen door types and techniques to achieve re-usability of those authored behaviors. The behaviors are modelled using trees and feature logical reactivity and action sequences that can be executed with layered concurrency to increase speed. Primitive actions are built on top of our existing whole body controller which supports manipulation while walking. We include a perception system using both neural networks and classical computer vision for door mechanism detection outside of the lab environment. We present operator-robot interdependence analysis charts to explore how human cognition is combined with artificial intelligence to produce complex robot behavior. Finally, we present and discuss real robot performances of fast door traversals on our Nadia humanoid robot. Videos online at https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy.

## Content
Towards the role of humanoid robots as squad mates in urban operations and other domains, we identified doors as a major area lacking capability development. In this paper, we focus on the ability of humanoid robots to navigate and deal with doors. Human-sized doors are ubiquitous in many environment domains and the humanoid form factor is uniquely suited to operate and traverse them. We present an architecture which incorporates GPU accelerated perception and a tree based interactive behavior coordination system with a whole body motion and walking controller. Our system is capable of performing door traversals on a variety of door types. It supports rapid authoring of behaviors for unseen door types and techniques to achieve re-usability of those authored behaviors. The behaviors are modelled using trees and feature logical reactivity and action sequences that can be executed with layered concurrency to increase speed. Primitive actions are built on top of our existing whole body controller which supports manipulation while walking. We include a perception system using both neural networks and classical computer vision for door mechanism detection outside of the lab environment. We present operator-robot interdependence analysis charts to explore how human cognition is combined with artificial intelligence to produce complex robot behavior. Finally, we present and discuss real robot performances of fast door traversals on our Nadia humanoid robot. Videos online at https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy.

## 개요
인간형 로봇이 도시 작전 및 기타 영역에서 분대원 역할을 수행하는 방향으로 나아가면서, 우리는 문이 능력 개발이 부족한 주요 영역임을 확인했습니다. 본 논문에서는 인간형 로봇이 문을 탐색하고 처리하는 능력에 초점을 맞춥니다. 인간 크기의 문은 다양한 환경 영역에서 흔히 존재하며, 인간형 폼팩터는 이를 작동하고 통과하는 데 독특하게 적합합니다. 우리는 GPU 가속 인식과 트리 기반의 상호작용적 행동 조정 시스템을 전신 동작 및 보행 제어기와 통합한 아키텍처를 제시합니다. 우리 시스템은 다양한 유형의 문을 통과할 수 있습니다. 또한, 보지 못한 문 유형에 대한 행동을 신속하게 작성하고, 작성된 행동의 재사용성을 달성하는 기술을 지원합니다. 행동은 트리를 사용하여 모델링되며, 계층적 동시성을 통해 실행 속도를 높일 수 있는 논리적 반응성과 동작 시퀀스를 특징으로 합니다. 기본 동작은 걷는 동안 조작을 지원하는 기존의 전신 제어기 위에 구축됩니다. 우리는 실험실 환경 밖에서 문 메커니즘을 감지하기 위해 신경망과 고전적 컴퓨터 비전을 모두 사용하는 인식 시스템을 포함합니다. 인간 인지와 인공지능이 결합되어 복잡한 로봇 행동을 생성하는 방식을 탐구하기 위해 운영자-로봇 상호의존성 분석 차트를 제시합니다. 마지막으로, Nadia 인간형 로봇에서의 빠른 문 통과에 대한 실제 로봇 성능을 제시하고 논의합니다. 동영상은 https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy 에서 온라인으로 확인할 수 있습니다.

## 핵심 내용
인간형 로봇이 도시 작전 및 기타 영역에서 분대원 역할을 수행하는 방향으로 나아가면서, 우리는 문이 능력 개발이 부족한 주요 영역임을 확인했습니다. 본 논문에서는 인간형 로봇이 문을 탐색하고 처리하는 능력에 초점을 맞춥니다. 인간 크기의 문은 다양한 환경 영역에서 흔히 존재하며, 인간형 폼팩터는 이를 작동하고 통과하는 데 독특하게 적합합니다. 우리는 GPU 가속 인식과 트리 기반의 상호작용적 행동 조정 시스템을 전신 동작 및 보행 제어기와 통합한 아키텍처를 제시합니다. 우리 시스템은 다양한 유형의 문을 통과할 수 있습니다. 또한, 보지 못한 문 유형에 대한 행동을 신속하게 작성하고, 작성된 행동의 재사용성을 달성하는 기술을 지원합니다. 행동은 트리를 사용하여 모델링되며, 계층적 동시성을 통해 실행 속도를 높일 수 있는 논리적 반응성과 동작 시퀀스를 특징으로 합니다. 기본 동작은 걷는 동안 조작을 지원하는 기존의 전신 제어기 위에 구축됩니다. 우리는 실험실 환경 밖에서 문 메커니즘을 감지하기 위해 신경망과 고전적 컴퓨터 비전을 모두 사용하는 인식 시스템을 포함합니다. 인간 인지와 인공지능이 결합되어 복잡한 로봇 행동을 생성하는 방식을 탐구하기 위해 운영자-로봇 상호의존성 분석 차트를 제시합니다. 마지막으로, Nadia 인간형 로봇에서의 빠른 문 통과에 대한 실제 로봇 성능을 제시하고 논의합니다. 동영상은 https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy 에서 온라인으로 확인할 수 있습니다.
