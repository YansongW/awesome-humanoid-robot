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

