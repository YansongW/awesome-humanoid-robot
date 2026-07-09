---
$id: ent_paper_furniturevla_learning_long_hor_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action
    Model'
  zh: 'FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action
    Model'
  ko: ''
summary:
  en: "arXiv:2607.01212v1 Announce Type: new \nAbstract: Current work on robot furniture\
    \ assembly mostly focuses on toy-scale settings or single-arm manipulation. We\
    \ introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture\
    \ assembly using Vision-Language-Action models (VLAs). We formalize the task,\
    \ develop a scalable simulation pipeline for expert data generation and evaluation,\
    \ and build a VR teleoperation system for single-operator bimanual control to\
    \ collect high-quality real-world demonstrations. To address extreme long-horizon\
    \ assembly with up to 7 subtasks and 1550 control steps, we propose a progress-enhanced\
    \ VLA, finetuned on semantically grounded subtasks, that jointly predicts actions\
    \ and a continuous progress signal, enabling automatic subtask transitions and\
    \ reducing compounding errors during inference. We further study perception and\
    \ control design factors that critically affect precision in real-scale assembly.\
    \ FurnitureVLA improves average simulation success from 48% to 80% compared to\
    \ baselines across three furniture types, with an additional 21% gain from our\
    \ design factor study. We validate on a real Kinova Gen3 platform with only 16%\
    \ drop on the hardest task."
  zh: "arXiv:2607.01212v1 Announce Type: new \nAbstract: Current work on robot furniture\
    \ assembly mostly focuses on toy-scale settings or single-arm manipulation. We\
    \ introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture\
    \ assembly using Vision-Language-Action models (VLAs). We formalize the task,\
    \ develop a scalable simulation pipeline for expert data generation and evaluation,\
    \ and build a VR teleoperation system for single-operator bimanual control to\
    \ collect high-quality real-world demonstrations. To address extreme long-horizon\
    \ assembly with up to 7 subtasks and 1550 control steps, we propose a progress-enhanced\
    \ VLA, finetuned on semantically grounded subtasks, that jointly predicts actions\
    \ and a continuous progress signal, enabling automatic subtask transitions and\
    \ reducing compounding errors during inference. We further study perception and\
    \ control design factors that critically affect precision in real-scale assembly.\
    \ FurnitureVLA improves average simulation success from 48% to 80% compared to\
    \ baselines across three furniture types, with an additional 21% gain from our\
    \ design factor study. We validate on a real Kinova Gen3 platform with only 16%\
    \ drop on the hardest task."
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
- furniturevla
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
  title: 'FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action
    Model (arXiv)'
  url: https://arxiv.org/abs/2607.01212
  date: '2026'
  accessed_at: '2026-07-03'
---

arXiv:2607.01212v1 Announce Type: new 
Abstract: Current work on robot furniture assembly mostly focuses on toy-scale settings or single-arm manipulation. We introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture assembly using Vision-Language-Action models (VLAs). We formalize the task, develop a scalable simulation pipeline for expert data generation and evaluation, and build a VR teleoperation system for single-operator bimanual control to collect high-quality real-world demonstrations. To address extreme long-horizon assembly with up to 7 subtasks and 1550 control steps, we propose a progress-enhanced VLA, finetuned on semantically grounded subtasks, that jointly predicts actions and a continuous progress signal, enabling automatic subtask transitions and reducing compounding errors during inference. We further study perception and control design factors that critically affect precision in real-scale assembly. FurnitureVLA improves average simulation success from 48% to 80% compared to baselines across three furniture types, with an additional 21% gain from our design factor study. We validate on a real Kinova Gen3 platform with only 16% drop on the hardest task.
