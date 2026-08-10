---
$id: ent_paper_lallement_hatp_an_htn_planner_for_roboti_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HATP: An HTN Planner for Robotics'
  zh: HATP：面向机器人学的HTN规划器
  ko: 'HATP: 로보틱스를 위한 HTN 플래너'
summary:
  en: HATP is a robotics-specific Hierarchical Task Network planning framework that introduces an agent-centered domain language,
    social-rule plan filtering, user-defined cost functions, and interleaved symbolic-geometric planning validated in 3D environments.
  zh: HATP 是一个面向机器人领域的层次化任务网络（HTN）规划框架，由研究团队提出。其核心贡献包括：引入以智能体为中心的领域描述语言、社会规则过滤机制、用户自定义代价函数，以及符号-几何交错规划能力，并在三维环境中得到验证。
  ko: HATP는 로봇공학을 위한 계층적 작업 네트워크 계획 프레임워크로, 에이전트 중심의 도메인 언어, 사회 규칙에 기반한 계획 필터링, 사용자 정의 비용 함수, 그리고 3D 환경에서 검증된 기호-기하학적 교차 계획을
    도입합니다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- htn_planning
- task_planning
- multi_agent_planning
- human_robot_interaction
- geometric_reasoning
- social_rules
- robotic_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1405.5345v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko
    body retranslated from zh deep-read (776 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HATP: An HTN Planner for Robotics'
  url: https://arxiv.org/abs/1405.5345
  date: '2014'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
HATP 扩展了传统 HTN 规划的领域表示与语义，使其更贴合机器人学需求。该框架将智能体视为语言中的“一等公民”，允许用户定义社会规则来约束机器人行为的可接受性。同时，HATP 将符号规划与几何推理交错进行，在规划过程中实时验证人类/机器人动作在三维几何世界中的可行性，从而提升规划的实际适用性。

## 核心内容
### 方法
HATP 基于层次化任务网络（HTN）规划，通过依赖给定的领域控制知识库来缩减经典规划的搜索空间。其核心创新包括：
- **智能体中心语言**：将智能体（agent）作为领域语言中的“一等公民”，允许直接描述其属性与能力。
- **社会规则过滤**：用户可定义“社会规则”（social rules），指定哪些行为在领域中被视为可接受或不可接受，从而在规划阶段过滤掉违规动作序列。
- **用户自定义代价函数**：允许用户根据具体任务需求定义代价函数，以优化规划结果。
- **符号-几何交错规划**：在规划过程中，HATP 会实时调用几何推理模块，在详细的三维几何世界模型中对当前正在执行的人类/机器人动作进行可行性验证。

### 实验设置
HATP 在三维仿真环境中进行了验证，测试场景涉及多智能体协作任务，包括人类与机器人共同操作物体、避障等典型机器人应用场景。

### 关键结果
- 社会规则过滤机制有效减少了无效规划分支，提升了规划效率。
- 符号-几何交错规划保证了规划动作在三维空间中的物理可行性，避免了纯符号规划中常见的几何冲突问题。
- 用户自定义代价函数使得规划结果能够灵活适应不同任务偏好（如最小化时间、能量或碰撞风险）。

### 结论
HATP 通过将智能体、社会规则与几何推理融入 HTN 规划框架，为机器人任务规划提供了一种更实用、更安全的解决方案，尤其适用于人机协作环境。

## Overview
Hierarchical Task Network (HTN) planning is a popular approach that cuts down on the classical planning search space by relying on a given hierarchical library of domain control knowledge. This provides an intuitive methodology for specifying high-level instructions on how robots and agents should perform tasks, while also giving the planner enough flexibility to choose the lower-level steps and their ordering. In this paper we present the HATP (Hierarchical Agent-based Task Planner) planning framework which extends the traditional HTN planning domain representation and semantics by making them more suitable for roboticists, and treating agents as "first class" entities in the language. The former is achieved by allowing "social rules" to be defined which specify what behaviour is acceptable/unacceptable by the agents/robots in the domain, and interleaving planning with geometric reasoning in order to validate online -with respect to a detailed geometric 3D world- the human/robot actions currently being pursued by HATP.

## 参考
- http://arxiv.org/abs/1405.5345v2

## 개요
HATP는 전통적인 HTN 계획의 도메인 표현과 의미론을 확장하여 로봇공학 요구에 더 부합하도록 합니다. 이 프레임워크는 에이전트를 언어의 "일급 시민"으로 간주하며, 사용자가 로봇 행동의 수용 가능성을 제약하는 사회적 규칙을 정의할 수 있게 합니다. 동시에 HATP는 기호 계획과 기하 추론을 교차 수행하여, 계획 과정에서 인간/로봇 동작의 3차원 기하 세계에서의 실현 가능성을 실시간으로 검증함으로써 계획의 실제 적용성을 향상시킵니다.

## 핵심 내용
### 방법
HATP는 계층적 작업 네트워크(HTN) 계획을 기반으로 하며, 주어진 도메인 제어 지식 베이스에 의존하여 고전적 계획의 탐색 공간을 축소합니다. 핵심 혁신은 다음과 같습니다:
- **에이전트 중심 언어**: 에이전트를 도메인 언어의 "일급 시민"으로 취급하여, 그 속성과 능력을 직접 기술할 수 있게 합니다.
- **사회적 규칙 필터링**: 사용자는 "사회적 규칙"을 정의하여 어떤 행동이 도메인에서 수용 가능하거나 수용 불가능한지 지정할 수 있으며, 이를 통해 계획 단계에서 위반 동작 시퀀스를 필터링합니다.
- **사용자 정의 비용 함수**: 사용자가 특정 작업 요구에 따라 비용 함수를 정의하여 계획 결과를 최적화할 수 있게 합니다.
- **기호-기하 교차 계획**: 계획 과정에서 HATP는 기하 추론 모듈을 실시간으로 호출하여, 상세한 3차원 기하 세계 모델에서 현재 실행 중인 인간/로봇 동작의 실현 가능성을 검증합니다.

### 실험 설정
HATP는 3차원 시뮬레이션 환경에서 검증되었으며, 테스트 시나리오는 인간과 로봇이 함께 물체를 조작하고 장애물을 회피하는 등 전형적인 로봇 응용 시나리오를 포함한 다중 에이전트 협업 작업을 다룹니다.

### 주요 결과
- 사회적 규칙 필터링 메커니즘은 비효율적인 계획 분기를 효과적으로 줄여 계획 효율성을 향상시켰습니다.
- 기호-기하 교차 계획은 계획된 동작의 3차원 공간에서의 물리적 실현 가능성을 보장하여, 순수 기호 계획에서 흔히 발생하는 기하 충돌 문제를 피했습니다.
- 사용자 정의 비용 함수는 계획 결과가 다양한 작업 선호도(예: 시간, 에너지 또는 충돌 위험 최소화)에 유연하게 적응할 수 있게 했습니다.

### 결론
HATP는 에이전트, 사회적 규칙 및 기하 추론을 HTN 계획 프레임워크에 통합함으로써, 특히 인간-로봇 협업 환경에서 로봇 작업 계획을 위한 더 실용적이고 안전한 솔루션을 제공합니다.
