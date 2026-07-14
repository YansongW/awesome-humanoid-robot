---
$id: ent_paper_mao_robomatrix_a_skill_centric_hie_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World'
  zh: RoboMatrix
  ko: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World'
summary:
  en: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World (RoboMatrix),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Waseda University, Beijing Institute
    of Technology, The Chinese University of Hong Kong, MEGVII Technology, Chinese Academy of Sciences.'
  zh: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World (RoboMatrix),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Waseda University, Beijing Institute
    of Technology, The Chinese University of Hong Kong, MEGVII Technology, Chinese Academy of Sciences.'
  ko: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World (RoboMatrix),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Waseda University, Beijing Institute
    of Technology, The Chinese University of Hong Kong, MEGVII Technology, Chinese Academy of Sciences.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robomatrix
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.00171v3.
sources:
- id: src_001
  type: paper
  title: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World
    (arXiv)'
  url: https://arxiv.org/abs/2412.00171
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboMatrix source
  url: https://doi.org/10.48550/arXiv.2412.00171
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Existing robot policies predominantly adopt the task-centric approach, requiring end-to-end task data collection. This results in limited generalization to new tasks and difficulties in pinpointing errors within long-horizon, multi-stage tasks. To address this, we propose RoboMatrix, a skill-centric hierarchical framework designed for scalable robot task planning and execution in open-world environments. RoboMatrix extracts general meta-skills from diverse complex tasks, enabling the completion of unseen tasks through skill composition. Its architecture consists of a high-level scheduling layer that utilizes large language models (LLMs) for task decomposition, an intermediate skill layer housing meta-skill models, and a low-level hardware layer for robot control. A key innovation of our work is the introduction of the first unified vision-language-action (VLA) model capable of seamlessly integrating both movement and manipulation within one model. This is achieved by combining vision and language prompts to generate discrete actions. Experimental results demonstrate that RoboMatrix achieves a 50% higher success rate than task-centric baselines when applied to unseen objects, scenes, and tasks. To advance open-world robotics research, we will open-source code, hardware designs, model weights, and datasets at https://github.com/WayneMao/RoboMatrix.

## 核心内容
Existing robot policies predominantly adopt the task-centric approach, requiring end-to-end task data collection. This results in limited generalization to new tasks and difficulties in pinpointing errors within long-horizon, multi-stage tasks. To address this, we propose RoboMatrix, a skill-centric hierarchical framework designed for scalable robot task planning and execution in open-world environments. RoboMatrix extracts general meta-skills from diverse complex tasks, enabling the completion of unseen tasks through skill composition. Its architecture consists of a high-level scheduling layer that utilizes large language models (LLMs) for task decomposition, an intermediate skill layer housing meta-skill models, and a low-level hardware layer for robot control. A key innovation of our work is the introduction of the first unified vision-language-action (VLA) model capable of seamlessly integrating both movement and manipulation within one model. This is achieved by combining vision and language prompts to generate discrete actions. Experimental results demonstrate that RoboMatrix achieves a 50% higher success rate than task-centric baselines when applied to unseen objects, scenes, and tasks. To advance open-world robotics research, we will open-source code, hardware designs, model weights, and datasets at https://github.com/WayneMao/RoboMatrix.

## 参考
- http://arxiv.org/abs/2412.00171v3

