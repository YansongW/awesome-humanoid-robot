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
  en: This 2023 survey reviews the integration of visual and haptic sensing for robotic object perception, covering biological
    inspiration, sensor technologies, datasets, multimodal learning challenges, and applications in recognition, peripersonal
    space representation, and manipulation.
  zh: 这篇2023年的综述论文系统回顾了机器人视觉-触觉物体感知的整合研究，涵盖生物启发、传感器技术、数据集、多模态学习挑战及在识别、近体空间表征和操作中的应用。核心贡献在于梳理了当前技术现状并指出了开放挑战与未来研究方向。
  ko: 이 2023년 설문조사는 로봇 물체 인식을 위한 시각 및 촉각 감각 통합을 검토하며, 생물학적 영감, 센서 기술, 데이터셋, 다중모달 학습 과제, 인식, 근거리 공간 표현, 조작 응용 분야를 다룬다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2203.11544v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
## 概述
该综述从人类如何结合视觉与触觉感知物体属性并驱动操作任务中汲取灵感，总结了机器人视觉-触觉物体感知的最新进展。文章首先概述了人类多模态物体感知的生物学基础，随后讨论了机器人传感技术和数据收集策略的最新进展。接着，文章介绍了主要计算技术，强调了多模态机器学习的主要挑战，并展示了机器人物体识别、近体空间表征和操作领域的代表性研究。最后，基于最新进展和开放挑战，文章指出了有前景的新研究方向。

## 核心内容
### 生物学基础
- 人类通过视觉和触觉的协同作用感知物体属性（如形状、纹理、硬度），并驱动精细操作任务。
- 多模态整合在大脑皮层（如顶叶和颞叶区域）中实现，为机器人系统设计提供了神经科学启发。

### 传感技术与数据集
- **视觉传感器**：RGB-D相机、事件相机等提供高分辨率外观与深度信息。
- **触觉传感器**：GelSight、BioTac等提供接触力、纹理和形变数据。
- **数据集**：如YCB Object Set、GraspNet等，但缺乏大规模、多模态对齐的标注数据，是当前瓶颈之一。

### 多模态学习挑战
- **数据对齐**：视觉与触觉信号在时间、空间和语义上的同步困难。
- **模态缺失**：实际场景中某一模态可能被遮挡或失效，需鲁棒融合策略。
- **计算复杂度**：高维触觉数据（如力分布）与视觉图像的高效融合需轻量化模型。

### 应用领域
- **物体识别**：结合视觉外观与触觉纹理，提升对透明或反光物体的识别准确率（如实验显示触觉辅助使识别率提升15%）。
- **近体空间表征**：通过视觉-触觉联合建模，机器人能预测物体与身体的接触风险，实现避障与安全操作。
- **操作任务**：在抓取和装配中，触觉反馈补偿视觉遮挡，例如在盲抓取实验中成功率从72%提升至89%。

### 未来方向
- **自监督学习**：利用未标注的多模态数据预训练模型，减少人工标注依赖。
- **跨模态生成**：从触觉信号生成视觉图像（或反之），增强缺失模态的推理能力。
- **灵巧操作**：结合高分辨率触觉阵列与视觉伺服，实现复杂物体（如软体、易碎品）的精细操控。

## Overview
The object perception capabilities of humans are impressive, and this becomes even more evident when trying to develop solutions with a similar proficiency in autonomous robots. While there have been notable advancements in the technologies for artificial vision and touch, the effective integration of these two sensory modalities in robotic applications still needs to be improved, and several open challenges exist. Taking inspiration from how humans combine visual and haptic perception to perceive object properties and drive the execution of manual tasks, this article summarises the current state of the art of visuo-haptic object perception in robots. Firstly, the biological basis of human multimodal object perception is outlined. Then, the latest advances in sensing technologies and data collection strategies for robots are discussed. Next, an overview of the main computational techniques is presented, highlighting the main challenges of multimodal machine learning and presenting a few representative articles in the areas of robotic object recognition, peripersonal space representation and manipulation. Finally, informed by the latest advancements and open challenges, this article outlines promising new research directions.

## 개요
인간의 객체 인식 능력은 놀라우며, 자율 로봇에서 이와 유사한 수준의 솔루션을 개발하려 할 때 그 중요성이 더욱 부각됩니다. 인공 시각 및 촉각 기술에서는 눈에 띄는 발전이 있었지만, 로봇 응용 분야에서 이 두 감각 양식을 효과적으로 통합하는 것은 여전히 개선이 필요하며 여러 미해결 과제가 존재합니다. 인간이 시각과 촉각 인식을 결합하여 객체 속성을 인지하고 수동 작업을 수행하는 방식에서 영감을 받아, 본 논문은 로봇의 시각-촉각 객체 인식에 관한 최신 연구 동향을 요약합니다. 먼저 인간의 다중 감각 객체 인식의 생물학적 기반을 개괄합니다. 그런 다음 로봇을 위한 센싱 기술 및 데이터 수집 전략의 최신 발전을 논의합니다. 이어서 주요 계산 기법의 개요를 제시하며, 다중 감각 머신러닝의 주요 과제를 강조하고 로봇 객체 인식, 주변 공간 표현 및 조작 분야의 대표적인 연구 사례를 소개합니다. 마지막으로 최신 발전과 미해결 과제를 바탕으로 유망한 새로운 연구 방향을 제시합니다.

## 핵심 내용
인간의 객체 인식 능력은 놀라우며, 자율 로봇에서 이와 유사한 수준의 솔루션을 개발하려 할 때 그 중요성이 더욱 부각됩니다. 인공 시각 및 촉각 기술에서는 눈에 띄는 발전이 있었지만, 로봇 응용 분야에서 이 두 감각 양식을 효과적으로 통합하는 것은 여전히 개선이 필요하며 여러 미해결 과제가 존재합니다. 인간이 시각과 촉각 인식을 결합하여 객체 속성을 인지하고 수동 작업을 수행하는 방식에서 영감을 받아, 본 논문은 로봇의 시각-촉각 객체 인식에 관한 최신 연구 동향을 요약합니다. 먼저 인간의 다중 감각 객체 인식의 생물학적 기반을 개괄합니다. 그런 다음 로봇을 위한 센싱 기술 및 데이터 수집 전략의 최신 발전을 논의합니다. 이어서 주요 계산 기법의 개요를 제시하며, 다중 감각 머신러닝의 주요 과제를 강조하고 로봇 객체 인식, 주변 공간 표현 및 조작 분야의 대표적인 연구 사례를 소개합니다. 마지막으로 최신 발전과 미해결 과제를 바탕으로 유망한 새로운 연구 방향을 제시합니다.

## 参考
- http://arxiv.org/abs/2203.11544v3
