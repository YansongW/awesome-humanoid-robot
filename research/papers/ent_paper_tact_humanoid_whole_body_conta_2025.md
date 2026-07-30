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
  zh: TACT 是 2025 年提出的人形机器人全身接触操控系统，由研究团队开发。其核心贡献在于通过深度模仿学习融合触觉模态，使配备上身触觉传感器的人形机器人 RHP7 Kaleido 学会基于人类遥操作数据的全身操控策略，并成功实现行走与平衡下的接触操控。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.15146v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality (arXiv)'
  url: https://arxiv.org/abs/2506.15146
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人利用全身接触进行操控具有增强稳定性和降低负载的优势，但也面临运动生成计算成本高、大面积接触测量困难等挑战。为此，研究团队开发了一套控制系统，让上身配备触觉传感器的人形机器人通过基于人类遥操作数据的模仿学习，习得全身操控策略。该策略名为 TACT，可同时输入关节位置、视觉和触觉测量等多种传感器模态。通过将该策略与基于双足模型的重定向和运动控制集成，研究团队在真实尺寸人形机器人 RHP7 Kaleido 上展示了其在保持平衡和行走的同时完成全身接触操控的能力。

## 核心内容
### 方法
- TACT 策略基于模仿学习框架，从人类遥操作数据中学习全身操控策略。
- 策略输入包含三种模态：关节位置、视觉图像和触觉测量，其中触觉传感器安装于机器人上身。
- 通过将学习到的策略与重定向（retargeting）及基于双足模型的运动控制（locomotion control）集成，实现全身协调。

### 实验设置
- 使用真实尺寸人形机器人 RHP7 Kaleido 进行验证。
- 实验任务涉及全身接触操控，要求机器人在保持平衡和行走的同时完成操作。

### 关键结果
- 实验证明，同时输入视觉和触觉模态（vision and tactile modalities）有助于提升涉及大面积和精细接触的操控鲁棒性。
- 系统成功实现了全身接触操控，验证了触觉模态在复杂接触任务中的有效性。

### 结论
TACT 通过融合触觉信息，有效解决了人形机器人全身接触操控中的计算复杂度和接触测量难题，为未来人形机器人在真实环境中的稳定操控提供了可行方案。

## Overview
Manipulation with whole-body contact by humanoid robots offers distinct advantages, including enhanced stability and reduced load. On the other hand, we need to address challenges such as the increased computational cost of motion generation and the difficulty of measuring broad-area contact. We therefore have developed a humanoid control system that allows a humanoid robot equipped with tactile sensors on its upper body to learn a policy for whole-body manipulation through imitation learning based on human teleoperation data. This policy, named tactile-modality extended ACT (TACT), has a feature to take multiple sensor modalities as input, including joint position, vision, and tactile measurements. Furthermore, by integrating this policy with retargeting and locomotion control based on a biped model, we demonstrate that the life-size humanoid robot RHP7 Kaleido is capable of achieving whole-body contact manipulation while maintaining balance and walking. Through detailed experimental verification, we show that inputting both vision and tactile modalities into the policy contributes to improving the robustness of manipulation involving broad and delicate contact.

## 개요
휴머노이드 로봇의 전신 접촉을 통한 조작은 향상된 안정성과 부하 감소 등 뚜렷한 장점을 제공합니다. 반면, 동작 생성의 계산 비용 증가와 광범위한 접촉 측정의 어려움과 같은 과제를 해결해야 합니다. 이에 따라 우리는 상체에 촉각 센서를 장착한 휴머노이드 로봇이 인간 원격 조작 데이터 기반 모방 학습을 통해 전신 조작 정책을 학습할 수 있는 휴머노이드 제어 시스템을 개발했습니다. 이 정책은 촉각 모달리티 확장 ACT(TACT)라고 명명되었으며, 관절 위치, 시각, 촉각 측정값을 포함한 여러 센서 모달리티를 입력으로 받는 특징을 가집니다. 또한, 이 정책을 이족 보행 모델 기반 리타겟팅 및 보행 제어와 통합함으로써, 실물 크기 휴머노이드 로봇 RHP7 Kaleido가 균형 유지 및 보행 중 전신 접촉 조작을 수행할 수 있음을 입증했습니다. 상세한 실험 검증을 통해, 시각 및 촉각 모달리티를 정책에 입력하는 것이 광범위하고 미세한 접촉을 포함하는 조작의 견고성 향상에 기여함을 보여줍니다.

## 핵심 내용
휴머노이드 로봇의 전신 접촉을 통한 조작은 향상된 안정성과 부하 감소 등 뚜렷한 장점을 제공합니다. 반면, 동작 생성의 계산 비용 증가와 광범위한 접촉 측정의 어려움과 같은 과제를 해결해야 합니다. 이에 따라 우리는 상체에 촉각 센서를 장착한 휴머노이드 로봇이 인간 원격 조작 데이터 기반 모방 학습을 통해 전신 조작 정책을 학습할 수 있는 휴머노이드 제어 시스템을 개발했습니다. 이 정책은 촉각 모달리티 확장 ACT(TACT)라고 명명되었으며, 관절 위치, 시각, 촉각 측정값을 포함한 여러 센서 모달리티를 입력으로 받는 특징을 가집니다. 또한, 이 정책을 이족 보행 모델 기반 리타겟팅 및 보행 제어와 통합함으로써, 실물 크기 휴머노이드 로봇 RHP7 Kaleido가 균형 유지 및 보행 중 전신 접촉 조작을 수행할 수 있음을 입증했습니다. 상세한 실험 검증을 통해, 시각 및 촉각 모달리티를 정책에 입력하는 것이 광범위하고 미세한 접촉을 포함하는 조작의 견고성 향상에 기여함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2506.15146v1
