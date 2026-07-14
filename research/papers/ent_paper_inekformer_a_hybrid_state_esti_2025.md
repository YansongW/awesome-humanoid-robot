---
$id: ent_paper_inekformer_a_hybrid_state_esti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots'
  zh: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots'
  ko: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots'
summary:
  en: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots is a 2025 work on state estimation for humanoid robots.'
  zh: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots is a 2025 work on state estimation for humanoid robots.'
  ko: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots is a 2025 work on state estimation for humanoid robots.'
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
- inekformer
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16306v1.
sources:
- id: src_001
  type: paper
  title: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2511.16306
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have great potential for a wide range of applications, including industrial and domestic use, healthcare, and search and rescue missions. However, bipedal locomotion in different environments is still a challenge when it comes to performing stable and dynamic movements. This is where state estimation plays a crucial role, providing fast and accurate feedback of the robot's floating base state to the motion controller. Although classical state estimation methods such as Kalman filters are widely used in robotics, they require expert knowledge to fine-tune the noise parameters. Due to recent advances in the field of machine learning, deep learning methods are increasingly used for state estimation tasks. In this work, we propose the InEKFormer, a novel hybrid state estimation method that incorporates an invariant extended Kalman filter (InEKF) and a Transformer network. We compare our method with the InEKF and the KalmanNet approaches on datasets obtained from the humanoid robot RH5. The results indicate the potential of Transformers in humanoid state estimation, but also highlight the need for robust autoregressive training in these high-dimensional problems.

## 核心内容
Humanoid robots have great potential for a wide range of applications, including industrial and domestic use, healthcare, and search and rescue missions. However, bipedal locomotion in different environments is still a challenge when it comes to performing stable and dynamic movements. This is where state estimation plays a crucial role, providing fast and accurate feedback of the robot's floating base state to the motion controller. Although classical state estimation methods such as Kalman filters are widely used in robotics, they require expert knowledge to fine-tune the noise parameters. Due to recent advances in the field of machine learning, deep learning methods are increasingly used for state estimation tasks. In this work, we propose the InEKFormer, a novel hybrid state estimation method that incorporates an invariant extended Kalman filter (InEKF) and a Transformer network. We compare our method with the InEKF and the KalmanNet approaches on datasets obtained from the humanoid robot RH5. The results indicate the potential of Transformers in humanoid state estimation, but also highlight the need for robust autoregressive training in these high-dimensional problems.

## 参考
- http://arxiv.org/abs/2511.16306v1

