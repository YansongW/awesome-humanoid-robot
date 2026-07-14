---
$id: ent_paper_deep_whole_body_parkour_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Deep Whole-body Parkour
  zh: 全身动作必须理解环境几何
  ko: Deep Whole-body Parkour
summary:
  en: Deep Whole-body Parkour is a knowledge node related to paper in the humanoid robot value chain.
  zh: 'Current approaches to humanoid control generally fall into two paradigms: perceptive locomotion, which handles terrain
    well but is limited to pedal gaits, and general motion tracking, which reproduces complex skills but ignores environmental
    capabilities. This work unites these paradigms to achieve perceptive general motion control. We present a framework where
    exteroceptive sensing is integrated into whole-body motion tracking, permitting a humanoid to perform highly dynamic,
    non-locomotion tasks on uneven terrain. By training a single policy to perform multiple distinct motions across varied
    terrestrial features, we demonstrate the non-trivial benefit of integrating perception into the control loop. Our results
    show that this framework enables robust, highly dynamic multi-contact motions'
  ko: Deep Whole-body Parkour is a knowledge node related to paper in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.07701v1.
sources:
- id: src_001
  type: paper
  title: Deep Whole-body Parkour (arXiv)
  url: https://arxiv.org/abs/2601.07701
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 全身动作必须理解环境几何 project page
  url: https://project-instinct.github.io/deep-whole-body-parkour
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Current approaches to humanoid control generally fall into two paradigms: perceptive locomotion, which handles terrain well but is limited to pedal gaits, and general motion tracking, which reproduces complex skills but ignores environmental capabilities. This work unites these paradigms to achieve perceptive general motion control. We present a framework where exteroceptive sensing is integrated into whole-body motion tracking, permitting a humanoid to perform highly dynamic, non-locomotion tasks on uneven terrain. By training a single policy to perform multiple distinct motions across varied terrestrial features, we demonstrate the non-trivial benefit of integrating perception into the control loop. Our results show that this framework enables robust, highly dynamic multi-contact motions, such as vaulting and dive-rolling, on unstructured terrain, significantly expanding the robot's traversability beyond simple walking or running. https://project-instinct.github.io/deep-whole-body-parkour

## 核心内容
Current approaches to humanoid control generally fall into two paradigms: perceptive locomotion, which handles terrain well but is limited to pedal gaits, and general motion tracking, which reproduces complex skills but ignores environmental capabilities. This work unites these paradigms to achieve perceptive general motion control. We present a framework where exteroceptive sensing is integrated into whole-body motion tracking, permitting a humanoid to perform highly dynamic, non-locomotion tasks on uneven terrain. By training a single policy to perform multiple distinct motions across varied terrestrial features, we demonstrate the non-trivial benefit of integrating perception into the control loop. Our results show that this framework enables robust, highly dynamic multi-contact motions, such as vaulting and dive-rolling, on unstructured terrain, significantly expanding the robot's traversability beyond simple walking or running. https://project-instinct.github.io/deep-whole-body-parkour

## 参考
- http://arxiv.org/abs/2601.07701v1

