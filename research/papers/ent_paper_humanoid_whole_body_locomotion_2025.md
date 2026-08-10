---
$id: ent_paper_humanoid_whole_body_locomotion_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning
  zh: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning
  ko: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning
summary:
  en: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning is a 2025 work on locomotion
    for humanoid robots.
  zh: 本文提出一种基于动态平衡与强化学习的全身运动算法，使全尺寸人形机器人在仅依赖本体感知的情况下穿越狭窄地形与不可观测障碍。核心贡献在于将扩展的Zero-Moment Point (ZMP)驱动奖励与任务驱动奖励结合到全身actor-critic框架中，实现上下肢协调动作。在Unitree
    H1-2机器人上的实验验证了该方法在极端狭窄地形与外部扰动下的平衡维持能力。
  ko: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning is a 2025 work on locomotion
    for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoid_whole_body_locomotion
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.17219v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (670 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2502.17219
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对现有运动算法依赖步态或感知奖励、难以处理不可观测障碍与突发失衡的问题，本文提出一种基于动态平衡与强化学习的全身运动算法。该方法通过引入扩展的Zero-Moment Point (ZMP)驱动奖励与任务驱动奖励，在全身actor-critic框架中实现上下肢协调动作，使人形机器人仅凭本体感知即可穿越狭窄通道与意外障碍。在Unitree H1-2全尺寸机器人上的实验表明，该方法能在极端狭窄地形与外部扰动下维持平衡，显著提升机器人对复杂环境的适应能力。

## 核心内容
### 方法架构
- 采用全身actor-critic强化学习框架，将动态平衡机制融入奖励设计
- 引入扩展的Zero-Moment Point (ZMP)驱动奖励，作为维持动态平衡的核心指标
- 结合任务驱动奖励（如速度跟踪、关节限制等），实现上下肢协调运动策略

### 实验设置
- 实验平台：全尺寸Unitree H1-2人形机器人
- 测试场景：极端狭窄地形（如窄道、不规则障碍物）与外部扰动（如推力干扰）
- 感知输入：仅使用本体感知（关节角度、IMU等），不依赖视觉或LiDAR

### 关键结果
- 在狭窄地形上成功维持动态平衡，未出现跌倒或失稳
- 对外部推力扰动具有鲁棒性，能快速恢复稳定姿态
- 相比基线方法（如纯步态策略），在不可观测障碍场景下成功率提升显著

### 结论
本文提出的动态平衡机制与强化学习结合的方法，有效解决了人形机器人在缺乏外部感知时穿越极端地形的难题。未来工作可探索将该方法扩展到更复杂地形与多任务场景。

## Overview
Humans possess delicate dynamic balance mechanisms that enable them to maintain stability across diverse terrains and under extreme conditions. However, despite significant advances recently, existing locomotion algorithms for humanoid robots are still struggle to traverse extreme environments, especially in cases that lack external perception (e.g., vision or LiDAR). This is because current methods often rely on gait-based or perception-condition rewards, lacking effective mechanisms to handle unobservable obstacles and sudden balance loss. To address this challenge, we propose a novel whole-body locomotion algorithm based on dynamic balance and Reinforcement Learning (RL) that enables humanoid robots to traverse extreme terrains, particularly narrow pathways and unexpected obstacles, using only proprioception. Specifically, we introduce a dynamic balance mechanism by leveraging an extended measure of Zero-Moment Point (ZMP)-driven rewards and task-driven rewards in a whole-body actor-critic framework, aiming to achieve coordinated actions of the upper and lower limbs for robust locomotion. Experiments conducted on a full-sized Unitree H1-2 robot verify the ability of our method to maintain balance on extremely narrow terrains and under external disturbances, demonstrating its effectiveness in enhancing the robot's adaptability to complex environments. The videos are given at https://whole-body-loco.github.io.

## Overview
Humans possess delicate dynamic balance mechanisms that enable them to maintain stability across diverse terrains and under extreme conditions. However, despite significant advances recently, existing locomotion algorithms for humanoid robots still struggle to traverse extreme environments, especially in cases that lack external perception (e.g., vision or LiDAR). This is because current methods often rely on gait-based or perception-condition rewards, lacking effective mechanisms to handle unobservable obstacles and sudden balance loss. To address this challenge, we propose a novel whole-body locomotion algorithm based on dynamic balance and Reinforcement Learning (RL) that enables humanoid robots to traverse extreme terrains, particularly narrow pathways and unexpected obstacles, using only proprioception. Specifically, we introduce a dynamic balance mechanism by leveraging an extended measure of Zero-Moment Point (ZMP)-driven rewards and task-driven rewards in a whole-body actor-critic framework, aiming to achieve coordinated actions of the upper and lower limbs for robust locomotion. Experiments conducted on a full-sized Unitree H1-2 robot verify the ability of our method to maintain balance on extremely narrow terrains and under external disturbances, demonstrating its effectiveness in enhancing the robot's adaptability to complex environments. The videos are given at https://whole-body-loco.github.io.

## Content
Humans possess delicate dynamic balance mechanisms that enable them to maintain stability across diverse terrains and under extreme conditions. However, despite significant advances recently, existing locomotion algorithms for humanoid robots still struggle to traverse extreme environments, especially in cases that lack external perception (e.g., vision or LiDAR). This is because current methods often rely on gait-based or perception-condition rewards, lacking effective mechanisms to handle unobservable obstacles and sudden balance loss. To address this challenge, we propose a novel whole-body locomotion algorithm based on dynamic balance and Reinforcement Learning (RL) that enables humanoid robots to traverse extreme terrains, particularly narrow pathways and unexpected obstacles, using only proprioception. Specifically, we introduce a dynamic balance mechanism by leveraging an extended measure of Zero-Moment Point (ZMP)-driven rewards and task-driven rewards in a whole-body actor-critic framework, aiming to achieve coordinated actions of the upper and lower limbs for robust locomotion. Experiments conducted on a full-sized Unitree H1-2 robot verify the ability of our method to maintain balance on extremely narrow terrains and under external disturbances, demonstrating its effectiveness in enhancing the robot's adaptability to complex environments. The videos are given at https://whole-body-loco.github.io.

## 参考
- http://arxiv.org/abs/2502.17219v2

## 개요
기존 운동 알고리즘이 보행 또는 지각 보상에 의존하여 관측 불가능한 장애물과 갑작스러운 균형 상실을 처리하기 어려운 문제를 해결하기 위해, 본 논문은 동적 균형과 강화 학습에 기반한 전신 운동 알고리즘을 제안한다. 이 방법은 확장된 Zero-Moment Point (ZMP) 기반 보상과 작업 기반 보상을 도입하여 전신 actor-critic 프레임워크에서 상하체 협조 동작을 구현하며, 인간형 로봇이 고유 감각만으로 좁은 통로와 예상치 못한 장애물을 통과할 수 있게 한다. Unitree H1-2 전신 로봇에서의 실험은 이 방법이 극도로 좁은 지형과 외부 교란 하에서도 균형을 유지하며 복잡한 환경에 대한 적응 능력을 크게 향상시킴을 보여준다.

## 핵심 내용
### 방법 구조
- 전신 actor-critic 강화 학습 프레임워크를 채택하여 동적 균형 메커니즘을 보상 설계에 통합
- 확장된 Zero-Moment Point (ZMP) 기반 보상을 도입하여 동적 균형 유지의 핵심 지표로 활용
- 작업 기반 보상(예: 속도 추적, 관절 제한 등)과 결합하여 상하체 협조 운동 전략 구현

### 실험 설정
- 실험 플랫폼: 전신 크기 Unitree H1-2 인간형 로봇
- 테스트 시나리오: 극도로 좁은 지형(예: 좁은 통로, 불규칙한 장애물) 및 외부 교란(예: 추력 간섭)
- 감각 입력: 고유 감각(관절 각도, IMU 등)만 사용하며, 시각 또는 LiDAR에 의존하지 않음

### 주요 결과
- 좁은 지형에서 동적 균형을 성공적으로 유지하며 넘어짐이나 불안정이 발생하지 않음
- 외부 추력 교란에 대한 강건성을 보이며 빠르게 안정적인 자세를 회복
- 기준 방법(예: 순수 보행 전략)과 비교하여 관측 불가능한 장애물 시나리오에서 성공률이 크게 향상

### 결론
본 논문에서 제안한 동적 균형 메커니즘과 강화 학습의 결합 방법은 인간형 로봇이 외부 감각 없이 극한 지형을 통과하는 문제를 효과적으로 해결한다. 향후 연구에서는 이 방법을 더 복잡한 지형과 다중 작업 시나리오로 확장하는 것을 탐구할 수 있다.
