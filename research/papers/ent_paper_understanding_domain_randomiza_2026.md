---
$id: ent_paper_understanding_domain_randomiza_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Understanding Domain Randomization for Sim-to-real Transfer
  zh: Understanding Domain Randomization for Sim-to-real Transfer
  ko: Understanding Domain Randomization for Sim-to-real Transfer
summary:
  en: Reinforcement learning encounters many challenges when applied directly in the real world. Sim-to-real transfer is widely
    used to transfer the knowledge learned from simulation to the real world. Domain randomization -- one of the most popular
    algorithms for sim-to-real transfer -- has been demonstrated to be effective in various tasks in robotics and autonomous
    driving. Despite its empirical successes, theoretical understanding on why this simple algorithm works is limited. In
    this paper, we propose a theoretical framework for sim-to-real transfers, in which the simulator is modeled as a set of
    MDPs with tunable parameters (corresponding to unknown physical parameters such as friction). We provide sharp bounds
    on the sim-to-real gap -- the difference between the value of policy returned b
  zh: Understanding Domain Randomization for Sim-to-real Transfer is a paper on 仿真到现实 for humanoid robotics.
  ko: Understanding Domain Randomization for Sim-to-real Transfer is a paper on 仿真到现实 for humanoid robotics.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- foundation
- humanoid
- reinforcement_learning
- understanding_domain_randomiza
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Understanding Domain Randomization
    for Sim-to-real Transfer.'
sources:
- id: src_001
  type: website
  title: Understanding Domain Randomization for Sim-to-real Transfer
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning encounters many challenges when applied directly in the real world. Sim-to-real transfer is widely used to transfer the knowledge learned from simulation to the real world. Domain randomization -- one of the most popular algorithms for sim-to-real transfer -- has been demonstrated to be effective in various tasks in robotics and autonomous driving. Despite its empirical successes, theoretical understanding on why this simple algorithm works is limited. In this paper, we propose a theoretical framework for sim-to-real transfers, in which the simulator is modeled as a set of MDPs with tunable parameters (corresponding to unknown physical parameters such as friction). We provide sharp bounds on the sim-to-real gap -- the difference between the value of policy returned by domain randomization and the value of an optimal policy for the real world. We prove that sim-to-real transfer can succeed under mild conditions without any real-world training samples. Our theory also highlights the importance of using memory (i.e., history-dependent policies) in domain randomization. Our proof is based on novel techniques that reduce the problem of bounding the sim-to-real gap to the problem of designing efficient learning algorithms for infinite-horizon MDPs, which we believe are of independent interest.

## 核心内容
Reinforcement learning encounters many challenges when applied directly in the real world. Sim-to-real transfer is widely used to transfer the knowledge learned from simulation to the real world. Domain randomization -- one of the most popular algorithms for sim-to-real transfer -- has been demonstrated to be effective in various tasks in robotics and autonomous driving. Despite its empirical successes, theoretical understanding on why this simple algorithm works is limited. In this paper, we propose a theoretical framework for sim-to-real transfers, in which the simulator is modeled as a set of MDPs with tunable parameters (corresponding to unknown physical parameters such as friction). We provide sharp bounds on the sim-to-real gap -- the difference between the value of policy returned by domain randomization and the value of an optimal policy for the real world. We prove that sim-to-real transfer can succeed under mild conditions without any real-world training samples. Our theory also highlights the importance of using memory (i.e., history-dependent policies) in domain randomization. Our proof is based on novel techniques that reduce the problem of bounding the sim-to-real gap to the problem of designing efficient learning algorithms for infinite-horizon MDPs, which we believe are of independent interest.

## 参考
- Semantic Scholar search: Understanding Domain Randomization for Sim-to-real Transfer

