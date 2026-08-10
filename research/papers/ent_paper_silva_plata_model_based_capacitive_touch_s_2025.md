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
  zh: 本文提出一种基于电容耦合与SOFA有限元仿真的软体机器人触觉皮肤，能抵抗变形干扰并定位任意三维曲面上的触摸点。该技术由研究团队开发，核心贡献在于实现人类触摸（导电物体）选择性感知，同时不受气动变形影响，并在交互式软雕塑上验证了多触点定位的鲁棒性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.02280v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (724 chars, DeepSeek).'
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
该研究将互电容传感与SOFA框架的在线固体力学仿真相结合，为软体机器人构建了变形鲁棒的触觉皮肤。传感器仅对导电物体（如人手）敏感，而软体机器人的气动变形不会产生干扰信号，从而实现了任意形状表面的接触检测。多触点交互功能也得到支持。研究团队在视觉艺术家创作的有机软雕塑上进行了评估，重点验证了设备变形时触摸定位的稳定性，并探讨了该方法在艺术、娱乐及其他领域的应用潜力。

## 核心内容
### 方法架构
- **传感原理**：采用互电容（mutual-capacitance）传感技术，通过电极阵列检测人体触摸引起的电容变化，对非导电物体（如气动变形）不敏感。
- **仿真耦合**：在线集成SOFA框架的有限元仿真（finite-element simulation），实时模拟软体机器人的变形状态，将电容信号映射到三维曲面上的触摸位置。
- **多触点支持**：系统可同时处理多个触摸点，满足复杂交互需求。

### 实验设置
- **测试平台**：由视觉艺术家设计的有机软雕塑，具有不规则三维曲面和动态气动变形能力。
- **评估指标**：在设备静止与变形状态下，分别测量触摸定位的精度与鲁棒性。

### 关键结果
- **变形鲁棒性**：即使软雕塑在气动驱动下发生显著形变，触摸定位仍保持稳定，误差未显著增加。
- **选择性感知**：传感器仅响应人手等导电物体，气动变形不产生误触信号。
- **多触点性能**：多指同时触摸时，系统能准确区分各触点位置。

### 结论
该技术为软体机器人提供了低成本、易集成的触觉交互方案，尤其适用于艺术装置、娱乐机器人等需要变形表面触摸交互的场景。未来可扩展至医疗康复、人机协作等领域。

## Overview
In this paper, we present a touch technology to achieve tactile interactivity for human-robot interaction (HRI) in soft robotics. By combining a capacitive touch sensor with an online solid mechanics simulation provided by the SOFA framework, contact detection is achieved for arbitrary shapes. Furthermore, the implementation of the capacitive touch technology presented here is selectively sensitive to human touch (conductive objects), while it is largely unaffected by the deformations created by the pneumatic actuation of our soft robot. Multi-touch interactions are also possible. We evaluated our approach with an organic soft robotics sculpture that was created by a visual artist. In particular, we evaluate that the touch localization capabilities are robust under the deformation of the device. We discuss the potential this approach has for the arts and entertainment as well as other domains.

## 参考
- http://arxiv.org/abs/2503.02280v1

## 개요
이 연구는 상호 정전용량 센싱과 SOFA 프레임워크의 온라인 고체 역학 시뮬레이션을 결합하여, 소프트 로봇을 위한 변형에 강건한 촉각 피부를 구축했습니다. 센서는 사람의 손과 같은 전도성 물체에만 민감하며, 소프트 로봇의 공압 변형은 간섭 신호를 발생시키지 않아 임의의 형태를 가진 표면에서 접촉 감지가 가능합니다. 다중 접촉 상호작용 기능도 지원됩니다. 연구팀은 시각 예술가가 제작한 유기적 소프트 조각에서 평가를 진행했으며, 장치 변형 시 터치 위치 결정의 안정성을 중점적으로 검증하고, 이 방법의 예술, 엔터테인먼트 및 기타 분야에서의 응용 가능성을 탐구했습니다.

## 핵심 내용
### 방법 아키텍처
- **센싱 원리**: 상호 정전용량(mutual-capacitance) 센싱 기술을 채택하여 전극 배열을 통해 인체 터치로 인한 정전용량 변화를 감지하며, 비전도성 물체(예: 공압 변형)에는 민감하지 않습니다.
- **시뮬레이션 결합**: SOFA 프레임워크의 유한 요소 시뮬레이션(finite-element simulation)을 온라인으로 통합하여 소프트 로봇의 변형 상태를 실시간으로 모델링하고, 정전용량 신호를 3D 곡면 위의 터치 위치로 매핑합니다.
- **다중 접촉 지원**: 시스템은 여러 터치 포인트를 동시에 처리할 수 있어 복잡한 상호작용 요구를 충족합니다.

### 실험 설정
- **테스트 플랫폼**: 시각 예술가가 설계한 유기적 소프트 조각으로, 불규칙한 3D 곡면과 동적 공압 변형 능력을 갖추고 있습니다.
- **평가 지표**: 장치가 정지 상태와 변형 상태일 때 각각 터치 위치 결정의 정확도와 강건성을 측정했습니다.

### 주요 결과
- **변형 강건성**: 소프트 조각이 공압 구동으로 인해 상당한 변형을 겪어도 터치 위치 결정은 안정적으로 유지되었으며, 오차가 크게 증가하지 않았습니다.
- **선택적 감지**: 센서는 사람의 손과 같은 전도성 물체에만 반응하며, 공압 변형은 오접촉 신호를 발생시키지 않습니다.
- **다중 접촉 성능**: 여러 손가락이 동시에 터치할 때 시스템이 각 접촉 지점의 위치를 정확히 구분할 수 있습니다.

### 결론
이 기술은 소프트 로봇에 저비용이고 통합이 쉬운 촉각 상호작용 솔루션을 제공하며, 특히 변형 표면 터치 상호작용이 필요한 예술 설치물, 엔터테인먼트 로봇 등의 시나리오에 적합합니다. 향후 의료 재활, 인간-로봇 협업 등의 분야로 확장할 수 있습니다.
