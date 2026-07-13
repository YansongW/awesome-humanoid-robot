---
$id: ent_paper_geoprop_grounding_robot_state_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GeoProp: Grounding Robot State in Vision for Generalist Manipulation'
  zh: 'GeoProp: Grounding Robot State in Vision for Generalist Manipulation'
  ko: ''
summary:
  en: "arXiv:2607.07101v1 Announce Type: new \nAbstract: Proprioception is fundamental\
    \ to robotic manipulation, yet standard fusion methods often treat it as an isolated\
    \ vector lacking explicit alignment with visual tokens. Without a direct correspondence\
    \ between 3D kinematics and 2D feature maps, manipulation policies struggle to\
    \ ground the robot's state within the scene, frequently underperforming even vision-only\
    \ baselines. To address this, we introduce GeoProp, a lightweight, plug-and-play\
    \ adapter that aligns proprioception with vision through explicit geometric grounding\
    \ and spatial feature sampling. GeoProp projects the robot state onto the image\
    \ plane to sample localized visual features, constructing a grounded state token.\
    \ It then injects state-derived spatial priors into the corresponding visual features\
    \ via FiLM modulation. To capture motion intent, GeoProp further samples features\
    \ at a short-horizon predicted coordinate derived from recent kinematics, providing\
    \ look-ahead visual context. Across 67 tasks, GeoProp improves Diffusion Policy\
    \ by 8.7% on 63 simulation tasks and pi_0 by 4.0% on the RoboTwin subset, and\
    \ yields a 10.6% average gain across both policy families in the real world, while\
    \ adding only 2-3% to the parameter count. These results demonstrate that GeoProp\
    \ is a simple yet high-impact inductive bias for generalist embodied policies.\
    \ Project page: https://alibaba-damo-academy.github.io/GeoProp/."
  zh: "arXiv:2607.07101v1 Announce Type: new \nAbstract: Proprioception is fundamental\
    \ to robotic manipulation, yet standard fusion methods often treat it as an isolated\
    \ vector lacking explicit alignment with visual tokens. Without a direct correspondence\
    \ between 3D kinematics and 2D feature maps, manipulation policies struggle to\
    \ ground the robot's state within the scene, frequently underperforming even vision-only\
    \ baselines. To address this, we introduce GeoProp, a lightweight, plug-and-play\
    \ adapter that aligns proprioception with vision through explicit geometric grounding\
    \ and spatial feature sampling. GeoProp projects the robot state onto the image\
    \ plane to sample localized visual features, constructing a grounded state token.\
    \ It then injects state-derived spatial priors into the corresponding visual features\
    \ via FiLM modulation. To capture motion intent, GeoProp further samples features\
    \ at a short-horizon predicted coordinate derived from recent kinematics, providing\
    \ look-ahead visual context. Across 67 tasks, GeoProp improves Diffusion Policy\
    \ by 8.7% on 63 simulation tasks and pi_0 by 4.0% on the RoboTwin subset, and\
    \ yields a 10.6% average gain across both policy families in the real world, while\
    \ adding only 2-3% to the parameter count. These results demonstrate that GeoProp\
    \ is a simple yet high-impact inductive bias for generalist embodied policies.\
    \ Project page: https://alibaba-damo-academy.github.io/GeoProp/."
  ko: ''
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
- robotics
- geoprop
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-10'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'GeoProp: Grounding Robot State in Vision for Generalist Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.07101
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.07101v1 Announce Type: new 
Abstract: Proprioception is fundamental to robotic manipulation, yet standard fusion methods often treat it as an isolated vector lacking explicit alignment with visual tokens. Without a direct correspondence between 3D kinematics and 2D feature maps, manipulation policies struggle to ground the robot's state within the scene, frequently underperforming even vision-only baselines. To address this, we introduce GeoProp, a lightweight, plug-and-play adapter that aligns proprioception with vision through explicit geometric grounding and spatial feature sampling. GeoProp projects the robot state onto the image plane to sample localized visual features, constructing a grounded state token. It then injects state-derived spatial priors into the corresponding visual features via FiLM modulation. To capture motion intent, GeoProp further samples features at a short-horizon predicted coordinate derived from recent kinematics, providing look-ahead visual context. Across 67 tasks, GeoProp improves Diffusion Policy by 8.7% on 63 simulation tasks and pi_0 by 4.0% on the RoboTwin subset, and yields a 10.6% average gain across both policy families in the real world, while adding only 2-3% to the parameter count. These results demonstrate that GeoProp is a simple yet high-impact inductive bias for generalist embodied policies. Project page: https://alibaba-damo-academy.github.io/GeoProp/.
