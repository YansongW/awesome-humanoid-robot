---
$id: ent_paper_chebotar_q_transformer_scalable_offline_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions'
  zh: Q-Transformer
  ko: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions'
summary:
  en: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions (Q-Transformer), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
  zh: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions (Q-Transformer), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
  ko: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions (Q-Transformer), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- q_transformer
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.10150v2.
sources:
- id: src_001
  type: paper
  title: Q-Transformer source
  url: https://proceedings.mlr.press/v229/chebotar23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and autonomously collected data. Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups. We therefore refer to the method as Q-Transformer. By discretizing each action dimension and representing the Q-value of each action dimension as separate tokens, we can apply effective high-capacity sequence modeling techniques for Q-learning. We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a large diverse real-world robotic manipulation task suite. The project's website and videos can be found at https://qtransformer.github.io

## 核心内容
In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and autonomously collected data. Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups. We therefore refer to the method as Q-Transformer. By discretizing each action dimension and representing the Q-value of each action dimension as separate tokens, we can apply effective high-capacity sequence modeling techniques for Q-learning. We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a large diverse real-world robotic manipulation task suite. The project's website and videos can be found at https://qtransformer.github.io

## 参考
- http://arxiv.org/abs/2309.10150v2

