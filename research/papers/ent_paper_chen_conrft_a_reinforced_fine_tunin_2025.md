---
$id: ent_paper_chen_conrft_a_reinforced_fine_tunin_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy'
  zh: ConRFT
  ko: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy'
summary:
  en: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (ConRFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by SKL-MAIS, Institute of Automation, Chinese Academy of Sciences, School of
    Artificial Intelligence, University of Chinese Academy of Sciences, and published at RSS25.'
  zh: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (ConRFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by SKL-MAIS, Institute of Automation, Chinese Academy of Sciences, School of
    Artificial Intelligence, University of Chinese Academy of Sciences, and published at RSS25.'
  ko: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (ConRFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by SKL-MAIS, Institute of Automation, Chinese Academy of Sciences, School of
    Artificial Intelligence, University of Chinese Academy of Sciences, and published at RSS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- conrft
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05450v2.
sources:
- id: src_001
  type: paper
  title: 'ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (arXiv)'
  url: https://arxiv.org/abs/2502.05450
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ConRFT source
  url: https://doi.org/10.48550/arXiv.2502.05450
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown substantial potential in real-world robotic manipulation. However, fine-tuning these models through supervised learning struggles to achieve robust performance due to limited, inconsistent demonstrations, especially in contact-rich environments. In this paper, we propose a reinforced fine-tuning approach for VLA models, named ConRFT, which consists of offline and online fine-tuning with a unified consistency-based training objective, to address these challenges. In the offline stage, our method integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating. In the online stage, the VLA model is further fine-tuned via consistency policy, with human interventions to ensure safe exploration and high sample efficiency. We evaluate our approach on eight diverse real-world manipulation tasks. It achieves an average success rate of 96.3% within 45-90 minutes of online fine-tuning, outperforming prior supervised methods with a 144% improvement in success rate and 1.9x shorter episode length. This work highlights the potential of integrating reinforcement learning to enhance the performance of VLA models for real-world robotic applications. Videos and code are available at our project website https://cccedric.github.io/conrft/.

## 核心内容
Vision-Language-Action (VLA) models have shown substantial potential in real-world robotic manipulation. However, fine-tuning these models through supervised learning struggles to achieve robust performance due to limited, inconsistent demonstrations, especially in contact-rich environments. In this paper, we propose a reinforced fine-tuning approach for VLA models, named ConRFT, which consists of offline and online fine-tuning with a unified consistency-based training objective, to address these challenges. In the offline stage, our method integrates behavior cloning and Q-learning to effectively extract policy from a small set of demonstrations and stabilize value estimating. In the online stage, the VLA model is further fine-tuned via consistency policy, with human interventions to ensure safe exploration and high sample efficiency. We evaluate our approach on eight diverse real-world manipulation tasks. It achieves an average success rate of 96.3% within 45-90 minutes of online fine-tuning, outperforming prior supervised methods with a 144% improvement in success rate and 1.9x shorter episode length. This work highlights the potential of integrating reinforcement learning to enhance the performance of VLA models for real-world robotic applications. Videos and code are available at our project website https://cccedric.github.io/conrft/.

## 参考
- http://arxiv.org/abs/2502.05450v2

