---
$id: ent_paper_skillmimic_learning_basketball_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations'
  zh: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations'
  ko: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations'
summary:
  en: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations is a 2024 work on physics-based character animation
    for humanoid robots.'
  zh: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations is a 2024 work on physics-based character animation
    for humanoid robots.'
  ko: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations is a 2024 work on physics-based character animation
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
- humanoid
- physics_based
- skillmimic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.15270v2.
sources:
- id: src_001
  type: paper
  title: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2408.15270
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Traditional reinforcement learning methods for human-object interaction (HOI) rely on labor-intensive, manually designed skill rewards that do not generalize well across different interactions. We introduce SkillMimic, a unified data-driven framework that fundamentally changes how agents learn interaction skills by eliminating the need for skill-specific rewards. Our key insight is that a unified HOI imitation reward can effectively capture the essence of diverse interaction patterns from HOI datasets. This enables SkillMimic to learn a single policy that not only masters multiple interaction skills but also facilitates skill transitions, with both diversity and generalization improving as the HOI dataset grows. For evaluation, we collect and introduce two basketball datasets containing approximately 35 minutes of diverse basketball skills. Extensive experiments show that SkillMimic successfully masters a wide range of basketball skills including stylistic variations in dribbling, layup, and shooting. Moreover, these learned skills can be effectively composed by a high-level controller to accomplish complex and long-horizon tasks such as consecutive scoring, opening new possibilities for scalable and generalizable interaction skill learning. Project page: https://ingrid789.github.io/SkillMimic/

## 核心内容
Traditional reinforcement learning methods for human-object interaction (HOI) rely on labor-intensive, manually designed skill rewards that do not generalize well across different interactions. We introduce SkillMimic, a unified data-driven framework that fundamentally changes how agents learn interaction skills by eliminating the need for skill-specific rewards. Our key insight is that a unified HOI imitation reward can effectively capture the essence of diverse interaction patterns from HOI datasets. This enables SkillMimic to learn a single policy that not only masters multiple interaction skills but also facilitates skill transitions, with both diversity and generalization improving as the HOI dataset grows. For evaluation, we collect and introduce two basketball datasets containing approximately 35 minutes of diverse basketball skills. Extensive experiments show that SkillMimic successfully masters a wide range of basketball skills including stylistic variations in dribbling, layup, and shooting. Moreover, these learned skills can be effectively composed by a high-level controller to accomplish complex and long-horizon tasks such as consecutive scoring, opening new possibilities for scalable and generalizable interaction skill learning. Project page: https://ingrid789.github.io/SkillMimic/

## 参考
- http://arxiv.org/abs/2408.15270v2

