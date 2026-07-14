---
$id: ent_paper_zhong_dexgraspvla_a_vision_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping'
  zh: DexGraspVLA
  ko: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping'
summary:
  en: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping (DexGraspVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute for Artificial Intelligence, Peking University, PKU-PsiBot Joint
    Lab, Hong Kong University of Science and Technology (Guangzhou), University of Pennsylvania.'
  zh: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping (DexGraspVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute for Artificial Intelligence, Peking University, PKU-PsiBot Joint
    Lab, Hong Kong University of Science and Technology (Guangzhou), University of Pennsylvania.'
  ko: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping (DexGraspVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute for Artificial Intelligence, Peking University, PKU-PsiBot Joint
    Lab, Hong Kong University of Science and Technology (Guangzhou), University of Pennsylvania.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexgraspvla
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.20900v5.
sources:
- id: src_001
  type: paper
  title: 'DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping (arXiv)'
  url: https://arxiv.org/abs/2502.20900
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DexGraspVLA source
  url: https://doi.org/10.48550/arXiv.2502.20900
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Dexterous grasping remains a fundamental yet challenging problem in robotics. A general-purpose robot must be capable of grasping diverse objects in arbitrary scenarios. However, existing research typically relies on restrictive assumptions, such as single-object settings or limited environments, showing constrained generalization. We present DexGraspVLA, a hierarchical framework for robust generalization in language-guided general dexterous grasping and beyond. It utilizes a pre-trained Vision-Language model as the high-level planner and learns a diffusion-based low-level Action controller. The key insight to achieve generalization lies in iteratively transforming diverse language and visual inputs into domain-invariant representations via foundation models, where imitation learning can be effectively applied due to the alleviation of domain shift. Notably, our method achieves a 90+% dexterous grasping success rate under thousands of challenging unseen cluttered scenes. Empirical analysis confirms the consistency of internal model behavior across environmental variations, validating our design. DexGraspVLA also, for the first time, simultaneously demonstrates free-form long-horizon prompt execution, robustness to adversarial objects and human disturbance, and failure recovery. Extended application to nonprehensile grasping further proves its generality. Project website: https://dexgraspvla.github.io.

## 核心内容
Dexterous grasping remains a fundamental yet challenging problem in robotics. A general-purpose robot must be capable of grasping diverse objects in arbitrary scenarios. However, existing research typically relies on restrictive assumptions, such as single-object settings or limited environments, showing constrained generalization. We present DexGraspVLA, a hierarchical framework for robust generalization in language-guided general dexterous grasping and beyond. It utilizes a pre-trained Vision-Language model as the high-level planner and learns a diffusion-based low-level Action controller. The key insight to achieve generalization lies in iteratively transforming diverse language and visual inputs into domain-invariant representations via foundation models, where imitation learning can be effectively applied due to the alleviation of domain shift. Notably, our method achieves a 90+% dexterous grasping success rate under thousands of challenging unseen cluttered scenes. Empirical analysis confirms the consistency of internal model behavior across environmental variations, validating our design. DexGraspVLA also, for the first time, simultaneously demonstrates free-form long-horizon prompt execution, robustness to adversarial objects and human disturbance, and failure recovery. Extended application to nonprehensile grasping further proves its generality. Project website: https://dexgraspvla.github.io.

## 参考
- http://arxiv.org/abs/2502.20900v5

