---
$id: ent_paper_reinforcement_learning_based_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
  zh: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
  ko: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
summary:
  en: "arXiv:2606.31807v1 Announce Type: new \nAbstract: As humanoid robots become increasingly dynamic, coupling them with\
    \ reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline\
    \ skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile\
    \ agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this\
    \ paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid\
    \ robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal\
    \ robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven\
    \ propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion\
    \ data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation\
    \ contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation,\
    \ along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates\
    \ up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully\
    \ transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability\
    \ to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our\
    \ results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo."
  zh: "arXiv:2606.31807v1 Announce Type: new \nAbstract: As humanoid robots become increasingly dynamic, coupling them with\
    \ reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline\
    \ skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile\
    \ agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this\
    \ paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid\
    \ robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal\
    \ robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven\
    \ propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion\
    \ data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation\
    \ contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation,\
    \ along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates\
    \ up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully\
    \ transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability\
    \ to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our\
    \ results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo."
  ko: "arXiv:2606.31807v1 Announce Type: new \nAbstract: As humanoid robots become increasingly dynamic, coupling them with\
    \ reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline\
    \ skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile\
    \ agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this\
    \ paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid\
    \ robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal\
    \ robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven\
    \ propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion\
    \ data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation\
    \ contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation,\
    \ along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates\
    \ up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully\
    \ transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability\
    \ to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our\
    \ results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo."
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
- reinforcement_learning_based_c
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31807v1.
sources:
- id: src_001
  type: paper
  title: Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot
  url: https://arxiv.org/abs/2606.31807
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
As humanoid robots become increasingly dynamic, coupling them with reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo.

## 核心内容
As humanoid robots become increasingly dynamic, coupling them with reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo.

## 参考
- http://arxiv.org/abs/2606.31807v1

