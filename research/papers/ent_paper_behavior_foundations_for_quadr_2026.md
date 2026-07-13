---
$id: ent_paper_behavior_foundations_for_quadr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report'
  zh: 'Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report'
  ko: ''
summary:
  en: "arXiv:2607.07370v1 Announce Type: new \nAbstract: In embodied intelligence\
    \ systems, the motion controller serves as the critical bridge between semantic\
    \ reasoning and physical execution. Humanoid control has progressed rapidly through\
    \ large-scale human motion-capture data and motion-tracking paradigm. However,\
    \ producing quadruped robots motion corpora with scalability and physical feasibility\
    \ faces more fundamental obstacles: animal motion data is scarce, and cross-embodiment\
    \ retargeting remains fragile. We present ABot-C0, a generalist motion-control\
    \ system for quadruped robots that establishes three complementary behavior foundations:\
    \ a scalable multi-source motion-data pipeline, robust policy learning across\
    \ motion tracking, locomotion, and scene interaction, and a unified deployment\
    \ stack for reliable real-world operation. Fundamentally, we construct a data\
    \ pyramid through conditional video-generation synthesis, annotated motion capture,\
    \ teleoperation and human design, producing 16,074 physically feasible motion\
    \ clips as the data foundation for various motion learning demands. We then train\
    \ a Flow-Matching generalist policy that demonstrates for the first time quadruped\
    \ motion tracking scaling law that its performance improves consistently as training\
    \ scales up, with zero-shot capability to track unseen motions. Then, we push\
    \ a step further for robust all-terrain traversal locomotion by adopting a three-stage\
    \ privileged-to-perceptive framework with temporal LiDAR memory and terrain-predictive\
    \ supervision. Collectively, these components form a motion generalist that coordinates\
    \ multi-policy execution, smooth behavior transitions, energy-efficient control,\
    \ and safety mechanisms for real-world deployment. Extensive experiments on urban-terrain\
    \ autonomous navigation and companion-style multimodal interaction demonstrate\
    \ that quadruped robots move beyond single-function demos toward product-level\
    \ behavioral intelligence."
  zh: "arXiv:2607.07370v1 Announce Type: new \nAbstract: In embodied intelligence\
    \ systems, the motion controller serves as the critical bridge between semantic\
    \ reasoning and physical execution. Humanoid control has progressed rapidly through\
    \ large-scale human motion-capture data and motion-tracking paradigm. However,\
    \ producing quadruped robots motion corpora with scalability and physical feasibility\
    \ faces more fundamental obstacles: animal motion data is scarce, and cross-embodiment\
    \ retargeting remains fragile. We present ABot-C0, a generalist motion-control\
    \ system for quadruped robots that establishes three complementary behavior foundations:\
    \ a scalable multi-source motion-data pipeline, robust policy learning across\
    \ motion tracking, locomotion, and scene interaction, and a unified deployment\
    \ stack for reliable real-world operation. Fundamentally, we construct a data\
    \ pyramid through conditional video-generation synthesis, annotated motion capture,\
    \ teleoperation and human design, producing 16,074 physically feasible motion\
    \ clips as the data foundation for various motion learning demands. We then train\
    \ a Flow-Matching generalist policy that demonstrates for the first time quadruped\
    \ motion tracking scaling law that its performance improves consistently as training\
    \ scales up, with zero-shot capability to track unseen motions. Then, we push\
    \ a step further for robust all-terrain traversal locomotion by adopting a three-stage\
    \ privileged-to-perceptive framework with temporal LiDAR memory and terrain-predictive\
    \ supervision. Collectively, these components form a motion generalist that coordinates\
    \ multi-policy execution, smooth behavior transitions, energy-efficient control,\
    \ and safety mechanisms for real-world deployment. Extensive experiments on urban-terrain\
    \ autonomous navigation and companion-style multimodal interaction demonstrate\
    \ that quadruped robots move beyond single-function demos toward product-level\
    \ behavioral intelligence."
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
- behavior_foundations_for_quadr
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
  title: 'Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report (arXiv)'
  url: https://arxiv.org/abs/2607.07370
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.07370v1 Announce Type: new 
Abstract: In embodied intelligence systems, the motion controller serves as the critical bridge between semantic reasoning and physical execution. Humanoid control has progressed rapidly through large-scale human motion-capture data and motion-tracking paradigm. However, producing quadruped robots motion corpora with scalability and physical feasibility faces more fundamental obstacles: animal motion data is scarce, and cross-embodiment retargeting remains fragile. We present ABot-C0, a generalist motion-control system for quadruped robots that establishes three complementary behavior foundations: a scalable multi-source motion-data pipeline, robust policy learning across motion tracking, locomotion, and scene interaction, and a unified deployment stack for reliable real-world operation. Fundamentally, we construct a data pyramid through conditional video-generation synthesis, annotated motion capture, teleoperation and human design, producing 16,074 physically feasible motion clips as the data foundation for various motion learning demands. We then train a Flow-Matching generalist policy that demonstrates for the first time quadruped motion tracking scaling law that its performance improves consistently as training scales up, with zero-shot capability to track unseen motions. Then, we push a step further for robust all-terrain traversal locomotion by adopting a three-stage privileged-to-perceptive framework with temporal LiDAR memory and terrain-predictive supervision. Collectively, these components form a motion generalist that coordinates multi-policy execution, smooth behavior transitions, energy-efficient control, and safety mechanisms for real-world deployment. Extensive experiments on urban-terrain autonomous navigation and companion-style multimodal interaction demonstrate that quadruped robots move beyond single-function demos toward product-level behavioral intelligence.
