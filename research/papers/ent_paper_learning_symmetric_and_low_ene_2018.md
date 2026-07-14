---
$id: ent_paper_learning_symmetric_and_low_ene_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Symmetric and Low-energy Locomotion
  zh: Learning Symmetric and Low-energy Locomotion
  ko: Learning Symmetric and Low-energy Locomotion
summary:
  en: Learning Symmetric and Low-energy Locomotion is a 2018 work on physics-based character animation for humanoid robots.
  zh: Learning Symmetric and Low-energy Locomotion is a 2018 work on physics-based character animation for humanoid robots.
  ko: Learning Symmetric and Low-energy Locomotion is a 2018 work on physics-based character animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- learning_symmetric_and_low_ene
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1801.08093v3.
sources:
- id: src_001
  type: paper
  title: Learning Symmetric and Low-energy Locomotion (arXiv)
  url: https://arxiv.org/abs/1801.08093
  date: '2018'
  accessed_at: '2026-07-01'
---
## 概述
Learning locomotion skills is a challenging problem. To generate realistic and smooth locomotion, existing methods use motion capture, finite state machines or morphology-specific knowledge to guide the motion generation algorithms. Deep reinforcement learning (DRL) is a promising approach for the automatic creation of locomotion control. Indeed, a standard benchmark for DRL is to automatically create a running controller for a biped character from a simple reward function. Although several different DRL algorithms can successfully create a running controller, the resulting motions usually look nothing like a real runner. This paper takes a minimalist learning approach to the locomotion problem, without the use of motion examples, finite state machines, or morphology-specific knowledge. We introduce two modifications to the DRL approach that, when used together, produce locomotion behaviors that are symmetric, low-energy, and much closer to that of a real person. First, we introduce a new term to the loss function (not the reward function) that encourages symmetric actions. Second, we introduce a new curriculum learning method that provides modulated physical assistance to help the character with left/right balance and forward movement. The algorithm automatically computes appropriate assistance to the character and gradually relaxes this assistance, so that eventually the character learns to move entirely without help. Because our method does not make use of motion capture data, it can be applied to a variety of character morphologies. We demonstrate locomotion controllers for the lower half of a biped, a full humanoid, a quadruped, and a hexapod. Our results show that learned policies are able to produce symmetric, low-energy gaits. In addition, speed-appropriate gait patterns emerge without any guidance from motion examples or contact planning.

## 核心内容
Learning locomotion skills is a challenging problem. To generate realistic and smooth locomotion, existing methods use motion capture, finite state machines or morphology-specific knowledge to guide the motion generation algorithms. Deep reinforcement learning (DRL) is a promising approach for the automatic creation of locomotion control. Indeed, a standard benchmark for DRL is to automatically create a running controller for a biped character from a simple reward function. Although several different DRL algorithms can successfully create a running controller, the resulting motions usually look nothing like a real runner. This paper takes a minimalist learning approach to the locomotion problem, without the use of motion examples, finite state machines, or morphology-specific knowledge. We introduce two modifications to the DRL approach that, when used together, produce locomotion behaviors that are symmetric, low-energy, and much closer to that of a real person. First, we introduce a new term to the loss function (not the reward function) that encourages symmetric actions. Second, we introduce a new curriculum learning method that provides modulated physical assistance to help the character with left/right balance and forward movement. The algorithm automatically computes appropriate assistance to the character and gradually relaxes this assistance, so that eventually the character learns to move entirely without help. Because our method does not make use of motion capture data, it can be applied to a variety of character morphologies. We demonstrate locomotion controllers for the lower half of a biped, a full humanoid, a quadruped, and a hexapod. Our results show that learned policies are able to produce symmetric, low-energy gaits. In addition, speed-appropriate gait patterns emerge without any guidance from motion examples or contact planning.

## 参考
- http://arxiv.org/abs/1801.08093v3

