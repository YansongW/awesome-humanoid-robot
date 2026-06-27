---
$id: ent_paper_ribeiro_real_time_deep_learning_approa_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Real-Time Deep Learning Approach to Visual Servo Control and Grasp Detection
    for Autonomous Robotic Manipulation
  zh: 面向自主机器人操作的视觉伺服控制与抓取检测的实时深度学习方法
  ko: 자율 로봇 매니퓰레이션을 위한 시각 서보 제어 및 그래스프 감지의 실시간 딥러닝 접근법
summary:
  en: 'Proposes two lightweight CNNs for robotic manipulation: one predicts a five-dimensional
    grasp rectangle from a single RGB image using the Cornell Grasping Dataset, and
    a second, learned-from-scratch network regresses camera velocities for visual
    servoing from reference and current image pairs using a self-collected Kinova
    Gen3 dataset, enabling real-time dynamic grasping of novel objects.'
  zh: 提出两个轻量级卷积神经网络用于机器人操作：一个基于Cornell抓取数据集从单张RGB图像预测五维抓取矩形，另一个基于自采集的Kinova Gen3数据集从参考图像与当前图像对回归相机速度以实现视觉伺服，从而实现对未知物体的实时动态抓取。
  ko: '로봇 매니퓰레이션을 위한 두 개의 경량 CNN을 제안한다: 하나는 Cornell Grasping Dataset을 사용하여 단일 RGB
    이미지로부터 5차원 그래스프 사각형을 예측하고, 다른 하나는 자체 수집한 Kinova Gen3 데이터셋을 사용하여 참조 이미지와 현재 이미지
    쌍으로부터 카메라 속도를 회귀하여 시각 서보를 수행함으로써 새로운 객체에 대한 실시간 동적 그래스핑을 가능하게 한다.'
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
- visual_servoing
- grasp_detection
- convolutional_neural_network
- real_time
- robotic_manipulation
- kinova_gen3
- cornell_grasping_dataset
- visual_perception
- autonomous_grasping
- deep_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from abstract and metadata; requires human review of full text
    before verification.
sources:
- id: src_001
  type: paper
  title: Real-Time Deep Learning Approach to Visual Servo Control and Grasp Detection
    for Autonomous Robotic Manipulation
  url: https://arxiv.org/abs/2010.06544
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper addresses the visual perception and control pipeline required for autonomous robotic grasping in unstructured and dynamic environments. It develops a lightweight convolutional neural network trained on the Cornell Grasping Dataset that, given a single RGB image of a robot workspace, predicts a five-dimensional grasp rectangle representing the position, orientation, and opening of parallel grippers immediately before closing. The network is designed for real-time execution and integrates into a physical robotic system.

To handle object motion, the authors introduce a second convolutional network for visual servo control. This network is trained from scratch using a self-collected dataset generated automatically by a Kinova Gen3 7-DoF manipulator. It takes a reference image and a current image as input and regresses proportional linear and angular camera velocities to keep the target object within the field of view processed by the grasp network. The combined system enables closed-loop dynamic grasping of previously unseen objects.

## Key Contributions

- Survey of CGD-based grasp detection, learned visual servoing, and dynamic/reactive grasping.
- Lightweight CNN for real-time grasp rectangle prediction with state-of-the-art speed on the Cornell Grasping Dataset.
- Four CNN architectures evaluated for end-to-end visual servo control using only reference and current RGB images.
- Large publicly available visual servoing dataset collected with a Kinova Gen3 7-DoF manipulator.
- Integrated real-time system demonstrating dynamic grasping of novel objects with an 85.7% success rate.

## Relevance to Humanoid Robotics

Real-time, learning-based grasp detection and visual servoing are core perceptual-control capabilities for humanoid robots that must manipulate objects in unstructured, dynamic environments without relying on object-specific models or depth sensors. The paper's emphasis on lightweight CNNs and millimeter-level accuracy with a controller learned from scratch supports reliable real-world deployment at scale, which is directly transferable to humanoid manipulation scenarios.
