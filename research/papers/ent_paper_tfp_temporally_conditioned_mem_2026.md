---
$id: ent_paper_tfp_temporally_conditioned_mem_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TFP: Temporally Conditioned Memory-Fusion Policies for Visuomotor Learning'
  zh: 'TFP: Temporally Conditioned Memory-Fusion Policies for Visuomotor Learning'
  ko: ''
summary:
  en: "arXiv:2607.08283v1 Announce Type: new \nAbstract: Vision--Language--Action\
    \ (VLA) policies such as $\\pi_{0.5}$ and OpenVLA perform well on many manipulation\
    \ tasks, but they are often reactive: the next action is predicted from the current\
    \ observation, instruction, and proprioceptive state. This assumption breaks down\
    \ in stage-dependent manipulation, where visually similar states may require different\
    \ actions depending on latent task progress and previous interaction outcomes.\
    \ We argue that such tasks require not only memory, but dynamics-aware belief\
    \ updates: the policy should preserve task progress during stable or occluded\
    \ phases and revise its belief near contact, release, or subgoal transitions.\
    \ We introduce Temporally Conditioned Memory-Fusion Policies (TFP), a lightweight\
    \ memory-action framework for VLA backbones. TFP maintains an episode-local task-progress\
    \ belief with Liquid Time-Constant dynamics and injects the updated belief directly\
    \ into the flow-matching action decoder through adaptive modulation. This lets\
    \ temporally accumulated context shape the generated action chunk, rather than\
    \ serving only as passive history context. With a 3.3B-parameter model, TFP improves\
    \ the average success rate from \\(96.9\\%\\) to \\(98.75\\%\\) on LIBERO and\
    \ from \\(91.4\\%\\) to \\(93.77\\%\\) on LIBERO-plus. On the memory-focused MIKASA\
    \ ShellGameTouch diagnostic, TFP achieves success up to \\(75.0\\%\\). Mechanistic\
    \ analyses show that write-gain changes near manipulation events are about \\\
    (6\\times\\) larger than far non-event phases, and hidden-state interventions\
    \ show that the belief causally modulates generated action chunks. These results\
    \ suggest that compact, event-sensitive memory dynamics can improve VLA policies\
    \ under occlusion, visual perturbation, and stage-dependent task structure."
  zh: "arXiv:2607.08283v1 Announce Type: new \nAbstract: Vision--Language--Action\
    \ (VLA) policies such as $\\pi_{0.5}$ and OpenVLA perform well on many manipulation\
    \ tasks, but they are often reactive: the next action is predicted from the current\
    \ observation, instruction, and proprioceptive state. This assumption breaks down\
    \ in stage-dependent manipulation, where visually similar states may require different\
    \ actions depending on latent task progress and previous interaction outcomes.\
    \ We argue that such tasks require not only memory, but dynamics-aware belief\
    \ updates: the policy should preserve task progress during stable or occluded\
    \ phases and revise its belief near contact, release, or subgoal transitions.\
    \ We introduce Temporally Conditioned Memory-Fusion Policies (TFP), a lightweight\
    \ memory-action framework for VLA backbones. TFP maintains an episode-local task-progress\
    \ belief with Liquid Time-Constant dynamics and injects the updated belief directly\
    \ into the flow-matching action decoder through adaptive modulation. This lets\
    \ temporally accumulated context shape the generated action chunk, rather than\
    \ serving only as passive history context. With a 3.3B-parameter model, TFP improves\
    \ the average success rate from \\(96.9\\%\\) to \\(98.75\\%\\) on LIBERO and\
    \ from \\(91.4\\%\\) to \\(93.77\\%\\) on LIBERO-plus. On the memory-focused MIKASA\
    \ ShellGameTouch diagnostic, TFP achieves success up to \\(75.0\\%\\). Mechanistic\
    \ analyses show that write-gain changes near manipulation events are about \\\
    (6\\times\\) larger than far non-event phases, and hidden-state interventions\
    \ show that the belief causally modulates generated action chunks. These results\
    \ suggest that compact, event-sensitive memory dynamics can improve VLA policies\
    \ under occlusion, visual perturbation, and stage-dependent task structure."
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
- tfp
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
  title: 'TFP: Temporally Conditioned Memory-Fusion Policies for Visuomotor Learning
    (arXiv)'
  url: https://arxiv.org/abs/2607.08283
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2607.08283v1 Announce Type: new 
Abstract: Vision--Language--Action (VLA) policies such as $\pi_{0.5}$ and OpenVLA perform well on many manipulation tasks, but they are often reactive: the next action is predicted from the current observation, instruction, and proprioceptive state. This assumption breaks down in stage-dependent manipulation, where visually similar states may require different actions depending on latent task progress and previous interaction outcomes. We argue that such tasks require not only memory, but dynamics-aware belief updates: the policy should preserve task progress during stable or occluded phases and revise its belief near contact, release, or subgoal transitions. We introduce Temporally Conditioned Memory-Fusion Policies (TFP), a lightweight memory-action framework for VLA backbones. TFP maintains an episode-local task-progress belief with Liquid Time-Constant dynamics and injects the updated belief directly into the flow-matching action decoder through adaptive modulation. This lets temporally accumulated context shape the generated action chunk, rather than serving only as passive history context. With a 3.3B-parameter model, TFP improves the average success rate from \(96.9\%\) to \(98.75\%\) on LIBERO and from \(91.4\%\) to \(93.77\%\) on LIBERO-plus. On the memory-focused MIKASA ShellGameTouch diagnostic, TFP achieves success up to \(75.0\%\). Mechanistic analyses show that write-gain changes near manipulation events are about \(6\times\) larger than far non-event phases, and hidden-state interventions show that the belief causally modulates generated action chunks. These results suggest that compact, event-sensitive memory dynamics can improve VLA policies under occlusion, visual perturbation, and stage-dependent task structure.
