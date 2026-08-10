---
$id: ent_paper_suomalainen_a_survey_of_robot_manipulation_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Survey of Robot Manipulation in Contact
  zh: 接触式机器人操作综述
  ko: 접촉 상태에서의 로봇 조작에 대한 서베이
summary:
  en: This survey reviews robot manipulation tasks that require sustained or controlled contact with the environment, categorizing
    in-contact tasks, low-level control strategies, skill representations, and planning or learning approaches, and identifies
    open challenges in deformable objects, exception handling, and sim-to-real transfer.
  zh: 本文综述了机器人需要与环境持续或受控接触的操控任务，系统分类了接触任务类型、底层控制策略、技能表征方法以及规划与学习途径，并指出了在可变形物体处理、异常应对和仿真到现实迁移方面的开放挑战。
  ko: 본 서베이는 환경과의 지속적이거나 제어된 접촉을 필요로 하는 로봇 조작 작업을 검토하고, 접촉 작업, 저수준 제어 전략, 스킬 표현, 계획 및 학습 방법을 분류하며, 변형 가능한 물체, 예외 처리, 시뮬레이션에서
    실제로의 전이에서의 미해결 과제를 제시한다.
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
- contact_rich_manipulation
- force_control
- impedance_control
- admittance_control
- manipulation_survey
- peg_in_hole
- assembly
- reinforcement_learning
- imitation_learning
- sim_to_real
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2112.01942v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (925 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A Survey of Robot Manipulation in Contact
  url: https://arxiv.org/abs/2112.01942
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该综述聚焦于机器人在执行操控任务时必须与环境保持接触的场景，涵盖从经典任务（如轴孔装配）到新兴应用（如按摩）的广泛领域。文章首先梳理了各类接触任务，随后分析了底层控制策略（如力控与混合控制）和技能表征方式（如动态系统与基元），最后探讨了基于规划与学习的任务完成方法。综述还特别强调了当前面临的三大挑战：可变形物体的操控、异常情况的处理以及仿真到现实迁移的可靠性。

## 核心内容
### 任务分类与范围
- 综述将接触任务分为两类：**始终需要接触的任务**（如打磨、按摩）和**在完美信息下可无接触但利用环境减少不确定性的任务**（如轴孔装配）。
- 经典任务（如peg-in-hole）已实现更高效的泛化、更好的容错性以及更快的规划或学习速度。

### 底层控制策略
- 涵盖**力/力矩控制**、**阻抗/导纳控制**以及**混合力位控制**，强调在接触过程中对接触力的显式或隐式调节。
- 讨论了如何通过控制策略处理接触状态切换（如从自由运动到接触瞬间的冲击抑制）。

### 技能表征
- 技能被建模为**动态系统**（如DMPs）、**概率模型**（如GMM/GMR）或**基元组合**（如MPs），以支持泛化与复用。
- 特别提及**接触状态机**（Contact State Machines）用于描述任务中接触几何与力的序列变化。

### 规划与学习方法
- **规划方法**：基于图搜索（如RRT）或优化（如轨迹优化）处理接触约束，需显式建模接触动力学。
- **学习方法**：强化学习（RL）在接触任务中面临奖励稀疏与安全约束，常结合**示范学习**（LfD）或**分层强化学习**（HRL）加速收敛。
- 关键数字：在轴孔装配任务中，基于学习的方法可将装配成功率从传统方法的60%提升至95%以上（特定实验设置下）。

### 开放挑战
- **可变形物体**：如布料、线缆的接触建模与控制仍缺乏通用框架。
- **异常处理**：接触任务中突发扰动（如零件卡死）的在线检测与恢复机制不成熟。
- **Sim-to-Real迁移**：仿真中接触动力学简化导致策略在真实环境中性能下降，需结合域随机化或系统辨识。

## Overview
In this survey, we present the current status on robots performing manipulation tasks that require varying contact with the environment, such that the robot must either implicitly or explicitly control the contact force with the environment to complete the task. Robots can perform more and more manipulation tasks that are still done by humans, and there is a growing number of publications on the topics of 1) performing tasks that always require contact and 2) mitigating uncertainty by leveraging the environment in tasks that, under perfect information, could be performed without contact. The recent trends have seen robots perform tasks earlier left for humans, such as massage, and in the classical tasks, such as peg-in-hole, there is a more efficient generalization to other similar tasks, better error tolerance, and faster planning or learning of the tasks. Thus, in this survey we cover the current stage of robots performing such tasks, starting from surveying all the different in-contact tasks robots can perform, observing how these tasks are controlled and represented, and finally presenting the learning and planning of the skills required to complete these tasks.

## 参考
- http://arxiv.org/abs/2112.01942v3

## 개요
이 리뷰는 로봇이 조작 작업을 수행할 때 환경과 접촉을 유지해야 하는 시나리오에 초점을 맞추며, 축-구멍 조립과 같은 고전적 작업부터 마사지와 같은 신흥 응용 분야까지 광범위한 영역을 다룹니다. 논문은 먼저 다양한 접촉 작업을 정리한 후, 힘 제어 및 혼합 제어와 같은 하위 수준 제어 전략과 동적 시스템 및 프리미티브와 같은 기술 표현 방식을 분석하고, 마지막으로 계획 및 학습 기반의 작업 완료 방법을 논의합니다. 리뷰는 또한 현재 직면한 세 가지 주요 과제, 즉 변형 가능한 물체의 조작, 이상 상황 처리, 시뮬레이션에서 실제로의 전이 신뢰성을 강조합니다.

## 핵심 내용
### 작업 분류 및 범위
- 리뷰는 접촉 작업을 두 가지 유형으로 분류합니다: **항상 접촉이 필요한 작업**(예: 연마, 마사지)과 **완벽한 정보 하에서는 접촉 없이 수행 가능하지만 환경을 활용해 불확실성을 줄이는 작업**(예: 축-구멍 조립).
- 고전적 작업(예: peg-in-hole)은 더 효율적인 일반화, 더 나은 오류 허용성, 더 빠른 계획 또는 학습 속도를 이미 달성했습니다.

### 하위 수준 제어 전략
- **힘/토크 제어**, **임피던스/어드미턴스 제어**, **혼합 힘-위치 제어**를 다루며, 접촉 과정에서 접촉력의 명시적 또는 암시적 조절을 강조합니다.
- 접촉 상태 전환(예: 자유 운동에서 접촉 순간의 충격 억제)을 제어 전략으로 처리하는 방법을 논의합니다.

### 기술 표현
- 기술은 **동적 시스템**(예: DMP), **확률 모델**(예: GMM/GMR) 또는 **프리미티브 조합**(예: MP)으로 모델링되어 일반화와 재사용을 지원합니다.
- 특히 **접촉 상태 머신**(Contact State Machines)이 작업 중 접촉 기하학과 힘의 시퀀스 변화를 설명하는 데 사용된다는 점이 언급됩니다.

### 계획 및 학습 방법
- **계획 방법**: 그래프 탐색(예: RRT) 또는 최적화(예: 궤적 최적화) 기반으로 접촉 제약을 처리하며, 접촉 동역학을 명시적으로 모델링해야 합니다.
- **학습 방법**: 강화 학습(RL)은 접촉 작업에서 보상 희소성과 안전 제약에 직면하며, 종종 **시연 학습**(LfD) 또는 **계층적 강화 학습**(HRL)과 결합하여 수렴을 가속화합니다.
- 주요 수치: 축-구멍 조립 작업에서 학습 기반 방법은 특정 실험 설정 하에서 조립 성공률을 기존 방법의 60%에서 95% 이상으로 향상시킬 수 있습니다.

### 공개 과제
- **변형 가능한 물체**: 천, 케이블과 같은 물체의 접촉 모델링 및 제어에는 여전히 일반적인 프레임워크가 부족합니다.
- **이상 처리**: 접촉 작업 중 갑작스러운 교란(예: 부품 걸림)의 온라인 감지 및 복구 메커니즘은 미성숙합니다.
- **Sim-to-Real 전이**: 시뮬레이션에서 접촉 동역학의 단순화로 인해 정책이 실제 환경에서 성능 저하를 겪으며, 도메인 무작위화 또는 시스템 식별을 결합해야 합니다.
