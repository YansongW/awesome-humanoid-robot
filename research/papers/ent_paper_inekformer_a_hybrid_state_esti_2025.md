---
$id: ent_paper_inekformer_a_hybrid_state_esti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots'
  zh: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots'
  ko: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots'
summary:
  en: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots is a 2025 work on state estimation for humanoid robots.'
  zh: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots is a 2025 work on state estimation for humanoid robots.'
  ko: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots is a 2025 work on state estimation for humanoid robots.'
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
- inekformer
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16306v1.
sources:
- id: src_001
  type: paper
  title: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2511.16306
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have great potential for a wide range of applications, including industrial and domestic use, healthcare, and search and rescue missions. However, bipedal locomotion in different environments is still a challenge when it comes to performing stable and dynamic movements. This is where state estimation plays a crucial role, providing fast and accurate feedback of the robot's floating base state to the motion controller. Although classical state estimation methods such as Kalman filters are widely used in robotics, they require expert knowledge to fine-tune the noise parameters. Due to recent advances in the field of machine learning, deep learning methods are increasingly used for state estimation tasks. In this work, we propose the InEKFormer, a novel hybrid state estimation method that incorporates an invariant extended Kalman filter (InEKF) and a Transformer network. We compare our method with the InEKF and the KalmanNet approaches on datasets obtained from the humanoid robot RH5. The results indicate the potential of Transformers in humanoid state estimation, but also highlight the need for robust autoregressive training in these high-dimensional problems.

## 核心内容
Humanoid robots have great potential for a wide range of applications, including industrial and domestic use, healthcare, and search and rescue missions. However, bipedal locomotion in different environments is still a challenge when it comes to performing stable and dynamic movements. This is where state estimation plays a crucial role, providing fast and accurate feedback of the robot's floating base state to the motion controller. Although classical state estimation methods such as Kalman filters are widely used in robotics, they require expert knowledge to fine-tune the noise parameters. Due to recent advances in the field of machine learning, deep learning methods are increasingly used for state estimation tasks. In this work, we propose the InEKFormer, a novel hybrid state estimation method that incorporates an invariant extended Kalman filter (InEKF) and a Transformer network. We compare our method with the InEKF and the KalmanNet approaches on datasets obtained from the humanoid robot RH5. The results indicate the potential of Transformers in humanoid state estimation, but also highlight the need for robust autoregressive training in these high-dimensional problems.

## 参考
- http://arxiv.org/abs/2511.16306v1

## Overview
Humanoid robots have great potential for a wide range of applications, including industrial and domestic use, healthcare, and search and rescue missions. However, bipedal locomotion in different environments is still a challenge when it comes to performing stable and dynamic movements. This is where state estimation plays a crucial role, providing fast and accurate feedback of the robot's floating base state to the motion controller. Although classical state estimation methods such as Kalman filters are widely used in robotics, they require expert knowledge to fine-tune the noise parameters. Due to recent advances in the field of machine learning, deep learning methods are increasingly used for state estimation tasks. In this work, we propose the InEKFormer, a novel hybrid state estimation method that incorporates an invariant extended Kalman filter (InEKF) and a Transformer network. We compare our method with the InEKF and the KalmanNet approaches on datasets obtained from the humanoid robot RH5. The results indicate the potential of Transformers in humanoid state estimation, but also highlight the need for robust autoregressive training in these high-dimensional problems.

## Content
Humanoid robots have great potential for a wide range of applications, including industrial and domestic use, healthcare, and search and rescue missions. However, bipedal locomotion in different environments is still a challenge when it comes to performing stable and dynamic movements. This is where state estimation plays a crucial role, providing fast and accurate feedback of the robot's floating base state to the motion controller. Although classical state estimation methods such as Kalman filters are widely used in robotics, they require expert knowledge to fine-tune the noise parameters. Due to recent advances in the field of machine learning, deep learning methods are increasingly used for state estimation tasks. In this work, we propose the InEKFormer, a novel hybrid state estimation method that incorporates an invariant extended Kalman filter (InEKF) and a Transformer network. We compare our method with the InEKF and the KalmanNet approaches on datasets obtained from the humanoid robot RH5. The results indicate the potential of Transformers in humanoid state estimation, but also highlight the need for robust autoregressive training in these high-dimensional problems.

## 개요
휴머노이드 로봇은 산업 및 가정용, 의료, 수색 및 구조 임무를 포함한 광범위한 응용 분야에서 큰 잠재력을 가지고 있습니다. 그러나 다양한 환경에서의 이족 보행은 안정적이고 동적인 움직임을 수행하는 데 여전히 도전 과제로 남아 있습니다. 여기서 상태 추정이 중요한 역할을 하며, 로봇의 부동 베이스 상태에 대한 빠르고 정확한 피드백을 모션 컨트롤러에 제공합니다. 칼만 필터와 같은 고전적인 상태 추정 방법은 로봇 공학에서 널리 사용되지만, 노이즈 매개변수를 미세 조정하기 위해 전문가의 지식이 필요합니다. 최근 머신러닝 분야의 발전으로 인해 딥러닝 방법이 상태 추정 작업에 점점 더 많이 사용되고 있습니다. 본 연구에서는 불변 확장 칼만 필터(InEKF)와 트랜스포머 네트워크를 결합한 새로운 하이브리드 상태 추정 방법인 InEKFormer를 제안합니다. 우리는 휴머노이드 로봇 RH5에서 얻은 데이터셋을 사용하여 InEKF 및 KalmanNet 접근법과 우리의 방법을 비교합니다. 결과는 휴머노이드 상태 추정에서 트랜스포머의 잠재력을 보여주지만, 이러한 고차원 문제에서 강건한 자기회귀 훈련의 필요성도 강조합니다.

## 핵심 내용
휴머노이드 로봇은 산업 및 가정용, 의료, 수색 및 구조 임무를 포함한 광범위한 응용 분야에서 큰 잠재력을 가지고 있습니다. 그러나 다양한 환경에서의 이족 보행은 안정적이고 동적인 움직임을 수행하는 데 여전히 도전 과제로 남아 있습니다. 여기서 상태 추정이 중요한 역할을 하며, 로봇의 부동 베이스 상태에 대한 빠르고 정확한 피드백을 모션 컨트롤러에 제공합니다. 칼만 필터와 같은 고전적인 상태 추정 방법은 로봇 공학에서 널리 사용되지만, 노이즈 매개변수를 미세 조정하기 위해 전문가의 지식이 필요합니다. 최근 머신러닝 분야의 발전으로 인해 딥러닝 방법이 상태 추정 작업에 점점 더 많이 사용되고 있습니다. 본 연구에서는 불변 확장 칼만 필터(InEKF)와 트랜스포머 네트워크를 결합한 새로운 하이브리드 상태 추정 방법인 InEKFormer를 제안합니다. 우리는 휴머노이드 로봇 RH5에서 얻은 데이터셋을 사용하여 InEKF 및 KalmanNet 접근법과 우리의 방법을 비교합니다. 결과는 휴머노이드 상태 추정에서 트랜스포머의 잠재력을 보여주지만, 이러한 고차원 문제에서 강건한 자기회귀 훈련의 필요성도 강조합니다.
