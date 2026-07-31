---
$id: ent_paper_kung_fu_athlete_bot_that_can_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'A Kung Fu Athlete Bot That Can Do It All Day: Highly Dynamic, Balance-Challenging Motion Dataset and Autonomous Fall-Resilient
    Tracking'
  zh: 'A Kung Fu Athlete Bot That Can Do It All Day: Highly Dynamic, Balance-Challenging Motion Dataset and Autonomous Fall-Resilient
    Tracking'
  ko: 'A Kung Fu Athlete Bot That Can Do It All Day: Highly Dynamic, Balance-Challenging Motion Dataset and Autonomous Fall-Resilient
    Tracking'
summary:
  en: 'Current humanoid motion tracking systems can execute routine and moderately dynamic behaviors, yet significant gaps
    remain near hardware performance limits and algorithmic robustness boundaries. Institutions per source list: 北京理工大学（BIT）、启元实验室（QIYUAN
    Lab）.'
  zh: 本文提出了KungFuAthlete，一个基于专业武术运动员日常训练视频构建的高动态武术动作数据集，包含地面和跳跃子集，其运动强度显著高于LAFAN1、PHUMA和AMASS等常用数据集。同时，作者提出了一种统一训练范式，使单一策略能同时学习高动态动作跟踪和摔倒恢复，从而提升人形机器人在极限动态场景下的鲁棒性和自主性。
  ko: 'Current humanoid motion tracking systems can execute routine and moderately dynamic behaviors, yet significant gaps
    remain near hardware performance limits and algorithmic robustness boundaries. Institutions per source list: 北京理工大学（BIT）、启元实验室（QIYUAN
    Lab）.'
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
- kung
- fu
- athlete
- bot
- that
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 684 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2602.13656 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2602.13656v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2602.13656 A Kung Fu Athlete Bot That Can Do It All Day: Highly Dynamic, Balance-Challenging Motion Dataset
    and Autonomous Fall-Resilient Tracking'
  url: https://arxiv.org/abs/2602.13656
  accessed_at: '2026-07-31'
  date: '2026-02-14'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

当前人形机器人运动跟踪系统能执行常规和中等动态行为，但在硬件性能极限和算法鲁棒性边界附近仍存在显著差距。武术作为高动态人体运动的极端案例，具有质心快速移动、复杂协调和突然姿态转换的特点，但针对此类高强度场景的数据集十分稀缺。为此，研究者从专业运动员日常训练视频中构建了KungFuAthlete数据集，包含地面和跳跃两个子集，覆盖代表性复杂运动模式。该数据集的跳跃子集在关节速度、线速度和角速度上均显著高于LAFAN1、PHUMA和AMASS等常用数据集，表明其运动强度和复杂度大幅提升。此外，即使专业运动员在高动态动作中也可能失败，人形机器人在外部干扰或执行错误下同样容易失稳摔倒。现有工作大多假设运动执行处于安全状态，缺乏对不安全状态建模和可靠自主恢复的统一策略。本文提出一种新训练范式，使单一策略能同时学习高动态运动跟踪和摔倒恢复，将敏捷执行与稳定控制统一在一个框架内，从而将机器人能力从纯运动跟踪扩展到带恢复能力的执行，推动人形机器人在真实高动态场景中实现更鲁棒和自主的表现。

## 核心内容
### 数据集构建
- **KungFuAthlete数据集**：从专业武术运动员的日常训练视频中提取，包含地面和跳跃两个子集，覆盖代表性复杂运动模式。
- **运动强度对比**：跳跃子集在关节速度、线速度和角速度上均显著高于LAFAN1、PHUMA和AMASS等常用数据集，表明其运动强度和复杂度大幅提升。

### 问题与挑战
- 现有系统假设运动执行始终处于安全状态，缺乏对不安全状态（如摔倒）的建模和自主恢复策略。
- 即使专业运动员在高动态动作中也可能失败，人形机器人在外部干扰或执行错误下同样容易失稳摔倒。

### 方法框架
- **统一训练范式**：提出一种新训练范式，使单一策略能同时学习高动态运动跟踪和摔倒恢复，将敏捷执行与稳定控制统一在一个框架内。
- **能力扩展**：该框架将机器人能力从纯运动跟踪扩展到带恢复能力的执行，促进人形机器人在真实高动态场景中实现更鲁棒和自主的表现。

### 实验设置与关键结果
- 实验基于KungFuAthlete数据集进行训练和评估，对比了常用数据集（LAFAN1、PHUMA、AMASS）的运动强度指标。
- 跳跃子集在关节速度、线速度和角速度上均显著高于对比数据集，验证了其高动态特性。
- 所提框架在跟踪高动态动作的同时，能有效处理摔倒状态并实现自主恢复，显著提升了系统的鲁棒性和自主性。

### 结论
本文通过构建高动态武术动作数据集KungFuAthlete，并设计统一训练范式，解决了人形机器人在极限动态场景下运动跟踪与摔倒恢复的难题，为更鲁棒和自主的人形机器人应用奠定了基础。

## Overview
Current humanoid motion tracking systems can execute routine and moderately dynamic behaviors, yet significant gaps remain near hardware performance limits and algorithmic robustness boundaries. Martial arts represent an extreme case of highly dynamic human motion, characterized by rapid center-of-mass shifts, complex coordination, and abrupt posture transitions. However, datasets tailored to such high-intensity scenarios remain scarce. To address this gap, we construct KungFuAthlete, a high-dynamic martial arts motion dataset derived from professional athletes' daily training videos. The dataset includes ground and jump subsets covering representative complex motion patterns. The jump subset exhibits substantially higher joint, linear, and angular velocities compared to commonly used datasets such as LAFAN1, PHUMA, and AMASS, indicating significantly increased motion intensity and complexity. Importantly, even professional athletes may fail during highly dynamic movements. Similarly, humanoid robots are prone to instability and falls under external disturbances or execution errors. Most prior work assumes motion execution remains within safe states and lacks a unified strategy for modeling unsafe states and enabling reliable autonomous recovery. We propose a novel training paradigm that enables a single policy to jointly learn high-dynamic motion tracking and fall recovery, unifying agile execution and stabilization within one framework. This framework expands robotic capability from pure motion tracking to recovery-enabled execution, promoting more robust and autonomous humanoid performance in real-world high-dynamic scenarios.

## 参考
- https://arxiv.org/abs/2602.13656
- https://github.com/ImChong/Robotics_Notebooks

## 개요

현재 인간형 로봇 운동 추적 시스템은 일반적이고 중간 수준의 동적 행동을 수행할 수 있지만, 하드웨어 성능 한계와 알고리즘 강건성 경계 부근에서는 여전히 상당한 격차가 존재합니다. 무술은 고동적 인간 운동의 극단적인 사례로, 질량 중심의 빠른 이동, 복잡한 협응 및 갑작스러운 자세 전환이 특징이지만, 이러한 고강도 시나리오에 대한 데이터셋은 매우 부족합니다. 이에 연구자들은 전문 운동선수의 일상 훈련 비디오에서 KungFuAthlete 데이터셋을 구축했으며, 지상과 점프 두 가지 하위 집합을 포함하여 대표적인 복잡한 운동 패턴을 다룹니다. 이 데이터셋의 점프 하위 집합은 관절 속도, 선속도 및 각속도에서 LAFAN1, PHUMA, AMASS 등 일반적인 데이터셋보다 현저히 높아, 운동 강도와 복잡성이 크게 향상되었음을 나타냅니다. 또한, 전문 운동선수도 고동적 동작에서 실패할 수 있으며, 인간형 로봇은 외부 간섭이나 실행 오류로 인해 쉽게 불안정해져 넘어질 수 있습니다. 기존 연구는 대부분 운동 실행이 안전한 상태에 있다고 가정하며, 불안전 상태 모델링과 신뢰할 수 있는 자율 복구에 대한 통합 전략이 부족합니다. 본 논문은 단일 전략이 고동적 운동 추적과 넘어짐 복구를 동시에 학습할 수 있는 새로운 훈련 패러다임을 제안하여, 민첩한 실행과 안정적인 제어를 하나의 프레임워크로 통합함으로써 로봇 능력을 순수 운동 추적에서 복구 능력을 갖춘 실행으로 확장하고, 인간형 로봇이 실제 고동적 시나리오에서 더 강건하고 자율적인 성능을 발휘하도록 촉진합니다.

## 핵심 내용
### 데이터셋 구축
- **KungFuAthlete 데이터셋**: 전문 무술 운동선수의 일상 훈련 비디오에서 추출되었으며, 지상과 점프 두 가지 하위 집합을 포함하여 대표적인 복잡한 운동 패턴을 다룹니다.
- **운동 강도 비교**: 점프 하위 집합은 관절 속도, 선속도 및 각속도에서 LAFAN1, PHUMA, AMASS 등 일반적인 데이터셋보다 현저히 높아, 운동 강도와 복잡성이 크게 향상되었음을 나타냅니다.

### 문제와 도전 과제
- 기존 시스템은 운동 실행이 항상 안전한 상태에 있다고 가정하며, 불안전 상태(예: 넘어짐)에 대한 모델링과 자율 복구 전략이 부족합니다.
- 전문 운동선수도 고동적 동작에서 실패할 수 있으며, 인간형 로봇은 외부 간섭이나 실행 오류로 인해 쉽게 불안정해져 넘어질 수 있습니다.

### 방법 프레임워크
- **통합 훈련 패러다임**: 단일 전략이 고동적 운동 추적과 넘어짐 복구를 동시에 학습할 수 있는 새로운 훈련 패러다임을 제안하여, 민첩한 실행과 안정적인 제어를 하나의 프레임워크로 통합합니다.
- **능력 확장**: 이 프레임워크는 로봇 능력을 순수 운동 추적에서 복구 능력을 갖춘 실행으로 확장하여, 인간형 로봇이 실제 고동적 시나리오에서 더 강건하고 자율적인 성능을 발휘하도록 촉진합니다.

### 실험 설정 및 주요 결과
- 실험은 KungFuAthlete 데이터셋을 기반으로 훈련 및 평가가 수행되었으며, 일반적인 데이터셋(LAFAN1, PHUMA, AMASS)의 운동 강도 지표와 비교되었습니다.
- 점프 하위 집합은 관절 속도, 선속도 및 각속도에서 비교 데이터셋보다 현저히 높아, 고동적 특성을 검증했습니다.
- 제안된 프레임워크는 고동적 동작을 추적하는 동시에 넘어짐 상태를 효과적으로 처리하고 자율 복구를 구현하여, 시스템의 강건성과 자율성을 크게 향상시켰습니다.

### 결론
본 논문은 고동적 무술 동작 데이터셋 KungFuAthlete를 구축하고 통합 훈련 패러다임을 설계함으로써, 인간형 로봇의 극한 동적 시나리오에서 운동 추적과 넘어짐 복구의 문제를 해결하여, 더 강건하고 자율적인 인간형 로봇 응용을 위한 기반을 마련했습니다.
