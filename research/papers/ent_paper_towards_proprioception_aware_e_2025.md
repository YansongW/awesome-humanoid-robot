---
$id: ent_paper_towards_proprioception_aware_e_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots
  zh: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots
  ko: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots
summary:
  en: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots is a 2025 work on manipulation for humanoid
    robots.
  zh: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots is a 2025 work on manipulation for humanoid
    robots.
  ko: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots is a 2025 work on manipulation for humanoid
    robots.
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
- manipulation
- towards_proprioception_aware_e
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07882v2.
sources:
- id: src_001
  type: paper
  title: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2510.07882
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In recent years, Multimodal Large Language Models (MLLMs) have demonstrated the ability to serve as high-level planners, enabling robots to follow complex human instructions. However, their effectiveness, especially in long-horizon tasks involving dual-arm humanoid robots, remains limited. This limitation arises from two main challenges: (i) the absence of simulation platforms that systematically support task evaluation and data collection for humanoid robots, and (ii) the insufficient embodiment awareness of current MLLMs, which hinders reasoning about dual-arm selection logic and body positions during planning. To address these issues, we present DualTHOR, a new dual-arm humanoid simulator, with continuous transition and a contingency mechanism. Building on this platform, we propose Proprio-MLLM, a model that enhances embodiment awareness by incorporating proprioceptive information with motion-based position embedding and a cross-spatial encoder. Experiments show that, while existing MLLMs struggle in this environment, Proprio-MLLM achieves an average improvement of 19.75% in planning performance. Our work provides both an essential simulation platform and an effective model to advance embodied intelligence in humanoid robotics. The code is available at https://anonymous.4open.science/r/DualTHOR-5F3B.

## 核心内容
In recent years, Multimodal Large Language Models (MLLMs) have demonstrated the ability to serve as high-level planners, enabling robots to follow complex human instructions. However, their effectiveness, especially in long-horizon tasks involving dual-arm humanoid robots, remains limited. This limitation arises from two main challenges: (i) the absence of simulation platforms that systematically support task evaluation and data collection for humanoid robots, and (ii) the insufficient embodiment awareness of current MLLMs, which hinders reasoning about dual-arm selection logic and body positions during planning. To address these issues, we present DualTHOR, a new dual-arm humanoid simulator, with continuous transition and a contingency mechanism. Building on this platform, we propose Proprio-MLLM, a model that enhances embodiment awareness by incorporating proprioceptive information with motion-based position embedding and a cross-spatial encoder. Experiments show that, while existing MLLMs struggle in this environment, Proprio-MLLM achieves an average improvement of 19.75% in planning performance. Our work provides both an essential simulation platform and an effective model to advance embodied intelligence in humanoid robotics. The code is available at https://anonymous.4open.science/r/DualTHOR-5F3B.

## 参考
- http://arxiv.org/abs/2510.07882v2

