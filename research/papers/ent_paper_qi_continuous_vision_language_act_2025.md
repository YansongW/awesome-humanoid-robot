---
$id: ent_paper_qi_continuous_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning
  zh: CCoL
  ko: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning
summary:
  en: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning (CCoL), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Nankai University, The Hong Kong Polytechnic
    University, The Education University of Hong Kong, City University of Hong Kong.
  zh: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning (CCoL), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Nankai University, The Hong Kong Polytechnic
    University, The Education University of Hong Kong, City University of Hong Kong.
  ko: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning (CCoL), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Nankai University, The Hong Kong Polytechnic
    University, The Education University of Hong Kong, City University of Hong Kong.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ccol
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14396v5.
sources:
- id: src_001
  type: paper
  title: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning (arXiv)
  url: https://arxiv.org/abs/2511.14396
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CCoL source
  url: https://doi.org/10.48550/arXiv.2511.14396
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Language-conditioned manipulation facilitates human-robot interaction via behavioral cloning (BC), which learns control policies from human demonstrations and serves as a cornerstone of embodied AI. Overcoming compounding errors in sequential action decisions remains a central challenge to improving BC performance. Existing approaches mitigate compounding errors through data augmentation, expressive representation, or temporal abstraction. However, they suffer from physical discontinuities and semantic-physical misalignment, leading to inaccurate action cloning and intermittent execution. In this paper, we present Continuous vision-language-action Co-Learning with Semantic-Physical Alignment (CCoL), a novel BC framework that ensures temporally consistent execution and fine-grained semantic grounding. It generates robust and smooth action execution trajectories through continuous co-learning across vision, language, and proprioceptive inputs (e.g., robot internal states). Meanwhile, we anchor language semantics to visuomotor representations by a bidirectional cross-attention to learn contextual information for action generation, successfully overcoming the problem of semantic-physical misalignment. Extensive experiments show that CCoL achieves an average 8.0% relative improvement across three simulation suites, with up to 19.2% relative gain in human-demonstrated bimanual insertion tasks. Real-world tests on a 7-DoF robot further confirm CCoL's generalization under unseen and noisy object states.

## 核心内容
Language-conditioned manipulation facilitates human-robot interaction via behavioral cloning (BC), which learns control policies from human demonstrations and serves as a cornerstone of embodied AI. Overcoming compounding errors in sequential action decisions remains a central challenge to improving BC performance. Existing approaches mitigate compounding errors through data augmentation, expressive representation, or temporal abstraction. However, they suffer from physical discontinuities and semantic-physical misalignment, leading to inaccurate action cloning and intermittent execution. In this paper, we present Continuous vision-language-action Co-Learning with Semantic-Physical Alignment (CCoL), a novel BC framework that ensures temporally consistent execution and fine-grained semantic grounding. It generates robust and smooth action execution trajectories through continuous co-learning across vision, language, and proprioceptive inputs (e.g., robot internal states). Meanwhile, we anchor language semantics to visuomotor representations by a bidirectional cross-attention to learn contextual information for action generation, successfully overcoming the problem of semantic-physical misalignment. Extensive experiments show that CCoL achieves an average 8.0% relative improvement across three simulation suites, with up to 19.2% relative gain in human-demonstrated bimanual insertion tasks. Real-world tests on a 7-DoF robot further confirm CCoL's generalization under unseen and noisy object states.

## 参考
- http://arxiv.org/abs/2511.14396v5

