---
$id: ent_paper_cao_fastdrivevla_efficient_end_to_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning'
  zh: FastDriveVLA
  ko: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning'
summary:
  en: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning (FastDriveVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, XPeng Motors.'
  zh: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning (FastDriveVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, XPeng Motors.'
  ko: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning (FastDriveVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, XPeng Motors.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fastdrivevla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.23318v4.
sources:
- id: src_001
  type: paper
  title: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning (arXiv)'
  url: https://arxiv.org/abs/2507.23318
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FastDriveVLA source
  url: https://doi.org/10.48550/arXiv.2507.23318
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have demonstrated significant potential in complex scene understanding and action reasoning, leading to their increasing adoption in end-to-end autonomous driving systems. However, the long visual tokens of VLA models greatly increase computational costs. Current visual token pruning methods in Vision-Language Models (VLM) rely on either visual token similarity or visual-text attention, but both have shown poor performance in autonomous driving scenarios. Given that human drivers concentrate on relevant foreground areas while driving, we assert that retaining visual tokens containing this foreground information is essential for effective decision-making. Inspired by this, we propose FastDriveVLA, a novel reconstruction-based vision token pruning framework designed specifically for autonomous driving. FastDriveVLA includes a plug-and-play visual token pruner called ReconPruner, which prioritizes foreground information through MAE-style pixel reconstruction. A novel adversarial foreground-background reconstruction strategy is designed to train ReconPruner for the visual encoder of VLA models. Once trained, ReconPruner can be seamlessly applied to different VLA models with the same visual encoder without retraining. To train ReconPruner, we also introduce a large-scale dataset called nuScenes-FG, consisting of 241K image-mask pairs with annotated foreground regions. Our approach achieves state-of-the-art results on the nuScenes open-loop planning benchmark across different pruning ratios.

## 核心内容
Vision-Language-Action (VLA) models have demonstrated significant potential in complex scene understanding and action reasoning, leading to their increasing adoption in end-to-end autonomous driving systems. However, the long visual tokens of VLA models greatly increase computational costs. Current visual token pruning methods in Vision-Language Models (VLM) rely on either visual token similarity or visual-text attention, but both have shown poor performance in autonomous driving scenarios. Given that human drivers concentrate on relevant foreground areas while driving, we assert that retaining visual tokens containing this foreground information is essential for effective decision-making. Inspired by this, we propose FastDriveVLA, a novel reconstruction-based vision token pruning framework designed specifically for autonomous driving. FastDriveVLA includes a plug-and-play visual token pruner called ReconPruner, which prioritizes foreground information through MAE-style pixel reconstruction. A novel adversarial foreground-background reconstruction strategy is designed to train ReconPruner for the visual encoder of VLA models. Once trained, ReconPruner can be seamlessly applied to different VLA models with the same visual encoder without retraining. To train ReconPruner, we also introduce a large-scale dataset called nuScenes-FG, consisting of 241K image-mask pairs with annotated foreground regions. Our approach achieves state-of-the-art results on the nuScenes open-loop planning benchmark across different pruning ratios.

## 参考
- http://arxiv.org/abs/2507.23318v4

