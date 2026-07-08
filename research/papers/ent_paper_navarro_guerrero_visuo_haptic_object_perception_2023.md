---
$id: ent_paper_navarro_guerrero_visuo_haptic_object_perception_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Visuo-Haptic Object Perception for Robots: An Overview'
  zh: 机器人视触觉物体感知综述
  ko: 로봇을 위한 시각-촉각 물체 인식 개요
summary:
  en: This 2023 survey reviews the integration of visual and haptic sensing for robotic
    object perception, covering biological inspiration, sensor technologies, datasets,
    multimodal learning challenges, and applications in recognition, peripersonal
    space representation, and manipulation.
  zh: 本2023年综述回顾了机器人物体感知中视觉与触觉感知的整合，涵盖生物学启发、传感器技术、数据集、多模态学习挑战以及在识别、近体空间表示和抓取操作中的应用。
  ko: 이 2023년 설문조사는 로봇 물체 인식을 위한 시각 및 촉각 감각 통합을 검토하며, 생물학적 영감, 센서 기술, 데이터셋, 다중모달 학습
    과제, 인식, 근거리 공간 표현, 조작 응용 분야를 다룬다.
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
- visuo_haptic_perception
- multimodal_learning
- tactile_sensing
- object_recognition
- manipulation
- robot_perception
- sensor_fusion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; requires human review against
    full text before verification.
sources:
- id: src_001
  type: paper
  title: 'Visuo-Haptic Object Perception for Robots: An Overview'
  url: https://arxiv.org/abs/2203.11544
  date: '2023'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

This paper is a 2023 survey of visuo-haptic object perception for robots, authored by Navarro-Guerrero, Toprak, Josifovski, and Jamone, and published on arXiv (arXiv:2203.11544). It begins by outlining the biological and neural basis of human multimodal object perception, providing inspiration for artificial systems. The survey then covers tactile and visual sensing technologies, including commercial sensors, and discusses datasets and data-collection strategies used to gather paired visual and haptic data for robotic learning. The authors identify open challenges in integrating artificial vision and touch, noting that tactile sensing still lags behind vision in robustness, affordability, and ease of integration.

The core technical review presents multimodal machine learning challenges organized around representation, translation, alignment, fusion, and co-learning. The authors highlight representative work in robotic object recognition, peripersonal space representation, and manipulation. They observe that vision-only grasping remains more common in practice due to greater sensor maturity and simulation availability, while large-scale visuo-haptic datasets remain scarce because real-world tactile data collection is resource-intensive and robot-dependent. The paper concludes by outlining promising research directions informed by these advances and gaps.

The survey is explicitly positioned as holistic rather than exhaustive, bridging biological and technical perspectives on visuo-haptic perception. Its scope spans sensing hardware, datasets, learning methods, and applications, making it a broad reference for researchers working on multimodal robot perception.

## Key Contributions

- Outlines the biological and neural basis of human visuo-haptic object perception.
- Reviews tactile and visual sensing technologies and commercial sensor solutions.
- Surveys multimodal datasets and data collection strategies for robotic perception.
- Discusses core multimodal machine learning challenges: representation, translation, alignment, fusion, and co-learning.
- Reviews applications in robotic object recognition, peripersonal space representation, and manipulation.

## Relevance to Humanoid Robotics

Visuo-haptic perception is essential for humanoid robot deployment because robust grasping, manipulation, and object recognition under visual uncertainty are core requirements for assembly, service, and human-robot collaboration tasks. By integrating touch with vision, humanoids can compensate for occlusion, poor lighting, and unknown object properties, improving reliability in unstructured environments.

The paper's coverage of tactile sensors, multimodal datasets, and fusion methods directly supports the design of perception systems for humanoid end-effectors. Its discussion of peripersonal space representation is also relevant to safe and reactive humanoid behavior near people and obstacles.
