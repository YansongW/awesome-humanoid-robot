---
$id: ent_paper_he_forceband_learning_forceful_ma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ForceBand: Learning Forceful Manipulation with sEMG'
  zh: ForceBand：利用表面肌电信号学习有力操作
  ko: 'ForceBand: sEMG를 이용한 힘 있는 조작 학습'
summary:
  en: ForceBand introduces a low-cost wrist-worn sEMG system that predicts per-finger
    forces from muscle activity, enabling force-enriched human demonstrations for
    robot policy learning. It achieves 87% success on pick-squeeze-place tasks and
    over 50% lower force prediction error than vision-based baselines.
  zh: ForceBand 提出了一种低成本腕戴式表面肌电系统，通过肌肉活动预测每根手指的力，从而为机器人策略学习提供富含力信息的人类演示。在抓取-挤压-放置任务中达到87%的成功率，力预测误差比基于视觉的基线降低50%以上。
  ko: ForceBand는 근육 활동으로부터 손가락별 힘을 예측하는 저비용 손목 착용 sEMG 시스템을 도입하여 로봇 정책 학습을 위한 힘 정보가
    풍부한 인간 시연을 가능하게 합니다. 집기-짜기-놓기 작업에서 87%의 성공률을 달성하고, 비전 기반 기준선보다 50% 이상 낮은 힘 예측
    오차를 보입니다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- force_estimation
- semg
- imitation_learning
- forceful_manipulation
- robot_policy_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'ForceBand: Learning Forceful Manipulation with sEMG'
  url: https://arxiv.org/abs/2606.26093
  date: '2026'
  accessed_at: '2026-06-25'
related_entities: []
theoretical_depth:
- system
---

## Overview

ForceBand presents a low-cost, wrist-worn surface electromyography (sEMG) system that captures human muscle activity to predict per-finger forces, thereby augmenting human demonstrations with force information for robot policy learning. The system comprises a custom sEMG band with muscle-aware electrode placement, an IMU, and an egocentric camera. The authors collected a 10-hour multimodal dataset of synchronized egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, they pre-trained an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only the ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments demonstrate that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines, and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights.

## Key Contributions

- Low-cost, reproducible wrist-worn sEMG band with muscle-aware electrode placement
- 10-hour multimodal dataset of synchronized egocentric video, sEMG, IMU, and fingertip forces
- EMG2Force model that predicts per-finger forces from sEMG and IMU with over 50% lower error than vision baselines
- Force-aware policy learning pipeline that achieves 87% success on pick-squeeze-place tasks
- Demonstration of object-specific force control and transfer to out-of-distribution objects

## Relevance to Humanoid Robotics

ForceBand provides a scalable method to add force supervision to human demonstrations, which is essential for humanoid robots to learn forceful manipulation tasks required in mass production and deployment. By enabling force-enriched demonstrations from human activity, it addresses a critical gap in imitation learning for humanoid robots that need to apply appropriate forces during manipulation. The system's low cost and ease of use make it practical for collecting large-scale force-augmented data, which can be used to train humanoid robot policies for tasks such as assembly, packaging, and other force-sensitive industrial applications.
