---
$id: ent_paper_wam_ttt_steering_world_action_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time'
  zh: 'WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time'
  ko: ''
summary:
  en: "arXiv:2607.06988v1 Announce Type: new \nAbstract: Steering robot foundation\
    \ models (RFMs) toward new task variants or user-preferred behaviors remains challenging,\
    \ often requiring additional robot demonstrations, task-specific fine-tuning,\
    \ or long-context conditioning. We present WAM-TTT, a test-time training framework\
    \ for steering world action models from raw human videos. Rather than treating\
    \ human videos as trajectories to imitate, WAM-TTT absorbs them into a lightweight\
    \ adaptive memory inside a frozen WAM through self-supervised video prediction.\
    \ To make this memory useful for control, we introduce a meta-training stage that\
    \ aligns human demonstrations with robot behaviors using paired human-robot data\
    \ and a key--value memory reconstruction objective. At test time, only unlabeled\
    \ human videos are required to adapt the memory, while the pretrained WAM remains\
    \ frozen. This enables efficient and reusable steering without robot actions,\
    \ human-side annotations, or task-specific fine-tuning, while preserving the generalization\
    \ ability of the foundation model. Extensive experiments show that WAM-TTT consistently\
    \ outperforms in-context human-video conditioning baselines across diverse manipulation\
    \ tasks and generalization settings."
  zh: "arXiv:2607.06988v1 Announce Type: new \nAbstract: Steering robot foundation\
    \ models (RFMs) toward new task variants or user-preferred behaviors remains challenging,\
    \ often requiring additional robot demonstrations, task-specific fine-tuning,\
    \ or long-context conditioning. We present WAM-TTT, a test-time training framework\
    \ for steering world action models from raw human videos. Rather than treating\
    \ human videos as trajectories to imitate, WAM-TTT absorbs them into a lightweight\
    \ adaptive memory inside a frozen WAM through self-supervised video prediction.\
    \ To make this memory useful for control, we introduce a meta-training stage that\
    \ aligns human demonstrations with robot behaviors using paired human-robot data\
    \ and a key--value memory reconstruction objective. At test time, only unlabeled\
    \ human videos are required to adapt the memory, while the pretrained WAM remains\
    \ frozen. This enables efficient and reusable steering without robot actions,\
    \ human-side annotations, or task-specific fine-tuning, while preserving the generalization\
    \ ability of the foundation model. Extensive experiments show that WAM-TTT consistently\
    \ outperforms in-context human-video conditioning baselines across diverse manipulation\
    \ tasks and generalization settings."
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
- wam_ttt
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
  title: 'WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time
    (arXiv)'
  url: https://arxiv.org/abs/2607.06988
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.06988v1 Announce Type: new 
Abstract: Steering robot foundation models (RFMs) toward new task variants or user-preferred behaviors remains challenging, often requiring additional robot demonstrations, task-specific fine-tuning, or long-context conditioning. We present WAM-TTT, a test-time training framework for steering world action models from raw human videos. Rather than treating human videos as trajectories to imitate, WAM-TTT absorbs them into a lightweight adaptive memory inside a frozen WAM through self-supervised video prediction. To make this memory useful for control, we introduce a meta-training stage that aligns human demonstrations with robot behaviors using paired human-robot data and a key--value memory reconstruction objective. At test time, only unlabeled human videos are required to adapt the memory, while the pretrained WAM remains frozen. This enables efficient and reusable steering without robot actions, human-side annotations, or task-specific fine-tuning, while preserving the generalization ability of the foundation model. Extensive experiments show that WAM-TTT consistently outperforms in-context human-video conditioning baselines across diverse manipulation tasks and generalization settings.
