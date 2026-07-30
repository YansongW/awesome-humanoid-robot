---
$id: ent_paper_eva_client_a_unified_data_coll_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots'
  zh: 'EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots'
  ko: 'EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots'
summary:
  en: 'arXiv:2607.02646v1 Announce Type: new Abstract: We present EVA-Client, an open-source framework for deployment, data
    collection, and evaluation of trained manipulation policies on real robots. Sitting between a policy server and the physical
    hardware, EVA-Client unifies the real-robot stages of the policy iteration loop within a single codebase. It makes three
    contributions. First, a component-decoupled architecture in which robot backends, inference strategies, and transport
    middlewares form an orthogonal grid: adding a robot or a strategy touches only its own layer. Second, inspectable execution
    through Debug, Collect, and Eval workflows, with modes ranging from open-loop simulation to continuous real-time control.
    Third, every evaluation run doubles as a data collection, recording full rollouts in training-ready format alongside exhaustive
    logs and a side-by-side comparison viewer, so each evaluation feeds the next round of training rather than ending as an
    unrecorded impression. EVA-Client further consolidates major real-time inference strategies, synchronous and asynchronous
    execution, ACT-style temporal ensembling, Real-Time Chunking, and a naive-async ablation baseline, behind a single configuration
    surface.'
  zh: EVA-Client 是一个开源框架，用于在真实机器人上部署、收集数据和评估训练好的操作策略。它位于策略服务器与物理硬件之间，将策略迭代循环中的真实机器人阶段统一到单一代码库中。其核心贡献包括组件解耦架构、可检查执行工作流以及将每次评估运行同时作为数据收集。
  ko: 'arXiv:2607.02646v1 Announce Type: new Abstract: We present EVA-Client, an open-source framework for deployment, data
    collection, and evaluation of trained manipulation policies on real robots. Sitting between a policy server and the physical
    hardware, EVA-Client unifies the real-robot stages of the policy iteration loop within a single codebase. It makes three
    contributions. First, a component-decoupled architecture in which robot backends, inference strategies, and transport
    middlewares form an orthogonal grid: adding a robot or a strategy touches only its own layer. Second, inspectable execution
    through Debug, Collect, and Eval workflows, with modes ranging from open-loop simulation to continuous real-time control.
    Third, every evaluation run doubles as a data collection, recording full rollouts in training-ready format alongside exhaustive
    logs and a side-by-side comparison viewer, so each evaluation feeds the next round of training rather than ending as an
    unrecorded impression. EVA-Client further consolidates major real-time inference strategies, synchronous and asynchronous
    execution, ACT-style temporal ensembling, Real-Time Chunking, and a naive-async ablation baseline, behind a single configuration
    surface.'
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
- eva_client
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02646v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots
    (arXiv)'
  url: https://arxiv.org/abs/2607.02646
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
EVA-Client 通过组件解耦架构，将机器人后端、推理策略和传输中间件设计为正交网格，使得添加新机器人或策略时只需修改对应层。它提供 Debug、Collect 和 Eval 三种可检查执行工作流，支持从开环仿真到连续实时控制等多种模式。此外，每次评估运行都会自动记录完整的 rollout 数据，格式可直接用于训练，并附带详尽日志和并排比较视图，确保每次评估都能反馈到下一轮训练中。该框架还整合了多种实时推理策略，包括同步与异步执行、ACT 风格的时间集成、实时分块以及朴素异步消融基线，所有配置均通过统一界面管理。

## 核心内容
### 核心架构与贡献

EVA-Client 的架构围绕三个关键贡献设计：

- **组件解耦架构**：机器人后端、推理策略和传输中间件形成正交网格。添加新机器人或策略时，只需修改对应层，不影响其他组件。
- **可检查执行工作流**：提供 Debug、Collect 和 Eval 三种模式，支持从开环仿真到连续实时控制的多种运行方式，便于调试和监控。
- **评估即数据收集**：每次评估运行都会自动记录完整的 rollout 数据，格式可直接用于训练，并附带详尽日志和并排比较视图。这使得每次评估都能直接反馈到下一轮训练中，避免成为未记录的印象。

### 推理策略整合

EVA-Client 通过统一配置界面整合了多种实时推理策略：

- 同步与异步执行模式
- ACT 风格的时间集成（ACT-style temporal ensembling）
- 实时分块（Real-Time Chunking）
- 朴素异步消融基线（naive-async ablation baseline）

### 实验设置与关键数字

- 框架在真实机器人上进行了部署和评估，但摘要中未提供具体实验数字或基准结果。
- 所有评估运行均以训练就绪格式记录完整 rollout 数据，并附带详尽日志和并排比较视图。

### 结论

EVA-Client 通过统一框架简化了真实机器人上的策略迭代循环，其组件解耦架构和可检查工作流提高了开发效率，而评估即数据收集的设计确保了每次评估都能为下一轮训练提供有价值的数据。

## Overview
We present EVA-Client, an open-source framework for deployment, data collection, and evaluation of trained manipulation policies on real robots. Sitting between a policy server and the physical hardware, EVA-Client unifies the real-robot stages of the policy iteration loop within a single codebase. It makes three contributions. First, a component-decoupled architecture in which robot backends, inference strategies, and transport middlewares form an orthogonal grid: adding a robot or a strategy touches only its own layer. Second, inspectable execution through Debug, Collect, and Eval workflows, with modes ranging from open-loop simulation to continuous real-time control. Third, every evaluation run doubles as a data collection, recording full rollouts in training-ready format alongside exhaustive logs and a side-by-side comparison viewer, so each evaluation feeds the next round of training rather than ending as an unrecorded impression. EVA-Client further consolidates major real-time inference strategies, synchronous and asynchronous execution, ACT-style temporal ensembling, Real-Time Chunking, and a naive-async ablation baseline, behind a single configuration surface.

## 개요
본 논문에서는 실제 로봇에서 훈련된 조작 정책의 배포, 데이터 수집 및 평가를 위한 오픈소스 프레임워크인 EVA-Client를 제시합니다. 정책 서버와 물리적 하드웨어 사이에 위치하는 EVA-Client는 정책 반복 루프의 실제 로봇 단계를 단일 코드베이스로 통합합니다. 이 프레임워크는 세 가지 기여를 합니다. 첫째, 로봇 백엔드, 추론 전략 및 전송 미들웨어가 직교 그리드를 형성하는 컴포넌트 분리 아키텍처로, 로봇이나 전략을 추가할 때 해당 계층만 수정하면 됩니다. 둘째, Debug, Collect 및 Eval 워크플로를 통한 검사 가능한 실행으로, 개방 루프 시뮬레이션부터 연속 실시간 제어까지 다양한 모드를 지원합니다. 셋째, 모든 평가 실행은 데이터 수집을 겸하며, 훈련 준비 형식의 전체 롤아웃 기록, 포괄적인 로그 및 나란히 비교하는 뷰어를 제공하여 각 평가가 기록되지 않은 인상으로 끝나지 않고 다음 훈련 라운드에 기여하도록 합니다. EVA-Client는 또한 주요 실시간 추론 전략, 동기 및 비동기 실행, ACT 스타일의 시간적 앙상블, 실시간 청킹(Real-Time Chunking), 그리고 naive-async 절제 기준선을 단일 구성 인터페이스 뒤에 통합합니다.

## 핵심 내용
본 논문에서는 실제 로봇에서 훈련된 조작 정책의 배포, 데이터 수집 및 평가를 위한 오픈소스 프레임워크인 EVA-Client를 제시합니다. 정책 서버와 물리적 하드웨어 사이에 위치하는 EVA-Client는 정책 반복 루프의 실제 로봇 단계를 단일 코드베이스로 통합합니다. 이 프레임워크는 세 가지 기여를 합니다. 첫째, 로봇 백엔드, 추론 전략 및 전송 미들웨어가 직교 그리드를 형성하는 컴포넌트 분리 아키텍처로, 로봇이나 전략을 추가할 때 해당 계층만 수정하면 됩니다. 둘째, Debug, Collect 및 Eval 워크플로를 통한 검사 가능한 실행으로, 개방 루프 시뮬레이션부터 연속 실시간 제어까지 다양한 모드를 지원합니다. 셋째, 모든 평가 실행은 데이터 수집을 겸하며, 훈련 준비 형식의 전체 롤아웃 기록, 포괄적인 로그 및 나란히 비교하는 뷰어를 제공하여 각 평가가 기록되지 않은 인상으로 끝나지 않고 다음 훈련 라운드에 기여하도록 합니다. EVA-Client는 또한 주요 실시간 추론 전략, 동기 및 비동기 실행, ACT 스타일의 시간적 앙상블, 실시간 청킹(Real-Time Chunking), 그리고 naive-async 절제 기준선을 단일 구성 인터페이스 뒤에 통합합니다.

## 参考
- http://arxiv.org/abs/2607.02646v1
