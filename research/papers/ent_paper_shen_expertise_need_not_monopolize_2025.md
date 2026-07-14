---
$id: ent_paper_shen_expertise_need_not_monopolize_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning'
  zh: AdaMoE
  ko: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning'
summary:
  en: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (AdaMoE),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tsinghua
    University, The University of Hong Kong, Tongji University, D-Robotics, Key Laboratory of System Control and Information
    Processing, Shanghai Key Laboratory of Integrated Administration Technologies for Information Security.'
  zh: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (AdaMoE),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tsinghua
    University, The University of Hong Kong, Tongji University, D-Robotics, Key Laboratory of System Control and Information
    Processing, Shanghai Key Laboratory of Integrated Administration Technologies for Information Security.'
  ko: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (AdaMoE),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tsinghua
    University, The University of Hong Kong, Tongji University, D-Robotics, Key Laboratory of System Control and Information
    Processing, Shanghai Key Laboratory of Integrated Administration Technologies for Information Security.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- adamoe
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14300v1.
sources:
- id: src_001
  type: paper
  title: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (arXiv)'
  url: https://arxiv.org/abs/2510.14300
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AdaMoE source
  url: https://doi.org/10.48550/arXiv.2510.14300
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models are experiencing rapid development and demonstrating promising capabilities in robotic manipulation tasks. However, scaling up VLA models presents several critical challenges: (1) Training new VLA models from scratch demands substantial computational resources and extensive datasets. Given the current scarcity of robot data, it becomes particularly valuable to fully leverage well-pretrained VLA model weights during the scaling process. (2) Real-time control requires carefully balancing model capacity with computational efficiency. To address these challenges, We propose AdaMoE, a Mixture-of-Experts (MoE) architecture that inherits pretrained weights from dense VLA models, and scales up the action expert by substituting the feedforward layers into sparsely activated MoE layers. AdaMoE employs a decoupling technique that decouples expert selection from expert weighting through an independent scale adapter working alongside the traditional router. This enables experts to be selected based on task relevance while contributing with independently controlled weights, allowing collaborative expert utilization rather than winner-takes-all dynamics. Our approach demonstrates that expertise need not monopolize. Instead, through collaborative expert utilization, we can achieve superior performance while maintaining computational efficiency. AdaMoE consistently outperforms the baseline model across key benchmarks, delivering performance gains of 1.8% on LIBERO and 9.3% on RoboTwin. Most importantly, a substantial 21.5% improvement in real-world experiments validates its practical effectiveness for robotic manipulation tasks.

## 核心内容
Vision-Language-Action (VLA) models are experiencing rapid development and demonstrating promising capabilities in robotic manipulation tasks. However, scaling up VLA models presents several critical challenges: (1) Training new VLA models from scratch demands substantial computational resources and extensive datasets. Given the current scarcity of robot data, it becomes particularly valuable to fully leverage well-pretrained VLA model weights during the scaling process. (2) Real-time control requires carefully balancing model capacity with computational efficiency. To address these challenges, We propose AdaMoE, a Mixture-of-Experts (MoE) architecture that inherits pretrained weights from dense VLA models, and scales up the action expert by substituting the feedforward layers into sparsely activated MoE layers. AdaMoE employs a decoupling technique that decouples expert selection from expert weighting through an independent scale adapter working alongside the traditional router. This enables experts to be selected based on task relevance while contributing with independently controlled weights, allowing collaborative expert utilization rather than winner-takes-all dynamics. Our approach demonstrates that expertise need not monopolize. Instead, through collaborative expert utilization, we can achieve superior performance while maintaining computational efficiency. AdaMoE consistently outperforms the baseline model across key benchmarks, delivering performance gains of 1.8% on LIBERO and 9.3% on RoboTwin. Most importantly, a substantial 21.5% improvement in real-world experiments validates its practical effectiveness for robotic manipulation tasks.

## 参考
- http://arxiv.org/abs/2510.14300v1

