---
$id: ent_paper_slac_simulation_pretrained_lat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning'
  zh: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning'
  ko: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning'
summary:
  en: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
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
- slac
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.04147v4.
sources:
- id: src_001
  type: paper
  title: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2506.04147
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning project page'
  url: https://robo-rl.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Building capable household and industrial robots requires mastering the control of versatile, high-degree-of-freedom (DoF) systems such as mobile manipulators. While reinforcement learning (RL) holds promise for autonomously acquiring robot control policies, scaling it to high-DoF embodiments remains challenging. Direct RL in the real world demands both safe exploration and high sample efficiency, which are difficult to achieve in practice. Sim-to-real RL, on the other hand, is often brittle due to the reality gap. This paper introduces SLAC, a method that renders real-world RL feasible for complex embodiments by leveraging a low-fidelity simulator to pretrain a task-agnostic latent action space. SLAC trains this latent action space via a customized unsupervised skill discovery method designed to promote temporal abstraction, disentanglement, and safety, thereby facilitating efficient downstream learning. Once a latent action space is learned, SLAC uses it as the action interface for a novel off-policy RL algorithm to autonomously learn downstream tasks through real-world interactions. We evaluate SLAC against existing methods on a suite of bimanual mobile manipulation tasks, where it achieves state-of-the-art performance. Notably, SLAC learns contact-rich whole-body tasks in under an hour of real-world interactions, without relying on any demonstrations or hand-crafted behavior priors. More information and robot videos at robo-rl.github.io

## 核心内容
Building capable household and industrial robots requires mastering the control of versatile, high-degree-of-freedom (DoF) systems such as mobile manipulators. While reinforcement learning (RL) holds promise for autonomously acquiring robot control policies, scaling it to high-DoF embodiments remains challenging. Direct RL in the real world demands both safe exploration and high sample efficiency, which are difficult to achieve in practice. Sim-to-real RL, on the other hand, is often brittle due to the reality gap. This paper introduces SLAC, a method that renders real-world RL feasible for complex embodiments by leveraging a low-fidelity simulator to pretrain a task-agnostic latent action space. SLAC trains this latent action space via a customized unsupervised skill discovery method designed to promote temporal abstraction, disentanglement, and safety, thereby facilitating efficient downstream learning. Once a latent action space is learned, SLAC uses it as the action interface for a novel off-policy RL algorithm to autonomously learn downstream tasks through real-world interactions. We evaluate SLAC against existing methods on a suite of bimanual mobile manipulation tasks, where it achieves state-of-the-art performance. Notably, SLAC learns contact-rich whole-body tasks in under an hour of real-world interactions, without relying on any demonstrations or hand-crafted behavior priors. More information and robot videos at robo-rl.github.io

## 参考
- http://arxiv.org/abs/2506.04147v4

## Overview
Building capable household and industrial robots requires mastering the control of versatile, high-degree-of-freedom (DoF) systems such as mobile manipulators. While reinforcement learning (RL) holds promise for autonomously acquiring robot control policies, scaling it to high-DoF embodiments remains challenging. Direct RL in the real world demands both safe exploration and high sample efficiency, which are difficult to achieve in practice. Sim-to-real RL, on the other hand, is often brittle due to the reality gap. This paper introduces SLAC, a method that renders real-world RL feasible for complex embodiments by leveraging a low-fidelity simulator to pretrain a task-agnostic latent action space. SLAC trains this latent action space via a customized unsupervised skill discovery method designed to promote temporal abstraction, disentanglement, and safety, thereby facilitating efficient downstream learning. Once a latent action space is learned, SLAC uses it as the action interface for a novel off-policy RL algorithm to autonomously learn downstream tasks through real-world interactions. We evaluate SLAC against existing methods on a suite of bimanual mobile manipulation tasks, where it achieves state-of-the-art performance. Notably, SLAC learns contact-rich whole-body tasks in under an hour of real-world interactions, without relying on any demonstrations or hand-crafted behavior priors. More information and robot videos at robo-rl.github.io

## Content
Building capable household and industrial robots requires mastering the control of versatile, high-degree-of-freedom (DoF) systems such as mobile manipulators. While reinforcement learning (RL) holds promise for autonomously acquiring robot control policies, scaling it to high-DoF embodiments remains challenging. Direct RL in the real world demands both safe exploration and high sample efficiency, which are difficult to achieve in practice. Sim-to-real RL, on the other hand, is often brittle due to the reality gap. This paper introduces SLAC, a method that renders real-world RL feasible for complex embodiments by leveraging a low-fidelity simulator to pretrain a task-agnostic latent action space. SLAC trains this latent action space via a customized unsupervised skill discovery method designed to promote temporal abstraction, disentanglement, and safety, thereby facilitating efficient downstream learning. Once a latent action space is learned, SLAC uses it as the action interface for a novel off-policy RL algorithm to autonomously learn downstream tasks through real-world interactions. We evaluate SLAC against existing methods on a suite of bimanual mobile manipulation tasks, where it achieves state-of-the-art performance. Notably, SLAC learns contact-rich whole-body tasks in under an hour of real-world interactions, without relying on any demonstrations or hand-crafted behavior priors. More information and robot videos at robo-rl.github.io

## 개요
유능한 가정용 및 산업용 로봇을 구축하려면 모바일 매니퓰레이터와 같은 다재다능하고 고자유도(DoF) 시스템의 제어를 마스터해야 합니다. 강화 학습(RL)은 로봇 제어 정책을 자율적으로 획득할 가능성이 있지만, 고자유도 구현체로 확장하는 것은 여전히 어려운 과제입니다. 실제 세계에서의 직접 RL은 안전한 탐험과 높은 샘플 효율성을 모두 요구하지만, 실제로 이를 달성하기는 어렵습니다. 반면, 시뮬레이션-실제 RL은 현실 격차로 인해 종종 취약합니다. 본 논문은 저정밀 시뮬레이터를 활용하여 작업에 구애받지 않는 잠재 행동 공간을 사전 학습함으로써 복잡한 구현체에서 실제 세계 RL을 실현 가능하게 만드는 방법인 SLAC를 소개합니다. SLAC는 시간적 추상화, 분리성 및 안전성을 촉진하도록 설계된 맞춤형 비지도 기술 발견 방법을 통해 이 잠재 행동 공간을 학습하며, 이를 통해 효율적인 하위 학습을 용이하게 합니다. 잠재 행동 공간이 학습되면, SLAC는 이를 새로운 오프-정책 RL 알고리즘의 행동 인터페이스로 사용하여 실제 세계 상호작용을 통해 하위 작업을 자율적으로 학습합니다. 우리는 SLAC를 기존 방법들과 양손 모바일 매니퓰레이션 작업 세트에서 평가했으며, 최첨단 성능을 달성했습니다. 특히, SLAC는 시연이나 수작업 행동 사전 지식에 의존하지 않고 1시간 미만의 실제 세계 상호작용으로 접촉이 많은 전신 작업을 학습합니다. 더 많은 정보와 로봇 비디오는 robo-rl.github.io에서 확인할 수 있습니다.

## 핵심 내용
유능한 가정용 및 산업용 로봇을 구축하려면 모바일 매니퓰레이터와 같은 다재다능하고 고자유도(DoF) 시스템의 제어를 마스터해야 합니다. 강화 학습(RL)은 로봇 제어 정책을 자율적으로 획득할 가능성이 있지만, 고자유도 구현체로 확장하는 것은 여전히 어려운 과제입니다. 실제 세계에서의 직접 RL은 안전한 탐험과 높은 샘플 효율성을 모두 요구하지만, 실제로 이를 달성하기는 어렵습니다. 반면, 시뮬레이션-실제 RL은 현실 격차로 인해 종종 취약합니다. 본 논문은 저정밀 시뮬레이터를 활용하여 작업에 구애받지 않는 잠재 행동 공간을 사전 학습함으로써 복잡한 구현체에서 실제 세계 RL을 실현 가능하게 만드는 방법인 SLAC를 소개합니다. SLAC는 시간적 추상화, 분리성 및 안전성을 촉진하도록 설계된 맞춤형 비지도 기술 발견 방법을 통해 이 잠재 행동 공간을 학습하며, 이를 통해 효율적인 하위 학습을 용이하게 합니다. 잠재 행동 공간이 학습되면, SLAC는 이를 새로운 오프-정책 RL 알고리즘의 행동 인터페이스로 사용하여 실제 세계 상호작용을 통해 하위 작업을 자율적으로 학습합니다. 우리는 SLAC를 기존 방법들과 양손 모바일 매니퓰레이션 작업 세트에서 평가했으며, 최첨단 성능을 달성했습니다. 특히, SLAC는 시연이나 수작업 행동 사전 지식에 의존하지 않고 1시간 미만의 실제 세계 상호작용으로 접촉이 많은 전신 작업을 학습합니다. 더 많은 정보와 로봇 비디오는 robo-rl.github.io에서 확인할 수 있습니다.
