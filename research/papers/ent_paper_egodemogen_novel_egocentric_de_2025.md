---
$id: ent_paper_egodemogen_novel_egocentric_de_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation'
  zh: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation'
  ko: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation'
summary:
  en: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation is a 2025 work on manipulation
    for humanoid robots.'
  zh: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation is a 2025 work on manipulation
    for humanoid robots.'
  ko: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation is a 2025 work on manipulation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egodemogen
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22578v2.
sources:
- id: src_001
  type: paper
  title: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.22578
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning based visuomotor policies have achieved strong performance in robotic manipulation, yet they often remain sensitive to egocentric viewpoint shifts. Unlike third-person viewpoint changes that only move the camera, egocentric shifts simultaneously alter both the camera pose and the robot action coordinate frame, making it necessary to jointly transfer action trajectories and synthesize corresponding observations under novel egocentric viewpoints. To address this challenge, we present EgoDemoGen, a framework that generates paired observation--action demonstrations under novel egocentric viewpoints through two key components: 1{)} EgoTrajTransfer, which transfers robot trajectories to the novel egocentric coordinate frame through motion-skill segmentation, geometry-aware transformation, and inverse kinematics filtering; and 2{)} EgoViewTransfer, a conditional video generation model that fuses a novel-viewpoint reprojected scene video and a robot motion video rendered from the transferred trajectory to synthesize photorealistic observations, trained with a self-supervised double reprojection strategy without requiring multi-viewpoint data. Experiments in simulation and real-world settings show that EgoDemoGen consistently improves policy success rates under both standard and novel egocentric viewpoints, with absolute gains of +24.6\% and +16.9\% in simulation and +16.0\% and +23.0\% on the real robot. Moreover, EgoViewTransfer achieves superior video generation quality for novel egocentric observations.

## 核心内容
Imitation learning based visuomotor policies have achieved strong performance in robotic manipulation, yet they often remain sensitive to egocentric viewpoint shifts. Unlike third-person viewpoint changes that only move the camera, egocentric shifts simultaneously alter both the camera pose and the robot action coordinate frame, making it necessary to jointly transfer action trajectories and synthesize corresponding observations under novel egocentric viewpoints. To address this challenge, we present EgoDemoGen, a framework that generates paired observation--action demonstrations under novel egocentric viewpoints through two key components: 1{)} EgoTrajTransfer, which transfers robot trajectories to the novel egocentric coordinate frame through motion-skill segmentation, geometry-aware transformation, and inverse kinematics filtering; and 2{)} EgoViewTransfer, a conditional video generation model that fuses a novel-viewpoint reprojected scene video and a robot motion video rendered from the transferred trajectory to synthesize photorealistic observations, trained with a self-supervised double reprojection strategy without requiring multi-viewpoint data. Experiments in simulation and real-world settings show that EgoDemoGen consistently improves policy success rates under both standard and novel egocentric viewpoints, with absolute gains of +24.6\% and +16.9\% in simulation and +16.0\% and +23.0\% on the real robot. Moreover, EgoViewTransfer achieves superior video generation quality for novel egocentric observations.

## 参考
- http://arxiv.org/abs/2509.22578v2

## Overview
Imitation learning based visuomotor policies have achieved strong performance in robotic manipulation, yet they often remain sensitive to egocentric viewpoint shifts. Unlike third-person viewpoint changes that only move the camera, egocentric shifts simultaneously alter both the camera pose and the robot action coordinate frame, making it necessary to jointly transfer action trajectories and synthesize corresponding observations under novel egocentric viewpoints. To address this challenge, we present EgoDemoGen, a framework that generates paired observation--action demonstrations under novel egocentric viewpoints through two key components: 1{)} EgoTrajTransfer, which transfers robot trajectories to the novel egocentric coordinate frame through motion-skill segmentation, geometry-aware transformation, and inverse kinematics filtering; and 2{)} EgoViewTransfer, a conditional video generation model that fuses a novel-viewpoint reprojected scene video and a robot motion video rendered from the transferred trajectory to synthesize photorealistic observations, trained with a self-supervised double reprojection strategy without requiring multi-viewpoint data. Experiments in simulation and real-world settings show that EgoDemoGen consistently improves policy success rates under both standard and novel egocentric viewpoints, with absolute gains of +24.6\% and +16.9\% in simulation and +16.0\% and +23.0\% on the real robot. Moreover, EgoViewTransfer achieves superior video generation quality for novel egocentric observations.

## Content
Imitation learning based visuomotor policies have achieved strong performance in robotic manipulation, yet they often remain sensitive to egocentric viewpoint shifts. Unlike third-person viewpoint changes that only move the camera, egocentric shifts simultaneously alter both the camera pose and the robot action coordinate frame, making it necessary to jointly transfer action trajectories and synthesize corresponding observations under novel egocentric viewpoints. To address this challenge, we present EgoDemoGen, a framework that generates paired observation--action demonstrations under novel egocentric viewpoints through two key components: 1{)} EgoTrajTransfer, which transfers robot trajectories to the novel egocentric coordinate frame through motion-skill segmentation, geometry-aware transformation, and inverse kinematics filtering; and 2{)} EgoViewTransfer, a conditional video generation model that fuses a novel-viewpoint reprojected scene video and a robot motion video rendered from the transferred trajectory to synthesize photorealistic observations, trained with a self-supervised double reprojection strategy without requiring multi-viewpoint data. Experiments in simulation and real-world settings show that EgoDemoGen consistently improves policy success rates under both standard and novel egocentric viewpoints, with absolute gains of +24.6\% and +16.9\% in simulation and +16.0\% and +23.0\% on the real robot. Moreover, EgoViewTransfer achieves superior video generation quality for novel egocentric observations.

## 개요
모방 학습 기반 시각-운동 정책(visuomotor policy)은 로봇 조작 작업에서 뛰어난 성능을 보여주었지만, 여전히 자기중심 시점(egocentric viewpoint) 변화에 민감한 경우가 많습니다. 카메라만 이동시키는 3인칭 시점 변화와 달리, 자기중심 시점 변화는 카메라 자세와 로봇 동작 좌표계를 동시에 변경하므로, 새로운 자기중심 시점에서 동작 궤적을 함께 전이하고 이에 대응하는 관측 데이터를 합성하는 것이 필요합니다. 이러한 문제를 해결하기 위해, 우리는 EgoDemoGen을 제안합니다. 이 프레임워크는 두 가지 핵심 구성 요소를 통해 새로운 자기중심 시점에서 짝을 이루는 관측-동작 데모를 생성합니다: 1) EgoTrajTransfer는 동작-기술 분할, 기하학 인식 변환, 역기구학 필터링을 통해 로봇 궤적을 새로운 자기중심 좌표계로 전이합니다; 2) EgoViewTransfer는 조건부 비디오 생성 모델로, 새로운 시점에서 재투영된 장면 비디오와 전이된 궤적으로부터 렌더링된 로봇 동작 비디오를 융합하여 사실적인 관측 데이터를 합성하며, 다중 시점 데이터 없이 자기지도 이중 재투영 전략으로 훈련됩니다. 시뮬레이션 및 실제 환경 실험에서 EgoDemoGen은 표준 및 새로운 자기중심 시점 모두에서 정책 성공률을 일관되게 향상시켰으며, 시뮬레이션에서 +24.6% 및 +16.9%, 실제 로봇에서 +16.0% 및 +23.0%의 절대적 성능 향상을 보였습니다. 또한, EgoViewTransfer는 새로운 자기중심 관측 데이터에 대해 우수한 비디오 생성 품질을 달성했습니다.

## 핵심 내용
모방 학습 기반 시각-운동 정책(visuomotor policy)은 로봇 조작 작업에서 뛰어난 성능을 보여주었지만, 여전히 자기중심 시점(egocentric viewpoint) 변화에 민감한 경우가 많습니다. 카메라만 이동시키는 3인칭 시점 변화와 달리, 자기중심 시점 변화는 카메라 자세와 로봇 동작 좌표계를 동시에 변경하므로, 새로운 자기중심 시점에서 동작 궤적을 함께 전이하고 이에 대응하는 관측 데이터를 합성하는 것이 필요합니다. 이러한 문제를 해결하기 위해, 우리는 EgoDemoGen을 제안합니다. 이 프레임워크는 두 가지 핵심 구성 요소를 통해 새로운 자기중심 시점에서 짝을 이루는 관측-동작 데모를 생성합니다: 1) EgoTrajTransfer는 동작-기술 분할, 기하학 인식 변환, 역기구학 필터링을 통해 로봇 궤적을 새로운 자기중심 좌표계로 전이합니다; 2) EgoViewTransfer는 조건부 비디오 생성 모델로, 새로운 시점에서 재투영된 장면 비디오와 전이된 궤적으로부터 렌더링된 로봇 동작 비디오를 융합하여 사실적인 관측 데이터를 합성하며, 다중 시점 데이터 없이 자기지도 이중 재투영 전략으로 훈련됩니다. 시뮬레이션 및 실제 환경 실험에서 EgoDemoGen은 표준 및 새로운 자기중심 시점 모두에서 정책 성공률을 일관되게 향상시켰으며, 시뮬레이션에서 +24.6% 및 +16.9%, 실제 로봇에서 +16.0% 및 +23.0%의 절대적 성능 향상을 보였습니다. 또한, EgoViewTransfer는 새로운 자기중심 관측 데이터에 대해 우수한 비디오 생성 품질을 달성했습니다.
