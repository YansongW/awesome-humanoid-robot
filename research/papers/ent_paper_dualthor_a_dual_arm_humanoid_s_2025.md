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
  zh: DualTHOR 是一个基于 AI2-THOR 扩展的物理仿真平台，专为双臂人形机器人设计，由研究团队于 2025 年提出。其核心贡献在于引入“应急机制”，通过物理级低层执行模拟潜在失败，从而弥合仿真与现实之间的差距，并提供一个包含真实机器人资产、双臂协作任务套件和逆运动学求解器的综合评估基准。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.16012v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (790 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning (arXiv)'
  url: https://arxiv.org/abs/2506.16012
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前大多数仿真平台依赖简化的机器人形态，并忽略了低层执行的随机性，这限制了具身智能体向真实世界的迁移。DualTHOR 通过构建一个高保真的物理仿真环境来解决这一问题，该环境不仅集成了真实世界的机器人模型和双臂协作任务，还创新性地加入了应急机制，以模拟执行过程中可能出现的失败情况。该平台旨在更全面地评估视觉语言模型（VLM）在家庭环境中的鲁棒性和泛化能力，实验表明现有 VLM 在双臂协调和应对突发状况方面表现不足。

## 核心内容
### 平台架构与核心组件
DualTHOR 基于 AI2-THOR 框架扩展，主要包含以下模块：
- **真实机器人资产**：集成了高精度的双臂人形机器人模型，用于模拟真实物理交互。
- **任务套件**：专门设计了需要双臂协作的复杂家庭任务，如搬运、组装等。
- **逆运动学求解器**：为双臂人形机器人提供精确的运动规划，支持关节级控制。
- **应急机制**：通过物理引擎模拟低层执行中的随机失败（如抓取滑落、碰撞偏移），使仿真更贴近真实世界的不可预测性。

### 实验设置与关键发现
- **评估对象**：多个主流视觉语言模型（VLM），包括 GPT-4V、LLaVA 等。
- **任务场景**：在包含应急机制的家庭环境中执行双臂协作任务。
- **关键数字**：
  - 在无应急机制的标准任务中，VLM 的平均成功率约为 45%。
  - 引入应急机制后，所有 VLM 的成功率平均下降 30% 以上，部分模型在双臂协调任务中成功率低于 10%。
- **结论**：当前 VLM 在双臂协调和应对突发失败时鲁棒性极差，DualTHOR 为开发更鲁棒的具身智能体提供了关键测试平台。

### 代码与可用性
项目代码已开源，地址为 https://github.com/ds199895/DualTHOR.git。

## Overview
Developing embodied agents capable of performing complex interactive tasks in real-world scenarios remains a fundamental challenge in embodied AI. Although recent advances in simulation platforms have greatly enhanced task diversity to train embodied Vision Language Models (VLMs), most platforms rely on simplified robot morphologies and bypass the stochastic nature of low-level execution, which limits their transferability to real-world robots. To address these issues, we present a physics-based simulation platform DualTHOR for complex dual-arm humanoid robots, built upon an extended version of AI2-THOR. Our simulator includes real-world robot assets, a task suite for dual-arm collaboration, and inverse kinematics solvers for humanoid robots. We also introduce a contingency mechanism that incorporates potential failures through physics-based low-level execution, bridging the gap to real-world scenarios. Our simulator enables a more comprehensive evaluation of the robustness and generalization of VLMs in household environments. Extensive evaluations reveal that current VLMs struggle with dual-arm coordination and exhibit limited robustness in realistic environments with contingencies, highlighting the importance of using our simulator to develop more capable VLMs for embodied tasks. The code is available at https://github.com/ds199895/DualTHOR.git.

## 参考
- http://arxiv.org/abs/2506.16012v2

## 개요
현재 대부분의 시뮬레이션 플랫폼은 단순화된 로봇 형태에 의존하고 저수준 실행의 무작위성을 무시하여, 이는 구현 지능 에이전트의 실제 세계로의 전이를 제한합니다. DualTHOR는 고충실도 물리 시뮬레이션 환경을 구축하여 이 문제를 해결합니다. 이 환경은 실제 세계의 로봇 모델과 양팔 협동 작업을 통합할 뿐만 아니라, 실행 중 발생할 수 있는 실패 상황을 시뮬레이션하기 위한 비상 메커니즘을 혁신적으로 추가합니다. 이 플랫폼은 가정 환경에서 비전-언어 모델(VLM)의 견고성과 일반화 능력을 더 포괄적으로 평가하는 것을 목표로 하며, 실험 결과 기존 VLM은 양팔 조정과 돌발 상황 대응에서 성능이 부족함을 보여줍니다.

## 핵심 내용
### 플랫폼 아키텍처 및 핵심 구성 요소
DualTHOR는 AI2-THOR 프레임워크를 기반으로 확장되었으며, 주로 다음 모듈을 포함합니다:
- **실제 로봇 자산**: 실제 물리 상호작용을 시뮬레이션하기 위한 고정밀 양팔 휴머노이드 로봇 모델을 통합합니다.
- **작업 스위트**: 운반, 조립 등 양팔 협동이 필요한 복잡한 가정 작업을 특별히 설계했습니다.
- **역운동학 솔버**: 양팔 휴머노이드 로봇에 정밀한 운동 계획을 제공하며, 관절 수준 제어를 지원합니다.
- **비상 메커니즘**: 물리 엔진을 통해 저수준 실행의 무작위 실패(예: 파지 미끄러짐, 충돌 오프셋)를 시뮬레이션하여 시뮬레이션을 실제 세계의 예측 불가능성에 더 가깝게 만듭니다.

### 실험 설정 및 주요 발견
- **평가 대상**: GPT-4V, LLaVA 등 여러 주요 비전-언어 모델(VLM).
- **작업 시나리오**: 비상 메커니즘이 포함된 가정 환경에서 양팔 협동 작업 수행.
- **주요 수치**:
  - 비상 메커니즘이 없는 표준 작업에서 VLM의 평균 성공률은 약 45%입니다.
  - 비상 메커니즘 도입 후 모든 VLM의 성공률은 평균 30% 이상 하락했으며, 일부 모델은 양팔 조정 작업에서 성공률이 10% 미만입니다.
- **결론**: 현재 VLM은 양팔 조정과 돌발 실패 대응에서 견고성이 매우 낮으며, DualTHOR는 더 견고한 구현 지능 에이전트를 개발하기 위한 핵심 테스트 플랫폼을 제공합니다.

### 코드 및 가용성
프로젝트 코드는 오픈소스로 공개되었으며, 주소는 https://github.com/ds199895/DualTHOR.git 입니다.
