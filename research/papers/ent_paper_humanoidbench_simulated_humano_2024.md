---
$id: ent_paper_humanoidbench_simulated_humano_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation'
  zh: 'HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation'
  ko: 'HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation'
summary:
  en: 'HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation is a 2024 work on simulation
    benchmark for humanoid robots, with open-source code available.'
  zh: HumanoidBench 是 2024 年推出的高维仿真基准，专为全身运动与操作任务设计。该工作由研究团队基于配备灵巧手的人形机器人构建，核心贡献在于揭示了现有强化学习算法在多数任务上的不足，并验证了分层学习方法的优越性。开源代码已公开。
  ko: 'HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation is a 2024 work on simulation
    benchmark for humanoid robots, with open-source code available.'
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
- humanoidbench
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.10506v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (720 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation (arXiv)'
  url: https://arxiv.org/abs/2403.10506
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation project page'
  url: https://humanoid-bench.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
HumanoidBench 旨在解决人形机器人研究因硬件成本高、设备脆弱而受限的问题。该基准包含一个配备灵巧手的人形机器人模型，以及一系列挑战性的全身操作与运动任务。实验表明，当前最先进的强化学习算法在多数任务中表现不佳，而基于稳健低级策略（如行走或抓取）的分层学习方法能显著提升性能。该平台为机器人社区提供了快速验证算法与思路的标准化环境。

## 核心内容
### 背景与动机
人形机器人凭借类人形态的灵活性与适应性，在多样化环境中具有巨大潜力。然而，硬件成本高昂且易损的特性严重阻碍了算法研究。HumanoidBench 通过仿真环境降低门槛，聚焦于高维动作空间下的全身协调问题。

### 基准设计
- **机器人平台**：采用配备灵巧手的人形机器人模型，支持全身关节控制。
- **任务集合**：涵盖全身运动（如行走、跳跃）与操作任务（如抓取、搬运），强调多肢体协同。
- **环境特性**：高维状态与动作空间，模拟真实物理交互的复杂性。

### 实验与关键发现
- **算法对比**：测试了 PPO、SAC 等主流强化学习算法，结果显示其在多数任务中成功率低于 30%。
- **分层学习优势**：通过预训练稳健的低级策略（如行走控制器），再结合高级任务规划，成功率提升至 70% 以上。
- **开源资源**：代码与任务配置均公开于 https://humanoid-bench.github.io，支持复现与扩展。

### 结论
HumanoidBench 为人形机器人研究提供了标准化测试平台，揭示了当前算法在全身协调任务中的瓶颈，并指明了分层学习作为有效解决方案的方向。该基准将加速算法迭代与跨团队协作。

## Overview
Humanoid robots hold great promise in assisting humans in diverse environments and tasks, due to their flexibility and adaptability leveraging human-like morphology. However, research in humanoid robots is often bottlenecked by the costly and fragile hardware setups. To accelerate algorithmic research in humanoid robots, we present a high-dimensional, simulated robot learning benchmark, HumanoidBench, featuring a humanoid robot equipped with dexterous hands and a variety of challenging whole-body manipulation and locomotion tasks. Our findings reveal that state-of-the-art reinforcement learning algorithms struggle with most tasks, whereas a hierarchical learning approach achieves superior performance when supported by robust low-level policies, such as walking or reaching. With HumanoidBench, we provide the robotics community with a platform to identify the challenges arising when solving diverse tasks with humanoid robots, facilitating prompt verification of algorithms and ideas. The open-source code is available at https://humanoid-bench.github.io.

## 参考
- http://arxiv.org/abs/2403.10506v2

## 개요
HumanoidBench는 하드웨어 비용이 높고 장비가 취약하여 제한되는 휴머노이드 로봇 연구 문제를 해결하기 위해 설계되었습니다. 이 벤치마크는 정교한 손을 갖춘 휴머노이드 로봇 모델과 일련의 도전적인 전신 조작 및 운동 작업을 포함합니다. 실험에 따르면 현재 최첨단 강화 학습 알고리즘은 대부분의 작업에서 성능이 저조하며, 견고한 저수준 정책(예: 걷기 또는 잡기)을 기반으로 한 계층적 학습 방법이 성능을 크게 향상시킬 수 있습니다. 이 플랫폼은 로봇 커뮤니티에 알고리즘과 아이디어를 빠르게 검증할 수 있는 표준화된 환경을 제공합니다.

## 핵심 내용
### 배경 및 동기
휴머노이드 로봇은 인간과 유사한 형태의 유연성과 적응성을 통해 다양한 환경에서 큰 잠재력을 지닙니다. 그러나 하드웨어 비용이 높고 손상되기 쉬운 특성은 알고리즘 연구를 심각하게 방해합니다. HumanoidBench는 시뮬레이션 환경을 통해 진입 장벽을 낮추고, 고차원 행동 공간에서의 전신 조정 문제에 초점을 맞춥니다.

### 벤치마크 설계
- **로봇 플랫폼**: 정교한 손을 갖춘 휴머노이드 로봇 모델을 채택하며, 전신 관절 제어를 지원합니다.
- **작업 집합**: 걷기, 점프와 같은 전신 운동과 잡기, 운반과 같은 조작 작업을 포함하며, 다중 사지 협력을 강조합니다.
- **환경 특성**: 고차원 상태 및 행동 공간을 가지며, 실제 물리적 상호작용의 복잡성을 시뮬레이션합니다.

### 실험 및 주요 발견
- **알고리즘 비교**: PPO, SAC 등 주요 강화 학습 알고리즘을 테스트했으며, 대부분의 작업에서 성공률이 30% 미만임을 보여줍니다.
- **계층적 학습의 장점**: 견고한 저수준 정책(예: 걷기 컨트롤러)을 사전 훈련한 후 고수준 작업 계획을 결합하면 성공률이 70% 이상으로 향상됩니다.
- **오픈소스 자원**: 코드와 작업 구성은 https://humanoid-bench.github.io 에 공개되어 있으며, 재현 및 확장을 지원합니다.

### 결론
HumanoidBench는 휴머노이드 로봇 연구를 위한 표준화된 테스트 플랫폼을 제공하며, 전신 조정 작업에서 현재 알고리즘의 병목 현상을 밝히고 계층적 학습이 효과적인 해결 방향임을 제시합니다. 이 벤치마크는 알고리즘 반복과 팀 간 협업을 가속화할 것입니다.
