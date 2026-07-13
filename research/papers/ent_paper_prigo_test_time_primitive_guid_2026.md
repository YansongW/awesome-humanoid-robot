---
$id: ent_paper_prigo_test_time_primitive_guid_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PriGo: Test-Time Primitive Guidance to Diffusion and Flow Policies for Adaptive
    Robotic Manipulation'
  zh: 'PriGo: Test-Time Primitive Guidance to Diffusion and Flow Policies for Adaptive
    Robotic Manipulation'
  ko: ''
summary:
  en: "arXiv:2607.07076v1 Announce Type: new \nAbstract: Imitation learning has enabled\
    \ remarkable progress in robotic manipulation, especially with diffusion and flow-based\
    \ policies that generate complex visuomotor behaviors directly from demonstrations.\
    \ Yet, despite their strong performance, these policies often fail to generalize\
    \ across tasks and environments. A key reason is that existing policies tend to\
    \ imitate superficial action correlations rather than the underlying intent. Inspired\
    \ by the compositional structure of human behaviors, we propose PriGo, a primitive-guided\
    \ test-time adaptive framework for robust robotic manipulation. PriGo introduces\
    \ PANet, a lightweight primitive prediction module that infers primitive distributions\
    \ directly from observations. We further propose a differentiable primitive guidance\
    \ mechanism that refines generated actions during inference, steering trajectories\
    \ toward semantically consistent behaviors. Unlike prior primitive-conditioned\
    \ approaches, PriGo operates entirely at test time and can be seamlessly integrated\
    \ into pretrained diffusion and flow policies without retraining. Extensive experiments\
    \ on LIBERO, CALVIN, SIMPLER, and real-world robotic tasks demonstrate that PriGo\
    \ consistently improves robustness, long-horizon execution, and generalization\
    \ ability across both diffusion and flow-based policies."
  zh: "arXiv:2607.07076v1 Announce Type: new \nAbstract: Imitation learning has enabled\
    \ remarkable progress in robotic manipulation, especially with diffusion and flow-based\
    \ policies that generate complex visuomotor behaviors directly from demonstrations.\
    \ Yet, despite their strong performance, these policies often fail to generalize\
    \ across tasks and environments. A key reason is that existing policies tend to\
    \ imitate superficial action correlations rather than the underlying intent. Inspired\
    \ by the compositional structure of human behaviors, we propose PriGo, a primitive-guided\
    \ test-time adaptive framework for robust robotic manipulation. PriGo introduces\
    \ PANet, a lightweight primitive prediction module that infers primitive distributions\
    \ directly from observations. We further propose a differentiable primitive guidance\
    \ mechanism that refines generated actions during inference, steering trajectories\
    \ toward semantically consistent behaviors. Unlike prior primitive-conditioned\
    \ approaches, PriGo operates entirely at test time and can be seamlessly integrated\
    \ into pretrained diffusion and flow policies without retraining. Extensive experiments\
    \ on LIBERO, CALVIN, SIMPLER, and real-world robotic tasks demonstrate that PriGo\
    \ consistently improves robustness, long-horizon execution, and generalization\
    \ ability across both diffusion and flow-based policies."
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
- prigo
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
  title: 'PriGo: Test-Time Primitive Guidance to Diffusion and Flow Policies for Adaptive
    Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.07076
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.07076v1 Announce Type: new 
Abstract: Imitation learning has enabled remarkable progress in robotic manipulation, especially with diffusion and flow-based policies that generate complex visuomotor behaviors directly from demonstrations. Yet, despite their strong performance, these policies often fail to generalize across tasks and environments. A key reason is that existing policies tend to imitate superficial action correlations rather than the underlying intent. Inspired by the compositional structure of human behaviors, we propose PriGo, a primitive-guided test-time adaptive framework for robust robotic manipulation. PriGo introduces PANet, a lightweight primitive prediction module that infers primitive distributions directly from observations. We further propose a differentiable primitive guidance mechanism that refines generated actions during inference, steering trajectories toward semantically consistent behaviors. Unlike prior primitive-conditioned approaches, PriGo operates entirely at test time and can be seamlessly integrated into pretrained diffusion and flow policies without retraining. Extensive experiments on LIBERO, CALVIN, SIMPLER, and real-world robotic tasks demonstrate that PriGo consistently improves robustness, long-horizon execution, and generalization ability across both diffusion and flow-based policies.
