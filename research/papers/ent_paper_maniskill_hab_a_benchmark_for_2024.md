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
  zh: ManiSkill-HAB 是 2024 年提出的面向人形机器人的低层级操作与家庭物品重排仿真基准。该工作由研究团队基于 Home Assistant Benchmark (HAB) 开发，核心贡献包括 GPU 加速实现（速度提升超
    3 倍且显存占用更低）、强化学习与模仿学习基线训练，以及基于规则的轨迹过滤系统用于安全数据生成。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.13211v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (687 chars, DeepSeek).'
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
高质量基准是具身 AI 研究的基石，推动了长时程导航、操作与重排任务的显著进步。随着机器人前沿任务日益复杂，对仿真速度、测试环境多样性和大规模演示数据集的需求也随之增加。为此，ManiSkill-HAB 提供了一个全面的低层级操作与家庭物品重排基准。该工作首先对 Home Assistant Benchmark (HAB) 进行了 GPU 加速实现，支持逼真的低层级控制，速度较此前魔法抓取实现提升超 3 倍，且 GPU 内存占用更低。其次，训练了丰富的强化学习与模仿学习基线供后续研究对比。最后，开发了基于规则的轨迹过滤系统，能从 RL 策略中采样符合预设机器人行为与安全标准的特定演示，结合快速环境实现高效可控的大规模数据生成。

## 核心内容
### 背景与动机
高质量基准是具身 AI 研究的基础，推动了长时程导航、操作与重排任务的显著进步。然而，随着机器人前沿任务日益复杂，需要更快的仿真速度、更复杂的测试环境和更大的演示数据集。

### 核心贡献
#### GPU 加速实现
- 对 Home Assistant Benchmark (HAB) 进行 GPU 加速，支持逼真的低层级控制。
- 速度较此前魔法抓取实现提升超 3 倍，且 GPU 内存占用更低。

#### 基线训练
- 训练了广泛的强化学习 (RL) 和模仿学习 (IL) 基线，为未来工作提供对比基准。

#### 轨迹过滤系统
- 开发了基于规则的轨迹过滤系统，能从 RL 策略中采样符合预设机器人行为与安全标准的特定演示。
- 结合快速环境，实现高效可控的大规模数据生成。

## Overview
High-quality benchmarks are the foundation for embodied AI research, enabling significant advancements in long-horizon navigation, manipulation and rearrangement tasks. However, as frontier tasks in robotics get more advanced, they require faster simulation speed, more intricate test environments, and larger demonstration datasets. To this end, we present MS-HAB, a holistic benchmark for low-level manipulation and in-home object rearrangement. First, we provide a GPU-accelerated implementation of the Home Assistant Benchmark (HAB). We support realistic low-level control and achieve over 3x the speed of prior magical grasp implementations at a fraction of the GPU memory usage. Second, we train extensive reinforcement learning (RL) and imitation learning (IL) baselines for future work to compare against. Finally, we develop a rule-based trajectory filtering system to sample specific demonstrations from our RL policies which match predefined criteria for robot behavior and safety. Combining demonstration filtering with our fast environments enables efficient, controlled data generation at scale.

## 参考
- http://arxiv.org/abs/2412.13211v3

## 개요
고품질 벤치마크는 구현 AI 연구의 초석으로, 장시간 내비게이션, 조작 및 재배치 작업의 눈에 띄는 발전을 이끌었습니다. 로봇 최전선 작업이 점점 복잡해짐에 따라 시뮬레이션 속도, 테스트 환경 다양성 및 대규모 데모 데이터셋에 대한 수요도 증가했습니다. 이를 위해 ManiSkill-HAB은 포괄적인 저수준 조작 및 가정용 물품 재배치 벤치마크를 제공합니다. 이 작업은 먼저 Home Assistant Benchmark (HAB)를 GPU 가속 구현하여 사실적인 저수준 제어를 지원하며, 이전 매직 그랩 구현보다 속도가 3배 이상 빠르고 GPU 메모리 사용량도 더 낮습니다. 둘째, 후속 연구 비교를 위한 풍부한 강화 학습 및 모방 학습 베이스라인을 훈련했습니다. 마지막으로, 규칙 기반 궤적 필터링 시스템을 개발하여 RL 정책에서 사전 정의된 로봇 동작 및 안전 기준을 충족하는 특정 데모를 샘플링할 수 있으며, 빠른 환경과 결합하여 효율적이고 제어 가능한 대규모 데이터 생성을 가능하게 합니다.

## 핵심 내용
### 배경 및 동기
고품질 벤치마크는 구현 AI 연구의 기초로, 장시간 내비게이션, 조작 및 재배치 작업의 눈에 띄는 발전을 이끌었습니다. 그러나 로봇 최전선 작업이 점점 복잡해짐에 따라 더 빠른 시뮬레이션 속도, 더 복잡한 테스트 환경 및 더 큰 데모 데이터셋이 필요합니다.

### 핵심 기여
#### GPU 가속 구현
- Home Assistant Benchmark (HAB)를 GPU 가속하여 사실적인 저수준 제어를 지원합니다.
- 이전 매직 그랩 구현보다 속도가 3배 이상 빠르며 GPU 메모리 사용량도 더 낮습니다.

#### 베이스라인 훈련
- 광범위한 강화 학습 (RL) 및 모방 학습 (IL) 베이스라인을 훈련하여 향후 작업에 비교 기준을 제공합니다.

#### 궤적 필터링 시스템
- 규칙 기반 궤적 필터링 시스템을 개발하여 RL 정책에서 사전 정의된 로봇 동작 및 안전 기준을 충족하는 특정 데모를 샘플링할 수 있습니다.
- 빠른 환경과 결합하여 효율적이고 제어 가능한 대규모 데이터 생성을 실현합니다.
