---
$id: ent_paper_jiang_kaiwu_a_multimodal_manipulatio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Kaiwu: A Multimodal Manipulation Dataset and Framework for Robot Learning and Human-Robot Interaction'
  zh: Kaiwu：用于机器人学习与人和机器人交互的多模态操作数据集与框架
  ko: 'Kaiwu: 로봇 학습 및 인간-로봇 상호작용을 위한 다중감각 조작 데이터셋과 프레임워크'
summary:
  en: Kaiwu is a large-scale, real-world multimodal manipulation dataset and collection framework for industrial assembly,
    providing synchronized vision, force, sound, gaze, EMG, and motion-capture recordings with fine-grained spatio-temporal
    annotations for robot learning and human-robot interaction research.
  zh: Kaiwu是一个面向工业装配的大规模真实世界多模态操作数据集与采集框架，提供同步视觉、力觉、声音、注视、肌电和运动捕捉记录，并带有细粒度时空标注，以支持机器人学习和人机交互研究。
  ko: Kaiwu는 산업 조립을 위한 대규모 실제 다중감각 조작 데이터셋 및 수집 프레임워크로, 로봇 학습과 인간-로봇 상호작용 연구를 위해 시각, 힘, 소리, 시선, 근전도 및 모션 캡처 기록을 동기화하여 세밀한
    시공간 주석과 함께 제공한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.05231v2.
sources:
- id: src_001
  type: paper
  title: 'Kaiwu: A Multimodal Manipulation Dataset and Framework for Robot Learning and Human-Robot Interaction'
  url: https://arxiv.org/abs/2503.05231
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Cutting-edge robot learning techniques including foundation models and imitation learning from humans all pose huge demands on large-scale and high-quality datasets which constitute one of the bottleneck in the general intelligent robot fields. This paper presents the Kaiwu multimodal dataset to address the missing real-world synchronized multimodal data problems in the sophisticated assembling scenario,especially with dynamics information and its fine-grained labelling. The dataset first provides an integration of human,environment and robot data collection framework with 20 subjects and 30 interaction objects resulting in totally 11,664 instances of integrated actions. For each of the demonstration,hand motions,operation pressures,sounds of the assembling process,multi-view videos, high-precision motion capture information,eye gaze with first-person videos,electromyography signals are all recorded. Fine-grained multi-level annotation based on absolute timestamp,and semantic segmentation labelling are performed. Kaiwu dataset aims to facilitate robot learning,dexterous manipulation,human intention investigation and human-robot collaboration research.

## 核心内容
Cutting-edge robot learning techniques including foundation models and imitation learning from humans all pose huge demands on large-scale and high-quality datasets which constitute one of the bottleneck in the general intelligent robot fields. This paper presents the Kaiwu multimodal dataset to address the missing real-world synchronized multimodal data problems in the sophisticated assembling scenario,especially with dynamics information and its fine-grained labelling. The dataset first provides an integration of human,environment and robot data collection framework with 20 subjects and 30 interaction objects resulting in totally 11,664 instances of integrated actions. For each of the demonstration,hand motions,operation pressures,sounds of the assembling process,multi-view videos, high-precision motion capture information,eye gaze with first-person videos,electromyography signals are all recorded. Fine-grained multi-level annotation based on absolute timestamp,and semantic segmentation labelling are performed. Kaiwu dataset aims to facilitate robot learning,dexterous manipulation,human intention investigation and human-robot collaboration research.

## 参考
- http://arxiv.org/abs/2503.05231v2

