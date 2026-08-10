---
$id: ent_paper_robodojo_a_unified_sim_and_rea_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies'
  zh: 'RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies'
  ko: 'RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies'
summary:
  en: 'arXiv:2607.04434v1 Announce Type: new Abstract: Generalist robot manipulation policies have advanced rapidly, yet existing
    benchmarks remain limited in systematically evaluating their capabilities. Many rely on simple, short-horizon, or skill-narrow
    tasks with limited capability coverage, and are often conducted only in simulation or only in the real world. Simulation
    enables scalable feedback but misses physical deployment challenges, while real-world evaluation is costly, time-consuming,
    and difficult to reproduce. We introduce RoboDojo, a unified sim-and-real benchmark for comprehensive evaluation of generalist
    robot manipulation policies. RoboDojo includes 42 simulation tasks and 18 real-world tasks covering diverse and complementary
    manipulation capabilities. The simulation benchmark evaluates five dimensions: generalization, memory, precision, long-horizon
    execution, and open-vocabulary instruction following, while the real-world benchmark exposes policies to challenging physical-world
    deployment conditions. RoboDojo supports scalable evaluation through heterogeneous parallel simulation in Isaac Sim and
    provides RoboDojo-RealEval, a reproducible real-world evaluation system with remote cloud access, standardized hardware,
    scene reset, evaluation protocol, and deployment interface. Together with XPolicyLab, policies can be integrated once
    and evaluated across simulation and real-world settings with minimal adaptation. We integrate 30 policies into XPolicyLab
    and evaluate them on RoboDojo, establishing a public leaderboard and systematic analysis of current policy performance.
    The website is available at http://robodojo-benchmark.com/.'
  zh: RoboDojo 是一个统一的仿真与真实世界基准，用于全面评估通用机器人操作策略。由研究团队提出，包含 42 个仿真任务和 18 个真实世界任务，覆盖泛化、记忆、精度、长时程执行和开放词汇指令跟随五个维度。其核心贡献在于提供可扩展的异构并行仿真（基于
    Isaac Sim）和可复现的真实世界评估系统 RoboDojo-RealEval，并集成 30 种策略建立公开排行榜。
  ko: 'arXiv:2607.04434v1 Announce Type: new Abstract: Generalist robot manipulation policies have advanced rapidly, yet existing
    benchmarks remain limited in systematically evaluating their capabilities. Many rely on simple, short-horizon, or skill-narrow
    tasks with limited capability coverage, and are often conducted only in simulation or only in the real world. Simulation
    enables scalable feedback but misses physical deployment challenges, while real-world evaluation is costly, time-consuming,
    and difficult to reproduce. We introduce RoboDojo, a unified sim-and-real benchmark for comprehensive evaluation of generalist
    robot manipulation policies. RoboDojo includes 42 simulation tasks and 18 real-world tasks covering diverse and complementary
    manipulation capabilities. The simulation benchmark evaluates five dimensions: generalization, memory, precision, long-horizon
    execution, and open-vocabulary instruction following, while the real-world benchmark exposes policies to challenging physical-world
    deployment conditions. RoboDojo supports scalable evaluation through heterogeneous parallel simulation in Isaac Sim and
    provides RoboDojo-RealEval, a reproducible real-world evaluation system with remote cloud access, standardized hardware,
    scene reset, evaluation protocol, and deployment interface. Together with XPolicyLab, policies can be integrated once
    and evaluated across simulation and real-world settings with minimal adaptation. We integrate 30 policies into XPolicyLab
    and evaluate them on RoboDojo, establishing a public leaderboard and systematic analysis of current policy performance.
    The website is available at http://robodojo-benchmark.com/.'
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
- robodojo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04434v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1019 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies
    (arXiv)'
  url: https://arxiv.org/abs/2607.04434
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有通用机器人操作策略基准存在局限，多依赖简单、短时程或技能狭窄的任务，且常仅在仿真或真实世界中进行单一评估。仿真虽可扩展但忽略物理部署挑战，真实世界评估则成本高、耗时长且难以复现。RoboDojo 通过统一仿真与真实世界基准解决此问题，其仿真部分评估五维能力，真实世界部分暴露策略于挑战性物理条件。该基准支持通过 Isaac Sim 进行异构并行仿真，并提供 RoboDojo-RealEval 系统，包含远程云访问、标准化硬件、场景重置、评估协议和部署接口，结合 XPolicyLab 实现策略一次集成、跨环境评估。

## 核心内容
### 方法
RoboDojo 设计为统一仿真与真实世界的评估框架，旨在系统性地衡量通用机器人操作策略的全面能力。其仿真基准覆盖 42 个任务，真实世界基准包含 18 个任务，任务设计互补且多样化。

### 架构
- **仿真基准**：基于 Isaac Sim 实现异构并行仿真，支持可扩展评估。评估五个维度：
  - **泛化**：策略对未见物体、场景或配置的适应能力。
  - **记忆**：策略在任务中利用历史信息的能力。
  - **精度**：操作任务的精细控制要求。
  - **长时程执行**：多步骤任务的连贯完成能力。
  - **开放词汇指令跟随**：理解并执行自然语言指令的能力。
- **真实世界基准**：RoboDojo-RealEval 系统提供可复现评估，包括：
  - 远程云访问，降低硬件门槛。
  - 标准化硬件配置，确保一致性。
  - 自动场景重置，减少人工干预。
  - 标准化评估协议，保证结果可比性。
  - 部署接口，简化策略集成。

### 实验设置
- 集成 30 种策略至 XPolicyLab 平台，实现一次集成即可在仿真和真实世界环境中评估，仅需最小适配。
- 建立公开排行榜，对当前策略性能进行系统分析。

### 关键数字
- **仿真任务**：42 个
- **真实世界任务**：18 个
- **集成策略**：30 种
- **评估维度**：5 个（仿真基准）

### 结论
RoboDojo 通过统一仿真与真实世界评估，弥补了现有基准在能力覆盖和可复现性上的不足。其可扩展仿真和标准化真实世界系统，为通用机器人操作策略的全面比较提供了可靠平台。更多信息见 http://robodojo-benchmark.com/。

## Overview
Generalist robot manipulation policies have advanced rapidly, yet existing benchmarks remain limited in systematically evaluating their capabilities. Many rely on simple, short-horizon, or skill-narrow tasks with limited capability coverage, and are often conducted only in simulation or only in the real world. Simulation enables scalable feedback but misses physical deployment challenges, while real-world evaluation is costly, time-consuming, and difficult to reproduce. We introduce RoboDojo, a unified sim-and-real benchmark for comprehensive evaluation of generalist robot manipulation policies. RoboDojo includes 42 simulation tasks and 18 real-world tasks covering diverse and complementary manipulation capabilities. The simulation benchmark evaluates five dimensions: generalization, memory, precision, long-horizon execution, and open-vocabulary instruction following, while the real-world benchmark exposes policies to challenging physical-world deployment conditions. RoboDojo supports scalable evaluation through heterogeneous parallel simulation in Isaac Sim and provides RoboDojo-RealEval, a reproducible real-world evaluation system with remote cloud access, standardized hardware, scene reset, evaluation protocol, and deployment interface. Together with XPolicyLab, policies can be integrated once and evaluated across simulation and real-world settings with minimal adaptation. We integrate 30 policies into XPolicyLab and evaluate them on RoboDojo, establishing a public leaderboard and systematic analysis of current policy performance. The website is available at http://robodojo-benchmark.com/.

## 参考
- http://arxiv.org/abs/2607.04434v3

## 개요
기존의 범용 로봇 조작 정책 벤치마크는 한계가 있으며, 대부분 단순하거나 단기간 또는 좁은 기술 범위의 작업에 의존하고, 종종 시뮬레이션이나 실제 세계 중 하나에서만 단일 평가를 수행합니다. 시뮬레이션은 확장 가능하지만 물리적 배포 문제를 무시하고, 실제 세계 평가는 비용이 높고 시간이 오래 걸리며 재현이 어렵습니다. RoboDojo는 시뮬레이션과 실제 세계 벤치마크를 통합하여 이 문제를 해결하며, 시뮬레이션 부분은 5가지 능력을 평가하고 실제 세계 부분은 정책을 도전적인 물리적 조건에 노출시킵니다. 이 벤치마크는 Isaac Sim을 통한 이기종 병렬 시뮬레이션을 지원하며, 원격 클라우드 액세스, 표준화된 하드웨어, 장면 재설정, 평가 프로토콜 및 배포 인터페이스를 포함한 RoboDojo-RealEval 시스템을 제공하고, XPolicyLab과 결합하여 정책을 한 번 통합하고 여러 환경에서 평가할 수 있습니다.

## 핵심 내용
### 방법
RoboDojo는 시뮬레이션과 실제 세계를 통합한 평가 프레임워크로 설계되었으며, 범용 로봇 조작 정책의 포괄적인 능력을 체계적으로 측정하는 것을 목표로 합니다. 시뮬레이션 벤치마크는 42개의 작업을 포함하고, 실제 세계 벤치마크는 18개의 작업을 포함하며, 작업 설계는 상호 보완적이고 다양합니다.

### 아키텍처
- **시뮬레이션 벤치마크**: Isaac Sim 기반의 이기종 병렬 시뮬레이션을 구현하여 확장 가능한 평가를 지원합니다. 5가지 차원을 평가합니다:
  - **일반화**: 보지 못한 객체, 장면 또는 구성에 대한 정책의 적응 능력.
  - **기억**: 작업 중 역사적 정보를 활용하는 정책의 능력.
  - **정밀도**: 조작 작업의 세밀한 제어 요구 사항.
  - **장기 실행**: 다단계 작업의 연속적 완료 능력.
  - **개방형 어휘 지시 따르기**: 자연어 지시를 이해하고 실행하는 능력.
- **실제 세계 벤치마크**: RoboDojo-RealEval 시스템은 재현 가능한 평가를 제공하며, 다음을 포함합니다:
  - 원격 클라우드 액세스로 하드웨어 장벽을 낮춥니다.
  - 표준화된 하드웨어 구성으로 일관성을 보장합니다.
  - 자동 장면 재설정으로 수동 개입을 줄입니다.
  - 표준화된 평가 프로토콜로 결과 비교 가능성을 보장합니다.
  - 배포 인터페이스로 정책 통합을 단순화합니다.

### 실험 설정
- 30개의 정책을 XPolicyLab 플랫폼에 통합하여 한 번의 통합으로 시뮬레이션 및 실제 세계 환경에서 최소한의 적응만으로 평가할 수 있습니다.
- 공개 리더보드를 구축하여 현재 정책 성능에 대한 체계적인 분석을 제공합니다.

### 주요 수치
- **시뮬레이션 작업**: 42개
- **실제 세계 작업**: 18개
- **통합 정책**: 30개
- **평가 차원**: 5개 (시뮬레이션 벤치마크)

### 결론
RoboDojo는 시뮬레이션과 실제 세계 평가를 통합하여 기존 벤치마크의 능력 범위와 재현성 부족을 보완합니다. 확장 가능한 시뮬레이션과 표준화된 실제 세계 시스템은 범용 로봇 조작 정책의 포괄적인 비교를 위한 신뢰할 수 있는 플랫폼을 제공합니다. 자세한 정보는 http://robodojo-benchmark.com/ 에서 확인할 수 있습니다.
