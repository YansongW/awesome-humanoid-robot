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
  en: Presents an optimal parabolic contour algorithm that evaluates the two- and three-parameter Mittag–Leffler functions
    by numerical inversion of their Laplace transforms, with error control and a public MATLAB implementation.
  zh: 提出一种基于最优抛物线围道的拉普拉斯变换数值反演算法，用于计算双参数与三参数 Mittag–Leffler 函数，并包含误差控制与公开的 MATLAB 实现。
  ko: 최적 포물선 경로를 이용한 라플라스 변환 수치 역변환 알고리즘을 제안하여 2-변수 및 3-변수 Mittag–Leffler 함수를 평가하고, 오차 제어와 공개 MATLAB 구현을 제공한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1503.06569v2.
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
## 概述
The Mittag-Leffler (ML) function plays a fundamental role in fractional calculus but very few methods are available for its numerical evaluation. In this work we present a method for the efficient computation of the ML function based on the numerical inversion of its Laplace transform (LT): an optimal parabolic contour is selected on the basis of the distance and the strength of the singularities of the LT, with the aim of minimizing the computational effort and reduce the propagation of errors. Numerical experiments are presented to show accuracy and efficiency of the proposed approach. The application to the three parameter ML (also known as Prabhakar) function is also presented.

## 核心内容
The Mittag-Leffler (ML) function plays a fundamental role in fractional calculus but very few methods are available for its numerical evaluation. In this work we present a method for the efficient computation of the ML function based on the numerical inversion of its Laplace transform (LT): an optimal parabolic contour is selected on the basis of the distance and the strength of the singularities of the LT, with the aim of minimizing the computational effort and reduce the propagation of errors. Numerical experiments are presented to show accuracy and efficiency of the proposed approach. The application to the three parameter ML (also known as Prabhakar) function is also presented.

## 参考
- http://arxiv.org/abs/1503.06569v2

