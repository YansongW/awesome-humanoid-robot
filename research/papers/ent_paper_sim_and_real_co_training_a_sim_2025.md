---
$id: ent_paper_sim_and_real_co_training_a_sim_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation'
  zh: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation'
  ko: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation'
summary:
  en: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation is a 2025 work on manipulation for
    humanoid robots.'
  zh: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation is a 2025 work on manipulation for
    humanoid robots.'
  ko: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation is a 2025 work on manipulation for
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
- manipulation
- sim_and_real_co_training
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.24361v2.
sources:
- id: src_001
  type: paper
  title: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2503.24361
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation project page'
  url: https://co-training.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Large real-world robot datasets hold great potential to train generalist robot models, but scaling real-world human data collection is time-consuming and resource-intensive. Simulation has great potential in supplementing large-scale data, especially with recent advances in generative AI and automated data generation tools that enable scalable creation of robot behavior datasets. However, training a policy solely in simulation and transferring it to the real world often demands substantial human effort to bridge the reality gap. A compelling alternative is to co-train the policy on a mixture of simulation and real-world datasets. Preliminary studies have recently shown this strategy to substantially improve the performance of a policy over one trained on a limited amount of real-world data. Nonetheless, the community lacks a systematic understanding of sim-and-real co-training and what it takes to reap the benefits of simulation data for real-robot learning. This work presents a simple yet effective recipe for utilizing simulation data to solve vision-based robotic manipulation tasks. We derive this recipe from comprehensive experiments that validate the co-training strategy on various simulation and real-world datasets. Using two domains--a robot arm and a humanoid--across diverse tasks, we demonstrate that simulation data can enhance real-world task performance by an average of 38%, even with notable differences between the simulation and real-world data. Videos and additional results can be found at https://co-training.github.io/

## 核心内容
Large real-world robot datasets hold great potential to train generalist robot models, but scaling real-world human data collection is time-consuming and resource-intensive. Simulation has great potential in supplementing large-scale data, especially with recent advances in generative AI and automated data generation tools that enable scalable creation of robot behavior datasets. However, training a policy solely in simulation and transferring it to the real world often demands substantial human effort to bridge the reality gap. A compelling alternative is to co-train the policy on a mixture of simulation and real-world datasets. Preliminary studies have recently shown this strategy to substantially improve the performance of a policy over one trained on a limited amount of real-world data. Nonetheless, the community lacks a systematic understanding of sim-and-real co-training and what it takes to reap the benefits of simulation data for real-robot learning. This work presents a simple yet effective recipe for utilizing simulation data to solve vision-based robotic manipulation tasks. We derive this recipe from comprehensive experiments that validate the co-training strategy on various simulation and real-world datasets. Using two domains--a robot arm and a humanoid--across diverse tasks, we demonstrate that simulation data can enhance real-world task performance by an average of 38%, even with notable differences between the simulation and real-world data. Videos and additional results can be found at https://co-training.github.io/

## 参考
- http://arxiv.org/abs/2503.24361v2

