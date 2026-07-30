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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26082v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
휴머노이드 로봇은 설계와 제어 모두에서 상당한 발전을 이루었으며, 이러한 측면을 통합하여 전반적인 성능을 향상시키는 데 점점 더 중점을 두고 있습니다. 전통적으로 로봇 설계는 하드웨어가 최종 확정된 후에 제어 알고리즘이 개발되는 순차적 프로세스를 따랐습니다. 그러나 이는 근시안적일 수 있으며 로봇이 하드웨어 성능을 완전히 활용하지 못하게 할 수 있습니다. 최근 접근 방식은 설계와 제어를 병렬로 최적화하여 로봇의 성능을 극대화하는 공동 설계(co-design)를 지지합니다. 본 논문은 강화 학습(RL)과 진화 전략을 결합하여 제어 정책을 하드웨어에 지속적으로 적응시킬 수 있는 EA-CoRL(Evolutionary Continuous Adaptive RL-based Co-Design) 프레임워크를 제시합니다. EA-CoRL은 두 가지 핵심 구성 요소로 이루어져 있습니다: 진화 알고리즘을 사용하여 효율적인 구성을 식별하기 위해 하드웨어 선택을 탐색하는 설계 진화(Design Evolution)와, 진화하는 설계 전반에 걸쳐 작업별 제어 정책을 미세 조정하여 성능 보상을 극대화하는 정책 지속 적응(Policy Continuous Adaptation)입니다. 우리는 EA-CoRL을 평가하기 위해 이전에는 액추에이터 한계로 인해 불가능했던 고동적 턱걸이(chin-up) 작업을 위해 RH5 휴머노이드의 액추에이터(기어비)와 제어 정책을 공동 설계했습니다. 최신 RL 기반 공동 설계 방법과의 비교 결과, EA-CoRL은 더 높은 적합도 점수와 더 넓은 설계 공간 탐색을 달성하여 로봇 공동 설계에서 지속적인 정책 적응의 중요한 역할을 강조합니다.

## 핵심 내용
휴머노이드 로봇은 설계와 제어 모두에서 상당한 발전을 이루었으며, 이러한 측면을 통합하여 전반적인 성능을 향상시키는 데 점점 더 중점을 두고 있습니다. 전통적으로 로봇 설계는 하드웨어가 최종 확정된 후에 제어 알고리즘이 개발되는 순차적 프로세스를 따랐습니다. 그러나 이는 근시안적일 수 있으며 로봇이 하드웨어 성능을 완전히 활용하지 못하게 할 수 있습니다. 최근 접근 방식은 설계와 제어를 병렬로 최적화하여 로봇의 성능을 극대화하는 공동 설계(co-design)를 지지합니다. 본 논문은 강화 학습(RL)과 진화 전략을 결합하여 제어 정책을 하드웨어에 지속적으로 적응시킬 수 있는 EA-CoRL(Evolutionary Continuous Adaptive RL-based Co-Design) 프레임워크를 제시합니다. EA-CoRL은 두 가지 핵심 구성 요소로 이루어져 있습니다: 진화 알고리즘을 사용하여 효율적인 구성을 식별하기 위해 하드웨어 선택을 탐색하는 설계 진화(Design Evolution)와, 진화하는 설계 전반에 걸쳐 작업별 제어 정책을 미세 조정하여 성능 보상을 극대화하는 정책 지속 적응(Policy Continuous Adaptation)입니다. 우리는 EA-CoRL을 평가하기 위해 이전에는 액추에이터 한계로 인해 불가능했던 고동적 턱걸이(chin-up) 작업을 위해 RH5 휴머노이드의 액추에이터(기어비)와 제어 정책을 공동 설계했습니다. 최신 RL 기반 공동 설계 방법과의 비교 결과, EA-CoRL은 더 높은 적합도 점수와 더 넓은 설계 공간 탐색을 달성하여 로봇 공동 설계에서 지속적인 정책 적응의 중요한 역할을 강조합니다.

## 参考
- http://arxiv.org/abs/2509.26082v1
