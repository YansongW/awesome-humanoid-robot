---
$id: ent_paper_3d_hamster_bridging_planning_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action
    Models through 3D Trajectory Guidance'
  zh: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action
    Models through 3D Trajectory Guidance'
  ko: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action
    Models through 3D Trajectory Guidance'
summary:
  en: "arXiv:2606.31329v1 Announce Type: new \nAbstract: Hierarchical Vision-Language-Action\
    \ (VLA) models decouple high-level planning from low-level control to improve\
    \ generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector\
    \ trajectories predicted by a Vision-Language Model (VLM) as explicit guidance\
    \ for a downstream policy. However, state-of-the-art low-level policies operate\
    \ in 3D metric space on point clouds, and feeding them 2D guidance that lacks\
    \ depth forces each waypoint to be assigned the depth of whatever scene surface\
    \ lies beneath it, producing geometrically distorted trajectories. We propose\
    \ 3D HAMSTER, a hierarchical framework that closes this gap by having the planner\
    \ directly output metrically reliable 3D trajectories. We augment a VLM with a\
    \ dedicated depth encoder and a dense depth reconstruction objective to predict\
    \ 3D waypoint sequences, which are directly integrated into a pointcloudbased\
    \ low-level policy. Across 3D trajectory prediction, simulation, and real-world\
    \ manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided\
    \ baselines, with the largest gains under appearance-altering shifts and unseen\
    \ language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/."
  zh: "arXiv:2606.31329v1 Announce Type: new \nAbstract: Hierarchical Vision-Language-Action\
    \ (VLA) models decouple high-level planning from low-level control to improve\
    \ generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector\
    \ trajectories predicted by a Vision-Language Model (VLM) as explicit guidance\
    \ for a downstream policy. However, state-of-the-art low-level policies operate\
    \ in 3D metric space on point clouds, and feeding them 2D guidance that lacks\
    \ depth forces each waypoint to be assigned the depth of whatever scene surface\
    \ lies beneath it, producing geometrically distorted trajectories. We propose\
    \ 3D HAMSTER, a hierarchical framework that closes this gap by having the planner\
    \ directly output metrically reliable 3D trajectories. We augment a VLM with a\
    \ dedicated depth encoder and a dense depth reconstruction objective to predict\
    \ 3D waypoint sequences, which are directly integrated into a pointcloudbased\
    \ low-level policy. Across 3D trajectory prediction, simulation, and real-world\
    \ manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided\
    \ baselines, with the largest gains under appearance-altering shifts and unseen\
    \ language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/."
  ko: "arXiv:2606.31329v1 Announce Type: new \nAbstract: Hierarchical Vision-Language-Action\
    \ (VLA) models decouple high-level planning from low-level control to improve\
    \ generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector\
    \ trajectories predicted by a Vision-Language Model (VLM) as explicit guidance\
    \ for a downstream policy. However, state-of-the-art low-level policies operate\
    \ in 3D metric space on point clouds, and feeding them 2D guidance that lacks\
    \ depth forces each waypoint to be assigned the depth of whatever scene surface\
    \ lies beneath it, producing geometrically distorted trajectories. We propose\
    \ 3D HAMSTER, a hierarchical framework that closes this gap by having the planner\
    \ directly output metrically reliable 3D trajectories. We augment a VLM with a\
    \ dedicated depth encoder and a dense depth reconstruction objective to predict\
    \ 3D waypoint sequences, which are directly integrated into a pointcloudbased\
    \ low-level policy. Across 3D trajectory prediction, simulation, and real-world\
    \ manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided\
    \ baselines, with the largest gains under appearance-altering shifts and unseen\
    \ language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/."
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 3d_hamster
- humanoid
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
  title: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language
    Action Models through 3D Trajectory Guidance'
  url: https://arxiv.org/abs/2606.31329
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
arXiv:2606.31329v1 Announce Type: new 
Abstract: Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.

## Overview
arXiv:2606.31329v1 Announce Type: new 
Abstract: Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.

## 개요
arXiv:2606.31329v1 Announce Type: new 
Abstract: Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.
