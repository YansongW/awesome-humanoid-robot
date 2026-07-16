---
$id: ent_paper_unified_humanoid_fall_safety_p_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Humanoid Fall-Safety Policy from a Few Demonstrations
  zh: Unified Humanoid Fall-Safety Policy from a Few Demonstrations
  ko: Unified Humanoid Fall-Safety Policy from a Few Demonstrations
summary:
  en: Unified Humanoid Fall-Safety Policy from a Few Demonstrations is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Unified Humanoid Fall-Safety Policy from a Few Demonstrations is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Unified Humanoid Fall-Safety Policy from a Few Demonstrations is a 2025 work on loco-manipulation and whole-body-control
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
- loco_manipulation
- unified_humanoid_fall_safety_p
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.07407v1.
sources:
- id: src_001
  type: paper
  title: Unified Humanoid Fall-Safety Policy from a Few Demonstrations (arXiv)
  url: https://arxiv.org/abs/2511.07407
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Falling is an inherent risk of humanoid mobility. Maintaining stability is thus a primary safety focus in robot control and learning, yet no existing approach fully averts loss of balance. When instability does occur, prior work addresses only isolated aspects of falling: avoiding falls, choreographing a controlled descent, or standing up afterward. Consequently, humanoid robots lack integrated strategies for impact mitigation and prompt recovery when real falls defy these scripts. We aim to go beyond keeping balance to make the entire fall-and-recovery process safe and autonomous: prevent falls when possible, reduce impact when unavoidable, and stand up when fallen. By fusing sparse human demonstrations with reinforcement learning and an adaptive diffusion-based memory of safe reactions, we learn adaptive whole-body behaviors that unify fall prevention, impact mitigation, and rapid recovery in one policy. Experiments in simulation and on a Unitree G1 demonstrate robust sim-to-real transfer, lower impact forces, and consistently fast recovery across diverse disturbances, pointing towards safer, more resilient humanoids in real environments. Videos are available at https://firm2025.github.io/.

## 核心内容
Falling is an inherent risk of humanoid mobility. Maintaining stability is thus a primary safety focus in robot control and learning, yet no existing approach fully averts loss of balance. When instability does occur, prior work addresses only isolated aspects of falling: avoiding falls, choreographing a controlled descent, or standing up afterward. Consequently, humanoid robots lack integrated strategies for impact mitigation and prompt recovery when real falls defy these scripts. We aim to go beyond keeping balance to make the entire fall-and-recovery process safe and autonomous: prevent falls when possible, reduce impact when unavoidable, and stand up when fallen. By fusing sparse human demonstrations with reinforcement learning and an adaptive diffusion-based memory of safe reactions, we learn adaptive whole-body behaviors that unify fall prevention, impact mitigation, and rapid recovery in one policy. Experiments in simulation and on a Unitree G1 demonstrate robust sim-to-real transfer, lower impact forces, and consistently fast recovery across diverse disturbances, pointing towards safer, more resilient humanoids in real environments. Videos are available at https://firm2025.github.io/.

## 参考
- http://arxiv.org/abs/2511.07407v1

## Overview
Falling is an inherent risk of humanoid mobility. Maintaining stability is thus a primary safety focus in robot control and learning, yet no existing approach fully averts loss of balance. When instability does occur, prior work addresses only isolated aspects of falling: avoiding falls, choreographing a controlled descent, or standing up afterward. Consequently, humanoid robots lack integrated strategies for impact mitigation and prompt recovery when real falls defy these scripts. We aim to go beyond keeping balance to make the entire fall-and-recovery process safe and autonomous: prevent falls when possible, reduce impact when unavoidable, and stand up when fallen. By fusing sparse human demonstrations with reinforcement learning and an adaptive diffusion-based memory of safe reactions, we learn adaptive whole-body behaviors that unify fall prevention, impact mitigation, and rapid recovery in one policy. Experiments in simulation and on a Unitree G1 demonstrate robust sim-to-real transfer, lower impact forces, and consistently fast recovery across diverse disturbances, pointing towards safer, more resilient humanoids in real environments. Videos are available at https://firm2025.github.io/.

## Content
Falling is an inherent risk of humanoid mobility. Maintaining stability is thus a primary safety focus in robot control and learning, yet no existing approach fully averts loss of balance. When instability does occur, prior work addresses only isolated aspects of falling: avoiding falls, choreographing a controlled descent, or standing up afterward. Consequently, humanoid robots lack integrated strategies for impact mitigation and prompt recovery when real falls defy these scripts. We aim to go beyond keeping balance to make the entire fall-and-recovery process safe and autonomous: prevent falls when possible, reduce impact when unavoidable, and stand up when fallen. By fusing sparse human demonstrations with reinforcement learning and an adaptive diffusion-based memory of safe reactions, we learn adaptive whole-body behaviors that unify fall prevention, impact mitigation, and rapid recovery in one policy. Experiments in simulation and on a Unitree G1 demonstrate robust sim-to-real transfer, lower impact forces, and consistently fast recovery across diverse disturbances, pointing towards safer, more resilient humanoids in real environments. Videos are available at https://firm2025.github.io/.

## 개요
넘어짐은 인간형 로봇의 이동성에 내재된 위험입니다. 따라서 안정성 유지는 로봇 제어 및 학습에서 주요 안전 초점이지만, 기존의 어떤 접근법도 균형 상실을 완전히 방지하지는 못합니다. 불안정이 발생할 경우, 기존 연구는 넘어짐 방지, 통제된 낙하 동작 설계, 또는 이후 일어서기 등 넘어짐의 개별적인 측면만을 다룹니다. 결과적으로 인간형 로봇은 실제 넘어짐이 이러한 시나리오를 벗어날 때 충격 완화와 신속한 회복을 위한 통합 전략이 부족합니다. 우리는 균형 유지를 넘어 넘어짐과 회복 전 과정을 안전하고 자율적으로 만드는 것을 목표로 합니다: 가능할 때는 넘어짐을 방지하고, 불가피할 때는 충격을 줄이며, 넘어졌을 때는 일어서는 것입니다. 희소한 인간 시연과 강화 학습, 그리고 적응형 확산 기반 안전 반응 메모리를 융합하여, 넘어짐 방지, 충격 완화, 신속한 회복을 하나의 정책으로 통합하는 적응형 전신 행동을 학습합니다. 시뮬레이션과 Unitree G1 로봇에서의 실험은 강건한 시뮬레이션-실제 전이, 낮은 충격력, 다양한 외란에서 일관되게 빠른 회복을 입증하며, 실제 환경에서 더 안전하고 회복력 있는 인간형 로봇을 향한 방향을 제시합니다. 비디오는 https://firm2025.github.io/에서 확인할 수 있습니다.

## 핵심 내용
넘어짐은 인간형 로봇의 이동성에 내재된 위험입니다. 따라서 안정성 유지는 로봇 제어 및 학습에서 주요 안전 초점이지만, 기존의 어떤 접근법도 균형 상실을 완전히 방지하지는 못합니다. 불안정이 발생할 경우, 기존 연구는 넘어짐 방지, 통제된 낙하 동작 설계, 또는 이후 일어서기 등 넘어짐의 개별적인 측면만을 다룹니다. 결과적으로 인간형 로봇은 실제 넘어짐이 이러한 시나리오를 벗어날 때 충격 완화와 신속한 회복을 위한 통합 전략이 부족합니다. 우리는 균형 유지를 넘어 넘어짐과 회복 전 과정을 안전하고 자율적으로 만드는 것을 목표로 합니다: 가능할 때는 넘어짐을 방지하고, 불가피할 때는 충격을 줄이며, 넘어졌을 때는 일어서는 것입니다. 희소한 인간 시연과 강화 학습, 그리고 적응형 확산 기반 안전 반응 메모리를 융합하여, 넘어짐 방지, 충격 완화, 신속한 회복을 하나의 정책으로 통합하는 적응형 전신 행동을 학습합니다. 시뮬레이션과 Unitree G1 로봇에서의 실험은 강건한 시뮬레이션-실제 전이, 낮은 충격력, 다양한 외란에서 일관되게 빠른 회복을 입증하며, 실제 환경에서 더 안전하고 회복력 있는 인간형 로봇을 향한 방향을 제시합니다. 비디오는 https://firm2025.github.io/에서 확인할 수 있습니다.
