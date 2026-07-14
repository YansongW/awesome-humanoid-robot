---
$id: ent_paper_mimic2dm_learning_to_control_p_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions'
  zh: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions'
  ko: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions'
summary:
  en: Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing
    realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf
    motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle
    with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible
    poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters.
    We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly
    and solely from widely available 2D keypoint trajectorie
  zh: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a paper
    on 物理动画 for humanoid robotics.'
  ko: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a paper
    on 物理动画 for humanoid robotics.'
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
- mimic2dm
- physics_based
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Mimic2DM: Learning to Control
    Physically-simulated 3D Characters via Generating and Mimicking 2D Motions.'
sources:
- id: src_001
  type: website
  title: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions'
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

## 核心内容
Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

## 参考
- Semantic Scholar search: Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions

