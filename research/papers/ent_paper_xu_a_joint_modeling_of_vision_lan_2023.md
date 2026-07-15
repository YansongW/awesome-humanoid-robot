---
$id: ent_paper_xu_a_joint_modeling_of_vision_lan_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter
  zh: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter
  ko: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter
summary:
  en: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter (A Joint Modeling of Vision-Language-Action
    for Target-oriented Grasping in Clutter), is a 2023 large vision-language-action model for robotic manipulation, introduced
    by Zhejiang University, and published at ICRA23.
  zh: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter (A Joint Modeling of Vision-Language-Action
    for Target-oriented Grasping in Clutter), is a 2023 large vision-language-action model for robotic manipulation, introduced
    by Zhejiang University, and published at ICRA23.
  ko: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter (A Joint Modeling of Vision-Language-Action
    for Target-oriented Grasping in Clutter), is a 2023 large vision-language-action model for robotic manipulation, introduced
    by Zhejiang University, and published at ICRA23.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_joint_modeling_of_vision_lan
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.12610v3.
sources:
- id: src_001
  type: website
  title: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter source
  url: https://doi.org/10.1109/ICRA48891.2023.10161041
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We focus on the task of language-conditioned grasping in clutter, in which a robot is supposed to grasp the target object based on a language instruction. Previous works separately conduct visual grounding to localize the target object, and generate a grasp for that object. However, these works require object labels or visual attributes for grounding, which calls for handcrafted rules in planner and restricts the range of language instructions. In this paper, we propose to jointly model vision, language and action with object-centric representation. Our method is applicable under more flexible language instructions, and not limited by visual grounding error. Besides, by utilizing the powerful priors from the pre-trained multi-modal model and grasp model, sample efficiency is effectively improved and the sim2real problem is relived without additional data for transfer. A series of experiments carried out in simulation and real world indicate that our method can achieve better task success rate by less times of motion under more flexible language instructions. Moreover, our method is capable of generalizing better to scenarios with unseen objects and language instructions. Our code is available at https://github.com/xukechun/Vision-Language-Grasping

## 核心内容
We focus on the task of language-conditioned grasping in clutter, in which a robot is supposed to grasp the target object based on a language instruction. Previous works separately conduct visual grounding to localize the target object, and generate a grasp for that object. However, these works require object labels or visual attributes for grounding, which calls for handcrafted rules in planner and restricts the range of language instructions. In this paper, we propose to jointly model vision, language and action with object-centric representation. Our method is applicable under more flexible language instructions, and not limited by visual grounding error. Besides, by utilizing the powerful priors from the pre-trained multi-modal model and grasp model, sample efficiency is effectively improved and the sim2real problem is relived without additional data for transfer. A series of experiments carried out in simulation and real world indicate that our method can achieve better task success rate by less times of motion under more flexible language instructions. Moreover, our method is capable of generalizing better to scenarios with unseen objects and language instructions. Our code is available at https://github.com/xukechun/Vision-Language-Grasping

## 参考
- http://arxiv.org/abs/2302.12610v3

