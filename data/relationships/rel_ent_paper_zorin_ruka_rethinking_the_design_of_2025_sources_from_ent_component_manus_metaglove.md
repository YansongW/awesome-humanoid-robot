---
$id: rel_ent_paper_zorin_ruka_rethinking_the_design_of_2025_sources_from_ent_component_manus_metaglove
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: sources_from
source:
  id: ent_paper_zorin_ruka_rethinking_the_design_of_2025
  name:
    en: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
    zh: RUKA：以学习重新思考人形手机器人设计
    ko: 'RUKA: 학습을 통한 휴머노이드 손 설계의 재고'
target:
  id: ent_component_manus_metaglove
  name:
    en: MANUS Haptic Glove
    ko: ''
domains:
  source_domain: 02_components
  target_domain: 09_data_datasets
description:
  en: RUKA trains joint-to-actuator and fingertip-to-actuator models from MANUS glove motion-capture data.
  zh: RUKA 使用 MANUS 手套动作捕捉数据训练关节到执行器和指尖到执行器模型。
  ko: RUKA는 MANUS 장갑 모션 캡처 데이터에서 관절-액추에이터 및 손가락 끝-액추에이터 모델을 학습합니다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Abstract: ''To address control challenges, we learn joint-to-actuator
    and fingertip-to-actuator models from motion-capture data collected by the MANUS glove, leveraging the hand''s morphological
    accuracy.'''
sources:
- id: src_001
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-22'
---
