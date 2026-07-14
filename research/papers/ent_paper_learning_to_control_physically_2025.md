---
$id: ent_paper_learning_to_control_physically_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
  zh: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
  ko: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
summary:
  en: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a 2025 work on physics-based
    character animation for humanoid robots.
  zh: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a 2025 work on physics-based
    character animation for humanoid robots.
  ko: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a 2025 work on physics-based
    character animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- learning_to_control_physically
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08500v1.
sources:
- id: src_001
  type: paper
  title: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions (arXiv)
  url: https://arxiv.org/abs/2512.08500
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

## 核心内容
Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

## 参考
- http://arxiv.org/abs/2512.08500v1

