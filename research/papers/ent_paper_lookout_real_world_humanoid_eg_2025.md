---
$id: ent_paper_lookout_real_world_humanoid_eg_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LookOut: Real-World Humanoid Egocentric Navigation'
  zh: 'LookOut: Real-World Humanoid Egocentric Navigation'
  ko: 'LookOut: Real-World Humanoid Egocentric Navigation'
summary:
  en: 'LookOut: Real-World Humanoid Egocentric Navigation is a 2025 work on navigation for humanoid robots.'
  zh: 'LookOut: Real-World Humanoid Egocentric Navigation is a 2025 work on navigation for humanoid robots.'
  ko: 'LookOut: Real-World Humanoid Egocentric Navigation is a 2025 work on navigation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- lookout
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.14466v1.
sources:
- id: src_001
  type: paper
  title: 'LookOut: Real-World Humanoid Egocentric Navigation (arXiv)'
  url: https://arxiv.org/abs/2508.14466
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The ability to predict collision-free future trajectories from egocentric observations is crucial in applications such as humanoid robotics, VR / AR, and assistive navigation. In this work, we introduce the challenging problem of predicting a sequence of future 6D head poses from an egocentric video. In particular, we predict both head translations and rotations to learn the active information-gathering behavior expressed through head-turning events. To solve this task, we propose a framework that reasons over temporally aggregated 3D latent features, which models the geometric and semantic constraints for both the static and dynamic parts of the environment. Motivated by the lack of training data in this space, we further contribute a data collection pipeline using the Project Aria glasses, and present a dataset collected through this approach. Our dataset, dubbed Aria Navigation Dataset (AND), consists of 4 hours of recording of users navigating in real-world scenarios. It includes diverse situations and navigation behaviors, providing a valuable resource for learning real-world egocentric navigation policies. Extensive experiments show that our model learns human-like navigation behaviors such as waiting / slowing down, rerouting, and looking around for traffic while generalizing to unseen environments. Check out our project webpage at https://sites.google.com/stanford.edu/lookout.

## 核心内容
The ability to predict collision-free future trajectories from egocentric observations is crucial in applications such as humanoid robotics, VR / AR, and assistive navigation. In this work, we introduce the challenging problem of predicting a sequence of future 6D head poses from an egocentric video. In particular, we predict both head translations and rotations to learn the active information-gathering behavior expressed through head-turning events. To solve this task, we propose a framework that reasons over temporally aggregated 3D latent features, which models the geometric and semantic constraints for both the static and dynamic parts of the environment. Motivated by the lack of training data in this space, we further contribute a data collection pipeline using the Project Aria glasses, and present a dataset collected through this approach. Our dataset, dubbed Aria Navigation Dataset (AND), consists of 4 hours of recording of users navigating in real-world scenarios. It includes diverse situations and navigation behaviors, providing a valuable resource for learning real-world egocentric navigation policies. Extensive experiments show that our model learns human-like navigation behaviors such as waiting / slowing down, rerouting, and looking around for traffic while generalizing to unseen environments. Check out our project webpage at https://sites.google.com/stanford.edu/lookout.

## 参考
- http://arxiv.org/abs/2508.14466v1

## Overview
The ability to predict collision-free future trajectories from egocentric observations is crucial in applications such as humanoid robotics, VR / AR, and assistive navigation. In this work, we introduce the challenging problem of predicting a sequence of future 6D head poses from an egocentric video. In particular, we predict both head translations and rotations to learn the active information-gathering behavior expressed through head-turning events. To solve this task, we propose a framework that reasons over temporally aggregated 3D latent features, which models the geometric and semantic constraints for both the static and dynamic parts of the environment. Motivated by the lack of training data in this space, we further contribute a data collection pipeline using the Project Aria glasses, and present a dataset collected through this approach. Our dataset, dubbed Aria Navigation Dataset (AND), consists of 4 hours of recording of users navigating in real-world scenarios. It includes diverse situations and navigation behaviors, providing a valuable resource for learning real-world egocentric navigation policies. Extensive experiments show that our model learns human-like navigation behaviors such as waiting / slowing down, rerouting, and looking around for traffic while generalizing to unseen environments. Check out our project webpage at https://sites.google.com/stanford.edu/lookout.

## Content
The ability to predict collision-free future trajectories from egocentric observations is crucial in applications such as humanoid robotics, VR / AR, and assistive navigation. In this work, we introduce the challenging problem of predicting a sequence of future 6D head poses from an egocentric video. In particular, we predict both head translations and rotations to learn the active information-gathering behavior expressed through head-turning events. To solve this task, we propose a framework that reasons over temporally aggregated 3D latent features, which models the geometric and semantic constraints for both the static and dynamic parts of the environment. Motivated by the lack of training data in this space, we further contribute a data collection pipeline using the Project Aria glasses, and present a dataset collected through this approach. Our dataset, dubbed Aria Navigation Dataset (AND), consists of 4 hours of recording of users navigating in real-world scenarios. It includes diverse situations and navigation behaviors, providing a valuable resource for learning real-world egocentric navigation policies. Extensive experiments show that our model learns human-like navigation behaviors such as waiting / slowing down, rerouting, and looking around for traffic while generalizing to unseen environments. Check out our project webpage at https://sites.google.com/stanford.edu/lookout.

## 개요
자기중심적 관찰에서 충돌 없는 미래 궤적을 예측하는 능력은 휴머노이드 로봇공학, VR/AR, 보조 내비게이션과 같은 응용 분야에서 중요합니다. 본 연구에서는 자기중심적 비디오로부터 미래의 6D 머리 자세 시퀀스를 예측하는 도전적인 문제를 소개합니다. 특히, 머리 회전 이벤트를 통해 표현되는 능동적 정보 수집 행동을 학습하기 위해 머리 변환과 회전을 모두 예측합니다. 이 작업을 해결하기 위해, 환경의 정적 및 동적 부분에 대한 기하학적 및 의미론적 제약을 모델링하는 시간적으로 집계된 3D 잠재 특징을 추론하는 프레임워크를 제안합니다. 이 분야의 훈련 데이터 부족에 착안하여, Project Aria 안경을 사용한 데이터 수집 파이프라인을 추가로 제공하고, 이 접근법을 통해 수집된 데이터셋을 제시합니다. Aria Navigation Dataset (AND)라고 명명된 이 데이터셋은 실제 시나리오에서 사용자가 내비게이션하는 4시간 분량의 녹화로 구성됩니다. 다양한 상황과 내비게이션 행동을 포함하여 실제 세계의 자기중심적 내비게이션 정책을 학습하기 위한 귀중한 자원을 제공합니다. 광범위한 실험을 통해 우리의 모델이 대기/감속, 경로 재설정, 교통 상황을 살펴보는 등의 인간과 유사한 내비게이션 행동을 학습하고, 보지 못한 환경에도 일반화됨을 보여줍니다. 프로젝트 웹페이지는 https://sites.google.com/stanford.edu/lookout 에서 확인하세요.

## 핵심 내용
자기중심적 관찰에서 충돌 없는 미래 궤적을 예측하는 능력은 휴머노이드 로봇공학, VR/AR, 보조 내비게이션과 같은 응용 분야에서 중요합니다. 본 연구에서는 자기중심적 비디오로부터 미래의 6D 머리 자세 시퀀스를 예측하는 도전적인 문제를 소개합니다. 특히, 머리 회전 이벤트를 통해 표현되는 능동적 정보 수집 행동을 학습하기 위해 머리 변환과 회전을 모두 예측합니다. 이 작업을 해결하기 위해, 환경의 정적 및 동적 부분에 대한 기하학적 및 의미론적 제약을 모델링하는 시간적으로 집계된 3D 잠재 특징을 추론하는 프레임워크를 제안합니다. 이 분야의 훈련 데이터 부족에 착안하여, Project Aria 안경을 사용한 데이터 수집 파이프라인을 추가로 제공하고, 이 접근법을 통해 수집된 데이터셋을 제시합니다. Aria Navigation Dataset (AND)라고 명명된 이 데이터셋은 실제 시나리오에서 사용자가 내비게이션하는 4시간 분량의 녹화로 구성됩니다. 다양한 상황과 내비게이션 행동을 포함하여 실제 세계의 자기중심적 내비게이션 정책을 학습하기 위한 귀중한 자원을 제공합니다. 광범위한 실험을 통해 우리의 모델이 대기/감속, 경로 재설정, 교통 상황을 살펴보는 등의 인간과 유사한 내비게이션 행동을 학습하고, 보지 못한 환경에도 일반화됨을 보여줍니다. 프로젝트 웹페이지는 https://sites.google.com/stanford.edu/lookout 에서 확인하세요.
