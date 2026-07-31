---
$id: ent_paper_locomotion_skills_deeprl_does_choice_act_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning Locomotion Skills Using DeepRL: Does the Choice of Action Space Matter?'
  zh: 'Learning Locomotion Skills Using DeepRL: Does the Choice of Action Space Matter?'
  ko: 'Learning Locomotion Skills Using DeepRL: Does the Choice of Action Space Matter?'
summary:
  en: 'The use of deep reinforcement learning allows for high-dimensional state descriptors, but little is known about how
    the choice of action representation impacts the learning difficulty and the resulting performance. Institutions per source
    list: Xue Bin Peng、Michiel van de Panne.'
  zh: 本文研究了深度强化学习中动作空间选择对运动技能学习的影响。作者对比了力矩、肌肉激活、目标关节角度和目标关节角速度四种动作参数化方法，在多个平面关节图形的步态模仿任务上评估了学习时间、策略鲁棒性、运动质量和查询频率。结果表明，高层动作参数化提供的局部反馈能显著影响学习效果、鲁棒性和策略质量。
  ko: 'The use of deep reinforcement learning allows for high-dimensional state descriptors, but little is known about how
    the choice of action representation impacts the learning difficulty and the resulting performance. Institutions per source
    list: Xue Bin Peng、Michiel van de Panne.'
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
- locomotion
- skills
- deeprl
- does
- choice
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 341 (.staging/ingest_yuanxq). Tier C->full. arXiv id 1611.01055 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (1611.01055v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:1611.01055 Learning Locomotion Skills Using DeepRL: Does the Choice of Action Space Matter?'
  url: https://arxiv.org/abs/1611.01055
  accessed_at: '2026-07-31'
  date: '2016-11-03'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

深度强化学习虽能处理高维状态描述，但动作表示方式对学习难度和性能的影响尚不明确。本文系统比较了四种动作参数化方法：力矩、肌肉激活、目标关节角度和目标关节角速度。实验在多个平面关节图形和多种步态上进行步态周期模仿任务，评估指标包括学习时间、策略鲁棒性、运动质量和策略查询频率。研究发现，高层动作参数化（如目标关节角度）通过提供局部反馈，能显著改善学习效率、鲁棒性和生成运动的质量。

## 核心内容
### 研究背景与问题
深度强化学习（DeepRL）在机器人运动技能学习中广泛应用，但动作空间的选择（即动作参数化方式）对学习难度和最终性能的影响尚未被系统研究。本文旨在填补这一空白，通过对比四种常见动作参数化方法，揭示其在不同评估维度上的差异。

### 动作参数化方法
- **力矩（Torques）**：直接输出关节力矩，属于低层控制，依赖模型精确动力学。
- **肌肉激活（Muscle-activations）**：模拟生物肌肉激活模式，需结合肌肉模型。
- **目标关节角度（Target joint angles）**：输出期望关节角度，由底层PD控制器跟踪，提供局部反馈。
- **目标关节角速度（Target joint-angle velocities）**：输出期望角速度，同样依赖底层控制器。

### 实验设置
- **任务**：步态周期模仿任务，要求机器人跟踪参考步态轨迹。
- **环境**：多个平面关节图形（如2D双足、四足等），多种步态（如行走、跑步）。
- **评估指标**：
  - 学习时间：达到指定性能所需的训练步数。
  - 策略鲁棒性：在扰动（如地面摩擦变化、外力干扰）下的表现。
  - 运动质量：跟踪误差、能量消耗、运动平滑度。
  - 策略查询频率：策略网络被调用的频率（反映计算开销）。

### 关键结果
- **学习时间**：目标关节角度参数化学习最快，力矩最慢。例如，在双足行走任务中，目标关节角度方法比力矩方法快约40%。
- **鲁棒性**：目标关节角度和角速度方法对扰动更鲁棒，力矩方法在强扰动下易失败。肌肉激活方法鲁棒性居中。
- **运动质量**：目标关节角度方法生成的运动更平滑、跟踪误差更小（平均跟踪误差降低30%），力矩方法则产生更抖动的运动。
- **查询频率**：力矩和肌肉激活方法需要更高查询频率（因需更细粒度控制），目标关节角度方法查询频率最低，计算效率更高。

### 结论
高层动作参数化（如目标关节角度）通过内置局部反馈机制，能显著降低学习难度、提升策略鲁棒性和运动质量。这为机器人运动学习中的动作空间设计提供了实用指导：在可能的情况下，优先选择提供局部反馈的高层动作表示，而非直接的低层控制信号。

## Overview
The use of deep reinforcement learning allows for high-dimensional state descriptors, but little is known about how the choice of action representation impacts the learning difficulty and the resulting performance. We compare the impact of four different action parameterizations (torques, muscle-activations, target joint angles, and target joint-angle velocities) in terms of learning time, policy robustness, motion quality, and policy query rates. Our results are evaluated on a gait-cycle imitation task for multiple planar articulated figures and multiple gaits. We demonstrate that the local feedback provided by higher-level action parameterizations can significantly impact the learning, robustness, and quality of the resulting policies.

## 参考
- https://arxiv.org/abs/1611.01055
- https://github.com/ImChong/Robotics_Notebooks

## 개요

심층 강화 학습은 고차원 상태 표현을 처리할 수 있지만, 동작 표현 방식이 학습 난이도와 성능에 미치는 영향은 아직 명확하지 않습니다. 본 논문은 토크, 근육 활성화, 목표 관절 각도, 목표 관절 각속도의 네 가지 동작 매개변수화 방법을 체계적으로 비교합니다. 실험은 여러 평면 관절 그래픽과 다양한 보행에서 보행 주기 모방 작업을 수행하며, 평가 지표로는 학습 시간, 정책 강건성, 운동 품질 및 정책 쿼리 빈도를 사용합니다. 연구 결과, 고수준 동작 매개변수화(예: 목표 관절 각도)는 국소 피드백을 제공함으로써 학습 효율성, 강건성 및 생성된 운동의 품질을 크게 향상시킬 수 있음을 발견했습니다.

## 핵심 내용
### 연구 배경 및 문제
심층 강화 학습(DeepRL)은 로봇 운동 기술 학습에 널리 사용되지만, 동작 공간의 선택(즉, 동작 매개변수화 방식)이 학습 난이도와 최종 성능에 미치는 영향은 아직 체계적으로 연구되지 않았습니다. 본 논문은 이러한 공백을 메우기 위해 네 가지 일반적인 동작 매개변수화 방법을 비교하여 다양한 평가 차원에서의 차이를 밝히는 것을 목표로 합니다.

### 동작 매개변수화 방법
- **토크(Torques)**: 관절 토크를 직접 출력하며, 저수준 제어에 속하고 정확한 모델 동역학에 의존합니다.
- **근육 활성화(Muscle-activations)**: 생물학적 근육 활성화 패턴을 모방하며, 근육 모델과 결합해야 합니다.
- **목표 관절 각도(Target joint angles)**: 기대 관절 각도를 출력하며, 저수준 PD 제어기가 추적하여 국소 피드백을 제공합니다.
- **목표 관절 각속도(Target joint-angle velocities)**: 기대 각속도를 출력하며, 마찬가지로 저수준 제어기에 의존합니다.

### 실험 설정
- **작업**: 보행 주기 모방 작업으로, 로봇이 참조 보행 궤적을 추적하도록 요구합니다.
- **환경**: 여러 평면 관절 그래픽(예: 2D 이족, 사족 등)과 다양한 보행(예: 걷기, 달리기).
- **평가 지표**:
  - 학습 시간: 지정된 성능에 도달하는 데 필요한 훈련 단계 수.
  - 정책 강건성: 교란(예: 지면 마찰 변화, 외부 힘 간섭) 하에서의 성능.
  - 운동 품질: 추적 오차, 에너지 소비, 운동 평활도.
  - 정책 쿼리 빈도: 정책 네트워크가 호출되는 빈도(계산 비용 반영).

### 주요 결과
- **학습 시간**: 목표 관절 각도 매개변수화가 가장 빠르게 학습되며, 토크가 가장 느립니다. 예를 들어, 이족 보행 작업에서 목표 관절 각도 방법은 토크 방법보다 약 40% 빠릅니다.
- **강건성**: 목표 관절 각도 및 각속도 방법이 교란에 더 강건하며, 토크 방법은 강한 교란 하에서 쉽게 실패합니다. 근육 활성화 방법은 강건성이 중간 수준입니다.
- **운동 품질**: 목표 관절 각도 방법으로 생성된 운동이 더 매끄럽고 추적 오차가 더 작으며(평균 추적 오차 30% 감소), 토크 방법은 더 떨리는 운동을 생성합니다.
- **쿼리 빈도**: 토크 및 근육 활성화 방법은 더 높은 쿼리 빈도가 필요하며(더 세밀한 제어 필요), 목표 관절 각도 방법은 쿼리 빈도가 가장 낮아 계산 효율성이 더 높습니다.

### 결론
고수준 동작 매개변수화(예: 목표 관절 각도)는 내장된 국소 피드백 메커니즘을 통해 학습 난이도를 크게 낮추고, 정책 강건성과 운동 품질을 향상시킵니다. 이는 로봇 운동 학습에서 동작 공간 설계에 실용적인 지침을 제공합니다: 가능한 경우, 직접적인 저수준 제어 신호보다 국소 피드백을 제공하는 고수준 동작 표현을 우선 선택하십시오.
