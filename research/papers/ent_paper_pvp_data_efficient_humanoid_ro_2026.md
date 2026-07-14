---
$id: ent_paper_pvp_data_efficient_humanoid_ro_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations'
  zh: 训练时的 privileged state 如何变成部署时的本体能力
  ko: 'PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations'
summary:
  en: 'PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations is a knowledge
    node related to paper in the humanoid robot value chain.'
  zh: 'Achieving efficient and robust whole-body control (WBC) is essential for enabling humanoid robots to perform complex
    tasks in dynamic environments. Despite the success of reinforcement learning (RL) in this domain, its sample inefficiency
    remains a significant challenge due to the intricate dynamics and partial observability of humanoid robots. To address
    this limitation, we propose PvP, a Proprioceptive-Privileged contrastive learning framework that leverages the intrinsic
    complementarity between proprioceptive and privileged states. PvP learns compact and task-relevant latent representations
    without requiring hand-crafted data augmentations, enabling faster and more stable policy learning. To support systematic
    evaluation, we develop SRL4Humanoid, the first unified and modular framework '
  ko: 'PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations is a knowledge
    node related to paper in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- privileged_state
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13093v2.
sources:
- id: src_001
  type: paper
  title: 'PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations (arXiv)'
  url: https://arxiv.org/abs/2512.13093
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 训练时的 privileged state 如何变成部署时的本体能力 project page
  url: https://github.com/myismyname/SRL4Humanoid
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Achieving efficient and robust whole-body control (WBC) is essential for enabling humanoid robots to perform complex tasks in dynamic environments. Despite the success of reinforcement learning (RL) in this domain, its sample inefficiency remains a significant challenge due to the intricate dynamics and partial observability of humanoid robots. To address this limitation, we propose PvP, a Proprioceptive-Privileged contrastive learning framework that leverages the intrinsic complementarity between proprioceptive and privileged states. PvP learns compact and task-relevant latent representations without requiring hand-crafted data augmentations, enabling faster and more stable policy learning. To support systematic evaluation, we develop SRL4Humanoid, the first unified and modular framework that provides high-quality implementations of representative state representation learning (SRL) methods for humanoid robot learning. Extensive experiments on the LimX Oli robot across velocity tracking and motion imitation tasks demonstrate that PvP significantly improves sample efficiency and final performance compared to baseline SRL methods. Our study further provides practical insights into integrating SRL with RL for humanoid WBC, offering valuable guidance for data-efficient humanoid robot learning.

## 核心内容
Achieving efficient and robust whole-body control (WBC) is essential for enabling humanoid robots to perform complex tasks in dynamic environments. Despite the success of reinforcement learning (RL) in this domain, its sample inefficiency remains a significant challenge due to the intricate dynamics and partial observability of humanoid robots. To address this limitation, we propose PvP, a Proprioceptive-Privileged contrastive learning framework that leverages the intrinsic complementarity between proprioceptive and privileged states. PvP learns compact and task-relevant latent representations without requiring hand-crafted data augmentations, enabling faster and more stable policy learning. To support systematic evaluation, we develop SRL4Humanoid, the first unified and modular framework that provides high-quality implementations of representative state representation learning (SRL) methods for humanoid robot learning. Extensive experiments on the LimX Oli robot across velocity tracking and motion imitation tasks demonstrate that PvP significantly improves sample efficiency and final performance compared to baseline SRL methods. Our study further provides practical insights into integrating SRL with RL for humanoid WBC, offering valuable guidance for data-efficient humanoid robot learning.

## 参考
- http://arxiv.org/abs/2512.13093v2

