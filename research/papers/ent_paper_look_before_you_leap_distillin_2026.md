---
$id: ent_paper_look_before_you_leap_distillin_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen
    VLA Models'
  zh: 'Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen
    VLA Models'
  ko: ''
summary:
  en: "arXiv:2607.03751v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA)\
    \ models acquire broad embodied capabilities through large-scale pretraining,\
    \ yet their generalization remains far more fragile than that of LLMs and VLMs.\
    \ The prevailing remedy, post-training via supervised fine-tuning or reinforcement\
    \ learning, improves task-specific performance but narrows the generalist capability\
    \ that makes pretraining valuable. We identify a key bottleneck: VLA failures\
    \ stem not only from action generation but also from action evaluation. A diagnostic\
    \ pass@k study confirms that frozen VLAs already contain competent behaviors in\
    \ their output distribution, with overall success rates rising from 33% at pass@1\
    \ to 92% at pass@32. Inspired by this, we propose SVA (Search, Value, and Act),\
    \ a simple framework that equips frozen VLA policies with long-term consequence\
    \ awareness. SVA first uses Monte-Carlo tree search in simulation to fully explore\
    \ the VLA's output distribution and collect diverse trajectories annotated with\
    \ empirical returns; this knowledge is then distilled into a lightweight Q-value\
    \ model that predicts the expected consequence of candidate actions; at deployment,\
    \ the frozen VLA proposes multiple candidates and the evaluator selects the one\
    \ with the highest uncertainty-regularized Q-value, requiring no simulator access.\
    \ By decoupling action proposal from consequence evaluation, SVA preserves the\
    \ generalization capacity of the VLA backbone while substantially improving task\
    \ success rates. Experiments across embodied benchmarks show that SVA consistently\
    \ improves generalization on unseen tasks and exhibits strong test-time scaling\
    \ behavior. Strikingly, SVA enables a 9B VLA to outperform a 27B VLA by 7 points\
    \ at 27% lower inference latency, suggesting that scaling test-time evaluation\
    \ is more cost-effective than scaling model size."
  zh: "arXiv:2607.03751v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA)\
    \ models acquire broad embodied capabilities through large-scale pretraining,\
    \ yet their generalization remains far more fragile than that of LLMs and VLMs.\
    \ The prevailing remedy, post-training via supervised fine-tuning or reinforcement\
    \ learning, improves task-specific performance but narrows the generalist capability\
    \ that makes pretraining valuable. We identify a key bottleneck: VLA failures\
    \ stem not only from action generation but also from action evaluation. A diagnostic\
    \ pass@k study confirms that frozen VLAs already contain competent behaviors in\
    \ their output distribution, with overall success rates rising from 33% at pass@1\
    \ to 92% at pass@32. Inspired by this, we propose SVA (Search, Value, and Act),\
    \ a simple framework that equips frozen VLA policies with long-term consequence\
    \ awareness. SVA first uses Monte-Carlo tree search in simulation to fully explore\
    \ the VLA's output distribution and collect diverse trajectories annotated with\
    \ empirical returns; this knowledge is then distilled into a lightweight Q-value\
    \ model that predicts the expected consequence of candidate actions; at deployment,\
    \ the frozen VLA proposes multiple candidates and the evaluator selects the one\
    \ with the highest uncertainty-regularized Q-value, requiring no simulator access.\
    \ By decoupling action proposal from consequence evaluation, SVA preserves the\
    \ generalization capacity of the VLA backbone while substantially improving task\
    \ success rates. Experiments across embodied benchmarks show that SVA consistently\
    \ improves generalization on unseen tasks and exhibits strong test-time scaling\
    \ behavior. Strikingly, SVA enables a 9B VLA to outperform a 27B VLA by 7 points\
    \ at 27% lower inference latency, suggesting that scaling test-time evaluation\
    \ is more cost-effective than scaling model size."
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
- look_before_you_leap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Look Before You Leap: Distilling Tree Search into Action Evaluation for
    Frozen VLA Models (arXiv)'
  url: https://arxiv.org/abs/2607.03751
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2607.03751v1 Announce Type: new 
Abstract: Vision-Language-Action (VLA) models acquire broad embodied capabilities through large-scale pretraining, yet their generalization remains far more fragile than that of LLMs and VLMs. The prevailing remedy, post-training via supervised fine-tuning or reinforcement learning, improves task-specific performance but narrows the generalist capability that makes pretraining valuable. We identify a key bottleneck: VLA failures stem not only from action generation but also from action evaluation. A diagnostic pass@k study confirms that frozen VLAs already contain competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32. Inspired by this, we propose SVA (Search, Value, and Act), a simple framework that equips frozen VLA policies with long-term consequence awareness. SVA first uses Monte-Carlo tree search in simulation to fully explore the VLA's output distribution and collect diverse trajectories annotated with empirical returns; this knowledge is then distilled into a lightweight Q-value model that predicts the expected consequence of candidate actions; at deployment, the frozen VLA proposes multiple candidates and the evaluator selects the one with the highest uncertainty-regularized Q-value, requiring no simulator access. By decoupling action proposal from consequence evaluation, SVA preserves the generalization capacity of the VLA backbone while substantially improving task success rates. Experiments across embodied benchmarks show that SVA consistently improves generalization on unseen tasks and exhibits strong test-time scaling behavior. Strikingly, SVA enables a 9B VLA to outperform a 27B VLA by 7 points at 27% lower inference latency, suggesting that scaling test-time evaluation is more cost-effective than scaling model size.
