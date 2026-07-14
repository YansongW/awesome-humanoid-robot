---
$id: ent_paper_yuan_autodrive_r2_incentivizing_rea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving'
  zh: AutoDrive-R2
  ko: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving'
summary:
  en: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving (AutoDrive-R2),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by AMAP, Alibaba Group, University of
    Queensland, Lanzhou University, Case Western Reserve University.'
  zh: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving (AutoDrive-R2),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by AMAP, Alibaba Group, University of
    Queensland, Lanzhou University, Case Western Reserve University.'
  ko: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving (AutoDrive-R2),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by AMAP, Alibaba Group, University of
    Queensland, Lanzhou University, Case Western Reserve University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- autodrive_r2
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.01944v3.
sources:
- id: src_001
  type: paper
  title: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2509.01944
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AutoDrive-R2 source
  url: https://doi.org/10.48550/arXiv.2509.01944
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models in autonomous driving systems have recently demonstrated transformative potential by integrating multimodal perception with decision-making capabilities. However, the interpretability and coherence of the decision process and the plausibility of action sequences remain largely underexplored. To address these issues, we propose AutoDrive-R$^2$, a novel VLA framework that enhances both reasoning and self-reflection capabilities of autonomous driving systems through chain-of-thought (CoT) processing and reinforcement learning (RL). Specifically, we first propose an innovative CoT dataset named nuScenesR$^2$-6K for supervised fine-tuning, which effectively builds cognitive bridges between input information and output trajectories through a four-step logical chain with self-reflection for validation. Moreover, to maximize both reasoning and self-reflection during the RL stage, we further employ the Group Relative Policy Optimization (GRPO) algorithm within a physics-grounded reward framework that incorporates spatial alignment, vehicle dynamic, and temporal smoothness criteria to ensure reliable and realistic trajectory planning. Extensive evaluation results across both nuScenes and Waymo datasets demonstrates the state-of-the-art performance and robust generalization capacity of our proposed method.

## 核心内容
Vision-Language-Action (VLA) models in autonomous driving systems have recently demonstrated transformative potential by integrating multimodal perception with decision-making capabilities. However, the interpretability and coherence of the decision process and the plausibility of action sequences remain largely underexplored. To address these issues, we propose AutoDrive-R$^2$, a novel VLA framework that enhances both reasoning and self-reflection capabilities of autonomous driving systems through chain-of-thought (CoT) processing and reinforcement learning (RL). Specifically, we first propose an innovative CoT dataset named nuScenesR$^2$-6K for supervised fine-tuning, which effectively builds cognitive bridges between input information and output trajectories through a four-step logical chain with self-reflection for validation. Moreover, to maximize both reasoning and self-reflection during the RL stage, we further employ the Group Relative Policy Optimization (GRPO) algorithm within a physics-grounded reward framework that incorporates spatial alignment, vehicle dynamic, and temporal smoothness criteria to ensure reliable and realistic trajectory planning. Extensive evaluation results across both nuScenes and Waymo datasets demonstrates the state-of-the-art performance and robust generalization capacity of our proposed method.

## 参考
- http://arxiv.org/abs/2509.01944v3

