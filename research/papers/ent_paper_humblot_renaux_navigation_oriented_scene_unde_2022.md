---
$id: ent_paper_humblot_renaux_navigation_oriented_scene_unde_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Navigation-Oriented Scene Understanding for Robotic Autonomy: Learning to Segment Driveability in Egocentric Images'
  zh: 面向导航的场景理解：以自我中心图像学习可驾驶区域分割
  ko: '로봇 자율 주행을 위한 내비게이션 중심 장면 이해: 자기중심 영상에서 주행 가능 영역 분할 학습'
summary:
  en: The paper proposes a supervised segmentation framework that labels egocentric outdoor images with three ordinal driveability
    levels, using soft ordinal labels and a safety-critical pixel-wise loss weighting to improve generalization across urban
    and off-road datasets.
  zh: 该论文提出一种监督式分割框架，以自我中心户外图像为输入，使用三个有序可驾驶等级、软有序标签以及面向安全关键像素的损失加权，提升跨城市场景与越野场景数据集的泛化能力。
  ko: 본 논문은 자기중심 야외 영상에 3단계 순서형 주행 가능 수준 레이블을 부여하고, 소프트 순서형 라벨과 안전에 중요한 픽셀별 손실 가중치를 사용하여 도심과 오프로드 데이터셋 간 일반화 성능을 향상시키는 감독
    기반 분할 프레임워크를 제안한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- scene_understanding
- semantic_segmentation
- driveability_segmentation
- affordance_learning
- ordinal_classification
- outdoor_navigation
- egocentric_vision
- cross_dataset_generalization
- robot_perception
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2109.07245v2.
sources:
- id: src_001
  type: paper
  title: 'Navigation-Oriented Scene Understanding for Robotic Autonomy: Learning to Segment Driveability in Egocentric Images'
  url: https://arxiv.org/abs/2109.07245
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
This work tackles scene understanding for outdoor robotic navigation, solely relying on images captured by an on-board camera. Conventional visual scene understanding interprets the environment based on specific descriptive categories. However, such a representation is not directly interpretable for decision-making and constrains robot operation to a specific domain. Thus, we propose to segment egocentric images directly in terms of how a robot can navigate in them, and tailor the learning problem to an autonomous navigation task. Building around an image segmentation network, we present a generic affordance consisting of 3 driveability levels which can broadly apply to both urban and off-road scenes. By encoding these levels with soft ordinal labels, we incorporate inter-class distances during learning which improves segmentation compared to standard "hard" one-hot labelling. In addition, we propose a navigation-oriented pixel-wise loss weighting method which assigns higher importance to safety-critical areas. We evaluate our approach on large-scale public image segmentation datasets ranging from sunny city streets to snowy forest trails. In a cross-dataset generalization experiment, we show that our affordance learning scheme can be applied across a diverse mix of datasets and improves driveability estimation in unseen environments compared to general-purpose, single-dataset segmentation.

## 核心内容
This work tackles scene understanding for outdoor robotic navigation, solely relying on images captured by an on-board camera. Conventional visual scene understanding interprets the environment based on specific descriptive categories. However, such a representation is not directly interpretable for decision-making and constrains robot operation to a specific domain. Thus, we propose to segment egocentric images directly in terms of how a robot can navigate in them, and tailor the learning problem to an autonomous navigation task. Building around an image segmentation network, we present a generic affordance consisting of 3 driveability levels which can broadly apply to both urban and off-road scenes. By encoding these levels with soft ordinal labels, we incorporate inter-class distances during learning which improves segmentation compared to standard "hard" one-hot labelling. In addition, we propose a navigation-oriented pixel-wise loss weighting method which assigns higher importance to safety-critical areas. We evaluate our approach on large-scale public image segmentation datasets ranging from sunny city streets to snowy forest trails. In a cross-dataset generalization experiment, we show that our affordance learning scheme can be applied across a diverse mix of datasets and improves driveability estimation in unseen environments compared to general-purpose, single-dataset segmentation.

## 参考
- http://arxiv.org/abs/2109.07245v2

## Overview
This work tackles scene understanding for outdoor robotic navigation, solely relying on images captured by an on-board camera. Conventional visual scene understanding interprets the environment based on specific descriptive categories. However, such a representation is not directly interpretable for decision-making and constrains robot operation to a specific domain. Thus, we propose to segment egocentric images directly in terms of how a robot can navigate in them, and tailor the learning problem to an autonomous navigation task. Building around an image segmentation network, we present a generic affordance consisting of 3 driveability levels which can broadly apply to both urban and off-road scenes. By encoding these levels with soft ordinal labels, we incorporate inter-class distances during learning which improves segmentation compared to standard "hard" one-hot labelling. In addition, we propose a navigation-oriented pixel-wise loss weighting method which assigns higher importance to safety-critical areas. We evaluate our approach on large-scale public image segmentation datasets ranging from sunny city streets to snowy forest trails. In a cross-dataset generalization experiment, we show that our affordance learning scheme can be applied across a diverse mix of datasets and improves driveability estimation in unseen environments compared to general-purpose, single-dataset segmentation.

## Content
This work tackles scene understanding for outdoor robotic navigation, solely relying on images captured by an on-board camera. Conventional visual scene understanding interprets the environment based on specific descriptive categories. However, such a representation is not directly interpretable for decision-making and constrains robot operation to a specific domain. Thus, we propose to segment egocentric images directly in terms of how a robot can navigate in them, and tailor the learning problem to an autonomous navigation task. Building around an image segmentation network, we present a generic affordance consisting of 3 driveability levels which can broadly apply to both urban and off-road scenes. By encoding these levels with soft ordinal labels, we incorporate inter-class distances during learning which improves segmentation compared to standard "hard" one-hot labelling. In addition, we propose a navigation-oriented pixel-wise loss weighting method which assigns higher importance to safety-critical areas. We evaluate our approach on large-scale public image segmentation datasets ranging from sunny city streets to snowy forest trails. In a cross-dataset generalization experiment, we show that our affordance learning scheme can be applied across a diverse mix of datasets and improves driveability estimation in unseen environments compared to general-purpose, single-dataset segmentation.

## 개요
본 연구는 차량 탑재 카메라로 촬영한 이미지만을 활용하여 야외 로봇 항법을 위한 장면 이해 문제를 다룹니다. 기존의 시각적 장면 이해는 특정 설명적 범주를 기반으로 환경을 해석합니다. 그러나 이러한 표현 방식은 의사 결정에 직접적으로 해석 가능하지 않으며 로봇의 작동을 특정 영역으로 제한합니다. 따라서 우리는 로봇이 이미지 내에서 어떻게 항법할 수 있는지에 따라 자기중심적 이미지를 직접 분할하고, 학습 문제를 자율 항법 작업에 맞게 조정할 것을 제안합니다. 이미지 분할 네트워크를 기반으로, 도시 및 비포장 도로 장면에 광범위하게 적용 가능한 3가지 주행 가능성 수준으로 구성된 일반적 어포던스를 제시합니다. 이러한 수준을 소프트 순서 레이블로 인코딩함으로써 학습 중 클래스 간 거리를 통합하여 표준적인 "하드" 원-핫 레이블링보다 분할 성능을 향상시킵니다. 또한, 안전이 중요한 영역에 더 높은 중요도를 할당하는 항법 지향적 픽셀 단위 손실 가중치 방법을 제안합니다. 우리는 화창한 도시 거리에서 눈 덮인 숲길에 이르기까지 대규모 공개 이미지 분할 데이터셋에서 접근 방식을 평가합니다. 교차 데이터셋 일반화 실험을 통해, 우리의 어포던스 학습 방식이 다양한 데이터셋 혼합에 적용될 수 있으며, 범용 단일 데이터셋 분할에 비해 보이지 않는 환경에서 주행 가능성 추정을 개선함을 보여줍니다.

## 핵심 내용
본 연구는 차량 탑재 카메라로 촬영한 이미지만을 활용하여 야외 로봇 항법을 위한 장면 이해 문제를 다룹니다. 기존의 시각적 장면 이해는 특정 설명적 범주를 기반으로 환경을 해석합니다. 그러나 이러한 표현 방식은 의사 결정에 직접적으로 해석 가능하지 않으며 로봇의 작동을 특정 영역으로 제한합니다. 따라서 우리는 로봇이 이미지 내에서 어떻게 항법할 수 있는지에 따라 자기중심적 이미지를 직접 분할하고, 학습 문제를 자율 항법 작업에 맞게 조정할 것을 제안합니다. 이미지 분할 네트워크를 기반으로, 도시 및 비포장 도로 장면에 광범위하게 적용 가능한 3가지 주행 가능성 수준으로 구성된 일반적 어포던스를 제시합니다. 이러한 수준을 소프트 순서 레이블로 인코딩함으로써 학습 중 클래스 간 거리를 통합하여 표준적인 "하드" 원-핫 레이블링보다 분할 성능을 향상시킵니다. 또한, 안전이 중요한 영역에 더 높은 중요도를 할당하는 항법 지향적 픽셀 단위 손실 가중치 방법을 제안합니다. 우리는 화창한 도시 거리에서 눈 덮인 숲길에 이르기까지 대규모 공개 이미지 분할 데이터셋에서 접근 방식을 평가합니다. 교차 데이터셋 일반화 실험을 통해, 우리의 어포던스 학습 방식이 다양한 데이터셋 혼합에 적용될 수 있으며, 범용 단일 데이터셋 분할에 비해 보이지 않는 환경에서 주행 가능성 추정을 개선함을 보여줍니다.
