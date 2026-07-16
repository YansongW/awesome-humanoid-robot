---
$id: ent_paper_chung_rethinking_progression_of_memo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective'
  zh: Embodied-SlotSSM
  ko: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective'
summary:
  en: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (Embodied-SlotSSM), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by CMU, University of Arkansas.'
  zh: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (Embodied-SlotSSM), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by CMU, University of Arkansas.'
  ko: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (Embodied-SlotSSM), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by CMU, University of Arkansas.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodied_slotssm
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.11478v3.
sources:
- id: src_001
  type: paper
  title: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (arXiv)'
  url: https://arxiv.org/abs/2511.11478
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Embodied-SlotSSM source
  url: https://doi.org/10.48550/arXiv.2511.11478
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
As embodied agents operate in increasingly complex environments, the ability to perceive, track, and reason about individual object instances over time becomes essential, especially in tasks requiring sequenced interactions with visually similar objects. In these non-Markovian settings, key decision cues are often hidden in object-specific histories rather than the current scene. Without persistent memory of prior interactions (what has been interacted with, where it has been, or how it has changed) visuomotor policies may fail, repeat past actions, or overlook completed ones. To surface this challenge, we introduce LIBERO-Mem, a non-Markovian task suite for stress-testing robotic manipulation under object-level partial observability. It combines short- and long-horizon object tracking with temporally sequenced subgoals, requiring reasoning beyond the current frame. However, vision-language-action (VLA) models often struggle in such settings, with token scaling quickly becoming intractable even for tasks spanning just a few hundred frames. We propose Embodied-SlotSSM, a slot-centric VLA framework built for temporal scalability. It maintains spatio-temporally consistent slot identities and leverages them through two mechanisms: (1) slot-state-space modeling for reconstructing short-term history, and (2) a relational encoder to align the input tokens with action decoding. Together, these components enable temporally grounded, context-aware action prediction. Experiments show Embodied-SlotSSM's baseline performance on LIBERO-Mem and general tasks, offering a scalable solution for non-Markovian reasoning in object-centric robotic policies.

## 核心内容
As embodied agents operate in increasingly complex environments, the ability to perceive, track, and reason about individual object instances over time becomes essential, especially in tasks requiring sequenced interactions with visually similar objects. In these non-Markovian settings, key decision cues are often hidden in object-specific histories rather than the current scene. Without persistent memory of prior interactions (what has been interacted with, where it has been, or how it has changed) visuomotor policies may fail, repeat past actions, or overlook completed ones. To surface this challenge, we introduce LIBERO-Mem, a non-Markovian task suite for stress-testing robotic manipulation under object-level partial observability. It combines short- and long-horizon object tracking with temporally sequenced subgoals, requiring reasoning beyond the current frame. However, vision-language-action (VLA) models often struggle in such settings, with token scaling quickly becoming intractable even for tasks spanning just a few hundred frames. We propose Embodied-SlotSSM, a slot-centric VLA framework built for temporal scalability. It maintains spatio-temporally consistent slot identities and leverages them through two mechanisms: (1) slot-state-space modeling for reconstructing short-term history, and (2) a relational encoder to align the input tokens with action decoding. Together, these components enable temporally grounded, context-aware action prediction. Experiments show Embodied-SlotSSM's baseline performance on LIBERO-Mem and general tasks, offering a scalable solution for non-Markovian reasoning in object-centric robotic policies.

## 参考
- http://arxiv.org/abs/2511.11478v3

## Overview
As embodied agents operate in increasingly complex environments, the ability to perceive, track, and reason about individual object instances over time becomes essential, especially in tasks requiring sequenced interactions with visually similar objects. In these non-Markovian settings, key decision cues are often hidden in object-specific histories rather than the current scene. Without persistent memory of prior interactions (what has been interacted with, where it has been, or how it has changed) visuomotor policies may fail, repeat past actions, or overlook completed ones. To surface this challenge, we introduce LIBERO-Mem, a non-Markovian task suite for stress-testing robotic manipulation under object-level partial observability. It combines short- and long-horizon object tracking with temporally sequenced subgoals, requiring reasoning beyond the current frame. However, vision-language-action (VLA) models often struggle in such settings, with token scaling quickly becoming intractable even for tasks spanning just a few hundred frames. We propose Embodied-SlotSSM, a slot-centric VLA framework built for temporal scalability. It maintains spatio-temporally consistent slot identities and leverages them through two mechanisms: (1) slot-state-space modeling for reconstructing short-term history, and (2) a relational encoder to align the input tokens with action decoding. Together, these components enable temporally grounded, context-aware action prediction. Experiments show Embodied-SlotSSM's baseline performance on LIBERO-Mem and general tasks, offering a scalable solution for non-Markovian reasoning in object-centric robotic policies.

## Content
As embodied agents operate in increasingly complex environments, the ability to perceive, track, and reason about individual object instances over time becomes essential, especially in tasks requiring sequenced interactions with visually similar objects. In these non-Markovian settings, key decision cues are often hidden in object-specific histories rather than the current scene. Without persistent memory of prior interactions (what has been interacted with, where it has been, or how it has changed) visuomotor policies may fail, repeat past actions, or overlook completed ones. To surface this challenge, we introduce LIBERO-Mem, a non-Markovian task suite for stress-testing robotic manipulation under object-level partial observability. It combines short- and long-horizon object tracking with temporally sequenced subgoals, requiring reasoning beyond the current frame. However, vision-language-action (VLA) models often struggle in such settings, with token scaling quickly becoming intractable even for tasks spanning just a few hundred frames. We propose Embodied-SlotSSM, a slot-centric VLA framework built for temporal scalability. It maintains spatio-temporally consistent slot identities and leverages them through two mechanisms: (1) slot-state-space modeling for reconstructing short-term history, and (2) a relational encoder to align the input tokens with action decoding. Together, these components enable temporally grounded, context-aware action prediction. Experiments show Embodied-SlotSSM's baseline performance on LIBERO-Mem and general tasks, offering a scalable solution for non-Markovian reasoning in object-centric robotic policies.

## 개요
임베디드 에이전트가 점점 더 복잡한 환경에서 작동함에 따라, 시간이 지남에 따라 개별 객체 인스턴스를 인식, 추적 및 추론하는 능력이 필수적이 되고 있으며, 특히 시각적으로 유사한 객체와 순차적 상호작용이 필요한 작업에서 중요합니다. 이러한 비마르코프 환경에서는 주요 결정 단서가 현재 장면이 아닌 객체별 이력에 숨겨져 있는 경우가 많습니다. 이전 상호작용(무엇과 상호작용했는지, 어디에 있었는지, 어떻게 변화했는지)에 대한 지속적인 메모리가 없으면 시각운동 정책이 실패하거나, 이전 행동을 반복하거나, 완료된 행동을 간과할 수 있습니다. 이 문제를 부각시키기 위해, 우리는 객체 수준의 부분 관측 가능성 하에서 로봇 조작을 스트레스 테스트하는 비마르코프 작업 모음인 LIBERO-Mem을 소개합니다. 이는 단기 및 장기 객체 추적을 시간적으로 순차화된 하위 목표와 결합하여 현재 프레임을 넘어선 추론을 요구합니다. 그러나 시각-언어-행동(VLA) 모델은 이러한 환경에서 종종 어려움을 겪으며, 수백 프레임에 걸친 작업에서도 토큰 확장이 빠르게 다루기 어려워집니다. 우리는 시간적 확장성을 위해 설계된 슬롯 중심 VLA 프레임워크인 Embodied-SlotSSM을 제안합니다. 이는 시공간적으로 일관된 슬롯 정체성을 유지하고, 이를 두 가지 메커니즘을 통해 활용합니다: (1) 단기 이력을 재구성하기 위한 슬롯 상태 공간 모델링, (2) 입력 토큰을 행동 디코딩과 정렬하기 위한 관계형 인코더. 이러한 구성 요소는 함께 시간적으로 근거를 둔, 맥락 인식 행동 예측을 가능하게 합니다. 실험은 LIBERO-Mem 및 일반 작업에서 Embodied-SlotSSM의 기준 성능을 보여주며, 객체 중심 로봇 정책에서 비마르코프 추론을 위한 확장 가능한 솔루션을 제공합니다.

## 핵심 내용
임베디드 에이전트가 점점 더 복잡한 환경에서 작동함에 따라, 시간이 지남에 따라 개별 객체 인스턴스를 인식, 추적 및 추론하는 능력이 필수적이 되고 있으며, 특히 시각적으로 유사한 객체와 순차적 상호작용이 필요한 작업에서 중요합니다. 이러한 비마르코프 환경에서는 주요 결정 단서가 현재 장면이 아닌 객체별 이력에 숨겨져 있는 경우가 많습니다. 이전 상호작용(무엇과 상호작용했는지, 어디에 있었는지, 어떻게 변화했는지)에 대한 지속적인 메모리가 없으면 시각운동 정책이 실패하거나, 이전 행동을 반복하거나, 완료된 행동을 간과할 수 있습니다. 이 문제를 부각시키기 위해, 우리는 객체 수준의 부분 관측 가능성 하에서 로봇 조작을 스트레스 테스트하는 비마르코프 작업 모음인 LIBERO-Mem을 소개합니다. 이는 단기 및 장기 객체 추적을 시간적으로 순차화된 하위 목표와 결합하여 현재 프레임을 넘어선 추론을 요구합니다. 그러나 시각-언어-행동(VLA) 모델은 이러한 환경에서 종종 어려움을 겪으며, 수백 프레임에 걸친 작업에서도 토큰 확장이 빠르게 다루기 어려워집니다. 우리는 시간적 확장성을 위해 설계된 슬롯 중심 VLA 프레임워크인 Embodied-SlotSSM을 제안합니다. 이는 시공간적으로 일관된 슬롯 정체성을 유지하고, 이를 두 가지 메커니즘을 통해 활용합니다: (1) 단기 이력을 재구성하기 위한 슬롯 상태 공간 모델링, (2) 입력 토큰을 행동 디코딩과 정렬하기 위한 관계형 인코더. 이러한 구성 요소는 함께 시간적으로 근거를 둔, 맥락 인식 행동 예측을 가능하게 합니다. 실험은 LIBERO-Mem 및 일반 작업에서 Embodied-SlotSSM의 기준 성능을 보여주며, 객체 중심 로봇 정책에서 비마르코프 추론을 위한 확장 가능한 솔루션을 제공합니다.
