---
$id: ent_paper_liu_semantics_aware_adaptive_knowl_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Semantics-aware Adaptive Knowledge Distillation for Sensor-to-Vision Action Recognition
  zh: 面向传感器到视觉动作识别的语义感知自适应知识蒸馏
  ko: 센서-비전 동작 인식을 위한 의미 인지 적응형 지식 증류
summary:
  en: This paper proposes SAKDN, a framework that distills knowledge from multiple wearable-sensor modalities into an RGB-video
    student network for action recognition, using Gramian Angular Field virtual images and modules for adaptive teacher fusion
    and graph-guided semantic transfer.
  zh: 本文提出SAKDN框架，通过将多个可穿戴传感器模态的知识蒸馏到RGB视频学生网络中实现动作识别，并利用格拉姆角场虚拟图像以及自适应教师融合和图引导语义迁移模块完成跨模态知识传递。
  ko: 본 논문은 다수의 웨어러블 센서 모달리티에서 RGB 비디오 학생 네트워크로 지식을 증류하여 동작 인식을 수행하는 SAKDN 프레임워크를 제안하며, Gramian Angular Field 가상 이미지와 적응형
    교사 융합 및 그래프 기반 의미 전이 모듈을 활용한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- action_recognition
- knowledge_distillation
- multi_modal_fusion
- sensor_to_vision
- wearable_sensors
- rgb_video
- gramian_angular_field
- human_robot_interaction
- spatio_temporal_learning
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2009.00210v5.
sources:
- id: src_001
  type: paper
  title: Semantics-aware Adaptive Knowledge Distillation for Sensor-to-Vision Action Recognition
  url: https://arxiv.org/abs/2009.00210
  date: '2021'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Existing vision-based action recognition is susceptible to occlusion and appearance variations, while wearable sensors can alleviate these challenges by capturing human motion with one-dimensional time-series signal. For the same action, the knowledge learned from vision sensors and wearable sensors, may be related and complementary. However, there exists significantly large modality difference between action data captured by wearable-sensor and vision-sensor in data dimension, data distribution and inherent information content. In this paper, we propose a novel framework, named Semantics-aware Adaptive Knowledge Distillation Networks (SAKDN), to enhance action recognition in vision-sensor modality (videos) by adaptively transferring and distilling the knowledge from multiple wearable sensors. The SAKDN uses multiple wearable-sensors as teacher modalities and uses RGB videos as student modality. To preserve local temporal relationship and facilitate employing visual deep learning model, we transform one-dimensional time-series signals of wearable sensors to two-dimensional images by designing a gramian angular field based virtual image generation model. Then, we build a novel Similarity-Preserving Adaptive Multi-modal Fusion Module to adaptively fuse intermediate representation knowledge from different teacher networks. Finally, to fully exploit and transfer the knowledge of multiple well-trained teacher networks to the student network, we propose a novel Graph-guided Semantically Discriminative Mapping loss, which utilizes graph-guided ablation analysis to produce a good visual explanation highlighting the important regions across modalities and concurrently preserving the interrelations of original data. Experimental results on Berkeley-MHAD, UTD-MHAD and MMAct datasets well demonstrate the effectiveness of our proposed SAKDN.

## 核心内容
Existing vision-based action recognition is susceptible to occlusion and appearance variations, while wearable sensors can alleviate these challenges by capturing human motion with one-dimensional time-series signal. For the same action, the knowledge learned from vision sensors and wearable sensors, may be related and complementary. However, there exists significantly large modality difference between action data captured by wearable-sensor and vision-sensor in data dimension, data distribution and inherent information content. In this paper, we propose a novel framework, named Semantics-aware Adaptive Knowledge Distillation Networks (SAKDN), to enhance action recognition in vision-sensor modality (videos) by adaptively transferring and distilling the knowledge from multiple wearable sensors. The SAKDN uses multiple wearable-sensors as teacher modalities and uses RGB videos as student modality. To preserve local temporal relationship and facilitate employing visual deep learning model, we transform one-dimensional time-series signals of wearable sensors to two-dimensional images by designing a gramian angular field based virtual image generation model. Then, we build a novel Similarity-Preserving Adaptive Multi-modal Fusion Module to adaptively fuse intermediate representation knowledge from different teacher networks. Finally, to fully exploit and transfer the knowledge of multiple well-trained teacher networks to the student network, we propose a novel Graph-guided Semantically Discriminative Mapping loss, which utilizes graph-guided ablation analysis to produce a good visual explanation highlighting the important regions across modalities and concurrently preserving the interrelations of original data. Experimental results on Berkeley-MHAD, UTD-MHAD and MMAct datasets well demonstrate the effectiveness of our proposed SAKDN.

## 参考
- http://arxiv.org/abs/2009.00210v5

## Overview
Existing vision-based action recognition is susceptible to occlusion and appearance variations, while wearable sensors can alleviate these challenges by capturing human motion with one-dimensional time-series signals. For the same action, the knowledge learned from vision sensors and wearable sensors may be related and complementary. However, there exists a significantly large modality difference between action data captured by wearable sensors and vision sensors in terms of data dimension, data distribution, and inherent information content. In this paper, we propose a novel framework, named Semantics-aware Adaptive Knowledge Distillation Networks (SAKDN), to enhance action recognition in the vision-sensor modality (videos) by adaptively transferring and distilling knowledge from multiple wearable sensors. SAKDN uses multiple wearable sensors as teacher modalities and RGB videos as the student modality. To preserve local temporal relationships and facilitate the use of visual deep learning models, we transform one-dimensional time-series signals from wearable sensors into two-dimensional images by designing a Gramian Angular Field-based virtual image generation model. Then, we build a novel Similarity-Preserving Adaptive Multi-modal Fusion Module to adaptively fuse intermediate representation knowledge from different teacher networks. Finally, to fully exploit and transfer the knowledge of multiple well-trained teacher networks to the student network, we propose a novel Graph-guided Semantically Discriminative Mapping loss, which utilizes graph-guided ablation analysis to produce a good visual explanation highlighting important regions across modalities while preserving the interrelations of the original data. Experimental results on the Berkeley-MHAD, UTD-MHAD, and MMAct datasets well demonstrate the effectiveness of our proposed SAKDN.

## Content
Existing vision-based action recognition is susceptible to occlusion and appearance variations, while wearable sensors can alleviate these challenges by capturing human motion with one-dimensional time-series signals. For the same action, the knowledge learned from vision sensors and wearable sensors may be related and complementary. However, there exists a significantly large modality difference between action data captured by wearable sensors and vision sensors in terms of data dimension, data distribution, and inherent information content. In this paper, we propose a novel framework, named Semantics-aware Adaptive Knowledge Distillation Networks (SAKDN), to enhance action recognition in the vision-sensor modality (videos) by adaptively transferring and distilling knowledge from multiple wearable sensors. SAKDN uses multiple wearable sensors as teacher modalities and RGB videos as the student modality. To preserve local temporal relationships and facilitate the use of visual deep learning models, we transform one-dimensional time-series signals from wearable sensors into two-dimensional images by designing a Gramian Angular Field-based virtual image generation model. Then, we build a novel Similarity-Preserving Adaptive Multi-modal Fusion Module to adaptively fuse intermediate representation knowledge from different teacher networks. Finally, to fully exploit and transfer the knowledge of multiple well-trained teacher networks to the student network, we propose a novel Graph-guided Semantically Discriminative Mapping loss, which utilizes graph-guided ablation analysis to produce a good visual explanation highlighting important regions across modalities while preserving the interrelations of the original data. Experimental results on the Berkeley-MHAD, UTD-MHAD, and MMAct datasets well demonstrate the effectiveness of our proposed SAKDN.

## 개요
기존의 비전 기반 동작 인식은 폐색 및 외형 변화에 취약한 반면, 웨어러블 센서는 1차원 시계열 신호로 인간의 움직임을 포착하여 이러한 문제를 완화할 수 있습니다. 동일한 동작에 대해 비전 센서와 웨어러블 센서로부터 학습된 지식은 서로 연관되고 상호 보완적일 수 있습니다. 그러나 웨어러블 센서와 비전 센서로 포착된 동작 데이터 간에는 데이터 차원, 데이터 분포 및 내재된 정보 내용에서 상당히 큰 모달리티 차이가 존재합니다. 본 논문에서는 여러 웨어러블 센서의 지식을 적응적으로 전이 및 증류하여 비전 센서 모달리티(비디오)에서의 동작 인식을 향상시키는 새로운 프레임워크인 의미 인식 적응형 지식 증류 네트워크(SAKDN)를 제안합니다. SAKDN은 여러 웨어러블 센서를 교사 모달리티로 사용하고 RGB 비디오를 학생 모달리티로 사용합니다. 국소적 시간 관계를 보존하고 시각적 딥러닝 모델 적용을 용이하게 하기 위해, 그라미안 각도 필드 기반 가상 이미지 생성 모델을 설계하여 웨어러블 센서의 1차원 시계열 신호를 2차원 이미지로 변환합니다. 그런 다음, 새로운 유사성 보존 적응형 다중 모달 융합 모듈을 구축하여 서로 다른 교사 네트워크의 중간 표현 지식을 적응적으로 융합합니다. 마지막으로, 여러 잘 훈련된 교사 네트워크의 지식을 학생 네트워크로 완전히 활용 및 전이하기 위해, 그래프 기반 절제 분석을 활용하여 모달리티 간 중요한 영역을 강조하고 원본 데이터의 상호 관계를 동시에 보존하는 좋은 시각적 설명을 생성하는 새로운 그래프 유도 의미 판별 매핑 손실을 제안합니다. Berkeley-MHAD, UTD-MHAD 및 MMAct 데이터셋에 대한 실험 결과는 제안된 SAKDN의 효과성을 잘 입증합니다.

## 핵심 내용
기존의 비전 기반 동작 인식은 폐색 및 외형 변화에 취약한 반면, 웨어러블 센서는 1차원 시계열 신호로 인간의 움직임을 포착하여 이러한 문제를 완화할 수 있습니다. 동일한 동작에 대해 비전 센서와 웨어러블 센서로부터 학습된 지식은 서로 연관되고 상호 보완적일 수 있습니다. 그러나 웨어러블 센서와 비전 센서로 포착된 동작 데이터 간에는 데이터 차원, 데이터 분포 및 내재된 정보 내용에서 상당히 큰 모달리티 차이가 존재합니다. 본 논문에서는 여러 웨어러블 센서의 지식을 적응적으로 전이 및 증류하여 비전 센서 모달리티(비디오)에서의 동작 인식을 향상시키는 새로운 프레임워크인 의미 인식 적응형 지식 증류 네트워크(SAKDN)를 제안합니다. SAKDN은 여러 웨어러블 센서를 교사 모달리티로 사용하고 RGB 비디오를 학생 모달리티로 사용합니다. 국소적 시간 관계를 보존하고 시각적 딥러닝 모델 적용을 용이하게 하기 위해, 그라미안 각도 필드 기반 가상 이미지 생성 모델을 설계하여 웨어러블 센서의 1차원 시계열 신호를 2차원 이미지로 변환합니다. 그런 다음, 새로운 유사성 보존 적응형 다중 모달 융합 모듈을 구축하여 서로 다른 교사 네트워크의 중간 표현 지식을 적응적으로 융합합니다. 마지막으로, 여러 잘 훈련된 교사 네트워크의 지식을 학생 네트워크로 완전히 활용 및 전이하기 위해, 그래프 기반 절제 분석을 활용하여 모달리티 간 중요한 영역을 강조하고 원본 데이터의 상호 관계를 동시에 보존하는 좋은 시각적 설명을 생성하는 새로운 그래프 유도 의미 판별 매핑 손실을 제안합니다. Berkeley-MHAD, UTD-MHAD 및 MMAct 데이터셋에 대한 실험 결과는 제안된 SAKDN의 효과성을 잘 입증합니다.
