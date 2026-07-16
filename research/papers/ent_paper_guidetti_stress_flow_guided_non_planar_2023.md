---
$id: ent_paper_guidetti_stress_flow_guided_non_planar_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Stress Flow Guided Non-Planar Print Trajectory Optimization for Additive Manufacturing of Anisotropic Polymers
  zh: 各向异性聚合物增材制造中应力流引导的非平面打印轨迹优化
  ko: 이방성 폴리머 적층 제조를 위한 응력 흐름 기반 비평면 출력 궤적 최적화
summary:
  en: Presents a trajectory optimization framework that aligns non-planar fused filament fabrication paths with principal
    stress flow, demonstrating up to 44x failure strength and 6x stiffness improvements on a 5-axis printer using liquid crystal
    polymer.
  zh: When manufacturing parts using material extrusion additive manufacturing and anisotropic polymers, the mechanical properties
    of a manufactured component are strongly dependent on the print trajectory orientation. We conduct non-planar slicing
    and optimize the print trajectories to maximize the alignment between the material deposition direction and the stress
    flow induced by a predefined load case. The trajectory optimization framework considers manufacturability constraints
    in the form of uniform layer height and line spacing. We demonstrate the method by manufacturing a load bearing mechanic
  ko: 비평면 용융 필라멘트 제조 경로를 주 응력 흐름과 정렬하는 궤적 최적화 프레임워크를 제시하며, 액정 폴리머를 사용한 5축 프린터에서 최대 44배의 파괴 강도와 6배의 강성 향상을 입증하였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2301.04999v3.
sources:
- id: src_001
  type: paper
  title: Stress Flow Guided Non-Planar Print Trajectory Optimization for Additive Manufacturing of Anisotropic Polymers
  url: https://arxiv.org/abs/2301.04999
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
When manufacturing parts using material extrusion additive manufacturing and anisotropic polymers, the mechanical properties of a manufactured component are strongly dependent on the print trajectory orientation. We conduct non-planar slicing and optimize the print trajectories to maximize the alignment between the material deposition direction and the stress flow induced by a predefined load case. The trajectory optimization framework considers manufacturability constraints in the form of uniform layer height and line spacing. We demonstrate the method by manufacturing a load bearing mechanical bracket using a 5-axis 3D printer and a liquid crystal polymer material. The failure strength and stiffness of the optimized bracket are improved by a factor of 44 and 6 respectively when compared with conventional printing.

## 核心内容
When manufacturing parts using material extrusion additive manufacturing and anisotropic polymers, the mechanical properties of a manufactured component are strongly dependent on the print trajectory orientation. We conduct non-planar slicing and optimize the print trajectories to maximize the alignment between the material deposition direction and the stress flow induced by a predefined load case. The trajectory optimization framework considers manufacturability constraints in the form of uniform layer height and line spacing. We demonstrate the method by manufacturing a load bearing mechanical bracket using a 5-axis 3D printer and a liquid crystal polymer material. The failure strength and stiffness of the optimized bracket are improved by a factor of 44 and 6 respectively when compared with conventional printing.

## 参考
- http://arxiv.org/abs/2301.04999v3

## Overview
When manufacturing parts using material extrusion additive manufacturing and anisotropic polymers, the mechanical properties of a manufactured component are strongly dependent on the print trajectory orientation. We conduct non-planar slicing and optimize the print trajectories to maximize the alignment between the material deposition direction and the stress flow induced by a predefined load case. The trajectory optimization framework considers manufacturability constraints in the form of uniform layer height and line spacing. We demonstrate the method by manufacturing a load bearing mechanical bracket using a 5-axis 3D printer and a liquid crystal polymer material. The failure strength and stiffness of the optimized bracket are improved by a factor of 44 and 6 respectively when compared with conventional printing.

## Content
When manufacturing parts using material extrusion additive manufacturing and anisotropic polymers, the mechanical properties of a manufactured component are strongly dependent on the print trajectory orientation. We conduct non-planar slicing and optimize the print trajectories to maximize the alignment between the material deposition direction and the stress flow induced by a predefined load case. The trajectory optimization framework considers manufacturability constraints in the form of uniform layer height and line spacing. We demonstrate the method by manufacturing a load bearing mechanical bracket using a 5-axis 3D printer and a liquid crystal polymer material. The failure strength and stiffness of the optimized bracket are improved by a factor of 44 and 6 respectively when compared with conventional printing.

## 개요
재료 압출 적층 제조와 이방성 폴리머를 사용하여 부품을 제조할 때, 제조된 부품의 기계적 특성은 프린트 경로 방향에 크게 의존합니다. 우리는 비평면 슬라이싱을 수행하고 프린트 경로를 최적화하여 재료 증착 방향과 사전 정의된 하중 조건에 의해 유도된 응력 흐름 간의 정렬을 최대화합니다. 경로 최적화 프레임워크는 균일한 층 높이와 선 간격 형태의 제조 가능성 제약 조건을 고려합니다. 우리는 5축 3D 프린터와 액정 폴리머 재료를 사용하여 하중 지지 기계식 브래킷을 제조함으로써 이 방법을 입증합니다. 최적화된 브래킷의 파괴 강도와 강성은 기존 프린팅 방식과 비교하여 각각 44배와 6배 향상되었습니다.

## 핵심 내용
재료 압출 적층 제조와 이방성 폴리머를 사용하여 부품을 제조할 때, 제조된 부품의 기계적 특성은 프린트 경로 방향에 크게 의존합니다. 우리는 비평면 슬라이싱을 수행하고 프린트 경로를 최적화하여 재료 증착 방향과 사전 정의된 하중 조건에 의해 유도된 응력 흐름 간의 정렬을 최대화합니다. 경로 최적화 프레임워크는 균일한 층 높이와 선 간격 형태의 제조 가능성 제약 조건을 고려합니다. 우리는 5축 3D 프린터와 액정 폴리머 재료를 사용하여 하중 지지 기계식 브래킷을 제조함으로써 이 방법을 입증합니다. 최적화된 브래킷의 파괴 강도와 강성은 기존 프린팅 방식과 비교하여 각각 44배와 6배 향상되었습니다.
