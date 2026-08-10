---
$id: ent_paper_evolutionary_continuous_adapti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance
  zh: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance
  ko: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance
summary:
  en: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance is a 2025 work on hardware design
    for humanoid robots.
  zh: EA-CoRL 是一个 2025 年提出的进化连续自适应强化学习协同设计框架，由研究团队开发，用于人形机器人硬件与控制的联合优化。其核心贡献在于将强化学习与进化策略结合，实现控制策略对硬件设计的连续自适应，并在 RH5 人形机器人的引体向上任务中验证了有效性，获得了更高的适应度分数和更广的设计空间探索。
  ko: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance is a 2025 work on hardware design
    for humanoid robots.
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- evolutionary_continuous_adapti
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26082v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (562 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance (arXiv)
  url: https://arxiv.org/abs/2509.26082
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
传统机器人设计遵循硬件先定、控制后配的串行流程，这限制了硬件潜能的发挥。EA-CoRL 框架通过设计进化与策略连续自适应两大模块，并行优化硬件配置（如齿轮比）和控制策略。在 RH5 人形机器人的动态引体向上任务中，EA-CoRL 成功解决了因执行器限制而此前无法完成的任务，相比现有基于强化学习的协同设计方法，取得了更优的适应度分数和更广泛的设计空间探索。

## 核心内容
### 方法架构
EA-CoRL 框架包含两个核心组件：
- **设计进化（Design Evolution）**：采用进化算法探索硬件选择空间，识别高效的配置方案。
- **策略连续自适应（Policy Continuous Adaptation）**：在进化过程中，针对不断变化的设计，持续微调任务特定的控制策略，以最大化性能奖励。

### 实验设置
- **任务**：RH5 人形机器人的动态引体向上任务，该任务因执行器限制此前无法实现。
- **硬件设计参数**：协同设计执行器的齿轮比与控制策略。
- **对比方法**：与当前最先进的基于强化学习的协同设计方法进行比较。

### 关键结果
- EA-CoRL 在适应度分数上优于对比方法。
- 实现了更广泛的设计空间探索，证明了策略连续自适应在机器人协同设计中的关键作用。

## Overview
Humanoid robots have seen significant advancements in both design and control, with a growing emphasis on integrating these aspects to enhance overall performance. Traditionally, robot design has followed a sequential process, where control algorithms are developed after the hardware is finalized. However, this can be myopic and prevent robots to fully exploit their hardware capabilities. Recent approaches advocate for co-design, optimizing both design and control in parallel to maximize robotic capabilities. This paper presents the Evolutionary Continuous Adaptive RL-based Co-Design (EA-CoRL) framework, which combines reinforcement learning (RL) with evolutionary strategies to enable continuous adaptation of the control policy to the hardware. EA-CoRL comprises two key components: Design Evolution, which explores the hardware choices using an evolutionary algorithm to identify efficient configurations, and Policy Continuous Adaptation, which fine-tunes a task-specific control policy across evolving designs to maximize performance rewards. We evaluate EA-CoRL by co-designing the actuators (gear ratios) and control policy of the RH5 humanoid for a highly dynamic chin-up task, previously unfeasible due to actuator limitations. Comparative results against state-of-the-art RL-based co-design methods show that EA-CoRL achieves higher fitness score and broader design space exploration, highlighting the critical role of continuous policy adaptation in robot co-design.

## Overview
Humanoid robots have seen significant advancements in both design and control, with a growing emphasis on integrating these aspects to enhance overall performance. Traditionally, robot design has followed a sequential process, where control algorithms are developed after the hardware is finalized. However, this can be myopic and prevent robots from fully exploiting their hardware capabilities. Recent approaches advocate for co-design, optimizing both design and control in parallel to maximize robotic capabilities. This paper presents the Evolutionary Continuous Adaptive RL-based Co-Design (EA-CoRL) framework, which combines reinforcement learning (RL) with evolutionary strategies to enable continuous adaptation of the control policy to the hardware. EA-CoRL comprises two key components: Design Evolution, which explores the hardware choices using an evolutionary algorithm to identify efficient configurations, and Policy Continuous Adaptation, which fine-tunes a task-specific control policy across evolving designs to maximize performance rewards. We evaluate EA-CoRL by co-designing the actuators (gear ratios) and control policy of the RH5 humanoid for a highly dynamic chin-up task, previously unfeasible due to actuator limitations. Comparative results against state-of-the-art RL-based co-design methods show that EA-CoRL achieves higher fitness scores and broader design space exploration, highlighting the critical role of continuous policy adaptation in robot co-design.

## Content
Humanoid robots have seen significant advancements in both design and control, with a growing emphasis on integrating these aspects to enhance overall performance. Traditionally, robot design has followed a sequential process, where control algorithms are developed after the hardware is finalized. However, this can be myopic and prevent robots from fully exploiting their hardware capabilities. Recent approaches advocate for co-design, optimizing both design and control in parallel to maximize robotic capabilities. This paper presents the Evolutionary Continuous Adaptive RL-based Co-Design (EA-CoRL) framework, which combines reinforcement learning (RL) with evolutionary strategies to enable continuous adaptation of the control policy to the hardware. EA-CoRL comprises two key components: Design Evolution, which explores the hardware choices using an evolutionary algorithm to identify efficient configurations, and Policy Continuous Adaptation, which fine-tunes a task-specific control policy across evolving designs to maximize performance rewards. We evaluate EA-CoRL by co-designing the actuators (gear ratios) and control policy of the RH5 humanoid for a highly dynamic chin-up task, previously unfeasible due to actuator limitations. Comparative results against state-of-the-art RL-based co-design methods show that EA-CoRL achieves higher fitness scores and broader design space exploration, highlighting the critical role of continuous policy adaptation in robot co-design.

## 参考
- http://arxiv.org/abs/2509.26082v1

## 개요
전통적인 로봇 설계는 하드웨어를 먼저 결정하고 제어를 나중에 배치하는 직렬 프로세스를 따르며, 이는 하드웨어 잠재력의 발휘를 제한합니다. EA-CoRL 프레임워크는 설계 진화와 정책 연속 적응이라는 두 가지 모듈을 통해 하드웨어 구성(예: 기어비)과 제어 정책을 병렬로 최적화합니다. RH5 휴머노이드 로봇의 동적 턱걸이 작업에서 EA-CoRL은 액추에이터 제한으로 인해 이전에는 완료할 수 없었던 작업을 성공적으로 해결했으며, 기존 강화 학습 기반 공동 설계 방법보다 더 우수한 적합도 점수와 더 넓은 설계 공간 탐색을 달성했습니다.

## 핵심 내용
### 방법 아키텍처
EA-CoRL 프레임워크는 두 가지 핵심 구성 요소를 포함합니다:
- **설계 진화(Design Evolution)**: 진화 알고리즘을 사용하여 하드웨어 선택 공간을 탐색하고 효율적인 구성 방안을 식별합니다.
- **정책 연속 적응(Policy Continuous Adaptation)**: 진화 과정에서 변화하는 설계에 맞춰 작업별 제어 정책을 지속적으로 미세 조정하여 성능 보상을 최대화합니다.

### 실험 설정
- **작업**: RH5 휴머노이드 로봇의 동적 턱걸이 작업으로, 액추에이터 제한으로 인해 이전에는 구현할 수 없었습니다.
- **하드웨어 설계 매개변수**: 액추에이터의 기어비와 제어 정책을 공동 설계합니다.
- **비교 방법**: 현재 최첨단 강화 학습 기반 공동 설계 방법과 비교합니다.

### 주요 결과
- EA-CoRL은 적합도 점수에서 비교 방법보다 우수합니다.
- 더 넓은 설계 공간 탐색을 구현하여 로봇 공동 설계에서 정책 연속 적응의 핵심 역할을 입증했습니다.
