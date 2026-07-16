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
  zh: Multi-task Deep Reinforcement Learning with PopArt is a 2018 work on physics-based character animation for humanoid
    robots.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.04474v1.
sources:
- id: src_001
  type: paper
  title: Multi-task Deep Reinforcement Learning with PopArt (arXiv)
  url: https://arxiv.org/abs/1809.04474
  date: '2018'
  accessed_at: '2026-07-01'
---
## 概述
The reinforcement learning community has made great strides in designing algorithms capable of exceeding human performance on specific tasks. These algorithms are mostly trained one task at the time, each new task requiring to train a brand new agent instance. This means the learning algorithm is general, but each solution is not; each agent can only solve the one task it was trained on. In this work, we study the problem of learning to master not one but multiple sequential-decision tasks at once. A general issue in multi-task learning is that a balance must be found between the needs of multiple tasks competing for the limited resources of a single learning system. Many learning algorithms can get distracted by certain tasks in the set of tasks to solve. Such tasks appear more salient to the learning process, for instance because of the density or magnitude of the in-task rewards. This causes the algorithm to focus on those salient tasks at the expense of generality. We propose to automatically adapt the contribution of each task to the agent's updates, so that all tasks have a similar impact on the learning dynamics. This resulted in state of the art performance on learning to play all games in a set of 57 diverse Atari games. Excitingly, our method learned a single trained policy - with a single set of weights - that exceeds median human performance. To our knowledge, this was the first time a single agent surpassed human-level performance on this multi-task domain. The same approach also demonstrated state of the art performance on a set of 30 tasks in the 3D reinforcement learning platform DeepMind Lab.

## 核心内容
The reinforcement learning community has made great strides in designing algorithms capable of exceeding human performance on specific tasks. These algorithms are mostly trained one task at the time, each new task requiring to train a brand new agent instance. This means the learning algorithm is general, but each solution is not; each agent can only solve the one task it was trained on. In this work, we study the problem of learning to master not one but multiple sequential-decision tasks at once. A general issue in multi-task learning is that a balance must be found between the needs of multiple tasks competing for the limited resources of a single learning system. Many learning algorithms can get distracted by certain tasks in the set of tasks to solve. Such tasks appear more salient to the learning process, for instance because of the density or magnitude of the in-task rewards. This causes the algorithm to focus on those salient tasks at the expense of generality. We propose to automatically adapt the contribution of each task to the agent's updates, so that all tasks have a similar impact on the learning dynamics. This resulted in state of the art performance on learning to play all games in a set of 57 diverse Atari games. Excitingly, our method learned a single trained policy - with a single set of weights - that exceeds median human performance. To our knowledge, this was the first time a single agent surpassed human-level performance on this multi-task domain. The same approach also demonstrated state of the art performance on a set of 30 tasks in the 3D reinforcement learning platform DeepMind Lab.

## 参考
- http://arxiv.org/abs/1809.04474v1

## Overview
The reinforcement learning community has made great strides in designing algorithms capable of exceeding human performance on specific tasks. These algorithms are mostly trained one task at the time, each new task requiring to train a brand new agent instance. This means the learning algorithm is general, but each solution is not; each agent can only solve the one task it was trained on. In this work, we study the problem of learning to master not one but multiple sequential-decision tasks at once. A general issue in multi-task learning is that a balance must be found between the needs of multiple tasks competing for the limited resources of a single learning system. Many learning algorithms can get distracted by certain tasks in the set of tasks to solve. Such tasks appear more salient to the learning process, for instance because of the density or magnitude of the in-task rewards. This causes the algorithm to focus on those salient tasks at the expense of generality. We propose to automatically adapt the contribution of each task to the agent's updates, so that all tasks have a similar impact on the learning dynamics. This resulted in state of the art performance on learning to play all games in a set of 57 diverse Atari games. Excitingly, our method learned a single trained policy - with a single set of weights - that exceeds median human performance. To our knowledge, this was the first time a single agent surpassed human-level performance on this multi-task domain. The same approach also demonstrated state of the art performance on a set of 30 tasks in the 3D reinforcement learning platform DeepMind Lab.

## Content
The reinforcement learning community has made great strides in designing algorithms capable of exceeding human performance on specific tasks. These algorithms are mostly trained one task at the time, each new task requiring to train a brand new agent instance. This means the learning algorithm is general, but each solution is not; each agent can only solve the one task it was trained on. In this work, we study the problem of learning to master not one but multiple sequential-decision tasks at once. A general issue in multi-task learning is that a balance must be found between the needs of multiple tasks competing for the limited resources of a single learning system. Many learning algorithms can get distracted by certain tasks in the set of tasks to solve. Such tasks appear more salient to the learning process, for instance because of the density or magnitude of the in-task rewards. This causes the algorithm to focus on those salient tasks at the expense of generality. We propose to automatically adapt the contribution of each task to the agent's updates, so that all tasks have a similar impact on the learning dynamics. This resulted in state of the art performance on learning to play all games in a set of 57 diverse Atari games. Excitingly, our method learned a single trained policy - with a single set of weights - that exceeds median human performance. To our knowledge, this was the first time a single agent surpassed human-level performance on this multi-task domain. The same approach also demonstrated state of the art performance on a set of 30 tasks in the 3D reinforcement learning platform DeepMind Lab.

## 개요
강화 학습 커뮤니티는 특정 작업에서 인간의 성능을 초과할 수 있는 알고리즘을 설계하는 데 큰 진전을 이루었습니다. 이러한 알고리즘은 대부분 한 번에 하나의 작업만 학습하며, 각각의 새로운 작업은 완전히 새로운 에이전트 인스턴스를 학습해야 합니다. 이는 학습 알고리즘은 일반적이지만 각 솔루션은 그렇지 않다는 것을 의미합니다. 즉, 각 에이전트는 학습된 하나의 작업만 해결할 수 있습니다. 본 연구에서는 하나가 아닌 여러 순차적 의사 결정 작업을 동시에 마스터하는 문제를 연구합니다. 다중 작업 학습의 일반적인 문제는 단일 학습 시스템의 제한된 자원을 두고 경쟁하는 여러 작업의 요구 사이에서 균형을 찾아야 한다는 점입니다. 많은 학습 알고리즘은 해결해야 할 작업 집합 중 특정 작업에 의해 주의가 분산될 수 있습니다. 이러한 작업은 예를 들어 작업 내 보상의 밀도나 크기 때문에 학습 과정에서 더 두드러지게 나타납니다. 이로 인해 알고리즘은 일반성을 희생하면서 이러한 두드러진 작업에 집중하게 됩니다. 우리는 각 작업이 에이전트 업데이트에 기여하는 정도를 자동으로 조정하여 모든 작업이 학습 역학에 유사한 영향을 미치도록 제안합니다. 이는 57개의 다양한 Atari 게임 집합에서 모든 게임을 학습하는 데 최첨단 성능을 달성했습니다. 흥미롭게도, 우리의 방법은 단일 가중치 집합을 가진 단일 학습 정책을 학습하여 중간 인간 성능을 초과했습니다. 우리가 아는 한, 이는 단일 에이전트가 이 다중 작업 도메인에서 인간 수준의 성능을 처음으로 넘어선 사례입니다. 동일한 접근 방식은 3D 강화 학습 플랫폼 DeepMind Lab의 30개 작업 집합에서도 최첨단 성능을 입증했습니다.

## 핵심 내용
강화 학습 커뮤니티는 특정 작업에서 인간의 성능을 초과할 수 있는 알고리즘을 설계하는 데 큰 진전을 이루었습니다. 이러한 알고리즘은 대부분 한 번에 하나의 작업만 학습하며, 각각의 새로운 작업은 완전히 새로운 에이전트 인스턴스를 학습해야 합니다. 이는 학습 알고리즘은 일반적이지만 각 솔루션은 그렇지 않다는 것을 의미합니다. 즉, 각 에이전트는 학습된 하나의 작업만 해결할 수 있습니다. 본 연구에서는 하나가 아닌 여러 순차적 의사 결정 작업을 동시에 마스터하는 문제를 연구합니다. 다중 작업 학습의 일반적인 문제는 단일 학습 시스템의 제한된 자원을 두고 경쟁하는 여러 작업의 요구 사이에서 균형을 찾아야 한다는 점입니다. 많은 학습 알고리즘은 해결해야 할 작업 집합 중 특정 작업에 의해 주의가 분산될 수 있습니다. 이러한 작업은 예를 들어 작업 내 보상의 밀도나 크기 때문에 학습 과정에서 더 두드러지게 나타납니다. 이로 인해 알고리즘은 일반성을 희생하면서 이러한 두드러진 작업에 집중하게 됩니다. 우리는 각 작업이 에이전트 업데이트에 기여하는 정도를 자동으로 조정하여 모든 작업이 학습 역학에 유사한 영향을 미치도록 제안합니다. 이는 57개의 다양한 Atari 게임 집합에서 모든 게임을 학습하는 데 최첨단 성능을 달성했습니다. 흥미롭게도, 우리의 방법은 단일 가중치 집합을 가진 단일 학습 정책을 학습하여 중간 인간 성능을 초과했습니다. 우리가 아는 한, 이는 단일 에이전트가 이 다중 작업 도메인에서 인간 수준의 성능을 처음으로 넘어선 사례입니다. 동일한 접근 방식은 3D 강화 학습 플랫폼 DeepMind Lab의 30개 작업 집합에서도 최첨단 성능을 입증했습니다.
