---
$id: ent_paper_metaworld_skill_transfer_and_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions'
  zh: 语言语义、技能选择和物理控制要分层
  ko: 'MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions'
summary:
  en: 'MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions is a
    knowledge node related to paper in the humanoid robot value chain.'
  zh: 'Humanoid robot loco-manipulation remains constrained by the semantic-physical gap. Current methods face three limitations:
    Low sample efficiency in reinforcement learning, poor generalization in imitation learning, and physical inconsistency
    in VLMs. We propose MetaWorld, a hierarchical world model that integrates semantic planning and physical control via expert
    policy transfer. The framework decouples tasks into a VLM-driven semantic layer and a latent dynamics model operating
    in a compact state space. Our dynamic expert selection and motion prior fusion mechanism leverages a pre-trained multi-expert
    policy library as transferable knowledge, enabling efficient online adaptation via a two-stage framework. VLMs serve as
    semantic interfaces, mapping instructions to executable skills and byp'
  ko: 'MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions is a
    knowledge node related to paper in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- task_interface
- visual_closed_loop
- vla
- whole_body_control
- world_model
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.17507v1.
sources:
- id: src_001
  type: paper
  title: 'MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions (arXiv)'
  url: https://arxiv.org/abs/2601.17507
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 语言语义、技能选择和物理控制要分层 project page
  url: https://arxiv.org/abs/2601.17507
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Humanoid robot loco-manipulation remains constrained by the semantic-physical gap. Current methods face three limitations: Low sample efficiency in reinforcement learning, poor generalization in imitation learning, and physical inconsistency in VLMs. We propose MetaWorld, a hierarchical world model that integrates semantic planning and physical control via expert policy transfer. The framework decouples tasks into a VLM-driven semantic layer and a latent dynamics model operating in a compact state space. Our dynamic expert selection and motion prior fusion mechanism leverages a pre-trained multi-expert policy library as transferable knowledge, enabling efficient online adaptation via a two-stage framework. VLMs serve as semantic interfaces, mapping instructions to executable skills and bypassing symbol grounding. Experiments on Humanoid-Bench show MetaWorld outperforms world model-based RL in task completion and motion coherence. Our code will be found at https://anonymous.4open.science/r/metaworld-2BF4/

## 核心内容
Humanoid robot loco-manipulation remains constrained by the semantic-physical gap. Current methods face three limitations: Low sample efficiency in reinforcement learning, poor generalization in imitation learning, and physical inconsistency in VLMs. We propose MetaWorld, a hierarchical world model that integrates semantic planning and physical control via expert policy transfer. The framework decouples tasks into a VLM-driven semantic layer and a latent dynamics model operating in a compact state space. Our dynamic expert selection and motion prior fusion mechanism leverages a pre-trained multi-expert policy library as transferable knowledge, enabling efficient online adaptation via a two-stage framework. VLMs serve as semantic interfaces, mapping instructions to executable skills and bypassing symbol grounding. Experiments on Humanoid-Bench show MetaWorld outperforms world model-based RL in task completion and motion coherence. Our code will be found at https://anonymous.4open.science/r/metaworld-2BF4/

## 参考
- http://arxiv.org/abs/2601.17507v1

