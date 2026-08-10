---
$id: ent_paper_kaushik_adaptive_prior_selection_for_r_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adaptive Prior Selection for Repertoire-based Online Adaptation in Robotics
  zh: 机器人中基于技能库的在线自适应的自适应先验选择
  ko: 로봇 공학에서 레퍼토리 기반 온라인 적응을 위한 적응형 사전 선택
summary:
  en: This paper introduces APROL, an algorithm that maintains multiple MAP-Elites behavioral repertoires as simulation priors
    and selects the most suitable prior online using Gaussian-process transformation models and a MAP/UCB action-selection
    criterion. It enables reset-free adaptation to damage and environmental changes, and is shown to outperform single-prior
    and RTE baselines on simulated object pushing and hexapod locomotion, with validation on a real damaged hexapod.
  zh: APROL 是一种用于机器人在线适应的算法，由研究团队提出，通过维护多个 MAP-Elites 行为库作为仿真先验，并利用高斯过程转换模型和 MAP/UCB 动作选择准则在线选择最合适的先验。其核心贡献在于无需重置即可适应损伤和环境变化，在模拟物体推搡和六足机器人运动任务中优于单先验和
    RTE 基线，并在真实受损六足机器人上得到验证。
  ko: 본 논문은 여러 MAP-Elites 행동 레퍼토리를 시뮬레이션 사전 정보로 유지하고, 가우시안 프로세스 변환 모델과 MAP/UCB 행동 선택 기준을 통해 온라인으로 가장 적절한 사전 정보를 선택하는 APROL
    알고리즘을 제안한다. 이는 재설정 없는 손상 및 환경 변화 적응을 가능하게 하며, 모의 물체 밀기와 육족 보행 과제에서 단일 사전 정보 및 RTE 기준보다 우수한 성능을 보이고, 실제 손상된 육족 로봇에서 검증되었다.
domains:
- 07_ai_models_algorithms
- 03_manufacturing_processes
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- repertoire_based_learning
- online_adaptation
- map_elites
- gaussian_process
- reset_free_learning
- damage_recovery
- simulation_prior
- behavioral_repertoire
- robot_adaptation
- aprol
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1907.07029v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (942 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Adaptive Prior Selection for Repertoire-based Online Adaptation in Robotics
  url: https://arxiv.org/abs/1907.07029
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
本文提出 APROL 算法，旨在解决机器人适应过程中单一行为库先验不足的问题。APROL 通过生成多种情境下的 MAP-Elites 行为库，并在线选择最相关的先验来指导动作规划，从而无需重置即可应对损伤和环境变化。在模拟任务中，APROL 在物体推搡和六足机器人目标到达任务上均比 Reset-free Trial and Error (RTE) 和单先验基线更高效。此外，真实实验表明，受损六足机器人能利用 APROL 快速学习补偿策略，避开障碍物到达目标。

## 核心内容
### 方法
- **核心思想**：APROL 基于行为库的在线适应框架，通过生成多个 MAP-Elites 行为库（每个对应不同情境，如缺失腿、不同地面等），并在线选择最合适的先验来指导动作。
- **算法流程**：
  - 使用高斯过程转换模型（Gaussian-process transformation models）将当前机器人状态映射到各先验行为库中。
  - 采用 MAP/UCB 动作选择准则（MAP/UCB action-selection criterion）平衡探索与利用，选择最可能适应当前情境的动作。
  - 无需重置（reset-free），即机器人可在连续交互中直接调整策略。

### 实验设置
- **模拟任务**：
  1. **物体推搡**：机械臂推搡未知形状和尺寸的物体。
  2. **六足机器人目标到达**：受损六足机器人需到达指定目标位置。
- **基线对比**：与 Reset-free Trial and Error (RTE) 及多种单先验行为库基线比较。
- **真实实验**：在真实受损六足机器人上验证，机器人需避开障碍物到达目标。

### 关键结果
- **模拟任务**：APROL 在两种任务中均以更少的交互次数（interaction time）完成任务，优于所有基线。
- **真实实验**：受损六足机器人能快速学习补偿策略，成功避开障碍物并到达目标，验证了算法的实际有效性。

### 结论
APROL 通过多先验在线选择机制，显著提升了机器人对未知损伤和环境变化的适应效率，且无需重置，为行为库方法提供了更灵活的扩展。

## Overview
Repertoire-based learning is a data-efficient adaptation approach based on a two-step process in which (1) a large and diverse set of policies is learned in simulation, and (2) a planning or learning algorithm chooses the most appropriate policies according to the current situation (e.g., a damaged robot, a new object, etc.). In this paper, we relax the assumption of previous works that a single repertoire is enough for adaptation. Instead, we generate repertoires for many different situations (e.g., with a missing leg, on different floors, etc.) and let our algorithm selects the most useful prior. Our main contribution is an algorithm, APROL (Adaptive Prior selection for Repertoire-based Online Learning) to plan the next action by incorporating these priors when the robot has no information about the current situation. We evaluate APROL on two simulated tasks: (1) pushing unknown objects of various shapes and sizes with a robotic arm and (2) a goal reaching task with a damaged hexapod robot. We compare with "Reset-free Trial and Error" (RTE) and various single repertoire-based baselines. The results show that APROL solves both the tasks in less interaction time than the baselines. Additionally, we demonstrate APROL on a real, damaged hexapod that quickly learns to pick compensatory policies to reach a goal by avoiding obstacles in the path.

## 参考
- http://arxiv.org/abs/1907.07029v3

## 개요
본 논문은 로봇 적응 과정에서 단일 행동 라이브러리의 사전 지식 부족 문제를 해결하기 위해 APROL 알고리즘을 제안한다. APROL은 다양한 상황에서의 MAP-Elites 행동 라이브러리를 생성하고, 온라인으로 가장 관련성 높은 사전 지식을 선택하여 동작 계획을 안내함으로써, 재설정 없이 손상 및 환경 변화에 대응할 수 있다. 시뮬레이션 작업에서 APROL은 물체 밀기 및 육족 로봇 목표 도달 작업 모두에서 Reset-free Trial and Error (RTE) 및 단일 사전 지식 기준선보다 더 효율적이었다. 또한, 실제 실험에서 손상된 육족 로봇이 APROL을 활용하여 보상 전략을 빠르게 학습하고 장애물을 피해 목표에 도달할 수 있음을 보여주었다.

## 핵심 내용
### 방법
- **핵심 아이디어**: APROL은 행동 라이브러리 기반 온라인 적응 프레임워크로, 여러 MAP-Elites 행동 라이브러리(각각 다른 상황, 예: 다리 결손, 다양한 지면 등에 대응)를 생성하고, 온라인으로 가장 적합한 사전 지식을 선택하여 동작을 안내한다.
- **알고리즘 흐름**:
  - 가우시안 프로세스 변환 모델(Gaussian-process transformation models)을 사용하여 현재 로봇 상태를 각 사전 행동 라이브러리에 매핑한다.
  - MAP/UCB 동작 선택 기준(MAP/UCB action-selection criterion)을 사용하여 탐색과 활용의 균형을 맞추고, 현재 상황에 가장 적응할 가능성이 높은 동작을 선택한다.
  - 재설정 없음(reset-free), 즉 로봇이 연속적인 상호작용에서 직접 전략을 조정할 수 있다.

### 실험 설정
- **시뮬레이션 작업**:
  1. **물체 밀기**: 로봇 팔이 알 수 없는 모양과 크기의 물체를 민다.
  2. **육족 로봇 목표 도달**: 손상된 육족 로봇이 지정된 목표 위치에 도달해야 한다.
- **기준선 비교**: Reset-free Trial and Error (RTE) 및 다양한 단일 사전 지식 행동 라이브러리 기준선과 비교.
- **실제 실험**: 실제 손상된 육족 로봇에서 검증하며, 로봇은 장애물을 피해 목표에 도달해야 한다.

### 주요 결과
- **시뮬레이션 작업**: APROL은 두 작업 모두에서 더 적은 상호작용 시간(interaction time)으로 작업을 완료하여 모든 기준선보다 우수했다.
- **실제 실험**: 손상된 육족 로봇이 보상 전략을 빠르게 학습하고 장애물을 성공적으로 피해 목표에 도달하여 알고리즘의 실제 효용성을 검증했다.

### 결론
APROL은 다중 사전 지식 온라인 선택 메커니즘을 통해 로봇의 알 수 없는 손상 및 환경 변화에 대한 적응 효율성을 크게 향상시키며, 재설정이 필요 없어 행동 라이브러리 방법에 더 유연한 확장을 제공한다.
