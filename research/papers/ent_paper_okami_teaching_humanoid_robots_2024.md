---
$id: ent_paper_okami_teaching_humanoid_robots_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation'
  zh: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation'
  ko: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation'
summary:
  en: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation is a 2024 work on manipulation for
    humanoid robots.'
  zh: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation is a 2024 work on manipulation for
    humanoid robots.'
  ko: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation is a 2024 work on manipulation for
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
- manipulation
- okami
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.11792v1.
sources:
- id: src_001
  type: paper
  title: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation (arXiv)'
  url: https://arxiv.org/abs/2410.11792
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation project page'
  url: https://ut-austin-rpl.github.io/OKAMI/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
We study the problem of teaching humanoid robots manipulation skills by imitating from single video demonstrations. We introduce OKAMI, a method that generates a manipulation plan from a single RGB-D video and derives a policy for execution. At the heart of our approach is object-aware retargeting, which enables the humanoid robot to mimic the human motions in an RGB-D video while adjusting to different object locations during deployment. OKAMI uses open-world vision models to identify task-relevant objects and retarget the body motions and hand poses separately. Our experiments show that OKAMI achieves strong generalizations across varying visual and spatial conditions, outperforming the state-of-the-art baseline on open-world imitation from observation. Furthermore, OKAMI rollout trajectories are leveraged to train closed-loop visuomotor policies, which achieve an average success rate of 79.2% without the need for labor-intensive teleoperation. More videos can be found on our website https://ut-austin-rpl.github.io/OKAMI/.

## 核心内容
We study the problem of teaching humanoid robots manipulation skills by imitating from single video demonstrations. We introduce OKAMI, a method that generates a manipulation plan from a single RGB-D video and derives a policy for execution. At the heart of our approach is object-aware retargeting, which enables the humanoid robot to mimic the human motions in an RGB-D video while adjusting to different object locations during deployment. OKAMI uses open-world vision models to identify task-relevant objects and retarget the body motions and hand poses separately. Our experiments show that OKAMI achieves strong generalizations across varying visual and spatial conditions, outperforming the state-of-the-art baseline on open-world imitation from observation. Furthermore, OKAMI rollout trajectories are leveraged to train closed-loop visuomotor policies, which achieve an average success rate of 79.2% without the need for labor-intensive teleoperation. More videos can be found on our website https://ut-austin-rpl.github.io/OKAMI/.

## 参考
- http://arxiv.org/abs/2410.11792v1

