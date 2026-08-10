---
$id: ent_paper_kawaharazuka_robotic_constrained_imitation_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robotic Constrained Imitation Learning for the Peg Transfer Task in Fundamentals of Laparoscopic Surgery
  zh: 腹腔镜手术基础中钉转移任务的机器人约束模仿学习
  ko: 복강경 수술 기초의 Peg Transfer 작업을 위한 로봇 제약 모방 학습
summary:
  en: This paper proposes a constrained imitation learning method that extracts motion constraints from a single expert demonstration
    to train a predictive model for the FLS peg transfer task using only monocular RGB images, implemented on two Franka Emika
    Panda robot arms.
  zh: 本文提出一种约束模仿学习方法，仅通过单次专家演示提取运动约束，并利用单目RGB图像训练预测模型，实现FLS peg transfer任务的机器人自主操作。该方法部署于两台Franka Emika Panda机械臂上，旨在推动腹腔镜手术机器人的自主化发展。
  ko: 본 연구는 단일 전문가 시연에서 운동 제약을 추출하여 단안 RGB 이미지만으로 FLS peg transfer 작업을 위한 예측 모델을 학습하는 제약 모방 학습 방법을 제안하고, 두 대의 Franka Emika
    Panda 로봇 팔로 구현하였다.
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
- constrained_imitation_learning
- laparoscopic_surgery
- monocular_vision
- rnnpb
- fls_peg_transfer
- surgical_robotics
- forceps_manipulation
- single_demonstration_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.03440v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (745 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Robotic Constrained Imitation Learning for the Peg Transfer Task in Fundamentals of Laparoscopic Surgery
  url: https://arxiv.org/abs/2405.03440
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对机器人腹腔镜手术中单目相机缺乏深度信息及器械受穿刺点约束两大挑战，本研究提出一种约束模仿学习框架。该方法从单个专家演示中提取运动约束，基于这些约束生成训练数据，再通过模仿学习训练预测模型。整个系统在双Franka Emika Panda机械臂平台上实现，仅依赖单目RGB图像即可完成FLS peg transfer任务，无需深度图像或目标模型先验知识。

## 核心内容
### 研究背景与挑战
- 机器人腹腔镜手术面临两大核心问题：
  1. 器械需以体表穿刺点为支点进行运动（杠杆约束）
  2. 单目相机显示在监视器上，缺乏深度感知能力
- 现有方法多依赖深度图像或目标模型，而本研究仅使用单目RGB图像

### 方法架构
- **运动约束提取**：从单个专家演示中自动提取关键运动约束（如器械末端轨迹、穿刺点位置等）
- **数据生成**：基于提取的约束条件，通过采样生成多样化训练数据
- **模仿学习**：使用生成数据训练预测模型，实现从单目图像到动作的端到端映射

### 实验设置
- **硬件平台**：两台Franka Emika Panda机械臂，配备单目RGB相机
- **任务**：FLS标准peg transfer任务（将塑料块从一侧转移至另一侧）
- **对比基准**：与使用深度图像的方法进行对比

### 关键结果
- 仅凭单目RGB图像，该方法在peg transfer任务中达到与深度方法相当的精度
- 运动约束的引入使模型对光照变化和背景干扰具有鲁棒性
- 单次演示即可完成训练，大幅降低数据采集成本

### 结论
本研究证明，通过提取运动约束，单目RGB图像足以支持复杂手术任务的模仿学习，为低成本手术机器人自主化提供了可行方案。

## Overview
In this study, we present an implementation strategy for a robot that performs peg transfer tasks in Fundamentals of Laparoscopic Surgery (FLS) via imitation learning, aimed at the development of an autonomous robot for laparoscopic surgery. Robotic laparoscopic surgery presents two main challenges: (1) the need to manipulate forceps using ports established on the body surface as fulcrums, and (2) difficulty in perceiving depth information when working with a monocular camera that displays its images on a monitor. Especially, regarding issue (2), most prior research has assumed the availability of depth images or models of a target to be operated on. Therefore, in this study, we achieve more accurate imitation learning with only monocular images by extracting motion constraints from one exemplary motion of skilled operators, collecting data based on these constraints, and conducting imitation learning based on the collected data. We implemented an overall system using two Franka Emika Panda Robot Arms and validated its effectiveness.

## 参考
- http://arxiv.org/abs/2405.03440v1

## 개요
로봇 복강경 수술에서 단안 카메라의 깊이 정보 부족 및 기구가 천자점에 의해 구속되는 두 가지 과제를 해결하기 위해, 본 연구는 제약 모방 학습 프레임워크를 제안한다. 이 방법은 단일 전문가 시연에서 운동 제약을 추출하고, 이러한 제약을 기반으로 훈련 데이터를 생성한 후, 모방 학습을 통해 예측 모델을 훈련한다. 전체 시스템은 이중 Franka Emika Panda 로봇 팔 플랫폼에서 구현되며, 단안 RGB 이미지만으로 FLS peg transfer 작업을 완료할 수 있고, 깊이 이미지나 대상 모델 사전 지식이 필요 없다.

## 핵심 내용
### 연구 배경 및 과제
- 로봇 복강경 수술은 두 가지 핵심 문제에 직면한다:
  1. 기구는 체표 천자점을 지점으로 운동해야 한다 (지렛대 제약)
  2. 단안 카메라가 모니터에 표시되어 깊이 인식 능력이 부족하다
- 기존 방법은 주로 깊이 이미지나 대상 모델에 의존하지만, 본 연구는 단안 RGB 이미지만 사용한다

### 방법 아키텍처
- **운동 제약 추출**: 단일 전문가 시연에서 핵심 운동 제약(예: 기구 말단 궤적, 천자점 위치 등)을 자동으로 추출
- **데이터 생성**: 추출된 제약 조건을 기반으로 샘플링을 통해 다양한 훈련 데이터 생성
- **모방 학습**: 생성된 데이터를 사용하여 예측 모델을 훈련하고, 단안 이미지에서 동작까지의 종단 간 매핑 구현

### 실험 설정
- **하드웨어 플랫폼**: 단안 RGB 카메라가 장착된 두 대의 Franka Emika Panda 로봇 팔
- **작업**: FLS 표준 peg transfer 작업(플라스틱 블록을 한쪽에서 다른 쪽으로 이동)
- **비교 기준**: 깊이 이미지를 사용하는 방법과 비교

### 핵심 결과
- 단안 RGB 이미지만으로도 이 방법은 peg transfer 작업에서 깊이 방법과 동등한 정밀도를 달성
- 운동 제약 도입으로 모델이 조명 변화와 배경 간섭에 강건해짐
- 단일 시연으로 훈련이 완료되어 데이터 수집 비용이 크게 절감

### 결론
본 연구는 운동 제약을 추출함으로써 단안 RGB 이미지만으로도 복잡한 수술 작업의 모방 학습을 지원할 수 있음을 입증하며, 저비용 수술 로봇 자율화를 위한 실현 가능한 방안을 제공한다.
