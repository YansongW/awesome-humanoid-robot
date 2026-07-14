---
$id: ent_paper_pan_vision_language_action_model_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
  zh: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
  ko: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
summary:
  en: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand (Vision-Language-Action
    Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Swiss Federal Institute of Technology Lausanne.
  zh: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand (Vision-Language-Action
    Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Swiss Federal Institute of Technology Lausanne.
  ko: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand (Vision-Language-Action
    Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Swiss Federal Institute of Technology Lausanne.
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
- robotic_manipulation
- vision_language_action
- vision_language_action_model_a
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.14022v2.
sources:
- id: src_001
  type: paper
  title: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
    (arXiv)
  url: https://arxiv.org/abs/2410.14022
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
    source
  url: https://doi.org/10.48550/arXiv.2410.14022
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Human dexterity arises from combining high-level task reasoning with finger-level dexterity control and physical compliance at the muscle and skin layers. In robotics, large Vision-Language-Action (VLA) models demonstrate text-conditioned high-level planning across diverse manipulation tasks, typically using pincher grippers. Smaller imitation-learning policies, conversely, show success in dexterous tasks using higher degree-of-freedom (DoF) grippers, but only for limited-scope tasks. However, few approaches combine high-level reasoning with dexterous, robust low-level control, which requires both intelligent control and compliant robot design. We propose a method inspired by the two-channel hypothesis of human motor control that combines these capabilities using a switching controller integrating high-level VLAs and smaller control models. Coordination between the two channels is managed through an event-driven switching mechanism that monitors subtask progression and completion, requiring minimal demonstration data by fine-tuning the VLA to predict event signals and training lightweight subtask-level dexterous policies. This approach is applied to our custom compliant 13-DoF anthropomorphic robotic hand, where compliance can be modulated to evaluate its impact on dexterity and robustness when combined with an autonomous policy. We show that hardware-level compliance in robotic fingers enables passive adaptation to disturbances and improves contact stability. The methodology is validated across a range of language-conditioned dexterous tasks. To demonstrate modularity, we show that adaptation to additional dexterous skills and different compliant hands can be achieved without retraining the VLA model. This provides an efficient, scalable, cross-embodiment approach to dexterity that leverages compliance while retaining the advantages of large AI models.

## 核心内容
Human dexterity arises from combining high-level task reasoning with finger-level dexterity control and physical compliance at the muscle and skin layers. In robotics, large Vision-Language-Action (VLA) models demonstrate text-conditioned high-level planning across diverse manipulation tasks, typically using pincher grippers. Smaller imitation-learning policies, conversely, show success in dexterous tasks using higher degree-of-freedom (DoF) grippers, but only for limited-scope tasks. However, few approaches combine high-level reasoning with dexterous, robust low-level control, which requires both intelligent control and compliant robot design. We propose a method inspired by the two-channel hypothesis of human motor control that combines these capabilities using a switching controller integrating high-level VLAs and smaller control models. Coordination between the two channels is managed through an event-driven switching mechanism that monitors subtask progression and completion, requiring minimal demonstration data by fine-tuning the VLA to predict event signals and training lightweight subtask-level dexterous policies. This approach is applied to our custom compliant 13-DoF anthropomorphic robotic hand, where compliance can be modulated to evaluate its impact on dexterity and robustness when combined with an autonomous policy. We show that hardware-level compliance in robotic fingers enables passive adaptation to disturbances and improves contact stability. The methodology is validated across a range of language-conditioned dexterous tasks. To demonstrate modularity, we show that adaptation to additional dexterous skills and different compliant hands can be achieved without retraining the VLA model. This provides an efficient, scalable, cross-embodiment approach to dexterity that leverages compliance while retaining the advantages of large AI models.

## 参考
- http://arxiv.org/abs/2410.14022v2

