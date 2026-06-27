---
$id: ent_paper_ullah_three_dimensional_nonlinear_mi_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Three-dimensional nonlinear micro/meso-mechanical response of the fibre-reinforced
    polymer composites
  zh: 纤维增强聚合物复合材料的三维非线性微观/介观力学响应
  ko: 섬유 강화 폴리머 복합재의 3차원 비선형 미세/메조 역학 거동
summary:
  en: Presents a 3D multi-scale computational homogenisation framework for predicting
    the nonlinear micro/meso-mechanical response of fibre-reinforced polymer composites,
    incorporating matrix plasticity and fibre-matrix decohesion.
  zh: 提出了一种三维多尺度计算均匀化框架，用于预测纤维增强聚合物复合材料的非线性微观/介观力学响应，并考虑基体塑性和纤维-基体脱粘。
  ko: 섬유 강화 폴리머 복합재의 비선형 미세/메조 역학 거동을 예측하기 위해 기체 소성 및 섬유-기체 탈착을 포함하는 3차원 다중 척도 계산
    균질화 프레임워크를 제시한다.
domains:
- 01_raw_materials
- 06_design_engineering
- 05_mass_production
layers:
- midstream
- upstream
functional_roles:
- knowledge
- material
tags:
- fibre_reinforced_polymer_composites
- computational_homogenization
- multi_scale_modelling
- damage_mechanics
- lightweight_structural_materials
- polymer_matrix
- cohesive_interface
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Three-dimensional nonlinear micro/meso-mechanical response of the fibre-reinforced
    polymer composites
  url: https://arxiv.org/abs/1610.04610
  date: '2016'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper develops a fully three-dimensional, multi-scale computational homogenisation framework aimed at predicting the nonlinear mechanical behaviour of fibre-reinforced polymer (FRP) composites. It explicitly accounts for two dominant damage mechanisms: the elasto-plastic deformation of the polymer matrix and the progressive decohesion at the fibre-matrix interface. The matrix response is captured with a non-associative, pressure-dependent paraboloidal yield criterion, while cohesive interface elements represent interfacial failure. Yarns and fibres are treated as linear-elastic transversely isotropic materials within representative volume elements (RVEs). A unified boundary-condition formulation allows straightforward switching among linear displacement, uniform traction and periodic RVE boundary conditions.

The framework is implemented with hierarchic finite elements and parallelised for distributed-memory high-performance computing, enabling detailed 3D RVE analyses. The authors demonstrate accuracy and scalability for a unidirectional FRP, a multi-fibre multi-layer RVE, and a single-layer plain weave textile composite. Calibration of the matrix plasticity model against experimental epoxy data and validation of the RVE results against literature numerical and experimental data are also reported.

A parametric study examines how matrix and fibre-matrix interface properties influence the homogenised stress-strain response. The work highlights the importance of resolving micro/meso-scale nonlinear mechanisms for reliable macroscopic predictions of FRP composite behaviour.

## Key Contributions

- Development of a fully 3D nonlinear micro/meso-mechanical computational homogenisation framework for FRP composites.
- Unified imposition of RVE boundary conditions enabling convenient switching between displacement, traction and periodic conditions.
- Use of hierarchic finite elements and distributed-memory HPC for accuracy and scalability.
- Calibration and validation of the matrix plasticity model against experimental epoxy data and validation of UD, multi-layer and plain weave textile RVEs against literature.
- Parametric study of matrix and fibre-matrix interface properties on homogenised stress-strain responses.

## Relevance to Humanoid Robotics

Fibre-reinforced polymer composites with predictable nonlinear micro/meso-mechanical behaviour are attractive for humanoid robot structural shells, limbs and frames, where high specific strength, stiffness and durability are required. The paper's computational homogenisation framework supports informed material selection, virtual prototyping and quality assurance for lightweight composite components.

Because the framework links constituent properties and microstructural features to macroscopic nonlinear response, it can help engineers optimise composite layups and interfaces for robot mass production. Reliable prediction of matrix plasticity and fibre-matrix decohesion also aids in defining safety margins and inspection criteria for structural parts subjected to repeated loading.
