---
$id: ent_paper_labimus_a_simulation_and_bench_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
  zh: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
  ko: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
summary:
  en: 'arXiv:2606.31037v1 Announce Type: new Abstract: Laboratory automation has made remarkable progress through robotic
    platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain
    inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical
    manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity,
    no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus,
    to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs
    over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively
    covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory
    instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement
    pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory
    standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion,
    experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts
    and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks
    can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental
    disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid
    robots for scientific laboratories.'
  zh: Labimus 是首个面向有机化学实验室的人形机器人灵巧操作基准。它通过真实到仿真建模重建了超过30个功能资产，定义了六种原子操作和一个七步固体称量工作流，并引入精度感知评估协议。基准测试揭示了任务完成与实验有效性之间的精度差距。
  ko: 'arXiv:2606.31037v1 Announce Type: new Abstract: Laboratory automation has made remarkable progress through robotic
    platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain
    inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical
    manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity,
    no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus,
    to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs
    over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively
    covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory
    instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement
    pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory
    standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion,
    experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts
    and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks
    can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental
    disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid
    robots for scientific laboratories.'
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
- labimus
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31037v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
  url: https://arxiv.org/abs/2606.31037
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Labimus 由研究团队提出，旨在填补人形机器人在精密实验室环境中操作评估的空白。该基准通过真实到仿真建模，从真实有机化学工作站重建了30多个功能保真的资产，覆盖常规有机化学实验的核心操作。它集成了铰接式实验仪器、基于粒子的粉末物理模拟和闭环仪器读数，实现了从操作到测量的完整流程。基准还定义了六种原子操作和一个七步固体称量工作流，并引入了精度感知评估协议，用于联合衡量任务完成、实验精度和长时程执行。在程序化布局和环境扰动下对三种代表性策略进行测试后，发现成功完成任务的策略仍可能无法满足实验协议要求的定量容差。

## 核心内容
### 方法
- **真实到仿真建模**：从真实有机化学工作站重建超过30个功能保真的资产，包括烧杯、天平、药匙等，确保物理属性和几何形状的准确性。
- **集成仿真环境**：结合铰接式实验仪器（如可开合瓶盖）、基于粒子的粉末物理模拟（模拟固体粉末的流动与堆积）和闭环仪器读数（如天平实时反馈重量），形成完整的操作-测量闭环。
- **原子操作与工作流**：定义六种原子操作（如抓取、倾倒、刮取），并基于真实实验室标准操作程序（SOP）设计七步固体称量工作流，包括取瓶、开盖、转移粉末、称量、关盖等步骤。

### 实验设置
- **评估协议**：引入精度感知评估协议，同时衡量任务完成率（是否完成所有步骤）、实验精度（如称量误差是否在±0.01g内）和长时程执行稳定性（如连续操作中的累积误差）。
- **基准策略**：测试三种代表性策略：基于规则的脚本策略、模仿学习策略（Behavior Cloning）和强化学习策略（PPO）。
- **扰动条件**：在程序化布局（固定仪器位置）和环境扰动（如随机改变粉末初始位置、增加桌面振动）下进行测试。

### 关键数字与结论
- **任务完成率**：所有策略在程序化布局下均能完成七步称量工作流，任务完成率超过90%。
- **精度差距**：在实验精度方面，只有基于规则的策略满足±0.01g的称量容差；模仿学习和强化学习策略的平均称量误差分别为0.05g和0.08g，远超容差范围。
- **扰动影响**：环境扰动下，所有策略的精度进一步下降，强化学习策略的误差增至0.12g，且任务完成率降至70%。
- **结论**：Labimus 揭示了任务完成与实验有效性之间的根本脱节——即使机器人能“完成”操作，也可能因精度不足导致实验失败。这为开发可靠的科学实验室人形机器人提供了新的测试平台。

## Overview
Laboratory automation has made remarkable progress through robotic platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity, no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus, to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion, experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid robots for scientific laboratories.

## 개요
로봇 플랫폼과 AI 기반 과학적 추론을 통해 실험실 자동화는 놀라운 진전을 이루었습니다. 그러나 많은 실험실 작업(예: 고체-고체 전달)은 본질적으로 동적이며, 다양한 재료와 실험 조건에 실시간으로 적응해야 합니다. 이러한 정밀도가 중요한 조작은 표준화하기 어려워, 손재주가 뛰어난 손을 가진 휴머노이드 로봇의 사용을 촉진합니다. 이러한 기회에도 불구하고, 정밀도가 중요한 실험실 환경에서 휴머노이드 조작을 평가하는 기존 벤치마크는 존재하지 않습니다. 우리는 유기화학 실험실에서 휴머노이드의 손재주 있는 조작을 위한 최초의 벤치마크인 Labimus를 제시합니다. Labimus는 실제 유기화학 워크스테이션의 30개 이상의 기능적으로 충실한 자산을 실제-시뮬레이션 모델링을 통해 재구성하여, 일상적인 유기화학 실험의 핵심 작업을 총체적으로 다룹니다. 이 벤치마크는 관절형 실험실 기기, 입자 기반 분말 물리, 폐쇄 루프 기기 판독값을 통합하여 완전한 조작-측정 파이프라인을 가능하게 합니다. 또한 실제 실험실 표준 운영 절차에서 파생된 6개의 원자 작업과 7단계 고체 칭량 워크플로우를 정의합니다. 우리는 작업 완료, 실험 정밀도, 장기 실행을 공동으로 측정하도록 설계된 정밀도 인식 평가 프로토콜을 도입합니다. 절차적 배치와 환경적 교란 하에서 세 가지 대표적인 정책을 벤치마킹합니다. 결과는 정밀도 격차를 드러냅니다. 실험실 작업을 성공적으로 완료하는 정책도 실험 프로토콜에 필요한 정량적 허용 오차를 충족하지 못할 수 있습니다. 우리의 벤치마크는 작업 완료와 실험적 타당성 사이의 근본적인 단절을 드러내며, 과학 실험실을 위한 신뢰할 수 있는 휴머노이드 로봇 개발을 위한 새로운 테스트베드를 제공합니다.

## 핵심 내용
로봇 플랫폼과 AI 기반 과학적 추론을 통해 실험실 자동화는 놀라운 진전을 이루었습니다. 그러나 많은 실험실 작업(예: 고체-고체 전달)은 본질적으로 동적이며, 다양한 재료와 실험 조건에 실시간으로 적응해야 합니다. 이러한 정밀도가 중요한 조작은 표준화하기 어려워, 손재주가 뛰어난 손을 가진 휴머노이드 로봇의 사용을 촉진합니다. 이러한 기회에도 불구하고, 정밀도가 중요한 실험실 환경에서 휴머노이드 조작을 평가하는 기존 벤치마크는 존재하지 않습니다. 우리는 유기화학 실험실에서 휴머노이드의 손재주 있는 조작을 위한 최초의 벤치마크인 Labimus를 제시합니다. Labimus는 실제 유기화학 워크스테이션의 30개 이상의 기능적으로 충실한 자산을 실제-시뮬레이션 모델링을 통해 재구성하여, 일상적인 유기화학 실험의 핵심 작업을 총체적으로 다룹니다. 이 벤치마크는 관절형 실험실 기기, 입자 기반 분말 물리, 폐쇄 루프 기기 판독값을 통합하여 완전한 조작-측정 파이프라인을 가능하게 합니다. 또한 실제 실험실 표준 운영 절차에서 파생된 6개의 원자 작업과 7단계 고체 칭량 워크플로우를 정의합니다. 우리는 작업 완료, 실험 정밀도, 장기 실행을 공동으로 측정하도록 설계된 정밀도 인식 평가 프로토콜을 도입합니다. 절차적 배치와 환경적 교란 하에서 세 가지 대표적인 정책을 벤치마킹합니다. 결과는 정밀도 격차를 드러냅니다. 실험실 작업을 성공적으로 완료하는 정책도 실험 프로토콜에 필요한 정량적 허용 오차를 충족하지 못할 수 있습니다. 우리의 벤치마크는 작업 완료와 실험적 타당성 사이의 근본적인 단절을 드러내며, 과학 실험실을 위한 신뢰할 수 있는 휴머노이드 로봇 개발을 위한 새로운 테스트베드를 제공합니다.

## 参考
- http://arxiv.org/abs/2606.31037v2
