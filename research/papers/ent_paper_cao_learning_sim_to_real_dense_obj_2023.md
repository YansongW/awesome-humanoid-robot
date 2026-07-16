---
$id: ent_paper_cao_learning_sim_to_real_dense_obj_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Sim-to-Real Dense Object Descriptors for Robotic Manipulation
  zh: 面向机器人操作的仿真到现实稠密物体描述符学习
  ko: 로봇 조작을 위한 시뮬레이션-현실 밀집 객체 기술자 학습
summary:
  en: This paper proposes Sim-to-Real Dense Object Nets (SRDONs), a dense object descriptor representation that unifies simulated
    and real visual data in a shared feature space with pixel-wise consistency, enabling zero real-world training transfer
    for robotic manipulation tasks.
  zh: 本文提出仿真到现实稠密物体网络（SRDONs），一种将仿真与真实视觉数据映射到具有像素级一致性的统一特征空间的稠密物体描述符表示，使机器人操作任务能够在零真实世界训练的情况下实现迁移。
  ko: 본 논문은 시뮬레이션과 실제 시각 데이터를 픽셀 수준의 일관성을 가진 공유 특징 공간으로 통합하는 밀집 객체 기술자 표현인 SRDONs(Sim-to-Real Dense Object Nets)를 제안하여, 로봇
    조작 작업에서 실제 세계 훈련 없이 전이가 가능하도록 한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- dense_object_descriptors
- vision_based_manipulation
- contrastive_learning
- domain_adaptation
- rgb_d_perception
- zero_shot_transfer
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.08703v1.
sources:
- id: src_001
  type: paper
  title: Learning Sim-to-Real Dense Object Descriptors for Robotic Manipulation
  url: https://arxiv.org/abs/2304.08703
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
It is crucial to address the following issues for ubiquitous robotics manipulation applications: (a) vision-based manipulation tasks require the robot to visually learn and understand the object with rich information like dense object descriptors; and (b) sim-to-real transfer in robotics aims to close the gap between simulated and real data. In this paper, we present Sim-to-Real Dense Object Nets (SRDONs), a dense object descriptor that not only understands the object via appropriate representation but also maps simulated and real data to a unified feature space with pixel consistency. We proposed an object-to-object matching method for image pairs from different scenes and different domains. This method helps reduce the effort of training data from real-world by taking advantage of public datasets, such as GraspNet. With sim-to-real object representation consistency, our SRDONs can serve as a building block for a variety of sim-to-real manipulation tasks. We demonstrate in experiments that pre-trained SRDONs significantly improve performances on unseen objects and unseen visual environments for various robotic tasks with zero real-world training.

## 核心内容
It is crucial to address the following issues for ubiquitous robotics manipulation applications: (a) vision-based manipulation tasks require the robot to visually learn and understand the object with rich information like dense object descriptors; and (b) sim-to-real transfer in robotics aims to close the gap between simulated and real data. In this paper, we present Sim-to-Real Dense Object Nets (SRDONs), a dense object descriptor that not only understands the object via appropriate representation but also maps simulated and real data to a unified feature space with pixel consistency. We proposed an object-to-object matching method for image pairs from different scenes and different domains. This method helps reduce the effort of training data from real-world by taking advantage of public datasets, such as GraspNet. With sim-to-real object representation consistency, our SRDONs can serve as a building block for a variety of sim-to-real manipulation tasks. We demonstrate in experiments that pre-trained SRDONs significantly improve performances on unseen objects and unseen visual environments for various robotic tasks with zero real-world training.

## 参考
- http://arxiv.org/abs/2304.08703v1

## Overview
It is crucial to address the following issues for ubiquitous robotics manipulation applications: (a) vision-based manipulation tasks require the robot to visually learn and understand the object with rich information like dense object descriptors; and (b) sim-to-real transfer in robotics aims to close the gap between simulated and real data. In this paper, we present Sim-to-Real Dense Object Nets (SRDONs), a dense object descriptor that not only understands the object via appropriate representation but also maps simulated and real data to a unified feature space with pixel consistency. We proposed an object-to-object matching method for image pairs from different scenes and different domains. This method helps reduce the effort of training data from real-world by taking advantage of public datasets, such as GraspNet. With sim-to-real object representation consistency, our SRDONs can serve as a building block for a variety of sim-to-real manipulation tasks. We demonstrate in experiments that pre-trained SRDONs significantly improve performances on unseen objects and unseen visual environments for various robotic tasks with zero real-world training.

## Content
It is crucial to address the following issues for ubiquitous robotics manipulation applications: (a) vision-based manipulation tasks require the robot to visually learn and understand the object with rich information like dense object descriptors; and (b) sim-to-real transfer in robotics aims to close the gap between simulated and real data. In this paper, we present Sim-to-Real Dense Object Nets (SRDONs), a dense object descriptor that not only understands the object via appropriate representation but also maps simulated and real data to a unified feature space with pixel consistency. We proposed an object-to-object matching method for image pairs from different scenes and different domains. This method helps reduce the effort of training data from real-world by taking advantage of public datasets, such as GraspNet. With sim-to-real object representation consistency, our SRDONs can serve as a building block for a variety of sim-to-real manipulation tasks. We demonstrate in experiments that pre-trained SRDONs significantly improve performances on unseen objects and unseen visual environments for various robotic tasks with zero real-world training.

## 개요
범용 로봇 조작 애플리케이션에서 다음 문제를 해결하는 것이 중요합니다: (a) 시각 기반 조작 작업은 로봇이 밀집 객체 디스크립터(dense object descriptors)와 같은 풍부한 정보를 통해 객체를 시각적으로 학습하고 이해해야 하며; (b) 로봇공학에서의 시뮬레이션-실제 전환(sim-to-real transfer)은 시뮬레이션 데이터와 실제 데이터 간의 차이를 줄이는 것을 목표로 합니다. 본 논문에서는 Sim-to-Real Dense Object Nets (SRDONs)을 제시합니다. 이는 적절한 표현을 통해 객체를 이해할 뿐만 아니라 시뮬레이션 및 실제 데이터를 픽셀 일관성을 가진 통합 특징 공간으로 매핑하는 밀집 객체 디스크립터입니다. 우리는 서로 다른 장면과 서로 다른 도메인의 이미지 쌍을 위한 객체 간 매칭 방법을 제안했습니다. 이 방법은 GraspNet과 같은 공개 데이터셋을 활용하여 실제 세계에서의 훈련 데이터 노력을 줄이는 데 도움을 줍니다. 시뮬레이션-실제 객체 표현 일관성을 통해 SRDONs는 다양한 시뮬레이션-실제 조작 작업을 위한 기본 구성 요소로 사용될 수 있습니다. 실험을 통해 사전 훈련된 SRDONs가 실제 세계 훈련 없이 다양한 로봇 작업에서 보이지 않는 객체와 보이지 않는 시각적 환경에 대한 성능을 크게 향상시킴을 입증했습니다.

## 핵심 내용
범용 로봇 조작 애플리케이션에서 다음 문제를 해결하는 것이 중요합니다: (a) 시각 기반 조작 작업은 로봇이 밀집 객체 디스크립터(dense object descriptors)와 같은 풍부한 정보를 통해 객체를 시각적으로 학습하고 이해해야 하며; (b) 로봇공학에서의 시뮬레이션-실제 전환(sim-to-real transfer)은 시뮬레이션 데이터와 실제 데이터 간의 차이를 줄이는 것을 목표로 합니다. 본 논문에서는 Sim-to-Real Dense Object Nets (SRDONs)을 제시합니다. 이는 적절한 표현을 통해 객체를 이해할 뿐만 아니라 시뮬레이션 및 실제 데이터를 픽셀 일관성을 가진 통합 특징 공간으로 매핑하는 밀집 객체 디스크립터입니다. 우리는 서로 다른 장면과 서로 다른 도메인의 이미지 쌍을 위한 객체 간 매칭 방법을 제안했습니다. 이 방법은 GraspNet과 같은 공개 데이터셋을 활용하여 실제 세계에서의 훈련 데이터 노력을 줄이는 데 도움을 줍니다. 시뮬레이션-실제 객체 표현 일관성을 통해 SRDONs는 다양한 시뮬레이션-실제 조작 작업을 위한 기본 구성 요소로 사용될 수 있습니다. 실험을 통해 사전 훈련된 SRDONs가 실제 세계 훈련 없이 다양한 로봇 작업에서 보이지 않는 객체와 보이지 않는 시각적 환경에 대한 성능을 크게 향상시킴을 입증했습니다.
