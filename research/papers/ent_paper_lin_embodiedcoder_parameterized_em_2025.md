---
$id: ent_paper_lin_embodiedcoder_parameterized_em_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model'
  zh: EmbodiedCoder
  ko: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model'
summary:
  en: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (EmbodiedCoder), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by University of Chinese Academy of Sciences (UCAS),
    Institute of Automation, Chinese Academy of Sciences (CASIA), New Laboratory of Pattern Recognition (NLPR), State Key
    Laboratory of Multimodal Artificial Intelligence Systems (MAIS), Beihang University, Chinese University of Hong Kong.'
  zh: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (EmbodiedCoder), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by University of Chinese Academy of Sciences (UCAS),
    Institute of Automation, Chinese Academy of Sciences (CASIA), New Laboratory of Pattern Recognition (NLPR), State Key
    Laboratory of Multimodal Artificial Intelligence Systems (MAIS), Beihang University, Chinese University of Hong Kong.'
  ko: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (EmbodiedCoder), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by University of Chinese Academy of Sciences (UCAS),
    Institute of Automation, Chinese Academy of Sciences (CASIA), New Laboratory of Pattern Recognition (NLPR), State Key
    Laboratory of Multimodal Artificial Intelligence Systems (MAIS), Beihang University, Chinese University of Hong Kong.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodiedcoder
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.06207v2.
sources:
- id: src_001
  type: paper
  title: 'EmbodiedCoder: Parameterized Embodied Mobile Manipulation via Modern Coding Model (arXiv)'
  url: https://arxiv.org/abs/2510.06207
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EmbodiedCoder source
  url: https://doi.org/10.48550/arXiv.2510.06207
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in control robot methods, from end-to-end vision-language-action frameworks to modular systems with predefined primitives, have advanced robots' ability to follow natural language instructions. Nonetheless, many approaches still struggle to scale to diverse environments, as they often rely on large annotated datasets and offer limited interpretability.In this work, we introduce EmbodiedCoder, a training-free framework for open-world mobile robot manipulation that leverages coding models to directly generate executable robot trajectories. By grounding high-level instructions in code, EmbodiedCoder enables flexible object geometry parameterization and manipulation trajectory synthesis without additional data collection or fine-tuning.This coding-based paradigm provides a transparent and generalizable way to connect perception with manipulation. Experiments on real mobile robots show that EmbodiedCoder achieves robust performance across diverse long-term tasks and generalizes effectively to novel objects and environments.Our results demonstrate an interpretable approach for bridging high-level reasoning and low-level control, moving beyond fixed primitives toward versatile robot intelligence. See the project page at: https://embodiedcoder.github.io/EmbodiedCoder/

## 核心内容
Recent advances in control robot methods, from end-to-end vision-language-action frameworks to modular systems with predefined primitives, have advanced robots' ability to follow natural language instructions. Nonetheless, many approaches still struggle to scale to diverse environments, as they often rely on large annotated datasets and offer limited interpretability.In this work, we introduce EmbodiedCoder, a training-free framework for open-world mobile robot manipulation that leverages coding models to directly generate executable robot trajectories. By grounding high-level instructions in code, EmbodiedCoder enables flexible object geometry parameterization and manipulation trajectory synthesis without additional data collection or fine-tuning.This coding-based paradigm provides a transparent and generalizable way to connect perception with manipulation. Experiments on real mobile robots show that EmbodiedCoder achieves robust performance across diverse long-term tasks and generalizes effectively to novel objects and environments.Our results demonstrate an interpretable approach for bridging high-level reasoning and low-level control, moving beyond fixed primitives toward versatile robot intelligence. See the project page at: https://embodiedcoder.github.io/EmbodiedCoder/

## 参考
- http://arxiv.org/abs/2510.06207v2

