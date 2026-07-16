---
$id: ent_paper_li_urbanvla_a_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility'
  zh: UrbanVLA
  ko: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility'
summary:
  en: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (UrbanVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Galbot, USTC, BAAI.'
  zh: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (UrbanVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Galbot, USTC, BAAI.'
  ko: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (UrbanVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Galbot, USTC, BAAI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- urbanvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.23576v1.
sources:
- id: src_001
  type: paper
  title: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (arXiv)'
  url: https://arxiv.org/abs/2510.23576
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UrbanVLA source
  url: https://doi.org/10.48550/arXiv.2510.23576
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Urban micromobility applications, such as delivery robots, demand reliable navigation across large-scale urban environments while following long-horizon route instructions. This task is particularly challenging due to the dynamic and unstructured nature of real-world city areas, yet most existing navigation methods remain tailored to short-scale and controllable scenarios. Effective urban micromobility requires two complementary levels of navigation skills: low-level capabilities such as point-goal reaching and obstacle avoidance, and high-level capabilities, such as route-visual alignment. To this end, we propose UrbanVLA, a route-conditioned Vision-Language-Action (VLA) framework designed for scalable urban navigation. Our method explicitly aligns noisy route waypoints with visual observations during execution, and subsequently plans trajectories to drive the robot. To enable UrbanVLA to master both levels of navigation, we employ a two-stage training pipeline. The process begins with Supervised Fine-Tuning (SFT) using simulated environments and trajectories parsed from web videos. This is followed by Reinforcement Fine-Tuning (RFT) on a mixture of simulation and real-world data, which enhances the model's safety and adaptability in real-world settings. Experiments demonstrate that UrbanVLA surpasses strong baselines by more than 55% in the SocialNav task on MetaUrban. Furthermore, UrbanVLA achieves reliable real-world navigation, showcasing both scalability to large-scale urban environments and robustness against real-world uncertainties.

## 核心内容
Urban micromobility applications, such as delivery robots, demand reliable navigation across large-scale urban environments while following long-horizon route instructions. This task is particularly challenging due to the dynamic and unstructured nature of real-world city areas, yet most existing navigation methods remain tailored to short-scale and controllable scenarios. Effective urban micromobility requires two complementary levels of navigation skills: low-level capabilities such as point-goal reaching and obstacle avoidance, and high-level capabilities, such as route-visual alignment. To this end, we propose UrbanVLA, a route-conditioned Vision-Language-Action (VLA) framework designed for scalable urban navigation. Our method explicitly aligns noisy route waypoints with visual observations during execution, and subsequently plans trajectories to drive the robot. To enable UrbanVLA to master both levels of navigation, we employ a two-stage training pipeline. The process begins with Supervised Fine-Tuning (SFT) using simulated environments and trajectories parsed from web videos. This is followed by Reinforcement Fine-Tuning (RFT) on a mixture of simulation and real-world data, which enhances the model's safety and adaptability in real-world settings. Experiments demonstrate that UrbanVLA surpasses strong baselines by more than 55% in the SocialNav task on MetaUrban. Furthermore, UrbanVLA achieves reliable real-world navigation, showcasing both scalability to large-scale urban environments and robustness against real-world uncertainties.

## 参考
- http://arxiv.org/abs/2510.23576v1

## Overview
Urban micromobility applications, such as delivery robots, demand reliable navigation across large-scale urban environments while following long-horizon route instructions. This task is particularly challenging due to the dynamic and unstructured nature of real-world city areas, yet most existing navigation methods remain tailored to short-scale and controllable scenarios. Effective urban micromobility requires two complementary levels of navigation skills: low-level capabilities such as point-goal reaching and obstacle avoidance, and high-level capabilities, such as route-visual alignment. To this end, we propose UrbanVLA, a route-conditioned Vision-Language-Action (VLA) framework designed for scalable urban navigation. Our method explicitly aligns noisy route waypoints with visual observations during execution, and subsequently plans trajectories to drive the robot. To enable UrbanVLA to master both levels of navigation, we employ a two-stage training pipeline. The process begins with Supervised Fine-Tuning (SFT) using simulated environments and trajectories parsed from web videos. This is followed by Reinforcement Fine-Tuning (RFT) on a mixture of simulation and real-world data, which enhances the model's safety and adaptability in real-world settings. Experiments demonstrate that UrbanVLA surpasses strong baselines by more than 55% in the SocialNav task on MetaUrban. Furthermore, UrbanVLA achieves reliable real-world navigation, showcasing both scalability to large-scale urban environments and robustness against real-world uncertainties.

## Content
Urban micromobility applications, such as delivery robots, demand reliable navigation across large-scale urban environments while following long-horizon route instructions. This task is particularly challenging due to the dynamic and unstructured nature of real-world city areas, yet most existing navigation methods remain tailored to short-scale and controllable scenarios. Effective urban micromobility requires two complementary levels of navigation skills: low-level capabilities such as point-goal reaching and obstacle avoidance, and high-level capabilities, such as route-visual alignment. To this end, we propose UrbanVLA, a route-conditioned Vision-Language-Action (VLA) framework designed for scalable urban navigation. Our method explicitly aligns noisy route waypoints with visual observations during execution, and subsequently plans trajectories to drive the robot. To enable UrbanVLA to master both levels of navigation, we employ a two-stage training pipeline. The process begins with Supervised Fine-Tuning (SFT) using simulated environments and trajectories parsed from web videos. This is followed by Reinforcement Fine-Tuning (RFT) on a mixture of simulation and real-world data, which enhances the model's safety and adaptability in real-world settings. Experiments demonstrate that UrbanVLA surpasses strong baselines by more than 55% in the SocialNav task on MetaUrban. Furthermore, UrbanVLA achieves reliable real-world navigation, showcasing both scalability to large-scale urban environments and robustness against real-world uncertainties.

## 개요
도시 마이크로모빌리티 애플리케이션(예: 배달 로봇)은 장기 경로 지침을 따르면서 대규모 도시 환경에서 안정적인 내비게이션을 요구합니다. 실제 도시 지역의 동적이고 비구조적인 특성으로 인해 이 작업은 특히 어렵지만, 대부분의 기존 내비게이션 방법은 단기적이고 통제 가능한 시나리오에 맞춰져 있습니다. 효과적인 도시 마이크로모빌리티는 두 가지 상호 보완적인 수준의 내비게이션 기술을 필요로 합니다: 지점 목표 도달 및 장애물 회피와 같은 저수준 능력, 그리고 경로-시각 정렬과 같은 고수준 능력입니다. 이를 위해 우리는 확장 가능한 도시 내비게이션을 위해 설계된 경로 조건부 Vision-Language-Action (VLA) 프레임워크인 UrbanVLA를 제안합니다. 우리의 방법은 실행 중에 잡음이 있는 경로 웨이포인트를 시각적 관찰과 명시적으로 정렬한 후, 로봇을 구동하기 위한 궤적을 계획합니다. UrbanVLA가 두 수준의 내비게이션을 모두 마스터할 수 있도록 하기 위해, 우리는 2단계 훈련 파이프라인을 사용합니다. 이 과정은 시뮬레이션 환경과 웹 비디오에서 추출된 궤적을 사용한 지도 미세 조정(SFT)으로 시작됩니다. 그 다음, 시뮬레이션과 실제 데이터의 혼합에 대한 강화 미세 조정(RFT)이 이어져, 실제 환경에서 모델의 안전성과 적응성을 향상시킵니다. 실험 결과, UrbanVLA는 MetaUrban의 SocialNav 작업에서 강력한 기준선을 55% 이상 능가합니다. 또한, UrbanVLA는 신뢰할 수 있는 실제 내비게이션을 달성하여 대규모 도시 환경으로의 확장성과 실제 불확실성에 대한 강건성을 모두 보여줍니다.

## 핵심 내용
도시 마이크로모빌리티 애플리케이션(예: 배달 로봇)은 장기 경로 지침을 따르면서 대규모 도시 환경에서 안정적인 내비게이션을 요구합니다. 실제 도시 지역의 동적이고 비구조적인 특성으로 인해 이 작업은 특히 어렵지만, 대부분의 기존 내비게이션 방법은 단기적이고 통제 가능한 시나리오에 맞춰져 있습니다. 효과적인 도시 마이크로모빌리티는 두 가지 상호 보완적인 수준의 내비게이션 기술을 필요로 합니다: 지점 목표 도달 및 장애물 회피와 같은 저수준 능력, 그리고 경로-시각 정렬과 같은 고수준 능력입니다. 이를 위해 우리는 확장 가능한 도시 내비게이션을 위해 설계된 경로 조건부 Vision-Language-Action (VLA) 프레임워크인 UrbanVLA를 제안합니다. 우리의 방법은 실행 중에 잡음이 있는 경로 웨이포인트를 시각적 관찰과 명시적으로 정렬한 후, 로봇을 구동하기 위한 궤적을 계획합니다. UrbanVLA가 두 수준의 내비게이션을 모두 마스터할 수 있도록 하기 위해, 우리는 2단계 훈련 파이프라인을 사용합니다. 이 과정은 시뮬레이션 환경과 웹 비디오에서 추출된 궤적을 사용한 지도 미세 조정(SFT)으로 시작됩니다. 그 다음, 시뮬레이션과 실제 데이터의 혼합에 대한 강화 미세 조정(RFT)이 이어져, 실제 환경에서 모델의 안전성과 적응성을 향상시킵니다. 실험 결과, UrbanVLA는 MetaUrban의 SocialNav 작업에서 강력한 기준선을 55% 이상 능가합니다. 또한, UrbanVLA는 신뢰할 수 있는 실제 내비게이션을 달성하여 대규모 도시 환경으로의 확장성과 실제 불확실성에 대한 강건성을 모두 보여줍니다.
