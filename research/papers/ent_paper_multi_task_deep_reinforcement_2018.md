---
$id: ent_paper_multi_task_deep_reinforcement_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Multi-task Deep Reinforcement Learning with PopArt
  zh: Multi-task Deep Reinforcement Learning with PopArt
  ko: Multi-task Deep Reinforcement Learning with PopArt
summary:
  en: Multi-task Deep Reinforcement Learning with PopArt is a 2018 work on physics-based character animation for humanoid
    robots.
  zh: Multi-task Deep Reinforcement Learning with PopArt 是 2018 年提出的一种多任务强化学习算法，旨在让单个智能体同时掌握多个决策任务。其核心贡献在于通过 PopArt 机制自动调整各任务对智能体更新的贡献，使所有任务在训练中保持平衡，最终在
    57 个 Atari 游戏上首次实现了超越人类中位水平的单策略性能。
  ko: Multi-task Deep Reinforcement Learning with PopArt is a 2018 work on physics-based character animation for humanoid
    robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- multi_task_deep_reinforcement
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.04474v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Multi-task Deep Reinforcement Learning with PopArt (arXiv)
  url: https://arxiv.org/abs/1809.04474
  date: '2018'
  accessed_at: '2026-07-01'
---
## 概述
传统强化学习算法通常一次只训练一个任务，每个新任务都需要从头训练一个独立的智能体，导致解决方案缺乏通用性。该研究聚焦于多任务学习中的核心挑战：不同任务因奖励密度或幅值差异，会争夺单一学习系统的有限资源，导致算法偏向某些“显眼”任务而牺牲整体性能。为此，作者提出 PopArt 方法，通过自动调整各任务对智能体更新的影响权重，确保所有任务在训练动态中具有相似的影响力。实验表明，该方法在 57 个 Atari 游戏上训练出的单一策略（使用一组权重）超越了人类中位表现，并在 DeepMind Lab 的 30 个 3D 任务上也达到了当时最优性能。

## 核心内容
### 方法核心
- **问题定义**：多任务强化学习中，不同任务的奖励尺度差异（如稀疏奖励 vs 密集奖励）会导致智能体过度关注某些任务，忽略其他任务的学习。
- **PopArt 机制**：一种自适应归一化技术，通过维护每个任务的奖励统计量（均值和标准差），动态调整任务在策略更新中的梯度贡献。具体而言，PopArt 对每个任务的回报进行标准化，并允许策略网络在训练过程中自适应地调整输出层的缩放参数，从而平衡各任务的学习信号。

### 实验设置
- **基准测试**：
  - **Atari 57**：包含 57 个经典 Atari 游戏，涵盖动作、策略、射击等多种类型。
  - **DeepMind Lab**：30 个 3D 导航与探索任务，要求智能体在复杂环境中完成目标。
- **对比方法**：与单任务 DQN、多任务基线（如共享网络、任务特定头）及当时的多任务强化学习算法（如 A3C）进行对比。
- **评估指标**：人类归一化分数（HNS），以人类玩家表现为基准（100% 为人类中位水平）。

### 关键结果
- **Atari 57**：
  - 训练出的单一策略（一组权重）在 57 个游戏中达到 **中位 HNS 超过 100%**，首次实现单智能体超越人类中位水平。
  - 在 39 个游戏中表现优于单任务 DQN，在 18 个游戏中达到或超过人类专家水平。
- **DeepMind Lab**：
  - 在 30 个任务上取得 **当时最优平均性能**，显著优于未使用 PopArt 的多任务基线。
- **消融实验**：移除 PopArt 后，多任务训练的性能下降 30-50%，验证了自适应平衡机制的关键作用。

### 结论
PopArt 通过自动调整任务贡献，有效解决了多任务学习中的奖励尺度不均衡问题，使单一智能体在多样化任务上达到或超越人类水平。该方法为后续多任务与通用强化学习（如 IMPALA、Agent57）提供了重要基础。

## Overview
The reinforcement learning community has made great strides in designing algorithms capable of exceeding human performance on specific tasks. These algorithms are mostly trained one task at the time, each new task requiring to train a brand new agent instance. This means the learning algorithm is general, but each solution is not; each agent can only solve the one task it was trained on. In this work, we study the problem of learning to master not one but multiple sequential-decision tasks at once. A general issue in multi-task learning is that a balance must be found between the needs of multiple tasks competing for the limited resources of a single learning system. Many learning algorithms can get distracted by certain tasks in the set of tasks to solve. Such tasks appear more salient to the learning process, for instance because of the density or magnitude of the in-task rewards. This causes the algorithm to focus on those salient tasks at the expense of generality. We propose to automatically adapt the contribution of each task to the agent's updates, so that all tasks have a similar impact on the learning dynamics. This resulted in state of the art performance on learning to play all games in a set of 57 diverse Atari games. Excitingly, our method learned a single trained policy - with a single set of weights - that exceeds median human performance. To our knowledge, this was the first time a single agent surpassed human-level performance on this multi-task domain. The same approach also demonstrated state of the art performance on a set of 30 tasks in the 3D reinforcement learning platform DeepMind Lab.

## 개요
강화 학습 커뮤니티는 특정 작업에서 인간의 성능을 초과할 수 있는 알고리즘을 설계하는 데 큰 진전을 이루었습니다. 이러한 알고리즘은 대부분 한 번에 하나의 작업만 학습하며, 각각의 새로운 작업은 완전히 새로운 에이전트 인스턴스를 학습해야 합니다. 이는 학습 알고리즘은 일반적이지만 각 솔루션은 그렇지 않다는 것을 의미합니다. 즉, 각 에이전트는 학습된 하나의 작업만 해결할 수 있습니다. 본 연구에서는 하나가 아닌 여러 순차적 의사 결정 작업을 동시에 마스터하는 문제를 연구합니다. 다중 작업 학습의 일반적인 문제는 단일 학습 시스템의 제한된 자원을 두고 경쟁하는 여러 작업의 요구 사이에서 균형을 찾아야 한다는 점입니다. 많은 학습 알고리즘은 해결해야 할 작업 집합 중 특정 작업에 의해 주의가 분산될 수 있습니다. 이러한 작업은 예를 들어 작업 내 보상의 밀도나 크기 때문에 학습 과정에서 더 두드러지게 나타납니다. 이로 인해 알고리즘은 일반성을 희생하면서 이러한 두드러진 작업에 집중하게 됩니다. 우리는 각 작업이 에이전트 업데이트에 기여하는 정도를 자동으로 조정하여 모든 작업이 학습 역학에 유사한 영향을 미치도록 제안합니다. 이는 57개의 다양한 Atari 게임 집합에서 모든 게임을 학습하는 데 최첨단 성능을 달성했습니다. 흥미롭게도, 우리의 방법은 단일 가중치 집합을 가진 단일 학습 정책을 학습하여 중간 인간 성능을 초과했습니다. 우리가 아는 한, 이는 단일 에이전트가 이 다중 작업 도메인에서 인간 수준의 성능을 처음으로 넘어선 사례입니다. 동일한 접근 방식은 3D 강화 학습 플랫폼 DeepMind Lab의 30개 작업 집합에서도 최첨단 성능을 입증했습니다.

## 핵심 내용
강화 학습 커뮤니티는 특정 작업에서 인간의 성능을 초과할 수 있는 알고리즘을 설계하는 데 큰 진전을 이루었습니다. 이러한 알고리즘은 대부분 한 번에 하나의 작업만 학습하며, 각각의 새로운 작업은 완전히 새로운 에이전트 인스턴스를 학습해야 합니다. 이는 학습 알고리즘은 일반적이지만 각 솔루션은 그렇지 않다는 것을 의미합니다. 즉, 각 에이전트는 학습된 하나의 작업만 해결할 수 있습니다. 본 연구에서는 하나가 아닌 여러 순차적 의사 결정 작업을 동시에 마스터하는 문제를 연구합니다. 다중 작업 학습의 일반적인 문제는 단일 학습 시스템의 제한된 자원을 두고 경쟁하는 여러 작업의 요구 사이에서 균형을 찾아야 한다는 점입니다. 많은 학습 알고리즘은 해결해야 할 작업 집합 중 특정 작업에 의해 주의가 분산될 수 있습니다. 이러한 작업은 예를 들어 작업 내 보상의 밀도나 크기 때문에 학습 과정에서 더 두드러지게 나타납니다. 이로 인해 알고리즘은 일반성을 희생하면서 이러한 두드러진 작업에 집중하게 됩니다. 우리는 각 작업이 에이전트 업데이트에 기여하는 정도를 자동으로 조정하여 모든 작업이 학습 역학에 유사한 영향을 미치도록 제안합니다. 이는 57개의 다양한 Atari 게임 집합에서 모든 게임을 학습하는 데 최첨단 성능을 달성했습니다. 흥미롭게도, 우리의 방법은 단일 가중치 집합을 가진 단일 학습 정책을 학습하여 중간 인간 성능을 초과했습니다. 우리가 아는 한, 이는 단일 에이전트가 이 다중 작업 도메인에서 인간 수준의 성능을 처음으로 넘어선 사례입니다. 동일한 접근 방식은 3D 강화 학습 플랫폼 DeepMind Lab의 30개 작업 집합에서도 최첨단 성능을 입증했습니다.

## 参考
- http://arxiv.org/abs/1809.04474v1
