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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1709.05435v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
모듈형 로봇이 사전에 알려지지 않은 환경에서 복잡한 작업에 대응하여 재구성할 수 있는 이론적 능력은 자주 장점으로 언급되어 왔으며, 이 분야 연구의 주요 동기로 남아 있습니다. 우리는 인지된 사전 미지의 환경의 요구에 반응적으로 재구성함으로써 고수준 작업을 자율적으로 완료할 수 있는 모듈형 로봇 시스템을 제시합니다. 이 시스템은 인식, 고수준 계획 및 모듈형 하드웨어를 통합하며, 세 가지 하드웨어 데모를 통해 검증되었습니다. 고수준 작업 사양이 주어지면 모듈형 로봇은 미지의 환경을 자율적으로 탐색하고, 언제 어떻게 재구성할지 결정하며, 객체를 조작하여 작업을 완료합니다. 시스템 아키텍처는 분산된 기계적 요소와 중앙 집중식 인식, 계획 및 제어 간의 균형을 유지합니다. 미지의 환경에서 반응적 재구성 가능성을 활용하도록 모듈형 로봇 시스템을 설계하는 방법의 예를 제공함으로써, 우리는 모듈형 자가 재구성 로봇이 실제 세계의 작업을 처리할 수 있는 기반을 마련하기 시작했습니다.

## 핵심 내용
모듈형 로봇이 사전에 알려지지 않은 환경에서 복잡한 작업에 대응하여 재구성할 수 있는 이론적 능력은 자주 장점으로 언급되어 왔으며, 이 분야 연구의 주요 동기로 남아 있습니다. 우리는 인지된 사전 미지의 환경의 요구에 반응적으로 재구성함으로써 고수준 작업을 자율적으로 완료할 수 있는 모듈형 로봇 시스템을 제시합니다. 이 시스템은 인식, 고수준 계획 및 모듈형 하드웨어를 통합하며, 세 가지 하드웨어 데모를 통해 검증되었습니다. 고수준 작업 사양이 주어지면 모듈형 로봇은 미지의 환경을 자율적으로 탐색하고, 언제 어떻게 재구성할지 결정하며, 객체를 조작하여 작업을 완료합니다. 시스템 아키텍처는 분산된 기계적 요소와 중앙 집중식 인식, 계획 및 제어 간의 균형을 유지합니다. 미지의 환경에서 반응적 재구성 가능성을 활용하도록 모듈형 로봇 시스템을 설계하는 방법의 예를 제공함으로써, 우리는 모듈형 자가 재구성 로봇이 실제 세계의 작업을 처리할 수 있는 기반을 마련하기 시작했습니다.

## 参考
- http://arxiv.org/abs/1709.05435v2
