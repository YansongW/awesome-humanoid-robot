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
  zh: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance is a 2025 work on hardware design
    for humanoid robots.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26082v1.
sources:
- id: src_001
  type: paper
  title: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance (arXiv)
  url: https://arxiv.org/abs/2509.26082
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have seen significant advancements in both design and control, with a growing emphasis on integrating these aspects to enhance overall performance. Traditionally, robot design has followed a sequential process, where control algorithms are developed after the hardware is finalized. However, this can be myopic and prevent robots to fully exploit their hardware capabilities. Recent approaches advocate for co-design, optimizing both design and control in parallel to maximize robotic capabilities. This paper presents the Evolutionary Continuous Adaptive RL-based Co-Design (EA-CoRL) framework, which combines reinforcement learning (RL) with evolutionary strategies to enable continuous adaptation of the control policy to the hardware. EA-CoRL comprises two key components: Design Evolution, which explores the hardware choices using an evolutionary algorithm to identify efficient configurations, and Policy Continuous Adaptation, which fine-tunes a task-specific control policy across evolving designs to maximize performance rewards. We evaluate EA-CoRL by co-designing the actuators (gear ratios) and control policy of the RH5 humanoid for a highly dynamic chin-up task, previously unfeasible due to actuator limitations. Comparative results against state-of-the-art RL-based co-design methods show that EA-CoRL achieves higher fitness score and broader design space exploration, highlighting the critical role of continuous policy adaptation in robot co-design.

## 核心内容
Humanoid robots have seen significant advancements in both design and control, with a growing emphasis on integrating these aspects to enhance overall performance. Traditionally, robot design has followed a sequential process, where control algorithms are developed after the hardware is finalized. However, this can be myopic and prevent robots to fully exploit their hardware capabilities. Recent approaches advocate for co-design, optimizing both design and control in parallel to maximize robotic capabilities. This paper presents the Evolutionary Continuous Adaptive RL-based Co-Design (EA-CoRL) framework, which combines reinforcement learning (RL) with evolutionary strategies to enable continuous adaptation of the control policy to the hardware. EA-CoRL comprises two key components: Design Evolution, which explores the hardware choices using an evolutionary algorithm to identify efficient configurations, and Policy Continuous Adaptation, which fine-tunes a task-specific control policy across evolving designs to maximize performance rewards. We evaluate EA-CoRL by co-designing the actuators (gear ratios) and control policy of the RH5 humanoid for a highly dynamic chin-up task, previously unfeasible due to actuator limitations. Comparative results against state-of-the-art RL-based co-design methods show that EA-CoRL achieves higher fitness score and broader design space exploration, highlighting the critical role of continuous policy adaptation in robot co-design.

## 参考
- http://arxiv.org/abs/2509.26082v1

## Overview
Humanoid robots have seen significant advancements in both design and control, with a growing emphasis on integrating these aspects to enhance overall performance. Traditionally, robot design has followed a sequential process, where control algorithms are developed after the hardware is finalized. However, this can be myopic and prevent robots from fully exploiting their hardware capabilities. Recent approaches advocate for co-design, optimizing both design and control in parallel to maximize robotic capabilities. This paper presents the Evolutionary Continuous Adaptive RL-based Co-Design (EA-CoRL) framework, which combines reinforcement learning (RL) with evolutionary strategies to enable continuous adaptation of the control policy to the hardware. EA-CoRL comprises two key components: Design Evolution, which explores the hardware choices using an evolutionary algorithm to identify efficient configurations, and Policy Continuous Adaptation, which fine-tunes a task-specific control policy across evolving designs to maximize performance rewards. We evaluate EA-CoRL by co-designing the actuators (gear ratios) and control policy of the RH5 humanoid for a highly dynamic chin-up task, previously unfeasible due to actuator limitations. Comparative results against state-of-the-art RL-based co-design methods show that EA-CoRL achieves higher fitness scores and broader design space exploration, highlighting the critical role of continuous policy adaptation in robot co-design.

## Content
Humanoid robots have seen significant advancements in both design and control, with a growing emphasis on integrating these aspects to enhance overall performance. Traditionally, robot design has followed a sequential process, where control algorithms are developed after the hardware is finalized. However, this can be myopic and prevent robots from fully exploiting their hardware capabilities. Recent approaches advocate for co-design, optimizing both design and control in parallel to maximize robotic capabilities. This paper presents the Evolutionary Continuous Adaptive RL-based Co-Design (EA-CoRL) framework, which combines reinforcement learning (RL) with evolutionary strategies to enable continuous adaptation of the control policy to the hardware. EA-CoRL comprises two key components: Design Evolution, which explores the hardware choices using an evolutionary algorithm to identify efficient configurations, and Policy Continuous Adaptation, which fine-tunes a task-specific control policy across evolving designs to maximize performance rewards. We evaluate EA-CoRL by co-designing the actuators (gear ratios) and control policy of the RH5 humanoid for a highly dynamic chin-up task, previously unfeasible due to actuator limitations. Comparative results against state-of-the-art RL-based co-design methods show that EA-CoRL achieves higher fitness scores and broader design space exploration, highlighting the critical role of continuous policy adaptation in robot co-design.

## 개요
휴머노이드 로봇은 설계와 제어 모두에서 상당한 발전을 이루었으며, 이러한 측면을 통합하여 전반적인 성능을 향상시키는 데 점점 더 중점을 두고 있습니다. 전통적으로 로봇 설계는 하드웨어가 최종 확정된 후에 제어 알고리즘이 개발되는 순차적 프로세스를 따랐습니다. 그러나 이는 근시안적일 수 있으며 로봇이 하드웨어 성능을 완전히 활용하지 못하게 할 수 있습니다. 최근 접근 방식은 설계와 제어를 병렬로 최적화하여 로봇의 성능을 극대화하는 공동 설계(co-design)를 지지합니다. 본 논문은 강화 학습(RL)과 진화 전략을 결합하여 제어 정책을 하드웨어에 지속적으로 적응시킬 수 있는 EA-CoRL(Evolutionary Continuous Adaptive RL-based Co-Design) 프레임워크를 제시합니다. EA-CoRL은 두 가지 핵심 구성 요소로 이루어져 있습니다: 진화 알고리즘을 사용하여 효율적인 구성을 식별하기 위해 하드웨어 선택을 탐색하는 설계 진화(Design Evolution)와, 진화하는 설계 전반에 걸쳐 작업별 제어 정책을 미세 조정하여 성능 보상을 극대화하는 정책 지속 적응(Policy Continuous Adaptation)입니다. 우리는 EA-CoRL을 평가하기 위해 이전에는 액추에이터 한계로 인해 불가능했던 고동적 턱걸이(chin-up) 작업을 위해 RH5 휴머노이드의 액추에이터(기어비)와 제어 정책을 공동 설계했습니다. 최신 RL 기반 공동 설계 방법과의 비교 결과, EA-CoRL은 더 높은 적합도 점수와 더 넓은 설계 공간 탐색을 달성하여 로봇 공동 설계에서 지속적인 정책 적응의 중요한 역할을 강조합니다.

## 핵심 내용
휴머노이드 로봇은 설계와 제어 모두에서 상당한 발전을 이루었으며, 이러한 측면을 통합하여 전반적인 성능을 향상시키는 데 점점 더 중점을 두고 있습니다. 전통적으로 로봇 설계는 하드웨어가 최종 확정된 후에 제어 알고리즘이 개발되는 순차적 프로세스를 따랐습니다. 그러나 이는 근시안적일 수 있으며 로봇이 하드웨어 성능을 완전히 활용하지 못하게 할 수 있습니다. 최근 접근 방식은 설계와 제어를 병렬로 최적화하여 로봇의 성능을 극대화하는 공동 설계(co-design)를 지지합니다. 본 논문은 강화 학습(RL)과 진화 전략을 결합하여 제어 정책을 하드웨어에 지속적으로 적응시킬 수 있는 EA-CoRL(Evolutionary Continuous Adaptive RL-based Co-Design) 프레임워크를 제시합니다. EA-CoRL은 두 가지 핵심 구성 요소로 이루어져 있습니다: 진화 알고리즘을 사용하여 효율적인 구성을 식별하기 위해 하드웨어 선택을 탐색하는 설계 진화(Design Evolution)와, 진화하는 설계 전반에 걸쳐 작업별 제어 정책을 미세 조정하여 성능 보상을 극대화하는 정책 지속 적응(Policy Continuous Adaptation)입니다. 우리는 EA-CoRL을 평가하기 위해 이전에는 액추에이터 한계로 인해 불가능했던 고동적 턱걸이(chin-up) 작업을 위해 RH5 휴머노이드의 액추에이터(기어비)와 제어 정책을 공동 설계했습니다. 최신 RL 기반 공동 설계 방법과의 비교 결과, EA-CoRL은 더 높은 적합도 점수와 더 넓은 설계 공간 탐색을 달성하여 로봇 공동 설계에서 지속적인 정책 적응의 중요한 역할을 강조합니다.
