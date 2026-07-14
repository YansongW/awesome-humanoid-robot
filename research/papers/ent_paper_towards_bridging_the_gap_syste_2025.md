---
$id: ent_paper_towards_bridging_the_gap_syste_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots'
  zh: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots'
  ko: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots'
summary:
  en: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots is a 2025 work on sim-to-real for
    humanoid robots.'
  zh: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots is a 2025 work on sim-to-real for
    humanoid robots.'
  ko: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots is a 2025 work on sim-to-real for
    humanoid robots.'
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
- sim_to_real
- towards_bridging_the_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.06342v1.
sources:
- id: src_001
  type: paper
  title: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots (arXiv)'
  url: https://arxiv.org/abs/2509.06342
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Legged robots must achieve both robust locomotion and energy efficiency to be practical in real-world environments. Yet controllers trained in simulation often fail to transfer reliably, and most existing approaches neglect actuator-specific energy losses or depend on complex, hand-tuned reward formulations. We propose a framework that integrates sim-to-real reinforcement learning with a physics-grounded energy model for permanent magnet synchronous motors. The framework requires a minimal parameter set to capture the simulation-to-reality gap and employs a compact four-term reward with a first-principle-based energetic loss formulation that balances electrical and mechanical dissipation. We evaluate and validate the approach through a bottom-up dynamic parameter identification study, spanning actuators, full-robot in-air trajectories and on-ground locomotion. The framework is tested on three primary platforms and deployed on ten additional robots, demonstrating reliable policy transfer without randomization of dynamic parameters. Our method improves energetic efficiency over state-of-the-art methods, achieving a 32 percent reduction in the full Cost of Transport of ANYmal (value 1.27). All code, models, and datasets will be released.

## 核心内容
Legged robots must achieve both robust locomotion and energy efficiency to be practical in real-world environments. Yet controllers trained in simulation often fail to transfer reliably, and most existing approaches neglect actuator-specific energy losses or depend on complex, hand-tuned reward formulations. We propose a framework that integrates sim-to-real reinforcement learning with a physics-grounded energy model for permanent magnet synchronous motors. The framework requires a minimal parameter set to capture the simulation-to-reality gap and employs a compact four-term reward with a first-principle-based energetic loss formulation that balances electrical and mechanical dissipation. We evaluate and validate the approach through a bottom-up dynamic parameter identification study, spanning actuators, full-robot in-air trajectories and on-ground locomotion. The framework is tested on three primary platforms and deployed on ten additional robots, demonstrating reliable policy transfer without randomization of dynamic parameters. Our method improves energetic efficiency over state-of-the-art methods, achieving a 32 percent reduction in the full Cost of Transport of ANYmal (value 1.27). All code, models, and datasets will be released.

## 参考
- http://arxiv.org/abs/2509.06342v1

