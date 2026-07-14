---
$id: ent_paper_armor_egocentric_perception_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning'
  zh: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning'
  ko: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning'
summary:
  en: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning is a 2024 work on navigation
    for humanoid robots.'
  zh: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning is a 2024 work on navigation
    for humanoid robots.'
  ko: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning is a 2024 work on navigation
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
- armor
- humanoid
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.00396v1.
sources:
- id: src_001
  type: paper
  title: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning (arXiv)'
  url: https://arxiv.org/abs/2412.00396
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have significant gaps in their sensing and perception, making it hard to perform motion planning in dense environments. To address this, we introduce ARMOR, a novel egocentric perception system that integrates both hardware and software, specifically incorporating wearable-like depth sensors for humanoid robots. Our distributed perception approach enhances the robot's spatial awareness, and facilitates more agile motion planning. We also train a transformer-based imitation learning (IL) policy in simulation to perform dynamic collision avoidance, by leveraging around 86 hours worth of human realistic motions from the AMASS dataset. We show that our ARMOR perception is superior against a setup with multiple dense head-mounted, and externally mounted depth cameras, with a 63.7% reduction in collisions, and 78.7% improvement on success rate. We also compare our IL policy against a sampling-based motion planning expert cuRobo, showing 31.6% less collisions, 16.9% higher success rate, and 26x reduction in computational latency. Lastly, we deploy our ARMOR perception on our real-world GR1 humanoid from Fourier Intelligence. We are going to update the link to the source code, HW description, and 3D CAD files in the arXiv version of this text.

## 核心内容
Humanoid robots have significant gaps in their sensing and perception, making it hard to perform motion planning in dense environments. To address this, we introduce ARMOR, a novel egocentric perception system that integrates both hardware and software, specifically incorporating wearable-like depth sensors for humanoid robots. Our distributed perception approach enhances the robot's spatial awareness, and facilitates more agile motion planning. We also train a transformer-based imitation learning (IL) policy in simulation to perform dynamic collision avoidance, by leveraging around 86 hours worth of human realistic motions from the AMASS dataset. We show that our ARMOR perception is superior against a setup with multiple dense head-mounted, and externally mounted depth cameras, with a 63.7% reduction in collisions, and 78.7% improvement on success rate. We also compare our IL policy against a sampling-based motion planning expert cuRobo, showing 31.6% less collisions, 16.9% higher success rate, and 26x reduction in computational latency. Lastly, we deploy our ARMOR perception on our real-world GR1 humanoid from Fourier Intelligence. We are going to update the link to the source code, HW description, and 3D CAD files in the arXiv version of this text.

## 参考
- http://arxiv.org/abs/2412.00396v1

