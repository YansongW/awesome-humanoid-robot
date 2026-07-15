---
$id: ent_paper_leal_sara_rt_scaling_up_robotics_tr_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention'
  zh: SARA-RT
  ko: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention'
summary:
  en: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention (SARA-RT), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google, and published at ICRA 2023.'
  zh: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention (SARA-RT), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google, and published at ICRA 2023.'
  ko: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention (SARA-RT), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google, and published at ICRA 2023.'
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
- sara_rt
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.01990v1.
sources:
- id: src_001
  type: website
  title: SARA-RT source
  url: https://doi.org/10.1109/ICRA57147.2024.10611597
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment. SARA-RT relies on the new method of fine-tuning proposed by us, called up-training. It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterparts maintaining high quality. We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models, the first VLA robotic policies pre-trained on internet-scale data, as well as (b) Point Cloud Transformer (PCT) robotic policies operating on large point clouds. We complement our results with the rigorous mathematical analysis providing deeper insight into the phenomenon of SARA.

## 核心内容
We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment. SARA-RT relies on the new method of fine-tuning proposed by us, called up-training. It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterparts maintaining high quality. We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models, the first VLA robotic policies pre-trained on internet-scale data, as well as (b) Point Cloud Transformer (PCT) robotic policies operating on large point clouds. We complement our results with the rigorous mathematical analysis providing deeper insight into the phenomenon of SARA.

## 参考
- http://arxiv.org/abs/2312.01990v1

