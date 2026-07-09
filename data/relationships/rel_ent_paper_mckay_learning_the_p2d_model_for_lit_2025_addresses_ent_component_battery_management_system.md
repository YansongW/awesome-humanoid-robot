---
$id: rel_ent_paper_mckay_learning_the_p2d_model_for_lit_2025_addresses_ent_component_battery_management_system
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: addresses
source:
  id: ent_paper_mckay_learning_the_p2d_model_for_lit_2025
  name:
    en: Learning the P2D Model for Lithium-Ion Batteries with SOH Detection
    zh: 具有SOH检测的锂离子电池P2D模型学习
    ko: SOH 감지를 위한 리튬 이온 배터리 P2D 모델 학습
target:
  id: ent_component_battery_management_system
  name:
    en: Battery Management System
    ko: ''
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: The surrogate model is intended to run inside a BMS for real-time prediction and SOH detection.
  zh: 该代理模型旨在电池管理系统内部运行，用于实时预测和SOH检测。
  ko: 서로게이트 모델은 실시간 예측 및 SOH 감지를 위해 BMS 내부에서 실행되도록 의도되었다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Abstract: ''Battery management systems control their optimal use and
    charging and predict when the battery will cease to deliver the required output on a planned duty or driving cycle''.'
sources:
- id: src_001
  type: paper
  title: Learning the P2D Model for Lithium-Ion Batteries with SOH Detection
  url: https://arxiv.org/abs/2502.14147
  date: '2025'
  accessed_at: '2026-06-27'
---
