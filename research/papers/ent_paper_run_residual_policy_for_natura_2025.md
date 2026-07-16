---
$id: ent_paper_run_residual_policy_for_natura_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RuN: Residual Policy for Natural Humanoid Locomotion'
  zh: 'RuN: Residual Policy for Natural Humanoid Locomotion'
  ko: 'RuN: Residual Policy for Natural Humanoid Locomotion'
summary:
  en: 'RuN: Residual Policy for Natural Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
  zh: 'RuN: Residual Policy for Natural Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
  ko: 'RuN: Residual Policy for Natural Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
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
- run
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20696v1.
sources:
- id: src_001
  type: paper
  title: 'RuN: Residual Policy for Natural Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2509.20696
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Enabling humanoid robots to achieve natural and dynamic locomotion across a wide range of speeds, including smooth transitions from walking to running, presents a significant challenge. Existing deep reinforcement learning methods typically require the policy to directly track a reference motion, forcing a single policy to simultaneously learn motion imitation, velocity tracking, and stability maintenance. To address this, we introduce RuN, a novel decoupled residual learning framework. RuN decomposes the control task by pairing a pre-trained Conditional Motion Generator, which provides a kinematically natural motion prior, with a reinforcement learning policy that learns a lightweight residual correction to handle dynamical interactions. Experiments in simulation and reality on the Unitree G1 humanoid robot demonstrate that RuN achieves stable, natural gaits and smooth walk-run transitions across a broad velocity range (0-2.5 m/s), outperforming state-of-the-art methods in both training efficiency and final performance.

## 核心内容
Enabling humanoid robots to achieve natural and dynamic locomotion across a wide range of speeds, including smooth transitions from walking to running, presents a significant challenge. Existing deep reinforcement learning methods typically require the policy to directly track a reference motion, forcing a single policy to simultaneously learn motion imitation, velocity tracking, and stability maintenance. To address this, we introduce RuN, a novel decoupled residual learning framework. RuN decomposes the control task by pairing a pre-trained Conditional Motion Generator, which provides a kinematically natural motion prior, with a reinforcement learning policy that learns a lightweight residual correction to handle dynamical interactions. Experiments in simulation and reality on the Unitree G1 humanoid robot demonstrate that RuN achieves stable, natural gaits and smooth walk-run transitions across a broad velocity range (0-2.5 m/s), outperforming state-of-the-art methods in both training efficiency and final performance.

## 参考
- http://arxiv.org/abs/2509.20696v1

## Overview
Enabling humanoid robots to achieve natural and dynamic locomotion across a wide range of speeds, including smooth transitions from walking to running, presents a significant challenge. Existing deep reinforcement learning methods typically require the policy to directly track a reference motion, forcing a single policy to simultaneously learn motion imitation, velocity tracking, and stability maintenance. To address this, we introduce RuN, a novel decoupled residual learning framework. RuN decomposes the control task by pairing a pre-trained Conditional Motion Generator, which provides a kinematically natural motion prior, with a reinforcement learning policy that learns a lightweight residual correction to handle dynamical interactions. Experiments in simulation and reality on the Unitree G1 humanoid robot demonstrate that RuN achieves stable, natural gaits and smooth walk-run transitions across a broad velocity range (0-2.5 m/s), outperforming state-of-the-art methods in both training efficiency and final performance.

## Content
Enabling humanoid robots to achieve natural and dynamic locomotion across a wide range of speeds, including smooth transitions from walking to running, presents a significant challenge. Existing deep reinforcement learning methods typically require the policy to directly track a reference motion, forcing a single policy to simultaneously learn motion imitation, velocity tracking, and stability maintenance. To address this, we introduce RuN, a novel decoupled residual learning framework. RuN decomposes the control task by pairing a pre-trained Conditional Motion Generator, which provides a kinematically natural motion prior, with a reinforcement learning policy that learns a lightweight residual correction to handle dynamical interactions. Experiments in simulation and reality on the Unitree G1 humanoid robot demonstrate that RuN achieves stable, natural gaits and smooth walk-run transitions across a broad velocity range (0-2.5 m/s), outperforming state-of-the-art methods in both training efficiency and final performance.

## 개요
휴머노이드 로봇이 걷기에서 달리기로의 부드러운 전환을 포함하여 광범위한 속도에서 자연스럽고 역동적인 보행을 구현하는 것은 중요한 도전 과제입니다. 기존의 심층 강화 학습 방법은 일반적으로 정책이 참조 동작을 직접 추적하도록 요구하며, 단일 정책이 동작 모방, 속도 추적 및 안정성 유지를 동시에 학습하도록 강제합니다. 이를 해결하기 위해 우리는 RuN이라는 새로운 분리된 잔차 학습 프레임워크를 소개합니다. RuN은 운동학적으로 자연스러운 동작 사전을 제공하는 사전 훈련된 조건부 동작 생성기와 동적 상호작용을 처리하기 위해 가벼운 잔차 보정을 학습하는 강화 학습 정책을 결합하여 제어 작업을 분해합니다. Unitree G1 휴머노이드 로봇을 대상으로 한 시뮬레이션 및 실제 실험에서 RuN은 광범위한 속도 범위(0-2.5m/s)에서 안정적이고 자연스러운 보행과 부드러운 걷기-달리기 전환을 달성하며, 훈련 효율성과 최종 성능 모두에서 최신 방법을 능가함을 입증했습니다.

## 핵심 내용
휴머노이드 로봇이 걷기에서 달리기로의 부드러운 전환을 포함하여 광범위한 속도에서 자연스럽고 역동적인 보행을 구현하는 것은 중요한 도전 과제입니다. 기존의 심층 강화 학습 방법은 일반적으로 정책이 참조 동작을 직접 추적하도록 요구하며, 단일 정책이 동작 모방, 속도 추적 및 안정성 유지를 동시에 학습하도록 강제합니다. 이를 해결하기 위해 우리는 RuN이라는 새로운 분리된 잔차 학습 프레임워크를 소개합니다. RuN은 운동학적으로 자연스러운 동작 사전을 제공하는 사전 훈련된 조건부 동작 생성기와 동적 상호작용을 처리하기 위해 가벼운 잔차 보정을 학습하는 강화 학습 정책을 결합하여 제어 작업을 분해합니다. Unitree G1 휴머노이드 로봇을 대상으로 한 시뮬레이션 및 실제 실험에서 RuN은 광범위한 속도 범위(0-2.5m/s)에서 안정적이고 자연스러운 보행과 부드러운 걷기-달리기 전환을 달성하며, 훈련 효율성과 최종 성능 모두에서 최신 방법을 능가함을 입증했습니다.
