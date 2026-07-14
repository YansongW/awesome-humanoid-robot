---
$id: ent_paper_zheng_flare_robot_learning_with_impl_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FLARE: Robot Learning with Implicit World Modeling'
  zh: FLARE
  ko: 'FLARE: Robot Learning with Implicit World Modeling'
summary:
  en: 'FLARE: Robot Learning with Implicit World Modeling (FLARE), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by California Institute of Technology, and published at CoRL25.'
  zh: 'FLARE: Robot Learning with Implicit World Modeling (FLARE), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by California Institute of Technology, and published at CoRL25.'
  ko: 'FLARE: Robot Learning with Implicit World Modeling (FLARE), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by California Institute of Technology, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flare
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.15659v1.
sources:
- id: src_001
  type: paper
  title: 'FLARE: Robot Learning with Implicit World Modeling (arXiv)'
  url: https://arxiv.org/abs/2505.15659
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FLARE source
  url: https://doi.org/10.48550/arXiv.2505.15659
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce $\textbf{F}$uture $\textbf{LA}$tent $\textbf{RE}$presentation Alignment ($\textbf{FLARE}$), a novel framework that integrates predictive latent world modeling into robot policy learning. By aligning features from a diffusion transformer with latent embeddings of future observations, $\textbf{FLARE}$ enables a diffusion transformer policy to anticipate latent representations of future observations, allowing it to reason about long-term consequences while generating actions. Remarkably lightweight, $\textbf{FLARE}$ requires only minimal architectural modifications -- adding a few tokens to standard vision-language-action (VLA) models -- yet delivers substantial performance gains. Across two challenging multitask simulation imitation learning benchmarks spanning single-arm and humanoid tabletop manipulation, $\textbf{FLARE}$ achieves state-of-the-art performance, outperforming prior policy learning baselines by up to 26%. Moreover, $\textbf{FLARE}$ unlocks the ability to co-train with human egocentric video demonstrations without action labels, significantly boosting policy generalization to a novel object with unseen geometry with as few as a single robot demonstration. Our results establish $\textbf{FLARE}$ as a general and scalable approach for combining implicit world modeling with high-frequency robotic control.

## 核心内容
We introduce $\textbf{F}$uture $\textbf{LA}$tent $\textbf{RE}$presentation Alignment ($\textbf{FLARE}$), a novel framework that integrates predictive latent world modeling into robot policy learning. By aligning features from a diffusion transformer with latent embeddings of future observations, $\textbf{FLARE}$ enables a diffusion transformer policy to anticipate latent representations of future observations, allowing it to reason about long-term consequences while generating actions. Remarkably lightweight, $\textbf{FLARE}$ requires only minimal architectural modifications -- adding a few tokens to standard vision-language-action (VLA) models -- yet delivers substantial performance gains. Across two challenging multitask simulation imitation learning benchmarks spanning single-arm and humanoid tabletop manipulation, $\textbf{FLARE}$ achieves state-of-the-art performance, outperforming prior policy learning baselines by up to 26%. Moreover, $\textbf{FLARE}$ unlocks the ability to co-train with human egocentric video demonstrations without action labels, significantly boosting policy generalization to a novel object with unseen geometry with as few as a single robot demonstration. Our results establish $\textbf{FLARE}$ as a general and scalable approach for combining implicit world modeling with high-frequency robotic control.

## 参考
- http://arxiv.org/abs/2505.15659v1

