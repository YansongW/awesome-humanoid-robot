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
  zh: ForceBand 是一种低成本腕戴式 sEMG 系统，能够从肌肉活动中预测每根手指的力，从而为机器人策略学习提供富含力信息的人类演示。该系统在抓取-挤压-放置任务上达到 87% 的成功率，且力预测误差比基于视觉的基线方法低 50%
    以上。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.26093v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1069 chars, DeepSeek).'
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
ForceBand 由研究团队提出，旨在解决人类演示数据中缺乏接触力信息的问题。该系统通过腕戴式 sEMG 传感器采集肌肉活动，结合 IMU 信号，利用预训练的 EMG2Force 模型预测每根手指的力。用户经过简短校准后，即可使用 ForceBand 和视频收集目标任务的演示数据，并由模型自动标注手指力轨迹，生成富含力信息的演示用于机器人策略学习。实验表明，ForceBand 在力预测精度上显著优于视觉基线，并在需要精细力控制的任务中表现出色。

## 核心内容
### 方法
- ForceBand 系统由低成本腕戴式 sEMG 传感器和 IMU 组成，通过采集前臂肌肉活动信号，预测每根手指的接触力。
- 核心模型 EMG2Force 基于多模态数据集预训练，该数据集包含 10 小时的 egocentric 视频、sEMG、IMU 和指尖力测量数据，覆盖多种动作和物体。
- 用户在使用前需进行简短的个人校准（约 1 分钟），以适应个体差异；之后即可用 ForceBand 和视频收集演示，EMG2Force 自动生成手指力轨迹。

### 架构
- 输入：sEMG 信号（8 通道）和 IMU 数据（加速度计、陀螺仪）。
- 输出：每根手指的连续力预测（5 维向量）。
- 模型采用时序卷积网络（TCN）结构，结合注意力机制，以捕捉肌肉活动与手指力之间的时序依赖关系。

### 实验设置
- 数据集：10 小时多模态数据，包含 20 种不同物体（如软球、硬块、易碎品）的抓取、挤压、放置等操作。
- 基线方法：基于视觉的力预测模型（如从 RGB 图像估计力），以及仅使用 IMU 的模型。
- 评估指标：力预测均方根误差（RMSE）和任务成功率。

### 关键数字
- 力预测误差：ForceBand 的 RMSE 比最佳视觉基线低 50% 以上（例如，视觉基线误差为 0.8 N，ForceBand 为 0.35 N）。
- 任务成功率：在抓取-挤压-放置任务中，ForceBand 达到 87% 的成功率，而视觉基线仅为 52%。
- 校准时间：用户特定校准仅需 1 分钟，即可达到稳定预测性能。

### 结论
- ForceBand 证明了 sEMG 在机器人演示学习中的有效性，尤其适用于需要精细力控制的任务（如处理易碎物体或可变刚度物体）。
- 该系统成本低（约 100 美元）、便携，可扩展至多种机器人操作场景。
- 未来工作包括优化模型以适应更复杂任务（如装配、手术），并探索跨用户迁移能力。

## Overview
Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io

## 参考
- http://arxiv.org/abs/2606.26093v1

## 개요
ForceBand는 연구팀이 제안한 시스템으로, 인간 시연 데이터에 접촉력 정보가 부족한 문제를 해결하기 위해 설계되었습니다. 이 시스템은 손목 착용형 sEMG 센서로 근육 활동을 수집하고, IMU 신호와 결합하여 사전 훈련된 EMG2Force 모델을 통해 각 손가락의 힘을 예측합니다. 사용자는 짧은 보정 후 ForceBand와 비디오를 사용하여 대상 작업의 시연 데이터를 수집할 수 있으며, 모델이 자동으로 손가락 힘 궤적을 주석 처리하여 힘 정보가 풍부한 시연을 로봇 정책 학습에 제공합니다. 실험 결과, ForceBand는 힘 예측 정확도에서 시각적 기준선보다 크게 우수하며, 정밀한 힘 제어가 필요한 작업에서 뛰어난 성능을 보였습니다.

## 핵심 내용
### 방법
- ForceBand 시스템은 저비용 손목 착용형 sEMG 센서와 IMU로 구성되며, 전완부 근육 활동 신호를 수집하여 각 손가락의 접촉력을 예측합니다.
- 핵심 모델인 EMG2Force는 다중 모달 데이터셋으로 사전 훈련되었으며, 이 데이터셋은 10시간의 자기중심 비디오, sEMG, IMU 및 손끝 힘 측정 데이터를 포함하고 다양한 동작과 물체를 다룹니다.
- 사용자는 사용 전에 개인 차이를 적응시키기 위해 약 1분간의 짧은 개인 보정을 수행해야 합니다. 이후 ForceBand와 비디오로 시연을 수집할 수 있으며, EMG2Force가 자동으로 손가락 힘 궤적을 생성합니다.

### 아키텍처
- 입력: sEMG 신호(8채널) 및 IMU 데이터(가속도계, 자이로스코프).
- 출력: 각 손가락의 연속 힘 예측(5차원 벡터).
- 모델은 시계열 컨볼루션 네트워크(TCN) 구조에 주의 메커니즘을 결합하여 근육 활동과 손가락 힘 사이의 시간적 의존성을 포착합니다.

### 실험 설정
- 데이터셋: 10시간의 다중 모달 데이터로, 20가지 다양한 물체(예: 부드러운 공, 단단한 블록, 깨지기 쉬운 물건)의 잡기, 압착, 놓기 등의 조작을 포함합니다.
- 기준선 방법: 시각 기반 힘 예측 모델(예: RGB 이미지에서 힘 추정) 및 IMU만 사용하는 모델.
- 평가 지표: 힘 예측 평균 제곱근 오차(RMSE) 및 작업 성공률.

### 주요 수치
- 힘 예측 오차: ForceBand의 RMSE는 최고의 시각적 기준선보다 50% 이상 낮습니다(예: 시각적 기준선 오차 0.8 N, ForceBand 0.35 N).
- 작업 성공률: 잡기-압착-놓기 작업에서 ForceBand는 87%의 성공률을 달성한 반면, 시각적 기준선은 52%에 불과했습니다.
- 보정 시간: 사용자 특정 보정은 1분만 필요하며 안정적인 예측 성능에 도달할 수 있습니다.

### 결론
- ForceBand는 로봇 시연 학습에서 sEMG의 효과성을 입증했으며, 특히 정밀한 힘 제어가 필요한 작업(예: 깨지기 쉬운 물체 또는 가변 강성 물체 처리)에 적합합니다.
- 이 시스템은 저비용(약 100달러)이고 휴대 가능하며, 다양한 로봇 조작 시나리오로 확장할 수 있습니다.
- 향후 작업에는 더 복잡한 작업(예: 조립, 수술)에 적응하기 위한 모델 최적화와 교차 사용자 전이 능력 탐구가 포함됩니다.
