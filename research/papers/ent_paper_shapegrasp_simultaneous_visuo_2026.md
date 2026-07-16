---
$id: ent_paper_shapegrasp_simultaneous_visuo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation'
  zh: 'ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation'
  ko: 'ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation'
summary:
  en: 'arXiv:2605.02347v2 Announce Type: replace Abstract: Humans grasp unfamiliar objects by combining an initial visual
    estimate with tactile and proprioceptive feedback during interaction. We present ShapeGrasp, a robotic implementation
    of this approach. The proposed method is an iterative grasp-and-complete pipeline that couples implicit surface visuo-haptic
    shape completion (creation of full 3D shape from partial information) with physics-based grasp planning. From a single
    RGB-D view, ShapeGrasp infers a complete shape (point cloud or triangular mesh), generates candidate grasps via rigid-body
    simulation, and executes the best feasible grasp. Each grasp attempt yields additional geometric constraints -- tactile
    surface contacts and space occupied by the gripper body -- which are fused to update the object shape. Failures trigger
    pose re-estimation and regrasping using the refined shape. We evaluate ShapeGrasp in the real world using two different
    robots and grippers. To the best of our knowledge, this is the first approach that updates shape representations following
    a real-world grasp. We achieved superior results over baselines for both grippers (grasp success rate of 84% with a three-finger
    gripper and 91% with a two-finger gripper), while improving the 3D shape reconstruction quality in all evaluation metrics
    used.'
  zh: 'arXiv:2605.02347v2 Announce Type: replace Abstract: Humans grasp unfamiliar objects by combining an initial visual
    estimate with tactile and proprioceptive feedback during interaction. We present ShapeGrasp, a robotic implementation
    of this approach. The proposed method is an iterative grasp-and-complete pipeline that couples implicit surface visuo-haptic
    shape completion (creation of full 3D shape from partial information) with physics-based grasp planning. From a single
    RGB-D view, ShapeGrasp infers a complete shape (point cloud or triangular mesh), generates candidate grasps via rigid-body
    simulation, and executes the best feasible grasp. Each grasp attempt yields additional geometric constraints -- tactile
    surface contacts and space occupied by the gripper body -- which are fused to update the object shape. Failures trigger
    pose re-estimation and regrasping using the refined shape. We evaluate ShapeGrasp in the real world using two different
    robots and grippers. To the best of our knowledge, this is the first approach that updates shape representations following
    a real-world grasp. We achieved superior results over baselines for both grippers (grasp success rate of 84% with a three-finger
    gripper and 91% with a two-finger gripper), while improving the 3D shape reconstruction quality in all evaluation metrics
    used.'
  ko: 'arXiv:2605.02347v2 Announce Type: replace Abstract: Humans grasp unfamiliar objects by combining an initial visual
    estimate with tactile and proprioceptive feedback during interaction. We present ShapeGrasp, a robotic implementation
    of this approach. The proposed method is an iterative grasp-and-complete pipeline that couples implicit surface visuo-haptic
    shape completion (creation of full 3D shape from partial information) with physics-based grasp planning. From a single
    RGB-D view, ShapeGrasp infers a complete shape (point cloud or triangular mesh), generates candidate grasps via rigid-body
    simulation, and executes the best feasible grasp. Each grasp attempt yields additional geometric constraints -- tactile
    surface contacts and space occupied by the gripper body -- which are fused to update the object shape. Failures trigger
    pose re-estimation and regrasping using the refined shape. We evaluate ShapeGrasp in the real world using two different
    robots and grippers. To the best of our knowledge, this is the first approach that updates shape representations following
    a real-world grasp. We achieved superior results over baselines for both grippers (grasp success rate of 84% with a three-finger
    gripper and 91% with a two-finger gripper), while improving the 3D shape reconstruction quality in all evaluation metrics
    used.'
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
- shapegrasp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.02347v2.
sources:
- id: src_001
  type: paper
  title: 'ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation'
  url: https://arxiv.org/abs/2605.02347
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humans grasp unfamiliar objects by combining an initial visual estimate with tactile and proprioceptive feedback during interaction. We present ShapeGrasp, a robotic implementation of this approach. The proposed method is an iterative grasp-and-complete pipeline that couples implicit surface visuo-haptic shape completion (creation of full 3D shape from partial information) with physics-based grasp planning. From a single RGB-D view, ShapeGrasp infers a complete shape (point cloud or triangular mesh), generates candidate grasps via rigid-body simulation, and executes the best feasible grasp. Each grasp attempt yields additional geometric constraints -- tactile surface contacts and space occupied by the gripper body -- which are fused to update the object shape. Failures trigger pose re-estimation and regrasping using the refined shape. We evaluate ShapeGrasp in the real world using two different robots and grippers. To the best of our knowledge, this is the first approach that updates shape representations following a real-world grasp. We achieved superior results over baselines for both grippers (grasp success rate of 84% with a three-finger gripper and 91% with a two-finger gripper), while improving the 3D shape reconstruction quality in all evaluation metrics used.

## 核心内容
Humans grasp unfamiliar objects by combining an initial visual estimate with tactile and proprioceptive feedback during interaction. We present ShapeGrasp, a robotic implementation of this approach. The proposed method is an iterative grasp-and-complete pipeline that couples implicit surface visuo-haptic shape completion (creation of full 3D shape from partial information) with physics-based grasp planning. From a single RGB-D view, ShapeGrasp infers a complete shape (point cloud or triangular mesh), generates candidate grasps via rigid-body simulation, and executes the best feasible grasp. Each grasp attempt yields additional geometric constraints -- tactile surface contacts and space occupied by the gripper body -- which are fused to update the object shape. Failures trigger pose re-estimation and regrasping using the refined shape. We evaluate ShapeGrasp in the real world using two different robots and grippers. To the best of our knowledge, this is the first approach that updates shape representations following a real-world grasp. We achieved superior results over baselines for both grippers (grasp success rate of 84% with a three-finger gripper and 91% with a two-finger gripper), while improving the 3D shape reconstruction quality in all evaluation metrics used.

## 参考
- http://arxiv.org/abs/2605.02347v2

