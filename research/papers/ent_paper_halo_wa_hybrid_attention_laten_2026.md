---
$id: ent_paper_halo_wa_hybrid_attention_laten_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action
    Models'
  zh: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action
    Models'
  ko: ''
summary:
  en: "arXiv:2607.04265v1 Announce Type: new \nAbstract: World-action (WA) models\
    \ can generate long-horizon action chunks for general-purpose robotic manipulation,\
    \ but they remain vulnerable to calibration, perception, and contact-dynamics\
    \ errors in real-world precision tasks, often failing in the final few millimeters\
    \ of alignment or insertion. We propose HALO-WA, a hybrid-attention latent-guided\
    \ online reinforcement learning (RL) framework for WA models, which leverages\
    \ latent features and action priors from the WA generation process through a lightweight\
    \ actor-critic adapter to enable fast online adaptation to real deployment errors.\
    \ HALO-WA introduces a hybrid-attention structure that preserves the temporal\
    \ consistency of action chunks while reading task-relevant information from WA\
    \ latents conditioned on visual context and end-stage correction requirements,\
    \ thereby producing refined action chunks. We validate HALO-WA on four real-world\
    \ precision manipulation tasks, where it improves the average success rate from\
    \ 26.4\\% for WA-base to 87.1\\%, outperforming the strongest baseline by 19.2\
    \ percentage points while requiring only 45--75 minutes of online training per\
    \ task. To facilitate reproducibility, we further conduct supplementary simulation\
    \ experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA."
  zh: "arXiv:2607.04265v1 Announce Type: new \nAbstract: World-action (WA) models\
    \ can generate long-horizon action chunks for general-purpose robotic manipulation,\
    \ but they remain vulnerable to calibration, perception, and contact-dynamics\
    \ errors in real-world precision tasks, often failing in the final few millimeters\
    \ of alignment or insertion. We propose HALO-WA, a hybrid-attention latent-guided\
    \ online reinforcement learning (RL) framework for WA models, which leverages\
    \ latent features and action priors from the WA generation process through a lightweight\
    \ actor-critic adapter to enable fast online adaptation to real deployment errors.\
    \ HALO-WA introduces a hybrid-attention structure that preserves the temporal\
    \ consistency of action chunks while reading task-relevant information from WA\
    \ latents conditioned on visual context and end-stage correction requirements,\
    \ thereby producing refined action chunks. We validate HALO-WA on four real-world\
    \ precision manipulation tasks, where it improves the average success rate from\
    \ 26.4\\% for WA-base to 87.1\\%, outperforming the strongest baseline by 19.2\
    \ percentage points while requiring only 45--75 minutes of online training per\
    \ task. To facilitate reproducibility, we further conduct supplementary simulation\
    \ experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA."
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
- halo_wa
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for
    World-Action Models (arXiv)'
  url: https://arxiv.org/abs/2607.04265
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2607.04265v1 Announce Type: new 
Abstract: World-action (WA) models can generate long-horizon action chunks for general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA, a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks, where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by 19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility, we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.
