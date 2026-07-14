---
$id: ent_paper_egodemogen_novel_egocentric_de_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation'
  zh: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation'
  ko: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation'
summary:
  en: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation is a 2025 work on manipulation
    for humanoid robots.'
  zh: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation is a 2025 work on manipulation
    for humanoid robots.'
  ko: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation is a 2025 work on manipulation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egodemogen
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22578v2.
sources:
- id: src_001
  type: paper
  title: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.22578
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning based visuomotor policies have achieved strong performance in robotic manipulation, yet they often remain sensitive to egocentric viewpoint shifts. Unlike third-person viewpoint changes that only move the camera, egocentric shifts simultaneously alter both the camera pose and the robot action coordinate frame, making it necessary to jointly transfer action trajectories and synthesize corresponding observations under novel egocentric viewpoints. To address this challenge, we present EgoDemoGen, a framework that generates paired observation--action demonstrations under novel egocentric viewpoints through two key components: 1{)} EgoTrajTransfer, which transfers robot trajectories to the novel egocentric coordinate frame through motion-skill segmentation, geometry-aware transformation, and inverse kinematics filtering; and 2{)} EgoViewTransfer, a conditional video generation model that fuses a novel-viewpoint reprojected scene video and a robot motion video rendered from the transferred trajectory to synthesize photorealistic observations, trained with a self-supervised double reprojection strategy without requiring multi-viewpoint data. Experiments in simulation and real-world settings show that EgoDemoGen consistently improves policy success rates under both standard and novel egocentric viewpoints, with absolute gains of +24.6\% and +16.9\% in simulation and +16.0\% and +23.0\% on the real robot. Moreover, EgoViewTransfer achieves superior video generation quality for novel egocentric observations.

## 核心内容
Imitation learning based visuomotor policies have achieved strong performance in robotic manipulation, yet they often remain sensitive to egocentric viewpoint shifts. Unlike third-person viewpoint changes that only move the camera, egocentric shifts simultaneously alter both the camera pose and the robot action coordinate frame, making it necessary to jointly transfer action trajectories and synthesize corresponding observations under novel egocentric viewpoints. To address this challenge, we present EgoDemoGen, a framework that generates paired observation--action demonstrations under novel egocentric viewpoints through two key components: 1{)} EgoTrajTransfer, which transfers robot trajectories to the novel egocentric coordinate frame through motion-skill segmentation, geometry-aware transformation, and inverse kinematics filtering; and 2{)} EgoViewTransfer, a conditional video generation model that fuses a novel-viewpoint reprojected scene video and a robot motion video rendered from the transferred trajectory to synthesize photorealistic observations, trained with a self-supervised double reprojection strategy without requiring multi-viewpoint data. Experiments in simulation and real-world settings show that EgoDemoGen consistently improves policy success rates under both standard and novel egocentric viewpoints, with absolute gains of +24.6\% and +16.9\% in simulation and +16.0\% and +23.0\% on the real robot. Moreover, EgoViewTransfer achieves superior video generation quality for novel egocentric observations.

## 参考
- http://arxiv.org/abs/2509.22578v2

