---
$id: ent_paper_embodiedcpp_a_portable_inferen_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots'
  zh: 'Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots'
  ko: 'Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots'
summary:
  en: 'arXiv:2607.02501v2 Announce Type: replace Abstract: Embodied AI models now span vision-language-action (VLA) models
    and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend
    assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed
    mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate
    execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied
    interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based
    on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and
    organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters.
    The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support,
    enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate
    Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer
    block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively.
    The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment
    efficiency while preserving high accuracy across diverse embodied model architectures.'
  zh: 'arXiv:2607.02501v2 Announce Type: replace Abstract: Embodied AI models now span vision-language-action (VLA) models
    and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend
    assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed
    mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate
    execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied
    interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based
    on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and
    organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters.
    The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support,
    enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate
    Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer
    block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively.
    The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment
    efficiency while preserving high accuracy across diverse embodied model architectures.'
  ko: 'arXiv:2607.02501v2 Announce Type: replace Abstract: Embodied AI models now span vision-language-action (VLA) models
    and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend
    assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed
    mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate
    execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied
    interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based
    on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and
    organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters.
    The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support,
    enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate
    Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer
    block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively.
    The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment
    efficiency while preserving high accuracy across diverse embodied model architectures.'
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
- embodiedcpp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02501v2.
sources:
- id: src_001
  type: paper
  title: 'Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots (arXiv)'
  url: https://arxiv.org/abs/2607.02501
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively. The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment efficiency while preserving high accuracy across diverse embodied model architectures.

## 核心内容
Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied$.$cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied$.$cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied$.$cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively. The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied$.$cpp improves deployment efficiency while preserving high accuracy across diverse embodied model architectures.

## 参考
- http://arxiv.org/abs/2607.02501v2

