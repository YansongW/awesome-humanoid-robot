---
$id: ent_paper_ace_a_cross_platform_visual_ex_2024_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation'
  zh: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation'
  ko: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation'
summary:
  en: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation is a 2024 work on teleoperation
    for humanoid robots, with open-source code available.'
  zh: ACE 是一个 2024 年提出的跨平台视觉外骨骼遥操作系统，旨在以低成本实现灵巧操作。该系统通过手部摄像头和便携式外骨骼捕捉手指与手腕姿态，可泛化至人形手、臂手、臂夹爪及四足夹爪等多种机器人平台，并已开源代码。
  ko: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation is a 2024 work on teleoperation
    for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ace
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.11805v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation (arXiv)'
  url: https://arxiv.org/abs/2408.11805
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation project page'
  url: https://ace-teleop.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
ACE 系统由手部摄像头和便携式外骨骼组成，能实时高精度捕捉手指与手腕的 3D 姿态。与需要针对不同机器人进行硬件定制的传统方案不同，ACE 单一系统即可适配人形手、臂手、臂夹爪以及四足夹爪等多种末端执行器。该系统支持跨平台高精度遥操作，从而能够在多种机器人平台上实现复杂操作任务的模仿学习，有效降低了灵巧遥操作的成本与使用门槛。

## 核心内容
### 背景与问题
- 基于演示的学习（Learning from demonstrations）在机器人操作中效果显著，尤其是近期通过遥操作系统收集的大规模机器人数据。
- 构建跨不同机器人平台的高效遥操作系统至关重要，但现有系统缺乏针对多种末端执行器（如拟人机器人手和夹爪）的低成本、用户友好方案。

### ACE 系统设计
- **核心组件**：一个面向手部的摄像头（hand-facing camera）用于捕捉 3D 手部姿态，以及一个安装在便携式底座上的外骨骼（exoskeleton）。
- **功能**：实现对手指和手腕姿态的精确实时捕捉。
- **跨平台能力**：单一系统即可泛化至人形手（humanoid hands）、臂手（arm-hands）、臂夹爪（arm-gripper）以及四足夹爪（quadruped-gripper）系统，无需针对不同机器人进行硬件定制。

### 实验与结论
- 该系统支持高精度遥操作，使得在多种平台上进行复杂操作任务的模仿学习成为可能。
- 与以往需要硬件定制的系统相比，ACE 显著降低了成本并提升了易用性。

## Overview
Learning from demonstrations has shown to be an effective approach to robotic manipulation, especially with the recently collected large-scale robot data with teleoperation systems. Building an efficient teleoperation system across diverse robot platforms has become more crucial than ever. However, there is a notable lack of cost-effective and user-friendly teleoperation systems for different end-effectors, e.g., anthropomorphic robot hands and grippers, that can operate across multiple platforms. To address this issue, we develop ACE, a cross-platform visual-exoskeleton system for low-cost dexterous teleoperation. Our system utilizes a hand-facing camera to capture 3D hand poses and an exoskeleton mounted on a portable base, enabling accurate real-time capture of both finger and wrist poses. Compared to previous systems, which often require hardware customization according to different robots, our single system can generalize to humanoid hands, arm-hands, arm-gripper, and quadruped-gripper systems with high-precision teleoperation. This enables imitation learning for complex manipulation tasks on diverse platforms.

## 개요
시연을 통한 학습은 로봇 조작에 효과적인 접근 방식으로 입증되었으며, 특히 최근 원격 조작 시스템을 통해 수집된 대규모 로봇 데이터에서 두드러집니다. 다양한 로봇 플랫폼에서 효율적인 원격 조작 시스템을 구축하는 것이 그 어느 때보다 중요해졌습니다. 그러나 인체공학적 로봇 손이나 그리퍼와 같은 다양한 엔드 이펙터에 대해 비용 효율적이고 사용자 친화적인 원격 조작 시스템이 여러 플랫폼에서 작동할 수 있도록 하는 데는 현저한 부족이 있습니다. 이 문제를 해결하기 위해 우리는 저비용의 정교한 원격 조작을 위한 크로스 플랫폼 시각-외골격 시스템인 ACE를 개발했습니다. 우리 시스템은 손을 향한 카메라를 사용하여 3D 손 자세를 캡처하고, 휴대용 베이스에 장착된 외골격을 통해 손가락과 손목 자세를 모두 실시간으로 정확하게 캡처합니다. 이전 시스템이 종종 로봇에 따라 하드웨어를 맞춤 제작해야 했던 것과 달리, 우리의 단일 시스템은 인간형 손, 팔-손, 팔-그리퍼, 사족-그리퍼 시스템에 고정밀 원격 조작으로 일반화할 수 있습니다. 이를 통해 다양한 플랫폼에서 복잡한 조작 작업에 대한 모방 학습이 가능해집니다.

## 핵심 내용
시연을 통한 학습은 로봇 조작에 효과적인 접근 방식으로 입증되었으며, 특히 최근 원격 조작 시스템을 통해 수집된 대규모 로봇 데이터에서 두드러집니다. 다양한 로봇 플랫폼에서 효율적인 원격 조작 시스템을 구축하는 것이 그 어느 때보다 중요해졌습니다. 그러나 인체공학적 로봇 손이나 그리퍼와 같은 다양한 엔드 이펙터에 대해 비용 효율적이고 사용자 친화적인 원격 조작 시스템이 여러 플랫폼에서 작동할 수 있도록 하는 데는 현저한 부족이 있습니다. 이 문제를 해결하기 위해 우리는 저비용의 정교한 원격 조작을 위한 크로스 플랫폼 시각-외골격 시스템인 ACE를 개발했습니다. 우리 시스템은 손을 향한 카메라를 사용하여 3D 손 자세를 캡처하고, 휴대용 베이스에 장착된 외골격을 통해 손가락과 손목 자세를 모두 실시간으로 정확하게 캡처합니다. 이전 시스템이 종종 로봇에 따라 하드웨어를 맞춤 제작해야 했던 것과 달리, 우리의 단일 시스템은 인간형 손, 팔-손, 팔-그리퍼, 사족-그리퍼 시스템에 고정밀 원격 조작으로 일반화할 수 있습니다. 이를 통해 다양한 플랫폼에서 복잡한 조작 작업에 대한 모방 학습이 가능해집니다.

## 参考
- http://arxiv.org/abs/2408.11805v1
