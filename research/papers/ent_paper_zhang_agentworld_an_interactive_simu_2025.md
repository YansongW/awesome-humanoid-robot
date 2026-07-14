---
$id: ent_paper_zhang_agentworld_an_interactive_simu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation'
  zh: AgentWorld
  ko: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation'
summary:
  en: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation (AgentWorld),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tencent Robotics X, Shanghai Jiao
    Tong University, and published at CoRL25.'
  zh: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation (AgentWorld),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tencent Robotics X, Shanghai Jiao
    Tong University, and published at CoRL25.'
  ko: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation (AgentWorld),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tencent Robotics X, Shanghai Jiao
    Tong University, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- agentworld
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.07770v2.
sources:
- id: src_001
  type: paper
  title: 'AgentWorld: An Interactive Simulation Platform for Scene Construction and Mobile Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2508.07770
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AgentWorld source
  url: https://doi.org/10.48550/arXiv.2508.07770
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce AgentWorld, an interactive simulation platform for developing household mobile manipulation capabilities. Our platform combines automated scene construction that encompasses layout generation, semantic asset placement, visual material configuration, and physics simulation, with a dual-mode teleoperation system supporting both wheeled bases and humanoid locomotion policies for data collection. The resulting AgentWorld Dataset captures diverse tasks ranging from primitive actions (pick-and-place, push-pull, etc.) to multistage activities (serve drinks, heat up food, etc.) across living rooms, bedrooms, and kitchens. Through extensive benchmarking of imitation learning methods including behavior cloning, action chunking transformers, diffusion policies, and vision-language-action models, we demonstrate the dataset's effectiveness for sim-to-real transfer. The integrated system provides a comprehensive solution for scalable robotic skill acquisition in complex home environments, bridging the gap between simulation-based training and real-world deployment. The code, datasets will be available at https://yizhengzhang1.github.io/agent_world/

## 核心内容
We introduce AgentWorld, an interactive simulation platform for developing household mobile manipulation capabilities. Our platform combines automated scene construction that encompasses layout generation, semantic asset placement, visual material configuration, and physics simulation, with a dual-mode teleoperation system supporting both wheeled bases and humanoid locomotion policies for data collection. The resulting AgentWorld Dataset captures diverse tasks ranging from primitive actions (pick-and-place, push-pull, etc.) to multistage activities (serve drinks, heat up food, etc.) across living rooms, bedrooms, and kitchens. Through extensive benchmarking of imitation learning methods including behavior cloning, action chunking transformers, diffusion policies, and vision-language-action models, we demonstrate the dataset's effectiveness for sim-to-real transfer. The integrated system provides a comprehensive solution for scalable robotic skill acquisition in complex home environments, bridging the gap between simulation-based training and real-world deployment. The code, datasets will be available at https://yizhengzhang1.github.io/agent_world/

## 参考
- http://arxiv.org/abs/2508.07770v2

