---
$id: ent_paper_ullah_three_dimensional_nonlinear_mi_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Three-dimensional nonlinear micro/meso-mechanical response of the fibre-reinforced polymer composites
  zh: 纤维增强聚合物复合材料的三维非线性微观/介观力学响应
  ko: 섬유 강화 폴리머 복합재의 3차원 비선형 미세/메조 역학 거동
summary:
  en: Presents a 3D multi-scale computational homogenisation framework for predicting the nonlinear micro/meso-mechanical
    response of fibre-reinforced polymer composites, incorporating matrix plasticity and fibre-matrix decohesion.
  zh: A three-dimensional multi-scale computational homogenisation framework is developed for the prediction of nonlinear
    micro/meso-mechanical response of the fibre-reinforced polymer (FRP) composites. Two dominant damage mechanisms, i.e.
    matrix elasto-plastic response and fibre-matrix decohesion are considered and modelled using a non-associative pressure
    dependent paraboloidal yield criterion and cohesive interface elements respectively. A linear-elastic transversely isotropic
    material model is used to model yarns/fibres within the representative volume element (RVE). A unified approach is used
    t
  ko: 섬유 강화 폴리머 복합재의 비선형 미세/메조 역학 거동을 예측하기 위해 기체 소성 및 섬유-기체 탈착을 포함하는 3차원 다중 척도 계산 균질화 프레임워크를 제시한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1610.04610v1.
sources:
- id: src_001
  type: paper
  title: Three-dimensional nonlinear micro/meso-mechanical response of the fibre-reinforced polymer composites
  url: https://arxiv.org/abs/1610.04610
  date: '2016'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
A three-dimensional multi-scale computational homogenisation framework is developed for the prediction of nonlinear micro/meso-mechanical response of the fibre-reinforced polymer (FRP) composites. Two dominant damage mechanisms, i.e. matrix elasto-plastic response and fibre-matrix decohesion are considered and modelled using a non-associative pressure dependent paraboloidal yield criterion and cohesive interface elements respectively. A linear-elastic transversely isotropic material model is used to model yarns/fibres within the representative volume element (RVE). A unified approach is used to impose the RVE boundary conditions, which allows convenient switching between linear displacement, uniform traction and periodic boundary conditions. The computational model is implemented within the framework of the hierarchic finite element, which permits the use of arbitrary orders of approximation. Furthermore, the computational framework is designed to take advantage of distributed memory high-performance computing. The accuracy and performance of the computational framework are demonstrated with a variety of numerical examples, including unidirectional FRP composite, a composite comprising a multi-fibre and multi-layer RVE, with randomly generated fibres, and a single layered plain weave textile composite. Results are validated against the reference experimental/numerical results from the literature. The computational framework is also used to study the effect of matrix and fibre-matrix interfaces properties on the homogenised stress-strain responses.

## 核心内容
A three-dimensional multi-scale computational homogenisation framework is developed for the prediction of nonlinear micro/meso-mechanical response of the fibre-reinforced polymer (FRP) composites. Two dominant damage mechanisms, i.e. matrix elasto-plastic response and fibre-matrix decohesion are considered and modelled using a non-associative pressure dependent paraboloidal yield criterion and cohesive interface elements respectively. A linear-elastic transversely isotropic material model is used to model yarns/fibres within the representative volume element (RVE). A unified approach is used to impose the RVE boundary conditions, which allows convenient switching between linear displacement, uniform traction and periodic boundary conditions. The computational model is implemented within the framework of the hierarchic finite element, which permits the use of arbitrary orders of approximation. Furthermore, the computational framework is designed to take advantage of distributed memory high-performance computing. The accuracy and performance of the computational framework are demonstrated with a variety of numerical examples, including unidirectional FRP composite, a composite comprising a multi-fibre and multi-layer RVE, with randomly generated fibres, and a single layered plain weave textile composite. Results are validated against the reference experimental/numerical results from the literature. The computational framework is also used to study the effect of matrix and fibre-matrix interfaces properties on the homogenised stress-strain responses.

## 参考
- http://arxiv.org/abs/1610.04610v1


