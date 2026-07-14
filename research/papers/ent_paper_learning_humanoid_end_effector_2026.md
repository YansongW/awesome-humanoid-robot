---
$id: ent_paper_learning_humanoid_end_effector_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation
  zh: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation
  ko: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation
summary:
  en: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
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
- learning_humanoid_end_effector
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.16705v3.
sources:
- id: src_001
  type: paper
  title: Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation (arXiv)
  url: https://arxiv.org/abs/2602.16705
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Visual loco-manipulation of arbitrary in-the-wild objects requires accurate end-effector (EE) control and a generalizable understanding of the scene from visual inputs (eg, RGB-D images). Existing imitation and sim2real methods jointly learn both these aspects via monolithic end-to-end learning and are thus hard to scale. In this work, we bring to bear the best tools for each of these problems -- large vision models for generalizable scene understanding and simulated training for accurate EE control -- leading to an overall modular loco-manipulation system that exhibits strong generalization. Our core technical innovation is HERO, an accurate residual-aware EE tracking policy made possible by combining classical robotics with machine learning. It uses a) inverse kinematics to convert residual end-effector targets into reference trajectories, b) a learned neural forward model for accurate forward kinematics, and c) goal adjustment and replanning. Together, these innovations reduce the end-effector tracking error to 2.44cm, outperforming the strongest prior method by 5.5x. Our overall system operates in diverse real-world environments, from offices to coffee shops, where the robot reliably grasps various everyday objects (eg, mugs, apples, toys) on surfaces ranging from 43cm to 92cm in height. Systematic modular and end-to-end tests demonstrate the effectiveness of our proposed design. We believe our advances open up new ways of training humanoids to interact with daily objects.

## 核心内容
Visual loco-manipulation of arbitrary in-the-wild objects requires accurate end-effector (EE) control and a generalizable understanding of the scene from visual inputs (eg, RGB-D images). Existing imitation and sim2real methods jointly learn both these aspects via monolithic end-to-end learning and are thus hard to scale. In this work, we bring to bear the best tools for each of these problems -- large vision models for generalizable scene understanding and simulated training for accurate EE control -- leading to an overall modular loco-manipulation system that exhibits strong generalization. Our core technical innovation is HERO, an accurate residual-aware EE tracking policy made possible by combining classical robotics with machine learning. It uses a) inverse kinematics to convert residual end-effector targets into reference trajectories, b) a learned neural forward model for accurate forward kinematics, and c) goal adjustment and replanning. Together, these innovations reduce the end-effector tracking error to 2.44cm, outperforming the strongest prior method by 5.5x. Our overall system operates in diverse real-world environments, from offices to coffee shops, where the robot reliably grasps various everyday objects (eg, mugs, apples, toys) on surfaces ranging from 43cm to 92cm in height. Systematic modular and end-to-end tests demonstrate the effectiveness of our proposed design. We believe our advances open up new ways of training humanoids to interact with daily objects.

## 参考
- http://arxiv.org/abs/2602.16705v3

