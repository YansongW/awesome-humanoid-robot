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
  zh: 本文提出了一种基于物理的固体电解质界面膜（SEI）生长四参数模型，仅使用三个参数化老化协议和阳极开路电压曲线预测锂离子电池容量衰减，并在25个独立老化协议上验证得到1.28%的均方根误差。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2112.13671v2.
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
Accurately predicting aging of lithium-ion batteries would help to prolong their lifespan, but remains a challenge owing to the complexity and interrelation of different aging mechanisms. As a result, aging prediction often relies on empirical or data-driven approaches, which obtain their performance from analyzing large datasets. However, these datasets are expensive to generate and the models are agnostic of the underlying physics and thus difficult to extrapolate to new conditions. In this article, a physical model is used to predict capacity fade caused by solid-electrolyte interphase (SEI) growth in 62 automotive cells, aged with 28 different protocols. Three protocols parametrize the time, current and temperature dependence of the model, the state of charge dependence results from the anode's open circuit voltage curve. The model validation with the remaining 25 protocols shows a high predictivity with a root-mean squared error of $1.28\%$. A case study with the so-validated model shows that the operating window, i.e. maximum and minimum state of charge, has the largest impact on SEI growth, while the influence of the applied current is almost negligible. Thereby the presented model is a promising approach to better understand, quantify and predict aging of lithium-ion batteries.

## 核心内容
Accurately predicting aging of lithium-ion batteries would help to prolong their lifespan, but remains a challenge owing to the complexity and interrelation of different aging mechanisms. As a result, aging prediction often relies on empirical or data-driven approaches, which obtain their performance from analyzing large datasets. However, these datasets are expensive to generate and the models are agnostic of the underlying physics and thus difficult to extrapolate to new conditions. In this article, a physical model is used to predict capacity fade caused by solid-electrolyte interphase (SEI) growth in 62 automotive cells, aged with 28 different protocols. Three protocols parametrize the time, current and temperature dependence of the model, the state of charge dependence results from the anode's open circuit voltage curve. The model validation with the remaining 25 protocols shows a high predictivity with a root-mean squared error of $1.28\%$. A case study with the so-validated model shows that the operating window, i.e. maximum and minimum state of charge, has the largest impact on SEI growth, while the influence of the applied current is almost negligible. Thereby the presented model is a promising approach to better understand, quantify and predict aging of lithium-ion batteries.

## 参考
- http://arxiv.org/abs/2112.13671v2

