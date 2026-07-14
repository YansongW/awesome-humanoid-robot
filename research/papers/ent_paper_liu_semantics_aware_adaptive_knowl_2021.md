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

