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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.18964v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (936 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2410.18964v1

## 개요
본 연구는 로봇 조작에서 능동적 또는 상호작용적 탐색 행동이 필요한 작업을 위해, 분해된 맥락 마르코프 결정 과정(factorized Contextual Markov Decision Processes) 문제 모델을 제안한다. 저자들은 DISaM 이중 정책 프레임워크를 설계했으며, 이는 관련 맥락 정보를 획득하기 위해 환경을 탐색하는 정보 탐색 정책과, 해당 맥락을 활용하여 조작 목표를 완수하는 정보 수신 정책을 포함한다. 두 정책을 분리하여 훈련함으로써, 정보 수신 정책은 정보 탐색 정책에 보상 신호를 제공할 수 있다. 테스트 단계에서는 이중 에이전트가 조작 정책의 다음 최적 행동에 대한 불확실성에 기반하여 탐색과 활용의 균형을 조정한다. 실험은 정보 탐색 행동이 필요한 다섯 가지 조작 작업(시뮬레이션 및 실제 환경 포함)에서 DISaM의 우수한 성능을 검증했다.

## 핵심 내용
### 문제 정의
- 분해된 맥락 마르코프 결정 과정(factorized Contextual MDPs)을 제안하여 작업을 정보 탐색 단계와 정보 활용 단계로 분해
- 능동적 탐색이 필요한 로봇 조작 시나리오에 적용 가능. 예: 로봇 머리 움직임을 통한 조작 관련 정보 탐색, 또는 다중 로봇 시스템에서 정찰 로봇이 정보를 탐색하여 의사결정 로봇에 제공

### 방법 아키텍처: DISaM
- **이중 정책 프레임워크**:
  - 정보 탐색 정책(information-seeking policy): 환경을 탐색하여 관련 맥락 정보를 찾는 역할
  - 정보 수신 정책(information-receiving policy): 획득한 맥락 정보를 활용하여 조작 목표를 완수하는 역할
- **훈련 메커니즘**:
  - 두 정책은 분리하여 훈련 가능하며, 정보 수신 정책이 정보 탐색 정책에 보상 신호를 제공
  - 테스트 시 조작 정책의 다음 최적 행동에 대한 불확실성에 기반하여 탐색과 활용을 동적으로 균형 조정

### 실험 설정
- 정보 탐색 행동이 필요한 다섯 가지 조작 작업으로, 시뮬레이션 환경과 실제 세계 시나리오를 포함
- 기존 방법과 비교하여 DISaM은 모든 작업에서 현저히 우수한 성능을 보임

### 주요 결과
- 시뮬레이션 및 실제 환경 모두에서 DISaM은 더 강력한 정보 탐색 및 조작 의사결정 능력을 입증
- 이중 정책 분해 설계는 탐색과 활용의 균형 문제를 효과적으로 해결

### 결론
- 분해된 맥락 MDP는 능동적 탐색이 필요한 조작 작업을 위한 통합 모델링 프레임워크를 제공
- DISaM의 이중 정책 분리 훈련 방법은 확장 가능하며, 다양한 로봇 조작 시나리오에 적용 가능

더 많은 정보는 프로젝트 홈페이지에서 확인: https://robin-lab.cs.utexas.edu/learning2look/
