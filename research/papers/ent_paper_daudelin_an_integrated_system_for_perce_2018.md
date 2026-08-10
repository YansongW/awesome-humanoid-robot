---
$id: ent_paper_daudelin_an_integrated_system_for_perce_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: An Integrated System for Perception-Driven Autonomy with Modular Robots
  zh: 面向模块化机器人的感知驱动自主集成系统
  ko: 모듈형 로봇을 위한 지각 기반 자율 통합 시스템
summary:
  en: Presents a modular robot system that combines centralized perception, mapping, and LTL-based high-level planning with
    distributed SMORES-EP hardware so the robot can autonomously explore unknown environments, decide when and how to reconfigure,
    and manipulate objects to complete tasks, validated in three hardware demonstrations.
  zh: 本文提出了一套集成感知驱动自主性的模块化机器人系统，结合集中式感知、地图构建、LTL 高层规划与分布式 SMORES-EP 硬件，使机器人能在未知环境中自主探索、决定何时及如何重构，并操作物体完成任务，通过三项硬件演示验证了系统有效性。
  ko: 중앙 집중식 인지, 매핑 및 LTL 기반 고수준 계획을 분산형 SMORES-EP 하드웨어와 결합하여 로봇이 미지 환경을 자율 탐색하고, 언제 어떻게 재구성할지 결정하며, 물체를 조작해 작업을 완료할 수 있게
    하는 모듈형 로봇 시스템을 제시하고 세 가지 하드웨어 시연으로 검증하였다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- intelligence
- system
- knowledge
tags:
- modular_robotics
- self_reconfigurable_robotics
- smores_ep
- ltl_planning
- reactive_reconfiguration
- perception_planning_integration
- apriltag_localization
- rgb_d_perception
- autonomous_exploration
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1709.05435v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (724 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: An Integrated System for Perception-Driven Autonomy with Modular Robots
  url: https://arxiv.org/abs/1709.05435
  date: '2018'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该研究由团队开发，旨在实现模块化机器人在未知环境中的自主重构与任务执行。系统架构融合了集中式感知与规划模块（包括环境感知、地图构建和基于 LTL 的高层任务规划）与分布式 SMORES-EP 硬件模块。机器人能够根据高层任务规范，自主探索未知环境，动态判断重构时机与方式，并通过操作物体完成指定任务。三项硬件演示证明了系统在真实场景中的可行性，为模块化自重构机器人走向实际应用奠定了基础。

## 核心内容
### 系统架构
- **集中式感知与规划**：系统采用集中式模块处理环境感知、地图构建和基于 LTL（线性时序逻辑）的高层任务规划，确保全局决策的一致性。
- **分布式硬件**：底层采用 SMORES-EP 模块化机器人硬件，各模块具备分布式执行能力，支持灵活重构。

### 核心功能
- **自主探索**：机器人在未知环境中自主移动，通过感知模块实时构建环境地图。
- **动态重构**：基于感知结果和 LTL 规划，机器人自主决定重构时机（如遇到障碍或任务需求变化）及重构方式（如改变形态以通过狭窄空间）。
- **物体操作**：完成重构后，机器人可操作环境中的物体，以达成高层任务目标。

### 实验验证
- **三项硬件演示**：系统在真实硬件平台上进行了三项演示，验证了从探索、重构到任务完成的完整流程。
- **关键结果**：演示表明，机器人能够成功应对未知环境中的动态变化，通过反应式重构完成指定任务，例如穿越障碍或搬运物体。

### 结论
本研究通过集成感知、规划与模块化硬件，展示了模块化机器人在未知环境中实现自主重构与任务执行的可行性，为未来模块化自重构机器人在现实世界中的应用提供了系统设计范例。

## Overview
The theoretical ability of modular robots to reconfigure in response to complex tasks in a priori unknown environments has frequently been cited as an advantage and remains a major motivator for work in the field. We present a modular robot system capable of autonomously completing high-level tasks by reactively reconfiguring to meet the needs of a perceived, a priori unknown environment. The system integrates perception, high-level planning, and modular hardware, and is validated in three hardware demonstrations. Given a high-level task specification, a modular robot autonomously explores an unknown environment, decides when and how to reconfigure, and manipulates objects to complete its task. The system architecture balances distributed mechanical elements with centralized perception, planning, and control. By providing an example of how a modular robot system can be designed to leverage reactive reconfigurability in unknown environments, we have begun to lay the groundwork for modular self-reconfigurable robots to address tasks in the real world.

## 参考
- http://arxiv.org/abs/1709.05435v2

## 개요
이 연구는 팀에 의해 개발되었으며, 모듈형 로봇이未知 환경에서 자율적으로 재구성하고 작업을 수행하는 것을 목표로 합니다. 시스템 아키텍처는 중앙 집중식 인식 및 계획 모듈(환경 인식, 지도 구축, LTL 기반 고수준 작업 계획 포함)과 분산형 SMORES-EP 하드웨어 모듈을 통합합니다. 로봇은 고수준 작업 사양에 따라未知 환경을 자율적으로 탐색하고, 재구성 시점과 방식을 동적으로 판단하며, 객체를 조작하여 지정된 작업을 완료할 수 있습니다. 세 가지 하드웨어 데모는 실제 시나리오에서 시스템의 실현 가능성을 입증하며, 모듈형 자가 재구성 로봇의 실제 응용으로 나아가는 기반을 마련했습니다.

## 핵심 내용
### 시스템 아키텍처
- **중앙 집중식 인식 및 계획**: 시스템은 중앙 집중식 모듈을 사용하여 환경 인식, 지도 구축 및 LTL(선형 시간 논리) 기반 고수준 작업 계획을 처리하여 전역 결정의 일관성을 보장합니다.
- **분산형 하드웨어**: 하위 계층은 SMORES-EP 모듈형 로봇 하드웨어를 사용하며, 각 모듈은 분산 실행 능력을 갖추어 유연한 재구성을 지원합니다.

### 핵심 기능
- **자율 탐색**: 로봇은未知 환경에서 자율적으로 이동하며, 인식 모듈을 통해 실시간으로 환경 지도를 구축합니다.
- **동적 재구성**: 인식 결과와 LTL 계획을 기반으로, 로봇은 재구성 시점(예: 장애물 직면 또는 작업 요구 변화)과 재구성 방식(예: 좁은 공간 통과를 위한 형태 변경)을 자율적으로 결정합니다.
- **객체 조작**: 재구성 완료 후, 로봇은 환경 내 객체를 조작하여 고수준 작업 목표를 달성할 수 있습니다.

### 실험 검증
- **세 가지 하드웨어 데모**: 시스템은 실제 하드웨어 플랫폼에서 세 가지 데모를 수행하여 탐색부터 재구성, 작업 완료까지의 전체 프로세스를 검증했습니다.
- **핵심 결과**: 데모는 로봇이未知 환경의 동적 변화에 성공적으로 대응하고, 반응형 재구성을 통해 장애물 통과나 객체 운반과 같은 지정된 작업을 완료할 수 있음을 보여주었습니다.

### 결론
이 연구는 인식, 계획 및 모듈형 하드웨어를 통합하여 모듈형 로봇이未知 환경에서 자율 재구성과 작업 수행의 실현 가능성을 입증했으며, 향후 모듈형 자가 재구성 로봇의 실제 세계 응용을 위한 시스템 설계 사례를 제공합니다.
