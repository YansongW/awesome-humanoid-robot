---
$id: ent_paper_top_time_optimization_policy_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots'
  zh: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots'
  ko: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots'
summary:
  en: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots is a 2025 work on
    manipulation for humanoid robots.'
  zh: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots is a 2025 work on
    manipulation for humanoid robots.'
  ko: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots is a 2025 work on
    manipulation for humanoid robots.'
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
- top
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.00355v1.
sources:
- id: src_001
  type: paper
  title: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2508.00355
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have the potential capability to perform a diverse range of manipulation tasks, but this is based on a robust and precise standing controller. Existing methods are either ill-suited to precisely control high-dimensional upper-body joints, or difficult to ensure both robustness and accuracy, especially when upper-body motions are fast. This paper proposes a novel time optimization policy (TOP), to train a standing manipulation control model that ensures balance, precision, and time efficiency simultaneously, with the idea of adjusting the time trajectory of upper-body motions but not only strengthening the disturbance resistance of the lower-body. Our approach consists of three parts. Firstly, we utilize motion prior to represent upper-body motions to enhance the coordination ability between the upper and lower-body by training a variational autoencoder (VAE). Then we decouple the whole-body control into an upper-body PD controller for precision and a lower-body RL controller to enhance robust stability. Finally, we train TOP method in conjunction with the decoupled controller and VAE to reduce the balance burden resulting from fast upper-body motions that would destabilize the robot and exceed the capabilities of the lower-body RL policy. The effectiveness of the proposed approach is evaluated via both simulation and real world experiments, which demonstrate the superiority on standing manipulation tasks stably and accurately. The project page can be found at https://anonymous.4open.science/w/top-258F/.

## 核心内容
Humanoid robots have the potential capability to perform a diverse range of manipulation tasks, but this is based on a robust and precise standing controller. Existing methods are either ill-suited to precisely control high-dimensional upper-body joints, or difficult to ensure both robustness and accuracy, especially when upper-body motions are fast. This paper proposes a novel time optimization policy (TOP), to train a standing manipulation control model that ensures balance, precision, and time efficiency simultaneously, with the idea of adjusting the time trajectory of upper-body motions but not only strengthening the disturbance resistance of the lower-body. Our approach consists of three parts. Firstly, we utilize motion prior to represent upper-body motions to enhance the coordination ability between the upper and lower-body by training a variational autoencoder (VAE). Then we decouple the whole-body control into an upper-body PD controller for precision and a lower-body RL controller to enhance robust stability. Finally, we train TOP method in conjunction with the decoupled controller and VAE to reduce the balance burden resulting from fast upper-body motions that would destabilize the robot and exceed the capabilities of the lower-body RL policy. The effectiveness of the proposed approach is evaluated via both simulation and real world experiments, which demonstrate the superiority on standing manipulation tasks stably and accurately. The project page can be found at https://anonymous.4open.science/w/top-258F/.

## 参考
- http://arxiv.org/abs/2508.00355v1

