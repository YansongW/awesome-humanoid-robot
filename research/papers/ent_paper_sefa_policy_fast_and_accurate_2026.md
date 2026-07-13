---
$id: ent_paper_sefa_policy_fast_and_accurate_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SeFA-Policy: Fast and Accurate Visuomotor Policy Learning with Selective Flow
    Alignment'
  zh: 'SeFA-Policy: Fast and Accurate Visuomotor Policy Learning with Selective Flow
    Alignment'
  ko: ''
summary:
  en: "arXiv:2511.08583v2 Announce Type: replace \nAbstract: Developing efficient\
    \ and accurate visuomotor policies poses a central challenge in robotic imitation\
    \ learning. While recent rectified flow approaches have advanced visuomotor policy\
    \ learning, they suffer from a key limitation: After iterative distillation, generated\
    \ actions may deviate from the ground-truth actions corresponding to the current\
    \ visual observation, leading to accumulated error as the reflow process repeats\
    \ and unstable task execution. We present Selective Flow Alignment (SeFA), an\
    \ efficient and accurate visuomotor policy learning framework. SeFA resolves this\
    \ challenge by a selective flow alignment strategy, which leverages expert demonstrations\
    \ to selectively correct generated actions and restore consistency with observations,\
    \ while preserving multimodality. This design introduces a consistency correction\
    \ mechanism that ensures generated actions remain observation-aligned without\
    \ sacrificing the efficiency of one-step flow inference. Extensive experiments\
    \ across both simulated and real-world manipulation tasks show that SeFA Policy\
    \ surpasses state-of-the-art diffusion-based and flow-based policies, achieving\
    \ superior accuracy and robustness while reducing inference latency by over 98%.\
    \ By unifying rectified flow efficiency with observation-consistent action generation,\
    \ SeFA provides a scalable and dependable solution for real-time visuomotor policy\
    \ learning. Code is available on https://github.com/RongXueZoe/SeFA."
  zh: "arXiv:2511.08583v2 Announce Type: replace \nAbstract: Developing efficient\
    \ and accurate visuomotor policies poses a central challenge in robotic imitation\
    \ learning. While recent rectified flow approaches have advanced visuomotor policy\
    \ learning, they suffer from a key limitation: After iterative distillation, generated\
    \ actions may deviate from the ground-truth actions corresponding to the current\
    \ visual observation, leading to accumulated error as the reflow process repeats\
    \ and unstable task execution. We present Selective Flow Alignment (SeFA), an\
    \ efficient and accurate visuomotor policy learning framework. SeFA resolves this\
    \ challenge by a selective flow alignment strategy, which leverages expert demonstrations\
    \ to selectively correct generated actions and restore consistency with observations,\
    \ while preserving multimodality. This design introduces a consistency correction\
    \ mechanism that ensures generated actions remain observation-aligned without\
    \ sacrificing the efficiency of one-step flow inference. Extensive experiments\
    \ across both simulated and real-world manipulation tasks show that SeFA Policy\
    \ surpasses state-of-the-art diffusion-based and flow-based policies, achieving\
    \ superior accuracy and robustness while reducing inference latency by over 98%.\
    \ By unifying rectified flow efficiency with observation-consistent action generation,\
    \ SeFA provides a scalable and dependable solution for real-time visuomotor policy\
    \ learning. Code is available on https://github.com/RongXueZoe/SeFA."
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
- sefa_policy
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
  title: 'SeFA-Policy: Fast and Accurate Visuomotor Policy Learning with Selective
    Flow Alignment (arXiv)'
  url: https://arxiv.org/abs/2511.08583
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2511.08583v2 Announce Type: replace 
Abstract: Developing efficient and accurate visuomotor policies poses a central challenge in robotic imitation learning. While recent rectified flow approaches have advanced visuomotor policy learning, they suffer from a key limitation: After iterative distillation, generated actions may deviate from the ground-truth actions corresponding to the current visual observation, leading to accumulated error as the reflow process repeats and unstable task execution. We present Selective Flow Alignment (SeFA), an efficient and accurate visuomotor policy learning framework. SeFA resolves this challenge by a selective flow alignment strategy, which leverages expert demonstrations to selectively correct generated actions and restore consistency with observations, while preserving multimodality. This design introduces a consistency correction mechanism that ensures generated actions remain observation-aligned without sacrificing the efficiency of one-step flow inference. Extensive experiments across both simulated and real-world manipulation tasks show that SeFA Policy surpasses state-of-the-art diffusion-based and flow-based policies, achieving superior accuracy and robustness while reducing inference latency by over 98%. By unifying rectified flow efficiency with observation-consistent action generation, SeFA provides a scalable and dependable solution for real-time visuomotor policy learning. Code is available on https://github.com/RongXueZoe/SeFA.
