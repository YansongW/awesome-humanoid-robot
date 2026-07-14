---
$id: ent_paper_hirose_omnivla_an_omni_modal_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation'
  zh: OmniVLA
  ko: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation'
summary:
  en: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (OmniVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.'
  zh: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (OmniVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.'
  ko: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (OmniVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.'
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
- omnivla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19480v1.
sources:
- id: src_001
  type: paper
  title: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (arXiv)'
  url: https://arxiv.org/abs/2509.19480
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OmniVLA source
  url: https://doi.org/10.48550/arXiv.2509.19480
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination. In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and complementary. In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation. Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as their combinations, through a randomized modality fusion strategy. This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations. The resulting model, OmniVLA, achieves strong generalization to unseen environments, robustness to scarce modalities, and the ability to follow novel natural language instructions. We demonstrate that OmniVLA outperforms specialist baselines across modalities and offers a flexible foundation for fine-tuning to new modalities and tasks. We believe OmniVLA provides a step toward broadly generalizable and flexible navigation policies, and a scalable path for building omni-modal robotic foundation models. We present videos showcasing OmniVLA performance and will release its checkpoints and training code on our project page.

## 核心内容
Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination. In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and complementary. In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation. Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as their combinations, through a randomized modality fusion strategy. This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations. The resulting model, OmniVLA, achieves strong generalization to unseen environments, robustness to scarce modalities, and the ability to follow novel natural language instructions. We demonstrate that OmniVLA outperforms specialist baselines across modalities and offers a flexible foundation for fine-tuning to new modalities and tasks. We believe OmniVLA provides a step toward broadly generalizable and flexible navigation policies, and a scalable path for building omni-modal robotic foundation models. We present videos showcasing OmniVLA performance and will release its checkpoints and training code on our project page.

## 参考
- http://arxiv.org/abs/2509.19480v1

