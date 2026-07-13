---
$id: ent_paper_contactmimic_humanoid_object_i_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ContactMimic: Humanoid Object Interaction via Contact Control'
  zh: 'ContactMimic: Humanoid Object Interaction via Contact Control'
  ko: ''
summary:
  en: "arXiv:2607.08742v1 Announce Type: new \nAbstract: Keypoint tracking alone is\
    \ insufficient for object interaction tasks such as sitting on a chair, wiping\
    \ a board, or pushing furniture, where the robot can reach the correct pose without\
    \ making meaningful physical contact with the object. We present CONTACTMIMIC,\
    \ a learning framework that tracks explicit partlevel binary contact commands\
    \ alongside keypoint trajectories. CONTACTMIMIC is made possible through the use\
    \ of contact-following rewards and a trajectory augmentation scheme aimed at breaking\
    \ the correlations between keypoint trajectories and contact labels. The resulting\
    \ policy successfully decouples contact behavior from keypoint geometry, and achieves\
    \ precise physical contact as well as contact-controllability (produce or suppress\
    \ contact during deployment as desired). Simulation experiments across 10 diverse\
    \ human-object interaction motions confirm that CONTACTMIMIC exhibits contact\
    \ controllability that enables it to complete manipulation tasks without task-specific\
    \ rewards, while also outperforming keypoint-only trackers on contact-relevant\
    \ tasks. Ablations confirm the necessity of the proposed trajectory augmentation\
    \ scheme and sim2real deployment validates contact controllability in the real\
    \ world across 5 different motions. Video results are available on https://lixinyao11.github.io/contactmimic-page/."
  zh: "arXiv:2607.08742v1 Announce Type: new \nAbstract: Keypoint tracking alone is\
    \ insufficient for object interaction tasks such as sitting on a chair, wiping\
    \ a board, or pushing furniture, where the robot can reach the correct pose without\
    \ making meaningful physical contact with the object. We present CONTACTMIMIC,\
    \ a learning framework that tracks explicit partlevel binary contact commands\
    \ alongside keypoint trajectories. CONTACTMIMIC is made possible through the use\
    \ of contact-following rewards and a trajectory augmentation scheme aimed at breaking\
    \ the correlations between keypoint trajectories and contact labels. The resulting\
    \ policy successfully decouples contact behavior from keypoint geometry, and achieves\
    \ precise physical contact as well as contact-controllability (produce or suppress\
    \ contact during deployment as desired). Simulation experiments across 10 diverse\
    \ human-object interaction motions confirm that CONTACTMIMIC exhibits contact\
    \ controllability that enables it to complete manipulation tasks without task-specific\
    \ rewards, while also outperforming keypoint-only trackers on contact-relevant\
    \ tasks. Ablations confirm the necessity of the proposed trajectory augmentation\
    \ scheme and sim2real deployment validates contact controllability in the real\
    \ world across 5 different motions. Video results are available on https://lixinyao11.github.io/contactmimic-page/."
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
- contactmimic
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
  title: 'ContactMimic: Humanoid Object Interaction via Contact Control (arXiv)'
  url: https://arxiv.org/abs/2607.08742
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2607.08742v1 Announce Type: new 
Abstract: Keypoint tracking alone is insufficient for object interaction tasks such as sitting on a chair, wiping a board, or pushing furniture, where the robot can reach the correct pose without making meaningful physical contact with the object. We present CONTACTMIMIC, a learning framework that tracks explicit partlevel binary contact commands alongside keypoint trajectories. CONTACTMIMIC is made possible through the use of contact-following rewards and a trajectory augmentation scheme aimed at breaking the correlations between keypoint trajectories and contact labels. The resulting policy successfully decouples contact behavior from keypoint geometry, and achieves precise physical contact as well as contact-controllability (produce or suppress contact during deployment as desired). Simulation experiments across 10 diverse human-object interaction motions confirm that CONTACTMIMIC exhibits contact controllability that enables it to complete manipulation tasks without task-specific rewards, while also outperforming keypoint-only trackers on contact-relevant tasks. Ablations confirm the necessity of the proposed trajectory augmentation scheme and sim2real deployment validates contact controllability in the real world across 5 different motions. Video results are available on https://lixinyao11.github.io/contactmimic-page/.
