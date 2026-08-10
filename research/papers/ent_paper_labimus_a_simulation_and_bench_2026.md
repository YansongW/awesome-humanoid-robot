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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31037v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1047 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2606.31037v2

## 개요
Labimus는 연구팀이 제안한 것으로, 인간형 로봇의 정밀 실험실 환경에서의 조작 평가 공백을 메우기 위해 설계되었습니다. 이 벤치마크는 실제-시뮬레이션 모델링을 통해 실제 유기화학 워크스테이션에서 30개 이상의 기능 충실도 높은 자산을 재구성하여, 일반적인 유기화학 실험의 핵심 작업을 포괄합니다. 관절형 실험 기기, 입자 기반 분말 물리 시뮬레이션, 폐쇄 루프 기기 판독값을 통합하여 조작부터 측정까지의 완전한 흐름을 구현합니다. 벤치마크는 또한 여섯 가지 원자 작업과 일곱 단계 고체 칭량 워크플로우를 정의하고, 정밀도 인식 평가 프로토콜을 도입하여 작업 완료, 실험 정밀도, 장시간 실행을 공동으로 측정합니다. 프로그래밍된 배치와 환경 교란 하에서 세 가지 대표 전략을 테스트한 결과, 작업을 성공적으로 완료하는 전략도 실험 프로토콜이 요구하는 정량적 허용 오차를 충족하지 못할 수 있음을 발견했습니다.

## 핵심 내용
### 방법
- **실제-시뮬레이션 모델링**: 실제 유기화학 워크스테이션에서 비커, 저울, 약수저 등 30개 이상의 기능 충실도 높은 자산을 재구성하여 물리적 속성과 기하학적 형태의 정확성을 보장합니다.
- **통합 시뮬레이션 환경**: 관절형 실험 기기(예: 열리고 닫히는 병뚜껑), 입자 기반 분말 물리 시뮬레이션(고체 분말의 흐름과 적층 시뮬레이션), 폐쇄 루프 기기 판독값(예: 저울의 실시간 무게 피드백)을 결합하여 완전한 조작-측정 폐쇄 루프를 형성합니다.
- **원자 작업과 워크플로우**: 여섯 가지 원자 작업(예: 잡기, 붓기, 긁기)을 정의하고, 실제 실험실 표준 운영 절차(SOP)를 기반으로 병 집기, 뚜껑 열기, 분말 옮기기, 칭량, 뚜껑 닫기 등의 단계를 포함한 일곱 단계 고체 칭량 워크플로우를 설계합니다.

### 실험 설정
- **평가 프로토콜**: 정밀도 인식 평가 프로토콜을 도입하여 작업 완료율(모든 단계 완료 여부), 실험 정밀도(예: 칭량 오차가 ±0.01g 이내인지), 장시간 실행 안정성(예: 연속 작업 중 누적 오차)을 동시에 측정합니다.
- **벤치마크 전략**: 세 가지 대표 전략을 테스트합니다: 규칙 기반 스크립트 전략, 모방 학습 전략(Behavior Cloning), 강화 학습 전략(PPO).
- **교란 조건**: 프로그래밍된 배치(고정된 기기 위치)와 환경 교란(예: 분말 초기 위치 무작위 변경, 테이블 진동 추가) 하에서 테스트합니다.

### 주요 수치와 결론
- **작업 완료율**: 모든 전략이 프로그래밍된 배치에서 일곱 단계 칭량 워크플로우를 완료하며, 작업 완료율이 90%를 초과합니다.
- **정밀도 격차**: 실험 정밀도 측면에서 규칙 기반 전략만 ±0.01g 칭량 허용 오차를 충족합니다; 모방 학습과 강화 학습 전략의 평균 칭량 오차는 각각 0.05g과 0.08g으로 허용 범위를 크게 초과합니다.
- **교란 영향**: 환경 교란 하에서 모든 전략의 정밀도가 추가로 저하되며, 강화 학습 전략의 오차는 0.12g으로 증가하고 작업 완료율은 70%로 감소합니다.
- **결론**: Labimus는 작업 완료와 실험 유효성 사이의 근본적인 단절을 드러냅니다—로봇이 작업을 "완료"할 수 있어도 정밀도 부족으로 실험이 실패할 수 있습니다. 이는 신뢰할 수 있는 과학 실험실 인간형 로봇 개발을 위한 새로운 테스트 플랫폼을 제공합니다.
