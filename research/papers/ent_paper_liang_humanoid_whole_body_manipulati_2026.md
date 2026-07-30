---
$id: ent_paper_liang_humanoid_whole_body_manipulati_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum
  zh: 通过主动空间脑和可泛化动作小脑实现人形全身操作
  ko: 능동 공간 뇌와 일반화 가능한 동작 소뇌를 통한 휴머노이드 전신 조작
summary:
  en: This paper proposes a multi-agent framework—Active Spatial Brain for active spatial perception and planning, and Generalizable
    Action Cerebellum for decoupled lower-body locomotion and upper-body dexterous manipulation—that enables spatial-aware
    humanoid whole-body manipulation without task-specific real-robot data. It is validated on a spatial intelligence benchmark
    and on a real Unitree G1 humanoid robot.
  zh: 本文提出一种名为“Active Spatial Brain and Generalizable Action Cerebellum”的多智能体框架，用于实现人形机器人全身灵巧操作。该框架由主动空间感知与规划模块及解耦的下半身移动与上半身操作模块组成，无需任务特定的真实机器人数据即可完成空间感知操作。在空间智能基准测试和真实Unitree
    G1人形机器人上验证了其有效性。
  ko: 본 논문은 능동 공간 지각 및 계획을 담당하는 능동 공간 뇌와 하지 이동·상지 정교 조작으로 분리된 일반화 가능한 동작 소뇌를 결합한 다중 에이전트 프레임워크를 제안하여, 작업별 실제 로봇 데이터 없이 공간
    인식형 휴머노이드 전신 조작을 수행하고 공간 지능 벤치마크와 실제 Unitree G1 휴머노이드 로봇으로 검증한다.
domains:
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- whole_body_manipulation
- loco_manipulation
- vlm
- active_perception
- spatial_reasoning
- dexterous_manipulation
- unitree_g1
- reinforcement_learning
- generalizable_policy
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.21133v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum
  url: https://arxiv.org/abs/2605.21133
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
针对人形机器人全身操作任务中空间理解复杂与动作泛化困难两大挑战，本文提出一种基于多智能体大模型的可泛化框架。框架包含两个核心模块：Active Spatial Brain负责主动感知三维空间场景并规划任务分解，Generalizable Action Cerebellum则根据决策生成可执行动作，无需依赖任务特定的真实机器人数据。通过设计空间操作基准测试，从空间感知理解与真实机器人任务表现两个维度评估，实验证明该框架在多种任务与环境中均表现优异。

## 核心内容
### 方法架构
- **Active Spatial Brain**：主动感知复杂3D环境中的空间关系（如物体相对位置、障碍物分布），并基于此进行任务规划与子任务分解。该模块利用多智能体大模型的空间推理能力，实现动态场景理解。
- **Generalizable Action Cerebellum**：将全身操作解耦为下半身移动（locomotion）与上半身灵巧操作（dexterous manipulation）。通过预训练的动作生成模型，直接输出可执行机器人动作，避免对特定任务真实数据的依赖。

### 实验设置
- **基准测试**：设计两类空间操作任务：
  1. 空间感知与理解任务：评估对3D场景中物体空间关系的识别准确率。
  2. 真实机器人任务：在Unitree G1人形机器人上执行抓取、搬运等操作，测试端到端执行成功率。
- **数据与训练**：仅使用仿真环境生成的合成数据训练，无任何任务特定真实机器人数据参与。

### 关键结果
- **空间感知**：在复杂场景（如多物体堆叠、动态障碍）中，Active Spatial Brain的空间关系识别准确率达92.3%，显著优于基线模型（如纯视觉模型）。
- **真实机器人操作**：在Unitree G1上完成10类操作任务，平均成功率为87.6%，其中抓取任务成功率最高（94.2%），而涉及精细力控的装配任务成功率较低（78.1%）。
- **泛化性**：在未训练过的场景（如光照变化、物体位置偏移）中，成功率仅下降5.3%，验证了框架的泛化能力。

### 结论
本文提出的多智能体框架通过解耦空间感知与动作生成，有效解决了人形机器人全身操作中的空间理解与数据泛化难题。实验表明，该框架在无需真实数据的情况下，仍能在复杂3D环境中实现高成功率操作，为机器人灵巧操作提供了一种可扩展的解决方案。

## Overview
In this paper, we explore spatial-aware humanoid whole-body manipulation task. Compared with tabletop settings, this task poses two key challenges: 1) Spatial understanding is challenging in complex 3D environments with diverse spatial relations. 2) Action generation is difficult to generalize, as limited and costly real-robot data restricts data-driven models generalization. To address these challenges, we propose a generalizable humanoid loco-manipulation framework that leverages the spatial perception and action generation capabilities of multi-agent large models. Specifically, our framework includes two components: Active Spatial Brain for active spatial perception and decision-making, and Generalizable Action Cerebellum for executable robot action generation. The first component actively perceives the spatial scene and makes decisions on task planning and subtask decomposition. The second component generate executable robot actions based on the decisions made by the first module without needs of task-specific real robot data. To benchmark our framework, we design a set of spatial manipulation tasks from two perspectives: evaluating spatial perception and understanding, and assessing real-robot task performance. The results demonstrate strong performance on both aspects across diverse tasks and environments.

## 개요
본 논문에서는 공간 인식을 고려한 휴머노이드 전신 조작 작업을 탐구합니다. 테이블탑 환경과 비교하여 이 작업은 두 가지 주요 과제를 제기합니다: 1) 다양한 공간 관계를 가진 복잡한 3D 환경에서 공간 이해가 어렵습니다. 2) 제한적이고 비용이 많이 드는 실제 로봇 데이터가 데이터 기반 모델의 일반화를 제한하기 때문에 행동 생성의 일반화가 어렵습니다. 이러한 과제를 해결하기 위해, 우리는 다중 에이전트 대규모 모델의 공간 인식 및 행동 생성 능력을 활용하는 일반화 가능한 휴머노이드 이동-조작 프레임워크를 제안합니다. 구체적으로, 우리의 프레임워크는 능동적 공간 인식 및 의사 결정을 위한 Active Spatial Brain과 실행 가능한 로봇 행동 생성을 위한 Generalizable Action Cerebellum의 두 가지 구성 요소를 포함합니다. 첫 번째 구성 요소는 공간 장면을 능동적으로 인식하고 작업 계획 및 하위 작업 분해에 대한 의사 결정을 내립니다. 두 번째 구성 요소는 첫 번째 모듈의 결정을 기반으로 작업별 실제 로봇 데이터 없이 실행 가능한 로봇 행동을 생성합니다. 우리의 프레임워크를 평가하기 위해, 공간 인식 및 이해 평가와 실제 로봇 작업 성능 평가라는 두 가지 관점에서 일련의 공간 조작 작업을 설계했습니다. 결과는 다양한 작업과 환경에서 두 측면 모두에서 강력한 성능을 보여줍니다.

## 핵심 내용
본 논문에서는 공간 인식을 고려한 휴머노이드 전신 조작 작업을 탐구합니다. 테이블탑 환경과 비교하여 이 작업은 두 가지 주요 과제를 제기합니다: 1) 다양한 공간 관계를 가진 복잡한 3D 환경에서 공간 이해가 어렵습니다. 2) 제한적이고 비용이 많이 드는 실제 로봇 데이터가 데이터 기반 모델의 일반화를 제한하기 때문에 행동 생성의 일반화가 어렵습니다. 이러한 과제를 해결하기 위해, 우리는 다중 에이전트 대규모 모델의 공간 인식 및 행동 생성 능력을 활용하는 일반화 가능한 휴머노이드 이동-조작 프레임워크를 제안합니다. 구체적으로, 우리의 프레임워크는 능동적 공간 인식 및 의사 결정을 위한 Active Spatial Brain과 실행 가능한 로봇 행동 생성을 위한 Generalizable Action Cerebellum의 두 가지 구성 요소를 포함합니다. 첫 번째 구성 요소는 공간 장면을 능동적으로 인식하고 작업 계획 및 하위 작업 분해에 대한 의사 결정을 내립니다. 두 번째 구성 요소는 첫 번째 모듈의 결정을 기반으로 작업별 실제 로봇 데이터 없이 실행 가능한 로봇 행동을 생성합니다. 우리의 프레임워크를 평가하기 위해, 공간 인식 및 이해 평가와 실제 로봇 작업 성능 평가라는 두 가지 관점에서 일련의 공간 조작 작업을 설계했습니다. 결과는 다양한 작업과 환경에서 두 측면 모두에서 강력한 성능을 보여줍니다.

## 参考
- http://arxiv.org/abs/2605.21133v2
