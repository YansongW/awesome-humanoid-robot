---
$id: ent_paper_learning_to_look_seeking_infor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization'
  zh: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization'
  ko: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization'
summary:
  en: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization is a 2024 work on manipulation for
    humanoid robots.'
  zh: '《Learning to Look: Seeking Information for Decision Making via Policy Factorization》是2024年关于人形机器人操作的研究。作者提出因子化上下文马尔可夫决策过程（factorized
    Contextual Markov Decision Processes）问题，并设计双策略框架DISaM，通过信息搜索策略与信息接收策略的分离训练，实现操作任务中的主动探索与决策。该方法在五项需要信息搜索行为的操作任务中显著优于现有方法。'
  ko: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization is a 2024 work on manipulation for
    humanoid robots.'
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
- learning_to_look
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.18964v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization (arXiv)'
  url: https://arxiv.org/abs/2410.18964
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization project page'
  url: https://robin-lab.cs.utexas.edu/learning2look/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对机器人操作中需要主动或交互式探索行为的任务，提出因子化上下文马尔可夫决策过程（factorized Contextual Markov Decision Processes）问题模型。作者设计DISaM双策略框架，包含一个负责探索环境以获取相关上下文信息的信息搜索策略，以及一个利用该上下文完成操作目标的信息接收策略。通过将两种策略分离训练，信息接收策略可为信息搜索策略提供奖励信号。在测试阶段，双智能体根据操作策略对下一步最佳行动的不确定性来平衡探索与利用。实验在五项需要信息搜索行为的操作任务中（包括仿真和真实环境）验证了DISaM的优越性能。

## 核心内容
### 问题定义
- 提出因子化上下文马尔可夫决策过程（factorized Contextual MDPs），将任务分解为信息搜索阶段与信息利用阶段
- 适用于需要主动探索的机器人操作场景，如机器人头部移动寻找操作相关信息，或多机器人系统中侦察机器人搜索信息供决策机器人使用

### 方法架构：DISaM
- **双策略框架**：
  - 信息搜索策略（information-seeking policy）：负责探索环境，寻找相关上下文信息
  - 信息接收策略（information-receiving policy）：利用获取的上下文信息完成操作目标
- **训练机制**：
  - 两种策略可分离训练，信息接收策略为信息搜索策略提供奖励信号
  - 测试时根据操作策略对下一步最佳行动的不确定性动态平衡探索与利用

### 实验设置
- 五项需要信息搜索行为的操作任务，涵盖仿真环境与真实世界场景
- 对比现有方法，DISaM在各项任务中均显著优于基线

### 关键结果
- 在仿真与真实环境中，DISaM均表现出更强的信息搜索与操作决策能力
- 双策略因子化设计有效解决了探索与利用的平衡问题

### 结论
- 因子化上下文MDP为需要主动探索的操作任务提供了统一建模框架
- DISaM的双策略分离训练方法具有可扩展性，适用于多种机器人操作场景

更多信息见项目主页：https://robin-lab.cs.utexas.edu/learning2look/

## Overview
Many robot manipulation tasks require active or interactive exploration behavior in order to be performed successfully. Such tasks are ubiquitous in embodied domains, where agents must actively search for the information necessary for each stage of a task, e.g., moving the head of the robot to find information relevant to manipulation, or in multi-robot domains, where one scout robot may search for the information that another robot needs to make informed decisions. We identify these tasks with a new type of problem, factorized Contextual Markov Decision Processes, and propose DISaM, a dual-policy solution composed of an information-seeking policy that explores the environment to find the relevant contextual information and an information-receiving policy that exploits the context to achieve the manipulation goal. This factorization allows us to train both policies separately, using the information-receiving one to provide reward to train the information-seeking policy. At test time, the dual agent balances exploration and exploitation based on the uncertainty the manipulation policy has on what the next best action is. We demonstrate the capabilities of our dual policy solution in five manipulation tasks that require information-seeking behaviors, both in simulation and in the real-world, where DISaM significantly outperforms existing methods. More information at https://robin-lab.cs.utexas.edu/learning2look/.

## 개요
많은 로봇 조작 작업은 성공적으로 수행되기 위해 능동적 또는 상호작용적 탐색 행동을 필요로 합니다. 이러한 작업은 에이전트가 작업의 각 단계에 필요한 정보를 능동적으로 검색해야 하는 구현된 도메인(예: 조작과 관련된 정보를 찾기 위해 로봇의 머리를 움직이는 경우)이나, 정찰 로봇이 다른 로봇이 정보에 기반한 결정을 내리는 데 필요한 정보를 검색할 수 있는 다중 로봇 도메인에서 흔히 나타납니다. 우리는 이러한 작업을 새로운 유형의 문제인 분해된 맥락적 마르코프 결정 과정(factorized Contextual Markov Decision Processes)으로 식별하고, DISaM을 제안합니다. DISaM은 환경을 탐색하여 관련 맥락 정보를 찾는 정보 탐색 정책과 맥락을 활용하여 조작 목표를 달성하는 정보 수신 정책으로 구성된 이중 정책 솔루션입니다. 이러한 분해를 통해 두 정책을 별도로 훈련할 수 있으며, 정보 수신 정책을 사용하여 정보 탐색 정책을 훈련하기 위한 보상을 제공합니다. 테스트 시에는 이중 에이전트가 조작 정책이 다음 최적 행동에 대해 가지는 불확실성에 기반하여 탐색과 활용의 균형을 맞춥니다. 우리는 시뮬레이션과 실제 환경 모두에서 정보 탐색 행동을 필요로 하는 다섯 가지 조작 작업에서 이중 정책 솔루션의 성능을 입증했으며, DISaM이 기존 방법을 크게 능가함을 보여줍니다. 자세한 정보는 https://robin-lab.cs.utexas.edu/learning2look/에서 확인할 수 있습니다.

## 핵심 내용
많은 로봇 조작 작업은 성공적으로 수행되기 위해 능동적 또는 상호작용적 탐색 행동을 필요로 합니다. 이러한 작업은 에이전트가 작업의 각 단계에 필요한 정보를 능동적으로 검색해야 하는 구현된 도메인(예: 조작과 관련된 정보를 찾기 위해 로봇의 머리를 움직이는 경우)이나, 정찰 로봇이 다른 로봇이 정보에 기반한 결정을 내리는 데 필요한 정보를 검색할 수 있는 다중 로봇 도메인에서 흔히 나타납니다. 우리는 이러한 작업을 새로운 유형의 문제인 분해된 맥락적 마르코프 결정 과정(factorized Contextual Markov Decision Processes)으로 식별하고, DISaM을 제안합니다. DISaM은 환경을 탐색하여 관련 맥락 정보를 찾는 정보 탐색 정책과 맥락을 활용하여 조작 목표를 달성하는 정보 수신 정책으로 구성된 이중 정책 솔루션입니다. 이러한 분해를 통해 두 정책을 별도로 훈련할 수 있으며, 정보 수신 정책을 사용하여 정보 탐색 정책을 훈련하기 위한 보상을 제공합니다. 테스트 시에는 이중 에이전트가 조작 정책이 다음 최적 행동에 대해 가지는 불확실성에 기반하여 탐색과 활용의 균형을 맞춥니다. 우리는 시뮬레이션과 실제 환경 모두에서 정보 탐색 행동을 필요로 하는 다섯 가지 조작 작업에서 이중 정책 솔루션의 성능을 입증했으며, DISaM이 기존 방법을 크게 능가함을 보여줍니다. 자세한 정보는 https://robin-lab.cs.utexas.edu/learning2look/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2410.18964v1
