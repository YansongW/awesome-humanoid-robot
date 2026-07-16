---
$id: ent_paper_dualthor_a_dual_arm_humanoid_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning'
  zh: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning'
  ko: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning'
summary:
  en: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning is a 2025 work on simulation benchmark
    for humanoid robots.'
  zh: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning is a 2025 work on simulation benchmark
    for humanoid robots.'
  ko: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning is a 2025 work on simulation benchmark
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- dualthor
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.16012v2.
sources:
- id: src_001
  type: paper
  title: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning (arXiv)'
  url: https://arxiv.org/abs/2506.16012
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Developing embodied agents capable of performing complex interactive tasks in real-world scenarios remains a fundamental challenge in embodied AI. Although recent advances in simulation platforms have greatly enhanced task diversity to train embodied Vision Language Models (VLMs), most platforms rely on simplified robot morphologies and bypass the stochastic nature of low-level execution, which limits their transferability to real-world robots. To address these issues, we present a physics-based simulation platform DualTHOR for complex dual-arm humanoid robots, built upon an extended version of AI2-THOR. Our simulator includes real-world robot assets, a task suite for dual-arm collaboration, and inverse kinematics solvers for humanoid robots. We also introduce a contingency mechanism that incorporates potential failures through physics-based low-level execution, bridging the gap to real-world scenarios. Our simulator enables a more comprehensive evaluation of the robustness and generalization of VLMs in household environments. Extensive evaluations reveal that current VLMs struggle with dual-arm coordination and exhibit limited robustness in realistic environments with contingencies, highlighting the importance of using our simulator to develop more capable VLMs for embodied tasks. The code is available at https://github.com/ds199895/DualTHOR.git.

## 核心内容
Developing embodied agents capable of performing complex interactive tasks in real-world scenarios remains a fundamental challenge in embodied AI. Although recent advances in simulation platforms have greatly enhanced task diversity to train embodied Vision Language Models (VLMs), most platforms rely on simplified robot morphologies and bypass the stochastic nature of low-level execution, which limits their transferability to real-world robots. To address these issues, we present a physics-based simulation platform DualTHOR for complex dual-arm humanoid robots, built upon an extended version of AI2-THOR. Our simulator includes real-world robot assets, a task suite for dual-arm collaboration, and inverse kinematics solvers for humanoid robots. We also introduce a contingency mechanism that incorporates potential failures through physics-based low-level execution, bridging the gap to real-world scenarios. Our simulator enables a more comprehensive evaluation of the robustness and generalization of VLMs in household environments. Extensive evaluations reveal that current VLMs struggle with dual-arm coordination and exhibit limited robustness in realistic environments with contingencies, highlighting the importance of using our simulator to develop more capable VLMs for embodied tasks. The code is available at https://github.com/ds199895/DualTHOR.git.

## 参考
- http://arxiv.org/abs/2506.16012v2

## Overview
Developing embodied agents capable of performing complex interactive tasks in real-world scenarios remains a fundamental challenge in embodied AI. Although recent advances in simulation platforms have greatly enhanced task diversity to train embodied Vision Language Models (VLMs), most platforms rely on simplified robot morphologies and bypass the stochastic nature of low-level execution, which limits their transferability to real-world robots. To address these issues, we present a physics-based simulation platform DualTHOR for complex dual-arm humanoid robots, built upon an extended version of AI2-THOR. Our simulator includes real-world robot assets, a task suite for dual-arm collaboration, and inverse kinematics solvers for humanoid robots. We also introduce a contingency mechanism that incorporates potential failures through physics-based low-level execution, bridging the gap to real-world scenarios. Our simulator enables a more comprehensive evaluation of the robustness and generalization of VLMs in household environments. Extensive evaluations reveal that current VLMs struggle with dual-arm coordination and exhibit limited robustness in realistic environments with contingencies, highlighting the importance of using our simulator to develop more capable VLMs for embodied tasks. The code is available at https://github.com/ds199895/DualTHOR.git.

## Content
Developing embodied agents capable of performing complex interactive tasks in real-world scenarios remains a fundamental challenge in embodied AI. Although recent advances in simulation platforms have greatly enhanced task diversity to train embodied Vision Language Models (VLMs), most platforms rely on simplified robot morphologies and bypass the stochastic nature of low-level execution, which limits their transferability to real-world robots. To address these issues, we present a physics-based simulation platform DualTHOR for complex dual-arm humanoid robots, built upon an extended version of AI2-THOR. Our simulator includes real-world robot assets, a task suite for dual-arm collaboration, and inverse kinematics solvers for humanoid robots. We also introduce a contingency mechanism that incorporates potential failures through physics-based low-level execution, bridging the gap to real-world scenarios. Our simulator enables a more comprehensive evaluation of the robustness and generalization of VLMs in household environments. Extensive evaluations reveal that current VLMs struggle with dual-arm coordination and exhibit limited robustness in realistic environments with contingencies, highlighting the importance of using our simulator to develop more capable VLMs for embodied tasks. The code is available at https://github.com/ds199895/DualTHOR.git.

## 개요
현실 세계 시나리오에서 복잡한 상호작용 작업을 수행할 수 있는 체화된 에이전트를 개발하는 것은 체화된 AI의 근본적인 과제로 남아 있습니다. 최근 시뮬레이션 플랫폼의 발전으로 체화된 비전-언어 모델(VLM)을 훈련하기 위한 작업 다양성이 크게 향상되었지만, 대부분의 플랫폼은 단순화된 로봇 형태에 의존하고 저수준 실행의 확률적 특성을 무시하여 실제 로봇으로의 전이 가능성을 제한합니다. 이러한 문제를 해결하기 위해, 우리는 AI2-THOR의 확장 버전을 기반으로 구축된 복잡한 이중 팔 휴머노이드 로봇을 위한 물리 기반 시뮬레이션 플랫폼 DualTHOR를 제시합니다. 우리의 시뮬레이터는 실제 로봇 자산, 이중 팔 협업을 위한 작업 제품군, 휴머노이드 로봇을 위한 역운동학 솔버를 포함합니다. 또한 물리 기반 저수준 실행을 통해 잠재적 실패를 통합하는 우발 상황 메커니즘을 도입하여 현실 세계 시나리오와의 격차를 해소합니다. 우리의 시뮬레이터는 가정 환경에서 VLM의 견고성과 일반화에 대한 더 포괄적인 평가를 가능하게 합니다. 광범위한 평가 결과, 현재 VLM은 이중 팔 조정에 어려움을 겪고 우발 상황이 있는 현실적인 환경에서 제한된 견고성을 보여, 체화된 작업을 위한 더 유능한 VLM을 개발하기 위해 우리의 시뮬레이터를 사용하는 것의 중요성을 강조합니다. 코드는 https://github.com/ds199895/DualTHOR.git에서 확인할 수 있습니다.

## 핵심 내용
현실 세계 시나리오에서 복잡한 상호작용 작업을 수행할 수 있는 체화된 에이전트를 개발하는 것은 체화된 AI의 근본적인 과제로 남아 있습니다. 최근 시뮬레이션 플랫폼의 발전으로 체화된 비전-언어 모델(VLM)을 훈련하기 위한 작업 다양성이 크게 향상되었지만, 대부분의 플랫폼은 단순화된 로봇 형태에 의존하고 저수준 실행의 확률적 특성을 무시하여 실제 로봇으로의 전이 가능성을 제한합니다. 이러한 문제를 해결하기 위해, 우리는 AI2-THOR의 확장 버전을 기반으로 구축된 복잡한 이중 팔 휴머노이드 로봇을 위한 물리 기반 시뮬레이션 플랫폼 DualTHOR를 제시합니다. 우리의 시뮬레이터는 실제 로봇 자산, 이중 팔 협업을 위한 작업 제품군, 휴머노이드 로봇을 위한 역운동학 솔버를 포함합니다. 또한 물리 기반 저수준 실행을 통해 잠재적 실패를 통합하는 우발 상황 메커니즘을 도입하여 현실 세계 시나리오와의 격차를 해소합니다. 우리의 시뮬레이터는 가정 환경에서 VLM의 견고성과 일반화에 대한 더 포괄적인 평가를 가능하게 합니다. 광범위한 평가 결과, 현재 VLM은 이중 팔 조정에 어려움을 겪고 우발 상황이 있는 현실적인 환경에서 제한된 견고성을 보여, 체화된 작업을 위한 더 유능한 VLM을 개발하기 위해 우리의 시뮬레이터를 사용하는 것의 중요성을 강조합니다. 코드는 https://github.com/ds199895/DualTHOR.git에서 확인할 수 있습니다.
