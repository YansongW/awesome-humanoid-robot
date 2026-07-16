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

## Overview
A three-dimensional multi-scale computational homogenisation framework is developed for the prediction of nonlinear micro/meso-mechanical response of the fibre-reinforced polymer (FRP) composites. Two dominant damage mechanisms, i.e. matrix elasto-plastic response and fibre-matrix decohesion are considered and modelled using a non-associative pressure dependent paraboloidal yield criterion and cohesive interface elements respectively. A linear-elastic transversely isotropic material model is used to model yarns/fibres within the representative volume element (RVE). A unified approach is used to impose the RVE boundary conditions, which allows convenient switching between linear displacement, uniform traction and periodic boundary conditions. The computational model is implemented within the framework of the hierarchic finite element, which permits the use of arbitrary orders of approximation. Furthermore, the computational framework is designed to take advantage of distributed memory high-performance computing. The accuracy and performance of the computational framework are demonstrated with a variety of numerical examples, including unidirectional FRP composite, a composite comprising a multi-fibre and multi-layer RVE, with randomly generated fibres, and a single layered plain weave textile composite. Results are validated against the reference experimental/numerical results from the literature. The computational framework is also used to study the effect of matrix and fibre-matrix interfaces properties on the homogenised stress-strain responses.

## Content
A three-dimensional multi-scale computational homogenisation framework is developed for the prediction of nonlinear micro/meso-mechanical response of the fibre-reinforced polymer (FRP) composites. Two dominant damage mechanisms, i.e. matrix elasto-plastic response and fibre-matrix decohesion are considered and modelled using a non-associative pressure dependent paraboloidal yield criterion and cohesive interface elements respectively. A linear-elastic transversely isotropic material model is used to model yarns/fibres within the representative volume element (RVE). A unified approach is used to impose the RVE boundary conditions, which allows convenient switching between linear displacement, uniform traction and periodic boundary conditions. The computational model is implemented within the framework of the hierarchic finite element, which permits the use of arbitrary orders of approximation. Furthermore, the computational framework is designed to take advantage of distributed memory high-performance computing. The accuracy and performance of the computational framework are demonstrated with a variety of numerical examples, including unidirectional FRP composite, a composite comprising a multi-fibre and multi-layer RVE, with randomly generated fibres, and a single layered plain weave textile composite. Results are validated against the reference experimental/numerical results from the literature. The computational framework is also used to study the effect of matrix and fibre-matrix interfaces properties on the homogenised stress-strain responses.

## 개요
섬유 강화 폴리머(FRP) 복합재의 비선형 미시/중간 역학적 응답을 예측하기 위해 3차원 다중 스케일 계산 균질화 프레임워크가 개발되었습니다. 두 가지 주요 손상 메커니즘, 즉 매트릭스의 탄소성 응답과 섬유-매트릭스 분리는 각각 비연관 압력 의존 포물선 항복 기준과 응집 계면 요소를 사용하여 고려 및 모델링되었습니다. 선형 탄성 횡등방성 재료 모델은 대표 체적 요소(RVE) 내의 얀/섬유를 모델링하는 데 사용됩니다. RVE 경계 조건을 부과하기 위해 통합 접근법이 사용되며, 이를 통해 선형 변위, 균일 트랙션 및 주기적 경계 조건 간의 편리한 전환이 가능합니다. 계산 모델은 계층적 유한 요소 프레임워크 내에서 구현되어 임의의 근사 차수를 사용할 수 있습니다. 또한, 계산 프레임워크는 분산 메모리 고성능 컴퓨팅을 활용하도록 설계되었습니다. 계산 프레임워크의 정확성과 성능은 단방향 FRP 복합재, 무작위로 생성된 섬유를 포함하는 다중 섬유 및 다층 RVE로 구성된 복합재, 단일 층 평직 직물 복합재를 포함한 다양한 수치 예제를 통해 입증되었습니다. 결과는 문헌의 참조 실험/수치 결과와 비교하여 검증되었습니다. 계산 프레임워크는 또한 균질화된 응력-변형률 응답에 대한 매트릭스 및 섬유-매트릭스 계면 특성의 영향을 연구하는 데 사용되었습니다.

## 핵심 내용
섬유 강화 폴리머(FRP) 복합재의 비선형 미시/중간 역학적 응답을 예측하기 위해 3차원 다중 스케일 계산 균질화 프레임워크가 개발되었습니다. 두 가지 주요 손상 메커니즘, 즉 매트릭스의 탄소성 응답과 섬유-매트릭스 분리는 각각 비연관 압력 의존 포물선 항복 기준과 응집 계면 요소를 사용하여 고려 및 모델링되었습니다. 선형 탄성 횡등방성 재료 모델은 대표 체적 요소(RVE) 내의 얀/섬유를 모델링하는 데 사용됩니다. RVE 경계 조건을 부과하기 위해 통합 접근법이 사용되며, 이를 통해 선형 변위, 균일 트랙션 및 주기적 경계 조건 간의 편리한 전환이 가능합니다. 계산 모델은 계층적 유한 요소 프레임워크 내에서 구현되어 임의의 근사 차수를 사용할 수 있습니다. 또한, 계산 프레임워크는 분산 메모리 고성능 컴퓨팅을 활용하도록 설계되었습니다. 계산 프레임워크의 정확성과 성능은 단방향 FRP 복합재, 무작위로 생성된 섬유를 포함하는 다중 섬유 및 다층 RVE로 구성된 복합재, 단일 층 평직 직물 복합재를 포함한 다양한 수치 예제를 통해 입증되었습니다. 결과는 문헌의 참조 실험/수치 결과와 비교하여 검증되었습니다. 계산 프레임워크는 또한 균질화된 응력-변형률 응답에 대한 매트릭스 및 섬유-매트릭스 계면 특성의 영향을 연구하는 데 사용되었습니다.
