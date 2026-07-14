---
$id: ent_paper_robostream_weaving_spatio_temp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language
    Models for Robotics'
  zh: 'RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language
    Models for Robotics'
  ko: ''
summary:
  en: "arXiv:2603.12939v2 Announce Type: replace \nAbstract: Enabling reliable long-horizon\
    \ robotic manipulation is a crucial step toward open-world embodied intelligence.\
    \ However, VLM-based planners treat each step as an isolated observation-to-action\
    \ mapping, forcing them to reinfer scene geometry from raw pixels at every decision\
    \ point while remaining unaware of how prior actions have reshaped the environment.\
    \ Despite strong short-horizon performance, these systems lack the spatio-temporal\
    \ reasoning required for persistent geometric anchoring and memory of action-triggered\
    \ state transitions. Without persistent state tracking, perceptual errors accumulate\
    \ across the execution horizon, temporarily occluded objects are catastrophically\
    \ forgotten, and these compounding failures lead to precondition violations that\
    \ cascade through subsequent steps. In contrast, humans maintain a persistent\
    \ mental model that continuously tracks spatial relations and action consequences\
    \ across interactions rather than reconstructing them at each instant. Inspired\
    \ by this human capacity for causal spatio-temporal reasoning with persistent\
    \ memory, we propose RoboStream, a training-free framework that achieves geometric\
    \ anchoring through Spatio-Temporal Fusion Tokens (STF-Tokens), which bind visual\
    \ evidence to 3D geometric attributes for persistent object grounding, and maintains\
    \ causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered\
    \ state transitions across steps. This design enables the planner to trace causal\
    \ chains and preserve object permanence under occlusion without additional training\
    \ or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4%\
    \ on challenging real-world block-building tasks, where both SoFar and VoxPoser\
    \ score 11.1%, demonstrating that spatio-temporal reasoning and causal memory\
    \ are critical missing components for reliable long-horizon manipulation."
  zh: "arXiv:2603.12939v2 Announce Type: replace \nAbstract: Enabling reliable long-horizon\
    \ robotic manipulation is a crucial step toward open-world embodied intelligence.\
    \ However, VLM-based planners treat each step as an isolated observation-to-action\
    \ mapping, forcing them to reinfer scene geometry from raw pixels at every decision\
    \ point while remaining unaware of how prior actions have reshaped the environment.\
    \ Despite strong short-horizon performance, these systems lack the spatio-temporal\
    \ reasoning required for persistent geometric anchoring and memory of action-triggered\
    \ state transitions. Without persistent state tracking, perceptual errors accumulate\
    \ across the execution horizon, temporarily occluded objects are catastrophically\
    \ forgotten, and these compounding failures lead to precondition violations that\
    \ cascade through subsequent steps. In contrast, humans maintain a persistent\
    \ mental model that continuously tracks spatial relations and action consequences\
    \ across interactions rather than reconstructing them at each instant. Inspired\
    \ by this human capacity for causal spatio-temporal reasoning with persistent\
    \ memory, we propose RoboStream, a training-free framework that achieves geometric\
    \ anchoring through Spatio-Temporal Fusion Tokens (STF-Tokens), which bind visual\
    \ evidence to 3D geometric attributes for persistent object grounding, and maintains\
    \ causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered\
    \ state transitions across steps. This design enables the planner to trace causal\
    \ chains and preserve object permanence under occlusion without additional training\
    \ or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4%\
    \ on challenging real-world block-building tasks, where both SoFar and VoxPoser\
    \ score 11.1%, demonstrating that spatio-temporal reasoning and causal memory\
    \ are critical missing components for reliable long-horizon manipulation."
  ko: ''
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
- robostream
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language
    Models for Robotics (arXiv)'
  url: https://arxiv.org/abs/2603.12939
  date: '2026'
  accessed_at: '2026-07-14'
---

arXiv:2603.12939v2 Announce Type: replace 
Abstract: Enabling reliable long-horizon robotic manipulation is a crucial step toward open-world embodied intelligence. However, VLM-based planners treat each step as an isolated observation-to-action mapping, forcing them to reinfer scene geometry from raw pixels at every decision point while remaining unaware of how prior actions have reshaped the environment. Despite strong short-horizon performance, these systems lack the spatio-temporal reasoning required for persistent geometric anchoring and memory of action-triggered state transitions. Without persistent state tracking, perceptual errors accumulate across the execution horizon, temporarily occluded objects are catastrophically forgotten, and these compounding failures lead to precondition violations that cascade through subsequent steps. In contrast, humans maintain a persistent mental model that continuously tracks spatial relations and action consequences across interactions rather than reconstructing them at each instant. Inspired by this human capacity for causal spatio-temporal reasoning with persistent memory, we propose RoboStream, a training-free framework that achieves geometric anchoring through Spatio-Temporal Fusion Tokens (STF-Tokens), which bind visual evidence to 3D geometric attributes for persistent object grounding, and maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions across steps. This design enables the planner to trace causal chains and preserve object permanence under occlusion without additional training or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world block-building tasks, where both SoFar and VoxPoser score 11.1%, demonstrating that spatio-temporal reasoning and causal memory are critical missing components for reliable long-horizon manipulation.
