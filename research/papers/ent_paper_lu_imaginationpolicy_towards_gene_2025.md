---
$id: ent_paper_lu_imaginationpolicy_towards_gene_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation'
  zh: ImaginationPolicy
  ko: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation'
summary:
  en: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation (ImaginationPolicy),
    is a 2025 large vision-language-action model for robotic manipulation.'
  zh: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation (ImaginationPolicy),
    is a 2025 large vision-language-action model for robotic manipulation.'
  ko: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation (ImaginationPolicy),
    is a 2025 large vision-language-action model for robotic manipulation.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- imaginationpolicy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20841v1.
sources:
- id: src_001
  type: paper
  title: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.20841
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ImaginationPolicy source
  url: https://doi.org/10.48550/arXiv.2509.20841
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
End-to-end robot manipulation policies offer significant potential for enabling embodied agents to understand and interact with the world. Unlike traditional modular pipelines, end-to-end learning mitigates key limitations such as information loss between modules and feature misalignment caused by isolated optimization targets. Despite these advantages, existing end-to-end neural networks for robotic manipulation--including those based on large VLM/VLA models--remain insufficiently performant for large-scale practical deployment. In this paper, we take a step towards an end-to-end manipulation policy that is generalizable, accurate and reliable. To achieve this goal, we propose a novel Chain of Moving Oriented Keypoints (CoMOK) formulation for robotic manipulation. Our formulation is used as the action representation of a neural policy, which can be trained in an end-to-end fashion. Such an action representation is general, as it extends the standard end-effector pose action representation and supports a diverse set of manipulation tasks in a unified manner. The oriented keypoint in our method enables natural generalization to objects with different shapes and sizes, while achieving sub-centimeter accuracy. Moreover, our formulation can easily handle multi-stage tasks, multi-modal robot behaviors, and deformable objects. Extensive simulated and hardware experiments demonstrate the effectiveness of our method.

## 核心内容
End-to-end robot manipulation policies offer significant potential for enabling embodied agents to understand and interact with the world. Unlike traditional modular pipelines, end-to-end learning mitigates key limitations such as information loss between modules and feature misalignment caused by isolated optimization targets. Despite these advantages, existing end-to-end neural networks for robotic manipulation--including those based on large VLM/VLA models--remain insufficiently performant for large-scale practical deployment. In this paper, we take a step towards an end-to-end manipulation policy that is generalizable, accurate and reliable. To achieve this goal, we propose a novel Chain of Moving Oriented Keypoints (CoMOK) formulation for robotic manipulation. Our formulation is used as the action representation of a neural policy, which can be trained in an end-to-end fashion. Such an action representation is general, as it extends the standard end-effector pose action representation and supports a diverse set of manipulation tasks in a unified manner. The oriented keypoint in our method enables natural generalization to objects with different shapes and sizes, while achieving sub-centimeter accuracy. Moreover, our formulation can easily handle multi-stage tasks, multi-modal robot behaviors, and deformable objects. Extensive simulated and hardware experiments demonstrate the effectiveness of our method.

## 参考
- http://arxiv.org/abs/2509.20841v1

