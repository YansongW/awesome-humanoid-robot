---
$id: ent_paper_bai_learning_to_see_and_act_task_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation'
  zh: TVVE
  ko: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation'
summary:
  en: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation (TVVE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University, Pengcheng Laboratory, Nanyang Technological University,
    Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, X-Era AI Lab.'
  zh: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation (TVVE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University, Pengcheng Laboratory, Nanyang Technological University,
    Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, X-Era AI Lab.'
  ko: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation (TVVE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University, Pengcheng Laboratory, Nanyang Technological University,
    Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, X-Era AI Lab.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- tvve
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.05186v5.
sources:
- id: src_001
  type: paper
  title: 'Learning to See and Act: Task-Aware Virtual View Exploration for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2508.05186
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent vision-language-action (VLA) models for multi-task robot manipulation often rely on fixed camera setups and shared visual encoders, which limit their performance under occlusions and during cross-task transfer. To address these challenges, we propose Task-aware Virtual View Exploration (TVVE), a framework that learns to select task-relevant virtual camera viewpoints and dynamically re-render observations from a reconstructed scene representation using the selected viewpoints. To enable efficient view selection, we train an exploration policy in a pseudo-environment. In addition, we introduce a Task-aware Mixture-of-Experts (TaskMoE) visual encoder that routes visual features to task-specialized experts, mitigating interference in multi-task learning. To evaluate robustness under distribution shifts, we construct RLBench-OG, an out-of-distribution benchmark with visual perturbations and camera pose variations. Experiments on RLBench and RLBench-OG demonstrate that TVVE achieves higher success rates than strong baselines, while real-robot experiments further confirm its robustness to visual disturbances and unseen instructions. Code and visualizations are available at: https://hcplab-sysu.github.io/TAVP.

## 核心内容
Recent vision-language-action (VLA) models for multi-task robot manipulation often rely on fixed camera setups and shared visual encoders, which limit their performance under occlusions and during cross-task transfer. To address these challenges, we propose Task-aware Virtual View Exploration (TVVE), a framework that learns to select task-relevant virtual camera viewpoints and dynamically re-render observations from a reconstructed scene representation using the selected viewpoints. To enable efficient view selection, we train an exploration policy in a pseudo-environment. In addition, we introduce a Task-aware Mixture-of-Experts (TaskMoE) visual encoder that routes visual features to task-specialized experts, mitigating interference in multi-task learning. To evaluate robustness under distribution shifts, we construct RLBench-OG, an out-of-distribution benchmark with visual perturbations and camera pose variations. Experiments on RLBench and RLBench-OG demonstrate that TVVE achieves higher success rates than strong baselines, while real-robot experiments further confirm its robustness to visual disturbances and unseen instructions. Code and visualizations are available at: https://hcplab-sysu.github.io/TAVP.

## 参考
- http://arxiv.org/abs/2508.05186v5

