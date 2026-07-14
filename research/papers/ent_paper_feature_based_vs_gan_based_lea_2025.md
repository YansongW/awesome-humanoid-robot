---
$id: ent_paper_feature_based_vs_gan_based_lea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why'
  zh: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why'
  ko: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why'
summary:
  en: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why is a 2025 work on physics-based character animation
    for humanoid robots.'
  zh: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why is a 2025 work on physics-based character animation
    for humanoid robots.'
  ko: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why is a 2025 work on physics-based character animation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- feature_based_vs_gan_based_lea
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.05906v2.
sources:
- id: src_001
  type: paper
  title: 'Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why (arXiv)'
  url: https://arxiv.org/abs/2507.05906
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This survey provides a comparative analysis of feature-based and GAN-based approaches to learning from demonstrations, with a focus on the structure of reward functions and their implications for policy learning. Feature-based methods offer dense, interpretable rewards that excel at high-fidelity motion imitation, yet often require sophisticated representations of references and struggle with generalization in unstructured settings. GAN-based methods, in contrast, use implicit, distributional supervision that enables scalability and adaptation flexibility, but are prone to training instability and coarse reward signals. Recent advancements in both paradigms converge on the importance of structured motion representations, which enable smoother transitions, controllable synthesis, and improved task integration. We argue that the dichotomy between feature-based and GAN-based methods is increasingly nuanced: rather than one paradigm dominating the other, the choice should be guided by task-specific priorities such as fidelity, diversity, interpretability, and adaptability. This work outlines the algorithmic trade-offs and design considerations that underlie method selection, offering a framework for principled decision-making in learning from demonstrations.

## 核心内容
This survey provides a comparative analysis of feature-based and GAN-based approaches to learning from demonstrations, with a focus on the structure of reward functions and their implications for policy learning. Feature-based methods offer dense, interpretable rewards that excel at high-fidelity motion imitation, yet often require sophisticated representations of references and struggle with generalization in unstructured settings. GAN-based methods, in contrast, use implicit, distributional supervision that enables scalability and adaptation flexibility, but are prone to training instability and coarse reward signals. Recent advancements in both paradigms converge on the importance of structured motion representations, which enable smoother transitions, controllable synthesis, and improved task integration. We argue that the dichotomy between feature-based and GAN-based methods is increasingly nuanced: rather than one paradigm dominating the other, the choice should be guided by task-specific priorities such as fidelity, diversity, interpretability, and adaptability. This work outlines the algorithmic trade-offs and design considerations that underlie method selection, offering a framework for principled decision-making in learning from demonstrations.

## 参考
- http://arxiv.org/abs/2507.05906v2

