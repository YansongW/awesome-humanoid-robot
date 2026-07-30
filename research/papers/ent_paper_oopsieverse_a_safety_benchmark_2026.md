---
$id: ent_paper_oopsieverse_a_safety_benchmark_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation'
  zh: 'OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation'
  ko: 'OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation'
summary:
  en: 'arXiv:2606.31993v1 Announce Type: new Abstract: While robotic manipulation capabilities have advanced rapidly, physical
    safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself
    or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation,
    yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce
    OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides
    damage as an explicit, physically-grounded, and taskagnostic signal by converting sources such as contact forces, temperature
    changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core
    elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation,
    and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and
    safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different
    physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE
    across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning
    safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking
    the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred
    policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable
    research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/'
  zh: OOPSIEVERSE 是由 UT Austin 的 Robin Lab 提出的统一仿真框架与基准，旨在解决机器人操作中物理安全检测缺失的问题。其核心贡献在于将接触力、温度变化等物理量转化为机械、热或流体损伤信号，并提供了 DAMAGESIM
    这一与仿真器无关的损伤检测量化工具，以及一套区分任务完成与安全执行的家居任务套件。
  ko: 'arXiv:2606.31993v1 Announce Type: new Abstract: While robotic manipulation capabilities have advanced rapidly, physical
    safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself
    or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation,
    yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce
    OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides
    damage as an explicit, physically-grounded, and taskagnostic signal by converting sources such as contact forces, temperature
    changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core
    elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation,
    and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and
    safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different
    physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE
    across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning
    safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking
    the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred
    policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable
    research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/'
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
- oopsieverse
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31993v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation'
  url: https://arxiv.org/abs/2606.31993
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
OOPSIEVERSE 是一个面向损伤感知的家居操作仿真框架与基准，由 DAMAGESIM 损伤检测框架和一套家居任务组成。DAMAGESIM 能够将接触力、温度变化和液体交互等物理源转化为机械、热或流体损伤信号，从而提供显式、物理可解释且与任务无关的安全度量。该框架已在 OmniGibson（基于 Nvidia Omniverse）和 RoboCasa（基于 MuJoCo）两个不同物理引擎的仿真器中成功实例化，验证了其通用性。研究展示了 OOPSIEVERSE 在多个场景中的实用性，包括通过实时损伤反馈引导更安全的演示收集、基于损伤条件的模仿学习与强化学习训练安全策略、评估最新 Vision Language Action 策略的安全性，以及提升 sim-to-real 迁移策略的真实世界安全性。

## 核心内容
### 方法架构
OOPSIEVERSE 包含两个核心组件：
- **DAMAGESIM**：一个与仿真器无关的框架，在导航和操作过程中检测并量化损伤。它将接触力、温度变化、液体交互等物理源映射为机械损伤（如碰撞变形）、热损伤（如过热）和流体损伤（如液体泄漏）。
- **家居任务套件**：一组专门设计的任务，用于评估常见的损伤模式，并明确区分“任务完成”与“安全执行”两个指标。

### 实验设置
- **仿真器实例化**：DAMAGESIM 在两个不同物理后端的仿真器中实现——OmniGibson（基于 Nvidia Omniverse）和 RoboCasa（基于 MuJoCo），以证明其框架通用性。
- **使用场景**：
  1. **安全演示收集**：通过实时损伤反馈引导人类演示者，减少不安全行为。
  2. **安全策略学习**：采用损伤条件化的模仿学习与强化学习，训练出更安全的操作策略。
  3. **策略安全基准测试**：评估当前最先进的 Vision Language Action 策略的安全性。
  4. **Sim-to-Real 安全迁移**：提升从仿真迁移到真实世界的策略的安全性。

### 关键结论
- OOPSIEVERSE 能够将物理交互转化为可量化的损伤信号，为安全评估提供统一标准。
- 在 OmniGibson 和 RoboCasa 中的实例化验证了 DAMAGESIM 的跨仿真器通用性。
- 实验表明，基于损伤反馈的训练方法能显著降低操作过程中的物理损伤风险，同时保持任务完成率。
- 该框架为系统化、可扩展的安全机器人操作研究提供了开源基础。

## Overview
While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and taskagnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

## Overview
While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and task-agnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

## Content
While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and task-agnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

## 개요
로봇 조작 능력이 빠르게 발전했지만, 물리적 안전은 가정용 로봇 배포의 주요 장벽으로 남아 있습니다. 로봇이 자신이나 주변 환경을 손상시키면 작업 성공만으로는 충분하지 않기 때문입니다. 시뮬레이션은 비용이 많이 들고 위험한 실제 환경 훈련 및 평가에 대한 무해한 대안을 제공하지만, 기존 시뮬레이터는 손상을 감지, 정량화 및 표현하는 일반적인 메커니즘이 부족합니다. 이러한 격차를 해결하기 위해, 우리는 손상 인식 가정용 조작을 위한 통합 시뮬레이션 프레임워크이자 벤치마크인 OOPSIEVERSE를 소개합니다. OOPSIEVERSE는 접촉력, 온도 변화, 액체 상호작용과 같은 소스를 해당 기계적, 열적 또는 유체 손상으로 변환하여 손상을 명시적이고 물리적으로 기반하며 작업에 구애받지 않는 신호로 제공합니다. OOPSIEVERSE는 두 가지 핵심 요소로 구성됩니다: (1) 탐색 및 조작 중 손상을 감지하고 정량화하는 시뮬레이터에 구애받지 않는 프레임워크인 DAMAGESIM, (2) 일반적인 손상 모드를 평가하고 작업 완료와 안전한 실행을 구분하도록 설계된 일련의 가정용 작업입니다. 우리는 서로 다른 물리 백엔드를 가진 두 시뮬레이터, OmniGibson (Nvidia Omniverse) 및 RoboCasa (MuJoCo)에서 DAMAGESIM을 구현하여 프레임워크의 일반성을 입증합니다. 또한, (1) 실시간 손상 피드백을 통한 더 안전한 시연 수집 안내, (2) 손상 조건부 모방 학습 및 강화 학습을 통한 더 안전한 조작 정책 학습, (3) 최첨단 Vision Language Action 정책의 안전성 벤치마킹, (4) sim-to-real 전이 정책의 실제 환경 안전성 향상 등 여러 사용 사례에서 OOPSIEVERSE의 유용성을 보여줍니다. 함께, 우리의 결과는 안전한 로봇 조작에 대한 체계적이고 확장 가능한 연구를 위한 오픈소스 기반으로서 OOPSIEVERSE의 잠재력을 강조합니다. 코드 및 자세한 정보는 https://robin-lab.cs.utexas.edu/oopsieverse/ 를 참조하십시오.

## 핵심 내용
로봇 조작 능력이 빠르게 발전했지만, 물리적 안전은 가정용 로봇 배포의 주요 장벽으로 남아 있습니다. 로봇이 자신이나 주변 환경을 손상시키면 작업 성공만으로는 충분하지 않기 때문입니다. 시뮬레이션은 비용이 많이 들고 위험한 실제 환경 훈련 및 평가에 대한 무해한 대안을 제공하지만, 기존 시뮬레이터는 손상을 감지, 정량화 및 표현하는 일반적인 메커니즘이 부족합니다. 이러한 격차를 해결하기 위해, 우리는 손상 인식 가정용 조작을 위한 통합 시뮬레이션 프레임워크이자 벤치마크인 OOPSIEVERSE를 소개합니다. OOPSIEVERSE는 접촉력, 온도 변화, 액체 상호작용과 같은 소스를 해당 기계적, 열적 또는 유체 손상으로 변환하여 손상을 명시적이고 물리적으로 기반하며 작업에 구애받지 않는 신호로 제공합니다. OOPSIEVERSE는 두 가지 핵심 요소로 구성됩니다: (1) 탐색 및 조작 중 손상을 감지하고 정량화하는 시뮬레이터에 구애받지 않는 프레임워크인 DAMAGESIM, (2) 일반적인 손상 모드를 평가하고 작업 완료와 안전한 실행을 구분하도록 설계된 일련의 가정용 작업입니다. 우리는 서로 다른 물리 백엔드를 가진 두 시뮬레이터, OmniGibson (Nvidia Omniverse) 및 RoboCasa (MuJoCo)에서 DAMAGESIM을 구현하여 프레임워크의 일반성을 입증합니다. 또한, (1) 실시간 손상 피드백을 통한 더 안전한 시연 수집 안내, (2) 손상 조건부 모방 학습 및 강화 학습을 통한 더 안전한 조작 정책 학습, (3) 최첨단 Vision Language Action 정책의 안전성 벤치마킹, (4) sim-to-real 전이 정책의 실제 환경 안전성 향상 등 여러 사용 사례에서 OOPSIEVERSE의 유용성을 보여줍니다. 함께, 우리의 결과는 안전한 로봇 조작에 대한 체계적이고 확장 가능한 연구를 위한 오픈소스 기반으로서 OOPSIEVERSE의 잠재력을 강조합니다. 코드 및 자세한 정보는 https://robin-lab.cs.utexas.edu/oopsieverse/ 를 참조하십시오.

## 参考
- http://arxiv.org/abs/2606.31993v1
