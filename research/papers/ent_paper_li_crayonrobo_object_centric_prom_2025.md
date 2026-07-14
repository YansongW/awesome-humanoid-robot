---
$id: ent_paper_li_crayonrobo_object_centric_prom_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation'
  zh: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation
  ko: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation'
summary:
  en: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation (Object-Centric Prompt-Driven
    Vision-Language-Action Model for Robotic Manipulation), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Peking University, PKU-Agibot Lab, and published at CVPR25.'
  zh: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation (Object-Centric Prompt-Driven
    Vision-Language-Action Model for Robotic Manipulation), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Peking University, PKU-Agibot Lab, and published at CVPR25.'
  ko: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation (Object-Centric Prompt-Driven
    Vision-Language-Action Model for Robotic Manipulation), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Peking University, PKU-Agibot Lab, and published at CVPR25.'
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
- object_centric_prompt_driven_v
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.02166v1.
sources:
- id: src_001
  type: paper
  title: 'CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2505.02166
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation source
  url: https://doi.org/10.48550/arXiv.2505.02166
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In robotic, task goals can be conveyed through various modalities, such as language, goal images, and goal videos. However, natural language can be ambiguous, while images or videos may offer overly detailed specifications. To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner. Specifically, for each key-frame in the task sequence, our method allows for manual or automatic generation of simple and expressive 2D visual prompts overlaid on RGB images. These prompts represent the required task goals, such as the end-effector pose and the desired movement direction after contact. We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space. Furthermore, by sequentially executing all key-frame steps, the model can complete long-horizon tasks. This approach not only helps the model explicitly understand the task objectives but also enhances its robustness on unseen tasks by providing easily interpretable prompts. We evaluate our method in both simulated and real-world environments, demonstrating its robust manipulation capabilities.

## 核心内容
In robotic, task goals can be conveyed through various modalities, such as language, goal images, and goal videos. However, natural language can be ambiguous, while images or videos may offer overly detailed specifications. To tackle these challenges, we introduce CrayonRobo that leverages comprehensive multi-modal prompts that explicitly convey both low-level actions and high-level planning in a simple manner. Specifically, for each key-frame in the task sequence, our method allows for manual or automatic generation of simple and expressive 2D visual prompts overlaid on RGB images. These prompts represent the required task goals, such as the end-effector pose and the desired movement direction after contact. We develop a training strategy that enables the model to interpret these visual-language prompts and predict the corresponding contact poses and movement directions in SE(3) space. Furthermore, by sequentially executing all key-frame steps, the model can complete long-horizon tasks. This approach not only helps the model explicitly understand the task objectives but also enhances its robustness on unseen tasks by providing easily interpretable prompts. We evaluate our method in both simulated and real-world environments, demonstrating its robust manipulation capabilities.

## 参考
- http://arxiv.org/abs/2505.02166v1

