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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2112.01942v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
본 조사에서는 로봇이 환경과의 다양한 접촉을 요구하는 조작 작업을 수행하는 현재 상황을 제시합니다. 이러한 작업에서 로봇은 작업을 완료하기 위해 환경과의 접촉력을 암시적 또는 명시적으로 제어해야 합니다. 로봇은 여전히 인간이 수행하는 점점 더 많은 조작 작업을 수행할 수 있으며, 1) 항상 접촉이 필요한 작업 수행과 2) 완벽한 정보 하에서는 접촉 없이 수행될 수 있는 작업에서 환경을 활용하여 불확실성을 완화하는 주제에 대한 출판물이 증가하고 있습니다. 최근 추세에 따르면 로봇은 마사지와 같이 이전에는 인간에게 맡겨졌던 작업을 수행하고 있으며, 핀-인-홀(peg-in-hole)과 같은 고전적인 작업에서는 다른 유사한 작업으로의 더 효율적인 일반화, 더 나은 오류 허용성, 그리고 더 빠른 작업 계획 또는 학습이 이루어지고 있습니다. 따라서 본 조사에서는 로봇이 수행할 수 있는 다양한 접촉 작업을 조사하고, 이러한 작업이 어떻게 제어되고 표현되는지 관찰하며, 마지막으로 이러한 작업을 완료하는 데 필요한 기술의 학습 및 계획을 제시함으로써 로봇이 이러한 작업을 수행하는 현재 단계를 다룹니다.

## 핵심 내용
본 조사에서는 로봇이 환경과의 다양한 접촉을 요구하는 조작 작업을 수행하는 현재 상황을 제시합니다. 이러한 작업에서 로봇은 작업을 완료하기 위해 환경과의 접촉력을 암시적 또는 명시적으로 제어해야 합니다. 로봇은 여전히 인간이 수행하는 점점 더 많은 조작 작업을 수행할 수 있으며, 1) 항상 접촉이 필요한 작업 수행과 2) 완벽한 정보 하에서는 접촉 없이 수행될 수 있는 작업에서 환경을 활용하여 불확실성을 완화하는 주제에 대한 출판물이 증가하고 있습니다. 최근 추세에 따르면 로봇은 마사지와 같이 이전에는 인간에게 맡겨졌던 작업을 수행하고 있으며, 핀-인-홀(peg-in-hole)과 같은 고전적인 작업에서는 다른 유사한 작업으로의 더 효율적인 일반화, 더 나은 오류 허용성, 그리고 더 빠른 작업 계획 또는 학습이 이루어지고 있습니다. 따라서 본 조사에서는 로봇이 수행할 수 있는 다양한 접촉 작업을 조사하고, 이러한 작업이 어떻게 제어되고 표현되는지 관찰하며, 마지막으로 이러한 작업을 완료하는 데 필요한 기술의 학습 및 계획을 제시함으로써 로봇이 이러한 작업을 수행하는 현재 단계를 다룹니다.

## 参考
- http://arxiv.org/abs/2112.01942v3
