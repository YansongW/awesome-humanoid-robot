---
$id: ent_paper_learning_to_get_up_across_morp_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy'
  zh: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy'
  ko: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy'
summary:
  en: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_to_get_up_across_morp
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.12230v1.
sources:
- id: src_001
  type: paper
  title: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy (arXiv)'
  url: https://arxiv.org/abs/2512.12230
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Fall recovery is a critical skill for humanoid robots in dynamic environments such as RoboCup, where prolonged downtime often decides the match. Recent techniques using deep reinforcement learning (DRL) have produced robust get-up behaviors, yet existing methods require training of separate policies for each robot morphology. This paper presents a single DRL policy capable of recovering from falls across seven humanoid robots with diverse heights (0.48 - 0.81 m), weights (2.8 - 7.9 kg), and dynamics. Trained with CrossQ, the unified policy transfers zero-shot up to 86 +/- 7% (95% CI [81, 89]) on unseen morphologies, eliminating the need for robot-specific training. Comprehensive leave-one-out experiments, morph scaling analysis, and diversity ablations show that targeted morphological coverage improves zero-shot generalization. In some cases, the shared policy even surpasses the specialist baselines. These findings illustrate the practicality of morphology-agnostic control for fall recovery, laying the foundation for generalist humanoid control. The software is open-source and available at: https://github.com/utra-robosoccer/unified-humanoid-getup

## 核心内容
Fall recovery is a critical skill for humanoid robots in dynamic environments such as RoboCup, where prolonged downtime often decides the match. Recent techniques using deep reinforcement learning (DRL) have produced robust get-up behaviors, yet existing methods require training of separate policies for each robot morphology. This paper presents a single DRL policy capable of recovering from falls across seven humanoid robots with diverse heights (0.48 - 0.81 m), weights (2.8 - 7.9 kg), and dynamics. Trained with CrossQ, the unified policy transfers zero-shot up to 86 +/- 7% (95% CI [81, 89]) on unseen morphologies, eliminating the need for robot-specific training. Comprehensive leave-one-out experiments, morph scaling analysis, and diversity ablations show that targeted morphological coverage improves zero-shot generalization. In some cases, the shared policy even surpasses the specialist baselines. These findings illustrate the practicality of morphology-agnostic control for fall recovery, laying the foundation for generalist humanoid control. The software is open-source and available at: https://github.com/utra-robosoccer/unified-humanoid-getup

## 参考
- http://arxiv.org/abs/2512.12230v1

