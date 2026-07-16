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
  zh: 本文提出了一种多智能体框架——主动空间脑负责主动空间感知与规划，可泛化动作小脑负责解耦的下肢移动与上肢灵巧操作——无需任务特定的真实机器人数据即可实现空间感知的人形全身操作，并在空间智能基准与真实Unitree G1人形机器人上进行了验证。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.21133v2.
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
In this paper, we explore spatial-aware humanoid whole-body manipulation task. Compared with tabletop settings, this task poses two key challenges: 1) Spatial understanding is challenging in complex 3D environments with diverse spatial relations. 2) Action generation is difficult to generalize, as limited and costly real-robot data restricts data-driven models generalization. To address these challenges, we propose a generalizable humanoid loco-manipulation framework that leverages the spatial perception and action generation capabilities of multi-agent large models. Specifically, our framework includes two components: Active Spatial Brain for active spatial perception and decision-making, and Generalizable Action Cerebellum for executable robot action generation. The first component actively perceives the spatial scene and makes decisions on task planning and subtask decomposition. The second component generate executable robot actions based on the decisions made by the first module without needs of task-specific real robot data. To benchmark our framework, we design a set of spatial manipulation tasks from two perspectives: evaluating spatial perception and understanding, and assessing real-robot task performance. The results demonstrate strong performance on both aspects across diverse tasks and environments.

## 核心内容
In this paper, we explore spatial-aware humanoid whole-body manipulation task. Compared with tabletop settings, this task poses two key challenges: 1) Spatial understanding is challenging in complex 3D environments with diverse spatial relations. 2) Action generation is difficult to generalize, as limited and costly real-robot data restricts data-driven models generalization. To address these challenges, we propose a generalizable humanoid loco-manipulation framework that leverages the spatial perception and action generation capabilities of multi-agent large models. Specifically, our framework includes two components: Active Spatial Brain for active spatial perception and decision-making, and Generalizable Action Cerebellum for executable robot action generation. The first component actively perceives the spatial scene and makes decisions on task planning and subtask decomposition. The second component generate executable robot actions based on the decisions made by the first module without needs of task-specific real robot data. To benchmark our framework, we design a set of spatial manipulation tasks from two perspectives: evaluating spatial perception and understanding, and assessing real-robot task performance. The results demonstrate strong performance on both aspects across diverse tasks and environments.

## 参考
- http://arxiv.org/abs/2605.21133v2

## Overview
In this paper, we explore spatial-aware humanoid whole-body manipulation task. Compared with tabletop settings, this task poses two key challenges: 1) Spatial understanding is challenging in complex 3D environments with diverse spatial relations. 2) Action generation is difficult to generalize, as limited and costly real-robot data restricts data-driven models generalization. To address these challenges, we propose a generalizable humanoid loco-manipulation framework that leverages the spatial perception and action generation capabilities of multi-agent large models. Specifically, our framework includes two components: Active Spatial Brain for active spatial perception and decision-making, and Generalizable Action Cerebellum for executable robot action generation. The first component actively perceives the spatial scene and makes decisions on task planning and subtask decomposition. The second component generate executable robot actions based on the decisions made by the first module without needs of task-specific real robot data. To benchmark our framework, we design a set of spatial manipulation tasks from two perspectives: evaluating spatial perception and understanding, and assessing real-robot task performance. The results demonstrate strong performance on both aspects across diverse tasks and environments.

## Content
In this paper, we explore spatial-aware humanoid whole-body manipulation task. Compared with tabletop settings, this task poses two key challenges: 1) Spatial understanding is challenging in complex 3D environments with diverse spatial relations. 2) Action generation is difficult to generalize, as limited and costly real-robot data restricts data-driven models generalization. To address these challenges, we propose a generalizable humanoid loco-manipulation framework that leverages the spatial perception and action generation capabilities of multi-agent large models. Specifically, our framework includes two components: Active Spatial Brain for active spatial perception and decision-making, and Generalizable Action Cerebellum for executable robot action generation. The first component actively perceives the spatial scene and makes decisions on task planning and subtask decomposition. The second component generate executable robot actions based on the decisions made by the first module without needs of task-specific real robot data. To benchmark our framework, we design a set of spatial manipulation tasks from two perspectives: evaluating spatial perception and understanding, and assessing real-robot task performance. The results demonstrate strong performance on both aspects across diverse tasks and environments.

## 개요
본 논문에서는 공간 인식을 고려한 휴머노이드 전신 조작 작업을 탐구합니다. 테이블탑 환경과 비교하여 이 작업은 두 가지 주요 과제를 제기합니다: 1) 다양한 공간 관계를 가진 복잡한 3D 환경에서 공간 이해가 어렵습니다. 2) 제한적이고 비용이 많이 드는 실제 로봇 데이터가 데이터 기반 모델의 일반화를 제한하기 때문에 행동 생성의 일반화가 어렵습니다. 이러한 과제를 해결하기 위해, 우리는 다중 에이전트 대규모 모델의 공간 인식 및 행동 생성 능력을 활용하는 일반화 가능한 휴머노이드 이동-조작 프레임워크를 제안합니다. 구체적으로, 우리의 프레임워크는 능동적 공간 인식 및 의사 결정을 위한 Active Spatial Brain과 실행 가능한 로봇 행동 생성을 위한 Generalizable Action Cerebellum의 두 가지 구성 요소를 포함합니다. 첫 번째 구성 요소는 공간 장면을 능동적으로 인식하고 작업 계획 및 하위 작업 분해에 대한 의사 결정을 내립니다. 두 번째 구성 요소는 첫 번째 모듈의 결정을 기반으로 작업별 실제 로봇 데이터 없이 실행 가능한 로봇 행동을 생성합니다. 우리의 프레임워크를 평가하기 위해, 공간 인식 및 이해 평가와 실제 로봇 작업 성능 평가라는 두 가지 관점에서 일련의 공간 조작 작업을 설계했습니다. 결과는 다양한 작업과 환경에서 두 측면 모두에서 강력한 성능을 보여줍니다.

## 핵심 내용
본 논문에서는 공간 인식을 고려한 휴머노이드 전신 조작 작업을 탐구합니다. 테이블탑 환경과 비교하여 이 작업은 두 가지 주요 과제를 제기합니다: 1) 다양한 공간 관계를 가진 복잡한 3D 환경에서 공간 이해가 어렵습니다. 2) 제한적이고 비용이 많이 드는 실제 로봇 데이터가 데이터 기반 모델의 일반화를 제한하기 때문에 행동 생성의 일반화가 어렵습니다. 이러한 과제를 해결하기 위해, 우리는 다중 에이전트 대규모 모델의 공간 인식 및 행동 생성 능력을 활용하는 일반화 가능한 휴머노이드 이동-조작 프레임워크를 제안합니다. 구체적으로, 우리의 프레임워크는 능동적 공간 인식 및 의사 결정을 위한 Active Spatial Brain과 실행 가능한 로봇 행동 생성을 위한 Generalizable Action Cerebellum의 두 가지 구성 요소를 포함합니다. 첫 번째 구성 요소는 공간 장면을 능동적으로 인식하고 작업 계획 및 하위 작업 분해에 대한 의사 결정을 내립니다. 두 번째 구성 요소는 첫 번째 모듈의 결정을 기반으로 작업별 실제 로봇 데이터 없이 실행 가능한 로봇 행동을 생성합니다. 우리의 프레임워크를 평가하기 위해, 공간 인식 및 이해 평가와 실제 로봇 작업 성능 평가라는 두 가지 관점에서 일련의 공간 조작 작업을 설계했습니다. 결과는 다양한 작업과 환경에서 두 측면 모두에서 강력한 성능을 보여줍니다.
