---
$id: ent_paper_garrappa_numerical_evaluation_of_two_an_2015
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Numerical Evaluation of Two and Three Parameter Mittag–Leffler Functions
  zh: 双参数与三参数 Mittag–Leffler 函数的数值计算
  ko: 두 변수 및 세 변수 Mittag–Leffler 함수의 수치 평가
summary:
  en: Presents an optimal parabolic contour algorithm that evaluates the two- and
    three-parameter Mittag–Leffler functions by numerical inversion of their Laplace
    transforms, with error control and a public MATLAB implementation.
  zh: 提出一种基于最优抛物线围道的拉普拉斯变换数值反演算法，用于计算双参数与三参数 Mittag–Leffler 函数，并包含误差控制与公开的 MATLAB
    实现。
  ko: 최적 포물선 경로를 이용한 라플라스 변환 수치 역변환 알고리즘을 제안하여 2-변수 및 3-변수 Mittag–Leffler 함수를 평가하고,
    오차 제어와 공개 MATLAB 구현을 제공한다.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- fractional_calculus
- mittag_leffler_function
- prabhakar_function
- laplace_transform_inversion
- optimal_parabolic_contour
- numerical_integration
- viscoelasticity
- control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; exact section-level citations
    were not verified against the full paper.
sources:
- id: src_001
  type: paper
  title: Numerical Evaluation of Two and Three Parameter Mittag–Leffler Functions
  url: https://arxiv.org/abs/1503.06569
  date: '2015'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Mittag–Leffler functions are central to fractional calculus, but their numerical evaluation over the complex plane is challenging: direct series summation can converge very slowly or overflow, and existing algorithms are often inaccurate or computationally uneven. This paper proposes an optimal parabolic contour (OPC) scheme that evaluates the two-parameter Mittag–Leffler function by numerically inverting its Laplace transform. The contour shape and quadrature parameters are chosen according to the location and strength of the Laplace-transform singularities, balancing discretization, truncation, and round-off errors.

The algorithm uses the trapezoidal rule along a parabolic contour in the complex plane. The authors derive practical rules for selecting contour parameters so that the overall computational cost is minimized while preserving accuracy. They also extend the approach to the three-parameter Mittag–Leffler function, commonly called the Prabhakar function, under restrictions on the parameters. A public MATLAB implementation is provided and tested against variable-precision reference values.

## Key Contributions

- Optimal parabolic contour algorithm for Laplace-transform inversion of the Mittag–Leffler function.
- Error analysis and parameter-selection strategy tied to the singularities of the Laplace transform.
- Extension of the method to the three-parameter (Prabhakar) Mittag–Leffler function.
- Public MATLAB code and numerical validation against variable-precision reference values.

## Relevance to Humanoid Robotics

The paper does not address humanoid robot hardware or deployment directly. Its relevance is indirect: fractional-order dynamics, viscoelastic material models, and advanced control formulations used in humanoid locomotion and actuation can require repeated evaluation of Mittag–Leffler functions. A robust and efficient numerical method for these functions therefore supports modeling and simulation work in humanoid design engineering and component-level material/control analysis.
