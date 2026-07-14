---
$id: ent_paper_flam_foundation_model_based_bo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation'
  zh: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation'
  ko: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation'
summary:
  en: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation is a 2025 work on loco-manipulation
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
- flam
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.22249v1.
sources:
- id: src_001
  type: paper
  title: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation (arXiv)'
  url: https://arxiv.org/abs/2503.22249
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have attracted significant attention in recent years. Reinforcement Learning (RL) is one of the main ways to control the whole body of humanoid robots. RL enables agents to complete tasks by learning from environment interactions, guided by task rewards. However, existing RL methods rarely explicitly consider the impact of body stability on humanoid locomotion and manipulation. Achieving high performance in whole-body control remains a challenge for RL methods that rely solely on task rewards. In this paper, we propose a Foundation model-based method for humanoid Locomotion And Manipulation (FLAM for short). FLAM integrates a stabilizing reward function with a basic policy. The stabilizing reward function is designed to encourage the robot to learn stable postures, thereby accelerating the learning process and facilitating task completion. Specifically, the robot pose is first mapped to the 3D virtual human model. Then, the human pose is stabilized and reconstructed through a human motion reconstruction model. Finally, the pose before and after reconstruction is used to compute the stabilizing reward. By combining this stabilizing reward with the task reward, FLAM effectively guides policy learning. Experimental results on a humanoid robot benchmark demonstrate that FLAM outperforms state-of-the-art RL methods, highlighting its effectiveness in improving stability and overall performance.

## 核心内容
Humanoid robots have attracted significant attention in recent years. Reinforcement Learning (RL) is one of the main ways to control the whole body of humanoid robots. RL enables agents to complete tasks by learning from environment interactions, guided by task rewards. However, existing RL methods rarely explicitly consider the impact of body stability on humanoid locomotion and manipulation. Achieving high performance in whole-body control remains a challenge for RL methods that rely solely on task rewards. In this paper, we propose a Foundation model-based method for humanoid Locomotion And Manipulation (FLAM for short). FLAM integrates a stabilizing reward function with a basic policy. The stabilizing reward function is designed to encourage the robot to learn stable postures, thereby accelerating the learning process and facilitating task completion. Specifically, the robot pose is first mapped to the 3D virtual human model. Then, the human pose is stabilized and reconstructed through a human motion reconstruction model. Finally, the pose before and after reconstruction is used to compute the stabilizing reward. By combining this stabilizing reward with the task reward, FLAM effectively guides policy learning. Experimental results on a humanoid robot benchmark demonstrate that FLAM outperforms state-of-the-art RL methods, highlighting its effectiveness in improving stability and overall performance.

## 参考
- http://arxiv.org/abs/2503.22249v1

