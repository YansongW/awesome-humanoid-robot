---
$id: ent_paper_kolzenberg_a_four_parameter_model_for_the_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A four parameter model for the solid-electrolyte interphase to predict battery
    aging during operation
  zh: 用于预测运行中电池老化的固体电解质界面膜四参数模型
  ko: 작동 중 배터리 노화 예측을 위한 고체 전해질 계면(SEI) 4개 매개변수 모델
summary:
  en: The paper presents a four-parameter physics-based SEI-growth model that predicts
    lithium-ion capacity fade using only three parametrization protocols plus the
    anode OCV curve, validated on 25 independent aging protocols with 1.28% RMSE.
  zh: 本文提出了一种基于物理的固体电解质界面膜（SEI）生长四参数模型，仅使用三个参数化老化协议和阳极开路电压曲线预测锂离子电池容量衰减，并在25个独立老化协议上验证得到1.28%的均方根误差。
  ko: 본 논문은 세 가지 매개변수화 프로토콜과 양극 개회로 전압 곡선만을 사용하여 리튬 이온 배터리 용량 감소를 예측하는 물리 기반 SEI 성장
    4개 매개변수 모델을 제시하며, 25개의 독립 노화 프로토콜에서 1.28% RMSE로 검증되었다.
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
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from arXiv full text; factual claims traceable to the paper,
    but humanoid-robot relevance is inferred rather than stated by the authors.
sources:
- id: src_001
  type: paper
  title: A four parameter model for the solid-electrolyte interphase to predict battery
    aging during operation
  url: https://arxiv.org/abs/2112.13671
  date: '2022'
  accessed_at: '2026-06-25'
related_entities:
- id: proposed_solid_electrolyte_interphase
  relationship: proposes
  description:
    en: The paper models capacity fade caused by solid-electrolyte interphase (SEI)
      growth.
    zh: 该论文对固体电解质界面膜（SEI）生长引起的容量衰减进行建模。
    ko: 해당 논문은 고체 전해질 계면(SEI) 성장에 의한 용량 감소를 모델링한다.
- id: proposed_graphite_anode
  relationship: uses
  description:
    en: The analyzed cells contain a graphite anode whose open-circuit voltage curve
      provides the state-of-charge dependence.
    zh: 所分析的电池含有石墨阳极，其开路电压曲线提供了荷电状态依赖性。
    ko: 분석된 전지는 흑연 양극을 포함하며, 그 개회로 전압 곡선이 SOC 의존성을 제공한다.
- id: proposed_nmc_cathode
  relationship: uses
  description:
    en: The analyzed cells use a blend cathode of NMC-622 and NMC-111.
    zh: 所分析的电池使用了NMC-622和NMC-111混合阴极。
    ko: 분석된 전지는 NMC-622와 NMC-111 혼합 음극을 사용한다.
- id: proposed_lithium_ion_pouch_cell
  relationship: uses
  description:
    en: The validation is performed on 62 automotive-grade lithium-ion pouch cells.
    zh: 验证在62个汽车级锂离子软包电池上进行。
    ko: 검증은 62개의 자동차 등급 리튬 이온 파우치 셀에서 수행되었다.
- id: proposed_ethylene_carbonate_electrolyte
  relationship: uses
  description:
    en: The SEI formation reaction is described using ethylene carbonate as an example
      electrolyte molecule.
    zh: SEI形成反应以碳酸亚乙酯为例进行了描述。
    ko: SEI 형성 반응은 전해질 분자의 예로 에틸렌 카보네이트를 사용하여 기술된다.
- id: proposed_lithium_ethylene_dicarbonate
  relationship: uses
  description:
    en: Li2EDC is identified as the commonly observed SEI component in the formation
      reaction.
    zh: Li2EDC被确定为形成反应中常见的SEI组分。
    ko: Li2EDC는 형성 반응에서 일반적으로 관찰되는 SEI 성분으로 확인되었다.
- id: proposed_differential_voltage_analysis
  relationship: uses
  description:
    en: Differential voltage analysis (DVA) is used to separate capacity fade into
      aging modes.
    zh: 差分电压分析（DVA）用于将容量衰减分解为不同老化模式。
    ko: 차분 전압 분석(DVA)은 용량 감소를 노화 모드로 분리하는 데 사용된다.
- id: proposed_coin_cell_post_mortem
  relationship: verified_by
  description:
    en: Post-mortem experiments with harvested electrode materials in coin cells provide
      complementary validation.
    zh: 从拆解电池中回收电极材料制成的扣式电池进行事后分析，以提供补充验证。
    ko: 회수된 전극 재료로 제작된 코인 셀의 사후 분석이 보완적 검증을 제공한다.
---

## Overview

This paper develops a computationally efficient, physics-based model for solid-electrolyte interphase (SEI) growth and the resulting capacity fade in lithium-ion batteries. The model is formulated with only four free parameters and combines half-cell cycling kinetics with a long-term diffusion-limited SEI formation law. Three aging protocols are used to parametrize the time, current, and temperature dependence of the model, while the state-of-charge dependence is derived directly from the graphite anode's open-circuit voltage curve.

The experimental work uses 62 automotive-grade lithium-ion pouch cells with a graphite anode and a blend cathode of Li(Ni0.6Mn0.2Co0.2)O2 and Li(Ni1/3Mn1/3Co1/3)O2. These cells are aged under 28 different protocols. The model is parametrized on three of these protocols and validated against the remaining 25, achieving a root-mean-squared error of 1.28%. Differential voltage analysis is employed to decompose capacity fade into loss of lithium inventory, loss of active material on the positive electrode, and loss of active material on the negative electrode, while post-mortem coin-cell experiments provide additional validation of the model assumptions.

A subsequent case study with the validated model examines how different operating conditions affect SEI-driven aging. The results indicate that the operating window—defined by the maximum and minimum state of charge—has the strongest influence on SEI growth, whereas the influence of applied charging current is almost negligible. This finding is used to compare various electric-vehicle charging and user behaviors in terms of long-term degradation.

## Key Contributions

- A four-parameter physics-based SEI growth model that captures time, current, temperature, and state-of-charge dependence of lithium-ion battery aging.
- Parametrization using only three aging protocols plus the anode open-circuit voltage curve, with validation on 25 independent protocols yielding 1.28% RMSE.
- Quantitative demonstration that the operating window (minimum and maximum SoC) dominates SEI-driven capacity fade, while charging current has a minor influence.
- Experimental validation through differential voltage analysis and post-mortem coin-cell analysis of 62 automotive-grade pouch cells.
- Case study comparing how different electric-vehicle charging and usage behaviors affect long-term battery degradation.

## Relevance to Humanoid Robotics

Reliable prediction of lithium-ion battery aging and lifetime is essential for the mass production and deployment of mobile humanoid robots, which depend on compact, high-energy-density power systems. The paper's physically interpretable SEI model offers a way to quantify degradation under varied operating conditions without requiring large empirical datasets, supporting the design of service intervals, warranty policies, and battery management strategies for humanoid platforms.

Because the model links degradation primarily to the operating window rather than to current rate, it can inform operating strategies for humanoids—such as charge-depth limits and duty-cycle planning—where battery weight and longevity are critical. However, the paper studies automotive pouch cells, so direct transfer to the smaller cylindrical or pouch cells typically used in humanoids would require re-parametrization and validation.
