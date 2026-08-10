---
$id: ent_paper_ai_towards_embodiment_scaling_law_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Embodiment Scaling Laws in Robot Locomotion
  zh: 机器人运动中的具身规模定律研究
  ko: 로봇 보행에서의 구현체 스케일링 법칙을 향하여
summary:
  en: Investigates embodiment scaling laws by training a single URMA policy on approximately 1,000 procedurally generated
    robot morphologies (GENBOT-1K), demonstrating zero-shot transfer to unseen simulated and real robots including the Unitree
    Go2 and H1.
  zh: 本文研究机器人运动中的具身缩放定律，通过训练单一URMA策略在约1000个程序化生成的机器人形态（GENBOT-1K）上，验证了增加训练形态数量可提升对未见形态的泛化能力。该策略实现了零样本迁移至未见过的模拟与真实机器人，包括Unitree
    Go2和H1。
  ko: 약 1,000개의 절차적 생성 로봇 형태(GENBOT-1K)로 단일 URMA 정책을 훈련하여 구현체 스케일링 법칙을 연구하고, Unitree Go2 및 H1을 포함한 새로운 시뮬레이션 및 실제 로봇으로의 제로샷
    전이를 보인다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- cross_embodiment_generalization
- embodiment_scaling_laws
- locomotion
- reinforcement_learning
- behavior_cloning
- sim_to_real
- urma
- genbot_1k
- procedural_generation
- unitree_h1
- unitree_go2
- robot_morphology
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.05753v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (827 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Towards Embodiment Scaling Laws in Robot Locomotion
  url: https://arxiv.org/abs/2505.05753
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
跨具身泛化是实现通用具身智能体的关键，但其影响因素尚不明确。本文以机器人运动为测试平台，系统研究了具身缩放定律，即增加训练形态数量能否提升对未见形态的泛化能力。研究者程序化生成了约1000个具有拓扑、几何和关节级运动学差异的形态，并在随机子集上训练策略。实验观察到支持该假设的正向缩放趋势，并发现具身缩放比固定形态上的数据缩放能带来更广泛的泛化。基于完整数据集训练的最佳策略，在模拟和真实世界中均能零样本迁移至新形态，包括Unitree Go2和H1。

## 核心内容
### 方法
- 采用**URMA**（Unified Robot Morphology Architecture）作为策略架构，支持处理不同形态的机器人。
- 程序化生成**GENBOT-1K**数据集，包含约1000个形态，涵盖拓扑、几何和关节运动学变化。
- 训练策略时，从GENBOT-1K中随机抽取不同大小的子集，以评估具身数量对泛化的影响。

### 实验设置
- 在模拟环境中训练策略，使用强化学习（RL）进行运动任务。
- 测试泛化能力时，评估策略在未见过的模拟形态上的表现，并直接部署到真实机器人（Unitree Go2和H1）上，无需额外微调。

### 关键结果
- **正向缩放趋势**：随着训练形态数量的增加，策略对未见形态的泛化性能持续提升，支持具身缩放定律假设。
- **具身缩放 vs. 数据缩放**：在固定形态上增加数据量（数据缩放）带来的泛化提升有限，而增加形态数量（具身缩放）能实现更广泛的泛化。
- **零样本迁移**：基于完整GENBOT-1K训练的策略，在模拟中成功迁移至多种新形态，并在真实机器人Unitree Go2和H1上实现零样本运动控制。

### 结论
- 具身缩放定律为构建通用具身智能体提供了重要指导，表明训练形态的多样性是关键因素。
- 该方法对可配置机器人的自适应控制、形态协同设计等领域具有潜在应用价值。

## Overview
Cross-embodiment generalization underpins the vision of building generalist embodied agents for any robot, yet its enabling factors remain poorly understood. We investigate embodiment scaling laws, the hypothesis that increasing the number of training embodiments improves generalization to unseen ones, using robot locomotion as a test bed. We procedurally generate ~1,000 embodiments with topological, geometric, and joint-level kinematic variations, and train policies on random subsets. We observe positive scaling trends supporting the hypothesis, and find that embodiment scaling enables substantially broader generalization than data scaling on fixed embodiments. Our best policy, trained on the full dataset, transfers zero-shot to novel embodiments in simulation and the real world, including the Unitree Go2 and H1. These results represent a step toward general embodied intelligence, with relevance to adaptive control for configurable robots, morphology co-design, and beyond.

## 参考
- http://arxiv.org/abs/2505.05753v2

## 개요
교차 형태 일반화는 범용 임베디드 에이전트를 구현하는 핵심이지만, 그 영향 요인은 아직 명확하지 않습니다. 본 논문은 로봇 운동을 테스트 플랫폼으로 삼아, 훈련 형태 수를 늘리면 보지 못한 형태에 대한 일반화 능력이 향상되는지, 즉 임베디드 스케일링 법칙을 체계적으로 연구합니다. 연구진은 토폴로지, 기하학, 관절 수준 운동학적 차이를 가진 약 1000개의 형태를 프로그램 방식으로 생성하고, 무작위 하위 집합에서 정책을 훈련했습니다. 실험을 통해 이 가설을 지지하는 긍정적 스케일링 추세를 관찰했으며, 임베디드 스케일링이 고정 형태에서의 데이터 스케일링보다 더 광범위한 일반화를 가져온다는 것을 발견했습니다. 전체 데이터 세트로 훈련된 최적 정책은 시뮬레이션과 실제 세계 모두에서 Unitree Go2 및 H1을 포함한 새로운 형태로 제로샷 전이가 가능했습니다.

## 핵심 내용
### 방법
- **URMA**(Unified Robot Morphology Architecture)를 정책 아키텍처로 채택하여 다양한 형태의 로봇을 처리할 수 있도록 지원합니다.
- **GENBOT-1K** 데이터 세트를 프로그램 방식으로 생성하며, 토폴로지, 기하학, 관절 운동학적 변화를 포함한 약 1000개의 형태를 포함합니다.
- 정책 훈련 시 GENBOT-1K에서 다양한 크기의 하위 집합을 무작위로 추출하여 임베디드 수가 일반화에 미치는 영향을 평가합니다.

### 실험 설정
- 시뮬레이션 환경에서 정책을 훈련하고, 강화 학습(RL)을 사용하여 운동 작업을 수행합니다.
- 일반화 능력을 테스트할 때, 보지 못한 시뮬레이션 형태에서 정책의 성능을 평가하고, 추가 미세 조정 없이 실제 로봇(Unitree Go2 및 H1)에 직접 배포합니다.

### 핵심 결과
- **긍정적 스케일링 추세**: 훈련 형태 수가 증가함에 따라 보지 못한 형태에 대한 정책의 일반화 성능이 지속적으로 향상되어 임베디드 스케일링 법칙 가설을 지지합니다.
- **임베디드 스케일링 vs. 데이터 스케일링**: 고정 형태에서 데이터 양을 늘리는 것(데이터 스케일링)은 일반화 향상이 제한적인 반면, 형태 수를 늘리는 것(임베디드 스케일링)은 더 광범위한 일반화를 달성할 수 있습니다.
- **제로샷 전이**: 전체 GENBOT-1K로 훈련된 정책은 시뮬레이션에서 다양한 새로운 형태로 성공적으로 전이되며, 실제 로봇 Unitree Go2 및 H1에서 제로샷 운동 제어를 구현합니다.

### 결론
- 임베디드 스케일링 법칙은 범용 임베디드 에이전트 구축에 중요한 지침을 제공하며, 훈련 형태의 다양성이 핵심 요소임을 시사합니다.
- 본 방법은 구성 가능한 로봇의 적응형 제어, 형태 공동 설계 등의 분야에서 잠재적 응용 가치를 지닙니다.
