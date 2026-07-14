---
$id: ent_paper_closing_the_reality_gap_zero_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based
    Grasping and Manipulation'
  zh: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based
    Grasping and Manipulation'
  ko: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based
    Grasping and Manipulation'
summary:
  en: "arXiv:2607.04940v1 Announce Type: new \nAbstract: Human-like dexterous hands\
    \ with multiple fingers offer human-level manipulation capabilities but remain\
    \ difficult to train the control policies that can deploy on real hardware due\
    \ to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement\
    \ learning method that leverages dense tactile feedback combined with joint torque\
    \ sensing to explicitly regulate physical interactions. To enable effective sim-to-real\
    \ transfer, we introduce (i) a computationally fast tactile simulation that computes\
    \ distances between dense virtual tactile units and the object via parallel forward\
    \ kinematics, providing high-rate, high-resolution touch signals needed by RL;\
    \ (ii) a current-to-torque calibration that eliminates the need for torque sensors\
    \ on dexterous hands by mapping motor current to joint torque; and (iii) actuator\
    \ dynamics modeling with randomization to account for non-ideal torque-speed effects\
    \ and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline,\
    \ we train policies entirely in simulation and deploy them directly to a five-finger\
    \ hand. The resulting policies demonstrate two essential human-hand skills: (1)\
    \ command-based controllable grasp force tracking and (2) reorientation of objects\
    \ in the hand, both of which are robustly executed without fine-tuning on the\
    \ robot. By combining tactile and torque in the observation space with scalable\
    \ sensing and actuation modeling, our system provides a practical solution to\
    \ achieve reliable dexterous manipulation. To our knowledge, this is the first\
    \ demonstration of controllable grasping on a multi-finger dexterous hand trained\
    \ entirely in simulation and transferred zero-shot on real hardware."
  zh: "arXiv:2607.04940v1 Announce Type: new \nAbstract: Human-like dexterous hands\
    \ with multiple fingers offer human-level manipulation capabilities but remain\
    \ difficult to train the control policies that can deploy on real hardware due\
    \ to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement\
    \ learning method that leverages dense tactile feedback combined with joint torque\
    \ sensing to explicitly regulate physical interactions. To enable effective sim-to-real\
    \ transfer, we introduce (i) a computationally fast tactile simulation that computes\
    \ distances between dense virtual tactile units and the object via parallel forward\
    \ kinematics, providing high-rate, high-resolution touch signals needed by RL;\
    \ (ii) a current-to-torque calibration that eliminates the need for torque sensors\
    \ on dexterous hands by mapping motor current to joint torque; and (iii) actuator\
    \ dynamics modeling with randomization to account for non-ideal torque-speed effects\
    \ and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline,\
    \ we train policies entirely in simulation and deploy them directly to a five-finger\
    \ hand. The resulting policies demonstrate two essential human-hand skills: (1)\
    \ command-based controllable grasp force tracking and (2) reorientation of objects\
    \ in the hand, both of which are robustly executed without fine-tuning on the\
    \ robot. By combining tactile and torque in the observation space with scalable\
    \ sensing and actuation modeling, our system provides a practical solution to\
    \ achieve reliable dexterous manipulation. To our knowledge, this is the first\
    \ demonstration of controllable grasping on a multi-finger dexterous hand trained\
    \ entirely in simulation and transferred zero-shot on real hardware."
  ko: "arXiv:2607.04940v1 Announce Type: new \nAbstract: Human-like dexterous hands\
    \ with multiple fingers offer human-level manipulation capabilities but remain\
    \ difficult to train the control policies that can deploy on real hardware due\
    \ to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement\
    \ learning method that leverages dense tactile feedback combined with joint torque\
    \ sensing to explicitly regulate physical interactions. To enable effective sim-to-real\
    \ transfer, we introduce (i) a computationally fast tactile simulation that computes\
    \ distances between dense virtual tactile units and the object via parallel forward\
    \ kinematics, providing high-rate, high-resolution touch signals needed by RL;\
    \ (ii) a current-to-torque calibration that eliminates the need for torque sensors\
    \ on dexterous hands by mapping motor current to joint torque; and (iii) actuator\
    \ dynamics modeling with randomization to account for non-ideal torque-speed effects\
    \ and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline,\
    \ we train policies entirely in simulation and deploy them directly to a five-finger\
    \ hand. The resulting policies demonstrate two essential human-hand skills: (1)\
    \ command-based controllable grasp force tracking and (2) reorientation of objects\
    \ in the hand, both of which are robustly executed without fine-tuning on the\
    \ robot. By combining tactile and torque in the observation space with scalable\
    \ sensing and actuation modeling, our system provides a practical solution to\
    \ achieve reliable dexterous manipulation. To our knowledge, this is the first\
    \ demonstration of controllable grasping on a multi-finger dexterous hand trained\
    \ entirely in simulation and transferred zero-shot on real hardware."
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
- closing_the_reality_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous
    Force-Based Grasping and Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.04940
  date: '2026'
  accessed_at: '2026-07-08'
---

## 概述
arXiv:2607.04940v1 Announce Type: new 
Abstract: Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1) command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

## Overview
arXiv:2607.04940v1 Announce Type: new 
Abstract: Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1) command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

## 개요
arXiv:2607.04940v1 Announce Type: new 
Abstract: Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1) command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.
