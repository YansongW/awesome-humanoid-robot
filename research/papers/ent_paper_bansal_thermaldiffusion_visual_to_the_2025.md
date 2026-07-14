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
  zh: 本文提出了一种条件去噪扩散概率模型（DDPM），将成对的RGB图像转换为合成热成像图像，以补充缺乏热成像数据的自主导航数据集。
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

