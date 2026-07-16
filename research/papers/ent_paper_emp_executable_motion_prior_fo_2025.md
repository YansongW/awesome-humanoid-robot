---
$id: ent_paper_emp_executable_motion_prior_fo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation'
  zh: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation'
  ko: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation'
summary:
  en: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- emp
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.15649v1.
sources:
- id: src_001
  type: paper
  title: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation (arXiv)'
  url: https://arxiv.org/abs/2507.15649
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To support humanoid robots in performing manipulation tasks, it is essential to study stable standing while accommodating upper-body motions. However, the limited controllable range of humanoid robots in a standing position affects the stability of the entire body. Thus we introduce a reinforcement learning based framework for humanoid robots to imitate human upper-body motions while maintaining overall stability. Our approach begins with designing a retargeting network that generates a large-scale upper-body motion dataset for training the reinforcement learning (RL) policy, which enables the humanoid robot to track upper-body motion targets, employing domain randomization for enhanced robustness. To avoid exceeding the robot's execution capability and ensure safety and stability, we propose an Executable Motion Prior (EMP) module, which adjusts the input target movements based on the robot's current state. This adjustment improves standing stability while minimizing changes to motion amplitude. We evaluate our framework through simulation and real-world tests, demonstrating its practical applicability.

## 核心内容
To support humanoid robots in performing manipulation tasks, it is essential to study stable standing while accommodating upper-body motions. However, the limited controllable range of humanoid robots in a standing position affects the stability of the entire body. Thus we introduce a reinforcement learning based framework for humanoid robots to imitate human upper-body motions while maintaining overall stability. Our approach begins with designing a retargeting network that generates a large-scale upper-body motion dataset for training the reinforcement learning (RL) policy, which enables the humanoid robot to track upper-body motion targets, employing domain randomization for enhanced robustness. To avoid exceeding the robot's execution capability and ensure safety and stability, we propose an Executable Motion Prior (EMP) module, which adjusts the input target movements based on the robot's current state. This adjustment improves standing stability while minimizing changes to motion amplitude. We evaluate our framework through simulation and real-world tests, demonstrating its practical applicability.

## 参考
- http://arxiv.org/abs/2507.15649v1

## Overview
To support humanoid robots in performing manipulation tasks, it is essential to study stable standing while accommodating upper-body motions. However, the limited controllable range of humanoid robots in a standing position affects the stability of the entire body. Thus we introduce a reinforcement learning based framework for humanoid robots to imitate human upper-body motions while maintaining overall stability. Our approach begins with designing a retargeting network that generates a large-scale upper-body motion dataset for training the reinforcement learning (RL) policy, which enables the humanoid robot to track upper-body motion targets, employing domain randomization for enhanced robustness. To avoid exceeding the robot's execution capability and ensure safety and stability, we propose an Executable Motion Prior (EMP) module, which adjusts the input target movements based on the robot's current state. This adjustment improves standing stability while minimizing changes to motion amplitude. We evaluate our framework through simulation and real-world tests, demonstrating its practical applicability.

## Content
To support humanoid robots in performing manipulation tasks, it is essential to study stable standing while accommodating upper-body motions. However, the limited controllable range of humanoid robots in a standing position affects the stability of the entire body. Thus we introduce a reinforcement learning based framework for humanoid robots to imitate human upper-body motions while maintaining overall stability. Our approach begins with designing a retargeting network that generates a large-scale upper-body motion dataset for training the reinforcement learning (RL) policy, which enables the humanoid robot to track upper-body motion targets, employing domain randomization for enhanced robustness. To avoid exceeding the robot's execution capability and ensure safety and stability, we propose an Executable Motion Prior (EMP) module, which adjusts the input target movements based on the robot's current state. This adjustment improves standing stability while minimizing changes to motion amplitude. We evaluate our framework through simulation and real-world tests, demonstrating its practical applicability.

## 개요
휴머노이드 로봇이 조작 작업을 수행할 수 있도록 지원하려면 상체 동작을 수용하면서 안정적인 서기를 연구하는 것이 필수적입니다. 그러나 서 있는 자세에서 휴머노이드 로봇의 제어 가능 범위가 제한적이어서 전신의 안정성에 영향을 미칩니다. 이에 우리는 전반적인 안정성을 유지하면서 인간의 상체 동작을 모방할 수 있는 강화 학습 기반 프레임워크를 소개합니다. 우리의 접근 방식은 먼저 리타겟팅 네트워크를 설계하여 강화 학습(RL) 정책 훈련을 위한 대규모 상체 동작 데이터셋을 생성하는 것으로 시작됩니다. 이를 통해 휴머노이드 로봇이 상체 동작 목표를 추적할 수 있으며, 도메인 무작위화를 적용하여 강건성을 향상시킵니다. 로봇의 실행 능력을 초과하는 것을 방지하고 안전성과 안정성을 보장하기 위해, 우리는 실행 가능 동작 사전(EMP) 모듈을 제안합니다. 이 모듈은 로봇의 현재 상태에 따라 입력 목표 동작을 조정합니다. 이러한 조정은 동작 진폭의 변화를 최소화하면서 서기 안정성을 개선합니다. 우리는 시뮬레이션과 실제 환경 테스트를 통해 프레임워크를 평가하여 실용적 적용 가능성을 입증합니다.

## 핵심 내용
휴머노이드 로봇이 조작 작업을 수행할 수 있도록 지원하려면 상체 동작을 수용하면서 안정적인 서기를 연구하는 것이 필수적입니다. 그러나 서 있는 자세에서 휴머노이드 로봇의 제어 가능 범위가 제한적이어서 전신의 안정성에 영향을 미칩니다. 이에 우리는 전반적인 안정성을 유지하면서 인간의 상체 동작을 모방할 수 있는 강화 학습 기반 프레임워크를 소개합니다. 우리의 접근 방식은 먼저 리타겟팅 네트워크를 설계하여 강화 학습(RL) 정책 훈련을 위한 대규모 상체 동작 데이터셋을 생성하는 것으로 시작됩니다. 이를 통해 휴머노이드 로봇이 상체 동작 목표를 추적할 수 있으며, 도메인 무작위화를 적용하여 강건성을 향상시킵니다. 로봇의 실행 능력을 초과하는 것을 방지하고 안전성과 안정성을 보장하기 위해, 우리는 실행 가능 동작 사전(EMP) 모듈을 제안합니다. 이 모듈은 로봇의 현재 상태에 따라 입력 목표 동작을 조정합니다. 이러한 조정은 동작 진폭의 변화를 최소화하면서 서기 안정성을 개선합니다. 우리는 시뮬레이션과 실제 환경 테스트를 통해 프레임워크를 평가하여 실용적 적용 가능성을 입증합니다.
