---
$id: ent_paper_robot_trajectron_v3_a_probabil_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation'
  zh: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation'
  ko: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation'
summary:
  en: "arXiv:2607.09315v1 Announce Type: new \nAbstract: We aim to address the challenge\
    \ of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation\
    \ tasks, which is cognitively demanding and error-prone, particularly when relying\
    \ on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic\
    \ shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates\
    \ shared control as Bayesian inference by learning a prior over user intent and\
    \ combining it with real-time user commands to estimate the posterior intent distribution.\
    \ The prior models user intent as a distribution over future trajectories conditioned\
    \ on past robot dynamics and visual scene context. The intent prior is parameterized\
    \ by a transformer-based conditional generative model that reasons over point\
    \ clouds and candidate grasp poses, together with a factorized translation-rotation\
    \ representation that improves learning efficiency in high-dimensional action\
    \ spaces. During execution, RT-V3 continuously estimates the posterior distribution\
    \ over future trajectories by combining the learned intent prior with a user-command\
    \ likelihood derived from the observed control input, enabling continuous intent\
    \ refinement and shared assistance. Comprehensive experiments demonstrate that\
    \ RT-V3 achieves high accuracy in trajectory prediction and competitive performance\
    \ in reactive planning. Furthermore, real-world user studies indicate that RT-V3\
    \ significantly outperforms baseline methods in terms of success rate and efficiency,\
    \ while substantially reducing the user's physical and mental workload."
  zh: "arXiv:2607.09315v1 Announce Type: new \nAbstract: We aim to address the challenge\
    \ of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation\
    \ tasks, which is cognitively demanding and error-prone, particularly when relying\
    \ on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic\
    \ shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates\
    \ shared control as Bayesian inference by learning a prior over user intent and\
    \ combining it with real-time user commands to estimate the posterior intent distribution.\
    \ The prior models user intent as a distribution over future trajectories conditioned\
    \ on past robot dynamics and visual scene context. The intent prior is parameterized\
    \ by a transformer-based conditional generative model that reasons over point\
    \ clouds and candidate grasp poses, together with a factorized translation-rotation\
    \ representation that improves learning efficiency in high-dimensional action\
    \ spaces. During execution, RT-V3 continuously estimates the posterior distribution\
    \ over future trajectories by combining the learned intent prior with a user-command\
    \ likelihood derived from the observed control input, enabling continuous intent\
    \ refinement and shared assistance. Comprehensive experiments demonstrate that\
    \ RT-V3 achieves high accuracy in trajectory prediction and competitive performance\
    \ in reactive planning. Furthermore, real-world user studies indicate that RT-V3\
    \ significantly outperforms baseline methods in terms of success rate and efficiency,\
    \ while substantially reducing the user's physical and mental workload."
  ko: "arXiv:2607.09315v1 Announce Type: new \nAbstract: We aim to address the challenge\
    \ of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation\
    \ tasks, which is cognitively demanding and error-prone, particularly when relying\
    \ on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic\
    \ shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates\
    \ shared control as Bayesian inference by learning a prior over user intent and\
    \ combining it with real-time user commands to estimate the posterior intent distribution.\
    \ The prior models user intent as a distribution over future trajectories conditioned\
    \ on past robot dynamics and visual scene context. The intent prior is parameterized\
    \ by a transformer-based conditional generative model that reasons over point\
    \ clouds and candidate grasp poses, together with a factorized translation-rotation\
    \ representation that improves learning efficiency in high-dimensional action\
    \ spaces. During execution, RT-V3 continuously estimates the posterior distribution\
    \ over future trajectories by combining the learned intent prior with a user-command\
    \ likelihood derived from the observed control input, enabling continuous intent\
    \ refinement and shared assistance. Comprehensive experiments demonstrate that\
    \ RT-V3 achieves high accuracy in trajectory prediction and competitive performance\
    \ in reactive planning. Furthermore, real-world user studies indicate that RT-V3\
    \ significantly outperforms baseline methods in terms of success rate and efficiency,\
    \ while substantially reducing the user's physical and mental workload."
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
- robot_trajectron_v3
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3)
    Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.09315
  date: '2026'
  accessed_at: '2026-07-14'
---

## 概述
arXiv:2607.09315v1 Announce Type: new 
Abstract: We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces. During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user's physical and mental workload.

## Overview
arXiv:2607.09315v1 Announce Type: new 
Abstract: We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces. During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user's physical and mental workload.

## 개요
arXiv:2607.09315v1 Announce Type: new 
Abstract: We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces. During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user's physical and mental workload.
