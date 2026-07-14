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
  zh: Park 等人提出了一种融合前臂肌电、手指弯曲和拇指压力感知的主动式手部矫形器，并在具有不同损伤模式的卒中患者身上评估了两种多模态控制方案。
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

