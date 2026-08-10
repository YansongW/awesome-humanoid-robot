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
  zh: 本文提出了一种三维多尺度计算均匀化框架，用于预测纤维增强聚合物复合材料在微观/细观尺度下的非线性力学响应。该框架由研究团队开发，核心贡献在于同时考虑了基体弹塑性行为与纤维-基体脱粘两种主要损伤机制，并采用非关联压力依赖抛物面屈服准则和粘性界面单元进行建模。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1610.04610v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (600 chars, DeepSeek).'
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
该研究构建了一个三维多尺度计算均匀化框架，旨在预测纤维增强聚合物复合材料在微观/细观尺度下的非线性力学响应。框架整合了基体弹塑性响应与纤维-基体脱粘两种关键损伤机制，分别通过非关联压力依赖抛物面屈服准则和粘性界面单元进行模拟。纱线/纤维采用线弹性横观各向同性材料模型，并通过统一方法施加代表性体积单元边界条件，支持线性位移、均匀牵引和周期性边界条件的灵活切换。计算模型基于分层有限元框架实现，允许使用任意阶近似，并针对分布式内存高性能计算进行了优化。

## 核心内容
### 方法
- 采用三维多尺度计算均匀化框架，结合基体弹塑性（非关联压力依赖抛物面屈服准则）与纤维-基体脱粘（粘性界面单元）两种损伤机制。
- 纱线/纤维使用线弹性横观各向同性材料模型，代表性体积单元边界条件通过统一方法施加，支持线性位移、均匀牵引和周期性边界条件的切换。
- 计算模型基于分层有限元框架，允许任意阶近似，并针对分布式内存高性能计算进行优化。

### 实验设置
- 数值示例包括：单向FRP复合材料、含随机生成纤维的多纤维多层RVE复合材料、单层平纹编织复合材料。
- 结果与文献中的参考实验/数值结果进行验证。

### 关键数字与结论
- 框架成功预测了不同复合材料结构在微观/细观尺度下的非线性响应。
- 研究了基体与纤维-基体界面特性对均匀化应力-应变响应的影响，验证了框架的准确性与性能。

## Overview
A three-dimensional multi-scale computational homogenisation framework is developed for the prediction of nonlinear micro/meso-mechanical response of the fibre-reinforced polymer (FRP) composites. Two dominant damage mechanisms, i.e. matrix elasto-plastic response and fibre-matrix decohesion are considered and modelled using a non-associative pressure dependent paraboloidal yield criterion and cohesive interface elements respectively. A linear-elastic transversely isotropic material model is used to model yarns/fibres within the representative volume element (RVE). A unified approach is used to impose the RVE boundary conditions, which allows convenient switching between linear displacement, uniform traction and periodic boundary conditions. The computational model is implemented within the framework of the hierarchic finite element, which permits the use of arbitrary orders of approximation. Furthermore, the computational framework is designed to take advantage of distributed memory high-performance computing. The accuracy and performance of the computational framework are demonstrated with a variety of numerical examples, including unidirectional FRP composite, a composite comprising a multi-fibre and multi-layer RVE, with randomly generated fibres, and a single layered plain weave textile composite. Results are validated against the reference experimental/numerical results from the literature. The computational framework is also used to study the effect of matrix and fibre-matrix interfaces properties on the homogenised stress-strain responses.

## 参考
- http://arxiv.org/abs/1610.04610v1

## 개요
본 연구는 섬유 강화 폴리머 복합재료의 미시/세시 규모에서 비선형 역학 응답을 예측하기 위한 3차원 다중 스케일 계산 균질화 프레임워크를 구축하였다. 이 프레임워크는 기지재의 탄소성 응답과 섬유-기지재 계면 박리라는 두 가지 주요 손상 메커니즘을 통합하며, 각각 비연관 압력 의존 포물면 항복 기준과 점성 계면 요소를 통해 모사된다. 토우/섬유는 선형 탄성 횡등방성 재료 모델을 사용하며, 대표 체적 요소 경계 조건은 통일된 방법으로 적용되어 선형 변위, 균일 견인, 주기적 경계 조건 간의 유연한 전환을 지원한다. 계산 모델은 계층적 유한 요소 프레임워크를 기반으로 구현되어 임의 차수 근사를 허용하며, 분산 메모리 고성능 컴퓨팅에 최적화되었다.

## 핵심 내용
### 방법
- 3차원 다중 스케일 계산 균질화 프레임워크를 채택하고, 기지재 탄소성(비연관 압력 의존 포물면 항복 기준)과 섬유-기지재 계면 박리(점성 계면 요소)라는 두 가지 손상 메커니즘을 결합.
- 토우/섬유는 선형 탄성 횡등방성 재료 모델을 사용하며, 대표 체적 요소 경계 조건은 통일된 방법으로 적용되어 선형 변위, 균일 견인, 주기적 경계 조건 간 전환을 지원.
- 계산 모델은 계층적 유한 요소 프레임워크를 기반으로 하여 임의 차수 근사를 허용하며, 분산 메모리 고성능 컴퓨팅에 최적화.

### 실험 설정
- 수치 예시에는 단방향 FRP 복합재료, 무작위 생성 섬유를 포함한 다중 섬유 다층 RVE 복합재료, 단층 평직 직물 복합재료가 포함됨.
- 결과는 문헌의 참조 실험/수치 결과와 검증됨.

### 주요 수치 및 결론
- 프레임워크는 다양한 복합재료 구조의 미시/세시 규모에서 비선형 응답을 성공적으로 예측.
- 기지재와 섬유-기지재 계면 특성이 균질화 응력-변형률 응답에 미치는 영향을 연구하여 프레임워크의 정확성과 성능을 검증.
