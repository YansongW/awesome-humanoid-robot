---
$id: ent_paper_ardy_autoregressive_diffusion_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human
    Motion Generation'
  zh: 'ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human
    Motion Generation'
  ko: ''
summary:
  en: "arXiv:2607.08741v1 Announce Type: cross \nAbstract: Generating realistic 3D\
    \ human motions in real-time within interactive applications is key for animation,\
    \ simulation, and humanoid robotics. While recent offline motion generation approaches\
    \ offer precise control via text and kinematic constraints, they lack the inference\
    \ speed required for interactive settings. Conversely, existing online methods\
    \ enable real-time synthesis but often sacrifice controllability or struggle with\
    \ complex text semantics and long-horizon goals due to limited context windows.\
    \ In this work, we introduce ARDY, a streaming generation framework that bridges\
    \ this gap by enabling high-fidelity motion generation controllable via online\
    \ text prompts and flexible kinematic constraints. ARDY employs a hybrid representation\
    \ that combines explicit root features with a latent body embedding, balancing\
    \ precise trajectory control with efficient generative learning. We propose a\
    \ two-stage autoregressive transformer denoiser that features variable history\
    \ context and supports conditioning on flexible, long-horizon kinematic constraints.\
    \ By training on a large-scale motion capture dataset and being directly conditioned\
    \ on text labels and kinematic constraints sampled from ground truth poses, ARDY\
    \ natively learns controllable generation that supports online prompting and flexible\
    \ long-horizon goals. Extensive evaluations on the HumanML3D benchmark and the\
    \ large-scale, high-fidelity Bones Rigplay dataset demonstrate ARDY's high motion\
    \ quality and constraint adherence, validating the efficacy of our key architectural\
    \ decisions. Finally, we demonstrate the method's practical versatility through\
    \ an interactive demo featuring dynamic text control, diverse keyframe pose constraints,\
    \ path following, and interactive locomotion control via mouse and keyboard. Supplementary\
    \ video results, code, and model releases can be found at https://research.nvidia.com/labs/sil/projects/ardy/."
  zh: "arXiv:2607.08741v1 Announce Type: cross \nAbstract: Generating realistic 3D\
    \ human motions in real-time within interactive applications is key for animation,\
    \ simulation, and humanoid robotics. While recent offline motion generation approaches\
    \ offer precise control via text and kinematic constraints, they lack the inference\
    \ speed required for interactive settings. Conversely, existing online methods\
    \ enable real-time synthesis but often sacrifice controllability or struggle with\
    \ complex text semantics and long-horizon goals due to limited context windows.\
    \ In this work, we introduce ARDY, a streaming generation framework that bridges\
    \ this gap by enabling high-fidelity motion generation controllable via online\
    \ text prompts and flexible kinematic constraints. ARDY employs a hybrid representation\
    \ that combines explicit root features with a latent body embedding, balancing\
    \ precise trajectory control with efficient generative learning. We propose a\
    \ two-stage autoregressive transformer denoiser that features variable history\
    \ context and supports conditioning on flexible, long-horizon kinematic constraints.\
    \ By training on a large-scale motion capture dataset and being directly conditioned\
    \ on text labels and kinematic constraints sampled from ground truth poses, ARDY\
    \ natively learns controllable generation that supports online prompting and flexible\
    \ long-horizon goals. Extensive evaluations on the HumanML3D benchmark and the\
    \ large-scale, high-fidelity Bones Rigplay dataset demonstrate ARDY's high motion\
    \ quality and constraint adherence, validating the efficacy of our key architectural\
    \ decisions. Finally, we demonstrate the method's practical versatility through\
    \ an interactive demo featuring dynamic text control, diverse keyframe pose constraints,\
    \ path following, and interactive locomotion control via mouse and keyboard. Supplementary\
    \ video results, code, and model releases can be found at https://research.nvidia.com/labs/sil/projects/ardy/."
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
- ardy
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
  title: 'ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive
    Human Motion Generation (arXiv)'
  url: https://arxiv.org/abs/2607.08741
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2607.08741v1 Announce Type: cross 
Abstract: Generating realistic 3D human motions in real-time within interactive applications is key for animation, simulation, and humanoid robotics. While recent offline motion generation approaches offer precise control via text and kinematic constraints, they lack the inference speed required for interactive settings. Conversely, existing online methods enable real-time synthesis but often sacrifice controllability or struggle with complex text semantics and long-horizon goals due to limited context windows. In this work, we introduce ARDY, a streaming generation framework that bridges this gap by enabling high-fidelity motion generation controllable via online text prompts and flexible kinematic constraints. ARDY employs a hybrid representation that combines explicit root features with a latent body embedding, balancing precise trajectory control with efficient generative learning. We propose a two-stage autoregressive transformer denoiser that features variable history context and supports conditioning on flexible, long-horizon kinematic constraints. By training on a large-scale motion capture dataset and being directly conditioned on text labels and kinematic constraints sampled from ground truth poses, ARDY natively learns controllable generation that supports online prompting and flexible long-horizon goals. Extensive evaluations on the HumanML3D benchmark and the large-scale, high-fidelity Bones Rigplay dataset demonstrate ARDY's high motion quality and constraint adherence, validating the efficacy of our key architectural decisions. Finally, we demonstrate the method's practical versatility through an interactive demo featuring dynamic text control, diverse keyframe pose constraints, path following, and interactive locomotion control via mouse and keyboard. Supplementary video results, code, and model releases can be found at https://research.nvidia.com/labs/sil/projects/ardy/.
