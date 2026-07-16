---
$id: ent_paper_volumedp_modeling_volumetric_r_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VolumeDP: Modeling Volumetric Representation for Manipulation Policy Learning'
  zh: 'VolumeDP: Modeling Volumetric Representation for Manipulation Policy Learning'
  ko: 'VolumeDP: Modeling Volumetric Representation for Manipulation Policy Learning'
summary:
  en: 'arXiv:2603.17720v2 Announce Type: replace Abstract: Imitation learning is a prominent paradigm for robotic manipulation.
    However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch
    that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial
    alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention.
    It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly
    reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire
    token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single
    descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming
    the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods
    on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust
    generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available
    on the project page: https://yzc0731.github.io/VolumeDP/'
  zh: 'arXiv:2603.17720v2 Announce Type: replace Abstract: Imitation learning is a prominent paradigm for robotic manipulation.
    However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch
    that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial
    alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention.
    It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly
    reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire
    token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single
    descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming
    the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods
    on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust
    generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available
    on the project page: https://yzc0731.github.io/VolumeDP/'
  ko: 'arXiv:2603.17720v2 Announce Type: replace Abstract: Imitation learning is a prominent paradigm for robotic manipulation.
    However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch
    that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial
    alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention.
    It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly
    reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire
    token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single
    descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming
    the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods
    on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust
    generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available
    on the project page: https://yzc0731.github.io/VolumeDP/'
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
- robotics
- volumedp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.17720v2.
sources:
- id: src_001
  type: paper
  title: 'VolumeDP: Modeling Volumetric Representation for Manipulation Policy Learning (arXiv)'
  url: https://arxiv.org/abs/2603.17720
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
Imitation learning is a prominent paradigm for robotic manipulation. However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention. It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available on the project page: https://yzc0731.github.io/VolumeDP/

## 核心内容
Imitation learning is a prominent paradigm for robotic manipulation. However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention. It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available on the project page: https://yzc0731.github.io/VolumeDP/

## 参考
- http://arxiv.org/abs/2603.17720v2

