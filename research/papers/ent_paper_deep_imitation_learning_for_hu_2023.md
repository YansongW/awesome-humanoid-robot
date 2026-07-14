---
$id: ent_paper_deep_imitation_learning_for_hu_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation
  zh: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation
  ko: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation
summary:
  en: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation is a 2023 work on teleoperation for
    humanoid robots, with open-source code available.
  zh: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation is a 2023 work on teleoperation for
    humanoid robots, with open-source code available.
  ko: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation is a 2023 work on teleoperation for
    humanoid robots, with open-source code available.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deep_imitation_learning_for_hu
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.01952v2.
sources:
- id: src_001
  type: paper
  title: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation (arXiv)
  url: https://arxiv.org/abs/2309.01952
  date: '2023'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation project page
  url: https://ut-austin-rpl.github.io/TRILL/
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We tackle the problem of developing humanoid loco-manipulation skills with deep imitation learning. The difficulty of collecting task demonstrations and training policies for humanoids with a high degree of freedom presents substantial challenges. We introduce TRILL, a data-efficient framework for training humanoid loco-manipulation policies from human demonstrations. In this framework, we collect human demonstration data through an intuitive Virtual Reality (VR) interface. We employ the whole-body control formulation to transform task-space commands by human operators into the robot's joint-torque actuation while stabilizing its dynamics. By employing high-level action abstractions tailored for humanoid loco-manipulation, our method can efficiently learn complex sensorimotor skills. We demonstrate the effectiveness of TRILL in simulation and on a real-world robot for performing various loco-manipulation tasks. Videos and additional materials can be found on the project page: https://ut-austin-rpl.github.io/TRILL.

## 核心内容
We tackle the problem of developing humanoid loco-manipulation skills with deep imitation learning. The difficulty of collecting task demonstrations and training policies for humanoids with a high degree of freedom presents substantial challenges. We introduce TRILL, a data-efficient framework for training humanoid loco-manipulation policies from human demonstrations. In this framework, we collect human demonstration data through an intuitive Virtual Reality (VR) interface. We employ the whole-body control formulation to transform task-space commands by human operators into the robot's joint-torque actuation while stabilizing its dynamics. By employing high-level action abstractions tailored for humanoid loco-manipulation, our method can efficiently learn complex sensorimotor skills. We demonstrate the effectiveness of TRILL in simulation and on a real-world robot for performing various loco-manipulation tasks. Videos and additional materials can be found on the project page: https://ut-austin-rpl.github.io/TRILL.

## 参考
- http://arxiv.org/abs/2309.01952v2

