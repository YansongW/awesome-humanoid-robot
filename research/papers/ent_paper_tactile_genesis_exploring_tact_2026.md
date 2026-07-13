---
$id: ent_paper_tactile_genesis_exploring_tact_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous
    Tasks'
  zh: 'Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous
    Tasks'
  ko: ''
summary:
  en: "arXiv:2606.22332v2 Announce Type: replace \nAbstract: Tactile sensing is critical\
    \ for contact-rich dexterous manipulation, yet it remains unclear which tactile\
    \ abstractions a policy needs and when richer tactile fields justify their hardware\
    \ cost. This is hard to study empirically: each sensor effectively defines a new\
    \ robot, and no lab can replicate the same learning experiment across all of them.\
    \ We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform\
    \ that exposes binary contact, contact depth, per-taxel kinematic force/torque,\
    \ elastomer marker displacement, geometry-aware proximity, contact audio, and\
    \ a voxelized temperature field (the first of its kind in robot learning physics\
    \ simulation platforms) under a common interface, with configurable placement,\
    \ resolution, and a realistic noise model (drift, hysteresis, dead taxels, crosstalk).\
    \ It scales past 20,000 parallel environments and 1,000 taxels on a single GPU,\
    \ improving throughput by 3 to 20 times over previous tactile simulators. We train\
    \ teacher-student policies on three dexterous tasks, ablating sensor type, placement,\
    \ resolution, and noise, and verify transfer to the real XHand1. Proprioception\
    \ alone is insufficient on every task. Sensor placement dominates sensor type:\
    \ fingertip-only coverage trails whole-hand coverage by a wide margin, while adding\
    \ the palm and proximal phalanges closes most of the gap to the privileged teacher.\
    \ Resolution matters far less than coverage: placing 200 taxels across the whole\
    \ hand suffices across tasks. We find that force/torque per taxel is consistently\
    \ the most useful sensor type. These results give concrete guidance for both future\
    \ tactile hardware design for improving robot hands and policy-side observation\
    \ choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/"
  zh: "arXiv:2606.22332v2 Announce Type: replace \nAbstract: Tactile sensing is critical\
    \ for contact-rich dexterous manipulation, yet it remains unclear which tactile\
    \ abstractions a policy needs and when richer tactile fields justify their hardware\
    \ cost. This is hard to study empirically: each sensor effectively defines a new\
    \ robot, and no lab can replicate the same learning experiment across all of them.\
    \ We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform\
    \ that exposes binary contact, contact depth, per-taxel kinematic force/torque,\
    \ elastomer marker displacement, geometry-aware proximity, contact audio, and\
    \ a voxelized temperature field (the first of its kind in robot learning physics\
    \ simulation platforms) under a common interface, with configurable placement,\
    \ resolution, and a realistic noise model (drift, hysteresis, dead taxels, crosstalk).\
    \ It scales past 20,000 parallel environments and 1,000 taxels on a single GPU,\
    \ improving throughput by 3 to 20 times over previous tactile simulators. We train\
    \ teacher-student policies on three dexterous tasks, ablating sensor type, placement,\
    \ resolution, and noise, and verify transfer to the real XHand1. Proprioception\
    \ alone is insufficient on every task. Sensor placement dominates sensor type:\
    \ fingertip-only coverage trails whole-hand coverage by a wide margin, while adding\
    \ the palm and proximal phalanges closes most of the gap to the privileged teacher.\
    \ Resolution matters far less than coverage: placing 200 taxels across the whole\
    \ hand suffices across tasks. We find that force/torque per taxel is consistently\
    \ the most useful sensor type. These results give concrete guidance for both future\
    \ tactile hardware design for improving robot hands and policy-side observation\
    \ choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/"
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
- tactile_genesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-13'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous
    Tasks (arXiv)'
  url: https://arxiv.org/abs/2606.22332
  date: '2026'
  accessed_at: '2026-07-13'
---

arXiv:2606.22332v2 Announce Type: replace 
Abstract: Tactile sensing is critical for contact-rich dexterous manipulation, yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis, dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin, while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design for improving robot hands and policy-side observation choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/
