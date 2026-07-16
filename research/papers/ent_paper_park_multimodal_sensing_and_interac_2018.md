---
$id: ent_paper_park_multimodal_sensing_and_interac_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Multimodal Sensing and Interaction for a Robotic Hand Orthosis
  zh: 机器人手部矫形器的多模态感知与交互
  ko: 로봇 손 보조기의 다중 감각 및 상호작용
summary:
  en: Park et al. present an active hand orthosis that combines forearm EMG, finger bend, and thumb pressure sensing, and
    evaluate two multimodal control schemes on stroke survivors with different impairment patterns.
  zh: 'Wearable robotic hand rehabilitation devices can allow greater freedom and flexibility than their workstation-like
    counterparts. However, the field is generally lacking effective methods by which the user can operate the device: such
    controls must be effective, intuitive, and robust to the wide range of possible impairment patterns. Even when focusing
    on a specific condition, such as stroke, the variety of encountered upper limb impairment patterns means that a single
    sensing modality, such as electromyography (EMG), might not be sufficient to enable controls for a broad range of users.
    To add'
  ko: Park 등은 전완근전도, 손가락 굽힘, 엄지 압력 감지를 결합한 능동형 손 보조기를 제시하고 다양한 손상 패턴을 가진 뇌졸중 생존자를 대상으로 두 가지 다중 감각 제어 방식을 평가했다.
domains:
- 02_components
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
- component
tags:
- hand_orthosis
- multimodal_sensing
- emg
- intent_recognition
- stroke_rehabilitation
- dexterous_hand
- physical_human_robot_interaction
- wearable_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1808.00092v4.
sources:
- id: src_001
  type: paper
  title: Multimodal Sensing and Interaction for a Robotic Hand Orthosis
  url: https://arxiv.org/abs/1808.00092
  date: '2018'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
Wearable robotic hand rehabilitation devices can allow greater freedom and flexibility than their workstation-like counterparts. However, the field is generally lacking effective methods by which the user can operate the device: such controls must be effective, intuitive, and robust to the wide range of possible impairment patterns. Even when focusing on a specific condition, such as stroke, the variety of encountered upper limb impairment patterns means that a single sensing modality, such as electromyography (EMG), might not be sufficient to enable controls for a broad range of users. To address this significant gap, we introduce a multimodal sensing and interaction paradigm for an active hand orthosis. In our proof-of-concept implementation, EMG is complemented by other sensing modalities, such as finger bend and contact pressure sensors. We propose multimodal interaction methods that utilize this sensory data as input, and show they can enable tasks for stroke survivors who exhibit different impairment patterns. We believe that robotic hand orthoses developed as multimodal sensory platforms with help address some of the key challenges in physical interaction with the user.

## 核心内容
Wearable robotic hand rehabilitation devices can allow greater freedom and flexibility than their workstation-like counterparts. However, the field is generally lacking effective methods by which the user can operate the device: such controls must be effective, intuitive, and robust to the wide range of possible impairment patterns. Even when focusing on a specific condition, such as stroke, the variety of encountered upper limb impairment patterns means that a single sensing modality, such as electromyography (EMG), might not be sufficient to enable controls for a broad range of users. To address this significant gap, we introduce a multimodal sensing and interaction paradigm for an active hand orthosis. In our proof-of-concept implementation, EMG is complemented by other sensing modalities, such as finger bend and contact pressure sensors. We propose multimodal interaction methods that utilize this sensory data as input, and show they can enable tasks for stroke survivors who exhibit different impairment patterns. We believe that robotic hand orthoses developed as multimodal sensory platforms with help address some of the key challenges in physical interaction with the user.

## 参考
- http://arxiv.org/abs/1808.00092v4

## Overview
Wearable robotic hand rehabilitation devices can allow greater freedom and flexibility than their workstation-like counterparts. However, the field is generally lacking effective methods by which the user can operate the device: such controls must be effective, intuitive, and robust to the wide range of possible impairment patterns. Even when focusing on a specific condition, such as stroke, the variety of encountered upper limb impairment patterns means that a single sensing modality, such as electromyography (EMG), might not be sufficient to enable controls for a broad range of users. To address this significant gap, we introduce a multimodal sensing and interaction paradigm for an active hand orthosis. In our proof-of-concept implementation, EMG is complemented by other sensing modalities, such as finger bend and contact pressure sensors. We propose multimodal interaction methods that utilize this sensory data as input, and show they can enable tasks for stroke survivors who exhibit different impairment patterns. We believe that robotic hand orthoses developed as multimodal sensory platforms with help address some of the key challenges in physical interaction with the user.

## Content
Wearable robotic hand rehabilitation devices can allow greater freedom and flexibility than their workstation-like counterparts. However, the field is generally lacking effective methods by which the user can operate the device: such controls must be effective, intuitive, and robust to the wide range of possible impairment patterns. Even when focusing on a specific condition, such as stroke, the variety of encountered upper limb impairment patterns means that a single sensing modality, such as electromyography (EMG), might not be sufficient to enable controls for a broad range of users. To address this significant gap, we introduce a multimodal sensing and interaction paradigm for an active hand orthosis. In our proof-of-concept implementation, EMG is complemented by other sensing modalities, such as finger bend and contact pressure sensors. We propose multimodal interaction methods that utilize this sensory data as input, and show they can enable tasks for stroke survivors who exhibit different impairment patterns. We believe that robotic hand orthoses developed as multimodal sensory platforms with help address some of the key challenges in physical interaction with the user.

## 개요
웨어러블 로봇 손 재활 장치는 워크스테이션 형태의 장치보다 더 큰 자유도와 유연성을 제공할 수 있습니다. 그러나 사용자가 장치를 작동할 수 있는 효과적인 방법이 일반적으로 부족한 실정입니다. 이러한 제어 방식은 효과적이고 직관적이며 다양한 손상 패턴에 강건해야 합니다. 뇌졸중과 같은 특정 질환에 초점을 맞추더라도, 상지 손상 패턴의 다양성으로 인해 근전도(EMG)와 같은 단일 감지 방식만으로는 광범위한 사용자를 위한 제어를 가능하게 하기에 충분하지 않을 수 있습니다. 이러한 중요한 격차를 해결하기 위해, 우리는 능동형 손 보조기를 위한 다중 감각 및 상호작용 패러다임을 소개합니다. 개념 증명 구현에서 EMG는 손가락 굽힘 센서 및 접촉 압력 센서와 같은 다른 감지 방식으로 보완됩니다. 우리는 이 감각 데이터를 입력으로 활용하는 다중 모드 상호작용 방법을 제안하며, 이 방법이 다양한 손상 패턴을 보이는 뇌졸중 생존자들에게 작업 수행을 가능하게 할 수 있음을 보여줍니다. 우리는 다중 감각 플랫폼으로 개발된 로봇 손 보조기가 사용자와의 물리적 상호작용에서 주요 과제 중 일부를 해결하는 데 도움이 될 것이라고 믿습니다.

## 핵심 내용
웨어러블 로봇 손 재활 장치는 워크스테이션 형태의 장치보다 더 큰 자유도와 유연성을 제공할 수 있습니다. 그러나 사용자가 장치를 작동할 수 있는 효과적인 방법이 일반적으로 부족한 실정입니다. 이러한 제어 방식은 효과적이고 직관적이며 다양한 손상 패턴에 강건해야 합니다. 뇌졸중과 같은 특정 질환에 초점을 맞추더라도, 상지 손상 패턴의 다양성으로 인해 근전도(EMG)와 같은 단일 감지 방식만으로는 광범위한 사용자를 위한 제어를 가능하게 하기에 충분하지 않을 수 있습니다. 이러한 중요한 격차를 해결하기 위해, 우리는 능동형 손 보조기를 위한 다중 감각 및 상호작용 패러다임을 소개합니다. 개념 증명 구현에서 EMG는 손가락 굽힘 센서 및 접촉 압력 센서와 같은 다른 감지 방식으로 보완됩니다. 우리는 이 감각 데이터를 입력으로 활용하는 다중 모드 상호작용 방법을 제안하며, 이 방법이 다양한 손상 패턴을 보이는 뇌졸중 생존자들에게 작업 수행을 가능하게 할 수 있음을 보여줍니다. 우리는 다중 감각 플랫폼으로 개발된 로봇 손 보조기가 사용자와의 물리적 상호작용에서 주요 과제 중 일부를 해결하는 데 도움이 될 것이라고 믿습니다.
