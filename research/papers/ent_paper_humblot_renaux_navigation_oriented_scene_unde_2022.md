---
$id: ent_paper_humblot_renaux_navigation_oriented_scene_unde_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Navigation-Oriented Scene Understanding for Robotic Autonomy: Learning to Segment
    Driveability in Egocentric Images'
  zh: 面向导航的场景理解：以自我中心图像学习可驾驶区域分割
  ko: '로봇 자율 주행을 위한 내비게이션 중심 장면 이해: 자기중심 영상에서 주행 가능 영역 분할 학습'
summary:
  en: The paper proposes a supervised segmentation framework that labels egocentric
    outdoor images with three ordinal driveability levels, using soft ordinal labels
    and a safety-critical pixel-wise loss weighting to improve generalization across
    urban and off-road datasets.
  zh: 该论文提出一种监督式分割框架，以自我中心户外图像为输入，使用三个有序可驾驶等级、软有序标签以及面向安全关键像素的损失加权，提升跨城市场景与越野场景数据集的泛化能力。
  ko: 본 논문은 자기중심 야외 영상에 3단계 순서형 주행 가능 수준 레이블을 부여하고, 소프트 순서형 라벨과 안전에 중요한 픽셀별 손실 가중치를
    사용하여 도심과 오프로드 데이터셋 간 일반화 성능을 향상시키는 감독 기반 분할 프레임워크를 제안한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'Navigation-Oriented Scene Understanding for Robotic Autonomy: Learning to
    Segment Driveability in Egocentric Images'
  url: https://arxiv.org/abs/2109.07245
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper addresses outdoor robotic scene understanding from a navigation perspective. Rather than predicting descriptive object categories, the authors propose to segment egocentric onboard images into three generic driveability levels: directly drivable, indirectly drivable, and non-drivable. This affordance representation is designed to transfer across urban and off-road domains without being tied to fixed semantic classes. The framework is built around an image segmentation network and trained in a supervised manner on publicly available segmentation datasets whose semantic labels are mapped to the three driveability levels.

A key element of the method is the use of soft ordinal (SORD) labels to represent the driveability classes. Instead of one-hot targets, the model learns a probability distribution over ordered classes that reflects the distance between levels, thereby encoding ambiguity and severity relationships. In addition, the authors introduce a navigation-oriented pixel-wise loss weighting strategy that gives higher importance to safety-critical regions, particularly pixels close to the camera and away from object boundaries. The combined approach is evaluated on a diverse collection of datasets spanning city streets, snowy trails, and forest paths.

The experiments include within-dataset training and cross-dataset generalization tests, with particular emphasis on the WildDash benchmark as an unseen evaluation set. Results indicate that the proposed ordinal encoding and loss weighting improve driveability estimation over standard hard-label segmentation, especially when models are trained on a mixture of datasets and evaluated on environments not seen during training.

## Key Contributions

- A navigation-oriented framework for learning driveability segmentation that enables cross-dataset training without real-world exploration or additional labeling.
- Soft ordinal label encoding that incorporates inter-class severity and ambiguity among the three driveability levels.
- A pixel-wise loss weighting method that emphasizes safety-critical regions near the camera and de-emphasizes object-boundary pixels.
- Cross-dataset generalization evaluation across multiple public datasets, including the WildDash benchmark.

## Relevance to Humanoid Robotics

The perception principles developed in this work are transferable to humanoid robots operating in unstructured outdoor environments. Pixel-wise driveability estimation provides a domain-agnostic representation that can feed into path planning and footstep placement decisions, reducing reliance on pre-defined object categories. The emphasis on safety-critical close-range regions is also relevant for bipedal locomotion, where local terrain traversability directly affects balance and collision avoidance. While the paper focuses on wheeled-robot applications, the scene-understanding methodology and cross-dataset generalization strategy offer a useful starting point for humanoid outdoor navigation research.
