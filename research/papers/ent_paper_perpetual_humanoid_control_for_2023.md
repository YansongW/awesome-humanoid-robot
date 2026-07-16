---
$id: ent_paper_perpetual_humanoid_control_for_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Perpetual Humanoid Control for Real-time Simulated Avatars
  zh: Perpetual Humanoid Control for Real-time Simulated Avatars
  ko: Perpetual Humanoid Control for Real-time Simulated Avatars
summary:
  en: Perpetual Humanoid Control for Real-time Simulated Avatars is a 2023 work on physics-based character animation for humanoid
    robots, with open-source code available.
  zh: Perpetual Humanoid Control for Real-time Simulated Avatars is a 2023 work on physics-based character animation for humanoid
    robots, with open-source code available.
  ko: Perpetual Humanoid Control for Real-time Simulated Avatars is a 2023 work on physics-based character animation for humanoid
    robots, with open-source code available.
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
- perpetual_humanoid_control_for
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2305.06456v3.
sources:
- id: src_001
  type: paper
  title: Perpetual Humanoid Control for Real-time Simulated Avatars (arXiv)
  url: https://arxiv.org/abs/2305.06456
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We present a physics-based humanoid controller that achieves high-fidelity motion imitation and fault-tolerant behavior in the presence of noisy input (e.g. pose estimates from video or generated from language) and unexpected falls. Our controller scales up to learning ten thousand motion clips without using any external stabilizing forces and learns to naturally recover from fail-state. Given reference motion, our controller can perpetually control simulated avatars without requiring resets. At its core, we propose the progressive multiplicative control policy (PMCP), which dynamically allocates new network capacity to learn harder and harder motion sequences. PMCP allows efficient scaling for learning from large-scale motion databases and adding new tasks, such as fail-state recovery, without catastrophic forgetting. We demonstrate the effectiveness of our controller by using it to imitate noisy poses from video-based pose estimators and language-based motion generators in a live and real-time multi-person avatar use case.

## 核心内容
We present a physics-based humanoid controller that achieves high-fidelity motion imitation and fault-tolerant behavior in the presence of noisy input (e.g. pose estimates from video or generated from language) and unexpected falls. Our controller scales up to learning ten thousand motion clips without using any external stabilizing forces and learns to naturally recover from fail-state. Given reference motion, our controller can perpetually control simulated avatars without requiring resets. At its core, we propose the progressive multiplicative control policy (PMCP), which dynamically allocates new network capacity to learn harder and harder motion sequences. PMCP allows efficient scaling for learning from large-scale motion databases and adding new tasks, such as fail-state recovery, without catastrophic forgetting. We demonstrate the effectiveness of our controller by using it to imitate noisy poses from video-based pose estimators and language-based motion generators in a live and real-time multi-person avatar use case.

## 参考
- http://arxiv.org/abs/2305.06456v3

## Overview
We present a physics-based humanoid controller that achieves high-fidelity motion imitation and fault-tolerant behavior in the presence of noisy input (e.g. pose estimates from video or generated from language) and unexpected falls. Our controller scales up to learning ten thousand motion clips without using any external stabilizing forces and learns to naturally recover from fail-state. Given reference motion, our controller can perpetually control simulated avatars without requiring resets. At its core, we propose the progressive multiplicative control policy (PMCP), which dynamically allocates new network capacity to learn harder and harder motion sequences. PMCP allows efficient scaling for learning from large-scale motion databases and adding new tasks, such as fail-state recovery, without catastrophic forgetting. We demonstrate the effectiveness of our controller by using it to imitate noisy poses from video-based pose estimators and language-based motion generators in a live and real-time multi-person avatar use case.

## Content
We present a physics-based humanoid controller that achieves high-fidelity motion imitation and fault-tolerant behavior in the presence of noisy input (e.g. pose estimates from video or generated from language) and unexpected falls. Our controller scales up to learning ten thousand motion clips without using any external stabilizing forces and learns to naturally recover from fail-state. Given reference motion, our controller can perpetually control simulated avatars without requiring resets. At its core, we propose the progressive multiplicative control policy (PMCP), which dynamically allocates new network capacity to learn harder and harder motion sequences. PMCP allows efficient scaling for learning from large-scale motion databases and adding new tasks, such as fail-state recovery, without catastrophic forgetting. We demonstrate the effectiveness of our controller by using it to imitate noisy poses from video-based pose estimators and language-based motion generators in a live and real-time multi-person avatar use case.

## 개요
우리는 노이즈가 있는 입력(예: 비디오에서 추정된 포즈 또는 언어로 생성된 포즈)과 예상치 못한 낙하 상황에서도 높은 정확도의 모션 모방과 결함 허용 동작을 달성하는 물리 기반 휴머노이드 제어기를 제시합니다. 우리의 제어기는 외부 안정화 힘을 사용하지 않고도 최대 1만 개의 모션 클립을 학습할 수 있으며, 실패 상태에서 자연스럽게 회복하는 방법을 학습합니다. 참조 모션이 주어지면, 우리의 제어기는 리셋 없이 시뮬레이션된 아바타를 지속적으로 제어할 수 있습니다. 핵심적으로, 우리는 점진적 곱셈 제어 정책(PMCP)을 제안합니다. 이는 점점 더 어려운 모션 시퀀스를 학습하기 위해 새로운 네트워크 용량을 동적으로 할당합니다. PMCP는 대규모 모션 데이터베이스에서 효율적인 학습 확장을 가능하게 하며, 파국적 망각 없이 실패 상태 복구와 같은 새로운 작업을 추가할 수 있게 합니다. 우리는 비디오 기반 포즈 추정기와 언어 기반 모션 생성기에서 얻은 노이즈가 있는 포즈를 실시간 다중 인물 아바타 사용 사례에서 모방함으로써 제어기의 효과를 입증합니다.

## 핵심 내용
우리는 노이즈가 있는 입력(예: 비디오에서 추정된 포즈 또는 언어로 생성된 포즈)과 예상치 못한 낙하 상황에서도 높은 정확도의 모션 모방과 결함 허용 동작을 달성하는 물리 기반 휴머노이드 제어기를 제시합니다. 우리의 제어기는 외부 안정화 힘을 사용하지 않고도 최대 1만 개의 모션 클립을 학습할 수 있으며, 실패 상태에서 자연스럽게 회복하는 방법을 학습합니다. 참조 모션이 주어지면, 우리의 제어기는 리셋 없이 시뮬레이션된 아바타를 지속적으로 제어할 수 있습니다. 핵심적으로, 우리는 점진적 곱셈 제어 정책(PMCP)을 제안합니다. 이는 점점 더 어려운 모션 시퀀스를 학습하기 위해 새로운 네트워크 용량을 동적으로 할당합니다. PMCP는 대규모 모션 데이터베이스에서 효율적인 학습 확장을 가능하게 하며, 파국적 망각 없이 실패 상태 복구와 같은 새로운 작업을 추가할 수 있게 합니다. 우리는 비디오 기반 포즈 추정기와 언어 기반 모션 생성기에서 얻은 노이즈가 있는 포즈를 실시간 다중 인물 아바타 사용 사례에서 모방함으로써 제어기의 효과를 입증합니다.
