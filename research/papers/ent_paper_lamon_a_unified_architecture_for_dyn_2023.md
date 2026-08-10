---
$id: ent_paper_lamon_a_unified_architecture_for_dyn_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Unified Architecture for Dynamic Role Allocation and Collaborative Task Planning in Mixed Human-Robot Teams
  zh: 混合人机团队中动态角色分配与协作任务规划的统一架构
  ko: 혼합 인간-로봇 팀에서의 동적 역할 할당 및 협업 작업 계획을 위한 통합 아키텍처
summary:
  en: This paper proposes a unified architecture that combines a centralized Behavior Tree planner for action scheduling with
    a Mixed-Integer Linear Program for dynamic role allocation in mixed human-robot teams, supported by an Augmented Reality
    interface for human-system negotiation.
  zh: 本文提出一种统一架构，结合基于Behavior Trees的集中式动作调度规划器与Mixed-Integer Linear Program动态角色分配方法，并集成Augmented Reality界面实现人机协商。该架构支持任意规模的人机混合团队，在工业级任务（50个动作、20个智能体）中计算时间低于1秒，显著优于现有方法。
  ko: 본 논문은 동작 스케줄링을 위한 중앙 집중형 비헤이비어 트리 플래너와 혼합 인간-로봇 팀에서의 동적 역할 할당을 위한 혼합정수선형계획법을 결합하고, 증강 현실 인터페이스를 통해 인간-시스템 간 협상을 지원하는
    통합 아키텍처를 제안한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 03_manufacturing_processes
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- intelligence
- knowledge
- system
tags:
- behavior_tree
- mixed_integer_linear_programming
- human_robot_collaboration
- dynamic_role_allocation
- augmented_reality
- task_planning
- collaborative_manufacturing
- industrial_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2301.08038v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (867 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A Unified Architecture for Dynamic Role Allocation and Collaborative Task Planning in Mixed Human-Robot Teams
  url: https://arxiv.org/abs/2301.08038
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---
## 概述
该架构采用集中式反应型规划方法，通过Behavior Trees实现任务无关的模块化动作调度，同时利用Mixed-Integer Linear Program动态分配个体或协作角色。MILP成本函数可灵活优化不同协作指标（如完工时间、人体工学、人类偏好），人类偏好通过AR界面的协商阶段（接受/拒绝任务）确定。实验表明，该方法在工业级任务规模（50个动作、20个智能体）下计算复杂度优于文献方法，且不同成本函数下的角色分配结果展示了架构对多种生产需求的适应性。主观评估验证了高可用性和场景适用性。

## 核心内容
### 方法架构
- **核心组件**：集中式Behavior Tree规划器负责动作调度，Mixed-Integer Linear Program处理动态角色分配，Augmented Reality界面支持人机双向通信。
- **角色分配机制**：MILP成本函数可配置为最小化完工时间、优化人体工学或满足人类偏好。人类偏好通过AR界面的协商阶段实现，人类可接受/拒绝分配的任务。
- **交互设计**：AR自定义用户界面提供直观功能，在不同动作阶段协助和协调工人。

### 实验设置
- **任务规模**：工业级场景，包含最多50个动作和20个智能体（含协作任务）。
- **性能指标**：计算时间低于1秒，优于文献中的现有方法。
- **评估维度**：不同成本函数下的角色分配结果对比，以及主观可用性评估。

### 关键结果
- **计算效率**：在50个动作、20个智能体的团队规模下，所有问题均在1秒内求解。
- **灵活性验证**：改变MILP成本函数（如从最小化完工时间转向优化人体工学）时，角色分配结果显著变化，证明架构可适应不同生产需求。
- **可用性评估**：主观评价显示高可用性水平，适合目标场景。

### 结论
该统一架构通过BT与MILP的协同，实现了大规模人机混合团队的高效动态角色分配与任务规划，AR界面增强了人机协商能力。未来可扩展至更复杂的协作模式与实时优化场景。

## Overview
The growing deployment of human-robot collaborative processes in several industrial applications, such as handling, welding, and assembly, unfolds the pursuit of systems which are able to manage large heterogeneous teams and, at the same time, monitor the execution of complex tasks. In this paper, we present a novel architecture for dynamic role allocation and collaborative task planning in a mixed human-robot team of arbitrary size. The architecture capitalizes on a centralized reactive and modular task-agnostic planning method based on Behavior Trees (BTs), in charge of actions scheduling, while the allocation problem is formulated through a Mixed-Integer Linear Program (MILP), that assigns dynamically individual roles or collaborations to the agents of the team. Different metrics used as MILP cost allow the architecture to favor various aspects of the collaboration (e.g. makespan, ergonomics, human preferences). Human preference are identified through a negotiation phase, in which, an human agent can accept/refuse to execute the assigned task.In addition, bilateral communication between humans and the system is achieved through an Augmented Reality (AR) custom user interface that provides intuitive functionalities to assist and coordinate workers in different action phases. The computational complexity of the proposed methodology outperforms literature approaches in industrial sized jobs and teams (problems up to 50 actions and 20 agents in the team with collaborations are solved within 1 s). The different allocated roles, as the cost functions change, highlights the flexibility of the architecture to several production requirements. Finally, the subjective evaluation demonstrating the high usability level and the suitability for the targeted scenario.

## 参考
- http://arxiv.org/abs/2301.08038v2

## 개요
이 아키텍처는 중앙 집중식 반응형 계획 방식을 채택하여 Behavior Trees를 통해 작업 비의존적 모듈식 동작 스케줄링을 구현하고, Mixed-Integer Linear Program을 통해 개인 또는 협업 역할을 동적으로 할당합니다. MILP 비용 함수는 다양한 협업 지표(예: 완공 시간, 인간공학, 인간 선호도)를 유연하게 최적화할 수 있으며, 인간 선호도는 AR 인터페이스의 협상 단계(작업 수락/거부)를 통해 결정됩니다. 실험 결과, 이 방법은 산업 규모의 작업(50개 동작, 20개 에이전트)에서 문헌의 방법보다 계산 복잡도가 우수하며, 다양한 비용 함수에 따른 역할 할당 결과는 아키텍처가 여러 생산 요구에 적응할 수 있음을 보여줍니다. 주관적 평가는 높은 사용성과 시나리오 적용 가능성을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 구성 요소**: 중앙 집중식 Behavior Tree 계획기가 동작 스케줄링을 담당하고, Mixed-Integer Linear Program이 동적 역할 할당을 처리하며, Augmented Reality 인터페이스가 인간-로봇 양방향 통신을 지원합니다.
- **역할 할당 메커니즘**: MILP 비용 함수는 완공 시간 최소화, 인간공학 최적화 또는 인간 선호도 충족으로 구성할 수 있습니다. 인간 선호도는 AR 인터페이스의 협상 단계를 통해 구현되며, 인간은 할당된 작업을 수락하거나 거부할 수 있습니다.
- **상호작용 설계**: AR 맞춤형 사용자 인터페이스는 직관적인 기능을 제공하여 다양한 동작 단계에서 작업자를 지원하고 조정합니다.

### 실험 설정
- **작업 규모**: 최대 50개 동작과 20개 에이전트(협업 작업 포함)를 포함한 산업 규모 시나리오.
- **성능 지표**: 계산 시간이 1초 미만으로 문헌의 기존 방법보다 우수합니다.
- **평가 차원**: 다양한 비용 함수에 따른 역할 할당 결과 비교 및 주관적 사용성 평가.

### 주요 결과
- **계산 효율성**: 50개 동작, 20개 에이전트 팀 규모에서 모든 문제가 1초 내에 해결되었습니다.
- **유연성 검증**: MILP 비용 함수를 변경할 때(예: 완공 시간 최소화에서 인간공학 최적화로 전환) 역할 할당 결과가 크게 달라져 아키텍처가 다양한 생산 요구에 적응할 수 있음을 입증했습니다.
- **사용성 평가**: 주관적 평가에서 높은 사용성 수준을 보였으며, 목표 시나리오에 적합합니다.

### 결론
이 통합 아키텍처는 BT와 MILP의 협력을 통해 대규모 인간-로봇 혼합 팀의 효율적인 동적 역할 할당과 작업 계획을 구현하며, AR 인터페이스는 인간-로봇 협상 능력을 강화합니다. 향후 더 복잡한 협업 모드와 실시간 최적화 시나리오로 확장할 수 있습니다.
