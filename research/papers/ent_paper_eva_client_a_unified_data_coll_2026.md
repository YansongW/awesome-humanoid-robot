---
$id: ent_paper_eva_client_a_unified_data_coll_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots'
  zh: 'EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots'
  ko: 'EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots'
summary:
  en: 'arXiv:2607.02646v1 Announce Type: new Abstract: We present EVA-Client, an open-source framework for deployment, data
    collection, and evaluation of trained manipulation policies on real robots. Sitting between a policy server and the physical
    hardware, EVA-Client unifies the real-robot stages of the policy iteration loop within a single codebase. It makes three
    contributions. First, a component-decoupled architecture in which robot backends, inference strategies, and transport
    middlewares form an orthogonal grid: adding a robot or a strategy touches only its own layer. Second, inspectable execution
    through Debug, Collect, and Eval workflows, with modes ranging from open-loop simulation to continuous real-time control.
    Third, every evaluation run doubles as a data collection, recording full rollouts in training-ready format alongside exhaustive
    logs and a side-by-side comparison viewer, so each evaluation feeds the next round of training rather than ending as an
    unrecorded impression. EVA-Client further consolidates major real-time inference strategies, synchronous and asynchronous
    execution, ACT-style temporal ensembling, Real-Time Chunking, and a naive-async ablation baseline, behind a single configuration
    surface.'
  zh: 'arXiv:2607.02646v1 Announce Type: new Abstract: We present EVA-Client, an open-source framework for deployment, data
    collection, and evaluation of trained manipulation policies on real robots. Sitting between a policy server and the physical
    hardware, EVA-Client unifies the real-robot stages of the policy iteration loop within a single codebase. It makes three
    contributions. First, a component-decoupled architecture in which robot backends, inference strategies, and transport
    middlewares form an orthogonal grid: adding a robot or a strategy touches only its own layer. Second, inspectable execution
    through Debug, Collect, and Eval workflows, with modes ranging from open-loop simulation to continuous real-time control.
    Third, every evaluation run doubles as a data collection, recording full rollouts in training-ready format alongside exhaustive
    logs and a side-by-side comparison viewer, so each evaluation feeds the next round of training rather than ending as an
    unrecorded impression. EVA-Client further consolidates major real-time inference strategies, synchronous and asynchronous
    execution, ACT-style temporal ensembling, Real-Time Chunking, and a naive-async ablation baseline, behind a single configuration
    surface.'
  ko: 'arXiv:2607.02646v1 Announce Type: new Abstract: We present EVA-Client, an open-source framework for deployment, data
    collection, and evaluation of trained manipulation policies on real robots. Sitting between a policy server and the physical
    hardware, EVA-Client unifies the real-robot stages of the policy iteration loop within a single codebase. It makes three
    contributions. First, a component-decoupled architecture in which robot backends, inference strategies, and transport
    middlewares form an orthogonal grid: adding a robot or a strategy touches only its own layer. Second, inspectable execution
    through Debug, Collect, and Eval workflows, with modes ranging from open-loop simulation to continuous real-time control.
    Third, every evaluation run doubles as a data collection, recording full rollouts in training-ready format alongside exhaustive
    logs and a side-by-side comparison viewer, so each evaluation feeds the next round of training rather than ending as an
    unrecorded impression. EVA-Client further consolidates major real-time inference strategies, synchronous and asynchronous
    execution, ACT-style temporal ensembling, Real-Time Chunking, and a naive-async ablation baseline, behind a single configuration
    surface.'
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
- eva_client
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02646v1.
sources:
- id: src_001
  type: paper
  title: 'EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots
    (arXiv)'
  url: https://arxiv.org/abs/2607.02646
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
We present EVA-Client, an open-source framework for deployment, data collection, and evaluation of trained manipulation policies on real robots. Sitting between a policy server and the physical hardware, EVA-Client unifies the real-robot stages of the policy iteration loop within a single codebase. It makes three contributions. First, a component-decoupled architecture in which robot backends, inference strategies, and transport middlewares form an orthogonal grid: adding a robot or a strategy touches only its own layer. Second, inspectable execution through Debug, Collect, and Eval workflows, with modes ranging from open-loop simulation to continuous real-time control. Third, every evaluation run doubles as a data collection, recording full rollouts in training-ready format alongside exhaustive logs and a side-by-side comparison viewer, so each evaluation feeds the next round of training rather than ending as an unrecorded impression. EVA-Client further consolidates major real-time inference strategies, synchronous and asynchronous execution, ACT-style temporal ensembling, Real-Time Chunking, and a naive-async ablation baseline, behind a single configuration surface.

## 核心内容
We present EVA-Client, an open-source framework for deployment, data collection, and evaluation of trained manipulation policies on real robots. Sitting between a policy server and the physical hardware, EVA-Client unifies the real-robot stages of the policy iteration loop within a single codebase. It makes three contributions. First, a component-decoupled architecture in which robot backends, inference strategies, and transport middlewares form an orthogonal grid: adding a robot or a strategy touches only its own layer. Second, inspectable execution through Debug, Collect, and Eval workflows, with modes ranging from open-loop simulation to continuous real-time control. Third, every evaluation run doubles as a data collection, recording full rollouts in training-ready format alongside exhaustive logs and a side-by-side comparison viewer, so each evaluation feeds the next round of training rather than ending as an unrecorded impression. EVA-Client further consolidates major real-time inference strategies, synchronous and asynchronous execution, ACT-style temporal ensembling, Real-Time Chunking, and a naive-async ablation baseline, behind a single configuration surface.

## 参考
- http://arxiv.org/abs/2607.02646v1

