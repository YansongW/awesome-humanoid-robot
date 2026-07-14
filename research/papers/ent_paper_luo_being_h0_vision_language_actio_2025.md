---
$id: ent_paper_luo_being_h0_vision_language_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos'
  zh: Being-H0
  ko: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos'
summary:
  en: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (Being-H0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Renmin University of China, BeingBeyond.'
  zh: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (Being-H0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Renmin University of China, BeingBeyond.'
  ko: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (Being-H0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Renmin University of China, BeingBeyond.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- being_h0
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.15597v1.
sources:
- id: src_001
  type: paper
  title: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (arXiv)'
  url: https://arxiv.org/abs/2507.15597
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Being-H0 source
  url: https://doi.org/10.48550/arXiv.2507.15597
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce Being-H0, a dexterous Vision-Language-Action model (VLA) trained on large-scale human videos. Existing VLAs struggle with complex manipulation tasks requiring high dexterity and generalize poorly to novel scenarios and tasks, primarily due to their reliance on synthetic data with significant sim-to-real gaps or teleoperated demonstrations lacking scale and diversity. To address this data bottleneck, we propose leveraging human hands as a foundation manipulator, capitalizing on the rich dexterity and scalability present in web data. Our approach centers on physical instruction tuning, a novel training paradigm that combines large-scale VLA pretraining from human videos, physical space alignment for 3D reasoning, and post-training adaptation for robotic tasks. Additionally, we introduce a part-level motion tokenization method which achieves millimeter-level reconstruction accuracy to model precise hand trajectories for action learning. To support our proposed paradigm, we further develop a comprehensive data curation pipeline that integrates heterogeneous sources -- including motion capture, VR, and RGB-only videos -- into a large-scale dataset with millions of motion-based instructional instances. We empirically show the excellence of Being-H0 in hand motion generation and instruction following, and it also scales well with model and data sizes. Importantly, we observe the expected gains of Being-H0 in real-world robotic manipulation as physical instruction tuning is applied. More details are available at https://beingbeyond.github.io/Being-H0.

## 核心内容
We introduce Being-H0, a dexterous Vision-Language-Action model (VLA) trained on large-scale human videos. Existing VLAs struggle with complex manipulation tasks requiring high dexterity and generalize poorly to novel scenarios and tasks, primarily due to their reliance on synthetic data with significant sim-to-real gaps or teleoperated demonstrations lacking scale and diversity. To address this data bottleneck, we propose leveraging human hands as a foundation manipulator, capitalizing on the rich dexterity and scalability present in web data. Our approach centers on physical instruction tuning, a novel training paradigm that combines large-scale VLA pretraining from human videos, physical space alignment for 3D reasoning, and post-training adaptation for robotic tasks. Additionally, we introduce a part-level motion tokenization method which achieves millimeter-level reconstruction accuracy to model precise hand trajectories for action learning. To support our proposed paradigm, we further develop a comprehensive data curation pipeline that integrates heterogeneous sources -- including motion capture, VR, and RGB-only videos -- into a large-scale dataset with millions of motion-based instructional instances. We empirically show the excellence of Being-H0 in hand motion generation and instruction following, and it also scales well with model and data sizes. Importantly, we observe the expected gains of Being-H0 in real-world robotic manipulation as physical instruction tuning is applied. More details are available at https://beingbeyond.github.io/Being-H0.

## 参考
- http://arxiv.org/abs/2507.15597v1

