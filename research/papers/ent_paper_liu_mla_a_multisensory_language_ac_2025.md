---
$id: ent_paper_liu_mla_a_multisensory_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation'
  zh: MLA
  ko: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation'
summary:
  en: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (MLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia
    Information Processing, School of Computer Science, Peking University, Beijing Innovation Center of Humanoid Robotics,
    Chinese University of Hong Kong.'
  zh: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (MLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia
    Information Processing, School of Computer Science, Peking University, Beijing Innovation Center of Humanoid Robotics,
    Chinese University of Hong Kong.'
  ko: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (MLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia
    Information Processing, School of Computer Science, Peking University, Beijing Innovation Center of Humanoid Robotics,
    Chinese University of Hong Kong.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- mla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26642v2.
sources:
- id: src_001
  type: paper
  title: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.26642
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MLA source
  url: https://doi.org/10.48550/arXiv.2509.26642
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action models (VLAs) have shown generalization capabilities in robotic manipulation tasks by inheriting from vision-language models (VLMs) and learning action generation. Most VLA models focus on interpreting vision and language to generate actions, whereas robots must perceive and interact within the spatial-physical world. This gap highlights the need for a comprehensive understanding of robotic-specific multisensory information, which is crucial for achieving complex and contact-rich control. To this end, we introduce a multisensory language-action (MLA) model that collaboratively perceives heterogeneous sensory modalities and predicts future multisensory objectives to facilitate physical world modeling. Specifically, to enhance perceptual representations, we propose an encoder-free multimodal alignment scheme that innovatively repurposes the large language model itself as a perception module, directly interpreting multimodal cues by aligning 2D images, 3D point clouds, and tactile tokens through positional correspondence. To further enhance MLA's understanding of physical dynamics, we design a future multisensory generation post-training strategy that enables MLA to reason about semantic, geometric, and interaction information, providing more robust conditions for action generation. For evaluation, the MLA model outperforms the previous state-of-the-art 2D and 3D VLA methods by 12% and 24% in complex, contact-rich real-world tasks, respectively, while also demonstrating improved generalization to unseen configurations.

## 核心内容
Vision-language-action models (VLAs) have shown generalization capabilities in robotic manipulation tasks by inheriting from vision-language models (VLMs) and learning action generation. Most VLA models focus on interpreting vision and language to generate actions, whereas robots must perceive and interact within the spatial-physical world. This gap highlights the need for a comprehensive understanding of robotic-specific multisensory information, which is crucial for achieving complex and contact-rich control. To this end, we introduce a multisensory language-action (MLA) model that collaboratively perceives heterogeneous sensory modalities and predicts future multisensory objectives to facilitate physical world modeling. Specifically, to enhance perceptual representations, we propose an encoder-free multimodal alignment scheme that innovatively repurposes the large language model itself as a perception module, directly interpreting multimodal cues by aligning 2D images, 3D point clouds, and tactile tokens through positional correspondence. To further enhance MLA's understanding of physical dynamics, we design a future multisensory generation post-training strategy that enables MLA to reason about semantic, geometric, and interaction information, providing more robust conditions for action generation. For evaluation, the MLA model outperforms the previous state-of-the-art 2D and 3D VLA methods by 12% and 24% in complex, contact-rich real-world tasks, respectively, while also demonstrating improved generalization to unseen configurations.

## 参考
- http://arxiv.org/abs/2509.26642v2

