---
$id: ent_paper_pac_act_post_training_actor_cr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers'
  zh: 'PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers'
  ko: ''
summary:
  en: "arXiv:2607.09590v1 Announce Type: new \nAbstract: Precision industrial contact\
    \ manipulation requires reliable robot policies under pose perturbations and contact-force\
    \ constraints. Vision-language-action models offer broad generalization but often\
    \ introduce high inference latency and GPU-memory cost, while vision-action chunking\
    \ policies are more suitable for real-time industrial control. However, these\
    \ policies are usually trained by behavior cloning and suffer from distribution\
    \ shift in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning\
    \ post-training framework for pretrained Action Chunking Transformer policies.\
    \ PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred\
    \ actor-critic architecture, and introduces a hybrid behavior-prior constraint\
    \ to preserve the pretrained action distribution during online fine-tuning. Experiments\
    \ on industrial precision-contact benchmarks show that PAC-ACT improves task success,\
    \ contact stability, and force safety while retaining low latency and low GPU-memory\
    \ usage. On the Contour task, PAC-ACT significantly reduces peak contact force\
    \ and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward\
    \ ablations further show that the proposed behavior-prior constraint enables effective\
    \ exploration under randomized initial poses."
  zh: "arXiv:2607.09590v1 Announce Type: new \nAbstract: Precision industrial contact\
    \ manipulation requires reliable robot policies under pose perturbations and contact-force\
    \ constraints. Vision-language-action models offer broad generalization but often\
    \ introduce high inference latency and GPU-memory cost, while vision-action chunking\
    \ policies are more suitable for real-time industrial control. However, these\
    \ policies are usually trained by behavior cloning and suffer from distribution\
    \ shift in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning\
    \ post-training framework for pretrained Action Chunking Transformer policies.\
    \ PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred\
    \ actor-critic architecture, and introduces a hybrid behavior-prior constraint\
    \ to preserve the pretrained action distribution during online fine-tuning. Experiments\
    \ on industrial precision-contact benchmarks show that PAC-ACT improves task success,\
    \ contact stability, and force safety while retaining low latency and low GPU-memory\
    \ usage. On the Contour task, PAC-ACT significantly reduces peak contact force\
    \ and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward\
    \ ablations further show that the proposed behavior-prior constraint enables effective\
    \ exploration under randomized initial poses."
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
- pac_act
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-13'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers (arXiv)'
  url: https://arxiv.org/abs/2607.09590
  date: '2026'
  accessed_at: '2026-07-13'
---

arXiv:2607.09590v1 Announce Type: new 
Abstract: Precision industrial contact manipulation requires reliable robot policies under pose perturbations and contact-force constraints. Vision-language-action models offer broad generalization but often introduce high inference latency and GPU-memory cost, while vision-action chunking policies are more suitable for real-time industrial control. However, these policies are usually trained by behavior cloning and suffer from distribution shift in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning post-training framework for pretrained Action Chunking Transformer policies. PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred actor-critic architecture, and introduces a hybrid behavior-prior constraint to preserve the pretrained action distribution during online fine-tuning. Experiments on industrial precision-contact benchmarks show that PAC-ACT improves task success, contact stability, and force safety while retaining low latency and low GPU-memory usage. On the Contour task, PAC-ACT significantly reduces peak contact force and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward ablations further show that the proposed behavior-prior constraint enables effective exploration under randomized initial poses.
