---
$id: ent_paper_guidetti_stress_flow_guided_non_planar_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Stress Flow Guided Non-Planar Print Trajectory Optimization for Additive Manufacturing
    of Anisotropic Polymers
  zh: 各向异性聚合物增材制造中应力流引导的非平面打印轨迹优化
  ko: 이방성 폴리머 적층 제조를 위한 응력 흐름 기반 비평면 출력 궤적 최적화
summary:
  en: Presents a trajectory optimization framework that aligns non-planar fused filament
    fabrication paths with principal stress flow, demonstrating up to 44x failure
    strength and 6x stiffness improvements on a 5-axis printer using liquid crystal
    polymer.
  zh: 提出了一种将非平面熔丝制造路径与主应力流对齐的轨迹优化框架，在使用液晶聚合物的五轴打印机上实现了高达44倍的断裂强度和6倍的刚度提升。
  ko: 비평면 용융 필라멘트 제조 경로를 주 응력 흐름과 정렬하는 궤적 최적화 프레임워크를 제시하며, 액정 폴리머를 사용한 5축 프린터에서 최대
    44배의 파괴 강도와 6배의 강성 향상을 입증하였다.
domains:
- 03_manufacturing_processes
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- process
tags:
- non_planar_printing
- fused_filament_fabrication
- additive_manufacturing
- anisotropic_polymers
- stress_flow_alignment
- trajectory_optimization
- 5_axis_printing
- liquid_crystal_polymer
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text verification is recommended
    before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Stress Flow Guided Non-Planar Print Trajectory Optimization for Additive
    Manufacturing of Anisotropic Polymers
  url: https://arxiv.org/abs/2301.04999
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper addresses the problem that conventional planar fused filament fabrication (FFF) deposits material in fixed layer orientations, which cannot align with the principal stress flow in loaded parts made from anisotropic polymers. Because anisotropic polymers such as liquid crystal polymer (LCP) are much stronger along the deposition direction than across layers, misalignment between print trajectories and stress flow leads to weak inter-layer interfaces and premature mechanical failure. To overcome this, the authors propose a non-planar slicing and trajectory optimization framework that computes the stress field for a predefined load case and then generates print paths whose local deposition direction follows the stress flow.

The optimization pipeline includes manufacturability constraints such as uniform layer height and line spacing, which are enforced through geodesic-heat offset slicing and a scalar-field trajectory optimization procedure with stress-flow rectification and propagation. The method is demonstrated on a load-bearing mechanical bracket manufactured on a modified 5-axis 3D printer using LCP filament. The optimized non-planar bracket is reported to achieve a 44-fold increase in failure strength and a 6-fold increase in stiffness compared with a conventionally printed counterpart. Additional tests on a bunny head geometry and a topology-optimized geometry illustrate the framework's applicability to complex shapes with holes and varying cross-sections.

Compared with prior stress-aligned path planning methods, the authors emphasize that their approach produces trajectories with much lower line-spacing variance, making the results more uniformly manufacturable on real hardware.

## Key Contributions

- A stress-aligned non-planar print trajectory optimization method that enforces uniform layer height and line spacing constraints.
- A non-planar FFF framework capable of handling complex mechanical geometries containing holes and varying cross-sections.
- Experimental validation on a 5-axis printer using liquid crystal polymer, reporting a 44x improvement in failure strength and a 6x improvement in stiffness over conventional 2.5D printing.
- Quantitative demonstration of substantially lower line-spacing variance relative to previous stress-aligned printing methods.

## Relevance to Humanoid Robotics

Humanoid robots require lightweight, stiff, and strong structural links, brackets, and joints that can withstand repeated dynamic loads. The proposed method can improve the structural performance of anisotropic polymer parts by aligning material deposition with stress flow, potentially enabling material-efficient replacements for metal components in low- to medium-load applications. Because the approach is geometry-agnostic and compatible with 5-axis additive manufacturing, it could support the fabrication of customized, high-performance robotic structural parts without requiring extensive redesign for each load case.
