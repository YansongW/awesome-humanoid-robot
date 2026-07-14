---
$id: ent_paper_li_posa_vla_enhancing_action_gene_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention'
  zh: PosA-VLA
  ko: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention'
summary:
  en: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention (PosA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Sydney.'
  zh: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention (PosA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Sydney.'
  ko: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention (PosA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Sydney.'
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
- posa_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.03724v2.
sources:
- id: src_001
  type: paper
  title: 'PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention (arXiv)'
  url: https://arxiv.org/abs/2512.03724
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: PosA-VLA source
  url: https://doi.org/10.48550/arXiv.2512.03724
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The Vision-Language-Action (VLA) models have demonstrated remarkable performance on embodied tasks and shown promising potential for real-world applications. However, current VLAs still struggle to produce consistent and precise target-oriented actions, as they often generate redundant or unstable motions along trajectories, limiting their applicability in time-sensitive scenarios.In this work, we attribute these redundant actions to the spatially uniform perception field of existing VLAs, which causes them to be distracted by target-irrelevant objects, especially in complex environments.To address this issue, we propose an efficient PosA-VLA framework that anchors visual attention via pose-conditioned supervision, consistently guiding the model's perception toward task-relevant regions. The pose-conditioned anchor attention mechanism enables the model to better align instruction semantics with actionable visual cues, thereby improving action generation precision and efficiency. Moreover, our framework adopts a lightweight architecture and requires no auxiliary perception modules (e.g., segmentation or grounding networks), ensuring efficient inference. Extensive experiments verify that our method executes embodied tasks with precise and time-efficient behavior across diverse robotic manipulation benchmarks and shows robust generalization in a variety of challenging environments.

## 核心内容
The Vision-Language-Action (VLA) models have demonstrated remarkable performance on embodied tasks and shown promising potential for real-world applications. However, current VLAs still struggle to produce consistent and precise target-oriented actions, as they often generate redundant or unstable motions along trajectories, limiting their applicability in time-sensitive scenarios.In this work, we attribute these redundant actions to the spatially uniform perception field of existing VLAs, which causes them to be distracted by target-irrelevant objects, especially in complex environments.To address this issue, we propose an efficient PosA-VLA framework that anchors visual attention via pose-conditioned supervision, consistently guiding the model's perception toward task-relevant regions. The pose-conditioned anchor attention mechanism enables the model to better align instruction semantics with actionable visual cues, thereby improving action generation precision and efficiency. Moreover, our framework adopts a lightweight architecture and requires no auxiliary perception modules (e.g., segmentation or grounding networks), ensuring efficient inference. Extensive experiments verify that our method executes embodied tasks with precise and time-efficient behavior across diverse robotic manipulation benchmarks and shows robust generalization in a variety of challenging environments.

## 参考
- http://arxiv.org/abs/2512.03724v2

