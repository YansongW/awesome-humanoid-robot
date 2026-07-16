---
$id: ent_paper_maniskill_hab_a_benchmark_for_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks'
  zh: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks'
  ko: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks'
summary:
  en: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks is a 2024 work on simulation benchmark
    for humanoid robots.'
  zh: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks is a 2024 work on simulation benchmark
    for humanoid robots.'
  ko: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks is a 2024 work on simulation benchmark
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- maniskill_hab
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.13211v3.
sources:
- id: src_001
  type: paper
  title: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks (arXiv)'
  url: https://arxiv.org/abs/2412.13211
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks project page'
  url: https://arth-shukla.github.io/mshab/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
High-quality benchmarks are the foundation for embodied AI research, enabling significant advancements in long-horizon navigation, manipulation and rearrangement tasks. However, as frontier tasks in robotics get more advanced, they require faster simulation speed, more intricate test environments, and larger demonstration datasets. To this end, we present MS-HAB, a holistic benchmark for low-level manipulation and in-home object rearrangement. First, we provide a GPU-accelerated implementation of the Home Assistant Benchmark (HAB). We support realistic low-level control and achieve over 3x the speed of prior magical grasp implementations at a fraction of the GPU memory usage. Second, we train extensive reinforcement learning (RL) and imitation learning (IL) baselines for future work to compare against. Finally, we develop a rule-based trajectory filtering system to sample specific demonstrations from our RL policies which match predefined criteria for robot behavior and safety. Combining demonstration filtering with our fast environments enables efficient, controlled data generation at scale.

## 核心内容
High-quality benchmarks are the foundation for embodied AI research, enabling significant advancements in long-horizon navigation, manipulation and rearrangement tasks. However, as frontier tasks in robotics get more advanced, they require faster simulation speed, more intricate test environments, and larger demonstration datasets. To this end, we present MS-HAB, a holistic benchmark for low-level manipulation and in-home object rearrangement. First, we provide a GPU-accelerated implementation of the Home Assistant Benchmark (HAB). We support realistic low-level control and achieve over 3x the speed of prior magical grasp implementations at a fraction of the GPU memory usage. Second, we train extensive reinforcement learning (RL) and imitation learning (IL) baselines for future work to compare against. Finally, we develop a rule-based trajectory filtering system to sample specific demonstrations from our RL policies which match predefined criteria for robot behavior and safety. Combining demonstration filtering with our fast environments enables efficient, controlled data generation at scale.

## 参考
- http://arxiv.org/abs/2412.13211v3

## Overview
High-quality benchmarks are the foundation for embodied AI research, enabling significant advancements in long-horizon navigation, manipulation and rearrangement tasks. However, as frontier tasks in robotics get more advanced, they require faster simulation speed, more intricate test environments, and larger demonstration datasets. To this end, we present MS-HAB, a holistic benchmark for low-level manipulation and in-home object rearrangement. First, we provide a GPU-accelerated implementation of the Home Assistant Benchmark (HAB). We support realistic low-level control and achieve over 3x the speed of prior magical grasp implementations at a fraction of the GPU memory usage. Second, we train extensive reinforcement learning (RL) and imitation learning (IL) baselines for future work to compare against. Finally, we develop a rule-based trajectory filtering system to sample specific demonstrations from our RL policies which match predefined criteria for robot behavior and safety. Combining demonstration filtering with our fast environments enables efficient, controlled data generation at scale.

## Content
High-quality benchmarks are the foundation for embodied AI research, enabling significant advancements in long-horizon navigation, manipulation and rearrangement tasks. However, as frontier tasks in robotics get more advanced, they require faster simulation speed, more intricate test environments, and larger demonstration datasets. To this end, we present MS-HAB, a holistic benchmark for low-level manipulation and in-home object rearrangement. First, we provide a GPU-accelerated implementation of the Home Assistant Benchmark (HAB). We support realistic low-level control and achieve over 3x the speed of prior magical grasp implementations at a fraction of the GPU memory usage. Second, we train extensive reinforcement learning (RL) and imitation learning (IL) baselines for future work to compare against. Finally, we develop a rule-based trajectory filtering system to sample specific demonstrations from our RL policies which match predefined criteria for robot behavior and safety. Combining demonstration filtering with our fast environments enables efficient, controlled data generation at scale.

## 개요
고품질 벤치마크는 체화된 AI 연구의 기초이며, 장기적 탐색, 조작 및 재배치 작업에서 중요한 발전을 가능하게 합니다. 그러나 로봇 공학의 최전선 작업이 더욱 고도화됨에 따라 더 빠른 시뮬레이션 속도, 더 복잡한 테스트 환경, 더 큰 데모 데이터셋이 필요합니다. 이를 위해 우리는 저수준 조작 및 가정 내 물체 재배치를 위한 포괄적인 벤치마크인 MS-HAB을 제시합니다. 첫째, 우리는 Home Assistant Benchmark (HAB)의 GPU 가속 구현을 제공합니다. 현실적인 저수준 제어를 지원하며, 이전의 마법 같은 그립 구현보다 3배 이상 빠른 속도를 GPU 메모리 사용량의 일부로 달성합니다. 둘째, 미래 연구가 비교할 수 있도록 광범위한 강화 학습(RL) 및 모방 학습(IL) 기준선을 훈련합니다. 마지막으로, 로봇 행동 및 안전에 대한 사전 정의된 기준과 일치하는 RL 정책에서 특정 데모를 샘플링하기 위한 규칙 기반 궤적 필터링 시스템을 개발합니다. 데모 필터링을 빠른 환경과 결합함으로써 대규모로 효율적이고 제어된 데이터 생성을 가능하게 합니다.

## 핵심 내용
고품질 벤치마크는 체화된 AI 연구의 기초이며, 장기적 탐색, 조작 및 재배치 작업에서 중요한 발전을 가능하게 합니다. 그러나 로봇 공학의 최전선 작업이 더욱 고도화됨에 따라 더 빠른 시뮬레이션 속도, 더 복잡한 테스트 환경, 더 큰 데모 데이터셋이 필요합니다. 이를 위해 우리는 저수준 조작 및 가정 내 물체 재배치를 위한 포괄적인 벤치마크인 MS-HAB을 제시합니다. 첫째, 우리는 Home Assistant Benchmark (HAB)의 GPU 가속 구현을 제공합니다. 현실적인 저수준 제어를 지원하며, 이전의 마법 같은 그립 구현보다 3배 이상 빠른 속도를 GPU 메모리 사용량의 일부로 달성합니다. 둘째, 미래 연구가 비교할 수 있도록 광범위한 강화 학습(RL) 및 모방 학습(IL) 기준선을 훈련합니다. 마지막으로, 로봇 행동 및 안전에 대한 사전 정의된 기준과 일치하는 RL 정책에서 특정 데모를 샘플링하기 위한 규칙 기반 궤적 필터링 시스템을 개발합니다. 데모 필터링을 빠른 환경과 결합함으로써 대규모로 효율적이고 제어된 데이터 생성을 가능하게 합니다.
