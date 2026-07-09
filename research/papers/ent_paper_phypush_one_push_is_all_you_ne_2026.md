---
$id: ent_paper_phypush_one_push_is_all_you_ne_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhyPush: One Push is All You Need for Sensorless Physical Property Estimation
    with Physics-Guided Transformers'
  zh: 'PhyPush: One Push is All You Need for Sensorless Physical Property Estimation
    with Physics-Guided Transformers'
  ko: ''
summary:
  en: "arXiv:2605.26284v2 Announce Type: replace \nAbstract: Accurately estimating\
    \ object mass and friction is fundamental to reliable robotic manipulation. While\
    \ interactive perception is powerful, most approaches rely on specialized hardware\
    \ like force/torque sensors, limiting scalability. This paper introduces PhyPush,\
    \ a physics-guided Transformer that estimates an object's mass and friction coefficient\
    \ using only end-effector velocity from a single push, data readily available\
    \ on standard robotic arms. By incorporating Newton's second law and the Coulomb\
    \ friction model through a physics-guided loss, the model improves physical consistency\
    \ and generalizes to unseen objects and surfaces. Across diverse setups, PhyPush\
    \ consistently achieves highly accurate estimations in challenging out-of-domain\
    \ conditions. In simulation, it reduces error by over 10% compared to a baseline\
    \ with privileged force data, while in real-world experiments, it successfully\
    \ zero-shot transfers from simulation to outperform a purely data-driven baseline."
  zh: "arXiv:2605.26284v2 Announce Type: replace \nAbstract: Accurately estimating\
    \ object mass and friction is fundamental to reliable robotic manipulation. While\
    \ interactive perception is powerful, most approaches rely on specialized hardware\
    \ like force/torque sensors, limiting scalability. This paper introduces PhyPush,\
    \ a physics-guided Transformer that estimates an object's mass and friction coefficient\
    \ using only end-effector velocity from a single push, data readily available\
    \ on standard robotic arms. By incorporating Newton's second law and the Coulomb\
    \ friction model through a physics-guided loss, the model improves physical consistency\
    \ and generalizes to unseen objects and surfaces. Across diverse setups, PhyPush\
    \ consistently achieves highly accurate estimations in challenging out-of-domain\
    \ conditions. In simulation, it reduces error by over 10% compared to a baseline\
    \ with privileged force data, while in real-world experiments, it successfully\
    \ zero-shot transfers from simulation to outperform a purely data-driven baseline."
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
- phypush
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-03'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'PhyPush: One Push is All You Need for Sensorless Physical Property Estimation
    with Physics-Guided Transformers (arXiv)'
  url: https://arxiv.org/abs/2605.26284
  date: '2026'
  accessed_at: '2026-07-03'
---

arXiv:2605.26284v2 Announce Type: replace 
Abstract: Accurately estimating object mass and friction is fundamental to reliable robotic manipulation. While interactive perception is powerful, most approaches rely on specialized hardware like force/torque sensors, limiting scalability. This paper introduces PhyPush, a physics-guided Transformer that estimates an object's mass and friction coefficient using only end-effector velocity from a single push, data readily available on standard robotic arms. By incorporating Newton's second law and the Coulomb friction model through a physics-guided loss, the model improves physical consistency and generalizes to unseen objects and surfaces. Across diverse setups, PhyPush consistently achieves highly accurate estimations in challenging out-of-domain conditions. In simulation, it reduces error by over 10% compared to a baseline with privileged force data, while in real-world experiments, it successfully zero-shot transfers from simulation to outperform a purely data-driven baseline.
