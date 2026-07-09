---
$id: ent_paper_abot_m05_unified_mobility_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model'
  zh: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model'
  ko: ''
summary:
  en: "arXiv:2607.00678v1 Announce Type: cross \nAbstract: Mobile manipulation is\
    \ a key capability for general-purpose robots, yet remains challenging for current\
    \ embodied learning methods. VLA policies are typically reactive and lack explicit\
    \ world modeling, while existing World Action Models (WAMs) are still poorly aligned\
    \ with the structure of mobile manipulation: they operate on coarse video chunks,\
    \ model entangled navigation-manipulation actions, and train inverse dynamics\
    \ under supervision that does not match autoregressive inference. As a result,\
    \ they often miss fine-grained contact dynamics, suffer from action-distribution\
    \ conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5,\
    \ a new WAM built on the insight that mobile manipulation requires alignment at\
    \ three levels: temporal granularity, action space, and train-test consistency.\
    \ To align temporal granularity, we introduce intermediate latent actions that\
    \ capture local visual state transitions and serve as an bridging action space\
    \ between video latents and embodiment-specific controls. To align action space,\
    \ we design a dual-level Mixture-of-Transformers architecture that disentangles\
    \ both modality representations and heterogeneous action subspaces such as base\
    \ movement and arm manipulation. To align inference conditions, we propose the\
    \ dream-forcing training strategy that progressively trains inverse dynamics on\
    \ model-predicted videos, improving train-test alignment and robustness during\
    \ autoregressive prediction. Experiments on challenging mobile and fine-grained\
    \ manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art\
    \ performance in both long-horizon task success and finegrained control accuracy.\
    \ These results highlight the critical importance of granularity-aligned, action-disentangled,\
    \ and inference-consistent world-action modeling."
  zh: "arXiv:2607.00678v1 Announce Type: cross \nAbstract: Mobile manipulation is\
    \ a key capability for general-purpose robots, yet remains challenging for current\
    \ embodied learning methods. VLA policies are typically reactive and lack explicit\
    \ world modeling, while existing World Action Models (WAMs) are still poorly aligned\
    \ with the structure of mobile manipulation: they operate on coarse video chunks,\
    \ model entangled navigation-manipulation actions, and train inverse dynamics\
    \ under supervision that does not match autoregressive inference. As a result,\
    \ they often miss fine-grained contact dynamics, suffer from action-distribution\
    \ conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5,\
    \ a new WAM built on the insight that mobile manipulation requires alignment at\
    \ three levels: temporal granularity, action space, and train-test consistency.\
    \ To align temporal granularity, we introduce intermediate latent actions that\
    \ capture local visual state transitions and serve as an bridging action space\
    \ between video latents and embodiment-specific controls. To align action space,\
    \ we design a dual-level Mixture-of-Transformers architecture that disentangles\
    \ both modality representations and heterogeneous action subspaces such as base\
    \ movement and arm manipulation. To align inference conditions, we propose the\
    \ dream-forcing training strategy that progressively trains inverse dynamics on\
    \ model-predicted videos, improving train-test alignment and robustness during\
    \ autoregressive prediction. Experiments on challenging mobile and fine-grained\
    \ manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art\
    \ performance in both long-horizon task success and finegrained control accuracy.\
    \ These results highlight the critical importance of granularity-aligned, action-disentangled,\
    \ and inference-consistent world-action modeling."
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
- abot_m05
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
  title: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model (arXiv)'
  url: https://arxiv.org/abs/2607.00678
  date: '2026'
  accessed_at: '2026-07-03'
---

arXiv:2607.00678v1 Announce Type: cross 
Abstract: Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics, suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space, and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local visual state transitions and serve as an bridging action space between video latents and embodiment-specific controls. To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test alignment and robustness during autoregressive prediction. Experiments on challenging mobile and fine-grained manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent world-action modeling.
