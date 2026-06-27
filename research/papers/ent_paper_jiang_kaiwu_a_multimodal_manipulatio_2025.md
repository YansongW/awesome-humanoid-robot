---
$id: ent_paper_jiang_kaiwu_a_multimodal_manipulatio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Kaiwu: A Multimodal Manipulation Dataset and Framework for Robot Learning and
    Human-Robot Interaction'
  zh: Kaiwu：用于机器人学习与人和机器人交互的多模态操作数据集与框架
  ko: 'Kaiwu: 로봇 학습 및 인간-로봇 상호작용을 위한 다중감각 조작 데이터셋과 프레임워크'
summary:
  en: Kaiwu is a large-scale, real-world multimodal manipulation dataset and collection
    framework for industrial assembly, providing synchronized vision, force, sound,
    gaze, EMG, and motion-capture recordings with fine-grained spatio-temporal annotations
    for robot learning and human-robot interaction research.
  zh: Kaiwu是一个面向工业装配的大规模真实世界多模态操作数据集与采集框架，提供同步视觉、力觉、声音、注视、肌电和运动捕捉记录，并带有细粒度时空标注，以支持机器人学习和人机交互研究。
  ko: Kaiwu는 산업 조립을 위한 대규모 실제 다중감각 조작 데이터셋 및 수집 프레임워크로, 로봇 학습과 인간-로봇 상호작용 연구를 위해 시각,
    힘, 소리, 시선, 근전도 및 모션 캡처 기록을 동기화하여 세밀한 시공간 주석과 함께 제공한다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- multimodal_dataset
- imitation_learning
- human_robot_interaction
- assembly
- motion_capture
- emg
- eye_tracking
- robot_learning
- fine_grained_annotation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    still pending.
sources:
- id: src_001
  type: paper
  title: 'Kaiwu: A Multimodal Manipulation Dataset and Framework for Robot Learning
    and Human-Robot Interaction'
  url: https://arxiv.org/abs/2503.05231
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Kaiwu addresses the shortage of synchronized real-world multimodal data for complex assembly tasks by introducing a multimodal data collection framework and a large-scale dataset. The framework integrates wearable and environment-mounted sensors—data gloves with angle/pressure sensing, EMG sensors, ACC/IMU, RGB-D cameras, an eye tracker, microphones, and a 3D motion-capture system—to capture human, environment, and robot information simultaneously. Twenty subjects performed assembly tasks with 30 interaction objects, producing 11,664 integrated action instances.

For each demonstration, the dataset records hand motion, operation pressure, assembly sounds, multi-view video, high-precision motion capture, first-person video with eye gaze, and electromyography signals. Data are aligned via absolute timestamps and annotated with fine-grained multi-level labels, including regions of interest and semantic segmentation. The authors release the data with APIs, documentation, and a structured directory layout to support robot learning, dexterous manipulation, human intention understanding, and human-robot collaboration research.

## Key Contributions

- A multimodal data collection framework with full situational awareness, including manipulation dynamics, neural signals, gaze, and multi-view vision.
- A large-scale, high-quality multimodal dataset for long-horizon autonomy using ground-truth motion capture.
- Fine-grained cross-modal annotations: regions of interest, semantic segmentation, action/gesture segmentation, and gesture classification.
- Open-source data release with APIs, documentation, and a structured directory layout.

## Relevance to Humanoid Robotics

The Kaiwu dataset captures synchronized multimodal human demonstration data—including dynamics, gaze, EMG, and motion capture—that can directly fuel imitation learning and skill transfer for humanoid robot manipulation and assembly. By providing ground-truth motion and force data alongside visual and physiological signals, it supports the development of policies and models that translate human assembly skills into humanoid robot behaviors in real-world industrial settings.
