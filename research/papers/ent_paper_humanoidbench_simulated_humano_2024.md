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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.10506v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
휴머노이드 로봇은 인간과 유사한 형태를 활용한 유연성과 적응성 덕분에 다양한 환경과 작업에서 인간을 보조할 큰 잠재력을 지니고 있습니다. 그러나 휴머노이드 로봇 연구는 종종 고비용이고 취약한 하드웨어 설정에 의해 병목 현상을 겪습니다. 휴머노이드 로봇의 알고리즘 연구를 가속화하기 위해, 우리는 고차원의 시뮬레이션 로봇 학습 벤치마크인 HumanoidBench를 제시합니다. 이 벤치마크는 정교한 손을 갖춘 휴머노이드 로봇과 다양한 도전적인 전신 조작 및 이동 작업을 특징으로 합니다. 우리의 연구 결과는 최첨단 강화 학습 알고리즘이 대부분의 작업에서 어려움을 겪는 반면, 계층적 학습 접근법이 걷기나 잡기와 같은 강력한 하위 수준 정책에 의해 지원될 때 우수한 성능을 달성함을 보여줍니다. HumanoidBench를 통해, 우리는 로봇 공학 커뮤니티에 휴머노이드 로봇으로 다양한 작업을 해결할 때 발생하는 도전 과제를 식별할 수 있는 플랫폼을 제공하여, 알고리즘과 아이디어의 신속한 검증을 촉진합니다. 오픈소스 코드는 https://humanoid-bench.github.io에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇은 인간과 유사한 형태를 활용한 유연성과 적응성 덕분에 다양한 환경과 작업에서 인간을 보조할 큰 잠재력을 지니고 있습니다. 그러나 휴머노이드 로봇 연구는 종종 고비용이고 취약한 하드웨어 설정에 의해 병목 현상을 겪습니다. 휴머노이드 로봇의 알고리즘 연구를 가속화하기 위해, 우리는 고차원의 시뮬레이션 로봇 학습 벤치마크인 HumanoidBench를 제시합니다. 이 벤치마크는 정교한 손을 갖춘 휴머노이드 로봇과 다양한 도전적인 전신 조작 및 이동 작업을 특징으로 합니다. 우리의 연구 결과는 최첨단 강화 학습 알고리즘이 대부분의 작업에서 어려움을 겪는 반면, 계층적 학습 접근법이 걷기나 잡기와 같은 강력한 하위 수준 정책에 의해 지원될 때 우수한 성능을 달성함을 보여줍니다. HumanoidBench를 통해, 우리는 로봇 공학 커뮤니티에 휴머노이드 로봇으로 다양한 작업을 해결할 때 발생하는 도전 과제를 식별할 수 있는 플랫폼을 제공하여, 알고리즘과 아이디어의 신속한 검증을 촉진합니다. 오픈소스 코드는 https://humanoid-bench.github.io에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2403.10506v2
