---
$id: ent_paper_generalizable_humanoid_manipul_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies
  zh: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies
  ko: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies
summary:
  en: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies is a 2024 work on manipulation for humanoid
    robots, with open-source code available.
  zh: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies is a 2024 work on manipulation for humanoid
    robots, with open-source code available.
  ko: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies is a 2024 work on manipulation for humanoid
    robots, with open-source code available.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalizable_humanoid_manipul
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.10803v3.
sources:
- id: src_001
  type: paper
  title: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies (arXiv)
  url: https://arxiv.org/abs/2410.10803
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies project page
  url: https://humanoid-manipulation.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots capable of autonomous operation in diverse environments have long been a goal for roboticists. However, autonomous manipulation by humanoid robots has largely been restricted to one specific scene, primarily due to the difficulty of acquiring generalizable skills and the expensiveness of in-the-wild humanoid robot data. In this work, we build a real-world robotic system to address this challenging problem. Our system is mainly an integration of 1) a whole-upper-body robotic teleoperation system to acquire human-like robot data, 2) a 25-DoF humanoid robot platform with a height-adjustable cart and a 3D LiDAR sensor, and 3) an improved 3D Diffusion Policy learning algorithm for humanoid robots to learn from noisy human data. We run more than 2000 episodes of policy rollouts on the real robot for rigorous policy evaluation. Empowered by this system, we show that using only data collected in one single scene and with only onboard computing, a full-sized humanoid robot can autonomously perform skills in diverse real-world scenarios. Videos are available at https://humanoid-manipulation.github.io .

## 核心内容
Humanoid robots capable of autonomous operation in diverse environments have long been a goal for roboticists. However, autonomous manipulation by humanoid robots has largely been restricted to one specific scene, primarily due to the difficulty of acquiring generalizable skills and the expensiveness of in-the-wild humanoid robot data. In this work, we build a real-world robotic system to address this challenging problem. Our system is mainly an integration of 1) a whole-upper-body robotic teleoperation system to acquire human-like robot data, 2) a 25-DoF humanoid robot platform with a height-adjustable cart and a 3D LiDAR sensor, and 3) an improved 3D Diffusion Policy learning algorithm for humanoid robots to learn from noisy human data. We run more than 2000 episodes of policy rollouts on the real robot for rigorous policy evaluation. Empowered by this system, we show that using only data collected in one single scene and with only onboard computing, a full-sized humanoid robot can autonomously perform skills in diverse real-world scenarios. Videos are available at https://humanoid-manipulation.github.io .

## 参考
- http://arxiv.org/abs/2410.10803v3

