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
  en: This paper proposes a lumped-parameter soft finger model with linear three-element viscoelastic joints to capture creep
    behavior, treats viscoelastic parameters and initial joint angles as stochastic distributions, and validates the resulting
    joint-angle probability densities and Sobol sensitivity indices against 100 experimental trials.
  zh: 本文提出了具有线性三元件黏弹性关节的集中参数软体手指模型以刻画蠕变行为，将黏弹性参数与初始关节角表示为随机分布，通过随机变量变换获得关节角度概率密度，并利用100次实验验证结果及Sobol敏感性指标。
  ko: 본 논문은 크리프 거동을 포착하기 위해 선형 3요소 점탄성 관절을 갖는 집중 파라미터 소프트 핑거 모델을 제안하고, 점탄성 파라미터와 초기 관절각을 확률 분포로 표현하여 확률변수 변환으로 관절각 확률 밀도를
    분석하고 100회 실험으로 검증한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.07035v1.
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
## 概述
Soft robots have high adaptability and safeness which are derived from their softness, and therefore it is paid attention to use them in human society. However, the controllability of soft robots is not enough to perform dexterous behaviors when considering soft robots as alternative laborers for humans. The model-based control is effective to achieve dexterous behaviors. When considering building a model which is suitable for control, there are problems based on their special properties such as the creep behavior or the variability of motion. In this paper, the lumped parameterized model with viscoelastic joints for a soft finger is established for the creep behavior. Parameters are expressed as distributions, which makes it possible to take into account the variability of motion. Furthermore, stochastic analyses are performed based on the parameters' distribution. They show high adaptivity compared with experimental results and also enable the investigation of the effects of parameters for robots' variability.

## 核心内容
Soft robots have high adaptability and safeness which are derived from their softness, and therefore it is paid attention to use them in human society. However, the controllability of soft robots is not enough to perform dexterous behaviors when considering soft robots as alternative laborers for humans. The model-based control is effective to achieve dexterous behaviors. When considering building a model which is suitable for control, there are problems based on their special properties such as the creep behavior or the variability of motion. In this paper, the lumped parameterized model with viscoelastic joints for a soft finger is established for the creep behavior. Parameters are expressed as distributions, which makes it possible to take into account the variability of motion. Furthermore, stochastic analyses are performed based on the parameters' distribution. They show high adaptivity compared with experimental results and also enable the investigation of the effects of parameters for robots' variability.

## 参考
- http://arxiv.org/abs/2306.07035v1

## Overview
Soft robots have high adaptability and safeness which are derived from their softness, and therefore it is paid attention to use them in human society. However, the controllability of soft robots is not enough to perform dexterous behaviors when considering soft robots as alternative laborers for humans. The model-based control is effective to achieve dexterous behaviors. When considering building a model which is suitable for control, there are problems based on their special properties such as the creep behavior or the variability of motion. In this paper, the lumped parameterized model with viscoelastic joints for a soft finger is established for the creep behavior. Parameters are expressed as distributions, which makes it possible to take into account the variability of motion. Furthermore, stochastic analyses are performed based on the parameters' distribution. They show high adaptivity compared with experimental results and also enable the investigation of the effects of parameters for robots' variability.

## Content
Soft robots have high adaptability and safeness which are derived from their softness, and therefore it is paid attention to use them in human society. However, the controllability of soft robots is not enough to perform dexterous behaviors when considering soft robots as alternative laborers for humans. The model-based control is effective to achieve dexterous behaviors. When considering building a model which is suitable for control, there are problems based on their special properties such as the creep behavior or the variability of motion. In this paper, the lumped parameterized model with viscoelastic joints for a soft finger is established for the creep behavior. Parameters are expressed as distributions, which makes it possible to take into account the variability of motion. Furthermore, stochastic analyses are performed based on the parameters' distribution. They show high adaptivity compared with experimental results and also enable the investigation of the effects of parameters for robots' variability.

## 개요
소프트 로봇은 유연성에서 비롯된 높은 적응성과 안전성을 가지며, 이로 인해 인간 사회에서의 활용이 주목받고 있습니다. 그러나 소프트 로봇을 인간의 대체 노동자로 고려할 때, 정교한 동작을 수행하기에는 제어성이 충분하지 않습니다. 모델 기반 제어는 정교한 동작을 달성하는 데 효과적입니다. 제어에 적합한 모델을 구축할 때는 크리프 거동이나 운동의 변동성과 같은 특수한 특성에 기반한 문제들이 존재합니다. 본 논문에서는 크리프 거동을 위해 소프트 핑거의 점탄성 관절을 가진 집중 매개변수 모델을 구축합니다. 매개변수는 분포로 표현되어 운동의 변동성을 고려할 수 있게 합니다. 또한, 매개변수 분포를 기반으로 확률론적 분석을 수행합니다. 이는 실험 결과와 비교하여 높은 적응성을 보여주며, 로봇의 변동성에 대한 매개변수의 영향을 조사할 수 있게 합니다.

## 핵심 내용
소프트 로봇은 유연성에서 비롯된 높은 적응성과 안전성을 가지며, 이로 인해 인간 사회에서의 활용이 주목받고 있습니다. 그러나 소프트 로봇을 인간의 대체 노동자로 고려할 때, 정교한 동작을 수행하기에는 제어성이 충분하지 않습니다. 모델 기반 제어는 정교한 동작을 달성하는 데 효과적입니다. 제어에 적합한 모델을 구축할 때는 크리프 거동이나 운동의 변동성과 같은 특수한 특성에 기반한 문제들이 존재합니다. 본 논문에서는 크리프 거동을 위해 소프트 핑거의 점탄성 관절을 가진 집중 매개변수 모델을 구축합니다. 매개변수는 분포로 표현되어 운동의 변동성을 고려할 수 있게 합니다. 또한, 매개변수 분포를 기반으로 확률론적 분석을 수행합니다. 이는 실험 결과와 비교하여 높은 적응성을 보여주며, 로봇의 변동성에 대한 매개변수의 영향을 조사할 수 있게 합니다.
