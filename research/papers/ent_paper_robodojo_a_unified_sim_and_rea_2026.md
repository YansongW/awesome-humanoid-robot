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
  zh: 'arXiv:2607.04434v1 Announce Type: new Abstract: Generalist robot manipulation policies have advanced rapidly, yet existing
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04434v3.
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
Generalist robot manipulation policies have advanced rapidly, yet existing benchmarks remain limited in systematically evaluating their capabilities. Many rely on simple, short-horizon, or skill-narrow tasks with limited capability coverage, and are often conducted only in simulation or only in the real world. Simulation enables scalable feedback but misses physical deployment challenges, while real-world evaluation is costly, time-consuming, and difficult to reproduce. We introduce RoboDojo, a unified sim-and-real benchmark for comprehensive evaluation of generalist robot manipulation policies. RoboDojo includes 42 simulation tasks and 18 real-world tasks covering diverse and complementary manipulation capabilities. The simulation benchmark evaluates five dimensions: generalization, memory, precision, long-horizon execution, and open-vocabulary instruction following, while the real-world benchmark exposes policies to challenging physical-world deployment conditions. RoboDojo supports scalable evaluation through heterogeneous parallel simulation in Isaac Sim and provides RoboDojo-RealEval, a reproducible real-world evaluation system with remote cloud access, standardized hardware, scene reset, evaluation protocol, and deployment interface. Together with XPolicyLab, policies can be integrated once and evaluated across simulation and real-world settings with minimal adaptation. We integrate 30 policies into XPolicyLab and evaluate them on RoboDojo, establishing a public leaderboard and systematic analysis of current policy performance. The website is available at http://robodojo-benchmark.com/.

## 核心内容
Generalist robot manipulation policies have advanced rapidly, yet existing benchmarks remain limited in systematically evaluating their capabilities. Many rely on simple, short-horizon, or skill-narrow tasks with limited capability coverage, and are often conducted only in simulation or only in the real world. Simulation enables scalable feedback but misses physical deployment challenges, while real-world evaluation is costly, time-consuming, and difficult to reproduce. We introduce RoboDojo, a unified sim-and-real benchmark for comprehensive evaluation of generalist robot manipulation policies. RoboDojo includes 42 simulation tasks and 18 real-world tasks covering diverse and complementary manipulation capabilities. The simulation benchmark evaluates five dimensions: generalization, memory, precision, long-horizon execution, and open-vocabulary instruction following, while the real-world benchmark exposes policies to challenging physical-world deployment conditions. RoboDojo supports scalable evaluation through heterogeneous parallel simulation in Isaac Sim and provides RoboDojo-RealEval, a reproducible real-world evaluation system with remote cloud access, standardized hardware, scene reset, evaluation protocol, and deployment interface. Together with XPolicyLab, policies can be integrated once and evaluated across simulation and real-world settings with minimal adaptation. We integrate 30 policies into XPolicyLab and evaluate them on RoboDojo, establishing a public leaderboard and systematic analysis of current policy performance. The website is available at http://robodojo-benchmark.com/.

## 参考
- http://arxiv.org/abs/2607.04434v3

## Overview
Generalist robot manipulation policies have advanced rapidly, yet existing benchmarks remain limited in systematically evaluating their capabilities. Many rely on simple, short-horizon, or skill-narrow tasks with limited capability coverage, and are often conducted only in simulation or only in the real world. Simulation enables scalable feedback but misses physical deployment challenges, while real-world evaluation is costly, time-consuming, and difficult to reproduce. We introduce RoboDojo, a unified sim-and-real benchmark for comprehensive evaluation of generalist robot manipulation policies. RoboDojo includes 42 simulation tasks and 18 real-world tasks covering diverse and complementary manipulation capabilities. The simulation benchmark evaluates five dimensions: generalization, memory, precision, long-horizon execution, and open-vocabulary instruction following, while the real-world benchmark exposes policies to challenging physical-world deployment conditions. RoboDojo supports scalable evaluation through heterogeneous parallel simulation in Isaac Sim and provides RoboDojo-RealEval, a reproducible real-world evaluation system with remote cloud access, standardized hardware, scene reset, evaluation protocol, and deployment interface. Together with XPolicyLab, policies can be integrated once and evaluated across simulation and real-world settings with minimal adaptation. We integrate 30 policies into XPolicyLab and evaluate them on RoboDojo, establishing a public leaderboard and systematic analysis of current policy performance. The website is available at http://robodojo-benchmark.com/.

## Content
Generalist robot manipulation policies have advanced rapidly, yet existing benchmarks remain limited in systematically evaluating their capabilities. Many rely on simple, short-horizon, or skill-narrow tasks with limited capability coverage, and are often conducted only in simulation or only in the real world. Simulation enables scalable feedback but misses physical deployment challenges, while real-world evaluation is costly, time-consuming, and difficult to reproduce. We introduce RoboDojo, a unified sim-and-real benchmark for comprehensive evaluation of generalist robot manipulation policies. RoboDojo includes 42 simulation tasks and 18 real-world tasks covering diverse and complementary manipulation capabilities. The simulation benchmark evaluates five dimensions: generalization, memory, precision, long-horizon execution, and open-vocabulary instruction following, while the real-world benchmark exposes policies to challenging physical-world deployment conditions. RoboDojo supports scalable evaluation through heterogeneous parallel simulation in Isaac Sim and provides RoboDojo-RealEval, a reproducible real-world evaluation system with remote cloud access, standardized hardware, scene reset, evaluation protocol, and deployment interface. Together with XPolicyLab, policies can be integrated once and evaluated across simulation and real-world settings with minimal adaptation. We integrate 30 policies into XPolicyLab and evaluate them on RoboDojo, establishing a public leaderboard and systematic analysis of current policy performance. The website is available at http://robodojo-benchmark.com/.

## 개요
범용 로봇 조작 정책(Generalist robot manipulation policies)은 빠르게 발전해 왔지만, 기존 벤치마크는 이러한 능력을 체계적으로 평가하는 데 여전히 한계가 있습니다. 많은 벤치마크가 단순하거나, 단기적이거나, 기술 범위가 좁은 작업에 의존하여 능력 범위가 제한적이며, 종종 시뮬레이션 또는 실제 환경 중 하나에서만 수행됩니다. 시뮬레이션은 확장 가능한 피드백을 제공하지만 물리적 배포 과제를 놓치는 반면, 실제 환경 평가는 비용이 많이 들고 시간이 오래 걸리며 재현이 어렵습니다. 우리는 범용 로봇 조작 정책의 포괄적 평가를 위한 통합 시뮬레이션-실제 벤치마크인 RoboDojo를 소개합니다. RoboDojo는 다양하고 상호 보완적인 조작 능력을 포괄하는 42개의 시뮬레이션 작업과 18개의 실제 작업을 포함합니다. 시뮬레이션 벤치마크는 일반화, 기억, 정밀도, 장기 실행, 개방형 어휘 명령 수행의 다섯 가지 차원을 평가하며, 실제 벤치마크는 정책을 까다로운 물리적 세계 배포 조건에 노출시킵니다. RoboDojo는 Isaac Sim에서 이기종 병렬 시뮬레이션을 통해 확장 가능한 평가를 지원하며, 원격 클라우드 접속, 표준화된 하드웨어, 장면 재설정, 평가 프로토콜 및 배포 인터페이스를 갖춘 재현 가능한 실제 평가 시스템인 RoboDojo-RealEval을 제공합니다. XPolicyLab과 함께, 정책은 한 번 통합되어 최소한의 적응으로 시뮬레이션 및 실제 환경에서 평가될 수 있습니다. 우리는 30개의 정책을 XPolicyLab에 통합하고 RoboDojo에서 평가하여 공개 리더보드와 현재 정책 성능에 대한 체계적 분석을 구축했습니다. 웹사이트는 http://robodojo-benchmark.com/에서 확인할 수 있습니다.

## 핵심 내용
범용 로봇 조작 정책(Generalist robot manipulation policies)은 빠르게 발전해 왔지만, 기존 벤치마크는 이러한 능력을 체계적으로 평가하는 데 여전히 한계가 있습니다. 많은 벤치마크가 단순하거나, 단기적이거나, 기술 범위가 좁은 작업에 의존하여 능력 범위가 제한적이며, 종종 시뮬레이션 또는 실제 환경 중 하나에서만 수행됩니다. 시뮬레이션은 확장 가능한 피드백을 제공하지만 물리적 배포 과제를 놓치는 반면, 실제 환경 평가는 비용이 많이 들고 시간이 오래 걸리며 재현이 어렵습니다. 우리는 범용 로봇 조작 정책의 포괄적 평가를 위한 통합 시뮬레이션-실제 벤치마크인 RoboDojo를 소개합니다. RoboDojo는 다양하고 상호 보완적인 조작 능력을 포괄하는 42개의 시뮬레이션 작업과 18개의 실제 작업을 포함합니다. 시뮬레이션 벤치마크는 일반화, 기억, 정밀도, 장기 실행, 개방형 어휘 명령 수행의 다섯 가지 차원을 평가하며, 실제 벤치마크는 정책을 까다로운 물리적 세계 배포 조건에 노출시킵니다. RoboDojo는 Isaac Sim에서 이기종 병렬 시뮬레이션을 통해 확장 가능한 평가를 지원하며, 원격 클라우드 접속, 표준화된 하드웨어, 장면 재설정, 평가 프로토콜 및 배포 인터페이스를 갖춘 재현 가능한 실제 평가 시스템인 RoboDojo-RealEval을 제공합니다. XPolicyLab과 함께, 정책은 한 번 통합되어 최소한의 적응으로 시뮬레이션 및 실제 환경에서 평가될 수 있습니다. 우리는 30개의 정책을 XPolicyLab에 통합하고 RoboDojo에서 평가하여 공개 리더보드와 현재 정책 성능에 대한 체계적 분석을 구축했습니다. 웹사이트는 http://robodojo-benchmark.com/에서 확인할 수 있습니다.
