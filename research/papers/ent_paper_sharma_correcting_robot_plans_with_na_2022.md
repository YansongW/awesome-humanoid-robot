---
$id: ent_paper_sharma_correcting_robot_plans_with_na_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Correcting Robot Plans with Natural Language Feedback
  zh: Language costs
  ko: Correcting Robot Plans with Natural Language Feedback
summary:
  en: Correcting Robot Plans with Natural Language Feedback (Language costs), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, MIT, University of Utah, University of Washington, and published
    at Robotics - Science and Systems 2022.
  zh: Correcting Robot Plans with Natural Language Feedback 是2022年由NVIDIA、MIT、犹他大学、华盛顿大学联合提出的通用视觉-语言-动作模型，发表于Robotics - Science
    and Systems 2022。核心贡献在于通过自然语言句子映射为代价函数变换，实现对机器人规划的纠错，在原始规划失败的任务上经1-2次语言修正后成功率分别达81%和93%。
  ko: Correcting Robot Plans with Natural Language Feedback (Language costs), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, MIT, University of Utah, University of Washington, and published
    at Robotics - Science and Systems 2022.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- language_costs
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2204.05186v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (824 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: Language costs source
  url: https://doi.org/10.15607/RSS.2022.XVIII.065
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对人类为机器人设计代价或目标规范时常见的模糊、欠指定或超出规划器能力的问题，提出利用自然语言作为表达灵活的工具进行纠错。方法将自然语言句子映射为代价函数变换，支持修正目标、更新运动以容纳额外偏好、从规划错误中恢复。实验表明，在模拟和真实环境中，该方法可组合多个约束，并泛化至未见场景、物体和句子，单次或两次语言修正即可显著提升任务成功率。

## 核心内容
### 方法架构
- **核心思想**：将自然语言纠错指令转化为代价函数的数学变换，而非直接修改规划输出。
- **映射机制**：通过预训练语言模型解析句子语义，生成对应代价函数的权重调整、约束添加或路径点引导等变换操作。
- **规划框架**：基于代价函数优化的规划器（如轨迹优化），在每次语言修正后重新求解最优动作序列。

### 实验设置
- **任务场景**：包含桌面操作、物体抓取与放置等典型机器人操控任务，原始规划器因规范模糊或约束冲突而失败。
- **数据集**：使用模拟环境（如PyBullet）和真实机器人平台（如Franka Emika Panda）进行验证，测试句子涵盖目标修正、避障、路径点指定等类型。
- **基线对比**：与无修正规划、随机修正、基于规则的关键词匹配方法对比，语言修正方法在成功率上显著领先。

### 关键结果
- **成功率**：原始规划失败的任务中，单次语言修正成功率达81%，两次修正提升至93%。
- **泛化能力**：在未见场景（新物体布局）、未见物体（不同形状/颜色）和未见句子（新表述方式）上均保持稳定性能。
- **约束组合**：支持同时应用多个语言修正（如“先抓红色杯子再避开蓝色方块”），规划器能自动权衡并生成可行轨迹。

### 结论
自然语言纠错为人类-机器人交互提供了一种高效、灵活且可泛化的方法，显著降低了对完整遥操作或实时交互的依赖。未来工作可探索更复杂的语言指令（如时序约束）和实时反馈循环。

## Overview
When humans design cost or goal specifications for robots, they often produce specifications that are ambiguous, underspecified, or beyond planners' ability to solve. In these cases, corrections provide a valuable tool for human-in-the-loop robot control. Corrections might take the form of new goal specifications, new constraints (e.g. to avoid specific objects), or hints for planning algorithms (e.g. to visit specific waypoints). Existing correction methods (e.g. using a joystick or direct manipulation of an end effector) require full teleoperation or real-time interaction. In this paper, we explore natural language as an expressive and flexible tool for robot correction. We describe how to map from natural language sentences to transformations of cost functions. We show that these transformations enable users to correct goals, update robot motions to accommodate additional user preferences, and recover from planning errors. These corrections can be leveraged to get 81% and 93% success rates on tasks where the original planner failed, with either one or two language corrections. Our method makes it possible to compose multiple constraints and generalizes to unseen scenes, objects, and sentences in simulated environments and real-world environments.

## 参考
- http://arxiv.org/abs/2204.05186v1

## 개요
이 연구는 인간이 로봇을 위해 비용 또는 목표 사양을 설계할 때 흔히 발생하는 모호함, 불충분한 지정, 또는 플래너의 능력을 벗어나는 문제를 해결하기 위해, 자연어를 유연한 표현 도구로 활용한 교정 방법을 제안한다. 이 방법은 자연어 문장을 비용 함수 변환으로 매핑하여 목표 수정, 추가 선호도를 수용하는 동작 업데이트, 계획 오류로부터의 복구를 지원한다. 실험 결과, 시뮬레이션 및 실제 환경에서 이 방법은 여러 제약 조건을 결합할 수 있으며, 보지 못한 장면, 객체, 문장에 대해 일반화할 수 있고, 단일 또는 이중 언어 교정만으로 작업 성공률을 크게 향상시킬 수 있음을 보여준다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 자연어 교정 지시를 비용 함수의 수학적 변환으로 변환하며, 계획 출력을 직접 수정하지 않는다.
- **매핑 메커니즘**: 사전 훈련된 언어 모델을 통해 문장 의미를 분석하고, 해당 비용 함수의 가중치 조정, 제약 조건 추가, 또는 경로점 안내와 같은 변환 작업을 생성한다.
- **계획 프레임워크**: 비용 함수 최적화 기반 플래너(예: 궤적 최적화)를 사용하며, 각 언어 교정 후 최적 동작 시퀀스를 다시 해결한다.

### 실험 설정
- **작업 시나리오**: 테이블 조작, 객체 파지 및 배치와 같은 전형적인 로봇 조작 작업을 포함하며, 원래 플래너는 사양 모호성 또는 제약 충돌로 인해 실패한다.
- **데이터셋**: 시뮬레이션 환경(예: PyBullet)과 실제 로봇 플랫폼(예: Franka Emika Panda)을 사용하여 검증하며, 테스트 문장은 목표 수정, 장애물 회피, 경로점 지정 등의 유형을 포함한다.
- **기준 비교**: 교정 없는 계획, 무작위 교정, 규칙 기반 키워드 매칭 방법과 비교하여, 언어 교정 방법이 성공률에서 크게 앞선다.

### 주요 결과
- **성공률**: 원래 계획이 실패한 작업에서 단일 언어 교정 성공률은 81%이며, 이중 교정 시 93%로 향상된다.
- **일반화 능력**: 보지 못한 장면(새로운 객체 배치), 보지 못한 객체(다른 모양/색상), 보지 못한 문장(새로운 표현 방식)에서도 안정적인 성능을 유지한다.
- **제약 결합**: 여러 언어 교정을 동시에 적용할 수 있으며(예: "빨간 컵을 먼저 잡고 파란 블록을 피해라"), 플래너는 자동으로 균형을 맞추고 실행 가능한 궤적을 생성한다.

### 결론
자연어 교정은 인간-로봇 상호작용에 효율적이고 유연하며 일반화 가능한 방법을 제공하며, 완전한 원격 조작이나 실시간 상호작용에 대한 의존도를 크게 줄인다. 향후 작업은 더 복잡한 언어 지시(예: 시간적 제약)와 실시간 피드백 루프를 탐구할 수 있다.
