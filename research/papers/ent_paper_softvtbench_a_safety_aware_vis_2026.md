---
$id: ent_paper_softvtbench_a_safety_aware_vis_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable Objects'
  zh: 'SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable Objects'
  ko: 'SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable Objects'
summary:
  en: 'arXiv:2607.04234v1 Announce Type: new Abstract: Deformable object manipulation poses challenges beyond task completion:
    successful execution must also maintain safe physical interaction, holding the object stably without slip or drop while
    avoiding excessive deformation. However, existing manipulation benchmarks are predominantly success-oriented and rarely
    evaluate whether a policy remains physically safe throughout execution. We present SoftVTBench, a safety-aware visuo-tactile
    benchmark for physically constrained deformable object manipulation. Built in Isaac Sim with finite-element-simulated
    deformable objects, SoftVTBench provides multi-view RGB observations, RGB tactile sensing with marker motion, proprioception,
    and language instructions, and defines four matched task suites over object type (deformable vs. rigid) and variation
    axis (object vs. spatial). It separately reports Goal Success and Safety Success; the latter additionally requires no
    drop and peak deformation below a calibrated object-specific threshold, measured from policy-hidden privileged Finite
    Element Method (FEM) states. We implement pi0.5-based baselines under this protocol. Experiments show that success-only
    evaluation substantially overstates policy performance, as a large fraction of goal-completing rollouts still violate
    physical safety. Furthermore, incorporating tactile sensing improves Safety Success (e.g., from 21.4% to 35.6% on object-centric
    deformable tasks) and reduces object deformation during execution, while maintaining comparable Goal Success. SoftVTBench
    provides a reproducible benchmark for studying visuo-tactile deformable manipulation under physical interaction constraints.'
  zh: 'arXiv:2607.04234v1 Announce Type: new Abstract: Deformable object manipulation poses challenges beyond task completion:
    successful execution must also maintain safe physical interaction, holding the object stably without slip or drop while
    avoiding excessive deformation. However, existing manipulation benchmarks are predominantly success-oriented and rarely
    evaluate whether a policy remains physically safe throughout execution. We present SoftVTBench, a safety-aware visuo-tactile
    benchmark for physically constrained deformable object manipulation. Built in Isaac Sim with finite-element-simulated
    deformable objects, SoftVTBench provides multi-view RGB observations, RGB tactile sensing with marker motion, proprioception,
    and language instructions, and defines four matched task suites over object type (deformable vs. rigid) and variation
    axis (object vs. spatial). It separately reports Goal Success and Safety Success; the latter additionally requires no
    drop and peak deformation below a calibrated object-specific threshold, measured from policy-hidden privileged Finite
    Element Method (FEM) states. We implement pi0.5-based baselines under this protocol. Experiments show that success-only
    evaluation substantially overstates policy performance, as a large fraction of goal-completing rollouts still violate
    physical safety. Furthermore, incorporating tactile sensing improves Safety Success (e.g., from 21.4% to 35.6% on object-centric
    deformable tasks) and reduces object deformation during execution, while maintaining comparable Goal Success. SoftVTBench
    provides a reproducible benchmark for studying visuo-tactile deformable manipulation under physical interaction constraints.'
  ko: 'arXiv:2607.04234v1 Announce Type: new Abstract: Deformable object manipulation poses challenges beyond task completion:
    successful execution must also maintain safe physical interaction, holding the object stably without slip or drop while
    avoiding excessive deformation. However, existing manipulation benchmarks are predominantly success-oriented and rarely
    evaluate whether a policy remains physically safe throughout execution. We present SoftVTBench, a safety-aware visuo-tactile
    benchmark for physically constrained deformable object manipulation. Built in Isaac Sim with finite-element-simulated
    deformable objects, SoftVTBench provides multi-view RGB observations, RGB tactile sensing with marker motion, proprioception,
    and language instructions, and defines four matched task suites over object type (deformable vs. rigid) and variation
    axis (object vs. spatial). It separately reports Goal Success and Safety Success; the latter additionally requires no
    drop and peak deformation below a calibrated object-specific threshold, measured from policy-hidden privileged Finite
    Element Method (FEM) states. We implement pi0.5-based baselines under this protocol. Experiments show that success-only
    evaluation substantially overstates policy performance, as a large fraction of goal-completing rollouts still violate
    physical safety. Furthermore, incorporating tactile sensing improves Safety Success (e.g., from 21.4% to 35.6% on object-centric
    deformable tasks) and reduces object deformation during execution, while maintaining comparable Goal Success. SoftVTBench
    provides a reproducible benchmark for studying visuo-tactile deformable manipulation under physical interaction constraints.'
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
- softvtbench
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04234v1.
sources:
- id: src_001
  type: paper
  title: 'SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable
    Objects (arXiv)'
  url: https://arxiv.org/abs/2607.04234
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Deformable object manipulation poses challenges beyond task completion: successful execution must also maintain safe physical interaction, holding the object stably without slip or drop while avoiding excessive deformation. However, existing manipulation benchmarks are predominantly success-oriented and rarely evaluate whether a policy remains physically safe throughout execution. We present SoftVTBench, a safety-aware visuo-tactile benchmark for physically constrained deformable object manipulation. Built in Isaac Sim with finite-element-simulated deformable objects, SoftVTBench provides multi-view RGB observations, RGB tactile sensing with marker motion, proprioception, and language instructions, and defines four matched task suites over object type (deformable vs. rigid) and variation axis (object vs. spatial). It separately reports Goal Success and Safety Success; the latter additionally requires no drop and peak deformation below a calibrated object-specific threshold, measured from policy-hidden privileged Finite Element Method (FEM) states. We implement pi0.5-based baselines under this protocol. Experiments show that success-only evaluation substantially overstates policy performance, as a large fraction of goal-completing rollouts still violate physical safety. Furthermore, incorporating tactile sensing improves Safety Success (e.g., from 21.4% to 35.6% on object-centric deformable tasks) and reduces object deformation during execution, while maintaining comparable Goal Success. SoftVTBench provides a reproducible benchmark for studying visuo-tactile deformable manipulation under physical interaction constraints.

## 核心内容
Deformable object manipulation poses challenges beyond task completion: successful execution must also maintain safe physical interaction, holding the object stably without slip or drop while avoiding excessive deformation. However, existing manipulation benchmarks are predominantly success-oriented and rarely evaluate whether a policy remains physically safe throughout execution. We present SoftVTBench, a safety-aware visuo-tactile benchmark for physically constrained deformable object manipulation. Built in Isaac Sim with finite-element-simulated deformable objects, SoftVTBench provides multi-view RGB observations, RGB tactile sensing with marker motion, proprioception, and language instructions, and defines four matched task suites over object type (deformable vs. rigid) and variation axis (object vs. spatial). It separately reports Goal Success and Safety Success; the latter additionally requires no drop and peak deformation below a calibrated object-specific threshold, measured from policy-hidden privileged Finite Element Method (FEM) states. We implement pi0.5-based baselines under this protocol. Experiments show that success-only evaluation substantially overstates policy performance, as a large fraction of goal-completing rollouts still violate physical safety. Furthermore, incorporating tactile sensing improves Safety Success (e.g., from 21.4% to 35.6% on object-centric deformable tasks) and reduces object deformation during execution, while maintaining comparable Goal Success. SoftVTBench provides a reproducible benchmark for studying visuo-tactile deformable manipulation under physical interaction constraints.

## 参考
- http://arxiv.org/abs/2607.04234v1

