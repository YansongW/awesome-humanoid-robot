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
  en: ForceBand introduces a low-cost wrist-worn sEMG system that predicts per-finger forces from muscle activity, enabling
    force-enriched human demonstrations for robot policy learning. It achieves 87% success on pick-squeeze-place tasks and
    over 50% lower force prediction error than vision-based baselines.
  zh: ForceBand 提出了一种低成本腕戴式表面肌电系统，通过肌肉活动预测每根手指的力，从而为机器人策略学习提供富含力信息的人类演示。在抓取-挤压-放置任务中达到87%的成功率，力预测误差比基于视觉的基线降低50%以上。
  ko: ForceBand는 근육 활동으로부터 손가락별 힘을 예측하는 저비용 손목 착용 sEMG 시스템을 도입하여 로봇 정책 학습을 위한 힘 정보가 풍부한 인간 시연을 가능하게 합니다. 집기-짜기-놓기 작업에서 87%의
    성공률을 달성하고, 비전 기반 기준선보다 50% 이상 낮은 힘 예측 오차를 보입니다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.26093v1.
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
## 概述
Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io

## 核心内容
Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io

## 参考
- http://arxiv.org/abs/2606.26093v1

## Overview
Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io

## Content
Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io

## 개요
인간의 시연은 로봇 조작 정책을 학습하기 위한 확장 가능한 데이터 소스입니다. 그러나 모션 캡처 궤적 및 인터넷 비디오와 같은 일반적인 인간 시연 데이터 소스는 주로 움직임과 외형을 포착하는 반면, 힘에 민감한 조작에 중요한 접촉 힘은 누락됩니다. 본 논문에서는 저렴한 손목 착용형 sEMG 시스템인 ForceBand를 소개합니다. 이 시스템은 인간의 근육 활동을 힘이 풍부한 시연으로 변환합니다. 먼저 다양한 동작과 객체에 걸쳐 자기중심적 비디오, sEMG, IMU 및 손끝 힘 측정값을 포함하는 10시간 분량의 다중 모달 데이터셋을 수집합니다. 이 데이터셋을 사용하여 sEMG 및 IMU 신호로부터 손가락별 힘을 예측하는 EMG2Force 모델을 사전 학습합니다. 짧은 사용자별 캘리브레이션 후, 사용자는 ForceBand와 비디오만을 사용하여 대상 작업 시연을 수집할 수 있습니다. 그런 다음 EMG2Force는 이러한 시연에 손가락별 힘 궤적을 레이블링하여 로봇 정책 학습을 위한 힘 증강 시연을 생성합니다. 실험 결과, ForceBand는 비전 기반 기준선보다 50% 이상 낮은 힘 예측 오차로 세밀한 손끝 상호작용을 복원하며, 다양한 모양, 크기 및 무게의 객체에 걸쳐 객체별 힘 제어가 필요한 집기, 쥐기 및 놓기 작업에서 87%의 성공률을 달성합니다. 프로젝트 웹사이트: https://forceband-emg.github.io

## 핵심 내용
인간의 시연은 로봇 조작 정책을 학습하기 위한 확장 가능한 데이터 소스입니다. 그러나 모션 캡처 궤적 및 인터넷 비디오와 같은 일반적인 인간 시연 데이터 소스는 주로 움직임과 외형을 포착하는 반면, 힘에 민감한 조작에 중요한 접촉 힘은 누락됩니다. 본 논문에서는 저렴한 손목 착용형 sEMG 시스템인 ForceBand를 소개합니다. 이 시스템은 인간의 근육 활동을 힘이 풍부한 시연으로 변환합니다. 먼저 다양한 동작과 객체에 걸쳐 자기중심적 비디오, sEMG, IMU 및 손끝 힘 측정값을 포함하는 10시간 분량의 다중 모달 데이터셋을 수집합니다. 이 데이터셋을 사용하여 sEMG 및 IMU 신호로부터 손가락별 힘을 예측하는 EMG2Force 모델을 사전 학습합니다. 짧은 사용자별 캘리브레이션 후, 사용자는 ForceBand와 비디오만을 사용하여 대상 작업 시연을 수집할 수 있습니다. 그런 다음 EMG2Force는 이러한 시연에 손가락별 힘 궤적을 레이블링하여 로봇 정책 학습을 위한 힘 증강 시연을 생성합니다. 실험 결과, ForceBand는 비전 기반 기준선보다 50% 이상 낮은 힘 예측 오차로 세밀한 손끝 상호작용을 복원하며, 다양한 모양, 크기 및 무게의 객체에 걸쳐 객체별 힘 제어가 필요한 집기, 쥐기 및 놓기 작업에서 87%의 성공률을 달성합니다. 프로젝트 웹사이트: https://forceband-emg.github.io
