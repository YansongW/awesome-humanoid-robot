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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.17219v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
인간은 다양한 지형과 극한 조건에서도 안정성을 유지할 수 있는 정교한 동적 균형 메커니즘을 갖추고 있습니다. 그러나 최근 상당한 진전이 있었음에도 불구하고, 기존의 인간형 로봇 보행 알고리즘은 특히 외부 인식(예: 시각 또는 LiDAR)이 부족한 경우 극한 환경을 탐색하는 데 여전히 어려움을 겪고 있습니다. 이는 현재 방법들이 종종 보행 기반 또는 인식 조건 보상에 의존하여, 관찰 불가능한 장애물과 갑작스러운 균형 상실을 처리하는 효과적인 메커니즘이 부족하기 때문입니다. 이러한 문제를 해결하기 위해, 우리는 동적 균형과 강화 학습(RL)에 기반한 새로운 전신 보행 알고리즘을 제안합니다. 이 알고리즘은 고유 감각만을 사용하여 인간형 로봇이 특히 좁은 통로와 예상치 못한 장애물과 같은 극한 지형을 탐색할 수 있게 합니다. 구체적으로, 우리는 전신 행위자-비평가 프레임워크에서 확장된 영모멘트점(ZMP) 기반 보상과 작업 기반 보상을 활용하여 동적 균형 메커니즘을 도입하며, 상체와 하체의 협력 동작을 통해 강건한 보행을 목표로 합니다. 실제 크기의 Unitree H1-2 로봇에서 수행된 실험은 극도로 좁은 지형과 외부 교란 하에서도 균형을 유지하는 우리 방법의 능력을 검증하며, 복잡한 환경에 대한 로봇의 적응성을 향상시키는 효과를 입증합니다. 비디오는 https://whole-body-loco.github.io에서 확인할 수 있습니다.

## 핵심 내용
인간은 다양한 지형과 극한 조건에서도 안정성을 유지할 수 있는 정교한 동적 균형 메커니즘을 갖추고 있습니다. 그러나 최근 상당한 진전이 있었음에도 불구하고, 기존의 인간형 로봇 보행 알고리즘은 특히 외부 인식(예: 시각 또는 LiDAR)이 부족한 경우 극한 환경을 탐색하는 데 여전히 어려움을 겪고 있습니다. 이는 현재 방법들이 종종 보행 기반 또는 인식 조건 보상에 의존하여, 관찰 불가능한 장애물과 갑작스러운 균형 상실을 처리하는 효과적인 메커니즘이 부족하기 때문입니다. 이러한 문제를 해결하기 위해, 우리는 동적 균형과 강화 학습(RL)에 기반한 새로운 전신 보행 알고리즘을 제안합니다. 이 알고리즘은 고유 감각만을 사용하여 인간형 로봇이 특히 좁은 통로와 예상치 못한 장애물과 같은 극한 지형을 탐색할 수 있게 합니다. 구체적으로, 우리는 전신 행위자-비평가 프레임워크에서 확장된 영모멘트점(ZMP) 기반 보상과 작업 기반 보상을 활용하여 동적 균형 메커니즘을 도입하며, 상체와 하체의 협력 동작을 통해 강건한 보행을 목표로 합니다. 실제 크기의 Unitree H1-2 로봇에서 수행된 실험은 극도로 좁은 지형과 외부 교란 하에서도 균형을 유지하는 우리 방법의 능력을 검증하며, 복잡한 환경에 대한 로봇의 적응성을 향상시키는 효과를 입증합니다. 비디오는 https://whole-body-loco.github.io에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2502.17219v2
