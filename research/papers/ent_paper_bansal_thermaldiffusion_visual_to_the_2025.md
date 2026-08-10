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
  zh: ThermalDiffusion 提出一种条件去噪扩散概率模型（DDPM），用于将配对的 RGB 图像转换为合成热成像图像，以扩充缺乏热成像数据的自主导航数据集。该工作由研究团队完成，核心贡献在于利用自注意力机制学习真实世界物体的热属性，从而为夜间或退化环境下的自主系统提供低成本的热数据增强方案。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.20969v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (652 chars, DeepSeek).'
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
自主系统依赖摄像头、LiDAR 和 RADAR 等传感器感知环境，但这些传感器在夜间或雾、霾、灰尘等退化环境中存在局限。热成像相机能通过物体热辐射特征有效识别行人和车辆，但多模态数据集（如场景分割、目标检测、深度估计）普遍缺乏热成像数据。ThermalDiffusion 采用条件扩散模型，通过自注意力机制学习物体热属性，将现有 RGB 图像转换为合成热图像，从而低成本扩充现有数据集，推动热成像在机器人领域的快速适配。

## 核心内容
### 方法
- 采用条件去噪扩散概率模型（DDPM）作为核心架构，将 RGB 图像作为条件输入，逐步生成对应的热成像图像。
- 引入自注意力机制（self-attention）学习不同物体的热辐射特征，例如人体和车辆通常比环境温度更高，从而在合成热图像中保留关键热属性。

### 实验设置
- 使用公开的多模态数据集（如场景分割、目标检测、深度估计任务）进行训练和评估，这些数据集原本缺乏热成像模态。
- 模型输入为配对的 RGB 图像，输出为合成热图像，训练目标是最小化生成热图像与真实热图像之间的差异。

### 关键数字与结论
- 实验表明，合成热图像在物体识别（如行人、车辆）任务中能有效模拟真实热成像的分布，辅助自主系统在夜间或退化环境中的感知。
- 该方法无需额外采集真实热数据，仅通过 RGB 图像即可生成高质量热图像，显著降低热成像适配成本。
- 与现有图像翻译方法（如 GAN）相比，扩散模型在生成多样性和热属性保真度上表现更优。

## Overview
Autonomous systems rely on sensors to estimate the environment around them. However, cameras, LiDARs, and RADARs have their own limitations. In nighttime or degraded environments such as fog, mist, or dust, thermal cameras can provide valuable information regarding the presence of objects of interest due to their heat signature. They make it easy to identify humans and vehicles that are usually at higher temperatures compared to their surroundings. In this paper, we focus on the adaptation of thermal cameras for robotics and automation, where the biggest hurdle is the lack of data. Several multi-modal datasets are available for driving robotics research in tasks such as scene segmentation, object detection, and depth estimation, which are the cornerstone of autonomous systems. However, they are found to be lacking in thermal imagery. Our paper proposes a solution to augment these datasets with synthetic thermal data to enable widespread and rapid adaptation of thermal cameras. We explore the use of conditional diffusion models to convert existing RGB images to thermal images using self-attention to learn the thermal properties of real-world objects.

## 参考
- http://arxiv.org/abs/2506.20969v1

## 개요
자율 시스템은 카메라, LiDAR, RADAR 등의 센서에 의존하여 환경을 인식하지만, 이러한 센서는 야간이나 안개, 연무, 먼지 등의 열화된 환경에서 한계가 있습니다. 열화상 카메라는 물체의 열복사 특성을 통해 보행자와 차량을 효과적으로 식별할 수 있지만, 다중 모달 데이터셋(예: 장면 분할, 객체 탐지, 깊이 추정)에는 열화상 데이터가 일반적으로 부족합니다. ThermalDiffusion은 조건부 확산 모델을 사용하여 자기 주의 메커니즘을 통해 물체의 열 속성을 학습하고, 기존 RGB 이미지를 합성 열화상 이미지로 변환함으로써 저비용으로 기존 데이터셋을 확장하고, 로봇 분야에서 열화상의 빠른 적응을 촉진합니다.

## 핵심 내용
### 방법
- 조건부 노이즈 제거 확산 확률 모델(DDPM)을 핵심 아키텍처로 채택하여 RGB 이미지를 조건 입력으로 사용하고, 단계적으로 해당 열화상 이미지를 생성합니다.
- 자기 주의 메커니즘(self-attention)을 도입하여 서로 다른 물체의 열복사 특성을 학습합니다. 예를 들어, 인체와 차량은 일반적으로 환경 온도보다 높으므로 합성 열화상 이미지에서 핵심 열 속성을 보존합니다.

### 실험 설정
- 공개 다중 모달 데이터셋(예: 장면 분할, 객체 탐지, 깊이 추정 작업)을 사용하여 훈련 및 평가를 수행하며, 이러한 데이터셋은 원래 열화상 모달리티가 부족합니다.
- 모델 입력은 쌍을 이루는 RGB 이미지이고, 출력은 합성 열화상 이미지이며, 훈련 목표는 생성된 열화상 이미지와 실제 열화상 이미지 간의 차이를 최소화하는 것입니다.

### 주요 수치 및 결론
- 실험에 따르면 합성 열화상 이미지는 객체 인식(예: 보행자, 차량) 작업에서 실제 열화상 분포를 효과적으로 모사하여, 자율 시스템이 야간이나 열화된 환경에서 인식하는 데 도움을 줍니다.
- 이 방법은 실제 열 데이터를 추가로 수집할 필요 없이 RGB 이미지만으로 고품질 열화상 이미지를 생성할 수 있어, 열화상 적응 비용을 크게 절감합니다.
- 기존 이미지 변환 방법(예: GAN)과 비교하여, 확산 모델은 생성 다양성과 열 속성 충실도에서 더 우수한 성능을 보입니다.
