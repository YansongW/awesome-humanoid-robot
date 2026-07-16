---
$id: ent_paper_przystupa_learning_state_conditioned_lin_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning State Conditioned Linear Mappings for Low-Dimensional Control of Robotic Manipulators
  zh: 学习状态条件线性映射用于机械臂低维控制
  ko: 로봇 매니퓰레이터의 저차원 제어를 위한 상태 조건부 선형 매핑 학습
summary:
  en: This paper proposes State Conditioned Linear Maps (SCL maps), a method that uses neural networks to predict a state-dependent
    linear basis for controlling high-DOF robotic manipulators with low-DOF inputs, and validates it through user studies
    on a Kinova Gen-3 lite arm.
  zh: 本文提出状态条件线性映射（SCL映射），利用神经网络预测状态相关的线性基，以低自由度输入控制高自由度机械臂，并在Kinova Gen-3 lite机械臂上通过用户研究验证。
  ko: 본 논문은 신경망을 사용하여 상태 의존적 선형 기저를 예측하고 저자유도 입력으로 고자유도 로봇 매니퓰레이터를 제어하는 상태 조건부 선형 매핑(SCL maps)을 제안하고 Kinova Gen-3 lite 매니퓰레이터를
    통한 사용자 연구로 검증한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- state_conditioned_linear_maps
- teleoperation
- low_dimensional_control
- manipulator_control
- dimensionality_reduction
- kinova_gen3_lite
- humanoid_arms
- robot_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.21441v1.
sources:
- id: src_001
  type: paper
  title: Learning State Conditioned Linear Mappings for Low-Dimensional Control of Robotic Manipulators
  url: https://arxiv.org/abs/2410.21441
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Identifying an appropriate task space that simplifies control solutions is important for solving robotic manipulation problems. One approach to this problem is learning an appropriate low-dimensional action space. Linear and nonlinear action mapping methods have trade-offs between simplicity on the one hand and the ability to express motor commands outside of a single low-dimensional subspace on the other. We propose that learning local linear action representations that adapt based on the current configuration of the robot achieves both of these benefits. Our state-conditioned linear maps ensure that for any given state, the high-dimensional robotic actuations are linear in the low-dimensional action. As the robot state evolves, so do the action mappings, ensuring the ability to represent motions that are immediately necessary. These local linear representations guarantee desirable theoretical properties by design, and we validate these findings empirically through two user studies. Results suggest state-conditioned linear maps outperform conditional autoencoder and PCA baselines on a pick-and-place task and perform comparably to mode switching in a more complex pouring task.

## 核心内容
Identifying an appropriate task space that simplifies control solutions is important for solving robotic manipulation problems. One approach to this problem is learning an appropriate low-dimensional action space. Linear and nonlinear action mapping methods have trade-offs between simplicity on the one hand and the ability to express motor commands outside of a single low-dimensional subspace on the other. We propose that learning local linear action representations that adapt based on the current configuration of the robot achieves both of these benefits. Our state-conditioned linear maps ensure that for any given state, the high-dimensional robotic actuations are linear in the low-dimensional action. As the robot state evolves, so do the action mappings, ensuring the ability to represent motions that are immediately necessary. These local linear representations guarantee desirable theoretical properties by design, and we validate these findings empirically through two user studies. Results suggest state-conditioned linear maps outperform conditional autoencoder and PCA baselines on a pick-and-place task and perform comparably to mode switching in a more complex pouring task.

## 参考
- http://arxiv.org/abs/2410.21441v1

## Overview
Identifying an appropriate task space that simplifies control solutions is important for solving robotic manipulation problems. One approach to this problem is learning an appropriate low-dimensional action space. Linear and nonlinear action mapping methods have trade-offs between simplicity on the one hand and the ability to express motor commands outside of a single low-dimensional subspace on the other. We propose that learning local linear action representations that adapt based on the current configuration of the robot achieves both of these benefits. Our state-conditioned linear maps ensure that for any given state, the high-dimensional robotic actuations are linear in the low-dimensional action. As the robot state evolves, so do the action mappings, ensuring the ability to represent motions that are immediately necessary. These local linear representations guarantee desirable theoretical properties by design, and we validate these findings empirically through two user studies. Results suggest state-conditioned linear maps outperform conditional autoencoder and PCA baselines on a pick-and-place task and perform comparably to mode switching in a more complex pouring task.

## Content
Identifying an appropriate task space that simplifies control solutions is important for solving robotic manipulation problems. One approach to this problem is learning an appropriate low-dimensional action space. Linear and nonlinear action mapping methods have trade-offs between simplicity on the one hand and the ability to express motor commands outside of a single low-dimensional subspace on the other. We propose that learning local linear action representations that adapt based on the current configuration of the robot achieves both of these benefits. Our state-conditioned linear maps ensure that for any given state, the high-dimensional robotic actuations are linear in the low-dimensional action. As the robot state evolves, so do the action mappings, ensuring the ability to represent motions that are immediately necessary. These local linear representations guarantee desirable theoretical properties by design, and we validate these findings empirically through two user studies. Results suggest state-conditioned linear maps outperform conditional autoencoder and PCA baselines on a pick-and-place task and perform comparably to mode switching in a more complex pouring task.

## 개요
로봇 조작 문제를 해결하기 위해 제어 솔루션을 단순화하는 적절한 작업 공간을 식별하는 것은 중요합니다. 이 문제에 대한 한 가지 접근 방식은 적절한 저차원 행동 공간을 학습하는 것입니다. 선형 및 비선형 행동 매핑 방법은 단순성과 단일 저차원 부분 공간 외부의 모터 명령을 표현하는 능력 사이에서 절충점을 가집니다. 우리는 로봇의 현재 구성에 따라 적응하는 로컬 선형 행동 표현을 학습함으로써 이 두 가지 이점을 모두 얻을 수 있다고 제안합니다. 상태 조건부 선형 맵은 주어진 상태에 대해 고차원 로봇 작동이 저차원 행동에서 선형임을 보장합니다. 로봇 상태가 변화함에 따라 행동 매핑도 변화하여 즉시 필요한 움직임을 표현할 수 있는 능력을 보장합니다. 이러한 로컬 선형 표현은 설계상 바람직한 이론적 특성을 보장하며, 두 가지 사용자 연구를 통해 이러한 발견을 경험적으로 검증합니다. 결과는 상태 조건부 선형 맵이 집어 옮기기 작업에서 조건부 오토인코더 및 PCA 기준선보다 우수한 성능을 보이며, 더 복잡한 따르기 작업에서 모드 전환과 유사한 성능을 나타냄을 시사합니다.

## 핵심 내용
로봇 조작 문제를 해결하기 위해 제어 솔루션을 단순화하는 적절한 작업 공간을 식별하는 것은 중요합니다. 이 문제에 대한 한 가지 접근 방식은 적절한 저차원 행동 공간을 학습하는 것입니다. 선형 및 비선형 행동 매핑 방법은 단순성과 단일 저차원 부분 공간 외부의 모터 명령을 표현하는 능력 사이에서 절충점을 가집니다. 우리는 로봇의 현재 구성에 따라 적응하는 로컬 선형 행동 표현을 학습함으로써 이 두 가지 이점을 모두 얻을 수 있다고 제안합니다. 상태 조건부 선형 맵은 주어진 상태에 대해 고차원 로봇 작동이 저차원 행동에서 선형임을 보장합니다. 로봇 상태가 변화함에 따라 행동 매핑도 변화하여 즉시 필요한 움직임을 표현할 수 있는 능력을 보장합니다. 이러한 로컬 선형 표현은 설계상 바람직한 이론적 특성을 보장하며, 두 가지 사용자 연구를 통해 이러한 발견을 경험적으로 검증합니다. 결과는 상태 조건부 선형 맵이 집어 옮기기 작업에서 조건부 오토인코더 및 PCA 기준선보다 우수한 성능을 보이며, 더 복잡한 따르기 작업에서 모드 전환과 유사한 성능을 나타냄을 시사합니다.
