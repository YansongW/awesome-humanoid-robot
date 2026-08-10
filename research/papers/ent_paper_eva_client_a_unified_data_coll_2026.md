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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02646v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (931 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.02646v1

## 개요
EVA-Client는 컴포넌트 분리 아키텍처를 통해 로봇 백엔드, 추론 전략, 전송 미들웨어를 직교 그리드로 설계하여, 새 로봇이나 전략을 추가할 때 해당 레이어만 수정하면 되도록 합니다. Debug, Collect, Eval 세 가지 검사 가능한 실행 워크플로우를 제공하며, 개루프 시뮬레이션부터 연속 실시간 제어까지 다양한 모드를 지원합니다. 또한, 각 평가 실행은 전체 롤아웃 데이터를 자동으로 기록하며, 해당 형식은 훈련에 직접 사용할 수 있고, 상세 로그와 병렬 비교 뷰가 포함되어 있어 매 평가가 다음 훈련 라운드에 피드백될 수 있도록 보장합니다. 이 프레임워크는 동기 및 비동기 실행, ACT 스타일 시간 통합, 실시간 청킹, 순수 비동기 절제 베이스라인을 포함한 여러 실시간 추론 전략을 통합하며, 모든 구성은 통합 인터페이스로 관리됩니다.

## 핵심 내용
### 핵심 아키텍처 및 기여

EVA-Client의 아키텍처는 세 가지 핵심 기여를 중심으로 설계되었습니다:

- **컴포넌트 분리 아키텍처**: 로봇 백엔드, 추론 전략, 전송 미들웨어가 직교 그리드를 형성합니다. 새 로봇이나 전략을 추가할 때 해당 레이어만 수정하면 되며, 다른 컴포넌트에는 영향을 미치지 않습니다.
- **검사 가능한 실행 워크플로우**: Debug, Collect, Eval 세 가지 모드를 제공하며, 개루프 시뮬레이션부터 연속 실시간 제어까지 다양한 실행 방식을 지원하여 디버깅과 모니터링을 용이하게 합니다.
- **평가 즉 데이터 수집**: 각 평가 실행은 전체 롤아웃 데이터를 자동으로 기록하며, 해당 형식은 훈련에 직접 사용할 수 있고, 상세 로그와 병렬 비교 뷰가 포함됩니다. 이를 통해 매 평가가 다음 훈련 라운드에 직접 피드백되어 기록되지 않은 인상으로 남지 않도록 합니다.

### 추론 전략 통합

EVA-Client는 통합 구성 인터페이스를 통해 여러 실시간 추론 전략을 통합합니다:

- 동기 및 비동기 실행 모드
- ACT 스타일 시간 통합 (ACT-style temporal ensembling)
- 실시간 청킹 (Real-Time Chunking)
- 순수 비동기 절제 베이스라인 (naive-async ablation baseline)

### 실험 설정 및 핵심 수치

- 프레임워크는 실제 로봇에 배포 및 평가되었지만, 요약에는 구체적인 실험 수치나 벤치마크 결과가 제공되지 않았습니다.
- 모든 평가 실행은 훈련 준비 형식으로 전체 롤아웃 데이터를 기록하며, 상세 로그와 병렬 비교 뷰가 포함됩니다.

### 결론

EVA-Client는 통합 프레임워크를 통해 실제 로봇에서의 전략 반복 루프를 단순화하며, 컴포넌트 분리 아키텍처와 검사 가능한 워크플로우는 개발 효율성을 높이고, 평가 즉 데이터 수집 설계는 매 평가가 다음 훈련 라운드에 가치 있는 데이터를 제공하도록 보장합니다.
