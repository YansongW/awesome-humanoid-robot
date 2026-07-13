---
$id: ent_paper_robosnap_one_shot_real_to_sim_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning
    and Evaluation'
  zh: 'RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning
    and Evaluation'
  ko: ''
summary:
  en: "arXiv:2607.06699v1 Announce Type: new \nAbstract: Recovering real-world scenes\
    \ as interactive simulation environments can enable generalizable robot learning\
    \ and reproducible policy evaluation. However, constructing scenes that are both\
    \ physically stable and visually faithful remains slow and expensive. In this\
    \ work, we present RoboSnap, a real-to-sim framework that turns a single RGB image\
    \ into a simulation-ready scene. The key idea is a layered design that separates\
    \ the physics-critical interaction area from the surrounding visual context: collision-aware\
    \ foreground assets are refined for stable robot interaction, while a 3D Gaussian\
    \ splatting visual layer preserves faithful background appearance under novel\
    \ views. Experiments on DROID scenes and real-robot tasks show that RoboSnap achieves\
    \ reliable trajectory replay in the recovered scenes, supports task-specific synthetic\
    \ data generation for policy training, and yields meaningful sim-real correlation\
    \ for policy evaluation. To further support real-to-sim research, we introduce\
    \ DROID-Sim, a real-to-sim companion dataset constructed from 564 real-world scenes\
    \ in DROID. Extensive experiments suggest that the value of real-to-sim methods\
    \ lies not only in high-fidelity visual reconstruction, but in turning real environments\
    \ into reusable infrastructure for robot learning and evaluation."
  zh: "arXiv:2607.06699v1 Announce Type: new \nAbstract: Recovering real-world scenes\
    \ as interactive simulation environments can enable generalizable robot learning\
    \ and reproducible policy evaluation. However, constructing scenes that are both\
    \ physically stable and visually faithful remains slow and expensive. In this\
    \ work, we present RoboSnap, a real-to-sim framework that turns a single RGB image\
    \ into a simulation-ready scene. The key idea is a layered design that separates\
    \ the physics-critical interaction area from the surrounding visual context: collision-aware\
    \ foreground assets are refined for stable robot interaction, while a 3D Gaussian\
    \ splatting visual layer preserves faithful background appearance under novel\
    \ views. Experiments on DROID scenes and real-robot tasks show that RoboSnap achieves\
    \ reliable trajectory replay in the recovered scenes, supports task-specific synthetic\
    \ data generation for policy training, and yields meaningful sim-real correlation\
    \ for policy evaluation. To further support real-to-sim research, we introduce\
    \ DROID-Sim, a real-to-sim companion dataset constructed from 564 real-world scenes\
    \ in DROID. Extensive experiments suggest that the value of real-to-sim methods\
    \ lies not only in high-fidelity visual reconstruction, but in turning real environments\
    \ into reusable infrastructure for robot learning and evaluation."
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
- robosnap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-10'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot
    Learning and Evaluation (arXiv)'
  url: https://arxiv.org/abs/2607.06699
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.06699v1 Announce Type: new 
Abstract: Recovering real-world scenes as interactive simulation environments can enable generalizable robot learning and reproducible policy evaluation. However, constructing scenes that are both physically stable and visually faithful remains slow and expensive. In this work, we present RoboSnap, a real-to-sim framework that turns a single RGB image into a simulation-ready scene. The key idea is a layered design that separates the physics-critical interaction area from the surrounding visual context: collision-aware foreground assets are refined for stable robot interaction, while a 3D Gaussian splatting visual layer preserves faithful background appearance under novel views. Experiments on DROID scenes and real-robot tasks show that RoboSnap achieves reliable trajectory replay in the recovered scenes, supports task-specific synthetic data generation for policy training, and yields meaningful sim-real correlation for policy evaluation. To further support real-to-sim research, we introduce DROID-Sim, a real-to-sim companion dataset constructed from 564 real-world scenes in DROID. Extensive experiments suggest that the value of real-to-sim methods lies not only in high-fidelity visual reconstruction, but in turning real environments into reusable infrastructure for robot learning and evaluation.
