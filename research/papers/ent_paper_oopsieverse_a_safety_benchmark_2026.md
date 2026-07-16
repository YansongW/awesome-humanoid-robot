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
  zh: 'arXiv:2606.31993v1 Announce Type: new Abstract: While robotic manipulation capabilities have advanced rapidly, physical
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31993v1.
sources:
- id: src_001
  type: paper
  title: 'OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation'
  url: https://arxiv.org/abs/2606.31993
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and taskagnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

## 核心内容
While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and taskagnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

## 参考
- http://arxiv.org/abs/2606.31993v1

## Overview
While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and task-agnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

## Content
While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and task-agnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

## 개요
로봇 조작 능력이 빠르게 발전했지만, 물리적 안전은 가정용 로봇 배포의 주요 장벽으로 남아 있습니다. 로봇이 자신이나 주변 환경을 손상시키면 작업 성공만으로는 충분하지 않기 때문입니다. 시뮬레이션은 비용이 많이 들고 위험한 실제 환경 훈련 및 평가에 대한 무해한 대안을 제공하지만, 기존 시뮬레이터는 손상을 감지, 정량화 및 표현하는 일반적인 메커니즘이 부족합니다. 이러한 격차를 해결하기 위해, 우리는 손상 인식 가정용 조작을 위한 통합 시뮬레이션 프레임워크이자 벤치마크인 OOPSIEVERSE를 소개합니다. OOPSIEVERSE는 접촉력, 온도 변화, 액체 상호작용과 같은 소스를 해당 기계적, 열적 또는 유체 손상으로 변환하여 손상을 명시적이고 물리적으로 기반하며 작업에 구애받지 않는 신호로 제공합니다. OOPSIEVERSE는 두 가지 핵심 요소로 구성됩니다: (1) 탐색 및 조작 중 손상을 감지하고 정량화하는 시뮬레이터에 구애받지 않는 프레임워크인 DAMAGESIM, (2) 일반적인 손상 모드를 평가하고 작업 완료와 안전한 실행을 구분하도록 설계된 일련의 가정용 작업입니다. 우리는 서로 다른 물리 백엔드를 가진 두 시뮬레이터, OmniGibson (Nvidia Omniverse) 및 RoboCasa (MuJoCo)에서 DAMAGESIM을 구현하여 프레임워크의 일반성을 입증합니다. 또한, (1) 실시간 손상 피드백을 통한 더 안전한 시연 수집 안내, (2) 손상 조건부 모방 학습 및 강화 학습을 통한 더 안전한 조작 정책 학습, (3) 최첨단 Vision Language Action 정책의 안전성 벤치마킹, (4) sim-to-real 전이 정책의 실제 환경 안전성 향상 등 여러 사용 사례에서 OOPSIEVERSE의 유용성을 보여줍니다. 함께, 우리의 결과는 안전한 로봇 조작에 대한 체계적이고 확장 가능한 연구를 위한 오픈소스 기반으로서 OOPSIEVERSE의 잠재력을 강조합니다. 코드 및 자세한 정보는 https://robin-lab.cs.utexas.edu/oopsieverse/ 를 참조하십시오.

## 핵심 내용
로봇 조작 능력이 빠르게 발전했지만, 물리적 안전은 가정용 로봇 배포의 주요 장벽으로 남아 있습니다. 로봇이 자신이나 주변 환경을 손상시키면 작업 성공만으로는 충분하지 않기 때문입니다. 시뮬레이션은 비용이 많이 들고 위험한 실제 환경 훈련 및 평가에 대한 무해한 대안을 제공하지만, 기존 시뮬레이터는 손상을 감지, 정량화 및 표현하는 일반적인 메커니즘이 부족합니다. 이러한 격차를 해결하기 위해, 우리는 손상 인식 가정용 조작을 위한 통합 시뮬레이션 프레임워크이자 벤치마크인 OOPSIEVERSE를 소개합니다. OOPSIEVERSE는 접촉력, 온도 변화, 액체 상호작용과 같은 소스를 해당 기계적, 열적 또는 유체 손상으로 변환하여 손상을 명시적이고 물리적으로 기반하며 작업에 구애받지 않는 신호로 제공합니다. OOPSIEVERSE는 두 가지 핵심 요소로 구성됩니다: (1) 탐색 및 조작 중 손상을 감지하고 정량화하는 시뮬레이터에 구애받지 않는 프레임워크인 DAMAGESIM, (2) 일반적인 손상 모드를 평가하고 작업 완료와 안전한 실행을 구분하도록 설계된 일련의 가정용 작업입니다. 우리는 서로 다른 물리 백엔드를 가진 두 시뮬레이터, OmniGibson (Nvidia Omniverse) 및 RoboCasa (MuJoCo)에서 DAMAGESIM을 구현하여 프레임워크의 일반성을 입증합니다. 또한, (1) 실시간 손상 피드백을 통한 더 안전한 시연 수집 안내, (2) 손상 조건부 모방 학습 및 강화 학습을 통한 더 안전한 조작 정책 학습, (3) 최첨단 Vision Language Action 정책의 안전성 벤치마킹, (4) sim-to-real 전이 정책의 실제 환경 안전성 향상 등 여러 사용 사례에서 OOPSIEVERSE의 유용성을 보여줍니다. 함께, 우리의 결과는 안전한 로봇 조작에 대한 체계적이고 확장 가능한 연구를 위한 오픈소스 기반으로서 OOPSIEVERSE의 잠재력을 강조합니다. 코드 및 자세한 정보는 https://robin-lab.cs.utexas.edu/oopsieverse/ 를 참조하십시오.
