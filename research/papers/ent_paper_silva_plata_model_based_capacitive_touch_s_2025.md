---
$id: ent_paper_silva_plata_model_based_capacitive_touch_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Model-Based Capacitive Touch Sensing in Soft Robotics: Achieving Robust Tactile
    Interactions for Artistic Applications'
  zh: 软体机器人中基于模型的电容式触觉感知：实现面向艺术应用的鲁棒触觉交互
  ko: '소프트 로보틱스에서 모델 기반 전容성 터치 감지: 예술적 응용을 위한 강건한 촉각 상호작용'
summary:
  en: Presents a deformation-robust capacitive touch skin for soft robots that couples
    mutual-capacitance sensing with online SOFA finite-element simulation to localize
    human touch on arbitrary 3D deforming surfaces, validated on an interactive soft
    sculpture.
  zh: 提出了一种用于软体机器人的形变鲁棒电容式触觉皮肤，通过将互电容传感与在线 SOFA 有限元仿真相结合，在任意三维形变表面上定位人体触摸，并在一件交互式软体雕塑上进行了验证。
  ko: 상호 커패시턴스 감지와 온라인 SOFA 유한 요소 시뮬레이션을 결합하여 임의의 3D 변형 표면에서 인간의 접촉을 localize하는, 변형에
    강한 소프트 로봇용 전容성 터치 스킨을 제안하고 대화형 소프트 조각에서 검증한다.
domains:
- 02_components
- 08_software_middleware
- 06_design_engineering
- 11_applications_markets
layers:
- intelligence
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- component
- system
tags:
- capacitive_touch_sensing
- soft_robotics
- tactile_sensing
- deformation_robustness
- sofa_simulation
- human_robot_interaction
- multi_touch
- pneumatic_actuation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-paper verification
    is required before promotion.
sources:
- id: src_001
  type: paper
  title: 'Model-Based Capacitive Touch Sensing in Soft Robotics: Achieving Robust
    Tactile Interactions for Artistic Applications'
  url: https://arxiv.org/abs/2503.02280
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper introduces a model-based capacitive touch-sensing pipeline for soft robots that is designed to remain reliable while the robot surface deforms under pneumatic actuation. It combines a conformable mutual-capacitive touch skin—made from stretchable conductive yarn and a commercial capacitance-to-digital converter—with an online finite-element solid-mechanics simulation running in the SOFA framework. A barycentric mapping step transfers 2D capacitive touch coordinates from the sensor grid onto the 3D deforming surface predicted by the simulation, enabling touch localization on arbitrary soft shapes.

The sensing system is intentionally selective to conductive objects such as human skin, while baseline shifts caused by the robot's own pneumatic deformation are largely suppressed. The authors report multi-touch capability and evaluate localization accuracy both at rest and under deformation using a soft robotic sculpture created in collaboration with a visual artist. The study positions the technology as relevant not only to art and entertainment, but also to broader human-robot interaction scenarios where soft, compliant surfaces must sense contact.

## Key Contributions

- A capacitive touch technology that remains robust to actuation-induced deformation in soft robots.
- A conformable, multi-touch-capable skin that can be applied to arbitrary 3D soft surfaces.
- An online FEM/SOFA-based model that maps 2D capacitive grid coordinates to 3D touch locations under deformation.
- Experimental validation on an interactive soft robotics sculpture, 'El Fruto de L'Érosarbénus'.

## Relevance to Humanoid Robotics

Humanoid robots increasingly use soft, pneumatic, or tendon-driven compliant covers to improve safety during contact, but these actuation-induced shape changes often corrupt conventional tactile sensing. The deformation-robust capacitive skin and model-based 3D localization pipeline described in this paper can be transferred to the limbs, hands, or torso of a humanoid robot to provide reliable touch detection and localization during motion. Its selectivity for conductive objects such as human skin also makes it suitable for close-proximity human-robot interaction tasks.
