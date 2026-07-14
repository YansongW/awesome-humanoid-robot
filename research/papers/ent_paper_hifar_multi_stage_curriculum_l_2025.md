---
$id: ent_paper_hifar_multi_stage_curriculum_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HiFAR: Multi-Stage Curriculum Learning for High-Dynamics Humanoid Fall Recovery'
  zh: 'HiFAR: Multi-Stage Curriculum Learning for High-Dynamics Humanoid Fall Recovery'
  ko: 'HiFAR: Multi-Stage Curriculum Learning for High-Dynamics Humanoid Fall Recovery'
summary:
  en: 'HiFAR: Multi-Stage Curriculum Learning for High-Dynamics Humanoid Fall Recovery is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'HiFAR: Multi-Stage Curriculum Learning for High-Dynamics Humanoid Fall Recovery is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'HiFAR: Multi-Stage Curriculum Learning for High-Dynamics Humanoid Fall Recovery is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hifar
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.20061v2.
sources:
- id: src_001
  type: paper
  title: 'HiFAR: Multi-Stage Curriculum Learning for High-Dynamics Humanoid Fall Recovery (arXiv)'
  url: https://arxiv.org/abs/2502.20061
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots encounter considerable difficulties in autonomously recovering from falls, especially within dynamic and unstructured environments. Conventional control methodologies are often inadequate in addressing the complexities associated with high-dimensional dynamics and the contact-rich nature of fall recovery. Meanwhile, reinforcement learning techniques are hindered by issues related to sparse rewards, intricate collision scenarios, and discrepancies between simulation and real-world applications. In this study, we introduce a multi-stage curriculum learning framework, termed HiFAR. This framework employs a staged learning approach that progressively incorporates increasingly complex and high-dimensional recovery tasks, thereby facilitating the robot's acquisition of efficient and stable fall recovery strategies. Furthermore, it enables the robot to adapt its policy to effectively manage real-world fall incidents. We assess the efficacy of the proposed method using a real humanoid robot, showcasing its capability to autonomously recover from a diverse range of falls with high success rates, rapid recovery times, robustness, and generalization.

## 核心内容
Humanoid robots encounter considerable difficulties in autonomously recovering from falls, especially within dynamic and unstructured environments. Conventional control methodologies are often inadequate in addressing the complexities associated with high-dimensional dynamics and the contact-rich nature of fall recovery. Meanwhile, reinforcement learning techniques are hindered by issues related to sparse rewards, intricate collision scenarios, and discrepancies between simulation and real-world applications. In this study, we introduce a multi-stage curriculum learning framework, termed HiFAR. This framework employs a staged learning approach that progressively incorporates increasingly complex and high-dimensional recovery tasks, thereby facilitating the robot's acquisition of efficient and stable fall recovery strategies. Furthermore, it enables the robot to adapt its policy to effectively manage real-world fall incidents. We assess the efficacy of the proposed method using a real humanoid robot, showcasing its capability to autonomously recover from a diverse range of falls with high success rates, rapid recovery times, robustness, and generalization.

## 参考
- http://arxiv.org/abs/2502.20061v2

