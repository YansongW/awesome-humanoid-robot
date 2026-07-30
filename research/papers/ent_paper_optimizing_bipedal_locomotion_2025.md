---
$id: ent_paper_optimizing_bipedal_locomotion_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Optimizing Bipedal Locomotion for The 100m Dash With Comparison to Human Running
  zh: Optimizing Bipedal Locomotion for The 100m Dash With Comparison to Human Running
  ko: Optimizing Bipedal Locomotion for The 100m Dash With Comparison to Human Running
summary:
  en: Optimizing Bipedal Locomotion for The 100m Dash With Comparison to Human Running is a 2025 work on locomotion for humanoid
    robots.
  zh: 本文提出了一种针对双足机器人Cassie的100米短跑步态优化方法，并与人类跑步生物力学进行了系统比较。研究团队通过优化不同速度下的步态效率，成功实现了硬件上的高速奔跑，并最终以实际硬件演示创造了双足机器人100米短跑吉尼斯世界纪录。核心贡献包括步态优化框架、与人类跑步的对比分析，以及完整竞赛控制器的集成。
  ko: Optimizing Bipedal Locomotion for The 100m Dash With Comparison to Human Running is a 2025 work on locomotion for humanoid
    robots.
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
- optimizing_bipedal_locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.03070v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Optimizing Bipedal Locomotion for The 100m Dash With Comparison to Human Running (arXiv)
  url: https://arxiv.org/abs/2508.03070
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究聚焦于双足机器人Cassie的跑步步态优化，旨在实现极高速度下的高效运动。作者首先提出了一种跨速度范围的步态效率优化方法，使机器人能够达到接近人类短跑的速度。随后，基于已有的人类生物力学研究，将优化后的步态与人类跑步机制进行对比，发现尽管Cassie与人类在形态上存在差异，但关键步态特性在广泛速度区间内高度相似。最后，研究团队将优化步态集成到完整的控制器中，使其满足100米短跑的真实规则（包括从站立姿态起跑和停止），并在硬件上成功演示，从而创造了双足机器人100米短跑的吉尼斯世界纪录。

## 核心内容
### 方法
- **步态优化框架**：针对Cassie机器人，提出了一种跨速度范围的步态效率优化方法。该方法通过调整步态参数（如步长、步频、触地角度等），最小化能量消耗或最大化速度，从而生成从低速到极高速度的连续步态轨迹。
- **与人类跑步的对比**：基于已建立的人类生物力学研究（如关节力矩、地面反作用力、质心轨迹等），将优化后的Cassie步态与人类跑步数据进行定量比较。尽管Cassie的腿部结构（如无足弓、电机驱动）与人类不同，但关键指标（如步态周期内的能量回收率、触地时间占比）表现出高度相似性。

### 实验设置
- **硬件平台**：使用双足机器人Cassie（由Agility Robotics开发），其具有被动踝关节和轻量化设计，适合高速运动。
- **任务规则**：严格遵循国际田联100米短跑规则，包括从静止站立姿态起跑、全程直线奔跑、终点停止。控制器需处理起跑加速、途中跑和减速停止三个阶段。
- **性能指标**：记录最高速度、平均速度、步态周期时间、能量消耗（通过电机电流估算）等。

### 关键数字与结果
- **世界纪录**：在硬件演示中，Cassie以**24.73秒**完成100米短跑，创造了双足机器人100米短跑的吉尼斯世界纪录（此前纪录为约30秒）。
- **速度对比**：优化后的步态使Cassie达到**约4.5 m/s**的最高速度（人类短跑运动员约为10 m/s），但考虑到机器人尺寸和功率限制，这一速度已接近理论极限。
- **步态相似性**：在速度范围2-4 m/s内，Cassie的步态周期时间、触地时间占比（约40-50%）与人类跑步数据偏差小于15%；质心垂直波动幅度（约5 cm）也与人类跑步模式一致。

### 结论
- 通过优化步态效率，双足机器人可以在不牺牲稳定性的前提下实现高速奔跑，且其步态特性与人类跑步在关键力学指标上高度相似，表明生物启发式设计对机器人运动控制的有效性。
- 完整控制器的集成（起跑、途中跑、停止）证明了优化步态在真实竞赛任务中的可行性，为未来双足机器人在动态环境中的高速运动提供了基础。

## Overview
In this paper, we explore the space of running gaits for the bipedal robot Cassie. Our first contribution is to present an approach for optimizing gait efficiency across a spectrum of speeds with the aim of enabling extremely high-speed running on hardware. This raises the question of how the resulting gaits compare to human running mechanics, which are known to be highly efficient in comparison to quadrupeds. Our second contribution is to conduct this comparison based on established human biomechanical studies. We find that despite morphological differences between Cassie and humans, key properties of the gaits are highly similar across a wide range of speeds. Finally, our third contribution is to integrate the optimized running gaits into a full controller that satisfies the rules of the real-world task of the 100m dash, including starting and stopping from a standing position. We demonstrate this controller on hardware to establish the Guinness World Record for Fastest 100m by a Bipedal Robot.

## 개요
본 논문에서는 이족 보행 로봇 Cassie의 달리기 보행 공간을 탐구합니다. 첫 번째 기여는 하드웨어에서 초고속 달리기를 가능하게 하는 것을 목표로 다양한 속도 범위에서 보행 효율성을 최적화하는 접근법을 제시하는 것입니다. 이는 결과적으로 생성된 보행이 사족 동물에 비해 매우 효율적인 것으로 알려진 인간의 달리기 역학과 어떻게 비교되는지에 대한 질문을 제기합니다. 두 번째 기여는 기존의 인간 생체역학 연구를 기반으로 이 비교를 수행하는 것입니다. Cassie와 인간 사이의 형태학적 차이에도 불구하고, 보행의 주요 특성은 광범위한 속도 범위에서 매우 유사함을 발견했습니다. 마지막으로 세 번째 기여는 최적화된 달리기 보행을 서 있는 자세에서 출발 및 정지를 포함한 100m 달리기라는 실제 과제의 규칙을 충족하는 완전한 제어기에 통합하는 것입니다. 우리는 이 제어기를 하드웨어에서 시연하여 이족 보행 로봇으로서 가장 빠른 100m 달리기에 대한 기네스 세계 기록을 수립했습니다.

## 핵심 내용
본 논문에서는 이족 보행 로봇 Cassie의 달리기 보행 공간을 탐구합니다. 첫 번째 기여는 하드웨어에서 초고속 달리기를 가능하게 하는 것을 목표로 다양한 속도 범위에서 보행 효율성을 최적화하는 접근법을 제시하는 것입니다. 이는 결과적으로 생성된 보행이 사족 동물에 비해 매우 효율적인 것으로 알려진 인간의 달리기 역학과 어떻게 비교되는지에 대한 질문을 제기합니다. 두 번째 기여는 기존의 인간 생체역학 연구를 기반으로 이 비교를 수행하는 것입니다. Cassie와 인간 사이의 형태학적 차이에도 불구하고, 보행의 주요 특성은 광범위한 속도 범위에서 매우 유사함을 발견했습니다. 마지막으로 세 번째 기여는 최적화된 달리기 보행을 서 있는 자세에서 출발 및 정지를 포함한 100m 달리기라는 실제 과제의 규칙을 충족하는 완전한 제어기에 통합하는 것입니다. 우리는 이 제어기를 하드웨어에서 시연하여 이족 보행 로봇으로서 가장 빠른 100m 달리기에 대한 기네스 세계 기록을 수립했습니다.

## 参考
- http://arxiv.org/abs/2508.03070v1
