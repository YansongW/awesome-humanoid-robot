---
$id: ent_paper_egm_efficiently_learning_gener_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control'
  zh: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control'
  ko: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control'
summary:
  en: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egm
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.19043v1.
sources:
- id: src_001
  type: paper
  title: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control (arXiv)'
  url: https://arxiv.org/abs/2512.19043
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning a general motion tracking policy from human motions shows great potential for versatile humanoid whole-body control. Conventional approaches are not only inefficient in data utilization and training processes but also exhibit limited performance when tracking highly dynamic motions. To address these challenges, we propose EGM, a framework that enables efficient learning of a general motion tracking policy. EGM integrates four core designs. Firstly, we introduce a Bin-based Cross-motion Curriculum Adaptive Sampling strategy to dynamically orchestrate the sampling probabilities based on tracking error of each motion bin, eficiently balancing the training process across motions with varying dificulty and durations. The sampled data is then processed by our proposed Composite Decoupled Mixture-of-Experts (CDMoE) architecture, which efficiently enhances the ability to track motions from different distributions by grouping experts separately for upper and lower body and decoupling orthogonal experts from shared experts to separately handle dedicated features and general features. Central to our approach is a key insight we identified: for training a general motion tracking policy, data quality and diversity are paramount. Building on these designs, we develop a three-stage curriculum training flow to progressively enhance the policy's robustness against disturbances. Despite training on only 4.08 hours of data, EGM generalized robustly across 49.25 hours of test motions, outperforming baselines on both routine and highly dynamic tasks.

## 核心内容
Learning a general motion tracking policy from human motions shows great potential for versatile humanoid whole-body control. Conventional approaches are not only inefficient in data utilization and training processes but also exhibit limited performance when tracking highly dynamic motions. To address these challenges, we propose EGM, a framework that enables efficient learning of a general motion tracking policy. EGM integrates four core designs. Firstly, we introduce a Bin-based Cross-motion Curriculum Adaptive Sampling strategy to dynamically orchestrate the sampling probabilities based on tracking error of each motion bin, eficiently balancing the training process across motions with varying dificulty and durations. The sampled data is then processed by our proposed Composite Decoupled Mixture-of-Experts (CDMoE) architecture, which efficiently enhances the ability to track motions from different distributions by grouping experts separately for upper and lower body and decoupling orthogonal experts from shared experts to separately handle dedicated features and general features. Central to our approach is a key insight we identified: for training a general motion tracking policy, data quality and diversity are paramount. Building on these designs, we develop a three-stage curriculum training flow to progressively enhance the policy's robustness against disturbances. Despite training on only 4.08 hours of data, EGM generalized robustly across 49.25 hours of test motions, outperforming baselines on both routine and highly dynamic tasks.

## 参考
- http://arxiv.org/abs/2512.19043v1

