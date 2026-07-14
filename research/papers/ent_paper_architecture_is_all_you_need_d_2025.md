---
$id: ent_paper_architecture_is_all_you_need_d_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion'
  zh: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion'
  ko: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion'
summary:
  en: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- architecture_is_all_you_need
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14947v2.
sources:
- id: src_001
  type: paper
  title: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2510.14947
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robust humanoid locomotion in unstructured environments requires architectures that balance fast low-level stabilization with slower perceptual decision-making. We show that a simple layered control architecture (LCA), a proprioceptive stabilizer running at high rate, coupled with a compact low-rate perceptual policy, enables substantially more robust performance than monolithic end-to-end designs, even when using minimal perception encoders. Through a two-stage training curriculum (blind stabilizer pretraining followed by perceptual fine-tuning), we demonstrate that layered policies consistently outperform one-stage alternatives in both simulation and hardware. On a Unitree G1 humanoid, our approach succeeds across stair and ledge tasks where one-stage perceptual policies fail. These results highlight that architectural separation of timescales, rather than network scale or complexity, is the key enabler for robust perception-conditioned locomotion.

## 核心内容
Robust humanoid locomotion in unstructured environments requires architectures that balance fast low-level stabilization with slower perceptual decision-making. We show that a simple layered control architecture (LCA), a proprioceptive stabilizer running at high rate, coupled with a compact low-rate perceptual policy, enables substantially more robust performance than monolithic end-to-end designs, even when using minimal perception encoders. Through a two-stage training curriculum (blind stabilizer pretraining followed by perceptual fine-tuning), we demonstrate that layered policies consistently outperform one-stage alternatives in both simulation and hardware. On a Unitree G1 humanoid, our approach succeeds across stair and ledge tasks where one-stage perceptual policies fail. These results highlight that architectural separation of timescales, rather than network scale or complexity, is the key enabler for robust perception-conditioned locomotion.

## 参考
- http://arxiv.org/abs/2510.14947v2

