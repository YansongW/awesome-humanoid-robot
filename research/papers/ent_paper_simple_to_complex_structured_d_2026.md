---
$id: ent_paper_simple_to_complex_structured_d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning
  zh: Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning
  ko: Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning
summary:
  en: 'arXiv:2607.04591v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have demonstrated strong capabilities
    in robotic manipulation by integrating visual perception, language understanding, and robot action generation. Existing
    research has primarily focused on improving model architectures, training strategies, and dataset scale, while little
    attention has been paid to how demonstrations are collected and organized. We identify demonstration organization as a
    fundamental yet overlooked aspect of imitation learning, as it directly affects policy learning efficiency, training stability,
    and policy generalization. To address this gap, we propose a simple-to-complex structured demonstration collection strategy
    for VLA learning using a dual-arm robotic platform. Our approach systematically organizes data through three general principles:
    (i) decomposing complex manipulation tasks into progressively learnable sub-skills, (ii) standardizing the interaction
    environment to reduce unnecessary variability, and (iii) organizing demonstrations according to progressively increasing
    task complexity. This structured design enables VLA models to first acquire fundamental manipulation skills before learning
    increasingly complex task compositions, facilitating more effective learning of long-horizon manipulation tasks. We evaluate
    the proposed strategy on two representative robotic manipulation tasks: block grasping and sorting, and towel folding.
    Experimental results show consistent improvements in task success rate and training stability compared with the baseline
    method of directly collecting end-to-end complete task trajectories. These findings highlight demonstration organization
    as a previously underexplored but important factor in VLA learning and provide practical insights into efficient skill
    acquisition, scalable dataset construction, and long-horizon robotic manipulation.'
  zh: 'arXiv:2607.04591v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have demonstrated strong capabilities
    in robotic manipulation by integrating visual perception, language understanding, and robot action generation. Existing
    research has primarily focused on improving model architectures, training strategies, and dataset scale, while little
    attention has been paid to how demonstrations are collected and organized. We identify demonstration organization as a
    fundamental yet overlooked aspect of imitation learning, as it directly affects policy learning efficiency, training stability,
    and policy generalization. To address this gap, we propose a simple-to-complex structured demonstration collection strategy
    for VLA learning using a dual-arm robotic platform. Our approach systematically organizes data through three general principles:
    (i) decomposing complex manipulation tasks into progressively learnable sub-skills, (ii) standardizing the interaction
    environment to reduce unnecessary variability, and (iii) organizing demonstrations according to progressively increasing
    task complexity. This structured design enables VLA models to first acquire fundamental manipulation skills before learning
    increasingly complex task compositions, facilitating more effective learning of long-horizon manipulation tasks. We evaluate
    the proposed strategy on two representative robotic manipulation tasks: block grasping and sorting, and towel folding.
    Experimental results show consistent improvements in task success rate and training stability compared with the baseline
    method of directly collecting end-to-end complete task trajectories. These findings highlight demonstration organization
    as a previously underexplored but important factor in VLA learning and provide practical insights into efficient skill
    acquisition, scalable dataset construction, and long-horizon robotic manipulation.'
  ko: 'arXiv:2607.04591v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have demonstrated strong capabilities
    in robotic manipulation by integrating visual perception, language understanding, and robot action generation. Existing
    research has primarily focused on improving model architectures, training strategies, and dataset scale, while little
    attention has been paid to how demonstrations are collected and organized. We identify demonstration organization as a
    fundamental yet overlooked aspect of imitation learning, as it directly affects policy learning efficiency, training stability,
    and policy generalization. To address this gap, we propose a simple-to-complex structured demonstration collection strategy
    for VLA learning using a dual-arm robotic platform. Our approach systematically organizes data through three general principles:
    (i) decomposing complex manipulation tasks into progressively learnable sub-skills, (ii) standardizing the interaction
    environment to reduce unnecessary variability, and (iii) organizing demonstrations according to progressively increasing
    task complexity. This structured design enables VLA models to first acquire fundamental manipulation skills before learning
    increasingly complex task compositions, facilitating more effective learning of long-horizon manipulation tasks. We evaluate
    the proposed strategy on two representative robotic manipulation tasks: block grasping and sorting, and towel folding.
    Experimental results show consistent improvements in task success rate and training stability compared with the baseline
    method of directly collecting end-to-end complete task trajectories. These findings highlight demonstration organization
    as a previously underexplored but important factor in VLA learning and provide practical insights into efficient skill
    acquisition, scalable dataset construction, and long-horizon robotic manipulation.'
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
- simple_to_complex_structured_d
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04591v1.
sources:
- id: src_001
  type: paper
  title: Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning (arXiv)
  url: https://arxiv.org/abs/2607.04591
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Vision-Language-Action (VLA) models have demonstrated strong capabilities in robotic manipulation by integrating visual perception, language understanding, and robot action generation. Existing research has primarily focused on improving model architectures, training strategies, and dataset scale, while little attention has been paid to how demonstrations are collected and organized. We identify demonstration organization as a fundamental yet overlooked aspect of imitation learning, as it directly affects policy learning efficiency, training stability, and policy generalization. To address this gap, we propose a simple-to-complex structured demonstration collection strategy for VLA learning using a dual-arm robotic platform. Our approach systematically organizes data through three general principles: (i) decomposing complex manipulation tasks into progressively learnable sub-skills, (ii) standardizing the interaction environment to reduce unnecessary variability, and (iii) organizing demonstrations according to progressively increasing task complexity. This structured design enables VLA models to first acquire fundamental manipulation skills before learning increasingly complex task compositions, facilitating more effective learning of long-horizon manipulation tasks. We evaluate the proposed strategy on two representative robotic manipulation tasks: block grasping and sorting, and towel folding. Experimental results show consistent improvements in task success rate and training stability compared with the baseline method of directly collecting end-to-end complete task trajectories. These findings highlight demonstration organization as a previously underexplored but important factor in VLA learning and provide practical insights into efficient skill acquisition, scalable dataset construction, and long-horizon robotic manipulation.

## 核心内容
Vision-Language-Action (VLA) models have demonstrated strong capabilities in robotic manipulation by integrating visual perception, language understanding, and robot action generation. Existing research has primarily focused on improving model architectures, training strategies, and dataset scale, while little attention has been paid to how demonstrations are collected and organized. We identify demonstration organization as a fundamental yet overlooked aspect of imitation learning, as it directly affects policy learning efficiency, training stability, and policy generalization. To address this gap, we propose a simple-to-complex structured demonstration collection strategy for VLA learning using a dual-arm robotic platform. Our approach systematically organizes data through three general principles: (i) decomposing complex manipulation tasks into progressively learnable sub-skills, (ii) standardizing the interaction environment to reduce unnecessary variability, and (iii) organizing demonstrations according to progressively increasing task complexity. This structured design enables VLA models to first acquire fundamental manipulation skills before learning increasingly complex task compositions, facilitating more effective learning of long-horizon manipulation tasks. We evaluate the proposed strategy on two representative robotic manipulation tasks: block grasping and sorting, and towel folding. Experimental results show consistent improvements in task success rate and training stability compared with the baseline method of directly collecting end-to-end complete task trajectories. These findings highlight demonstration organization as a previously underexplored but important factor in VLA learning and provide practical insights into efficient skill acquisition, scalable dataset construction, and long-horizon robotic manipulation.

## 参考
- http://arxiv.org/abs/2607.04591v1

