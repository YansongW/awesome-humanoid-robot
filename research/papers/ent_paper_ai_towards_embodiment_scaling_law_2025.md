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
  zh: 通过在大约1000个程序生成的机器人形态（GENBOT-1K）上训练单一URMA策略，研究具身规模定律，并展示对包括宇树Go2和H1在内的全新仿真与真实机器人的零样本迁移。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.05753v2.
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
Cross-embodiment generalization underpins the vision of building generalist embodied agents for any robot, yet its enabling factors remain poorly understood. We investigate embodiment scaling laws, the hypothesis that increasing the number of training embodiments improves generalization to unseen ones, using robot locomotion as a test bed. We procedurally generate ~1,000 embodiments with topological, geometric, and joint-level kinematic variations, and train policies on random subsets. We observe positive scaling trends supporting the hypothesis, and find that embodiment scaling enables substantially broader generalization than data scaling on fixed embodiments. Our best policy, trained on the full dataset, transfers zero-shot to novel embodiments in simulation and the real world, including the Unitree Go2 and H1. These results represent a step toward general embodied intelligence, with relevance to adaptive control for configurable robots, morphology co-design, and beyond.

## 核心内容
Cross-embodiment generalization underpins the vision of building generalist embodied agents for any robot, yet its enabling factors remain poorly understood. We investigate embodiment scaling laws, the hypothesis that increasing the number of training embodiments improves generalization to unseen ones, using robot locomotion as a test bed. We procedurally generate ~1,000 embodiments with topological, geometric, and joint-level kinematic variations, and train policies on random subsets. We observe positive scaling trends supporting the hypothesis, and find that embodiment scaling enables substantially broader generalization than data scaling on fixed embodiments. Our best policy, trained on the full dataset, transfers zero-shot to novel embodiments in simulation and the real world, including the Unitree Go2 and H1. These results represent a step toward general embodied intelligence, with relevance to adaptive control for configurable robots, morphology co-design, and beyond.

## 参考
- http://arxiv.org/abs/2505.05753v2

## Overview
Cross-embodiment generalization underpins the vision of building generalist embodied agents for any robot, yet its enabling factors remain poorly understood. We investigate embodiment scaling laws, the hypothesis that increasing the number of training embodiments improves generalization to unseen ones, using robot locomotion as a test bed. We procedurally generate ~1,000 embodiments with topological, geometric, and joint-level kinematic variations, and train policies on random subsets. We observe positive scaling trends supporting the hypothesis, and find that embodiment scaling enables substantially broader generalization than data scaling on fixed embodiments. Our best policy, trained on the full dataset, transfers zero-shot to novel embodiments in simulation and the real world, including the Unitree Go2 and H1. These results represent a step toward general embodied intelligence, with relevance to adaptive control for configurable robots, morphology co-design, and beyond.

## Content
Cross-embodiment generalization underpins the vision of building generalist embodied agents for any robot, yet its enabling factors remain poorly understood. We investigate embodiment scaling laws, the hypothesis that increasing the number of training embodiments improves generalization to unseen ones, using robot locomotion as a test bed. We procedurally generate ~1,000 embodiments with topological, geometric, and joint-level kinematic variations, and train policies on random subsets. We observe positive scaling trends supporting the hypothesis, and find that embodiment scaling enables substantially broader generalization than data scaling on fixed embodiments. Our best policy, trained on the full dataset, transfers zero-shot to novel embodiments in simulation and the real world, including the Unitree Go2 and H1. These results represent a step toward general embodied intelligence, with relevance to adaptive control for configurable robots, morphology co-design, and beyond.

## 개요
교차 체현 일반화는 모든 로봇을 위한 범용 체현 에이전트를 구축하려는 비전의 기초를 이루지만, 이를 가능하게 하는 요인은 아직 잘 이해되지 않고 있습니다. 우리는 로봇 보행을 테스트베드로 삼아, 훈련 체현의 수를 늘리면 보지 못한 체현에 대한 일반화가 향상된다는 가설인 체현 스케일링 법칙을 조사합니다. 우리는 위상적, 기하학적, 관절 수준의 운동학적 변형을 가진 약 1,000개의 체현을 절차적으로 생성하고, 무작위 부분 집합에 대해 정책을 훈련합니다. 우리는 가설을 지지하는 긍정적인 스케일링 추세를 관찰했으며, 체현 스케일링이 고정된 체현에서의 데이터 스케일링보다 훨씬 더 광범위한 일반화를 가능하게 한다는 것을 발견했습니다. 전체 데이터셋으로 훈련된 최고의 정책은 시뮬레이션과 실제 세계에서 Unitree Go2 및 H1을 포함한 새로운 체현으로 제로샷 전이됩니다. 이러한 결과는 구성 가능한 로봇을 위한 적응 제어, 형태 공동 설계 등과 관련된 일반 체현 지능을 향한 한 걸음을 나타냅니다.

## 핵심 내용
교차 체현 일반화는 모든 로봇을 위한 범용 체현 에이전트를 구축하려는 비전의 기초를 이루지만, 이를 가능하게 하는 요인은 아직 잘 이해되지 않고 있습니다. 우리는 로봇 보행을 테스트베드로 삼아, 훈련 체현의 수를 늘리면 보지 못한 체현에 대한 일반화가 향상된다는 가설인 체현 스케일링 법칙을 조사합니다. 우리는 위상적, 기하학적, 관절 수준의 운동학적 변형을 가진 약 1,000개의 체현을 절차적으로 생성하고, 무작위 부분 집합에 대해 정책을 훈련합니다. 우리는 가설을 지지하는 긍정적인 스케일링 추세를 관찰했으며, 체현 스케일링이 고정된 체현에서의 데이터 스케일링보다 훨씬 더 광범위한 일반화를 가능하게 한다는 것을 발견했습니다. 전체 데이터셋으로 훈련된 최고의 정책은 시뮬레이션과 실제 세계에서 Unitree Go2 및 H1을 포함한 새로운 체현으로 제로샷 전이됩니다. 이러한 결과는 구성 가능한 로봇을 위한 적응 제어, 형태 공동 설계 등과 관련된 일반 체현 지능을 향한 한 걸음을 나타냅니다.
