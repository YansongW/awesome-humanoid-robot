---
$id: ent_paper_bunny_visionpro_real_time_bima_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning'
  zh: 'Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning'
  ko: 'Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning'
summary:
  en: 'Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning is a 2024 work on manipulation for
    humanoid robots, with open-source code available.'
  zh: 'Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning is a 2024 work on manipulation for
    humanoid robots, with open-source code available.'
  ko: 'Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning is a 2024 work on manipulation for
    humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bunny_visionpro
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.03162v1.
sources:
- id: src_001
  type: paper
  title: 'Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning (arXiv)'
  url: https://arxiv.org/abs/2407.03162
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning project page'
  url: https://dingry.github.io/projects/bunny_visionpro.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Teleoperation is a crucial tool for collecting human demonstrations, but controlling robots with bimanual dexterous hands remains a challenge. Existing teleoperation systems struggle to handle the complexity of coordinating two hands for intricate manipulations. We introduce Bunny-VisionPro, a real-time bimanual dexterous teleoperation system that leverages a VR headset. Unlike previous vision-based teleoperation systems, we design novel low-cost devices to provide haptic feedback to the operator, enhancing immersion. Our system prioritizes safety by incorporating collision and singularity avoidance while maintaining real-time performance through innovative designs. Bunny-VisionPro outperforms prior systems on a standard task suite, achieving higher success rates and reduced task completion times. Moreover, the high-quality teleoperation demonstrations improve downstream imitation learning performance, leading to better generalizability. Notably, Bunny-VisionPro enables imitation learning with challenging multi-stage, long-horizon dexterous manipulation tasks, which have rarely been addressed in previous work. Our system's ability to handle bimanual manipulations while prioritizing safety and real-time performance makes it a powerful tool for advancing dexterous manipulation and imitation learning.

## 核心内容
Teleoperation is a crucial tool for collecting human demonstrations, but controlling robots with bimanual dexterous hands remains a challenge. Existing teleoperation systems struggle to handle the complexity of coordinating two hands for intricate manipulations. We introduce Bunny-VisionPro, a real-time bimanual dexterous teleoperation system that leverages a VR headset. Unlike previous vision-based teleoperation systems, we design novel low-cost devices to provide haptic feedback to the operator, enhancing immersion. Our system prioritizes safety by incorporating collision and singularity avoidance while maintaining real-time performance through innovative designs. Bunny-VisionPro outperforms prior systems on a standard task suite, achieving higher success rates and reduced task completion times. Moreover, the high-quality teleoperation demonstrations improve downstream imitation learning performance, leading to better generalizability. Notably, Bunny-VisionPro enables imitation learning with challenging multi-stage, long-horizon dexterous manipulation tasks, which have rarely been addressed in previous work. Our system's ability to handle bimanual manipulations while prioritizing safety and real-time performance makes it a powerful tool for advancing dexterous manipulation and imitation learning.

## 参考
- http://arxiv.org/abs/2407.03162v1

## Overview
Teleoperation is a crucial tool for collecting human demonstrations, but controlling robots with bimanual dexterous hands remains a challenge. Existing teleoperation systems struggle to handle the complexity of coordinating two hands for intricate manipulations. We introduce Bunny-VisionPro, a real-time bimanual dexterous teleoperation system that leverages a VR headset. Unlike previous vision-based teleoperation systems, we design novel low-cost devices to provide haptic feedback to the operator, enhancing immersion. Our system prioritizes safety by incorporating collision and singularity avoidance while maintaining real-time performance through innovative designs. Bunny-VisionPro outperforms prior systems on a standard task suite, achieving higher success rates and reduced task completion times. Moreover, the high-quality teleoperation demonstrations improve downstream imitation learning performance, leading to better generalizability. Notably, Bunny-VisionPro enables imitation learning with challenging multi-stage, long-horizon dexterous manipulation tasks, which have rarely been addressed in previous work. Our system's ability to handle bimanual manipulations while prioritizing safety and real-time performance makes it a powerful tool for advancing dexterous manipulation and imitation learning.

## Content
Teleoperation is a crucial tool for collecting human demonstrations, but controlling robots with bimanual dexterous hands remains a challenge. Existing teleoperation systems struggle to handle the complexity of coordinating two hands for intricate manipulations. We introduce Bunny-VisionPro, a real-time bimanual dexterous teleoperation system that leverages a VR headset. Unlike previous vision-based teleoperation systems, we design novel low-cost devices to provide haptic feedback to the operator, enhancing immersion. Our system prioritizes safety by incorporating collision and singularity avoidance while maintaining real-time performance through innovative designs. Bunny-VisionPro outperforms prior systems on a standard task suite, achieving higher success rates and reduced task completion times. Moreover, the high-quality teleoperation demonstrations improve downstream imitation learning performance, leading to better generalizability. Notably, Bunny-VisionPro enables imitation learning with challenging multi-stage, long-horizon dexterous manipulation tasks, which have rarely been addressed in previous work. Our system's ability to handle bimanual manipulations while prioritizing safety and real-time performance makes it a powerful tool for advancing dexterous manipulation and imitation learning.

## 개요
원격 조작은 인간의 시연을 수집하는 중요한 도구이지만, 양손을 사용하는 정교한 로봇을 제어하는 것은 여전히 어려운 과제입니다. 기존의 원격 조작 시스템은 복잡한 작업을 위해 두 손을 조정하는 복잡성을 처리하는 데 어려움을 겪고 있습니다. 우리는 VR 헤드셋을 활용하는 실시간 양손 정교 원격 조작 시스템인 Bunny-VisionPro를 소개합니다. 이전의 비전 기반 원격 조작 시스템과 달리, 우리는 조작자에게 촉각 피드백을 제공하여 몰입감을 높이는 혁신적인 저비용 장치를 설계했습니다. 우리 시스템은 혁신적인 설계를 통해 실시간 성능을 유지하면서 충돌 및 특이점 회피를 통합하여 안전성을 최우선으로 합니다. Bunny-VisionPro는 표준 작업 세트에서 이전 시스템보다 우수한 성능을 보여주며, 더 높은 성공률과 단축된 작업 완료 시간을 달성합니다. 또한, 고품질의 원격 조작 시연은 하위 모방 학습 성능을 향상시켜 더 나은 일반화 능력을 이끌어냅니다. 특히, Bunny-VisionPro는 이전 연구에서 거의 다루어지지 않았던 도전적인 다단계, 장기 정교 조작 작업을 통한 모방 학습을 가능하게 합니다. 우리 시스템이 안전성과 실시간 성능을 우선시하면서 양손 조작을 처리할 수 있는 능력은 정교 조작 및 모방 학습을 발전시키는 강력한 도구가 됩니다.

## 핵심 내용
원격 조작은 인간의 시연을 수집하는 중요한 도구이지만, 양손을 사용하는 정교한 로봇을 제어하는 것은 여전히 어려운 과제입니다. 기존의 원격 조작 시스템은 복잡한 작업을 위해 두 손을 조정하는 복잡성을 처리하는 데 어려움을 겪고 있습니다. 우리는 VR 헤드셋을 활용하는 실시간 양손 정교 원격 조작 시스템인 Bunny-VisionPro를 소개합니다. 이전의 비전 기반 원격 조작 시스템과 달리, 우리는 조작자에게 촉각 피드백을 제공하여 몰입감을 높이는 혁신적인 저비용 장치를 설계했습니다. 우리 시스템은 혁신적인 설계를 통해 실시간 성능을 유지하면서 충돌 및 특이점 회피를 통합하여 안전성을 최우선으로 합니다. Bunny-VisionPro는 표준 작업 세트에서 이전 시스템보다 우수한 성능을 보여주며, 더 높은 성공률과 단축된 작업 완료 시간을 달성합니다. 또한, 고품질의 원격 조작 시연은 하위 모방 학습 성능을 향상시켜 더 나은 일반화 능력을 이끌어냅니다. 특히, Bunny-VisionPro는 이전 연구에서 거의 다루어지지 않았던 도전적인 다단계, 장기 정교 조작 작업을 통한 모방 학습을 가능하게 합니다. 우리 시스템이 안전성과 실시간 성능을 우선시하면서 양손 조작을 처리할 수 있는 능력은 정교 조작 및 모방 학습을 발전시키는 강력한 도구가 됩니다.
