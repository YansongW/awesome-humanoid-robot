---
$id: ent_paper_reinforcegen_hybrid_skill_poli_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement
    Learning'
  zh: 'ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement
    Learning'
  ko: ''
summary:
  en: "arXiv:2512.16861v2 Announce Type: replace \nAbstract: Long-horizon manipulation\
    \ has been a long-standing challenge in the robotics community. We propose ReinforceGen,\
    \ a system that combines task decomposition, data generation, imitation learning,\
    \ and motion planning to form an initial solution, and improves each component\
    \ through reinforcement-learning-based fine-tuning. ReinforceGen first segments\
    \ the task into multiple localized skills, which are connected through motion\
    \ planning. The skills and motion planning targets are trained with imitation\
    \ learning on a dataset generated from 10 human demonstrations, and then fine-tuned\
    \ through online adaptation and reinforcement learning. When benchmarked on the\
    \ Robosuite dataset, ReinforceGen reaches 80% success rate on all tasks with visuomotor\
    \ controls in the highest reset range setting. Additional ablation studies show\
    \ that our fine-tuning approaches contribute to an 89% average performance increase.\
    \ Finally, ReinforceGen demonstrates significant improvement through fine-tuning\
    \ in our real-world evaluations. More results and videos are available at https://reinforcegen.github.io."
  zh: "arXiv:2512.16861v2 Announce Type: replace \nAbstract: Long-horizon manipulation\
    \ has been a long-standing challenge in the robotics community. We propose ReinforceGen,\
    \ a system that combines task decomposition, data generation, imitation learning,\
    \ and motion planning to form an initial solution, and improves each component\
    \ through reinforcement-learning-based fine-tuning. ReinforceGen first segments\
    \ the task into multiple localized skills, which are connected through motion\
    \ planning. The skills and motion planning targets are trained with imitation\
    \ learning on a dataset generated from 10 human demonstrations, and then fine-tuned\
    \ through online adaptation and reinforcement learning. When benchmarked on the\
    \ Robosuite dataset, ReinforceGen reaches 80% success rate on all tasks with visuomotor\
    \ controls in the highest reset range setting. Additional ablation studies show\
    \ that our fine-tuning approaches contribute to an 89% average performance increase.\
    \ Finally, ReinforceGen demonstrates significant improvement through fine-tuning\
    \ in our real-world evaluations. More results and videos are available at https://reinforcegen.github.io."
  ko: ''
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- reinforcegen
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-13'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement
    Learning (arXiv)'
  url: https://arxiv.org/abs/2512.16861
  date: '2026'
  accessed_at: '2026-07-13'
---

arXiv:2512.16861v2 Announce Type: replace 
Abstract: Long-horizon manipulation has been a long-standing challenge in the robotics community. We propose ReinforceGen, a system that combines task decomposition, data generation, imitation learning, and motion planning to form an initial solution, and improves each component through reinforcement-learning-based fine-tuning. ReinforceGen first segments the task into multiple localized skills, which are connected through motion planning. The skills and motion planning targets are trained with imitation learning on a dataset generated from 10 human demonstrations, and then fine-tuned through online adaptation and reinforcement learning. When benchmarked on the Robosuite dataset, ReinforceGen reaches 80% success rate on all tasks with visuomotor controls in the highest reset range setting. Additional ablation studies show that our fine-tuning approaches contribute to an 89% average performance increase. Finally, ReinforceGen demonstrates significant improvement through fine-tuning in our real-world evaluations. More results and videos are available at https://reinforcegen.github.io.
