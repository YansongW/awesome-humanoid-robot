---
$id: ent_paper_pyroki_a_modular_toolkit_for_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization'
  zh: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization'
  ko: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization'
summary:
  en: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- loco_manipulation
- pyroki
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03728v1.
sources:
- id: src_001
  type: paper
  title: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization (arXiv)'
  url: https://arxiv.org/abs/2505.03728
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization project page'
  url: https://pyroki-toolkit.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robot motion can have many goals. Depending on the task, we might optimize for pose error, speed, collision, or similarity to a human demonstration. Motivated by this, we present PyRoki: a modular, extensible, and cross-platform toolkit for solving kinematic optimization problems. PyRoki couples an interface for specifying kinematic variables and costs with an efficient nonlinear least squares optimizer. Unlike existing tools, it is also cross-platform: optimization runs natively on CPU, GPU, and TPU. In this paper, we present (i) the design and implementation of PyRoki, (ii) motion retargeting and planning case studies that highlight the advantages of PyRoki's modularity, and (iii) optimization benchmarking, where PyRoki can be 1.4-1.7x faster and converges to lower errors than cuRobo, an existing GPU-accelerated inverse kinematics library.

## 核心内容
Robot motion can have many goals. Depending on the task, we might optimize for pose error, speed, collision, or similarity to a human demonstration. Motivated by this, we present PyRoki: a modular, extensible, and cross-platform toolkit for solving kinematic optimization problems. PyRoki couples an interface for specifying kinematic variables and costs with an efficient nonlinear least squares optimizer. Unlike existing tools, it is also cross-platform: optimization runs natively on CPU, GPU, and TPU. In this paper, we present (i) the design and implementation of PyRoki, (ii) motion retargeting and planning case studies that highlight the advantages of PyRoki's modularity, and (iii) optimization benchmarking, where PyRoki can be 1.4-1.7x faster and converges to lower errors than cuRobo, an existing GPU-accelerated inverse kinematics library.

## 参考
- http://arxiv.org/abs/2505.03728v1

