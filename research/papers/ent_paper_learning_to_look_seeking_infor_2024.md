---
$id: ent_paper_learning_to_look_seeking_infor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization'
  zh: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization'
  ko: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization'
summary:
  en: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization is a 2024 work on manipulation for
    humanoid robots.'
  zh: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization is a 2024 work on manipulation for
    humanoid robots.'
  ko: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization is a 2024 work on manipulation for
    humanoid robots.'
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
- learning_to_look
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.18964v1.
sources:
- id: src_001
  type: paper
  title: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization (arXiv)'
  url: https://arxiv.org/abs/2410.18964
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Learning to Look: Seeking Information for Decision Making via Policy Factorization project page'
  url: https://robin-lab.cs.utexas.edu/learning2look/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Many robot manipulation tasks require active or interactive exploration behavior in order to be performed successfully. Such tasks are ubiquitous in embodied domains, where agents must actively search for the information necessary for each stage of a task, e.g., moving the head of the robot to find information relevant to manipulation, or in multi-robot domains, where one scout robot may search for the information that another robot needs to make informed decisions. We identify these tasks with a new type of problem, factorized Contextual Markov Decision Processes, and propose DISaM, a dual-policy solution composed of an information-seeking policy that explores the environment to find the relevant contextual information and an information-receiving policy that exploits the context to achieve the manipulation goal. This factorization allows us to train both policies separately, using the information-receiving one to provide reward to train the information-seeking policy. At test time, the dual agent balances exploration and exploitation based on the uncertainty the manipulation policy has on what the next best action is. We demonstrate the capabilities of our dual policy solution in five manipulation tasks that require information-seeking behaviors, both in simulation and in the real-world, where DISaM significantly outperforms existing methods. More information at https://robin-lab.cs.utexas.edu/learning2look/.

## 核心内容
Many robot manipulation tasks require active or interactive exploration behavior in order to be performed successfully. Such tasks are ubiquitous in embodied domains, where agents must actively search for the information necessary for each stage of a task, e.g., moving the head of the robot to find information relevant to manipulation, or in multi-robot domains, where one scout robot may search for the information that another robot needs to make informed decisions. We identify these tasks with a new type of problem, factorized Contextual Markov Decision Processes, and propose DISaM, a dual-policy solution composed of an information-seeking policy that explores the environment to find the relevant contextual information and an information-receiving policy that exploits the context to achieve the manipulation goal. This factorization allows us to train both policies separately, using the information-receiving one to provide reward to train the information-seeking policy. At test time, the dual agent balances exploration and exploitation based on the uncertainty the manipulation policy has on what the next best action is. We demonstrate the capabilities of our dual policy solution in five manipulation tasks that require information-seeking behaviors, both in simulation and in the real-world, where DISaM significantly outperforms existing methods. More information at https://robin-lab.cs.utexas.edu/learning2look/.

## 参考
- http://arxiv.org/abs/2410.18964v1

