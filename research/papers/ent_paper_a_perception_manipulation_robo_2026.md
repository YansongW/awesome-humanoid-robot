---
$id: ent_paper_a_perception_manipulation_robo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Perception-Manipulation Robotics System for Food Cutting
  zh: A Perception-Manipulation Robotics System for Food Cutting
  ko: A Perception-Manipulation Robotics System for Food Cutting
summary:
  en: 'arXiv:2607.04367v1 Announce Type: new Abstract: In the development of cooking robots, mastering the task of cutting
    is crucial. A significant challenge lies in the diverse properties of food, which necessitate distinct cutting policies
    and even different knives for optimal processing. This paper presents a perception-manipulation framework for food-cutting
    tasks. Our system features a knife selection module that utilizes force data from a preliminary fixed trial cut to select
    the appropriate knife for the given food. This is followed by an adaptive cutting phase using reinforcement learning (RL)
    to balance cutting speed and energy efficiency. In our experiments, the knife selection module achieved 100% successful
    rate on unseen food, and we compared the performances of fixed policy, RL policy, with human operators. Our method not
    only achieves high performance but also demonstrates comparable results to those of human participants.'
  zh: 本文提出一个面向食物切割任务的感知-操作框架，由刀具选择模块和自适应切割模块组成。刀具选择模块通过预切割阶段的力数据为不同食物自动匹配最佳刀具，自适应切割模块利用强化学习（RL）平衡切割速度与能耗。实验表明，刀具选择模块对未见食物的成功率达100%，整体性能与人类操作者相当。
  ko: 'arXiv:2607.04367v1 Announce Type: new Abstract: In the development of cooking robots, mastering the task of cutting
    is crucial. A significant challenge lies in the diverse properties of food, which necessitate distinct cutting policies
    and even different knives for optimal processing. This paper presents a perception-manipulation framework for food-cutting
    tasks. Our system features a knife selection module that utilizes force data from a preliminary fixed trial cut to select
    the appropriate knife for the given food. This is followed by an adaptive cutting phase using reinforcement learning (RL)
    to balance cutting speed and energy efficiency. In our experiments, the knife selection module achieved 100% successful
    rate on unseen food, and we compared the performances of fixed policy, RL policy, with human operators. Our method not
    only achieves high performance but also demonstrates comparable results to those of human participants.'
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
- robotics
- a_perception_manipulation_robo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04367v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (606 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A Perception-Manipulation Robotics System for Food Cutting (arXiv)
  url: https://arxiv.org/abs/2607.04367
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
该研究针对烹饪机器人中食物切割的多样性挑战，设计了一套包含刀具选择与自适应切割的完整框架。系统首先通过固定试切获取力数据，由刀具选择模块为特定食物推荐最合适的刀具；随后进入基于强化学习的自适应切割阶段，动态调整切割策略以兼顾速度与能效。实验对比了固定策略、RL策略与人类操作者的表现，结果显示RL策略不仅性能优异，且与人类操作水平接近。

## 核心内容
### 方法架构
- **刀具选择模块**：对食物进行固定试切，采集力数据作为输入，输出匹配的刀具类型。该模块在未见食物上实现100%成功率。
- **自适应切割模块**：采用强化学习（RL）策略，在切割过程中实时调整动作，以平衡切割速度与能量效率。RL策略与固定策略及人类操作者进行对比。

### 实验设置
- 测试对象包括多种具有不同物理属性的食物（如硬度、韧性等）。
- 对比条件：固定切割策略、RL自适应策略、人类操作者。
- 评估指标：切割成功率、速度、能耗。

### 关键结果
- 刀具选择模块对未见食物的分类准确率达100%。
- RL策略在切割速度与能效的综合表现上优于固定策略，且与人类操作者结果无显著差异。
- 系统展现了良好的泛化能力，无需针对每种食物单独编程。

### 结论
该感知-操作框架通过刀具选择与RL自适应切割的结合，有效解决了食物切割中的多样性问题，为烹饪机器人实现高效、类人的切割操作提供了可行方案。

## Overview
In the development of cooking robots, mastering the task of cutting is crucial. A significant challenge lies in the diverse properties of food, which necessitate distinct cutting policies and even different knives for optimal processing. This paper presents a perception-manipulation framework for food-cutting tasks. Our system features a knife selection module that utilizes force data from a preliminary fixed trial cut to select the appropriate knife for the given food. This is followed by an adaptive cutting phase using reinforcement learning (RL) to balance cutting speed and energy efficiency. In our experiments, the knife selection module achieved 100% successful rate on unseen food, and we compared the performances of fixed policy, RL policy, with human operators. Our method not only achieves high performance but also demonstrates comparable results to those of human participants.

## 参考
- http://arxiv.org/abs/2607.04367v1

## 개요
이 연구는 요리 로봇에서의 식품 절단 다양성 문제를 해결하기 위해, 칼 선택과 적응형 절단을 포함한 완전한 프레임워크를 설계했습니다. 시스템은 먼저 고정 시험 절단을 통해 힘 데이터를 획득하고, 칼 선택 모듈이 특정 식품에 가장 적합한 칼을 추천합니다. 이후 강화 학습 기반의 적응형 절단 단계로 전환하여, 절단 전략을 동적으로 조정함으로써 속도와 에너지 효율을 동시에 고려합니다. 실험에서는 고정 전략, RL 전략, 인간 작업자의 성능을 비교했으며, RL 전략이 우수한 성능을 보일 뿐만 아니라 인간 작업자 수준에 근접함을 확인했습니다.

## 핵심 내용
### 방법 구조
- **칼 선택 모듈**: 식품에 대해 고정 시험 절단을 수행하고, 힘 데이터를 입력으로 수집하여 일치하는 칼 유형을 출력합니다. 이 모듈은 보지 못한 식품에서 100% 성공률을 달성했습니다.
- **적응형 절단 모듈**: 강화 학습(RL) 전략을 사용하여 절단 과정에서 동작을 실시간으로 조정하며, 절단 속도와 에너지 효율의 균형을 맞춥니다. RL 전략은 고정 전략 및 인간 작업자와 비교됩니다.

### 실험 설정
- 테스트 대상은 다양한 물리적 속성(예: 경도, 인성 등)을 가진 여러 식품을 포함합니다.
- 비교 조건: 고정 절단 전략, RL 적응형 전략, 인간 작업자.
- 평가 지표: 절단 성공률, 속도, 에너지 소비.

### 주요 결과
- 칼 선택 모듈의 보지 못한 식품에 대한 분류 정확도는 100%입니다.
- RL 전략은 절단 속도와 에너지 효율의 종합 성능에서 고정 전략보다 우수하며, 인간 작업자 결과와 유의미한 차이가 없습니다.
- 시스템은 각 식품에 대해 개별적으로 프로그래밍할 필요 없이 우수한 일반화 능력을 보여줍니다.

### 결론
이 인식-작동 프레임워크는 칼 선택과 RL 적응형 절단의 결합을 통해 식품 절단의 다양성 문제를 효과적으로 해결하며, 요리 로봇이 효율적이고 인간과 유사한 절단 작업을 수행할 수 있는 실현 가능한 방안을 제공합니다.
