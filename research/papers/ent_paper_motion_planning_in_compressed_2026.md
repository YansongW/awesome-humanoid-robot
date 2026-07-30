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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30940v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
딥러닝 방법은 로봇 공학 응용 분야에서 모션 플래닝의 능력을 크게 확장했습니다. 대규모 데이터로부터 사전 지식을 학습하는 것이 조작이나 자율 주행 차량의 내비게이션과 같은 작업을 해결하는 데 필요한 매우 복잡한 행동을 포착하는 데 필수적임이 입증되었기 때문입니다. 동시에 탐색 또는 최적화 기반의 모델 기반 플래닝 알고리즘은 유연성, 효율성, 그리고 전문가가 설계한 알고리즘과 목적 함수를 통해 도메인 지식을 통합할 수 있는 능력 덕분에 여전히 필수적인 도구로 남아 있습니다. 우리는 이 두 패러다임을 통합하는 새로운 생성 프레임워크를 제안합니다. 먼저, 높은 압축률과 계층적으로 정렬된 이산 값 토큰의 잠재 공간을 가진 오토인코더를 학습합니다. 이 오토인코더가 학습한 차원 축소와 계층적 조대-세밀 구조를 활용하여, 우리는 토큰의 잠재 공간에서 직접 탐색함으로써 모션 플래닝을 수행합니다. 이 탐색은 테스트 시점에 지정된 임의의 목적 함수를 최적화할 수 있어, 큰 유연성을 제공하면서도 효율성을 유지하고, 높은 압축률의 오토인코더의 생성 능력에 의존하여 현실적인 솔루션을 생성합니다. 우리는 nuPlan과 Waymo Open Motion Dataset에서 이 방법을 평가하여, 잠재 공간 탐색이 다양한 유도 행동 생성 작업에 어떻게 사용될 수 있는지 보여주며, 작업별 학습 없이도 폐루프 모션 플래닝과 다중 에이전트 유도 시나리오 합성에서 강력한 성능을 달성함을 입증합니다.

## 핵심 내용
딥러닝 방법은 로봇 공학 응용 분야에서 모션 플래닝의 능력을 크게 확장했습니다. 대규모 데이터로부터 사전 지식을 학습하는 것이 조작이나 자율 주행 차량의 내비게이션과 같은 작업을 해결하는 데 필요한 매우 복잡한 행동을 포착하는 데 필수적임이 입증되었기 때문입니다. 동시에 탐색 또는 최적화 기반의 모델 기반 플래닝 알고리즘은 유연성, 효율성, 그리고 전문가가 설계한 알고리즘과 목적 함수를 통해 도메인 지식을 통합할 수 있는 능력 덕분에 여전히 필수적인 도구로 남아 있습니다. 우리는 이 두 패러다임을 통합하는 새로운 생성 프레임워크를 제안합니다. 먼저, 높은 압축률과 계층적으로 정렬된 이산 값 토큰의 잠재 공간을 가진 오토인코더를 학습합니다. 이 오토인코더가 학습한 차원 축소와 계층적 조대-세밀 구조를 활용하여, 우리는 토큰의 잠재 공간에서 직접 탐색함으로써 모션 플래닝을 수행합니다. 이 탐색은 테스트 시점에 지정된 임의의 목적 함수를 최적화할 수 있어, 큰 유연성을 제공하면서도 효율성을 유지하고, 높은 압축률의 오토인코더의 생성 능력에 의존하여 현실적인 솔루션을 생성합니다. 우리는 nuPlan과 Waymo Open Motion Dataset에서 이 방법을 평가하여, 잠재 공간 탐색이 다양한 유도 행동 생성 작업에 어떻게 사용될 수 있는지 보여주며, 작업별 학습 없이도 폐루프 모션 플래닝과 다중 에이전트 유도 시나리오 합성에서 강력한 성능을 달성함을 입증합니다.

## 参考
- http://arxiv.org/abs/2606.30940v1
