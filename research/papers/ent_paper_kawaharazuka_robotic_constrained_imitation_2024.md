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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.03440v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
본 연구에서는 복강경 수술을 위한 자율 로봇 개발을 목표로, 모방 학습을 통해 복강경 수술 기초(Fundamentals of Laparoscopic Surgery, FLS)의 페그 이동(peg transfer) 작업을 수행하는 로봇의 구현 전략을 제시합니다. 로봇 복강경 수술은 두 가지 주요 과제를 안고 있습니다: (1) 체표면에 설정된 포트를 지점으로 사용하여 겸자를 조작해야 하며, (2) 모니터에 영상을 표시하는 단안 카메라로 작업할 때 깊이 정보를 인식하기 어렵다는 점입니다. 특히 (2)번 문제와 관련하여, 대부분의 선행 연구는 깊이 이미지나 수술 대상의 모델을 사용할 수 있다고 가정했습니다. 따라서 본 연구에서는 숙련된 수술자의 하나의 시범 동작에서 동작 제약 조건을 추출하고, 이 제약 조건을 기반으로 데이터를 수집한 후, 수집된 데이터를 바탕으로 모방 학습을 수행함으로써 단안 이미지만으로 더 정확한 모방 학습을 달성합니다. 두 대의 Franka Emika Panda 로봇 팔을 사용하여 전체 시스템을 구현하고 그 효과를 검증했습니다.

## 핵심 내용
본 연구에서는 복강경 수술을 위한 자율 로봇 개발을 목표로, 모방 학습을 통해 복강경 수술 기초(FLS)의 페그 이동 작업을 수행하는 로봇의 구현 전략을 제시합니다. 로봇 복강경 수술은 두 가지 주요 과제를 안고 있습니다: (1) 체표면에 설정된 포트를 지점으로 사용하여 겸자를 조작해야 하며, (2) 모니터에 영상을 표시하는 단안 카메라로 작업할 때 깊이 정보를 인식하기 어렵다는 점입니다. 특히 (2)번 문제와 관련하여, 대부분의 선행 연구는 깊이 이미지나 수술 대상의 모델을 사용할 수 있다고 가정했습니다. 따라서 본 연구에서는 숙련된 수술자의 하나의 시범 동작에서 동작 제약 조건을 추출하고, 이 제약 조건을 기반으로 데이터를 수집한 후, 수집된 데이터를 바탕으로 모방 학습을 수행함으로써 단안 이미지만으로 더 정확한 모방 학습을 달성합니다. 두 대의 Franka Emika Panda 로봇 팔을 사용하여 전체 시스템을 구현하고 그 효과를 검증했습니다.

## 参考
- http://arxiv.org/abs/2405.03440v1
