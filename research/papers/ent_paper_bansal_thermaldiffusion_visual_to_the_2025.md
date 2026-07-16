---
$id: ent_paper_bansal_thermaldiffusion_visual_to_the_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ThermalDiffusion: Visual-to-Thermal Image-to-Image Translation for Autonomous Navigation'
  zh: ThermalDiffusion：用于自主导航的视觉到热成像图像转换
  ko: 'ThermalDiffusion: 자율 주행을 위한 가시광선-열영상 이미지 변환'
summary:
  en: This paper proposes a conditional denoising diffusion probabilistic model (DDPM) that translates paired RGB images into
    synthetic thermal images to augment autonomous navigation datasets lacking thermal imagery.
  zh: Autonomous systems rely on sensors to estimate the environment around them. However, cameras, LiDARs, and RADARs have
    their own limitations. In nighttime or degraded environments such as fog, mist, or dust, thermal cameras can provide valuable
    information regarding the presence of objects of interest due to their heat signature. They make it easy to identify humans
    and vehicles that are usually at higher temperatures compared to their surroundings. In this paper, we focus on the adaptation
    of thermal cameras for robotics and automation, where the biggest hurdle is the lack of data. Several mul
  ko: 본 논문은 열영상 데이터가 부족한 자율 주행 데이터셋을 보강하기 위해 쌍을 이룬 RGB 이미지를 합성 열영상으로 변환하는 조건부 노이즈 제거 확산 확률 모델(DDPM)을 제안한다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- thermal_imaging
- image_to_image_translation
- diffusion_models
- conditional_ddpm
- autonomous_navigation
- low_visibility_perception
- sensor_fusion
- computer_vision
- rgb_to_thermal
- data_augmentation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.20969v1.
sources:
- id: src_001
  type: paper
  title: 'ThermalDiffusion: Visual-to-Thermal Image-to-Image Translation for Autonomous Navigation'
  url: https://arxiv.org/abs/2506.20969
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## 概述
Autonomous systems rely on sensors to estimate the environment around them. However, cameras, LiDARs, and RADARs have their own limitations. In nighttime or degraded environments such as fog, mist, or dust, thermal cameras can provide valuable information regarding the presence of objects of interest due to their heat signature. They make it easy to identify humans and vehicles that are usually at higher temperatures compared to their surroundings. In this paper, we focus on the adaptation of thermal cameras for robotics and automation, where the biggest hurdle is the lack of data. Several multi-modal datasets are available for driving robotics research in tasks such as scene segmentation, object detection, and depth estimation, which are the cornerstone of autonomous systems. However, they are found to be lacking in thermal imagery. Our paper proposes a solution to augment these datasets with synthetic thermal data to enable widespread and rapid adaptation of thermal cameras. We explore the use of conditional diffusion models to convert existing RGB images to thermal images using self-attention to learn the thermal properties of real-world objects.

## 核心内容
Autonomous systems rely on sensors to estimate the environment around them. However, cameras, LiDARs, and RADARs have their own limitations. In nighttime or degraded environments such as fog, mist, or dust, thermal cameras can provide valuable information regarding the presence of objects of interest due to their heat signature. They make it easy to identify humans and vehicles that are usually at higher temperatures compared to their surroundings. In this paper, we focus on the adaptation of thermal cameras for robotics and automation, where the biggest hurdle is the lack of data. Several multi-modal datasets are available for driving robotics research in tasks such as scene segmentation, object detection, and depth estimation, which are the cornerstone of autonomous systems. However, they are found to be lacking in thermal imagery. Our paper proposes a solution to augment these datasets with synthetic thermal data to enable widespread and rapid adaptation of thermal cameras. We explore the use of conditional diffusion models to convert existing RGB images to thermal images using self-attention to learn the thermal properties of real-world objects.

## 参考
- http://arxiv.org/abs/2506.20969v1

## Overview
Autonomous systems rely on sensors to estimate the environment around them. However, cameras, LiDARs, and RADARs have their own limitations. In nighttime or degraded environments such as fog, mist, or dust, thermal cameras can provide valuable information regarding the presence of objects of interest due to their heat signature. They make it easy to identify humans and vehicles that are usually at higher temperatures compared to their surroundings. In this paper, we focus on the adaptation of thermal cameras for robotics and automation, where the biggest hurdle is the lack of data. Several multi-modal datasets are available for driving robotics research in tasks such as scene segmentation, object detection, and depth estimation, which are the cornerstone of autonomous systems. However, they are found to be lacking in thermal imagery. Our paper proposes a solution to augment these datasets with synthetic thermal data to enable widespread and rapid adaptation of thermal cameras. We explore the use of conditional diffusion models to convert existing RGB images to thermal images using self-attention to learn the thermal properties of real-world objects.

## Content
Autonomous systems rely on sensors to estimate the environment around them. However, cameras, LiDARs, and RADARs have their own limitations. In nighttime or degraded environments such as fog, mist, or dust, thermal cameras can provide valuable information regarding the presence of objects of interest due to their heat signature. They make it easy to identify humans and vehicles that are usually at higher temperatures compared to their surroundings. In this paper, we focus on the adaptation of thermal cameras for robotics and automation, where the biggest hurdle is the lack of data. Several multi-modal datasets are available for driving robotics research in tasks such as scene segmentation, object detection, and depth estimation, which are the cornerstone of autonomous systems. However, they are found to be lacking in thermal imagery. Our paper proposes a solution to augment these datasets with synthetic thermal data to enable widespread and rapid adaptation of thermal cameras. We explore the use of conditional diffusion models to convert existing RGB images to thermal images using self-attention to learn the thermal properties of real-world objects.

## 개요
자율 시스템은 주변 환경을 추정하기 위해 센서에 의존합니다. 그러나 카메라, LiDAR, RADAR는 각각 한계를 가지고 있습니다. 야간이나 안개, 연무, 먼지와 같은 열화된 환경에서 열화상 카메라는 열 신호를 통해 관심 대상의 존재에 대한 귀중한 정보를 제공할 수 있습니다. 이는 주변보다 일반적으로 높은 온도를 가진 사람과 차량을 식별하는 데 용이합니다. 본 논문에서는 로봇 공학 및 자동화를 위한 열화상 카메라의 적응에 초점을 맞추며, 가장 큰 장애물은 데이터 부족입니다. 장면 분할, 객체 탐지, 깊이 추정과 같은 작업에서 로봇 공학 연구를 추진하기 위한 여러 다중 모드 데이터셋이 존재하며, 이는 자율 시스템의 초석입니다. 그러나 이러한 데이터셋은 열화상 이미지가 부족한 것으로 나타났습니다. 본 논문은 이러한 데이터셋을 합성 열화상 데이터로 보강하여 열화상 카메라의 광범위하고 신속한 적응을 가능하게 하는 솔루션을 제안합니다. 우리는 조건부 확산 모델을 사용하여 기존 RGB 이미지를 열화상 이미지로 변환하고, 자기 주의 메커니즘을 통해 실제 객체의 열적 특성을 학습합니다.

## 핵심 내용
자율 시스템은 주변 환경을 추정하기 위해 센서에 의존합니다. 그러나 카메라, LiDAR, RADAR는 각각 한계를 가지고 있습니다. 야간이나 안개, 연무, 먼지와 같은 열화된 환경에서 열화상 카메라는 열 신호를 통해 관심 대상의 존재에 대한 귀중한 정보를 제공할 수 있습니다. 이는 주변보다 일반적으로 높은 온도를 가진 사람과 차량을 식별하는 데 용이합니다. 본 논문에서는 로봇 공학 및 자동화를 위한 열화상 카메라의 적응에 초점을 맞추며, 가장 큰 장애물은 데이터 부족입니다. 장면 분할, 객체 탐지, 깊이 추정과 같은 작업에서 로봇 공학 연구를 추진하기 위한 여러 다중 모드 데이터셋이 존재하며, 이는 자율 시스템의 초석입니다. 그러나 이러한 데이터셋은 열화상 이미지가 부족한 것으로 나타났습니다. 본 논문은 이러한 데이터셋을 합성 열화상 데이터로 보강하여 열화상 카메라의 광범위하고 신속한 적응을 가능하게 하는 솔루션을 제안합니다. 우리는 조건부 확산 모델을 사용하여 기존 RGB 이미지를 열화상 이미지로 변환하고, 자기 주의 메커니즘을 통해 실제 객체의 열적 특성을 학습합니다.
