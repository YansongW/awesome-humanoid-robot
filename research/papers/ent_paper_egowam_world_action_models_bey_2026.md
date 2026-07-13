---
$id: ent_paper_egowam_world_action_models_bey_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human
    Data'
  zh: 'EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human
    Data'
  ko: ''
summary:
  en: "arXiv:2607.08436v1 Announce Type: new \nAbstract: Egocentric human data offers\
    \ scalable supervision for robot manipulation. However, behavior cloning entangles\
    \ transferable content like objects, scenes, and task semantics, with non-transferable\
    \ factors like human morphology, head motion, and behavioral style. We study whether\
    \ World Action Models (WAMs) provide a better training signal by requiring policies\
    \ to predict not only actions, but also how the scene evolves. The central question\
    \ is what world representation best enables human-to-robot transfer. We hypothesize\
    \ that an effective world target should abstract appearance, capture agent-invariant\
    \ physical effects, and separate camera motion from environment change. We introduce\
    \ EgoWAM, a controlled human-robot co-training framework that fixes the policy\
    \ backbone, action head, and data mixture while varying only the world prediction\
    \ target, comparing Pixel, DINO, and 3D motion flow. Across three real-world bimanual\
    \ tasks, WAM co-training scales more effectively with in-the-wild egocentric human\
    \ data than behavior cloning. Pixel-based prediction transfers weakly, while DINO\
    \ and 3D flow yield substantial gains: DINO improves out-of-distribution object\
    \ and scene generalization by up to 4x, and 3D flow improves in-domain performance\
    \ by 20-30%. More details: https://gatech-rl2.github.io/egowam.github.io"
  zh: "arXiv:2607.08436v1 Announce Type: new \nAbstract: Egocentric human data offers\
    \ scalable supervision for robot manipulation. However, behavior cloning entangles\
    \ transferable content like objects, scenes, and task semantics, with non-transferable\
    \ factors like human morphology, head motion, and behavioral style. We study whether\
    \ World Action Models (WAMs) provide a better training signal by requiring policies\
    \ to predict not only actions, but also how the scene evolves. The central question\
    \ is what world representation best enables human-to-robot transfer. We hypothesize\
    \ that an effective world target should abstract appearance, capture agent-invariant\
    \ physical effects, and separate camera motion from environment change. We introduce\
    \ EgoWAM, a controlled human-robot co-training framework that fixes the policy\
    \ backbone, action head, and data mixture while varying only the world prediction\
    \ target, comparing Pixel, DINO, and 3D motion flow. Across three real-world bimanual\
    \ tasks, WAM co-training scales more effectively with in-the-wild egocentric human\
    \ data than behavior cloning. Pixel-based prediction transfers weakly, while DINO\
    \ and 3D flow yield substantial gains: DINO improves out-of-distribution object\
    \ and scene generalization by up to 4x, and 3D flow improves in-domain performance\
    \ by 20-30%. More details: https://gatech-rl2.github.io/egowam.github.io"
  ko: ''
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
- robotics
- egowam
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-11'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human
    Data (arXiv)'
  url: https://arxiv.org/abs/2607.08436
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2607.08436v1 Announce Type: new 
Abstract: Egocentric human data offers scalable supervision for robot manipulation. However, behavior cloning entangles transferable content like objects, scenes, and task semantics, with non-transferable factors like human morphology, head motion, and behavioral style. We study whether World Action Models (WAMs) provide a better training signal by requiring policies to predict not only actions, but also how the scene evolves. The central question is what world representation best enables human-to-robot transfer. We hypothesize that an effective world target should abstract appearance, capture agent-invariant physical effects, and separate camera motion from environment change. We introduce EgoWAM, a controlled human-robot co-training framework that fixes the policy backbone, action head, and data mixture while varying only the world prediction target, comparing Pixel, DINO, and 3D motion flow. Across three real-world bimanual tasks, WAM co-training scales more effectively with in-the-wild egocentric human data than behavior cloning. Pixel-based prediction transfers weakly, while DINO and 3D flow yield substantial gains: DINO improves out-of-distribution object and scene generalization by up to 4x, and 3D flow improves in-domain performance by 20-30%. More details: https://gatech-rl2.github.io/egowam.github.io
