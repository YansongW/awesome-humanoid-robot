---
$id: ent_paper_whole_body_humanoid_robot_loco_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Whole-body Humanoid Robot Locomotion with Human Reference
  zh: Whole-body Humanoid Robot Locomotion with Human Reference
  ko: Whole-body Humanoid Robot Locomotion with Human Reference
summary:
  en: Whole-body Humanoid Robot Locomotion with Human Reference is a 2024 work on locomotion for humanoid robots.
  zh: 本文提出一种基于对抗运动先验的全身仿人机器人运动模仿学习框架，由团队在2024年开发。核心贡献包括：设计全尺寸人形机器人"Adam"的创新结构，并首次将人类运动数据用于全尺寸人形机器人的模仿学习，使Adam在复杂运动任务中展现出与人类相当的性能。
  ko: Whole-body Humanoid Robot Locomotion with Human Reference is a 2024 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- whole_body_humanoid_robot_loco
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.18294v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (710 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Whole-body Humanoid Robot Locomotion with Human Reference (arXiv)
  url: https://arxiv.org/abs/2402.18294
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Whole-body Humanoid Robot Locomotion with Human Reference project page
  url: https://greatsjk.github.io/Adam-PNDbotics/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
针对强化学习在人形机器人应用中奖励函数设计复杂、系统训练困难等挑战，本文通过多次迭代研究，开发了全尺寸人形机器人"Adam"及其创新结构设计，显著提升了模仿学习效率。同时提出一种通用的对抗运动先验模仿学习框架，不仅适用于Adam，也可推广至其他人形机器人。实验表明，该框架使Adam在复杂运动任务中达到人类级表现，这是首次在全尺寸人形机器人上成功使用人类运动数据进行模仿学习。

## 核心内容
### 背景与挑战
- 强化学习虽推动人形机器人能力进步，但存在两大难题：复杂奖励函数设计困难、完整系统训练复杂度高
- 现有方法难以直接迁移人类运动数据至全尺寸人形机器人

### 核心方法
- **机器人平台**：自主研发全尺寸人形机器人"Adam"，其创新结构设计优化了模仿学习效率
- **模仿学习框架**：基于对抗运动先验（Adversarial Motion Prior）的通用框架，可适配不同人形机器人
- **训练策略**：通过对抗性训练使机器人学习人类运动数据的分布特征，无需手工设计复杂奖励函数

### 实验设置与结果
- **实验对象**：全尺寸人形机器人Adam
- **任务类型**：复杂运动任务（如行走、转向等）
- **关键发现**：
  - Adam成功复现人类运动特征，运动表现达到人类可比水平
  - 首次验证人类运动数据在全尺寸人形机器人模仿学习中的有效性
  - 框架具备通用性，可扩展至其他机器人平台

### 结论
本文通过机器人硬件创新与算法框架结合，解决了人形机器人运动学习中奖励函数设计难、系统训练复杂的问题，为人类运动数据在仿人机器人领域的应用开辟了新路径。

## Overview
Recently, humanoid robots have made significant advances in their ability to perform challenging tasks due to the deployment of Reinforcement Learning (RL), however, the inherent complexity of humanoid robots, including the difficulty of designing complicated reward functions and training entire sophisticated systems, still poses a notable challenge. To conquer these challenges, after many iterations and in-depth investigations, we have meticulously developed a full-size humanoid robot, "Adam", whose innovative structural design greatly improves the efficiency and effectiveness of the imitation learning process. In addition, we have developed a novel imitation learning framework based on an adversarial motion prior, which applies not only to Adam but also to humanoid robots in general. Using the framework, Adam can exhibit unprecedented human-like characteristics in locomotion tasks. Our experimental results demonstrate that the proposed framework enables Adam to achieve human-comparable performance in complex locomotion tasks, marking the first time that human locomotion data has been used for imitation learning in a full-size humanoid robot.

## Overview
Recently, humanoid robots have made significant advances in their ability to perform challenging tasks due to the deployment of Reinforcement Learning (RL). However, the inherent complexity of humanoid robots, including the difficulty of designing complicated reward functions and training entire sophisticated systems, still poses a notable challenge. To conquer these challenges, after many iterations and in-depth investigations, we have meticulously developed a full-size humanoid robot, "Adam", whose innovative structural design greatly improves the efficiency and effectiveness of the imitation learning process. In addition, we have developed a novel imitation learning framework based on an adversarial motion prior, which applies not only to Adam but also to humanoid robots in general. Using the framework, Adam can exhibit unprecedented human-like characteristics in locomotion tasks. Our experimental results demonstrate that the proposed framework enables Adam to achieve human-comparable performance in complex locomotion tasks, marking the first time that human locomotion data has been used for imitation learning in a full-size humanoid robot.

## Content
Recently, humanoid robots have made significant advances in their ability to perform challenging tasks due to the deployment of Reinforcement Learning (RL). However, the inherent complexity of humanoid robots, including the difficulty of designing complicated reward functions and training entire sophisticated systems, still poses a notable challenge. To conquer these challenges, after many iterations and in-depth investigations, we have meticulously developed a full-size humanoid robot, "Adam", whose innovative structural design greatly improves the efficiency and effectiveness of the imitation learning process. In addition, we have developed a novel imitation learning framework based on an adversarial motion prior, which applies not only to Adam but also to humanoid robots in general. Using the framework, Adam can exhibit unprecedented human-like characteristics in locomotion tasks. Our experimental results demonstrate that the proposed framework enables Adam to achieve human-comparable performance in complex locomotion tasks, marking the first time that human locomotion data has been used for imitation learning in a full-size humanoid robot.

## 参考
- http://arxiv.org/abs/2402.18294v4

## 개요
강화 학습이 휴머노이드 로봇 응용에서 보상 함수 설계가 복잡하고 시스템 훈련이 어려운 과제에 직면한 점을 고려하여, 본 논문은 여러 차례의 반복 연구를 통해 전신 휴머노이드 로봇 "Adam"과 그 혁신적인 구조 설계를 개발하여 모방 학습 효율을 크게 향상시켰습니다. 동시에 Adam뿐만 아니라 다른 휴머노이드 로봇에도 확장 가능한 범용 적대적 운동 사전 모방 학습 프레임워크를 제안합니다. 실험 결과, 이 프레임워크는 Adam이 복잡한 운동 작업에서 인간 수준의 성능을 달성하게 하였으며, 이는 전신 휴머노이드 로봇에서 인간 운동 데이터를 사용한 모방 학습이 처음으로 성공한 사례입니다.

## 핵심 내용
### 배경 및 과제
- 강화 학습은 휴머노이드 로봇의 능력 발전을 촉진했지만, 두 가지 주요 어려움이 존재합니다: 복잡한 보상 함수 설계의 어려움, 전체 시스템 훈련의 높은 복잡성
- 기존 방법은 인간 운동 데이터를 전신 휴머노이드 로봇에 직접 전이하기 어렵습니다

### 핵심 방법
- **로봇 플랫폼**: 자체 개발한 전신 휴머노이드 로봇 "Adam"으로, 혁신적인 구조 설계가 모방 학습 효율을 최적화했습니다
- **모방 학습 프레임워크**: 적대적 운동 사전(Adversarial Motion Prior) 기반의 범용 프레임워크로, 다양한 휴머노이드 로봇에 적용 가능
- **훈련 전략**: 적대적 훈련을 통해 로봇이 인간 운동 데이터의 분포 특성을 학습하도록 하여, 수작업으로 복잡한 보상 함수를 설계할 필요가 없습니다

### 실험 설정 및 결과
- **실험 대상**: 전신 휴머노이드 로봇 Adam
- **작업 유형**: 복잡한 운동 작업 (예: 보행, 회전 등)
- **주요 발견**:
  - Adam이 인간 운동 특성을 성공적으로 재현하여 운동 성능이 인간과 비교 가능한 수준에 도달
  - 전신 휴머노이드 로봇 모방 학습에서 인간 운동 데이터의 유효성을 처음으로 검증
  - 프레임워크가 범용성을 가지며 다른 로봇 플랫폼으로 확장 가능

### 결론
본 논문은 로봇 하드웨어 혁신과 알고리즘 프레임워크의 결합을 통해 휴머노이드 로봇 운동 학습에서 보상 함수 설계의 어려움과 시스템 훈련의 복잡성 문제를 해결하여, 인간 운동 데이터의 휴머노이드 로봇 분야 응용에 새로운 경로를 열었습니다.
