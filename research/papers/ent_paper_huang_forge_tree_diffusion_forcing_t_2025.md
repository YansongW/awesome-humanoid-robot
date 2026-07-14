---
$id: ent_paper_huang_forge_tree_diffusion_forcing_t_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation'
  zh: FORGE-Tree
  ko: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation'
summary:
  en: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation (FORGE-Tree), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology.'
  zh: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation (FORGE-Tree), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology.'
  ko: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation (FORGE-Tree), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- forge_tree
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.21744v1.
sources:
- id: src_001
  type: paper
  title: 'FORGE-Tree: Diffusion-Forcing Tree Search for Long-Horizon Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2510.21744
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FORGE-Tree source
  url: https://doi.org/10.48550/arXiv.2510.21744
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Long-horizon robot manipulation tasks remain challenging for Vision-Language-Action (VLA) policies due to drift and exposure bias, often denoise the entire trajectory with fixed hyperparameters, causing small geometric errors to compound across stages and offering no mechanism to allocate extra test-time compute where clearances are tight. To address these challenges, we introduce FORGE-Tree, a plug-in control layer that couples a stage-aligned Diffusion Forcing (DF) head with test-time Monte Carlo Tree Diffusion (MCTD). With a frozen VLA encoder, DF aligns timesteps to subtask stages; during inference we partially denoise only a target segment while keeping other tokens frozen, turning trajectory refinement into a sequence of local edits. We then apply Monte Carlo Tree Diffusion to select the next segment to refine. A scene graph supplies priors for expansion and geometry relation-aware scoring for rollouts, yielding tree-structured denoising whose performance scales with search budget while preserving the executed prefix. Evaluation on LIBERO, FORGE-Tree improves success rate by 13.4 to 17.2 pp over the native VLA baselines with both OpenVLA and Octo-Base. Gains remain consistent under comparable compute budgets, especially on long-horizon variants. Videos available at: https://taco-group.github.io/FORGE-Tree/

## 核心内容
Long-horizon robot manipulation tasks remain challenging for Vision-Language-Action (VLA) policies due to drift and exposure bias, often denoise the entire trajectory with fixed hyperparameters, causing small geometric errors to compound across stages and offering no mechanism to allocate extra test-time compute where clearances are tight. To address these challenges, we introduce FORGE-Tree, a plug-in control layer that couples a stage-aligned Diffusion Forcing (DF) head with test-time Monte Carlo Tree Diffusion (MCTD). With a frozen VLA encoder, DF aligns timesteps to subtask stages; during inference we partially denoise only a target segment while keeping other tokens frozen, turning trajectory refinement into a sequence of local edits. We then apply Monte Carlo Tree Diffusion to select the next segment to refine. A scene graph supplies priors for expansion and geometry relation-aware scoring for rollouts, yielding tree-structured denoising whose performance scales with search budget while preserving the executed prefix. Evaluation on LIBERO, FORGE-Tree improves success rate by 13.4 to 17.2 pp over the native VLA baselines with both OpenVLA and Octo-Base. Gains remain consistent under comparable compute budgets, especially on long-horizon variants. Videos available at: https://taco-group.github.io/FORGE-Tree/

## 参考
- http://arxiv.org/abs/2510.21744v1

