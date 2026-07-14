---
$id: ent_paper_mimicdroid_in_context_learning_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos'
  zh: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos'
  ko: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos'
summary:
  en: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos is a 2025 work on manipulation
    for humanoid robots.'
  zh: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos is a 2025 work on manipulation
    for humanoid robots.'
  ko: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos is a 2025 work on manipulation
    for humanoid robots.'
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
- mimicdroid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09769v1.
sources:
- id: src_001
  type: paper
  title: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos (arXiv)'
  url: https://arxiv.org/abs/2509.09769
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We aim to enable humanoid robots to efficiently solve new manipulation tasks from a few video examples. In-context learning (ICL) is a promising framework for achieving this goal due to its test-time data efficiency and rapid adaptability. However, current ICL methods rely on labor-intensive teleoperated data for training, which restricts scalability. We propose using human play videos -- continuous, unlabeled videos of people interacting freely with their environment -- as a scalable and diverse training data source. We introduce MimicDroid, which enables humanoids to perform ICL using human play videos as the only training data. MimicDroid extracts trajectory pairs with similar manipulation behaviors and trains the policy to predict the actions of one trajectory conditioned on the other. Through this process, the model acquired ICL capabilities for adapting to novel objects and environments at test time. To bridge the embodiment gap, MimicDroid first retargets human wrist poses estimated from RGB videos to the humanoid, leveraging kinematic similarity. It also applies random patch masking during training to reduce overfitting to human-specific cues and improve robustness to visual differences. To evaluate few-shot learning for humanoids, we introduce an open-source simulation benchmark with increasing levels of generalization difficulty. MimicDroid outperformed state-of-the-art methods and achieved nearly twofold higher success rates in the real world. Additional materials can be found on: ut-austin-rpl.github.io/MimicDroid

## 核心内容
We aim to enable humanoid robots to efficiently solve new manipulation tasks from a few video examples. In-context learning (ICL) is a promising framework for achieving this goal due to its test-time data efficiency and rapid adaptability. However, current ICL methods rely on labor-intensive teleoperated data for training, which restricts scalability. We propose using human play videos -- continuous, unlabeled videos of people interacting freely with their environment -- as a scalable and diverse training data source. We introduce MimicDroid, which enables humanoids to perform ICL using human play videos as the only training data. MimicDroid extracts trajectory pairs with similar manipulation behaviors and trains the policy to predict the actions of one trajectory conditioned on the other. Through this process, the model acquired ICL capabilities for adapting to novel objects and environments at test time. To bridge the embodiment gap, MimicDroid first retargets human wrist poses estimated from RGB videos to the humanoid, leveraging kinematic similarity. It also applies random patch masking during training to reduce overfitting to human-specific cues and improve robustness to visual differences. To evaluate few-shot learning for humanoids, we introduce an open-source simulation benchmark with increasing levels of generalization difficulty. MimicDroid outperformed state-of-the-art methods and achieved nearly twofold higher success rates in the real world. Additional materials can be found on: ut-austin-rpl.github.io/MimicDroid

## 参考
- http://arxiv.org/abs/2509.09769v1

