---
$id: ent_paper_collaboration_open_x_embodiment_robotic_lear_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'
  zh: RT-X
  ko: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'
summary:
  en: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models (RT-X), is a 2023 large vision-language-action model for
    robotic manipulation, introduced by Open X-Embodiment Collaboration, and published at ICRA 2023.'
  zh: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models (RT-X), is a 2023 large vision-language-action model for
    robotic manipulation, introduced by Open X-Embodiment Collaboration, and published at ICRA 2023.'
  ko: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models (RT-X), is a 2023 large vision-language-action model for
    robotic manipulation, introduced by Open X-Embodiment Collaboration, and published at ICRA 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- rt_x
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.08864v9.
sources:
- id: src_001
  type: website
  title: RT-X source
  url: https://doi.org/10.1109/ICRA57147.2024.10611477
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Large, high-capacity models trained on diverse datasets have shown remarkable successes on efficiently tackling downstream applications. In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting point for many applications. Can such a consolidation happen in robotics? Conventionally, robotic learning methods train a separate model for every application, every robot, and even every environment. Can we instead train generalist X-robot policy that can be adapted efficiently to new robots, tasks, and environments? In this paper, we provide datasets in standardized data formats and models to make it possible to explore this possibility in the context of robotic manipulation, alongside experimental results that provide an example of effective X-robot policies. We assemble a dataset from 22 different robots collected through a collaboration between 21 institutions, demonstrating 527 skills (160266 tasks). We show that a high-capacity model trained on this data, which we call RT-X, exhibits positive transfer and improves the capabilities of multiple robots by leveraging experience from other platforms. More details can be found on the project website https://robotics-transformer-x.github.io.

## 核心内容
Large, high-capacity models trained on diverse datasets have shown remarkable successes on efficiently tackling downstream applications. In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting point for many applications. Can such a consolidation happen in robotics? Conventionally, robotic learning methods train a separate model for every application, every robot, and even every environment. Can we instead train generalist X-robot policy that can be adapted efficiently to new robots, tasks, and environments? In this paper, we provide datasets in standardized data formats and models to make it possible to explore this possibility in the context of robotic manipulation, alongside experimental results that provide an example of effective X-robot policies. We assemble a dataset from 22 different robots collected through a collaboration between 21 institutions, demonstrating 527 skills (160266 tasks). We show that a high-capacity model trained on this data, which we call RT-X, exhibits positive transfer and improves the capabilities of multiple robots by leveraging experience from other platforms. More details can be found on the project website https://robotics-transformer-x.github.io.

## 参考
- http://arxiv.org/abs/2310.08864v9

