---
$id: ent_paper_zhao_more_unlocking_scalability_in_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models'
  zh: MoRE
  ko: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models'
summary:
  en: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models (MoRE), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab, and published at ICRA25.'
  zh: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models (MoRE), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab, and published at ICRA25.'
  ko: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models (MoRE), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab, and published at ICRA25.'
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
- more
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.08007v1.
sources:
- id: src_001
  type: website
  title: MoRE source
  url: https://doi.org/10.1109/ICRA55743.2025.11128601
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Developing versatile quadruped robots that can smoothly perform various actions and tasks in real-world environments remains a significant challenge. This paper introduces a novel vision-language-action (VLA) model, mixture of robotic experts (MoRE), for quadruped robots that aim to introduce reinforcement learning (RL) for fine-tuning large-scale VLA models with a large amount of mixed-quality data. MoRE integrates multiple low-rank adaptation modules as distinct experts within a dense multi-modal large language model (MLLM), forming a sparse-activated mixture-of-experts model. This design enables the model to effectively adapt to a wide array of downstream tasks. Moreover, we employ a reinforcement learning-based training objective to train our model as a Q-function after deeply exploring the structural properties of our tasks. Effective learning from automatically collected mixed-quality data enhances data efficiency and model performance. Extensive experiments demonstrate that MoRE outperforms all baselines across six different skills and exhibits superior generalization capabilities in out-of-distribution scenarios. We further validate our method in real-world scenarios, confirming the practicality of our approach and laying a solid foundation for future research on multi-task learning in quadruped robots.

## 核心内容
Developing versatile quadruped robots that can smoothly perform various actions and tasks in real-world environments remains a significant challenge. This paper introduces a novel vision-language-action (VLA) model, mixture of robotic experts (MoRE), for quadruped robots that aim to introduce reinforcement learning (RL) for fine-tuning large-scale VLA models with a large amount of mixed-quality data. MoRE integrates multiple low-rank adaptation modules as distinct experts within a dense multi-modal large language model (MLLM), forming a sparse-activated mixture-of-experts model. This design enables the model to effectively adapt to a wide array of downstream tasks. Moreover, we employ a reinforcement learning-based training objective to train our model as a Q-function after deeply exploring the structural properties of our tasks. Effective learning from automatically collected mixed-quality data enhances data efficiency and model performance. Extensive experiments demonstrate that MoRE outperforms all baselines across six different skills and exhibits superior generalization capabilities in out-of-distribution scenarios. We further validate our method in real-world scenarios, confirming the practicality of our approach and laying a solid foundation for future research on multi-task learning in quadruped robots.

## 参考
- http://arxiv.org/abs/2503.08007v1

