---
$id: ent_paper_li_bridgevla_input_output_alignme_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models'
  zh: BridgeVLA
  ko: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models'
summary:
  en: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (BridgeVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by ByteDance Seed, School of Artificial
    Intelligence, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, FiveAges,
    Nanjing University, and published at NIPS25.'
  zh: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (BridgeVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by ByteDance Seed, School of Artificial
    Intelligence, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, FiveAges,
    Nanjing University, and published at NIPS25.'
  ko: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (BridgeVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by ByteDance Seed, School of Artificial
    Intelligence, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, FiveAges,
    Nanjing University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bridgevla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.07961v2.
sources:
- id: src_001
  type: paper
  title: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (arXiv)'
  url: https://arxiv.org/abs/2506.07961
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: BridgeVLA source
  url: https://doi.org/10.48550/arXiv.2506.07961
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website:https://bridgevla.github.io/

## 核心内容
Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website:https://bridgevla.github.io/

## 参考
- http://arxiv.org/abs/2506.07961v2

