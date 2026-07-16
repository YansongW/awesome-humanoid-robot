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

