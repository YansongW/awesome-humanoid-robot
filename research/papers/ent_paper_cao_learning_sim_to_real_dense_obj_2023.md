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
  en: This paper proposes Sim-to-Real Dense Object Nets (SRDONs), a dense object descriptor
    representation that unifies simulated and real visual data in a shared feature
    space with pixel-wise consistency, enabling zero real-world training transfer
    for robotic manipulation tasks.
  zh: 本文提出仿真到现实稠密物体网络（SRDONs），一种将仿真与真实视觉数据映射到具有像素级一致性的统一特征空间的稠密物体描述符表示，使机器人操作任务能够在零真实世界训练的情况下实现迁移。
  ko: 본 논문은 시뮬레이션과 실제 시각 데이터를 픽셀 수준의 일관성을 가진 공유 특징 공간으로 통합하는 밀집 객체 기술자 표현인 SRDONs(Sim-to-Real
    Dense Object Nets)를 제안하여, 로봇 조작 작업에서 실제 세계 훈련 없이 전이가 가능하도록 한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    of section-level citations and exact experimental details is pending human review.
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

## Overview

Vision-based robotic manipulation requires the robot to learn rich, dense representations of objects that can generalize across visual conditions and deployment domains. This paper introduces Sim-to-Real Dense Object Nets (SRDONs), a dense object descriptor representation that maps simulated and real images into a unified feature space while preserving pixel-wise consistency. The approach leverages known object poses and 3D meshes to synthesize correspondence supervision across scenes and domains, then trains a descriptor network with a contrastive objective over Sim-Sim, Real-Real, and Sim-Real image pairs.

The core training strategy is an object-to-object matching method that pairs images of the same object from different scenes and different domains. By matching objects rather than whole scenes, the method can exploit existing public datasets such as GraspNet and GraspNet-1Billion to supplement synthetic V-REP data, reducing the amount of real-world annotation required. The resulting descriptors are designed to support downstream manipulation tasks without additional real-world training.

The authors evaluate SRDONs on grasping and cluttered-object picking with unseen objects and unseen visual environments. Pre-trained SRDONs are reported to significantly improve generalization under zero real-world training, demonstrating the value of sim-to-real consistent object descriptors as a reusable perception primitive.

## Key Contributions

- Introduce SRDONs, a dense object descriptor representation that enforces sim-to-real consistency and generalizes to unseen objects and visual environments.
- Propose an object-to-object matching method for image pairs from different scenes and domains, reducing reliance on real-world data by leveraging public datasets such as GraspNet.
- Demonstrate zero real-world training sim-to-real transfer for grasping and cluttered-object picking tasks.

## Relevance to Humanoid Robotics

Humanoid robots operating in unstructured human environments must perceive and manipulate a wide variety of objects without task-specific retraining. Dense object descriptors such as SRDONs provide a foundational perception building block that can represent object geometry and appearance in a domain-invariant way, enabling skills like grasping and object retrieval to transfer from simulation to the real world. Because the method reduces dependence on costly real-world data collection, it is particularly relevant for scaling humanoid manipulation capabilities across diverse scenes and objects.
