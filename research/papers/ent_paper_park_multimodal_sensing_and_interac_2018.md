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
  en: Park et al. present an active hand orthosis that combines forearm EMG, finger
    bend, and thumb pressure sensing, and evaluate two multimodal control schemes
    on stroke survivors with different impairment patterns.
  zh: Park 等人提出了一种融合前臂肌电、手指弯曲和拇指压力感知的主动式手部矫形器，并在具有不同损伤模式的卒中患者身上评估了两种多模态控制方案。
  ko: Park 등은 전완근전도, 손가락 굽힘, 엄지 압력 감지를 결합한 능동형 손 보조기를 제시하고 다양한 손상 패턴을 가진 뇌졸중 생존자를
    대상으로 두 가지 다중 감각 제어 방식을 평가했다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; requires human review against full
    text before verification.
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

## Overview

Wearable robotic hand rehabilitation devices can offer greater freedom than workstation-based systems, but effective user control remains a challenge. Stroke-related upper-limb impairments vary widely, so a single sensing modality such as electromyography (EMG) may not work for all users. To address this, Park et al. introduce a multimodal sensing and interaction paradigm for an active hand orthosis.

The prototype combines an exotendon-driven hand orthosis with multiple sensors: a Myo Armband for forearm EMG, bend-sensitive resistors for finger posture, and force-sensitive resistors (FSRs) for thumb contact pressure. The mechanical structure includes an aluminum forearm splint, 3D-printed fingertip components, Velcro straps, and tendon cables driven by a motor under PID position control.

The authors propose two multimodal control schemes. In "bend-to-open / EMG-to-close," finger extension triggers opening and EMG activation triggers closing. In "EMG-to-open / pressure-to-close," EMG activation opens the hand and thumb pressure against an object closes it. Both schemes are evaluated on four chronic stroke survivors with different impairment patterns using controller accuracy metrics and pick-and-place functional tasks.

## Key Contributions

- Developed an active hand orthosis as a multimodal sensory platform integrating EMG, finger bend, and thumb pressure sensors within an exotendon framework.
- Proposed two multimodal interaction methods—bend-to-open/EMG-to-close and EMG-to-open/pressure-to-close—that use natural hand movement signals rather than side channels such as voice.
- Demonstrated feasibility on four stroke survivors with different impairment patterns, using both controller accuracy tests and pick-and-place functional tasks.

## Relevance to Humanoid Robotics

Although the paper focuses on post-stroke hand rehabilitation, its core contributions are directly relevant to humanoid robotics. The multimodal fusion of EMG, proprioceptive bending, and contact pressure for intent inference maps closely onto the sensing and control problems faced by dexterous humanoid hands and upper-limb systems. The principle of combining multiple natural user signals to achieve robust, intuitive control is broadly applicable to humanoid teleoperation, shared autonomy, and physical human-robot interaction in unstructured environments. The tendon-driven exotendon architecture and PID position control also share design concerns with underactuated and compliant humanoid end effectors.
