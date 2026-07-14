---
$id: ent_paper_toward_humanoid_brain_body_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery'
  zh: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery'
  ko: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery'
summary:
  en: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery is a 2025 work
    on hardware design for humanoid robots.'
  zh: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery is a 2025 work
    on hardware design for humanoid robots.'
  ko: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery is a 2025 work
    on hardware design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- toward_humanoid_brain_body_co
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.22336v2.
sources:
- id: src_001
  type: paper
  title: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery (arXiv)'
  url: https://arxiv.org/abs/2510.22336
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots represent a central frontier in embodied intelligence, as their anthropomorphic form enables natural deployment in humans' workspace. Brain-body co-design for humanoids presents a promising approach to realizing this potential by jointly optimizing control policies and physical morphology. Within this context, fall recovery emerges as a critical capability. It not only enhances safety and resilience but also integrates naturally with locomotion systems, thereby advancing the autonomy of humanoids. In this paper, we propose RoboCraft, a scalable humanoid co-design framework for fall recovery that iteratively improves performance through the coupled updates of control policy and morphology. A shared policy pretrained across multiple designs is progressively finetuned on high-performing morphologies, enabling efficient adaptation without retraining from scratch. Concurrently, morphology search is guided by human-inspired priors and optimization algorithms, supported by a priority buffer that balances reevaluation of promising candidates with the exploration of novel designs. Experiments show that RoboCraft achieves an average performance gain of 44.55% on seven public humanoid robots, with morphology optimization drives at least 40% of improvements in co-designing four humanoid robots, underscoring the critical role of humanoid co-design.

## 核心内容
Humanoid robots represent a central frontier in embodied intelligence, as their anthropomorphic form enables natural deployment in humans' workspace. Brain-body co-design for humanoids presents a promising approach to realizing this potential by jointly optimizing control policies and physical morphology. Within this context, fall recovery emerges as a critical capability. It not only enhances safety and resilience but also integrates naturally with locomotion systems, thereby advancing the autonomy of humanoids. In this paper, we propose RoboCraft, a scalable humanoid co-design framework for fall recovery that iteratively improves performance through the coupled updates of control policy and morphology. A shared policy pretrained across multiple designs is progressively finetuned on high-performing morphologies, enabling efficient adaptation without retraining from scratch. Concurrently, morphology search is guided by human-inspired priors and optimization algorithms, supported by a priority buffer that balances reevaluation of promising candidates with the exploration of novel designs. Experiments show that RoboCraft achieves an average performance gain of 44.55% on seven public humanoid robots, with morphology optimization drives at least 40% of improvements in co-designing four humanoid robots, underscoring the critical role of humanoid co-design.

## 参考
- http://arxiv.org/abs/2510.22336v2

