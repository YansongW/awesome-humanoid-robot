---
$id: ent_paper_silva_plata_model_based_capacitive_touch_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Model-Based Capacitive Touch Sensing in Soft Robotics: Achieving Robust Tactile Interactions for Artistic Applications'
  zh: 软体机器人中基于模型的电容式触觉感知：实现面向艺术应用的鲁棒触觉交互
  ko: '소프트 로보틱스에서 모델 기반 전容성 터치 감지: 예술적 응용을 위한 강건한 촉각 상호작용'
summary:
  en: Presents a deformation-robust capacitive touch skin for soft robots that couples mutual-capacitance sensing with online
    SOFA finite-element simulation to localize human touch on arbitrary 3D deforming surfaces, validated on an interactive
    soft sculpture.
  zh: 提出了一种用于软体机器人的形变鲁棒电容式触觉皮肤，通过将互电容传感与在线 SOFA 有限元仿真相结合，在任意三维形变表面上定位人体触摸，并在一件交互式软体雕塑上进行了验证。
  ko: 상호 커패시턴스 감지와 온라인 SOFA 유한 요소 시뮬레이션을 결합하여 임의의 3D 변형 표면에서 인간의 접촉을 localize하는, 변형에 강한 소프트 로봇용 전容성 터치 스킨을 제안하고 대화형 소프트 조각에서
    검증한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.02280v1.
sources:
- id: src_001
  type: paper
  title: 'Model-Based Capacitive Touch Sensing in Soft Robotics: Achieving Robust Tactile Interactions for Artistic Applications'
  url: https://arxiv.org/abs/2503.02280
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
In this paper, we present a touch technology to achieve tactile interactivity for human-robot interaction (HRI) in soft robotics. By combining a capacitive touch sensor with an online solid mechanics simulation provided by the SOFA framework, contact detection is achieved for arbitrary shapes. Furthermore, the implementation of the capacitive touch technology presented here is selectively sensitive to human touch (conductive objects), while it is largely unaffected by the deformations created by the pneumatic actuation of our soft robot. Multi-touch interactions are also possible. We evaluated our approach with an organic soft robotics sculpture that was created by a visual artist. In particular, we evaluate that the touch localization capabilities are robust under the deformation of the device. We discuss the potential this approach has for the arts and entertainment as well as other domains.

## 核心内容
In this paper, we present a touch technology to achieve tactile interactivity for human-robot interaction (HRI) in soft robotics. By combining a capacitive touch sensor with an online solid mechanics simulation provided by the SOFA framework, contact detection is achieved for arbitrary shapes. Furthermore, the implementation of the capacitive touch technology presented here is selectively sensitive to human touch (conductive objects), while it is largely unaffected by the deformations created by the pneumatic actuation of our soft robot. Multi-touch interactions are also possible. We evaluated our approach with an organic soft robotics sculpture that was created by a visual artist. In particular, we evaluate that the touch localization capabilities are robust under the deformation of the device. We discuss the potential this approach has for the arts and entertainment as well as other domains.

## 参考
- http://arxiv.org/abs/2503.02280v1

