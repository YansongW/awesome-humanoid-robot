---
$id: rel_ent_paper_kolzenberg_a_four_parameter_model_for_the_2022_verified_by_proposed_differential_voltage_analysis
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: verified_by
source:
  id: ent_paper_kolzenberg_a_four_parameter_model_for_the_2022
  name:
    en: A four parameter model for the solid-electrolyte interphase to predict battery
      aging during operation
    zh: 用于预测运行中电池老化的固体电解质界面膜四参数模型
    ko: 작동 중 배터리 노화 예측을 위한 고체 전해질 계면(SEI) 4개 매개변수 모델
target:
  id: proposed_differential_voltage_analysis
  name:
    en: differential voltage analysis (DVA)
domains:
  source_domain: 02_components
  target_domain: 10_evaluation_benchmarks
description:
  en: DVA is used to separate capacity fade into loss of lithium inventory and loss
    of active material.
  zh: 差分电压分析用于将容量衰减分解为锂库存损失和活性材料损失。
  ko: 차분 전압 분석은 용량 감소를 리튬 재고 손실과 활성 물질 손실로 분리하는 데 사용된다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Abstract and Section 2.1: ''Using
    differential voltage analysis (DVA), we first separate capacity fade into the
    three aging modes loss of active material on positive and negative electrode and
    loss of lithium inventory.'''
sources:
- id: src_001
  type: paper
  title: A four parameter model for the solid-electrolyte interphase to predict battery
    aging during operation
  url: https://arxiv.org/abs/2112.13671
  date: '2022'
  accessed_at: '2026-06-25'
---
