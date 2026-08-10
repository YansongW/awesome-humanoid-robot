---
$id: ent_paper_kolzenberg_a_four_parameter_model_for_the_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A four parameter model for the solid-electrolyte interphase to predict battery aging during operation
  zh: 用于预测运行中电池老化的固体电解质界面膜四参数模型
  ko: 작동 중 배터리 노화 예측을 위한 고체 전해질 계면(SEI) 4개 매개변수 모델
summary:
  en: The paper presents a four-parameter physics-based SEI-growth model that predicts lithium-ion capacity fade using only
    three parametrization protocols plus the anode OCV curve, validated on 25 independent aging protocols with 1.28% RMSE.
  zh: 本文提出一个基于物理的四参数SEI生长模型，用于预测锂离子电池容量衰减。该模型仅需三种参数化协议和阳极OCV曲线即可完成校准，在25种独立老化协议上验证的RMSE为1.28%。
  ko: 본 논문은 세 가지 매개변수화 프로토콜과 양극 개회로 전압 곡선만을 사용하여 리튬 이온 배터리 용량 감소를 예측하는 물리 기반 SEI 성장 4개 매개변수 모델을 제시하며, 25개의 독립 노화 프로토콜에서 1.28%
    RMSE로 검증되었다.
domains:
- 02_components
- 05_mass_production
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- component
tags:
- battery_aging
- solid_electrolyte_interphase
- lithium_ion_battery
- capacity_fade_prediction
- physics_based_model
- energy_storage
- automotive_battery
- humanoid_power_system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2112.13671v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (576 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A four parameter model for the solid-electrolyte interphase to predict battery aging during operation
  url: https://arxiv.org/abs/2112.13671
  date: '2022'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
该研究针对锂离子电池老化预测的挑战，开发了一个物理驱动的SEI生长模型。模型包含四个参数，分别描述时间、电流、温度以及荷电状态的影响，其中荷电状态依赖性来自阳极开路电压曲线。在62个汽车级电池、28种老化协议的数据集上，模型通过三种协议完成参数化，并在剩余25种协议上展现出高预测精度（RMSE 1.28%）。案例研究表明，工作窗口（最大/最小荷电状态）对SEI生长影响最大，而施加电流的影响几乎可忽略。

## 核心内容
### 模型架构
- 基于物理的SEI生长模型，包含四个参数：时间依赖性参数、电流依赖性参数、温度依赖性参数，以及通过阳极OCV曲线推导的荷电状态依赖性参数。
- 模型仅需三种参数化协议即可完成校准，无需大量数据集。

### 实验设置
- 数据集：62个汽车级锂离子电池，经历28种不同老化协议。
- 参数化：使用其中3种协议确定模型的时间、电流和温度参数。
- 验证：剩余25种协议用于模型验证，计算RMSE。

### 关键结果
- 模型预测的RMSE为1.28%，表明高预测精度。
- 案例研究显示，工作窗口（最大/最小荷电状态）是影响SEI生长的最大因素。
- 施加电流对SEI生长的影响几乎可忽略。

### 结论
该四参数物理模型为理解和预测锂离子电池老化提供了有效工具，尤其适用于新工况下的外推预测。

## Overview
Accurately predicting aging of lithium-ion batteries would help to prolong their lifespan, but remains a challenge owing to the complexity and interrelation of different aging mechanisms. As a result, aging prediction often relies on empirical or data-driven approaches, which obtain their performance from analyzing large datasets. However, these datasets are expensive to generate and the models are agnostic of the underlying physics and thus difficult to extrapolate to new conditions. In this article, a physical model is used to predict capacity fade caused by solid-electrolyte interphase (SEI) growth in 62 automotive cells, aged with 28 different protocols. Three protocols parametrize the time, current and temperature dependence of the model, the state of charge dependence results from the anode's open circuit voltage curve. The model validation with the remaining 25 protocols shows a high predictivity with a root-mean squared error of $1.28\%$. A case study with the so-validated model shows that the operating window, i.e. maximum and minimum state of charge, has the largest impact on SEI growth, while the influence of the applied current is almost negligible. Thereby the presented model is a promising approach to better understand, quantify and predict aging of lithium-ion batteries.

## 参考
- http://arxiv.org/abs/2112.13671v2

## 개요
이 연구는 리튬이온 배터리 노화 예측의 도전 과제를 해결하기 위해 물리 기반 SEI 성장 모델을 개발했습니다. 모델은 시간, 전류, 온도 및 충전 상태의 영향을 각각 설명하는 네 개의 매개변수를 포함하며, 충전 상태 의존성은 양극 개방 회로 전압 곡선에서 도출됩니다. 62개의 자동차급 배터리, 28가지 노화 프로토콜 데이터 세트에서 모델은 세 가지 프로토콜로 매개변수화되었고, 나머지 25가지 프로토콜에서 높은 예측 정확도(RMSE 1.28%)를 보였습니다. 사례 연구에 따르면 작동 창(최대/최소 충전 상태)이 SEI 성장에 가장 큰 영향을 미치며, 인가 전류의 영향은 거의 무시할 수 있습니다.

## 핵심 내용
### 모델 아키텍처
- 물리 기반 SEI 성장 모델로, 시간 의존성 매개변수, 전류 의존성 매개변수, 온도 의존성 매개변수, 그리고 양극 OCV 곡선에서 도출된 충전 상태 의존성 매개변수의 네 가지 매개변수를 포함합니다.
- 모델은 세 가지 매개변수화 프로토콜만으로 보정이 가능하며, 대규모 데이터 세트가 필요하지 않습니다.

### 실험 설정
- 데이터 세트: 62개의 자동차급 리튬이온 배터리, 28가지 다양한 노화 프로토콜을 경험.
- 매개변수화: 그중 3가지 프로토콜을 사용하여 모델의 시간, 전류 및 온도 매개변수를 결정.
- 검증: 나머지 25가지 프로토콜을 모델 검증에 사용하여 RMSE를 계산.

### 주요 결과
- 모델 예측의 RMSE는 1.28%로 높은 예측 정확도를 나타냄.
- 사례 연구에 따르면 작동 창(최대/최소 충전 상태)이 SEI 성장에 영향을 미치는 가장 큰 요인임.
- 인가 전류가 SEI 성장에 미치는 영향은 거의 무시할 수 있음.

### 결론
이 네 매개변수 물리 모델은 리튬이온 배터리 노화를 이해하고 예측하는 효과적인 도구를 제공하며, 특히 새로운 작동 조건에서의 외삽 예측에 유용합니다.
