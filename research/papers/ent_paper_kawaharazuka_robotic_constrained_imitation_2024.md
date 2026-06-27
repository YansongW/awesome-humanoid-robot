---
$id: ent_paper_kawaharazuka_robotic_constrained_imitation_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robotic Constrained Imitation Learning for the Peg Transfer Task in Fundamentals
    of Laparoscopic Surgery
  zh: 腹腔镜手术基础中钉转移任务的机器人约束模仿学习
  ko: 복강경 수술 기초의 Peg Transfer 작업을 위한 로봇 제약 모방 학습
summary:
  en: This paper proposes a constrained imitation learning method that extracts motion
    constraints from a single expert demonstration to train a predictive model for
    the FLS peg transfer task using only monocular RGB images, implemented on two
    Franka Emika Panda robot arms.
  zh: 本研究提出了一种约束模仿学习方法，从单个专家示范中提取运动约束，仅使用单目 RGB 图像训练预测模型，并在两台 Franka Emika Panda 机械臂上实现了
    FLS 钉转移任务。
  ko: 본 연구는 단일 전문가 시연에서 운동 제약을 추출하여 단안 RGB 이미지만으로 FLS peg transfer 작업을 위한 예측 모델을 학습하는
    제약 모방 학습 방법을 제안하고, 두 대의 Franka Emika Panda 로봇 팔로 구현하였다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from abstract and metadata; requires human review against the
    full arXiv text before verification.
sources:
- id: src_001
  type: paper
  title: Robotic Constrained Imitation Learning for the Peg Transfer Task in Fundamentals
    of Laparoscopic Surgery
  url: https://arxiv.org/abs/2405.03440
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper addresses autonomous robotic laparoscopic surgery, specifically the Fundamentals of Laparoscopic Surgery (FLS) peg transfer task. The authors identify two core challenges in robotic laparoscopic surgery: forceps must pass through body-surface ports that act as fulcrums, and depth perception is limited because only a monocular endoscopic camera is available. Most prior work assumes access to depth images or object models, whereas this study aims to perform accurate imitation learning using only monocular RGB observations.

The proposed approach extracts phase-specific motion constraints from a single exemplary motion performed by a skilled operator. These constraints are then used to provide force feedback during human teaching, guiding data collection. A recurrent neural network with parametric bias (RNNPB) is trained on the collected monocular RGB data to learn predictive control policies. The authors also formulate a constrained inverse kinematics problem using a virtual linear joint to enforce the laparoscopic port constraint. The complete system is implemented on two Franka Emika Panda robot arms equipped with Maryland dissectors and parallel grippers, and experiments compare constrained versus unconstrained data collection.

The experimental results support the claim that collecting data under extracted motion constraints improves imitation learning success compared to unconstrained data collection. The paper also discusses limitations, including the manual design of phase transitions and constraint forms, the simplified FLS training box environment, uncertainty about constraint extraction in more complex scenarios, and the absence of bilateral force feedback.

## Key Contributions

- A constrained imitation learning method that extracts motion constraints from a single exemplary demonstration and trains a predictive model.
- An overall laparoscopic surgery robot system and control architecture that performs the FLS peg transfer task.
- A constrained inverse kinematics formulation with a virtual linear joint to enforce the laparoscopic port constraint.
- Experimental validation that constrained data collection improves imitation learning success over unconstrained data collection.

## Relevance to Humanoid Robotics

The constrained imitation learning framework developed in this paper is relevant to humanoid robotics because it shows how to derive and enforce motion constraints from a single demonstration under limited sensing. Humanoid robots deployed in mass production or constrained assembly environments often face kinematic constraints, limited camera viewpoints, and the need to learn manipulation skills quickly from few demonstrations. The paper's approach to extracting constraints, using them to guide data collection with force feedback, and training recurrent predictive models on monocular images provides a transferable methodology for humanoid teleoperation and constrained manipulation tasks.
