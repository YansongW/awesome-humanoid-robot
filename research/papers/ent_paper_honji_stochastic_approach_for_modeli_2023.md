---
$id: ent_paper_honji_stochastic_approach_for_modeli_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Stochastic Approach for Modeling the Soft Finger with the Creep Behavior
  zh: 软体手指蠕变行为的随机建模方法
  ko: 크리프 거동을 갖는 소프트 핑거의 확률적 모델링 접근
summary:
  en: This paper proposes a lumped-parameter soft finger model with linear three-element
    viscoelastic joints to capture creep behavior, treats viscoelastic parameters
    and initial joint angles as stochastic distributions, and validates the resulting
    joint-angle probability densities and Sobol sensitivity indices against 100 experimental
    trials.
  zh: 本文提出了具有线性三元件黏弹性关节的集中参数软体手指模型以刻画蠕变行为，将黏弹性参数与初始关节角表示为随机分布，通过随机变量变换获得关节角度概率密度，并利用100次实验验证结果及Sobol敏感性指标。
  ko: 본 논문은 크리프 거동을 포착하기 위해 선형 3요소 점탄성 관절을 갖는 집중 파라미터 소프트 핑거 모델을 제안하고, 점탄성 파라미터와 초기
    관절각을 확률 분포로 표현하여 확률변수 변환으로 관절각 확률 밀도를 분석하고 100회 실험으로 검증한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- soft_finger
- creep_behavior
- viscoelastic_joint
- lumped_parameter_model
- stochastic_modeling
- random_variable_transformation
- sobol_sensitivity_analysis
- model_based_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv LaTeX source (v1, 2023-06-12); component manufacturers
    ESCON/Maxon mentioned in supplied metadata were not found in the source and were
    omitted.
sources:
- id: src_001
  type: paper
  title: Stochastic Approach for Modeling the Soft Finger with the Creep Behavior
  url: https://arxiv.org/abs/2306.07035
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper targets the control of soft robots in human environments, where softness provides adaptability and safety but also introduces creep and trial-to-trial motion variability. To enable model-based control, the authors derive a lumped-parameter model of a 3-link soft finger whose joints are represented by linear three-element viscoelastic elements: a parallel spring-damper pair models viscoelastic behavior, while a series damper captures plastic deformation and creep. The full-body dynamics are built with a Lagrangian serial-link formulation and wire-actuation mapping.

For tractability, the authors assume negligible inertia and nonlinear terms and a constant joint torque input, obtaining an explicit analytical solution for joint displacement. They estimate viscoelastic parameters from 100 repeated constant-force experiments and model each parameter as a log-normal distribution. Using the random-variable transformation, they propagate parameter uncertainty into joint-angle probability density functions. A Sobol sensitivity analysis then reveals which parameters dominate the variance of each joint over time.

The stochastic predictions closely match the experimental mean and standard deviation, including the creep and transient responses. The authors also note remaining discrepancies at the distal joint, attributing them to accumulated measurement errors and wider parameter distributions.

## Key Contributions

- Lumped-parameter soft finger model with three-element viscoelastic joints that captures creep behavior and transient response.
- Representation of viscoelastic parameters and initial joint angles as stochastic distributions to account for motion variability.
- Analytical solution of joint displacement for constant-torque step inputs.
- Stochastic analysis via random-variable transformation validated against 100 experimental trials.
- Sobol sensitivity analysis revealing time-varying parameter influences on joint-angle variability.

## Relevance to Humanoid Robotics

Soft fingers are promising end-effectors for humanoid robots that must manipulate fragile or irregularly shaped objects safely in unstructured human environments. Reliable model-based control of these fingers requires accounting for creep and variability inherent to soft materials. The paper's computationally efficient lumped-parameter stochastic model provides a foundation for real-time observers and controllers, as well as a sensitivity-driven design tool for improving reproducibility in soft robotic hands.
