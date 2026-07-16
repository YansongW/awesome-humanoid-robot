---
$id: ent_paper_levy_meta_learning_online_dynamics_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving
  zh: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving
  ko: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving
summary:
  en: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving (Meta-Learning Online Dynamics Model Adaptation
    in Off-Road Autonomous Driving), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Jet Propulsion Laboratory, California Institute of Technology, University of Texas at Austin, Georgia Institute of Technology,
    and published at RSS25.
  zh: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving (Meta-Learning Online Dynamics Model Adaptation
    in Off-Road Autonomous Driving), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Jet Propulsion Laboratory, California Institute of Technology, University of Texas at Austin, Georgia Institute of Technology,
    and published at RSS25.
  ko: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving (Meta-Learning Online Dynamics Model Adaptation
    in Off-Road Autonomous Driving), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Jet Propulsion Laboratory, California Institute of Technology, University of Texas at Austin, Georgia Institute of Technology,
    and published at RSS25.
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
- meta_learning_online_dynamics
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.16923v1.
sources:
- id: src_001
  type: paper
  title: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving (arXiv)
  url: https://arxiv.org/abs/2504.16923
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving source
  url: https://doi.org/10.48550/arXiv.2504.16923
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
High-speed off-road autonomous driving presents unique challenges due to complex, evolving terrain characteristics and the difficulty of accurately modeling terrain-vehicle interactions. While dynamics models used in model-based control can be learned from real-world data, they often struggle to generalize to unseen terrain, making real-time adaptation essential. We propose a novel framework that combines a Kalman filter-based online adaptation scheme with meta-learned parameters to address these challenges. Offline meta-learning optimizes the basis functions along which adaptation occurs, as well as the adaptation parameters, while online adaptation dynamically adjusts the onboard dynamics model in real time for model-based control. We validate our approach through extensive experiments, including real-world testing on a full-scale autonomous off-road vehicle, demonstrating that our method outperforms baseline approaches in prediction accuracy, performance, and safety metrics, particularly in safety-critical scenarios. Our results underscore the effectiveness of meta-learned dynamics model adaptation, advancing the development of reliable autonomous systems capable of navigating diverse and unseen environments. Video is available at: https://youtu.be/cCKHHrDRQEA

## 核心内容
High-speed off-road autonomous driving presents unique challenges due to complex, evolving terrain characteristics and the difficulty of accurately modeling terrain-vehicle interactions. While dynamics models used in model-based control can be learned from real-world data, they often struggle to generalize to unseen terrain, making real-time adaptation essential. We propose a novel framework that combines a Kalman filter-based online adaptation scheme with meta-learned parameters to address these challenges. Offline meta-learning optimizes the basis functions along which adaptation occurs, as well as the adaptation parameters, while online adaptation dynamically adjusts the onboard dynamics model in real time for model-based control. We validate our approach through extensive experiments, including real-world testing on a full-scale autonomous off-road vehicle, demonstrating that our method outperforms baseline approaches in prediction accuracy, performance, and safety metrics, particularly in safety-critical scenarios. Our results underscore the effectiveness of meta-learned dynamics model adaptation, advancing the development of reliable autonomous systems capable of navigating diverse and unseen environments. Video is available at: https://youtu.be/cCKHHrDRQEA

## 参考
- http://arxiv.org/abs/2504.16923v1

## Overview
High-speed off-road autonomous driving presents unique challenges due to complex, evolving terrain characteristics and the difficulty of accurately modeling terrain-vehicle interactions. While dynamics models used in model-based control can be learned from real-world data, they often struggle to generalize to unseen terrain, making real-time adaptation essential. We propose a novel framework that combines a Kalman filter-based online adaptation scheme with meta-learned parameters to address these challenges. Offline meta-learning optimizes the basis functions along which adaptation occurs, as well as the adaptation parameters, while online adaptation dynamically adjusts the onboard dynamics model in real time for model-based control. We validate our approach through extensive experiments, including real-world testing on a full-scale autonomous off-road vehicle, demonstrating that our method outperforms baseline approaches in prediction accuracy, performance, and safety metrics, particularly in safety-critical scenarios. Our results underscore the effectiveness of meta-learned dynamics model adaptation, advancing the development of reliable autonomous systems capable of navigating diverse and unseen environments. Video is available at: https://youtu.be/cCKHHrDRQEA

## Content
High-speed off-road autonomous driving presents unique challenges due to complex, evolving terrain characteristics and the difficulty of accurately modeling terrain-vehicle interactions. While dynamics models used in model-based control can be learned from real-world data, they often struggle to generalize to unseen terrain, making real-time adaptation essential. We propose a novel framework that combines a Kalman filter-based online adaptation scheme with meta-learned parameters to address these challenges. Offline meta-learning optimizes the basis functions along which adaptation occurs, as well as the adaptation parameters, while online adaptation dynamically adjusts the onboard dynamics model in real time for model-based control. We validate our approach through extensive experiments, including real-world testing on a full-scale autonomous off-road vehicle, demonstrating that our method outperforms baseline approaches in prediction accuracy, performance, and safety metrics, particularly in safety-critical scenarios. Our results underscore the effectiveness of meta-learned dynamics model adaptation, advancing the development of reliable autonomous systems capable of navigating diverse and unseen environments. Video is available at: https://youtu.be/cCKHHrDRQEA

## 개요
고속 오프로드 자율 주행은 복잡하고 변화하는 지형 특성과 지형-차량 상호작용을 정확히 모델링하기 어렵다는 점에서 독특한 도전 과제를 제시합니다. 모델 기반 제어에 사용되는 동역학 모델은 실제 데이터로부터 학습될 수 있지만, 보지 못한 지형에 일반화하는 데 어려움을 겪는 경우가 많아 실시간 적응이 필수적입니다. 우리는 이러한 문제를 해결하기 위해 칼만 필터 기반 온라인 적응 기법과 메타 학습된 파라미터를 결합한 새로운 프레임워크를 제안합니다. 오프라인 메타 학습은 적응이 이루어지는 기저 함수와 적응 파라미터를 최적화하는 반면, 온라인 적응은 모델 기반 제어를 위해 탑재된 동역학 모델을 실시간으로 동적으로 조정합니다. 우리는 실제 대형 자율 오프로드 차량을 사용한 실험을 포함한 광범위한 실험을 통해 접근 방식을 검증했으며, 특히 안전이 중요한 시나리오에서 예측 정확도, 성능 및 안전 지표에서 기준 방법보다 뛰어난 성능을 보여주었습니다. 우리의 결과는 메타 학습된 동역학 모델 적응의 효과를 강조하며, 다양하고 보지 못한 환경을 탐색할 수 있는 신뢰할 수 있는 자율 시스템 개발을 진전시킵니다. 비디오는 다음에서 확인할 수 있습니다: https://youtu.be/cCKHHrDRQEA

## 핵심 내용
고속 오프로드 자율 주행은 복잡하고 변화하는 지형 특성과 지형-차량 상호작용을 정확히 모델링하기 어렵다는 점에서 독특한 도전 과제를 제시합니다. 모델 기반 제어에 사용되는 동역학 모델은 실제 데이터로부터 학습될 수 있지만, 보지 못한 지형에 일반화하는 데 어려움을 겪는 경우가 많아 실시간 적응이 필수적입니다. 우리는 이러한 문제를 해결하기 위해 칼만 필터 기반 온라인 적응 기법과 메타 학습된 파라미터를 결합한 새로운 프레임워크를 제안합니다. 오프라인 메타 학습은 적응이 이루어지는 기저 함수와 적응 파라미터를 최적화하는 반면, 온라인 적응은 모델 기반 제어를 위해 탑재된 동역학 모델을 실시간으로 동적으로 조정합니다. 우리는 실제 대형 자율 오프로드 차량을 사용한 실험을 포함한 광범위한 실험을 통해 접근 방식을 검증했으며, 특히 안전이 중요한 시나리오에서 예측 정확도, 성능 및 안전 지표에서 기준 방법보다 뛰어난 성능을 보여주었습니다. 우리의 결과는 메타 학습된 동역학 모델 적응의 효과를 강조하며, 다양하고 보지 못한 환경을 탐색할 수 있는 신뢰할 수 있는 자율 시스템 개발을 진전시킵니다. 비디오는 다음에서 확인할 수 있습니다: https://youtu.be/cCKHHrDRQEA
