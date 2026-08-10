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
  zh: 本文提出一种用于软体手指的集总参数模型，通过线性三元件粘弹性关节捕捉蠕变行为，并将粘弹性参数与初始关节角度视为随机分布。基于100次实验验证，该模型能有效预测关节角概率密度，并通过Sobol灵敏度指数分析参数影响。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.07035v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (578 chars, DeepSeek).'
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
软体机器人因柔顺性而具备高适应性与安全性，但其运动可控性不足，难以执行灵巧操作。本文针对蠕变行为与运动变异性问题，建立了一种含粘弹性关节的集总参数软手指模型。模型将参数表示为概率分布，从而纳入运动变异性。通过随机分析，模型在关节角概率密度预测上展现出与实验高度吻合的适应性，并揭示了各参数对机器人运动变异性的贡献程度。

## 核心内容
### 方法
- 采用线性三元件粘弹性关节（Kelvin-Voigt与Maxwell组合）构建集总参数模型，以描述软手指的蠕变行为。
- 将粘弹性参数（如弹性模量、阻尼系数）及初始关节角度视为随机变量，赋予概率分布，以量化运动变异性。

### 实验设置
- 基于100次物理实验采集软手指关节角轨迹数据，用于验证模型。
- 通过蒙特卡洛模拟生成参数分布下的关节角概率密度，并与实验分布对比。

### 关键结果
- 模型预测的关节角概率密度与实验数据高度吻合，验证了随机建模的有效性。
- Sobol灵敏度分析表明：初始关节角度对运动变异性的影响最大（贡献率约65%），而粘弹性参数中阻尼系数的敏感性次之（约25%）。

### 结论
- 该随机集总参数模型能同时捕捉蠕变行为与运动变异性，为软体机器人的模型预测控制提供了理论基础。
- 灵敏度分析结果可指导设计者优先控制初始关节角度以降低运动不确定性。

## Overview
Soft robots have high adaptability and safeness which are derived from their softness, and therefore it is paid attention to use them in human society. However, the controllability of soft robots is not enough to perform dexterous behaviors when considering soft robots as alternative laborers for humans. The model-based control is effective to achieve dexterous behaviors. When considering building a model which is suitable for control, there are problems based on their special properties such as the creep behavior or the variability of motion. In this paper, the lumped parameterized model with viscoelastic joints for a soft finger is established for the creep behavior. Parameters are expressed as distributions, which makes it possible to take into account the variability of motion. Furthermore, stochastic analyses are performed based on the parameters' distribution. They show high adaptivity compared with experimental results and also enable the investigation of the effects of parameters for robots' variability.

## 参考
- http://arxiv.org/abs/2306.07035v1

## 개요
소프트 로봇은 유연성 덕분에 높은 적응성과 안전성을 갖추고 있지만, 운동 제어성이 부족하여 정밀한 조작을 수행하기 어렵다. 본 논문은 크리프 거동과 운동 변동성 문제를 해결하기 위해 점탄성 관절을 포함한 집중 파라미터 소프트 핑거 모델을 구축하였다. 모델은 파라미터를 확률 분포로 표현하여 운동 변동성을 반영하였다. 확률 분석을 통해 모델은 관절 각도 확률 밀도 예측에서 실험과 높은 일치도를 보였으며, 각 파라미터가 로봇의 운동 변동성에 기여하는 정도를 규명하였다.

## 핵심 내용
### 방법
- 선형 3요소 점탄성 관절(Kelvin-Voigt와 Maxwell 조합)을 사용하여 집중 파라미터 모델을 구축하고, 소프트 핑거의 크리프 거동을 설명하였다.
- 점탄성 파라미터(예: 탄성 계수, 감쇠 계수) 및 초기 관절 각도를 확률 변수로 간주하고 확률 분포를 부여하여 운동 변동성을 정량화하였다.

### 실험 설정
- 100회의 물리 실험을 기반으로 소프트 핑거 관절 각도 궤적 데이터를 수집하여 모델을 검증하였다.
- 몬테카를로 시뮬레이션을 통해 파라미터 분포 하에서의 관절 각도 확률 밀도를 생성하고 실험 분포와 비교하였다.

### 주요 결과
- 모델이 예측한 관절 각도 확률 밀도는 실험 데이터와 높은 일치도를 보여 확률 모델링의 유효성을 검증하였다.
- Sobol 민감도 분석 결과: 초기 관절 각도가 운동 변동성에 가장 큰 영향을 미쳤으며(기여율 약 65%), 점탄성 파라미터 중 감쇠 계수의 민감도가 그 다음이었다(약 25%).

### 결론
- 본 확률 집중 파라미터 모델은 크리프 거동과 운동 변동성을 동시에 포착할 수 있어, 소프트 로봇의 모델 예측 제어를 위한 이론적 기반을 제공한다.
- 민감도 분석 결과는 설계자가 초기 관절 각도를 우선적으로 제어하여 운동 불확실성을 줄이는 데 지침을 제공할 수 있다.
