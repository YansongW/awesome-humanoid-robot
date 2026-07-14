---
$id: ent_paper_yu_forcevla_enhancing_vla_models_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation'
  zh: ForceVLA
  ko: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation'
summary:
  en: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (ForceVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Lab, National University of Singapore, Shanghai University,
    Xi’an Jiaotong University, Noematrix Intelligence, Fudan University, Shanghai Jiao Tong University, Shanghai Innovation
    Institute, and published at NIPS25.'
  zh: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (ForceVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Lab, National University of Singapore, Shanghai University,
    Xi’an Jiaotong University, Noematrix Intelligence, Fudan University, Shanghai Jiao Tong University, Shanghai Innovation
    Institute, and published at NIPS25.'
  ko: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (ForceVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Lab, National University of Singapore, Shanghai University,
    Xi’an Jiaotong University, Noematrix Intelligence, Fudan University, Shanghai Jiao Tong University, Shanghai Innovation
    Institute, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- forcevla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.22159v3.
sources:
- id: src_001
  type: paper
  title: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (arXiv)'
  url: https://arxiv.org/abs/2505.22159
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ForceVLA source
  url: https://doi.org/10.48550/arXiv.2505.22159
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2% over strong pi_0-based baselines, achieving up to 80% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025.

## 核心内容
Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2% over strong pi_0-based baselines, achieving up to 80% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025.

## 参考
- http://arxiv.org/abs/2505.22159v3

