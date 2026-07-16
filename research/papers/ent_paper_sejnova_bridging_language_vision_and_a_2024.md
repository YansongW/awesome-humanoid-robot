---
$id: ent_paper_sejnova_bridging_language_vision_and_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Bridging Language, Vision and Action: Multimodal VAEs in Robotic Manipulation Tasks'
  zh: Bridging Language Vision and Action
  ko: 'Bridging Language, Vision and Action: Multimodal VAEs in Robotic Manipulation Tasks'
summary:
  en: 'Bridging Language, Vision and Action: Multimodal VAEs in Robotic Manipulation Tasks (Bridging Language Vision and Action),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Czech Technical University in Prague,
    and published at IROS24.'
  zh: 'Bridging Language, Vision and Action: Multimodal VAEs in Robotic Manipulation Tasks (Bridging Language Vision and Action),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Czech Technical University in Prague,
    and published at IROS24.'
  ko: 'Bridging Language, Vision and Action: Multimodal VAEs in Robotic Manipulation Tasks (Bridging Language Vision and Action),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Czech Technical University in Prague,
    and published at IROS24.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bridging_language_vision_and_a
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2404.01932v2.
sources:
- id: src_001
  type: website
  title: Bridging Language Vision and Action source
  url: https://doi.org/10.1109/IROS58592.2024.10802160
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
In this work, we focus on unsupervised vision-language-action mapping in the area of robotic manipulation. Recently, multiple approaches employing pre-trained large language and vision models have been proposed for this task. However, they are computationally demanding and require careful fine-tuning of the produced outputs. A more lightweight alternative would be the implementation of multimodal Variational Autoencoders (VAEs) which can extract the latent features of the data and integrate them into a joint representation, as has been demonstrated mostly on image-image or image-text data for the state-of-the-art models. Here we explore whether and how can multimodal VAEs be employed in unsupervised robotic manipulation tasks in a simulated environment. Based on the obtained results, we propose a model-invariant training alternative that improves the models' performance in a simulator by up to 55%. Moreover, we systematically evaluate the challenges raised by the individual tasks such as object or robot position variability, number of distractors or the task length. Our work thus also sheds light on the potential benefits and limitations of using the current multimodal VAEs for unsupervised learning of robotic motion trajectories based on vision and language.

## 核心内容
In this work, we focus on unsupervised vision-language-action mapping in the area of robotic manipulation. Recently, multiple approaches employing pre-trained large language and vision models have been proposed for this task. However, they are computationally demanding and require careful fine-tuning of the produced outputs. A more lightweight alternative would be the implementation of multimodal Variational Autoencoders (VAEs) which can extract the latent features of the data and integrate them into a joint representation, as has been demonstrated mostly on image-image or image-text data for the state-of-the-art models. Here we explore whether and how can multimodal VAEs be employed in unsupervised robotic manipulation tasks in a simulated environment. Based on the obtained results, we propose a model-invariant training alternative that improves the models' performance in a simulator by up to 55%. Moreover, we systematically evaluate the challenges raised by the individual tasks such as object or robot position variability, number of distractors or the task length. Our work thus also sheds light on the potential benefits and limitations of using the current multimodal VAEs for unsupervised learning of robotic motion trajectories based on vision and language.

## 参考
- http://arxiv.org/abs/2404.01932v2

## Overview
In this work, we focus on unsupervised vision-language-action mapping in the area of robotic manipulation. Recently, multiple approaches employing pre-trained large language and vision models have been proposed for this task. However, they are computationally demanding and require careful fine-tuning of the produced outputs. A more lightweight alternative would be the implementation of multimodal Variational Autoencoders (VAEs) which can extract the latent features of the data and integrate them into a joint representation, as has been demonstrated mostly on image-image or image-text data for the state-of-the-art models. Here we explore whether and how can multimodal VAEs be employed in unsupervised robotic manipulation tasks in a simulated environment. Based on the obtained results, we propose a model-invariant training alternative that improves the models' performance in a simulator by up to 55%. Moreover, we systematically evaluate the challenges raised by the individual tasks such as object or robot position variability, number of distractors or the task length. Our work thus also sheds light on the potential benefits and limitations of using the current multimodal VAEs for unsupervised learning of robotic motion trajectories based on vision and language.

## Content
In this work, we focus on unsupervised vision-language-action mapping in the area of robotic manipulation. Recently, multiple approaches employing pre-trained large language and vision models have been proposed for this task. However, they are computationally demanding and require careful fine-tuning of the produced outputs. A more lightweight alternative would be the implementation of multimodal Variational Autoencoders (VAEs) which can extract the latent features of the data and integrate them into a joint representation, as has been demonstrated mostly on image-image or image-text data for the state-of-the-art models. Here we explore whether and how can multimodal VAEs be employed in unsupervised robotic manipulation tasks in a simulated environment. Based on the obtained results, we propose a model-invariant training alternative that improves the models' performance in a simulator by up to 55%. Moreover, we systematically evaluate the challenges raised by the individual tasks such as object or robot position variability, number of distractors or the task length. Our work thus also sheds light on the potential benefits and limitations of using the current multimodal VAEs for unsupervised learning of robotic motion trajectories based on vision and language.

## 개요
본 연구에서는 로봇 조작 분야에서의 비지도 시각-언어-행동 매핑에 초점을 맞춥니다. 최근 이 작업을 위해 사전 학습된 대규모 언어 및 시각 모델을 활용하는 여러 접근 방식이 제안되었습니다. 그러나 이러한 방식은 계산 요구량이 많고 생성된 출력물의 세심한 미세 조정이 필요합니다. 더 가벼운 대안으로는 데이터의 잠재 특징을 추출하고 이를 공동 표현으로 통합할 수 있는 다중 모드 변분 오토인코더(VAE)의 구현이 있으며, 이는 최첨단 모델에서 주로 이미지-이미지 또는 이미지-텍스트 데이터에 대해 입증되었습니다. 본 연구에서는 시뮬레이션 환경에서 비지도 로봇 조작 작업에 다중 모드 VAE를 적용할 수 있는지와 그 방법을 탐구합니다. 얻은 결과를 바탕으로 시뮬레이터에서 모델 성능을 최대 55% 향상시키는 모델 불변 훈련 대안을 제안합니다. 또한 객체 또는 로봇 위치 변동성, 방해 요소 수, 작업 길이 등 개별 작업에서 발생하는 문제를 체계적으로 평가합니다. 따라서 본 연구는 현재의 다중 모드 VAE를 사용하여 시각 및 언어 기반 로봇 운동 궤적의 비지도 학습에 대한 잠재적 이점과 한계를 조명합니다.

## 핵심 내용
본 연구에서는 로봇 조작 분야에서의 비지도 시각-언어-행동 매핑에 초점을 맞춥니다. 최근 이 작업을 위해 사전 학습된 대규모 언어 및 시각 모델을 활용하는 여러 접근 방식이 제안되었습니다. 그러나 이러한 방식은 계산 요구량이 많고 생성된 출력물의 세심한 미세 조정이 필요합니다. 더 가벼운 대안으로는 데이터의 잠재 특징을 추출하고 이를 공동 표현으로 통합할 수 있는 다중 모드 변분 오토인코더(VAE)의 구현이 있으며, 이는 최첨단 모델에서 주로 이미지-이미지 또는 이미지-텍스트 데이터에 대해 입증되었습니다. 본 연구에서는 시뮬레이션 환경에서 비지도 로봇 조작 작업에 다중 모드 VAE를 적용할 수 있는지와 그 방법을 탐구합니다. 얻은 결과를 바탕으로 시뮬레이터에서 모델 성능을 최대 55% 향상시키는 모델 불변 훈련 대안을 제안합니다. 또한 객체 또는 로봇 위치 변동성, 방해 요소 수, 작업 길이 등 개별 작업에서 발생하는 문제를 체계적으로 평가합니다. 따라서 본 연구는 현재의 다중 모드 VAE를 사용하여 시각 및 언어 기반 로봇 운동 궤적의 비지도 학습에 대한 잠재적 이점과 한계를 조명합니다.
