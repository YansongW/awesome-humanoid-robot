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

## Overview
Humans grasp unfamiliar objects by combining an initial visual estimate with tactile and proprioceptive feedback during interaction. We present ShapeGrasp, a robotic implementation of this approach. The proposed method is an iterative grasp-and-complete pipeline that couples implicit surface visuo-haptic shape completion (creation of full 3D shape from partial information) with physics-based grasp planning. From a single RGB-D view, ShapeGrasp infers a complete shape (point cloud or triangular mesh), generates candidate grasps via rigid-body simulation, and executes the best feasible grasp. Each grasp attempt yields additional geometric constraints -- tactile surface contacts and space occupied by the gripper body -- which are fused to update the object shape. Failures trigger pose re-estimation and regrasping using the refined shape. We evaluate ShapeGrasp in the real world using two different robots and grippers. To the best of our knowledge, this is the first approach that updates shape representations following a real-world grasp. We achieved superior results over baselines for both grippers (grasp success rate of 84% with a three-finger gripper and 91% with a two-finger gripper), while improving the 3D shape reconstruction quality in all evaluation metrics used.

## Content
Humans grasp unfamiliar objects by combining an initial visual estimate with tactile and proprioceptive feedback during interaction. We present ShapeGrasp, a robotic implementation of this approach. The proposed method is an iterative grasp-and-complete pipeline that couples implicit surface visuo-haptic shape completion (creation of full 3D shape from partial information) with physics-based grasp planning. From a single RGB-D view, ShapeGrasp infers a complete shape (point cloud or triangular mesh), generates candidate grasps via rigid-body simulation, and executes the best feasible grasp. Each grasp attempt yields additional geometric constraints -- tactile surface contacts and space occupied by the gripper body -- which are fused to update the object shape. Failures trigger pose re-estimation and regrasping using the refined shape. We evaluate ShapeGrasp in the real world using two different robots and grippers. To the best of our knowledge, this is the first approach that updates shape representations following a real-world grasp. We achieved superior results over baselines for both grippers (grasp success rate of 84% with a three-finger gripper and 91% with a two-finger gripper), while improving the 3D shape reconstruction quality in all evaluation metrics used.

## 개요
인간은 낯선 물체를 잡을 때 초기 시각적 추정과 상호작용 중 촉각 및 고유수용성 감각 피드백을 결합합니다. 우리는 이 접근법의 로봇 구현인 ShapeGrasp를 제시합니다. 제안된 방법은 암시적 표면 시각-촉각 형상 완성(부분 정보로부터 전체 3D 형상 생성)을 물리 기반 그랩 계획과 결합한 반복적인 그랩-앤-컴플리트 파이프라인입니다. 단일 RGB-D 뷰에서 ShapeGrasp는 완전한 형상(포인트 클라우드 또는 삼각형 메시)을 추론하고, 강체 시뮬레이션을 통해 후보 그랩을 생성하며, 최적의 실행 가능한 그랩을 수행합니다. 각 그랩 시도는 추가적인 기하학적 제약 조건(촉각 표면 접촉 및 그리퍼 본체가 차지하는 공간)을 생성하며, 이는 물체 형상을 업데이트하기 위해 융합됩니다. 실패 시 정제된 형상을 사용하여 자세 재추정 및 재그랩이 트리거됩니다. 우리는 두 가지 다른 로봇과 그리퍼를 사용하여 실제 환경에서 ShapeGrasp를 평가합니다. 우리가 아는 한, 이는 실제 그랩 후 형상 표현을 업데이트하는 첫 번째 접근법입니다. 우리는 두 그리퍼 모두에서 기준선보다 우수한 결과를 달성했으며(세 손가락 그리퍼의 그랩 성공률 84%, 두 손가락 그리퍼의 91%), 사용된 모든 평가 지표에서 3D 형상 재구성 품질을 개선했습니다.

## 핵심 내용
인간은 낯선 물체를 잡을 때 초기 시각적 추정과 상호작용 중 촉각 및 고유수용성 감각 피드백을 결합합니다. 우리는 이 접근법의 로봇 구현인 ShapeGrasp를 제시합니다. 제안된 방법은 암시적 표면 시각-촉각 형상 완성(부분 정보로부터 전체 3D 형상 생성)을 물리 기반 그랩 계획과 결합한 반복적인 그랩-앤-컴플리트 파이프라인입니다. 단일 RGB-D 뷰에서 ShapeGrasp는 완전한 형상(포인트 클라우드 또는 삼각형 메시)을 추론하고, 강체 시뮬레이션을 통해 후보 그랩을 생성하며, 최적의 실행 가능한 그랩을 수행합니다. 각 그랩 시도는 추가적인 기하학적 제약 조건(촉각 표면 접촉 및 그리퍼 본체가 차지하는 공간)을 생성하며, 이는 물체 형상을 업데이트하기 위해 융합됩니다. 실패 시 정제된 형상을 사용하여 자세 재추정 및 재그랩이 트리거됩니다. 우리는 두 가지 다른 로봇과 그리퍼를 사용하여 실제 환경에서 ShapeGrasp를 평가합니다. 우리가 아는 한, 이는 실제 그랩 후 형상 표현을 업데이트하는 첫 번째 접근법입니다. 우리는 두 그리퍼 모두에서 기준선보다 우수한 결과를 달성했으며(세 손가락 그리퍼의 그랩 성공률 84%, 두 손가락 그리퍼의 91%), 사용된 모든 평가 지표에서 3D 형상 재구성 품질을 개선했습니다.
