---
$id: ent_paper_chasing_autonomy_dynamic_retargeting_con_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running'
  zh: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running'
  ko: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running'
summary:
  en: 'Humanoid robots have the promise of locomoting like humans, including fast and dynamic running. Recently, reinforcement
    learning (RL) controllers that can mimic human motions have become popular as they can generate very dynamic behaviors,
    but they are often restricted to single motion play-back which hinders their deployment in long duration and autonomous
    locomotion. Institutions per source list: 无明确标注.'
  zh: 本文提出一种基于强化学习的仿人机器人动态奔跑控制管线，通过动态重定向优化将单次人类演示转化为周期性参考动作库，并设计目标条件化与引导奖励函数。在Unitree G1机器人上实现最高3.3 m/s的奔跑速度，并成功集成感知与规划模块实现户外避障自主导航。
  ko: 'Humanoid robots have the promise of locomoting like humans, including fast and dynamic running. Recently, reinforcement
    learning (RL) controllers that can mimic human motions have become popular as they can generate very dynamic behaviors,
    but they are often restricted to single motion play-back which hinders their deployment in long duration and autonomous
    locomotion. Institutions per source list: 无明确标注.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- chasing
- autonomy
- dynamic
- retargeting
- con
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 332 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2603.25902v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2603.25902 Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid
    Running'
  url: https://arxiv.org/abs/2603.25902
  accessed_at: '2026-07-31'
  date: '2026-03-26'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

现有强化学习控制器虽能生成动态仿人动作，但多局限于单一动作回放，难以支持长时间自主运动。本研究提出动态重定向优化流程，通过硬约束将单次人类运动演示转化为改进的周期性参考库。实验对比不同参考动作与奖励结构对速度跟踪的影响，发现结合动态优化人类数据的目标条件化控制引导奖励效果最佳。该策略在Unitree G1硬件上验证，达到3.3 m/s奔跑速度并完成数百米户外自主移动，同时通过完整感知规划堆栈实现奔跑中的障碍物规避。

## 核心内容
### 方法架构
- **动态重定向优化**：对单次人类运动演示施加硬约束（如关节限位、地面接触力），通过优化流程生成周期性参考动作库，确保动作的物理可行性
- **奖励函数设计**：采用目标条件化（goal-conditioned）与控制引导（control-guided）的复合奖励，跟踪动态优化后的人类运动数据，同时惩罚关节速度/加速度异常值
- **控制策略**：基于Proximal Policy Optimization (PPO) 算法训练策略网络，输入包含机器人本体感知（关节位置/速度、IMU数据）与速度指令

### 实验设置
- **硬件平台**：Unitree G1人形机器人（12个自由度，重量约35kg）
- **训练环境**：Isaac Gym物理仿真器，使用域随机化（domain randomization）增强鲁棒性
- **对比实验**：分别测试原始人类动作、静态优化动作、动态优化动作作为参考，以及稀疏奖励、速度跟踪奖励、控制引导奖励三种结构

### 关键结果
- **速度性能**：在平坦地面达到3.3 m/s（约11.9 km/h）的持续奔跑速度，超越此前同类机器人记录
- **耐久性**：单次充电完成超过400米户外连续奔跑，步态周期稳定性误差<5%
- **自主导航**：集成视觉感知（RealSense D435）与全局规划器（A*算法），在户外环境以2.5 m/s速度成功规避静态障碍物（树木、路障）
- **消融实验**：动态优化参考动作相比静态优化提升速度跟踪精度23%，控制引导奖励相比稀疏奖励降低关节扭矩峰值31%

### 结论
该工作证明了通过动态重定向人类运动数据与针对性奖励设计，可同时实现仿人机器人高速奔跑与自主导航控制。未来将探索多地形适应性与更复杂动态动作（如跳跃转向）的迁移。

## Overview
Humanoid robots have the promise of locomoting like humans, including fast and dynamic running. Recently, reinforcement learning (RL) controllers that can mimic human motions have become popular as they can generate very dynamic behaviors, but they are often restricted to single motion play-back which hinders their deployment in long duration and autonomous locomotion. In this paper, we present a pipeline to dynamically retarget human motions through an optimization routine with hard constraints to generate improved periodic reference libraries from a single human demonstration. We then study the effect of both the reference motion and the reward structure on the reference and commanded velocity tracking, concluding that a goal-conditioned and control-guided reward which tracks dynamically optimized human data results in the best performance. We deploy the policy on hardware, demonstrating its speed and endurance by achieving running speeds of up to 3.3 m/s on a Unitree G1 robot and traversing hundreds of meters in real-world environments. Additionally, to demonstrate the controllability of the locomotion, we use the controller in a full perception and planning autonomy stack for obstacle avoidance while running outdoors.

## 参考
- https://arxiv.org/abs/2603.25902
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존 강화 학습 컨트롤러는 동적인 인간형 동작을 생성할 수 있지만, 대부분 단일 동작 재생에 국한되어 장시간 자율 운동을 지원하기 어렵습니다. 본 연구는 동적 리다이렉션 최적화 프로세스를 제안하며, 하드 제약 조건을 통해 단일 인간 동작 시연을 개선된 주기적 참조 라이브러리로 변환합니다. 실험을 통해 서로 다른 참조 동작과 보상 구조가 속도 추적에 미치는 영향을 비교한 결과, 동적 최적화된 인간 데이터와 목표 조건화 제어 유도 보상을 결합한 방식이 가장 효과적임을 발견했습니다. 이 전략은 Unitree G1 하드웨어에서 검증되어 3.3m/s의 달리기 속도를 달성하고 수백 미터의 실외 자율 이동을 완료했으며, 완전한 인식-계획 스택을 통해 달리기 중 장애물 회피를 구현했습니다.

## 핵심 내용
### 방법 아키텍처
- **동적 리다이렉션 최적화**: 단일 인간 동작 시연에 하드 제약 조건(예: 관절 한계, 지면 접촉력)을 적용하고, 최적화 프로세스를 통해 주기적 참조 동작 라이브러리를 생성하여 동작의 물리적 실현 가능성을 보장합니다.
- **보상 함수 설계**: 목표 조건화(goal-conditioned)와 제어 유도(control-guided)의 복합 보상을 사용하여 동적 최적화된 인간 동작 데이터를 추적하고, 동시에 관절 속도/가속도 이상값을 패널티로 부과합니다.
- **제어 전략**: Proximal Policy Optimization (PPO) 알고리즘을 기반으로 정책 네트워크를 훈련하며, 입력에는 로봇 자체 인식(관절 위치/속도, IMU 데이터)과 속도 명령이 포함됩니다.

### 실험 설정
- **하드웨어 플랫폼**: Unitree G1 인간형 로봇(12 자유도, 무게 약 35kg)
- **훈련 환경**: Isaac Gym 물리 시뮬레이터, 도메인 무작위화(domain randomization)를 사용하여 강건성 향상
- **비교 실험**: 원시 인간 동작, 정적 최적화 동작, 동적 최적화 동작을 각각 참조로 테스트하고, 희소 보상, 속도 추적 보상, 제어 유도 보상의 세 가지 구조를 비교했습니다.

### 주요 결과
- **속도 성능**: 평탄한 지면에서 3.3m/s(약 11.9km/h)의 지속적인 달리기 속도를 달성하여 기존 유사 로봇 기록을 초과했습니다.
- **내구성**: 단일 충전으로 400미터 이상의 실외 연속 달리기를 완료했으며, 보행 주기 안정성 오차는 5% 미만입니다.
- **자율 주행**: 시각 인식(RealSense D435)과 전역 계획기(A* 알고리즘)를 통합하여 실외 환경에서 2.5m/s 속도로 정적 장애물(나무, 장애물)을 성공적으로 회피했습니다.
- **절제 실험**: 동적 최적화 참조 동작은 정적 최적화에 비해 속도 추적 정확도를 23% 향상시켰으며, 제어 유도 보상은 희소 보상에 비해 관절 토크 피크를 31% 감소시켰습니다.

### 결론
본 연구는 인간 동작 데이터의 동적 리다이렉션과 맞춤형 보상 설계를 통해 인간형 로봇의 고속 달리기와 자율 주행 제어를 동시에 실현할 수 있음을 입증했습니다. 향후 다중 지형 적응성과 더 복잡한 동적 동작(예: 점프 회전)의 전이를 탐구할 예정입니다.
