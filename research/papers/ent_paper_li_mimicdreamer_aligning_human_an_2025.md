---
$id: ent_paper_li_mimicdreamer_aligning_human_an_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training'
  zh: MimicDreamer
  ko: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training'
summary:
  en: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (MimicDreamer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by GigaAI, CASIA, NJUST, Tsinghua University.'
  zh: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (MimicDreamer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by GigaAI, CASIA, NJUST, Tsinghua University.'
  ko: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (MimicDreamer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by GigaAI, CASIA, NJUST, Tsinghua University.'
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
- mimicdreamer
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22199v2.
sources:
- id: src_001
  type: paper
  title: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (arXiv)'
  url: https://arxiv.org/abs/2509.22199
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MimicDreamer source
  url: https://doi.org/10.48550/arXiv.2509.22199
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision Language Action (VLA) models derive their generalization capability from diverse training data, yet collecting embodied robot interaction data remains prohibitively expensive. In contrast, human demonstration videos are far more scalable and cost-efficient to collect, and recent studies confirm their effectiveness in training VLA models. However, a significant domain gap persists between human videos and robot-executed videos, including unstable camera viewpoints, visual discrepancies between human hands and robotic arms, and differences in motion dynamics. To bridge this gap, we propose MimicDreamer, a framework that turns fast, low-cost human demonstrations into robot-usable supervision by jointly aligning vision, viewpoint, and actions to directly support policy training. For visual alignment, we propose H2R Aligner, a video diffusion model that generates high-fidelity robot demonstration videos by transferring motion from human manipulation footage. For viewpoint stabilization, EgoStabilizer is proposed, which canonicalizes egocentric videos via homography and inpaints occlusions and distortions caused by warping. For action alignment, we map human hand trajectories to the robot frame and apply a constrained inverse kinematics solver to produce feasible, low-jitter joint commands with accurate pose tracking. Empirically, VLA models trained purely on our synthesized human-to-robot videos achieve few-shot execution on real robots. Moreover, scaling training with human data significantly boosts performance compared to models trained solely on real robot data; our approach improves the average success rate by 14.7\% across six representative manipulation tasks.

## 核心内容
Vision Language Action (VLA) models derive their generalization capability from diverse training data, yet collecting embodied robot interaction data remains prohibitively expensive. In contrast, human demonstration videos are far more scalable and cost-efficient to collect, and recent studies confirm their effectiveness in training VLA models. However, a significant domain gap persists between human videos and robot-executed videos, including unstable camera viewpoints, visual discrepancies between human hands and robotic arms, and differences in motion dynamics. To bridge this gap, we propose MimicDreamer, a framework that turns fast, low-cost human demonstrations into robot-usable supervision by jointly aligning vision, viewpoint, and actions to directly support policy training. For visual alignment, we propose H2R Aligner, a video diffusion model that generates high-fidelity robot demonstration videos by transferring motion from human manipulation footage. For viewpoint stabilization, EgoStabilizer is proposed, which canonicalizes egocentric videos via homography and inpaints occlusions and distortions caused by warping. For action alignment, we map human hand trajectories to the robot frame and apply a constrained inverse kinematics solver to produce feasible, low-jitter joint commands with accurate pose tracking. Empirically, VLA models trained purely on our synthesized human-to-robot videos achieve few-shot execution on real robots. Moreover, scaling training with human data significantly boosts performance compared to models trained solely on real robot data; our approach improves the average success rate by 14.7\% across six representative manipulation tasks.

## 参考
- http://arxiv.org/abs/2509.22199v2

## Overview
Vision Language Action (VLA) models derive their generalization capability from diverse training data, yet collecting embodied robot interaction data remains prohibitively expensive. In contrast, human demonstration videos are far more scalable and cost-efficient to collect, and recent studies confirm their effectiveness in training VLA models. However, a significant domain gap persists between human videos and robot-executed videos, including unstable camera viewpoints, visual discrepancies between human hands and robotic arms, and differences in motion dynamics. To bridge this gap, we propose MimicDreamer, a framework that turns fast, low-cost human demonstrations into robot-usable supervision by jointly aligning vision, viewpoint, and actions to directly support policy training. For visual alignment, we propose H2R Aligner, a video diffusion model that generates high-fidelity robot demonstration videos by transferring motion from human manipulation footage. For viewpoint stabilization, EgoStabilizer is proposed, which canonicalizes egocentric videos via homography and inpaints occlusions and distortions caused by warping. For action alignment, we map human hand trajectories to the robot frame and apply a constrained inverse kinematics solver to produce feasible, low-jitter joint commands with accurate pose tracking. Empirically, VLA models trained purely on our synthesized human-to-robot videos achieve few-shot execution on real robots. Moreover, scaling training with human data significantly boosts performance compared to models trained solely on real robot data; our approach improves the average success rate by 14.7\% across six representative manipulation tasks.

## Content
Vision Language Action (VLA) models derive their generalization capability from diverse training data, yet collecting embodied robot interaction data remains prohibitively expensive. In contrast, human demonstration videos are far more scalable and cost-efficient to collect, and recent studies confirm their effectiveness in training VLA models. However, a significant domain gap persists between human videos and robot-executed videos, including unstable camera viewpoints, visual discrepancies between human hands and robotic arms, and differences in motion dynamics. To bridge this gap, we propose MimicDreamer, a framework that turns fast, low-cost human demonstrations into robot-usable supervision by jointly aligning vision, viewpoint, and actions to directly support policy training. For visual alignment, we propose H2R Aligner, a video diffusion model that generates high-fidelity robot demonstration videos by transferring motion from human manipulation footage. For viewpoint stabilization, EgoStabilizer is proposed, which canonicalizes egocentric videos via homography and inpaints occlusions and distortions caused by warping. For action alignment, we map human hand trajectories to the robot frame and apply a constrained inverse kinematics solver to produce feasible, low-jitter joint commands with accurate pose tracking. Empirically, VLA models trained purely on our synthesized human-to-robot videos achieve few-shot execution on real robots. Moreover, scaling training with human data significantly boosts performance compared to models trained solely on real robot data; our approach improves the average success rate by 14.7\% across six representative manipulation tasks.

## 개요
Vision Language Action (VLA) 모델은 다양한 훈련 데이터로부터 일반화 능력을 얻지만, 실제 로봇 상호작용 데이터를 수집하는 것은 엄청난 비용이 든다. 반면, 인간 시연 영상은 훨씬 확장 가능하고 비용 효율적으로 수집할 수 있으며, 최근 연구들은 VLA 모델 훈련에 있어 그 효과성을 확인하고 있다. 그러나 인간 영상과 로봇 실행 영상 사이에는 불안정한 카메라 시점, 인간 손과 로봇 팔 간의 시각적 차이, 동작 역학의 차이 등 상당한 도메인 격차가 존재한다. 이러한 격차를 해소하기 위해, 우리는 MimicDreamer를 제안한다. 이 프레임워크는 빠르고 저렴한 인간 시연을 로봇이 사용 가능한 감독 신호로 변환하며, 시각, 시점, 행동을 공동으로 정렬하여 정책 훈련을 직접 지원한다. 시각 정렬을 위해 H2R Aligner를 제안하는데, 이는 인간 조작 영상에서 동작을 전이하여 고충실도 로봇 시연 영상을 생성하는 비디오 확산 모델이다. 시점 안정화를 위해 EgoStabilizer를 제안하며, 이는 호모그래피를 통해 자아 중심 영상을 정규화하고 왜곡으로 인한 폐색과 변형을 인페인팅한다. 행동 정렬을 위해 인간 손 궤적을 로봇 프레임에 매핑하고 제약 조건이 있는 역기구학 솔버를 적용하여 정확한 자세 추적으로 실행 가능하고 저지터 관절 명령을 생성한다. 실험적으로, 우리가 합성한 인간-로봇 영상만으로 훈련된 VLA 모델은 실제 로봇에서 퓨샷 실행을 달성한다. 또한, 인간 데이터로 훈련 규모를 확장하면 실제 로봇 데이터만으로 훈련된 모델에 비해 성능이 크게 향상된다. 우리의 접근 방식은 여섯 가지 대표적인 조작 작업에서 평균 성공률을 14.7% 향상시킨다.

## 핵심 내용
Vision Language Action (VLA) 모델은 다양한 훈련 데이터로부터 일반화 능력을 얻지만, 실제 로봇 상호작용 데이터를 수집하는 것은 엄청난 비용이 든다. 반면, 인간 시연 영상은 훨씬 확장 가능하고 비용 효율적으로 수집할 수 있으며, 최근 연구들은 VLA 모델 훈련에 있어 그 효과성을 확인하고 있다. 그러나 인간 영상과 로봇 실행 영상 사이에는 불안정한 카메라 시점, 인간 손과 로봇 팔 간의 시각적 차이, 동작 역학의 차이 등 상당한 도메인 격차가 존재한다. 이러한 격차를 해소하기 위해, 우리는 MimicDreamer를 제안한다. 이 프레임워크는 빠르고 저렴한 인간 시연을 로봇이 사용 가능한 감독 신호로 변환하며, 시각, 시점, 행동을 공동으로 정렬하여 정책 훈련을 직접 지원한다. 시각 정렬을 위해 H2R Aligner를 제안하는데, 이는 인간 조작 영상에서 동작을 전이하여 고충실도 로봇 시연 영상을 생성하는 비디오 확산 모델이다. 시점 안정화를 위해 EgoStabilizer를 제안하며, 이는 호모그래피를 통해 자아 중심 영상을 정규화하고 왜곡으로 인한 폐색과 변형을 인페인팅한다. 행동 정렬을 위해 인간 손 궤적을 로봇 프레임에 매핑하고 제약 조건이 있는 역기구학 솔버를 적용하여 정확한 자세 추적으로 실행 가능하고 저지터 관절 명령을 생성한다. 실험적으로, 우리가 합성한 인간-로봇 영상만으로 훈련된 VLA 모델은 실제 로봇에서 퓨샷 실행을 달성한다. 또한, 인간 데이터로 훈련 규모를 확장하면 실제 로봇 데이터만으로 훈련된 모델에 비해 성능이 크게 향상된다. 우리의 접근 방식은 여섯 가지 대표적인 조작 작업에서 평균 성공률을 14.7% 향상시킨다.
