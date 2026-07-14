---
$id: ent_paper_scalable_dexterous_robot_learn_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scalable Dexterous Robot Learning with AR-based Remote Human-Robot Interactions
  zh: Scalable Dexterous Robot Learning with AR-based Remote Human-Robot Interactions
  ko: Scalable Dexterous Robot Learning with AR-based Remote Human-Robot Interactions
summary:
  en: "arXiv:2602.07341v2 Announce Type: replace-cross \nAbstract: This paper focuses on the scalable robot learning for manipulation\
    \ in the dexterous robot arm-hand systems, where the remote human-robot interactions via augmented reality (AR) are established\
    \ to collect the expert demonstration data for improving efficiency. In such a system, we present a novel method to address\
    \ the general manipulation task problem. Specifically, the proposed method consists of two phases: i) In the first phase\
    \ for pretraining, the policy is created in a behavior cloning (BC) manner, through leveraging the learning data from\
    \ our AR-based remote human-robot interaction system; ii) In the second phase, a contrastive learning empowered reinforcement\
    \ learning (RL) method is developed to obtain more efficient and robust policy than the BC, and thus a projection head\
    \ is designed to accelerate the learning progress. An event-driven augmented reward is adopted for enhancing the safety.\
    \ To validate the proposed method, both the physics simulations via PyBullet and real-world experiments are carried out.\
    \ The results demonstrate that compared to the baselines, our method not only significantly speeds up the training process,\
    \ but also achieves much better performance in terms of the success rate for fulfilling the manipulation tasks. By conducting\
    \ the ablation study, it is confirmed that the proposed RL with contrastive learning overcomes policy collapse. Supplementary\
    \ demonstrations are available at https://cyberyyc.github.io/."
  zh: "arXiv:2602.07341v2 Announce Type: replace-cross \nAbstract: This paper focuses on the scalable robot learning for manipulation\
    \ in the dexterous robot arm-hand systems, where the remote human-robot interactions via augmented reality (AR) are established\
    \ to collect the expert demonstration data for improving efficiency. In such a system, we present a novel method to address\
    \ the general manipulation task problem. Specifically, the proposed method consists of two phases: i) In the first phase\
    \ for pretraining, the policy is created in a behavior cloning (BC) manner, through leveraging the learning data from\
    \ our AR-based remote human-robot interaction system; ii) In the second phase, a contrastive learning empowered reinforcement\
    \ learning (RL) method is developed to obtain more efficient and robust policy than the BC, and thus a projection head\
    \ is designed to accelerate the learning progress. An event-driven augmented reward is adopted for enhancing the safety.\
    \ To validate the proposed method, both the physics simulations via PyBullet and real-world experiments are carried out.\
    \ The results demonstrate that compared to the baselines, our method not only significantly speeds up the training process,\
    \ but also achieves much better performance in terms of the success rate for fulfilling the manipulation tasks. By conducting\
    \ the ablation study, it is confirmed that the proposed RL with contrastive learning overcomes policy collapse. Supplementary\
    \ demonstrations are available at https://cyberyyc.github.io/."
  ko: "arXiv:2602.07341v2 Announce Type: replace-cross \nAbstract: This paper focuses on the scalable robot learning for manipulation\
    \ in the dexterous robot arm-hand systems, where the remote human-robot interactions via augmented reality (AR) are established\
    \ to collect the expert demonstration data for improving efficiency. In such a system, we present a novel method to address\
    \ the general manipulation task problem. Specifically, the proposed method consists of two phases: i) In the first phase\
    \ for pretraining, the policy is created in a behavior cloning (BC) manner, through leveraging the learning data from\
    \ our AR-based remote human-robot interaction system; ii) In the second phase, a contrastive learning empowered reinforcement\
    \ learning (RL) method is developed to obtain more efficient and robust policy than the BC, and thus a projection head\
    \ is designed to accelerate the learning progress. An event-driven augmented reward is adopted for enhancing the safety.\
    \ To validate the proposed method, both the physics simulations via PyBullet and real-world experiments are carried out.\
    \ The results demonstrate that compared to the baselines, our method not only significantly speeds up the training process,\
    \ but also achieves much better performance in terms of the success rate for fulfilling the manipulation tasks. By conducting\
    \ the ablation study, it is confirmed that the proposed RL with contrastive learning overcomes policy collapse. Supplementary\
    \ demonstrations are available at https://cyberyyc.github.io/."
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
- robotics
- scalable_dexterous_robot_learn
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.07341v2.
sources:
- id: src_001
  type: paper
  title: Scalable Dexterous Robot Learning with AR-based Remote Human-Robot Interactions (arXiv)
  url: https://arxiv.org/abs/2602.07341
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
This paper focuses on the scalable robot learning for manipulation in the dexterous robot arm-hand systems, where the remote human-robot interactions via augmented reality (AR) are established to collect the expert demonstration data for improving efficiency. In such a system, we present a novel method to address the general manipulation task problem. Specifically, the proposed method consists of two phases: i) In the first phase for pretraining, the policy is created in a behavior cloning (BC) manner, through leveraging the learning data from our AR-based remote human-robot interaction system; ii) In the second phase, a contrastive learning empowered reinforcement learning (RL) method is developed to obtain more efficient and robust policy than the BC, and thus a projection head is designed to accelerate the learning progress. An event-driven augmented reward is adopted for enhancing the safety. To validate the proposed method, both the physics simulations via PyBullet and real-world experiments are carried out. The results demonstrate that compared to the baselines, our method not only significantly speeds up the training process, but also achieves much better performance in terms of the success rate for fulfilling the manipulation tasks. By conducting the ablation study, it is confirmed that the proposed RL with contrastive learning overcomes policy collapse. Supplementary demonstrations are available at https://cyberyyc.github.io/.

## 核心内容
This paper focuses on the scalable robot learning for manipulation in the dexterous robot arm-hand systems, where the remote human-robot interactions via augmented reality (AR) are established to collect the expert demonstration data for improving efficiency. In such a system, we present a novel method to address the general manipulation task problem. Specifically, the proposed method consists of two phases: i) In the first phase for pretraining, the policy is created in a behavior cloning (BC) manner, through leveraging the learning data from our AR-based remote human-robot interaction system; ii) In the second phase, a contrastive learning empowered reinforcement learning (RL) method is developed to obtain more efficient and robust policy than the BC, and thus a projection head is designed to accelerate the learning progress. An event-driven augmented reward is adopted for enhancing the safety. To validate the proposed method, both the physics simulations via PyBullet and real-world experiments are carried out. The results demonstrate that compared to the baselines, our method not only significantly speeds up the training process, but also achieves much better performance in terms of the success rate for fulfilling the manipulation tasks. By conducting the ablation study, it is confirmed that the proposed RL with contrastive learning overcomes policy collapse. Supplementary demonstrations are available at https://cyberyyc.github.io/.

## 参考
- http://arxiv.org/abs/2602.07341v2

