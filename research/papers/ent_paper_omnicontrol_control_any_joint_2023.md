---
$id: ent_paper_omnicontrol_control_any_joint_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation'
  zh: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation'
  ko: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation'
summary:
  en: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation is a 2023 work on human motion analysis and
    synthesis for humanoid robots.'
  zh: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation is a 2023 work on human motion analysis and
    synthesis for humanoid robots.'
  ko: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation is a 2023 work on human motion analysis and
    synthesis for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- omnicontrol
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.08580v2.
sources:
- id: src_001
  type: paper
  title: 'OmniControl: Control Any Joint at Any Time for Human Motion Generation (arXiv)'
  url: https://arxiv.org/abs/2310.08580
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We present a novel approach named OmniControl for incorporating flexible spatial control signals into a text-conditioned human motion generation model based on the diffusion process. Unlike previous methods that can only control the pelvis trajectory, OmniControl can incorporate flexible spatial control signals over different joints at different times with only one model. Specifically, we propose analytic spatial guidance that ensures the generated motion can tightly conform to the input control signals. At the same time, realism guidance is introduced to refine all the joints to generate more coherent motion. Both the spatial and realism guidance are essential and they are highly complementary for balancing control accuracy and motion realism. By combining them, OmniControl generates motions that are realistic, coherent, and consistent with the spatial constraints. Experiments on HumanML3D and KIT-ML datasets show that OmniControl not only achieves significant improvement over state-of-the-art methods on pelvis control but also shows promising results when incorporating the constraints over other joints.

## 核心内容
We present a novel approach named OmniControl for incorporating flexible spatial control signals into a text-conditioned human motion generation model based on the diffusion process. Unlike previous methods that can only control the pelvis trajectory, OmniControl can incorporate flexible spatial control signals over different joints at different times with only one model. Specifically, we propose analytic spatial guidance that ensures the generated motion can tightly conform to the input control signals. At the same time, realism guidance is introduced to refine all the joints to generate more coherent motion. Both the spatial and realism guidance are essential and they are highly complementary for balancing control accuracy and motion realism. By combining them, OmniControl generates motions that are realistic, coherent, and consistent with the spatial constraints. Experiments on HumanML3D and KIT-ML datasets show that OmniControl not only achieves significant improvement over state-of-the-art methods on pelvis control but also shows promising results when incorporating the constraints over other joints.

## 参考
- http://arxiv.org/abs/2310.08580v2

