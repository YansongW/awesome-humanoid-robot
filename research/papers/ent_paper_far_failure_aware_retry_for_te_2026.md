---
$id: ent_paper_far_failure_aware_retry_for_te_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement'
  zh: 'FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement'
  ko: ''
summary:
  en: "arXiv:2607.01111v1 Announce Type: new \nAbstract: Robot policies inevitably\
    \ encounter failures when deployed in real environments. Naive retries often repeat\
    \ the same mistakes, while many existing recovery methods rely on human intervention.\
    \ In this paper, we propose Failure-Aware Retry (FAR), a framework that enables\
    \ robots to learn from previous failures at test time, adapt their behavior accordingly,\
    \ and eventually complete the task autonomously. FAR combines Failure-Contrastive\
    \ Preference Adaptation, which constructs preference learning data from failures\
    \ to steer the policy away from previously unsuccessful behaviors, with lightweight\
    \ action perturbations during retries to encourage local exploration. We further\
    \ incorporate successful recovery trajectories into a training loop for continual\
    \ policy improvement. Experiments in both simulation and real-world manipulation\
    \ tasks show that FAR substantially improves success rates and robustness, with\
    \ average gains of 17.6% over the standard diffusion policy in simulation and\
    \ 11.7% in the real world. In addition, FAR significantly improves data efficiency\
    \ under both reset and timestep budgets during continual policy improvement by\
    \ exploiting informative failure cases."
  zh: "arXiv:2607.01111v1 Announce Type: new \nAbstract: Robot policies inevitably\
    \ encounter failures when deployed in real environments. Naive retries often repeat\
    \ the same mistakes, while many existing recovery methods rely on human intervention.\
    \ In this paper, we propose Failure-Aware Retry (FAR), a framework that enables\
    \ robots to learn from previous failures at test time, adapt their behavior accordingly,\
    \ and eventually complete the task autonomously. FAR combines Failure-Contrastive\
    \ Preference Adaptation, which constructs preference learning data from failures\
    \ to steer the policy away from previously unsuccessful behaviors, with lightweight\
    \ action perturbations during retries to encourage local exploration. We further\
    \ incorporate successful recovery trajectories into a training loop for continual\
    \ policy improvement. Experiments in both simulation and real-world manipulation\
    \ tasks show that FAR substantially improves success rates and robustness, with\
    \ average gains of 17.6% over the standard diffusion policy in simulation and\
    \ 11.7% in the real world. In addition, FAR significantly improves data efficiency\
    \ under both reset and timestep budgets during continual policy improvement by\
    \ exploiting informative failure cases."
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
- far
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-03'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement
    (arXiv)'
  url: https://arxiv.org/abs/2607.01111
  date: '2026'
  accessed_at: '2026-07-03'
---

arXiv:2607.01111v1 Announce Type: new 
Abstract: Robot policies inevitably encounter failures when deployed in real environments. Naive retries often repeat the same mistakes, while many existing recovery methods rely on human intervention. In this paper, we propose Failure-Aware Retry (FAR), a framework that enables robots to learn from previous failures at test time, adapt their behavior accordingly, and eventually complete the task autonomously. FAR combines Failure-Contrastive Preference Adaptation, which constructs preference learning data from failures to steer the policy away from previously unsuccessful behaviors, with lightweight action perturbations during retries to encourage local exploration. We further incorporate successful recovery trajectories into a training loop for continual policy improvement. Experiments in both simulation and real-world manipulation tasks show that FAR substantially improves success rates and robustness, with average gains of 17.6% over the standard diffusion policy in simulation and 11.7% in the real world. In addition, FAR significantly improves data efficiency under both reset and timestep budgets during continual policy improvement by exploiting informative failure cases.
