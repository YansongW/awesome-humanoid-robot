---
$id: ent_paper_ace_a_cross_platform_visual_ex_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation'
  zh: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation'
  ko: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation'
summary:
  en: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
  zh: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
  ko: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation is a 2024 work on manipulation
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
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.11805v1.
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
Learning from demonstrations has shown to be an effective approach to robotic manipulation, especially with the recently collected large-scale robot data with teleoperation systems. Building an efficient teleoperation system across diverse robot platforms has become more crucial than ever. However, there is a notable lack of cost-effective and user-friendly teleoperation systems for different end-effectors, e.g., anthropomorphic robot hands and grippers, that can operate across multiple platforms. To address this issue, we develop ACE, a cross-platform visual-exoskeleton system for low-cost dexterous teleoperation. Our system utilizes a hand-facing camera to capture 3D hand poses and an exoskeleton mounted on a portable base, enabling accurate real-time capture of both finger and wrist poses. Compared to previous systems, which often require hardware customization according to different robots, our single system can generalize to humanoid hands, arm-hands, arm-gripper, and quadruped-gripper systems with high-precision teleoperation. This enables imitation learning for complex manipulation tasks on diverse platforms.

## 核心内容
Learning from demonstrations has shown to be an effective approach to robotic manipulation, especially with the recently collected large-scale robot data with teleoperation systems. Building an efficient teleoperation system across diverse robot platforms has become more crucial than ever. However, there is a notable lack of cost-effective and user-friendly teleoperation systems for different end-effectors, e.g., anthropomorphic robot hands and grippers, that can operate across multiple platforms. To address this issue, we develop ACE, a cross-platform visual-exoskeleton system for low-cost dexterous teleoperation. Our system utilizes a hand-facing camera to capture 3D hand poses and an exoskeleton mounted on a portable base, enabling accurate real-time capture of both finger and wrist poses. Compared to previous systems, which often require hardware customization according to different robots, our single system can generalize to humanoid hands, arm-hands, arm-gripper, and quadruped-gripper systems with high-precision teleoperation. This enables imitation learning for complex manipulation tasks on diverse platforms.

## 参考
- http://arxiv.org/abs/2408.11805v1

## Overview
Learning from demonstrations has shown to be an effective approach to robotic manipulation, especially with the recently collected large-scale robot data with teleoperation systems. Building an efficient teleoperation system across diverse robot platforms has become more crucial than ever. However, there is a notable lack of cost-effective and user-friendly teleoperation systems for different end-effectors, e.g., anthropomorphic robot hands and grippers, that can operate across multiple platforms. To address this issue, we develop ACE, a cross-platform visual-exoskeleton system for low-cost dexterous teleoperation. Our system utilizes a hand-facing camera to capture 3D hand poses and an exoskeleton mounted on a portable base, enabling accurate real-time capture of both finger and wrist poses. Compared to previous systems, which often require hardware customization according to different robots, our single system can generalize to humanoid hands, arm-hands, arm-gripper, and quadruped-gripper systems with high-precision teleoperation. This enables imitation learning for complex manipulation tasks on diverse platforms.

## Content
Learning from demonstrations has shown to be an effective approach to robotic manipulation, especially with the recently collected large-scale robot data with teleoperation systems. Building an efficient teleoperation system across diverse robot platforms has become more crucial than ever. However, there is a notable lack of cost-effective and user-friendly teleoperation systems for different end-effectors, e.g., anthropomorphic robot hands and grippers, that can operate across multiple platforms. To address this issue, we develop ACE, a cross-platform visual-exoskeleton system for low-cost dexterous teleoperation. Our system utilizes a hand-facing camera to capture 3D hand poses and an exoskeleton mounted on a portable base, enabling accurate real-time capture of both finger and wrist poses. Compared to previous systems, which often require hardware customization according to different robots, our single system can generalize to humanoid hands, arm-hands, arm-gripper, and quadruped-gripper systems with high-precision teleoperation. This enables imitation learning for complex manipulation tasks on diverse platforms.

## 개요
시연을 통한 학습은 로봇 조작 분야에서 효과적인 접근 방식으로 입증되었으며, 특히 최근 원격 조작 시스템을 통해 수집된 대규모 로봇 데이터와 함께 그 중요성이 더욱 부각되고 있습니다. 다양한 로봇 플랫폼에서 효율적인 원격 조작 시스템을 구축하는 것이 그 어느 때보다 중요해졌습니다. 그러나 인체공학적 로봇 손과 그리퍼와 같은 다양한 엔드 이펙터(end-effector)를 지원하면서 여러 플랫폼에서 작동 가능한 비용 효율적이고 사용자 친화적인 원격 조작 시스템은 현저히 부족한 실정입니다. 이 문제를 해결하기 위해 우리는 저비용 정밀 원격 조작을 위한 크로스 플랫폼 시각-외골격 시스템인 ACE를 개발했습니다. 본 시스템은 손을 향한 카메라를 사용하여 3D 손 자세를 포착하고, 휴대용 베이스에 장착된 외골격을 통해 손가락과 손목 자세를 실시간으로 정확하게 캡처합니다. 이전 시스템이 로봇에 따라 하드웨어를 맞춤 제작해야 했던 것과 달리, 우리의 단일 시스템은 휴머노이드 손, 팔-손, 팔-그리퍼, 사족-그리퍼 시스템에 고정밀 원격 조작을 적용할 수 있습니다. 이를 통해 다양한 플랫폼에서 복잡한 조작 작업을 위한 모방 학습이 가능해집니다.

## 핵심 내용
시연을 통한 학습은 로봇 조작 분야에서 효과적인 접근 방식으로 입증되었으며, 특히 최근 원격 조작 시스템을 통해 수집된 대규모 로봇 데이터와 함께 그 중요성이 더욱 부각되고 있습니다. 다양한 로봇 플랫폼에서 효율적인 원격 조작 시스템을 구축하는 것이 그 어느 때보다 중요해졌습니다. 그러나 인체공학적 로봇 손과 그리퍼와 같은 다양한 엔드 이펙터(end-effector)를 지원하면서 여러 플랫폼에서 작동 가능한 비용 효율적이고 사용자 친화적인 원격 조작 시스템은 현저히 부족한 실정입니다. 이 문제를 해결하기 위해 우리는 저비용 정밀 원격 조작을 위한 크로스 플랫폼 시각-외골격 시스템인 ACE를 개발했습니다. 본 시스템은 손을 향한 카메라를 사용하여 3D 손 자세를 포착하고, 휴대용 베이스에 장착된 외골격을 통해 손가락과 손목 자세를 실시간으로 정확하게 캡처합니다. 이전 시스템이 로봇에 따라 하드웨어를 맞춤 제작해야 했던 것과 달리, 우리의 단일 시스템은 휴머노이드 손, 팔-손, 팔-그리퍼, 사족-그리퍼 시스템에 고정밀 원격 조작을 적용할 수 있습니다. 이를 통해 다양한 플랫폼에서 복잡한 조작 작업을 위한 모방 학습이 가능해집니다.
