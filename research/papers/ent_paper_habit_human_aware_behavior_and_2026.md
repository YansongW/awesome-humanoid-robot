---
$id: ent_paper_habit_human_aware_behavior_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation'
  zh: 'HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation'
  ko: 'HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation'
summary:
  en: 'arXiv:2606.31682v1 Announce Type: new Abstract: Large-scale demonstration datasets have been central to recent progress
    in general-purpose robot policies. However, existing datasets are collected in human-absent settings, and policies trained
    on such data may perform tasks competently in isolation but fail to exhibit human-aware behaviors. To address this gap,
    we introduce HABIT, a large-scale robot demonstration dataset for human-present environments. We organize tasks into three
    roles capturing distinct modes of human-robot interaction: Collaborator, where human and robot jointly accomplish a task;
    Coworker, where they pursue separate tasks in a shared space; and Supervisor, where the human directs the robot. The dataset
    comprises over 10K episodes and over 160 hours across 60 tasks. Our experiments show that training on human-present data
    elicits human-aware behaviors that robot-only data fails to produce: spatiotemporal synchronization in Collaborator tasks,
    yielding in Coworker tasks, and gesture grounding in Supervisor tasks. Moreover, training on HABIT enables rapid adaptation
    to new human-robot interaction tasks. By introducing human presence as a new axis of dataset diversity, HABIT extends
    robot policies to environments shared with humans.'
  zh: HABIT 是一个面向人机共存环境的大规模机器人操作演示数据集，由研究团队提出，包含超过 1 万条演示片段和 160 小时数据，覆盖 60 个任务。其核心贡献在于将人类在场作为数据集多样性的新维度，通过 Collaborator、Coworker
    和 Supervisor 三种交互角色，使机器人策略学会人类感知行为，如时空同步、避让和手势理解。
  ko: 'arXiv:2606.31682v1 Announce Type: new Abstract: Large-scale demonstration datasets have been central to recent progress
    in general-purpose robot policies. However, existing datasets are collected in human-absent settings, and policies trained
    on such data may perform tasks competently in isolation but fail to exhibit human-aware behaviors. To address this gap,
    we introduce HABIT, a large-scale robot demonstration dataset for human-present environments. We organize tasks into three
    roles capturing distinct modes of human-robot interaction: Collaborator, where human and robot jointly accomplish a task;
    Coworker, where they pursue separate tasks in a shared space; and Supervisor, where the human directs the robot. The dataset
    comprises over 10K episodes and over 160 hours across 60 tasks. Our experiments show that training on human-present data
    elicits human-aware behaviors that robot-only data fails to produce: spatiotemporal synchronization in Collaborator tasks,
    yielding in Coworker tasks, and gesture grounding in Supervisor tasks. Moreover, training on HABIT enables rapid adaptation
    to new human-robot interaction tasks. By introducing human presence as a new axis of dataset diversity, HABIT extends
    robot policies to environments shared with humans.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- habit
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31682v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1122 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation'
  url: https://arxiv.org/abs/2606.31682
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有大规模机器人演示数据集多在无人环境下采集，训练出的策略虽能独立完成任务，却缺乏人类感知行为。HABIT 数据集填补了这一空白，专门在人类在场环境中收集数据，并按照人机交互模式将任务分为三类：Collaborator（人机协作完成同一任务）、Coworker（共享空间内各自独立工作）和 Supervisor（人类指挥机器人）。数据集规模达 1 万条以上演示片段、超过 160 小时，涵盖 60 个不同任务。实验表明，基于 HABIT 训练的策略能产生仅靠机器人数据无法实现的人类感知行为，例如协作任务中的时空同步、共享空间中的避让以及指挥任务中的手势理解，并且能快速适应新的人机交互任务。

## 核心内容
### 方法
HABIT 数据集的设计核心是将人类在场作为数据收集的新维度，并依据人机交互模式将任务组织为三种角色：
- **Collaborator**：人类与机器人共同完成同一任务，例如联合搬运物体。
- **Coworker**：人类与机器人在共享空间内各自执行独立任务，例如机器人整理桌面而人类在旁操作。
- **Supervisor**：人类通过手势或语言指挥机器人执行任务，例如指示机器人抓取特定物体。

### 数据集规模
- 总计超过 10,000 条演示片段（episodes），总时长超过 160 小时。
- 覆盖 60 个不同的操作任务，每个任务包含多种人类在场场景。

### 实验设置与关键结果
实验对比了基于 HABIT 训练的策略与仅使用机器人数据训练的策略，在三种交互角色下的表现：
- **Collaborator 任务**：HABIT 训练的策略实现了时空同步（spatiotemporal synchronization），即机器人与人类动作在时间和空间上协调一致，而机器人数据策略无法做到。
- **Coworker 任务**：HABIT 策略学会了避让（yielding）行为，例如在人类伸手取物时主动暂停或调整路径，避免碰撞。
- **Supervisor 任务**：HABIT 策略能够理解手势指令（gesture grounding），例如根据人类指向正确抓取目标物体，而机器人数据策略无法响应此类指令。

此外，迁移学习实验显示，基于 HABIT 预训练的策略在遇到新的人机交互任务时，仅需少量额外演示即可快速适应，表现出良好的泛化能力。

### 结论
HABIT 通过引入人类在场这一新的数据集多样性维度，显著提升了机器人策略在人类共存环境中的行为表现，使其具备人类感知能力，并支持快速适应新交互场景。该数据集为通用机器人策略从孤立环境向共享空间扩展提供了关键基础。

## Overview
Large-scale demonstration datasets have been central to recent progress in general-purpose robot policies. However, existing datasets are collected in human-absent settings, and policies trained on such data may perform tasks competently in isolation but fail to exhibit human-aware behaviors. To address this gap, we introduce HABIT, a large-scale robot demonstration dataset for human-present environments. We organize tasks into three roles capturing distinct modes of human-robot interaction: Collaborator, where human and robot jointly accomplish a task; Coworker, where they pursue separate tasks in a shared space; and Supervisor, where the human directs the robot. The dataset comprises over 10K episodes and over 160 hours across 60 tasks. Our experiments show that training on human-present data elicits human-aware behaviors that robot-only data fails to produce: spatiotemporal synchronization in Collaborator tasks, yielding in Coworker tasks, and gesture grounding in Supervisor tasks. Moreover, training on HABIT enables rapid adaptation to new human-robot interaction tasks. By introducing human presence as a new axis of dataset diversity, HABIT extends robot policies to environments shared with humans.

## 参考
- http://arxiv.org/abs/2606.31682v1

## 개요
기존의 대규모 로봇 시연 데이터셋은 대부분 사람이 없는 환경에서 수집되어, 훈련된 정책이 독립적으로 작업을 수행할 수는 있지만 인간 인지 행동이 부족합니다. HABIT 데이터셋은 이러한 공백을 메우기 위해 인간이 존재하는 환경에서 데이터를 수집하며, 인간-로봇 상호작용 패턴에 따라 작업을 세 가지 유형으로 분류합니다: Collaborator(인간-로봇 협력으로 동일 작업 수행), Coworker(공유 공간에서 각자 독립적으로 작업), Supervisor(인간이 로봇을 지휘). 데이터셋 규모는 10,000개 이상의 시연 에피소드, 160시간 이상, 60개의 다양한 작업을 포함합니다. 실험 결과, HABIT 기반으로 훈련된 정책은 로봇 데이터만으로는 구현할 수 없는 인간 인지 행동을 생성하며, 예를 들어 협력 작업에서의 시공간 동기화, 공유 공간에서의 회피, 지휘 작업에서의 제스처 이해 등이 가능하고, 새로운 인간-로봇 상호작용 작업에도 빠르게 적응할 수 있습니다.

## 핵심 내용
### 방법
HABIT 데이터셋의 설계 핵심은 인간의 존재를 데이터 수집의 새로운 차원으로 도입하고, 인간-로봇 상호작용 패턴에 따라 작업을 세 가지 역할로 구성하는 것입니다:
- **Collaborator**: 인간과 로봇이 동일한 작업을 공동으로 수행, 예를 들어 물체를 함께 운반.
- **Coworker**: 인간과 로봇이 공유 공간에서 각자 독립적인 작업을 수행, 예를 들어 로봇이 책상을 정리하고 인간이 옆에서 작업.
- **Supervisor**: 인간이 제스처나 언어로 로봇에게 작업을 지휘, 예를 들어 특정 물체를 집도록 지시.

### 데이터셋 규모
- 총 10,000개 이상의 시연 에피소드, 총 시간 160시간 이상.
- 60개의 다양한 조작 작업을 포함하며, 각 작업은 여러 인간 존재 시나리오를 포함.

### 실험 설정 및 주요 결과
실험은 HABIT 기반으로 훈련된 정책과 로봇 데이터만으로 훈련된 정책을 세 가지 상호작용 역할에서 비교했습니다:
- **Collaborator 작업**: HABIT으로 훈련된 정책은 시공간 동기화(spatiotemporal synchronization)를 달성, 즉 로봇과 인간의 동작이 시간과 공간에서 조화를 이루지만, 로봇 데이터 정책은 이를 수행할 수 없습니다.
- **Coworker 작업**: HABIT 정책은 회피(yielding) 행동을 학습, 예를 들어 인간이 물건을 집으려 할 때 능동적으로 일시 중지하거나 경로를 조정하여 충돌을 방지.
- **Supervisor 작업**: HABIT 정책은 제스처 지시 이해(gesture grounding)가 가능, 예를 들어 인간의 지시에 따라 올바른 목표 물체를 집지만, 로봇 데이터 정책은 이러한 지시에 반응할 수 없습니다.

또한, 전이 학습 실험에 따르면 HABIT 기반으로 사전 훈련된 정책은 새로운 인간-로봇 상호작용 작업을 만났을 때 소량의 추가 시연만으로 빠르게 적응하며, 우수한 일반화 능력을 보여줍니다.

### 결론
HABIT은 인간의 존재라는 새로운 데이터셋 다양성 차원을 도입하여, 인간과 공존하는 환경에서 로봇 정책의 행동 성능을 크게 향상시키고, 인간 인지 능력을 갖추게 하며, 새로운 상호작용 시나리오에 빠르게 적응할 수 있도록 지원합니다. 이 데이터셋은 범용 로봇 정책이 고립된 환경에서 공유 공간으로 확장되는 데 핵심적인 기반을 제공합니다.
