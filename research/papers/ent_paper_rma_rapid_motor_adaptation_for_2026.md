---
$id: ent_paper_rma_rapid_motor_adaptation_for_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RMA: Rapid Motor Adaptation for Legged Robots'
  zh: 'RMA: Rapid Motor Adaptation for Legged Robots'
  ko: 'RMA: Rapid Motor Adaptation for Legged Robots'
summary:
  en: 'Successful real-world deployment of legged robots would require them to adapt in real-time to unseen scenarios like
    changing terrains, changing payloads, wear and tear. This paper presents Rapid Motor Adaptation (RMA) algorithm to solve
    this problem of real-time online adaptation in quadruped robots. RMA consists of two components: a base policy and an
    adaptation module. The combination of these components enables the robot to adapt to novel situations in fractions of
    a second. RMA is trained completely in simulation without using any domain knowledge like reference trajectories or predefined
    foot trajectory generators and is deployed on the A1 robot without any fine-tuning. We train RMA on a varied terrain generator
    using bioenergetics-inspired rewards and deploy it on a variety of diffic'
  zh: 'RMA: Rapid Motor Adaptation for Legged Robots is a paper on 仿真到真实 for humanoid robotics.'
  ko: 'RMA: Rapid Motor Adaptation for Legged Robots is a paper on 仿真到真实 for humanoid robotics.'
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
- rma
- sim_to_real
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: RMA: Rapid Motor Adaptation
    for Legged Robots.'
sources:
- id: src_001
  type: website
  title: 'RMA: Rapid Motor Adaptation for Legged Robots'
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Successful real-world deployment of legged robots would require them to adapt in real-time to unseen scenarios like changing terrains, changing payloads, wear and tear. This paper presents Rapid Motor Adaptation (RMA) algorithm to solve this problem of real-time online adaptation in quadruped robots. RMA consists of two components: a base policy and an adaptation module. The combination of these components enables the robot to adapt to novel situations in fractions of a second. RMA is trained completely in simulation without using any domain knowledge like reference trajectories or predefined foot trajectory generators and is deployed on the A1 robot without any fine-tuning. We train RMA on a varied terrain generator using bioenergetics-inspired rewards and deploy it on a variety of difficult terrains including rocky, slippery, deformable surfaces in environments with grass, long vegetation, concrete, pebbles, stairs, sand, etc. RMA shows state-of-the-art performance across diverse real-world as well as simulation experiments. Video results at https://ashish-kmr.github.io/rma-legged-robots/

## 核心内容
Successful real-world deployment of legged robots would require them to adapt in real-time to unseen scenarios like changing terrains, changing payloads, wear and tear. This paper presents Rapid Motor Adaptation (RMA) algorithm to solve this problem of real-time online adaptation in quadruped robots. RMA consists of two components: a base policy and an adaptation module. The combination of these components enables the robot to adapt to novel situations in fractions of a second. RMA is trained completely in simulation without using any domain knowledge like reference trajectories or predefined foot trajectory generators and is deployed on the A1 robot without any fine-tuning. We train RMA on a varied terrain generator using bioenergetics-inspired rewards and deploy it on a variety of difficult terrains including rocky, slippery, deformable surfaces in environments with grass, long vegetation, concrete, pebbles, stairs, sand, etc. RMA shows state-of-the-art performance across diverse real-world as well as simulation experiments. Video results at https://ashish-kmr.github.io/rma-legged-robots/

## 参考
- Semantic Scholar search: RMA: Rapid Motor Adaptation for Legged Robots

