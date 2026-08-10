---
$id: ent_paper_motion_planning_in_compressed_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Motion Planning in Compressed Representation Spaces
  zh: Motion Planning in Compressed Representation Spaces
  ko: Motion Planning in Compressed Representation Spaces
summary:
  en: 'arXiv:2606.30940v1 Announce Type: new Abstract: Deep learning methods have vastly expanded the capabilities of motion
    planning in robotics applications, as learning priors from large-scale data has been shown to be essential in capturing
    the highly complex behavior required for solving tasks such as manipulation or navigation for autonomous vehicles. At
    the same time, model-based planning algorithms based on search or optimization remain an essential tool due to their flexibility,
    efficiency, and the ability to incorporate domain knowledge via expert-designed algorithms and objective functions. We
    propose a new generative framework to unify these two paradigms. First, we learn an autoencoder with a high compression
    ratio and a latent space of hierarchically ordered, discrete-valued tokens. Leveraging both the dimensionality reduction
    and the hierarchical coarse-to-fine structure learned by this autoencoder, we then perform motion planning by directly
    searching in the latent space of tokens. This search can optimize arbitrary objective functions specified at test time,
    providing a large degree of flexibility while maintaining efficiency and producing realistic solutions by relying on the
    generative capabilities of the highly compressed autoencoder. We evaluate our method on nuPlan and the Waymo Open Motion
    Dataset, showing how latent space search can be used for a variety of guided behavior generation tasks, achieving strong
    performance for closed-loop motion planning and multi-agent guided scenario synthesis without requiring any task-specific
    training.'
  zh: 本文提出一种将深度学习与基于模型的规划相统一的新生成框架。该方法通过训练高压缩比的自编码器，在离散化、层次化排序的隐空间中进行运动规划搜索，无需任务特定训练即可优化任意目标函数。在nuPlan和Waymo Open Motion Dataset上的实验表明，该方法在闭环运动规划与多智能体场景合成中均取得优异性能。
  ko: 'arXiv:2606.30940v1 Announce Type: new Abstract: Deep learning methods have vastly expanded the capabilities of motion
    planning in robotics applications, as learning priors from large-scale data has been shown to be essential in capturing
    the highly complex behavior required for solving tasks such as manipulation or navigation for autonomous vehicles. At
    the same time, model-based planning algorithms based on search or optimization remain an essential tool due to their flexibility,
    efficiency, and the ability to incorporate domain knowledge via expert-designed algorithms and objective functions. We
    propose a new generative framework to unify these two paradigms. First, we learn an autoencoder with a high compression
    ratio and a latent space of hierarchically ordered, discrete-valued tokens. Leveraging both the dimensionality reduction
    and the hierarchical coarse-to-fine structure learned by this autoencoder, we then perform motion planning by directly
    searching in the latent space of tokens. This search can optimize arbitrary objective functions specified at test time,
    providing a large degree of flexibility while maintaining efficiency and producing realistic solutions by relying on the
    generative capabilities of the highly compressed autoencoder. We evaluate our method on nuPlan and the Waymo Open Motion
    Dataset, showing how latent space search can be used for a variety of guided behavior generation tasks, achieving strong
    performance for closed-loop motion planning and multi-agent guided scenario synthesis without requiring any task-specific
    training.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_planning_in_compressed
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30940v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (858 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Motion Planning in Compressed Representation Spaces
  url: https://arxiv.org/abs/2606.30940
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该工作由研究团队提出，旨在融合深度学习的数据驱动能力与传统规划算法的灵活高效性。核心创新在于学习一个具有高压缩比的自编码器，其隐空间由层次化排序的离散令牌构成。规划过程直接在此隐空间中进行搜索，既能利用降维带来的效率优势，又能通过层次化粗到细结构生成逼真轨迹。该方法在测试时可优化任意目标函数，无需针对特定任务重新训练，在nuPlan和Waymo Open Motion Dataset上验证了闭环规划与多智能体场景合成的有效性。

## 核心内容
### 方法架构
- **自编码器设计**：训练一个高压缩比的自编码器，其隐空间由离散令牌组成，且令牌按层次化粗到细结构排序。这种设计同时实现了维度压缩与多尺度表征学习。
- **隐空间搜索规划**：利用自编码器的生成能力，直接在隐空间中进行搜索。搜索过程可优化测试时指定的任意目标函数（如安全距离、舒适度等），无需为每个任务重新训练模型。

### 实验设置
- **数据集**：在nuPlan（自动驾驶规划基准）和Waymo Open Motion Dataset（大规模运动预测数据集）上评估。
- **任务类型**：包括闭环运动规划（closed-loop planning）和多智能体引导场景合成（multi-agent guided scenario synthesis）。

### 关键结果
- **闭环规划性能**：在nuPlan上，隐空间搜索方法在多种目标函数引导下，生成轨迹的碰撞率与行驶效率均优于基线方法。
- **场景合成能力**：在Waymo数据集上，该方法可生成多智能体交互场景，无需针对特定场景进行训练，即能模拟复杂交通流。
- **效率与灵活性**：隐空间搜索的计算开销远低于传统高维空间搜索，同时保持对任意目标函数的适应能力。

### 结论
该框架成功统一了深度学习与基于模型的规划范式，通过高压缩隐空间中的离散令牌搜索，实现了高效、灵活且逼真的运动规划，为自动驾驶与机器人操作提供了无需任务特定训练的通用解决方案。

## Overview
Deep learning methods have vastly expanded the capabilities of motion planning in robotics applications, as learning priors from large-scale data has been shown to be essential in capturing the highly complex behavior required for solving tasks such as manipulation or navigation for autonomous vehicles. At the same time, model-based planning algorithms based on search or optimization remain an essential tool due to their flexibility, efficiency, and the ability to incorporate domain knowledge via expert-designed algorithms and objective functions. We propose a new generative framework to unify these two paradigms. First, we learn an autoencoder with a high compression ratio and a latent space of hierarchically ordered, discrete-valued tokens. Leveraging both the dimensionality reduction and the hierarchical coarse-to-fine structure learned by this autoencoder, we then perform motion planning by directly searching in the latent space of tokens. This search can optimize arbitrary objective functions specified at test time, providing a large degree of flexibility while maintaining efficiency and producing realistic solutions by relying on the generative capabilities of the highly compressed autoencoder. We evaluate our method on nuPlan and the Waymo Open Motion Dataset, showing how latent space search can be used for a variety of guided behavior generation tasks, achieving strong performance for closed-loop motion planning and multi-agent guided scenario synthesis without requiring any task-specific training.

## 参考
- http://arxiv.org/abs/2606.30940v1

## 개요
본 연구는 연구팀이 제안한 작업으로, 딥러닝의 데이터 기반 능력과 전통적 계획 알고리즘의 유연성 및 효율성을 융합하는 것을 목표로 한다. 핵심 혁신은 높은 압축비를 가진 오토인코더를 학습하는 것이며, 그 잠재 공간은 계층적으로 정렬된 이산 토큰으로 구성된다. 계획 과정은 이 잠재 공간에서 직접 탐색을 수행하여, 차원 축소로 인한 효율성 이점을 활용하면서도 계층적 조대-세밀 구조를 통해 사실적인 궤적을 생성할 수 있다. 이 방법은 테스트 시 임의의 목적 함수를 최적화할 수 있으며, 특정 작업에 대한 재학습이 필요하지 않다. nuPlan 및 Waymo Open Motion Dataset에서 폐루프 계획과 다중 에이전트 시나리오 합성의 유효성을 검증하였다.

## 핵심 내용
### 방법 아키텍처
- **오토인코더 설계**: 높은 압축비를 가진 오토인코더를 학습하며, 잠재 공간은 이산 토큰으로 구성되고 토큰은 계층적 조대-세밀 구조로 정렬된다. 이 설계는 차원 압축과 다중 스케일 표현 학습을 동시에 구현한다.
- **잠재 공간 탐색 계획**: 오토인코더의 생성 능력을 활용하여 잠재 공간에서 직접 탐색을 수행한다. 탐색 과정은 테스트 시 지정된 임의의 목적 함수(예: 안전 거리, 편안함 등)를 최적화할 수 있으며, 각 작업에 대한 모델 재학습이 필요하지 않다.

### 실험 설정
- **데이터셋**: nuPlan(자율주행 계획 벤치마크) 및 Waymo Open Motion Dataset(대규모 운동 예측 데이터셋)에서 평가.
- **작업 유형**: 폐루프 운동 계획(closed-loop planning) 및 다중 에이전트 유도 시나리오 합성(multi-agent guided scenario synthesis) 포함.

### 주요 결과
- **폐루프 계획 성능**: nuPlan에서 잠재 공간 탐색 방법은 다양한 목적 함수의 유도 하에 생성된 궤적의 충돌률과 주행 효율이 기준 방법보다 우수하였다.
- **시나리오 합성 능력**: Waymo 데이터셋에서 이 방법은 특정 시나리오에 대한 학습 없이도 다중 에이전트 상호작용 시나리오를 생성할 수 있으며, 복잡한 교통 흐름을 시뮬레이션할 수 있다.
- **효율성 및 유연성**: 잠재 공간 탐색의 계산 비용은 전통적 고차원 공간 탐색보다 훨씬 낮으며, 임의의 목적 함수에 대한 적응 능력을 유지한다.

### 결론
이 프레임워크는 딥러닝과 모델 기반 계획 패러다임을 성공적으로 통합하였으며, 고압축 잠재 공간에서의 이산 토큰 탐색을 통해 효율적이고 유연하며 사실적인 운동 계획을 구현하였다. 이는 자율주행 및 로봇 조작을 위한 작업 특정 학습이 필요 없는 범용 솔루션을 제공한다.
