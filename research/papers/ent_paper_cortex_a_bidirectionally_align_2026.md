---
$id: ent_paper_cortex_a_bidirectionally_align_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation'
  zh: 'Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation'
  ko: 'Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation'
summary:
  en: "arXiv:2607.05377v1 Announce Type: new \nAbstract: While recent Vision-Language-Action (VLA) models show promise toward\
    \ generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely\
    \ on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning\
    \ semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework\
    \ with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level\
    \ VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles,\
    \ such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This\
    \ enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data.\
    \ We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better\
    \ handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts\
    \ to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy,\
    \ e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist\
    \ VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments,\
    \ by simply combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone."
  zh: "arXiv:2607.05377v1 Announce Type: new \nAbstract: While recent Vision-Language-Action (VLA) models show promise toward\
    \ generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely\
    \ on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning\
    \ semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework\
    \ with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level\
    \ VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles,\
    \ such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This\
    \ enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data.\
    \ We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better\
    \ handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts\
    \ to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy,\
    \ e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist\
    \ VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments,\
    \ by simply combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone."
  ko: "arXiv:2607.05377v1 Announce Type: new \nAbstract: While recent Vision-Language-Action (VLA) models show promise toward\
    \ generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely\
    \ on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning\
    \ semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework\
    \ with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level\
    \ VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles,\
    \ such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This\
    \ enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data.\
    \ We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better\
    \ handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts\
    \ to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy,\
    \ e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist\
    \ VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments,\
    \ by simply combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone."
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
- cortex
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.05377v1.
sources:
- id: src_001
  type: paper
  title: 'Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.05377
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone.

## 核心内容
While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone.

## 参考
- http://arxiv.org/abs/2607.05377v1

