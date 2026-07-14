---
$id: ent_paper_maskedmimic_unified_physics_ba_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting'
  zh: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting'
  ko: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting'
summary:
  en: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting is a 2024 work on physics-based
    character animation for humanoid robots.'
  zh: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting is a 2024 work on physics-based
    character animation for humanoid robots.'
  ko: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting is a 2024 work on physics-based
    character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- maskedmimic
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.14393v1.
sources:
- id: src_001
  type: paper
  title: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting (arXiv)'
  url: https://arxiv.org/abs/2409.14393
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting project page'
  url: https://research.nvidia.com/labs/par/maskedmimic/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Crafting a single, versatile physics-based controller that can breathe life into interactive characters across a wide spectrum of scenarios represents an exciting frontier in character animation. An ideal controller should support diverse control modalities, such as sparse target keyframes, text instructions, and scene information. While previous works have proposed physically simulated, scene-aware control models, these systems have predominantly focused on developing controllers that each specializes in a narrow set of tasks and control modalities. This work presents MaskedMimic, a novel approach that formulates physics-based character control as a general motion inpainting problem. Our key insight is to train a single unified model to synthesize motions from partial (masked) motion descriptions, such as masked keyframes, objects, text descriptions, or any combination thereof. This is achieved by leveraging motion tracking data and designing a scalable training method that can effectively utilize diverse motion descriptions to produce coherent animations. Through this process, our approach learns a physics-based controller that provides an intuitive control interface without requiring tedious reward engineering for all behaviors of interest. The resulting controller supports a wide range of control modalities and enables seamless transitions between disparate tasks. By unifying character control through motion inpainting, MaskedMimic creates versatile virtual characters. These characters can dynamically adapt to complex scenes and compose diverse motions on demand, enabling more interactive and immersive experiences.

## 核心内容
Crafting a single, versatile physics-based controller that can breathe life into interactive characters across a wide spectrum of scenarios represents an exciting frontier in character animation. An ideal controller should support diverse control modalities, such as sparse target keyframes, text instructions, and scene information. While previous works have proposed physically simulated, scene-aware control models, these systems have predominantly focused on developing controllers that each specializes in a narrow set of tasks and control modalities. This work presents MaskedMimic, a novel approach that formulates physics-based character control as a general motion inpainting problem. Our key insight is to train a single unified model to synthesize motions from partial (masked) motion descriptions, such as masked keyframes, objects, text descriptions, or any combination thereof. This is achieved by leveraging motion tracking data and designing a scalable training method that can effectively utilize diverse motion descriptions to produce coherent animations. Through this process, our approach learns a physics-based controller that provides an intuitive control interface without requiring tedious reward engineering for all behaviors of interest. The resulting controller supports a wide range of control modalities and enables seamless transitions between disparate tasks. By unifying character control through motion inpainting, MaskedMimic creates versatile virtual characters. These characters can dynamically adapt to complex scenes and compose diverse motions on demand, enabling more interactive and immersive experiences.

## 参考
- http://arxiv.org/abs/2409.14393v1

