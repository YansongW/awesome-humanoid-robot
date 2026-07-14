---
$id: ent_paper_humanoidvlm_vision_language_gu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation'
  zh: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation'
  ko: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation'
summary:
  en: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation is a 2026 work on manipulation
    for humanoid robots.'
  zh: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation is a 2026 work on manipulation
    for humanoid robots.'
  ko: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation is a 2026 work on manipulation
    for humanoid robots.'
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
- humanoidvlm
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.14874v1.
sources:
- id: src_001
  type: paper
  title: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation (arXiv)'
  url: https://arxiv.org/abs/2601.14874
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots must adapt their contact behavior to diverse objects and tasks, yet most controllers rely on fixed, hand-tuned impedance gains and gripper settings. This paper introduces HumanoidVLM, a vision-language driven retrieval framework that enables the Unitree G1 humanoid to select task-appropriate Cartesian impedance parameters and gripper configurations directly from an egocentric RGB image. The system couples a vision-language model for semantic task inference with a FAISS-based Retrieval-Augmented Generation (RAG) module that retrieves experimentally validated stiffness-damping pairs and object-specific grasp angles from two custom databases, and executes them through a task-space impedance controller for compliant manipulation. We evaluate HumanoidVLM on 14 visual scenarios and achieve a retrieval accuracy of 93%. Real-world experiments show stable interaction dynamics, with z-axis tracking errors typically within 1-3.5 cm and virtual forces consistent with task-dependent impedance settings. These results demonstrate the feasibility of linking semantic perception with retrieval-based control as an interpretable path toward adaptive humanoid manipulation.

## 核心内容
Humanoid robots must adapt their contact behavior to diverse objects and tasks, yet most controllers rely on fixed, hand-tuned impedance gains and gripper settings. This paper introduces HumanoidVLM, a vision-language driven retrieval framework that enables the Unitree G1 humanoid to select task-appropriate Cartesian impedance parameters and gripper configurations directly from an egocentric RGB image. The system couples a vision-language model for semantic task inference with a FAISS-based Retrieval-Augmented Generation (RAG) module that retrieves experimentally validated stiffness-damping pairs and object-specific grasp angles from two custom databases, and executes them through a task-space impedance controller for compliant manipulation. We evaluate HumanoidVLM on 14 visual scenarios and achieve a retrieval accuracy of 93%. Real-world experiments show stable interaction dynamics, with z-axis tracking errors typically within 1-3.5 cm and virtual forces consistent with task-dependent impedance settings. These results demonstrate the feasibility of linking semantic perception with retrieval-based control as an interpretable path toward adaptive humanoid manipulation.

## 参考
- http://arxiv.org/abs/2601.14874v1

