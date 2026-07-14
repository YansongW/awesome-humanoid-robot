---
$id: ent_paper_commanding_humanoid_by_free_fo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary'
  zh: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary'
  ko: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary'
summary:
  en: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- commanding_humanoid_by_free_fo
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22963v3.
sources:
- id: src_001
  type: paper
  title: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary (arXiv)'
  url: https://arxiv.org/abs/2511.22963
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Enabling humanoid robots to follow free-form natural language commands is a critical step toward seamless human-robot interaction and general-purpose embodied AI. However, existing methods remain limited, often constrained to simple instructions or forced to sacrifice motion diversity for physical plausibility. To address this gap, we present Humanoid-LLA, a Large Language Action model that translates unconstrained natural language directly into executable whole-body motions for humanoid robots. Our approach tackles two core challenges: paired language-humanoid motion data scarcity and physical instability. First, we bridge high-level language semantics with physically-grounded control by learning a unified human-humanoid motion vocabulary. Second, we introduce a novel two-stage fine-tuning framework that begins with supervised motion Chain-of-Thought learning, followed by reinforcement learning refined with physical feedback to ensure robustness and stability. Extensive evaluation in simulation and real-world cross-embodiment experiments demonstrates that Humanoid-LLA achieves superior generalization to novel language commands and diverse motion generation while maintaining high physical fidelity.

## 核心内容
Enabling humanoid robots to follow free-form natural language commands is a critical step toward seamless human-robot interaction and general-purpose embodied AI. However, existing methods remain limited, often constrained to simple instructions or forced to sacrifice motion diversity for physical plausibility. To address this gap, we present Humanoid-LLA, a Large Language Action model that translates unconstrained natural language directly into executable whole-body motions for humanoid robots. Our approach tackles two core challenges: paired language-humanoid motion data scarcity and physical instability. First, we bridge high-level language semantics with physically-grounded control by learning a unified human-humanoid motion vocabulary. Second, we introduce a novel two-stage fine-tuning framework that begins with supervised motion Chain-of-Thought learning, followed by reinforcement learning refined with physical feedback to ensure robustness and stability. Extensive evaluation in simulation and real-world cross-embodiment experiments demonstrates that Humanoid-LLA achieves superior generalization to novel language commands and diverse motion generation while maintaining high physical fidelity.

## 参考
- http://arxiv.org/abs/2511.22963v3

