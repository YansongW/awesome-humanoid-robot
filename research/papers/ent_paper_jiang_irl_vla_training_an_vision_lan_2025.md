---
$id: ent_paper_jiang_irl_vla_training_an_vision_lan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model'
  zh: IRL-VLA
  ko: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model'
summary:
  en: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model (IRL-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Bosch Corporate Research, School of Communication and Information Engineering,
    Shanghai University, School of Mechanical Engineering, Shanghai Jiao Tong University, Bosch Mobility Solutions, Robert
    Bosch GmbH, AIR, Tsinghua University.'
  zh: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model (IRL-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Bosch Corporate Research, School of Communication and Information Engineering,
    Shanghai University, School of Mechanical Engineering, Shanghai Jiao Tong University, Bosch Mobility Solutions, Robert
    Bosch GmbH, AIR, Tsinghua University.'
  ko: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model (IRL-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Bosch Corporate Research, School of Communication and Information Engineering,
    Shanghai University, School of Mechanical Engineering, Shanghai Jiao Tong University, Bosch Mobility Solutions, Robert
    Bosch GmbH, AIR, Tsinghua University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- irl_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.06571v3.
sources:
- id: src_001
  type: paper
  title: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model (arXiv)'
  url: https://arxiv.org/abs/2508.06571
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: IRL-VLA source
  url: https://doi.org/10.48550/arXiv.2508.06571
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have demonstrated potential in autonomous driving. However, two critical challenges hinder their development: (1) Existing VLA architectures are typically based on imitation learning in open-loop setup which tends to capture the recorded behaviors in the dataset, leading to suboptimal and constrained performance, (2) Close-loop training relies heavily on high-fidelity sensor simulation, where domain gaps and computational inefficiencies pose significant barriers. In this paper, we introduce IRL-VLA, a novel close-loop Reinforcement Learning via \textbf{I}nverse \textbf{R}einforcement \textbf{L}earning reward world model with a self-built VLA approach. Our framework proceeds in a three-stage paradigm: In the first stage, we propose a VLA architecture and pretrain the VLA policy via imitation learning. In the second stage, we construct a lightweight reward world model via inverse reinforcement learning to enable efficient close-loop reward computation. To further enhance planning performance, finally, we design specialized reward world model guidence reinforcement learning via PPO(Proximal Policy Optimization) to effectively balance the safety incidents, comfortable driving, and traffic efficiency. Our approach achieves state-of-the-art performance in NAVSIM v2 end-to-end driving benchmark, 1st runner up in CVPR2025 Autonomous Grand Challenge. We hope that our framework will accelerate VLA research in close-loop autonomous driving.

## 核心内容
Vision-Language-Action (VLA) models have demonstrated potential in autonomous driving. However, two critical challenges hinder their development: (1) Existing VLA architectures are typically based on imitation learning in open-loop setup which tends to capture the recorded behaviors in the dataset, leading to suboptimal and constrained performance, (2) Close-loop training relies heavily on high-fidelity sensor simulation, where domain gaps and computational inefficiencies pose significant barriers. In this paper, we introduce IRL-VLA, a novel close-loop Reinforcement Learning via \textbf{I}nverse \textbf{R}einforcement \textbf{L}earning reward world model with a self-built VLA approach. Our framework proceeds in a three-stage paradigm: In the first stage, we propose a VLA architecture and pretrain the VLA policy via imitation learning. In the second stage, we construct a lightweight reward world model via inverse reinforcement learning to enable efficient close-loop reward computation. To further enhance planning performance, finally, we design specialized reward world model guidence reinforcement learning via PPO(Proximal Policy Optimization) to effectively balance the safety incidents, comfortable driving, and traffic efficiency. Our approach achieves state-of-the-art performance in NAVSIM v2 end-to-end driving benchmark, 1st runner up in CVPR2025 Autonomous Grand Challenge. We hope that our framework will accelerate VLA research in close-loop autonomous driving.

## 参考
- http://arxiv.org/abs/2508.06571v3

