---
$id: ent_paper_stage_transition_dense_reward_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Stage-Transition Dense Reward Modeling for Reinforcement Learning
  zh: Stage-Transition Dense Reward Modeling for Reinforcement Learning
  ko: ''
summary:
  en: "arXiv:2606.31377v1 Announce Type: new \nAbstract: Reinforcement learning for\
    \ long-horizon robotic manipulation is often limited by sparse and delayed rewards,\
    \ while manually designing dense shaping signals is costly and brittle to changes\
    \ in environments and object configurations. This work proposes Stage-Transition\
    \ Dense Reward (STDR), a visual reward-learning framework that converts unstructured\
    \ expert videos into logically grounded dense rewards for training RL agents from\
    \ scratch. STDR leverages semantic understanding to infer a task's stage structure\
    \ from demonstrations, and delivers two complementary learning signals during\
    \ online training: (i) stage-transition feedback that provides goal-directed reward,\
    \ and (ii) within-stage progress feedback that supplies fine-grained guidance\
    \ toward completing each stage. Furthermore, an out-of-distribution (OOD) detection\
    \ mechanism and a grasping regulation module are integrated to enhance robustness\
    \ and prevent reward hacking. Experiments on 14 manipulation tasks across MetaWorld,\
    \ ManiSkill, and Franka Kitchen show that STDR consistently improves sample efficiency\
    \ and success rates over multiple baselines, and matches or surpasses handcrafted\
    \ dense rewards on several challenging tasks. Real-robot evaluations further indicate\
    \ that STDR assigns stable, progress-aligned rewards on successful executions\
    \ while producing appropriately low rewards for failures, suggesting robustness\
    \ to visual noise and better-calibrated reward assignment across settings."
  zh: "arXiv:2606.31377v1 Announce Type: new \nAbstract: Reinforcement learning for\
    \ long-horizon robotic manipulation is often limited by sparse and delayed rewards,\
    \ while manually designing dense shaping signals is costly and brittle to changes\
    \ in environments and object configurations. This work proposes Stage-Transition\
    \ Dense Reward (STDR), a visual reward-learning framework that converts unstructured\
    \ expert videos into logically grounded dense rewards for training RL agents from\
    \ scratch. STDR leverages semantic understanding to infer a task's stage structure\
    \ from demonstrations, and delivers two complementary learning signals during\
    \ online training: (i) stage-transition feedback that provides goal-directed reward,\
    \ and (ii) within-stage progress feedback that supplies fine-grained guidance\
    \ toward completing each stage. Furthermore, an out-of-distribution (OOD) detection\
    \ mechanism and a grasping regulation module are integrated to enhance robustness\
    \ and prevent reward hacking. Experiments on 14 manipulation tasks across MetaWorld,\
    \ ManiSkill, and Franka Kitchen show that STDR consistently improves sample efficiency\
    \ and success rates over multiple baselines, and matches or surpasses handcrafted\
    \ dense rewards on several challenging tasks. Real-robot evaluations further indicate\
    \ that STDR assigns stable, progress-aligned rewards on successful executions\
    \ while producing appropriately low rewards for failures, suggesting robustness\
    \ to visual noise and better-calibrated reward assignment across settings."
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
- stage_transition_dense_reward
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from arXiv cs.RO RSS feed.
sources:
- id: src_001
  type: paper
  title: Stage-Transition Dense Reward Modeling for Reinforcement Learning
  url: https://arxiv.org/abs/2606.31377
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2606.31377v1 Announce Type: new 
Abstract: Reinforcement learning for long-horizon robotic manipulation is often limited by sparse and delayed rewards, while manually designing dense shaping signals is costly and brittle to changes in environments and object configurations. This work proposes Stage-Transition Dense Reward (STDR), a visual reward-learning framework that converts unstructured expert videos into logically grounded dense rewards for training RL agents from scratch. STDR leverages semantic understanding to infer a task's stage structure from demonstrations, and delivers two complementary learning signals during online training: (i) stage-transition feedback that provides goal-directed reward, and (ii) within-stage progress feedback that supplies fine-grained guidance toward completing each stage. Furthermore, an out-of-distribution (OOD) detection mechanism and a grasping regulation module are integrated to enhance robustness and prevent reward hacking. Experiments on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves sample efficiency and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several challenging tasks. Real-robot evaluations further indicate that STDR assigns stable, progress-aligned rewards on successful executions while producing appropriately low rewards for failures, suggesting robustness to visual noise and better-calibrated reward assignment across settings.
