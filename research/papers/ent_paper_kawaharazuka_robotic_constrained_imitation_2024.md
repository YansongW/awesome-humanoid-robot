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
  zh: 本研究提出了一种约束模仿学习方法，从单个专家示范中提取运动约束，仅使用单目 RGB 图像训练预测模型，并在两台 Franka Emika Panda 机械臂上实现了 FLS 钉转移任务。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.03440v1.
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
In this study, we present an implementation strategy for a robot that performs peg transfer tasks in Fundamentals of Laparoscopic Surgery (FLS) via imitation learning, aimed at the development of an autonomous robot for laparoscopic surgery. Robotic laparoscopic surgery presents two main challenges: (1) the need to manipulate forceps using ports established on the body surface as fulcrums, and (2) difficulty in perceiving depth information when working with a monocular camera that displays its images on a monitor. Especially, regarding issue (2), most prior research has assumed the availability of depth images or models of a target to be operated on. Therefore, in this study, we achieve more accurate imitation learning with only monocular images by extracting motion constraints from one exemplary motion of skilled operators, collecting data based on these constraints, and conducting imitation learning based on the collected data. We implemented an overall system using two Franka Emika Panda Robot Arms and validated its effectiveness.

## 核心内容
In this study, we present an implementation strategy for a robot that performs peg transfer tasks in Fundamentals of Laparoscopic Surgery (FLS) via imitation learning, aimed at the development of an autonomous robot for laparoscopic surgery. Robotic laparoscopic surgery presents two main challenges: (1) the need to manipulate forceps using ports established on the body surface as fulcrums, and (2) difficulty in perceiving depth information when working with a monocular camera that displays its images on a monitor. Especially, regarding issue (2), most prior research has assumed the availability of depth images or models of a target to be operated on. Therefore, in this study, we achieve more accurate imitation learning with only monocular images by extracting motion constraints from one exemplary motion of skilled operators, collecting data based on these constraints, and conducting imitation learning based on the collected data. We implemented an overall system using two Franka Emika Panda Robot Arms and validated its effectiveness.

## 参考
- http://arxiv.org/abs/2405.03440v1

## Overview
In this study, we present an implementation strategy for a robot that performs peg transfer tasks in Fundamentals of Laparoscopic Surgery (FLS) via imitation learning, aimed at the development of an autonomous robot for laparoscopic surgery. Robotic laparoscopic surgery presents two main challenges: (1) the need to manipulate forceps using ports established on the body surface as fulcrums, and (2) difficulty in perceiving depth information when working with a monocular camera that displays its images on a monitor. Especially, regarding issue (2), most prior research has assumed the availability of depth images or models of a target to be operated on. Therefore, in this study, we achieve more accurate imitation learning with only monocular images by extracting motion constraints from one exemplary motion of skilled operators, collecting data based on these constraints, and conducting imitation learning based on the collected data. We implemented an overall system using two Franka Emika Panda Robot Arms and validated its effectiveness.

## Content
In this study, we present an implementation strategy for a robot that performs peg transfer tasks in Fundamentals of Laparoscopic Surgery (FLS) via imitation learning, aimed at the development of an autonomous robot for laparoscopic surgery. Robotic laparoscopic surgery presents two main challenges: (1) the need to manipulate forceps using ports established on the body surface as fulcrums, and (2) difficulty in perceiving depth information when working with a monocular camera that displays its images on a monitor. Especially, regarding issue (2), most prior research has assumed the availability of depth images or models of a target to be operated on. Therefore, in this study, we achieve more accurate imitation learning with only monocular images by extracting motion constraints from one exemplary motion of skilled operators, collecting data based on these constraints, and conducting imitation learning based on the collected data. We implemented an overall system using two Franka Emika Panda Robot Arms and validated its effectiveness.

## 개요
본 연구에서는 복강경 수술을 위한 자율 로봇 개발을 목표로, 모방 학습을 통해 복강경 수술 기초(Fundamentals of Laparoscopic Surgery, FLS)의 페그 이동(peg transfer) 작업을 수행하는 로봇의 구현 전략을 제시합니다. 로봇 복강경 수술은 두 가지 주요 과제를 안고 있습니다: (1) 체표면에 설정된 포트를 지점으로 사용하여 겸자를 조작해야 하며, (2) 모니터에 영상을 표시하는 단안 카메라로 작업할 때 깊이 정보를 인식하기 어렵다는 점입니다. 특히 (2)번 문제와 관련하여, 대부분의 선행 연구는 깊이 이미지나 수술 대상의 모델을 사용할 수 있다고 가정했습니다. 따라서 본 연구에서는 숙련된 수술자의 하나의 시범 동작에서 동작 제약 조건을 추출하고, 이 제약 조건을 기반으로 데이터를 수집한 후, 수집된 데이터를 바탕으로 모방 학습을 수행함으로써 단안 이미지만으로 더 정확한 모방 학습을 달성합니다. 두 대의 Franka Emika Panda 로봇 팔을 사용하여 전체 시스템을 구현하고 그 효과를 검증했습니다.

## 핵심 내용
본 연구에서는 복강경 수술을 위한 자율 로봇 개발을 목표로, 모방 학습을 통해 복강경 수술 기초(FLS)의 페그 이동 작업을 수행하는 로봇의 구현 전략을 제시합니다. 로봇 복강경 수술은 두 가지 주요 과제를 안고 있습니다: (1) 체표면에 설정된 포트를 지점으로 사용하여 겸자를 조작해야 하며, (2) 모니터에 영상을 표시하는 단안 카메라로 작업할 때 깊이 정보를 인식하기 어렵다는 점입니다. 특히 (2)번 문제와 관련하여, 대부분의 선행 연구는 깊이 이미지나 수술 대상의 모델을 사용할 수 있다고 가정했습니다. 따라서 본 연구에서는 숙련된 수술자의 하나의 시범 동작에서 동작 제약 조건을 추출하고, 이 제약 조건을 기반으로 데이터를 수집한 후, 수집된 데이터를 바탕으로 모방 학습을 수행함으로써 단안 이미지만으로 더 정확한 모방 학습을 달성합니다. 두 대의 Franka Emika Panda 로봇 팔을 사용하여 전체 시스템을 구현하고 그 효과를 검증했습니다.
