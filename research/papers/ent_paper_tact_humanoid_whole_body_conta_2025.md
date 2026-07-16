---
$id: ent_paper_tact_humanoid_whole_body_conta_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality'
  zh: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality'
  ko: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality'
summary:
  en: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- loco_manipulation
- tact
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.15146v1.
sources:
- id: src_001
  type: paper
  title: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality (arXiv)'
  url: https://arxiv.org/abs/2506.15146
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Manipulation with whole-body contact by humanoid robots offers distinct advantages, including enhanced stability and reduced load. On the other hand, we need to address challenges such as the increased computational cost of motion generation and the difficulty of measuring broad-area contact. We therefore have developed a humanoid control system that allows a humanoid robot equipped with tactile sensors on its upper body to learn a policy for whole-body manipulation through imitation learning based on human teleoperation data. This policy, named tactile-modality extended ACT (TACT), has a feature to take multiple sensor modalities as input, including joint position, vision, and tactile measurements. Furthermore, by integrating this policy with retargeting and locomotion control based on a biped model, we demonstrate that the life-size humanoid robot RHP7 Kaleido is capable of achieving whole-body contact manipulation while maintaining balance and walking. Through detailed experimental verification, we show that inputting both vision and tactile modalities into the policy contributes to improving the robustness of manipulation involving broad and delicate contact.

## 核心内容
Manipulation with whole-body contact by humanoid robots offers distinct advantages, including enhanced stability and reduced load. On the other hand, we need to address challenges such as the increased computational cost of motion generation and the difficulty of measuring broad-area contact. We therefore have developed a humanoid control system that allows a humanoid robot equipped with tactile sensors on its upper body to learn a policy for whole-body manipulation through imitation learning based on human teleoperation data. This policy, named tactile-modality extended ACT (TACT), has a feature to take multiple sensor modalities as input, including joint position, vision, and tactile measurements. Furthermore, by integrating this policy with retargeting and locomotion control based on a biped model, we demonstrate that the life-size humanoid robot RHP7 Kaleido is capable of achieving whole-body contact manipulation while maintaining balance and walking. Through detailed experimental verification, we show that inputting both vision and tactile modalities into the policy contributes to improving the robustness of manipulation involving broad and delicate contact.

## 参考
- http://arxiv.org/abs/2506.15146v1

## Overview
Manipulation with whole-body contact by humanoid robots offers distinct advantages, including enhanced stability and reduced load. On the other hand, we need to address challenges such as the increased computational cost of motion generation and the difficulty of measuring broad-area contact. We therefore have developed a humanoid control system that allows a humanoid robot equipped with tactile sensors on its upper body to learn a policy for whole-body manipulation through imitation learning based on human teleoperation data. This policy, named tactile-modality extended ACT (TACT), has a feature to take multiple sensor modalities as input, including joint position, vision, and tactile measurements. Furthermore, by integrating this policy with retargeting and locomotion control based on a biped model, we demonstrate that the life-size humanoid robot RHP7 Kaleido is capable of achieving whole-body contact manipulation while maintaining balance and walking. Through detailed experimental verification, we show that inputting both vision and tactile modalities into the policy contributes to improving the robustness of manipulation involving broad and delicate contact.

## Content
Manipulation with whole-body contact by humanoid robots offers distinct advantages, including enhanced stability and reduced load. On the other hand, we need to address challenges such as the increased computational cost of motion generation and the difficulty of measuring broad-area contact. We therefore have developed a humanoid control system that allows a humanoid robot equipped with tactile sensors on its upper body to learn a policy for whole-body manipulation through imitation learning based on human teleoperation data. This policy, named tactile-modality extended ACT (TACT), has a feature to take multiple sensor modalities as input, including joint position, vision, and tactile measurements. Furthermore, by integrating this policy with retargeting and locomotion control based on a biped model, we demonstrate that the life-size humanoid robot RHP7 Kaleido is capable of achieving whole-body contact manipulation while maintaining balance and walking. Through detailed experimental verification, we show that inputting both vision and tactile modalities into the policy contributes to improving the robustness of manipulation involving broad and delicate contact.

## 개요
휴머노이드 로봇의 전신 접촉을 통한 조작은 향상된 안정성과 부하 감소 등 뚜렷한 장점을 제공합니다. 반면, 동작 생성의 계산 비용 증가와 광범위한 접촉 측정의 어려움과 같은 과제를 해결해야 합니다. 이에 따라 우리는 상체에 촉각 센서를 장착한 휴머노이드 로봇이 인간 원격 조작 데이터 기반 모방 학습을 통해 전신 조작 정책을 학습할 수 있는 휴머노이드 제어 시스템을 개발했습니다. 이 정책은 촉각 모달리티 확장 ACT(TACT)라고 명명되었으며, 관절 위치, 시각, 촉각 측정값을 포함한 여러 센서 모달리티를 입력으로 받는 특징을 가집니다. 또한, 이 정책을 이족 보행 모델 기반 리타겟팅 및 보행 제어와 통합함으로써, 실물 크기 휴머노이드 로봇 RHP7 Kaleido가 균형 유지 및 보행 중 전신 접촉 조작을 수행할 수 있음을 입증했습니다. 상세한 실험 검증을 통해, 시각 및 촉각 모달리티를 정책에 입력하는 것이 광범위하고 미세한 접촉을 포함하는 조작의 견고성 향상에 기여함을 보여줍니다.

## 핵심 내용
휴머노이드 로봇의 전신 접촉을 통한 조작은 향상된 안정성과 부하 감소 등 뚜렷한 장점을 제공합니다. 반면, 동작 생성의 계산 비용 증가와 광범위한 접촉 측정의 어려움과 같은 과제를 해결해야 합니다. 이에 따라 우리는 상체에 촉각 센서를 장착한 휴머노이드 로봇이 인간 원격 조작 데이터 기반 모방 학습을 통해 전신 조작 정책을 학습할 수 있는 휴머노이드 제어 시스템을 개발했습니다. 이 정책은 촉각 모달리티 확장 ACT(TACT)라고 명명되었으며, 관절 위치, 시각, 촉각 측정값을 포함한 여러 센서 모달리티를 입력으로 받는 특징을 가집니다. 또한, 이 정책을 이족 보행 모델 기반 리타겟팅 및 보행 제어와 통합함으로써, 실물 크기 휴머노이드 로봇 RHP7 Kaleido가 균형 유지 및 보행 중 전신 접촉 조작을 수행할 수 있음을 입증했습니다. 상세한 실험 검증을 통해, 시각 및 촉각 모달리티를 정책에 입력하는 것이 광범위하고 미세한 접촉을 포함하는 조작의 견고성 향상에 기여함을 보여줍니다.
