---
$id: ent_paper_fu_load_aware_locomotion_control_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Load-Aware Locomotion Control for Humanoid Robots in Industrial Transportation Tasks
  zh: 面向工业搬运任务的人形机器人负载感知 locomotion 控制
  ko: 산업 운반 작업을 위한 휴머노이드 로봇의 부하 인식 보행 제어
summary:
  en: This paper presents a reinforcement-learning-based load-aware locomotion framework for full-size humanoid robots performing
    industrial load-carrying and box-handling tasks, using a decoupled loco-manipulation architecture with kinematic references,
    height-conditioned joint offsets, and history-based state estimation, trained entirely in simulation and deployed zero-shot
    on the Tiangong 2.0 Pro robot.
  zh: 本文提出了一种基于强化学习的负载感知运动框架，用于全尺寸人形机器人在工业搬运任务中的稳定行走。该框架采用解耦的移动操作架构，结合运动学参考、高度条件关节偏移和历史状态估计，在仿真中训练后零样本部署于天工2.0 Pro机器人。
  ko: 본 논문은 산업용 운반 및 박스 취급 작업을 수행하는 실제 크기의 휴머노이드 로봇을 위한 강화학습 기반 부하 인식 보행 제어 프레임워크를 제안한다. 이 프레임워크는 운동학적 기준, 높이 조건부 관절 오프셋,
    그리고 이력 기반 상태 추정을 갖춘 분리된 loco-manipulation 아키텍처를 사용하며, 전적으로 시뮬레이션에서 훈련된 후 Tiangong 2.0 Pro 로봇에 미세 조정 없이 배포되었다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
- 03_manufacturing_processes
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- load_aware_locomotion
- loco_manipulation
- reinforcement_learning
- sim_to_real
- industrial_transportation
- state_estimation
- residual_policy
- tiangong_2_pro
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.14308v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (795 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Load-Aware Locomotion Control for Humanoid Robots in Industrial Transportation Tasks
  url: https://arxiv.org/abs/2603.14308
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
该研究针对人形机器人在工业环境中执行负载搬运任务时面临的动态耦合与部分可观测性问题，提出了一种负载感知运动控制框架。框架采用解耦但协调的移动操作架构，通过强化学习策略在下肢运动学参考配置上生成残余关节动作。关键创新包括高度条件关节空间偏移引导学习、基于历史的状态估计器推断基座线速度和高度，以及将负载和操作引起的扰动编码为紧凑潜在表征。整个框架在仿真中完成训练，无需微调即可直接部署于全尺寸人形机器人。

## 核心内容
### 方法架构
- **解耦移动操作架构**：将上肢操作与下肢运动分离，通过强化学习策略在下肢运动学参考配置上生成残余关节动作，实现协调控制。
- **运动学参考生成**：基于高度条件关节空间偏移（height-conditioned joint offset）生成标称配置，引导策略学习。
- **状态估计器**：利用历史观测序列推断基座线速度和高度，并将负载和操作引起的动态扰动编码为紧凑潜在表征（latent representation）。

### 实验设置
- **训练**：完全在仿真环境中进行，使用强化学习算法训练下肢运动策略。
- **部署**：零样本（zero-shot）迁移至天工2.0 Pro全尺寸人形机器人，无需任何微调。
- **任务**：工业负载搬运和箱体操作任务，涉及不同负载重量和上肢运动。

### 关键结果
- **训练效率**：相比基线方法，训练速度更快（faster training）。
- **高度跟踪**：在仿真和真实实验中均实现精确的高度跟踪（accurate height tracking）。
- **稳定性**：在负载变化和上肢运动干扰下，保持稳定的移动操作（stable loco-manipulation）。
- **项目页面**：https://lequn-f.github.io/LALO/

## Overview
Humanoid robots deployed in industrial environments are required to perform load-carrying transportation tasks that tightly couple locomotion and manipulation. However, achieving stable and robust locomotion under varying payloads and upper-body motions is challenging due to dynamic coupling and partial observability. This paper presents a load-aware locomotion framework for industrial humanoids based on a decoupled yet coordinated loco-manipulation architecture. Lower-body locomotion is controlled via a reinforcement learning policy producing residual joint actions on kinematically derived nominal configurations. A kinematics-based locomotion reference with a height-conditioned joint-space offset guides learning, while a history-based state estimator infers base linear velocity and height and encodes residual load- and manipulation-induced disturbances in a compact latent representation. The framework is trained entirely in simulation and deployed on a full-size humanoid robot without fine-tuning. Simulation and real-world experiments demonstrate faster training, accurate height tracking, and stable loco-manipulation. Project page: https://lequn-f.github.io/LALO/

## 参考
- http://arxiv.org/abs/2603.14308v1

## 개요
본 연구는 인간형 로봇이 산업 환경에서 부하 운반 작업을 수행할 때 직면하는 동적 결합 및 부분 관측 가능성 문제를 해결하기 위해, 부하 인식 운동 제어 프레임워크를 제안한다. 해당 프레임워크는 분리되었지만 조화를 이루는 이동 조작 아키텍처를 채택하며, 강화 학습 정책을 통해 하지 운동학적 참조 구성에서 잔여 관절 동작을 생성한다. 핵심 혁신에는 높이 조건부 관절 공간 오프셋 기반 학습 유도, 과거 데이터를 활용한 상태 추정기를 통한 베이스 선속도 및 높이 추론, 그리고 부하 및 조작으로 인한 교란을 컴팩트한 잠재 표현으로 인코딩하는 방식이 포함된다. 전체 프레임워크는 시뮬레이션에서 훈련되며, 미세 조정 없이 전신 인간형 로봇에 직접 배포할 수 있다.

## 핵심 내용
### 방법 아키텍처
- **분리된 이동 조작 아키텍처**: 상지 조작과 하지 운동을 분리하고, 강화 학습 정책을 통해 하지 운동학적 참조 구성에서 잔여 관절 동작을 생성하여 조화로운 제어를 구현한다.
- **운동학적 참조 생성**: 높이 조건부 관절 공간 오프셋(height-conditioned joint offset)을 기반으로 표준 구성을 생성하여 정책 학습을 유도한다.
- **상태 추정기**: 과거 관측 시퀀스를 활용하여 베이스 선속도와 높이를 추론하고, 부하 및 조작으로 인한 동적 교란을 컴팩트한 잠재 표현(latent representation)으로 인코딩한다.

### 실험 설정
- **훈련**: 전적으로 시뮬레이션 환경에서 수행되며, 강화 학습 알고리즘을 사용하여 하지 운동 정책을 훈련한다.
- **배포**: 제로샷(zero-shot) 방식으로 Tiangong 2.0 Pro 전신 인간형 로봇에 전이되며, 어떠한 미세 조정도 필요하지 않다.
- **작업**: 산업용 부하 운반 및 상자 조작 작업으로, 다양한 부하 중량과 상지 운동을 포함한다.

### 주요 결과
- **훈련 효율성**: 기준 방법에 비해 더 빠른 훈련 속도(faster training)를 달성한다.
- **높이 추적**: 시뮬레이션 및 실제 실험 모두에서 정확한 높이 추적(accurate height tracking)을 구현한다.
- **안정성**: 부하 변화 및 상지 운동 간섭 하에서도 안정적인 이동 조작(stable loco-manipulation)을 유지한다.
- **프로젝트 페이지**: https://lequn-f.github.io/LALO/
