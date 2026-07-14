---
$id: ent_paper_whole_world_grounded_hand_obje_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos'
  zh: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos'
  ko: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos'
summary:
  en: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos is a 2026 work on human motion analysis and synthesis
    for humanoid robots.'
  zh: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos is a 2026 work on human motion analysis and synthesis
    for humanoid robots.'
  ko: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos is a 2026 work on human motion analysis and synthesis
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- whole
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.22209v1.
sources:
- id: src_001
  type: paper
  title: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos (arXiv)'
  url: https://arxiv.org/abs/2602.22209
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos project page'
  url: https://judyye.github.io/whole-www/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Egocentric manipulation videos are highly challenging due to severe occlusions during interactions and frequent object entries and exits from the camera view as the person moves. Current methods typically focus on recovering either hand or object pose in isolation, but both struggle during interactions and fail to handle out-of-sight cases. Moreover, their independent predictions often lead to inconsistent hand-object relations. We introduce WHOLE, a method that holistically reconstructs hand and object motion in world space from egocentric videos given object templates. Our key insight is to learn a generative prior over hand-object motion to jointly reason about their interactions. At test time, the pretrained prior is guided to generate trajectories that conform to the video observations. This joint generative reconstruction substantially outperforms approaches that process hands and objects separately followed by post-processing. WHOLE achieves state-of-the-art performance on hand motion estimation, 6D object pose estimation, and their relative interaction reconstruction. Project website: https://judyye.github.io/whole-www

## 核心内容
Egocentric manipulation videos are highly challenging due to severe occlusions during interactions and frequent object entries and exits from the camera view as the person moves. Current methods typically focus on recovering either hand or object pose in isolation, but both struggle during interactions and fail to handle out-of-sight cases. Moreover, their independent predictions often lead to inconsistent hand-object relations. We introduce WHOLE, a method that holistically reconstructs hand and object motion in world space from egocentric videos given object templates. Our key insight is to learn a generative prior over hand-object motion to jointly reason about their interactions. At test time, the pretrained prior is guided to generate trajectories that conform to the video observations. This joint generative reconstruction substantially outperforms approaches that process hands and objects separately followed by post-processing. WHOLE achieves state-of-the-art performance on hand motion estimation, 6D object pose estimation, and their relative interaction reconstruction. Project website: https://judyye.github.io/whole-www

## 参考
- http://arxiv.org/abs/2602.22209v1

