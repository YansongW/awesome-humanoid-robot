---
$id: ent_paper_openspm_an_environment_transfe_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching Action
    Generation Model'
  zh: 'OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching Action
    Generation Model'
  ko: 'OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching Action
    Generation Model'
summary:
  en: "arXiv:2606.29936v2 Announce Type: replace \nAbstract: Open-environment tabletop robotic manipulation requires systems\
    \ to possess semantic understanding, precise geometric pose estimation, and high-frequency action generation. While end-to-end\
    \ vision-language-action (VLA) models excel at semantic generalization, they often lack explicit geometric constraints\
    \ for fine-grained tasks and require costly training. To bridge the gap between high-level semantics and low-level physical\
    \ execution, we propose OpenSPM, an open environment spatial persistent memory framework consisting of spatial pose memory\
    \ and flow-matching action generation model. OpenSPM first leverages semantically conditioned 3D perception and Kalman\
    \ filtering to track continuous 6D poses. It then extracts key spatial poses from human demonstrations, keeping them as\
    \ transferable, object-centric spatial persistent memory entries. During inference, OpenSPM retrieves relevant memory\
    \ entries in terms of natural language instructions, transfers the spatial poses to new scenes using SE(3) transformations,\
    \ and generates high-frequency action chunks via a lightweight conditional flow-matching model. Combined with real-time\
    \ proprioceptive state feedback and terminal residual correction, the system effectively suppresses trajectory error accumulation.\
    \ Evaluated on ten LIBERO-GOAL tasks, OpenSPM achieves an 85.6% success rate and an equivalent control frequency of 1033.3\
    \ Hz, while requiring minimal inference AI computing power. Extensive ablations illustrate that structured spatial persistent\
    \ memory and closed-loop residual correction play a crucial role in reliable, high-frequency robotic manipulation."
  zh: "arXiv:2606.29936v2 Announce Type: replace \nAbstract: Open-environment tabletop robotic manipulation requires systems\
    \ to possess semantic understanding, precise geometric pose estimation, and high-frequency action generation. While end-to-end\
    \ vision-language-action (VLA) models excel at semantic generalization, they often lack explicit geometric constraints\
    \ for fine-grained tasks and require costly training. To bridge the gap between high-level semantics and low-level physical\
    \ execution, we propose OpenSPM, an open environment spatial persistent memory framework consisting of spatial pose memory\
    \ and flow-matching action generation model. OpenSPM first leverages semantically conditioned 3D perception and Kalman\
    \ filtering to track continuous 6D poses. It then extracts key spatial poses from human demonstrations, keeping them as\
    \ transferable, object-centric spatial persistent memory entries. During inference, OpenSPM retrieves relevant memory\
    \ entries in terms of natural language instructions, transfers the spatial poses to new scenes using SE(3) transformations,\
    \ and generates high-frequency action chunks via a lightweight conditional flow-matching model. Combined with real-time\
    \ proprioceptive state feedback and terminal residual correction, the system effectively suppresses trajectory error accumulation.\
    \ Evaluated on ten LIBERO-GOAL tasks, OpenSPM achieves an 85.6% success rate and an equivalent control frequency of 1033.3\
    \ Hz, while requiring minimal inference AI computing power. Extensive ablations illustrate that structured spatial persistent\
    \ memory and closed-loop residual correction play a crucial role in reliable, high-frequency robotic manipulation."
  ko: "arXiv:2606.29936v2 Announce Type: replace \nAbstract: Open-environment tabletop robotic manipulation requires systems\
    \ to possess semantic understanding, precise geometric pose estimation, and high-frequency action generation. While end-to-end\
    \ vision-language-action (VLA) models excel at semantic generalization, they often lack explicit geometric constraints\
    \ for fine-grained tasks and require costly training. To bridge the gap between high-level semantics and low-level physical\
    \ execution, we propose OpenSPM, an open environment spatial persistent memory framework consisting of spatial pose memory\
    \ and flow-matching action generation model. OpenSPM first leverages semantically conditioned 3D perception and Kalman\
    \ filtering to track continuous 6D poses. It then extracts key spatial poses from human demonstrations, keeping them as\
    \ transferable, object-centric spatial persistent memory entries. During inference, OpenSPM retrieves relevant memory\
    \ entries in terms of natural language instructions, transfers the spatial poses to new scenes using SE(3) transformations,\
    \ and generates high-frequency action chunks via a lightweight conditional flow-matching model. Combined with real-time\
    \ proprioceptive state feedback and terminal residual correction, the system effectively suppresses trajectory error accumulation.\
    \ Evaluated on ten LIBERO-GOAL tasks, OpenSPM achieves an 85.6% success rate and an equivalent control frequency of 1033.3\
    \ Hz, while requiring minimal inference AI computing power. Extensive ablations illustrate that structured spatial persistent\
    \ memory and closed-loop residual correction play a crucial role in reliable, high-frequency robotic manipulation."
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
- openspm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.29936v2.
sources:
- id: src_001
  type: paper
  title: 'OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching
    Action Generation Model (arXiv)'
  url: https://arxiv.org/abs/2606.29936
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Open-environment tabletop robotic manipulation requires systems to possess semantic understanding, precise geometric pose estimation, and high-frequency action generation. While end-to-end vision-language-action (VLA) models excel at semantic generalization, they often lack explicit geometric constraints for fine-grained tasks and require costly training. To bridge the gap between high-level semantics and low-level physical execution, we propose OpenSPM, an open environment spatial persistent memory framework consisting of spatial pose memory and flow-matching action generation model. OpenSPM first leverages semantically conditioned 3D perception and Kalman filtering to track continuous 6D poses. It then extracts key spatial poses from human demonstrations, keeping them as transferable, object-centric spatial persistent memory entries. During inference, OpenSPM retrieves relevant memory entries in terms of natural language instructions, transfers the spatial poses to new scenes using SE(3) transformations, and generates high-frequency action chunks via a lightweight conditional flow-matching model. Combined with real-time proprioceptive state feedback and terminal residual correction, the system effectively suppresses trajectory error accumulation. Evaluated on ten LIBERO-GOAL tasks, OpenSPM achieves an 85.6% success rate and an equivalent control frequency of 1033.3 Hz, while requiring minimal inference AI computing power. Extensive ablations illustrate that structured spatial persistent memory and closed-loop residual correction play a crucial role in reliable, high-frequency robotic manipulation.

## 核心内容
Open-environment tabletop robotic manipulation requires systems to possess semantic understanding, precise geometric pose estimation, and high-frequency action generation. While end-to-end vision-language-action (VLA) models excel at semantic generalization, they often lack explicit geometric constraints for fine-grained tasks and require costly training. To bridge the gap between high-level semantics and low-level physical execution, we propose OpenSPM, an open environment spatial persistent memory framework consisting of spatial pose memory and flow-matching action generation model. OpenSPM first leverages semantically conditioned 3D perception and Kalman filtering to track continuous 6D poses. It then extracts key spatial poses from human demonstrations, keeping them as transferable, object-centric spatial persistent memory entries. During inference, OpenSPM retrieves relevant memory entries in terms of natural language instructions, transfers the spatial poses to new scenes using SE(3) transformations, and generates high-frequency action chunks via a lightweight conditional flow-matching model. Combined with real-time proprioceptive state feedback and terminal residual correction, the system effectively suppresses trajectory error accumulation. Evaluated on ten LIBERO-GOAL tasks, OpenSPM achieves an 85.6% success rate and an equivalent control frequency of 1033.3 Hz, while requiring minimal inference AI computing power. Extensive ablations illustrate that structured spatial persistent memory and closed-loop residual correction play a crucial role in reliable, high-frequency robotic manipulation.

## 参考
- http://arxiv.org/abs/2606.29936v2

