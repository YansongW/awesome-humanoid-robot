---
$id: ent_paper_autoodom_learning_auto_regress_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion'
  zh: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion'
  ko: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion'
summary:
  en: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion is a 2025 work on state estimation
    for humanoid robots.'
  zh: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion is a 2025 work on state estimation
    for humanoid robots.'
  ko: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion is a 2025 work on state estimation
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
- autoodom
- humanoid
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.18857v1.
sources:
- id: src_001
  type: paper
  title: 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion (arXiv)'
  url: https://arxiv.org/abs/2511.18857
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Accurate proprioceptive odometry is fundamental for legged robot navigation in GPS-denied and visually degraded environments where conventional visual odometry systems fail. Current approaches face critical limitations: analytical filtering methods suffer from modeling uncertainties and cumulative drift, hybrid learning-filtering approaches remain constrained by their analytical components, while pure learning-based methods struggle with simulation-to-reality transfer and demand extensive real-world data collection. This paper introduces AutoOdom, a novel autoregressive proprioceptive odometry system that overcomes these challenges through an innovative two-stage training paradigm. Stage 1 employs large-scale simulation data to learn complex nonlinear dynamics and rapidly changing contact states inherent in legged locomotion, while Stage 2 introduces an autoregressive enhancement mechanism using limited real-world data to effectively bridge the sim-to-real gap. The key innovation lies in our autoregressive training approach, where the model learns from its own predictions to develop resilience against sensor noise and improve robustness in highly dynamic environments. Comprehensive experimental validation on the Booster T1 humanoid robot demonstrates that AutoOdom significantly outperforms state-of-the-art methods across all evaluation metrics, achieving 57.2% improvement in absolute trajectory error, 59.2% improvement in Umeyama-aligned error, and 36.2% improvement in relative pose error compared to the Legolas baseline. Extensive ablation studies provide critical insights into sensor modality selection and temporal modeling, revealing counterintuitive findings about IMU acceleration data and validating our systematic design choices for robust proprioceptive odometry in challenging locomotion scenarios.

## 核心内容
Accurate proprioceptive odometry is fundamental for legged robot navigation in GPS-denied and visually degraded environments where conventional visual odometry systems fail. Current approaches face critical limitations: analytical filtering methods suffer from modeling uncertainties and cumulative drift, hybrid learning-filtering approaches remain constrained by their analytical components, while pure learning-based methods struggle with simulation-to-reality transfer and demand extensive real-world data collection. This paper introduces AutoOdom, a novel autoregressive proprioceptive odometry system that overcomes these challenges through an innovative two-stage training paradigm. Stage 1 employs large-scale simulation data to learn complex nonlinear dynamics and rapidly changing contact states inherent in legged locomotion, while Stage 2 introduces an autoregressive enhancement mechanism using limited real-world data to effectively bridge the sim-to-real gap. The key innovation lies in our autoregressive training approach, where the model learns from its own predictions to develop resilience against sensor noise and improve robustness in highly dynamic environments. Comprehensive experimental validation on the Booster T1 humanoid robot demonstrates that AutoOdom significantly outperforms state-of-the-art methods across all evaluation metrics, achieving 57.2% improvement in absolute trajectory error, 59.2% improvement in Umeyama-aligned error, and 36.2% improvement in relative pose error compared to the Legolas baseline. Extensive ablation studies provide critical insights into sensor modality selection and temporal modeling, revealing counterintuitive findings about IMU acceleration data and validating our systematic design choices for robust proprioceptive odometry in challenging locomotion scenarios.

## 参考
- http://arxiv.org/abs/2511.18857v1

