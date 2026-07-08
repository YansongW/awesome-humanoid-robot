---
$id: ent_paper_learning_all_terrain_locomotio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated
    Suspension
  zh: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated
    Suspension
  ko: ''
summary:
  en: "arXiv:2606.06790v2 Announce Type: replace \nAbstract: This paper presents ERNEST,\
    \ a four-wheeled planetary rover concept equipped with a two-degree-of-freedom\
    \ Active Gimbal Suspension that combines yaw and roll actuation to enable wheel\
    \ reconfiguration, steering, and active load redistribution. A single neural network\
    \ controller, trained to track a desired path across challenging terrain, fully\
    \ unlocks the capabilities of this actuated suspension system for autonomous obstacle\
    \ negotiation. A reinforcement learning framework is developed using the high-fidelity\
    \ DARTS simulation engine, which combines rigid-contact dynamics and Bekker-Wong\
    \ terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil\
    \ conditions. To obtain a single unified controller across heterogeneous terrains,\
    \ a policy consolidation strategy merges the experience of terrain-specialized\
    \ agents into one neural network, eliminating the need for explicit terrain classification\
    \ and controller switching. The resulting controller operates on a combination\
    \ of proprioceptive and exteroceptive feedback, including sparse stereo-derived\
    \ terrain elevation, chassis attitude, joint states, and force-torque measurements.\
    \ Zero-shot transfer to the physical rover is achieved through domain randomization,\
    \ sensor noise injection, and model-to-real system identification. Experimental\
    \ results demonstrate autonomous traversal of rock fields, a Bickler trap (bump\
    \ obstacle), a wheel-high step, sand ripples, and sandy slopes. On a 20{\\deg}\
    \ sandy slope, the learned controller reduces the cost of transport by 37% on\
    \ dry sand despite the additional actuation, and achieves superior performance\
    \ on wet sand where the passive suspension becomes completely immobilized. A video\
    \ accompanying this paper is available at https://youtu.be/d684P5a3xMc"
  zh: "arXiv:2606.06790v2 Announce Type: replace \nAbstract: This paper presents ERNEST,\
    \ a four-wheeled planetary rover concept equipped with a two-degree-of-freedom\
    \ Active Gimbal Suspension that combines yaw and roll actuation to enable wheel\
    \ reconfiguration, steering, and active load redistribution. A single neural network\
    \ controller, trained to track a desired path across challenging terrain, fully\
    \ unlocks the capabilities of this actuated suspension system for autonomous obstacle\
    \ negotiation. A reinforcement learning framework is developed using the high-fidelity\
    \ DARTS simulation engine, which combines rigid-contact dynamics and Bekker-Wong\
    \ terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil\
    \ conditions. To obtain a single unified controller across heterogeneous terrains,\
    \ a policy consolidation strategy merges the experience of terrain-specialized\
    \ agents into one neural network, eliminating the need for explicit terrain classification\
    \ and controller switching. The resulting controller operates on a combination\
    \ of proprioceptive and exteroceptive feedback, including sparse stereo-derived\
    \ terrain elevation, chassis attitude, joint states, and force-torque measurements.\
    \ Zero-shot transfer to the physical rover is achieved through domain randomization,\
    \ sensor noise injection, and model-to-real system identification. Experimental\
    \ results demonstrate autonomous traversal of rock fields, a Bickler trap (bump\
    \ obstacle), a wheel-high step, sand ripples, and sandy slopes. On a 20{\\deg}\
    \ sandy slope, the learned controller reduces the cost of transport by 37% on\
    \ dry sand despite the additional actuation, and achieves superior performance\
    \ on wet sand where the passive suspension becomes completely immobilized. A video\
    \ accompanying this paper is available at https://youtu.be/d684P5a3xMc"
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
- learning_all_terrain_locomotio
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from arXiv cs.RO RSS feed.
sources:
- id: src_001
  type: paper
  title: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated
    Suspension
  url: https://arxiv.org/abs/2606.06790
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2606.06790v2 Announce Type: replace 
Abstract: This paper presents ERNEST, a four-wheeled planetary rover concept equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration, steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples, and sandy slopes. On a 20{\deg} sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc
