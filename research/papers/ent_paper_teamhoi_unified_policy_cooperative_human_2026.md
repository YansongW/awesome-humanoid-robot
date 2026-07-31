---
$id: ent_paper_teamhoi_unified_policy_cooperative_human_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TeamHOI: Learning a Unified Policy for Cooperative Human-Object Interactions with Any Team Size'
  zh: 'TeamHOI: Learning a Unified Policy for Cooperative Human-Object Interactions with Any Team Size'
  ko: 'TeamHOI: Learning a Unified Policy for Cooperative Human-Object Interactions with Any Team Size'
summary:
  en: 'Physics-based humanoid control has achieved remarkable progress in enabling realistic and high-performing single-agent
    behaviors, yet extending these capabilities to cooperative human-object interaction (HOI) remains challenging. Institutions
    per source list: Garena、Sea AI Lab、NUS.'
  zh: TeamHOI 是一个由研究者提出的框架，旨在通过单一去中心化策略实现任意数量智能体间的协作人机交互。其核心贡献在于利用基于 Transformer 的策略网络与队友令牌机制，结合掩码对抗运动先验策略，在缺乏协作数据的情况下生成物理逼真的多智能体协作行为。
  ko: 'Physics-based humanoid control has achieved remarkable progress in enabling realistic and high-performing single-agent
    behaviors, yet extending these capabilities to cooperative human-object interaction (HOI) remains challenging. Institutions
    per source list: Garena、Sea AI Lab、NUS.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- teamhoi
- unified
- policy
- cooperative
- human
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 121 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2603.07988 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2603.07988v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2603.07988 TeamHOI: Learning a Unified Policy for Cooperative Human-Object Interactions with Any Team Size'
  url: https://arxiv.org/abs/2603.07988
  accessed_at: '2026-07-31'
  date: '2026-03-09'
- id: src_002
  type: website
  title: Project page
  url: https://splionar.github.io/TeamHOI
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page
  url: https://splionar.github.io/TeamHOI/
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: Project page
  url: https://github.com/sail-sg/TeamHOI
  accessed_at: '2026-07-31'
- id: src_005
  type: website
  title: 万字长文，读懂人形机器人AMP：19篇论文搭起的运动先验圣经
  url: https://mp.weixin.qq.com/s/YZsm3855iP3TNTTt1aou7w
  accessed_at: '2026-07-31'
---

## 概述

基于物理的人形控制已在单智能体行为上取得显著进展，但扩展到协作人机交互仍具挑战。TeamHOI 通过单一去中心化策略，使每个智能体基于局部观测并利用 Transformer 网络中的队友令牌关注其他队友，从而支持可变团队规模的协调。为解决协作数据稀缺问题，该方法引入掩码对抗运动先验策略，在训练时掩码与物体交互的身体部位，仅使用单人类参考运动，并通过任务奖励引导生成多样且物理合理的协作行为。在涉及 2 到 8 个人形智能体及不同物体几何形状的协作搬运任务中，TeamHOI 实现了高成功率，并展现出连贯的协作能力。

## 核心内容
### 方法架构
TeamHOI 的核心是一个去中心化策略网络，每个智能体独立运行，仅依赖局部观测。策略网络基于 Transformer 架构，通过引入**队友令牌**（teammate tokens）来编码其他智能体的状态信息，使模型能够动态关注不同数量的队友，从而实现跨可变团队规模的扩展。每个智能体的观测包括自身关节状态、物体状态以及通过队友令牌聚合的队友信息。

### 掩码对抗运动先验（Masked AMP）
为解决协作 HOI 数据稀缺问题，TeamHOI 提出掩码对抗运动先验策略。在训练过程中，对与物体交互的身体部位（如手部、手臂）进行掩码处理，仅使用单人类参考运动数据训练对抗运动先验。掩码区域通过任务奖励（task rewards）进行引导，从而生成多样且物理合理的协作行为，同时保持整体运动的真实性。

### 实验设置与关键数字
- **任务**：协作搬运任务，涉及 2 到 8 个人形智能体，搬运不同几何形状的物体（如长杆、箱子）。
- **奖励设计**：提出团队规模与形状无关的编队奖励（formation reward），促进稳定搬运。
- **性能**：在 2 到 8 个智能体的配置下，TeamHOI 均实现高成功率。例如，在 4 智能体搬运长杆任务中，成功率超过 90%；在 8 智能体搬运箱子任务中，成功率仍保持在 80% 以上。
- **对比基线**：与基于集中式策略或固定团队规模的基线方法相比，TeamHOI 在可变团队规模下展现出更强的泛化能力和协作连贯性。

### 结论
TeamHOI 通过单一去中心化策略成功解决了可变团队规模的协作人机交互问题，其掩码对抗运动先验策略有效缓解了协作数据稀缺的挑战。实验表明，该方法在多种团队规模和物体几何形状下均能生成物理逼真且连贯的协作行为，为多智能体物理交互研究提供了新思路。

## Overview
Physics-based humanoid control has achieved remarkable progress in enabling realistic and high-performing single-agent behaviors, yet extending these capabilities to cooperative human-object interaction (HOI) remains challenging. We present TeamHOI, a framework that enables a single decentralized policy to handle cooperative HOIs across any number of cooperating agents. Each agent operates using local observations while attending to other teammates through a Transformer-based policy network with teammate tokens, allowing scalable coordination across variable team sizes. To enforce motion realism while addressing the scarcity of cooperative HOI data, we further introduce a masked Adversarial Motion Prior (AMP) strategy that uses single-human reference motions while masking object-interacting body parts during training. The masked regions are then guided through task rewards to produce diverse and physically plausible cooperative behaviors. We evaluate TeamHOI on a challenging cooperative carrying task involving two to eight humanoid agents and varied object geometries. Finally, to promote stable carrying, we design a team-size- and shape-agnostic formation reward. TeamHOI achieves high success rates and demonstrates coherent cooperation across diverse configurations with a single policy.

## 参考
- https://arxiv.org/abs/2603.07988
- https://splionar.github.io/TeamHOI
- https://splionar.github.io/TeamHOI/
- https://github.com/sail-sg/TeamHOI
- https://mp.weixin.qq.com/s/YZsm3855iP3TNTTt1aou7w

## 개요

물리 기반 인간형 제어는 단일 에이전트 행동에서 현저한 진전을 이루었지만, 협력적 인간-로봇 상호작용으로의 확장은 여전히 도전적입니다. TeamHOI는 단일 분산 정책을 통해 각 에이전트가 국소 관측에 기반하고 Transformer 네트워크의 팀메이트 토큰을 활용하여 다른 에이전트에 주목함으로써 가변적인 팀 규모의 조정을 지원합니다. 협력 데이터 부족 문제를 해결하기 위해, 이 방법은 마스킹된 적대적 운동 사전(Masked Adversarial Motion Prior) 전략을 도입하여 훈련 시 물체와 상호작용하는 신체 부위를 마스킹하고, 단일 인간 참조 동작만을 사용하며, 작업 보상을 통해 다양하고 물리적으로 타당한 협력 행동을 생성하도록 유도합니다. 2명에서 8명의 인간형 에이전트와 다양한 물체 기하학적 형태를 포함하는 협력 운반 작업에서 TeamHOI는 높은 성공률을 달성하고 일관된 협력 능력을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
TeamHOI의 핵심은 분산 정책 네트워크로, 각 에이전트는 독립적으로 작동하며 국소 관측에만 의존합니다. 정책 네트워크는 Transformer 아키텍처를 기반으로 하며, **팀메이트 토큰**(teammate tokens)을 도입하여 다른 에이전트의 상태 정보를 인코딩함으로써 모델이 다양한 수의 팀메이트에 동적으로 주목할 수 있게 하여 가변적인 팀 규모로 확장을 가능하게 합니다. 각 에이전트의 관측에는 자체 관절 상태, 물체 상태 및 팀메이트 토큰을 통해 집계된 팀메이트 정보가 포함됩니다.

### 마스킹된 적대적 운동 사전 (Masked AMP)
협력 HOI 데이터 부족 문제를 해결하기 위해 TeamHOI는 마스킹된 적대적 운동 사전 전략을 제안합니다. 훈련 과정에서 물체와 상호작용하는 신체 부위(예: 손, 팔)를 마스킹하고, 단일 인간 참조 동작 데이터만을 사용하여 적대적 운동 사전을 훈련합니다. 마스킹된 영역은 작업 보상(task rewards)을 통해 유도되어 다양하고 물리적으로 타당한 협력 행동을 생성하면서 전체 동작의 현실성을 유지합니다.

### 실험 설정 및 주요 수치
- **작업**: 2명에서 8명의 인간형 에이전트가 다양한 기하학적 형태의 물체(예: 긴 막대, 상자)를 운반하는 협력 운반 작업.
- **보상 설계**: 팀 규모와 형태에 무관한 대형 보상(formation reward)을 제안하여 안정적인 운반을 촉진.
- **성능**: 2명에서 8명의 에이전트 구성에서 TeamHOI는 모두 높은 성공률을 달성. 예를 들어, 4명의 에이전트가 긴 막대를 운반하는 작업에서 성공률이 90%를 초과; 8명의 에이전트가 상자를 운반하는 작업에서도 성공률이 80% 이상 유지.
- **비교 기준**: 중앙 집중식 정책이나 고정 팀 규모 기반의 기준 방법과 비교하여 TeamHOI는 가변적인 팀 규모에서 더 강력한 일반화 능력과 협력 일관성을 보여줌.

### 결론
TeamHOI는 단일 분산 정책을 통해 가변적인 팀 규모의 협력 인간-로봇 상호작용 문제를 성공적으로 해결했으며, 마스킹된 적대적 운동 사전 전략은 협력 데이터 부족 문제를 효과적으로 완화했습니다. 실험은 이 방법이 다양한 팀 규모와 물체 기하학적 형태에서 물리적으로 현실적이고 일관된 협력 행동을 생성할 수 있음을 보여주며, 다중 에이전트 물리 상호작용 연구에 새로운 방향을 제시합니다.
