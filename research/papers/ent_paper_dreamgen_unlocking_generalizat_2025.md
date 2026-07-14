---
$id: ent_paper_dreamgen_unlocking_generalizat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories'
  zh: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories'
  ko: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories'
summary:
  en: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories is a 2025 work on manipulation for
    humanoid robots.'
  zh: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories is a 2025 work on manipulation for
    humanoid robots.'
  ko: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories is a 2025 work on manipulation for
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
- dreamgen
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.12705v2.
sources:
- id: src_001
  type: paper
  title: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories (arXiv)'
  url: https://arxiv.org/abs/2505.12705
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce DreamGen, a simple yet highly effective 4-stage pipeline for training robot policies that generalize across behaviors and environments through neural trajectories - synthetic robot data generated from video world models. DreamGen leverages state-of-the-art image-to-video generative models, adapting them to the target robot embodiment to produce photorealistic synthetic videos of familiar or novel tasks in diverse environments. Since these models generate only videos, we recover pseudo-action sequences using either a latent action model or an inverse-dynamics model (IDM). Despite its simplicity, DreamGen unlocks strong behavior and environment generalization: a humanoid robot can perform 22 new behaviors in both seen and unseen environments, while requiring teleoperation data from only a single pick-and-place task in one environment. To evaluate the pipeline systematically, we introduce DreamGen Bench, a video generation benchmark that shows a strong correlation between benchmark performance and downstream policy success. Our work establishes a promising new axis for scaling robot learning well beyond manual data collection. Code available at https://github.com/NVIDIA/GR00T-Dreams.

## 核心内容
We introduce DreamGen, a simple yet highly effective 4-stage pipeline for training robot policies that generalize across behaviors and environments through neural trajectories - synthetic robot data generated from video world models. DreamGen leverages state-of-the-art image-to-video generative models, adapting them to the target robot embodiment to produce photorealistic synthetic videos of familiar or novel tasks in diverse environments. Since these models generate only videos, we recover pseudo-action sequences using either a latent action model or an inverse-dynamics model (IDM). Despite its simplicity, DreamGen unlocks strong behavior and environment generalization: a humanoid robot can perform 22 new behaviors in both seen and unseen environments, while requiring teleoperation data from only a single pick-and-place task in one environment. To evaluate the pipeline systematically, we introduce DreamGen Bench, a video generation benchmark that shows a strong correlation between benchmark performance and downstream policy success. Our work establishes a promising new axis for scaling robot learning well beyond manual data collection. Code available at https://github.com/NVIDIA/GR00T-Dreams.

## 参考
- http://arxiv.org/abs/2505.12705v2

