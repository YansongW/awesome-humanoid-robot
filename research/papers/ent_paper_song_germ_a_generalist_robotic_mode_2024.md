---
$id: ent_paper_song_germ_a_generalist_robotic_mode_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot'
  zh: GeRM
  ko: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot'
summary:
  en: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot (GeRM), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by MiLAB, Westlake University, and published at IROS 2024.'
  zh: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot (GeRM), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by MiLAB, Westlake University, and published at IROS 2024.'
  ko: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot (GeRM), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by MiLAB, Westlake University, and published at IROS 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- germ
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.13358v2.
sources:
- id: src_001
  type: website
  title: GeRM source
  url: https://doi.org/10.1109/IROS58592.2024.10801816
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Multi-task robot learning holds significant importance in tackling diverse and complex scenarios. However, current approaches are hindered by performance issues and difficulties in collecting training datasets. In this paper, we propose GeRM (Generalist Robotic Model). We utilize offline reinforcement learning to optimize data utilization strategies to learn from both demonstrations and sub-optimal data, thus surpassing the limitations of human demonstrations. Thereafter, we employ a transformer-based VLA network to process multi-modal inputs and output actions. By introducing the Mixture-of-Experts structure, GeRM allows faster inference speed with higher whole model capacity, and thus resolves the issue of limited RL parameters, enhancing model performance in multi-task learning while controlling computational costs. Through a series of experiments, we demonstrate that GeRM outperforms other methods across all tasks, while also validating its efficiency in both training and inference processes. Additionally, we uncover its potential to acquire emergent skills. Additionally, we contribute the QUARD-Auto dataset, collected automatically to support our training approach and foster advancements in multi-task quadruped robot learning. This work presents a new paradigm for reducing the cost of collecting robot data and driving progress in the multi-task learning community. You can reach our project and video through the link: https://songwxuan.github.io/GeRM/ .

## 核心内容
Multi-task robot learning holds significant importance in tackling diverse and complex scenarios. However, current approaches are hindered by performance issues and difficulties in collecting training datasets. In this paper, we propose GeRM (Generalist Robotic Model). We utilize offline reinforcement learning to optimize data utilization strategies to learn from both demonstrations and sub-optimal data, thus surpassing the limitations of human demonstrations. Thereafter, we employ a transformer-based VLA network to process multi-modal inputs and output actions. By introducing the Mixture-of-Experts structure, GeRM allows faster inference speed with higher whole model capacity, and thus resolves the issue of limited RL parameters, enhancing model performance in multi-task learning while controlling computational costs. Through a series of experiments, we demonstrate that GeRM outperforms other methods across all tasks, while also validating its efficiency in both training and inference processes. Additionally, we uncover its potential to acquire emergent skills. Additionally, we contribute the QUARD-Auto dataset, collected automatically to support our training approach and foster advancements in multi-task quadruped robot learning. This work presents a new paradigm for reducing the cost of collecting robot data and driving progress in the multi-task learning community. You can reach our project and video through the link: https://songwxuan.github.io/GeRM/ .

## 参考
- http://arxiv.org/abs/2403.13358v2

