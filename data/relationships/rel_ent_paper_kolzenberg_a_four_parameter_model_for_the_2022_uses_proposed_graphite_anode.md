---
$id: rel_ent_paper_kolzenberg_a_four_parameter_model_for_the_2022_uses_proposed_graphite_anode
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_kolzenberg_a_four_parameter_model_for_the_2022
  name:
    en: A four parameter model for the solid-electrolyte interphase to predict battery
      aging during operation
    zh: 用于预测运行中电池老化的固体电解质界面膜四参数模型
    ko: 작동 중 배터리 노화 예측을 위한 고체 전해질 계면(SEI) 4개 매개변수 모델
target:
  id: proposed_graphite_anode
  name:
    en: graphite anode
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: The analyzed cells contain a graphite anode whose OCV curve supplies the SoC
    dependence of the model.
  zh: 所分析电池包含石墨阳极，其开路电压曲线提供了模型的SOC依赖性。
  ko: 분석된 전지는 흑연 양극을 포함하며, 그 개회로 전압 곡선이 모델의 SOC 의존성을 제공한다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Section 2.1: ''The cells contain
    a graphite anode and a blend cathode consisting of Li(Ni0.6Mn0.2Co0.2)O2 and Li(Ni1/3Mn1/3Co1/3)O2.'';
    Abstract: ''the state of charge dependence results from the anode''s open circuit
    voltage curve.'''
sources:
- id: src_001
  type: paper
  title: A four parameter model for the solid-electrolyte interphase to predict battery
    aging during operation
  url: https://arxiv.org/abs/2112.13671
  date: '2022'
  accessed_at: '2026-06-25'
---
