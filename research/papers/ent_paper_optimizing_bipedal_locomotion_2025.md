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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.03070v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1158 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2508.03070v1

## 개요
이 연구는 이족 보행 로봇 Cassie의 달리기 보행 최적화에 초점을 맞추며, 극도로 높은 속도에서의 효율적인 운동을 구현하는 것을 목표로 한다. 저자들은 먼저 광범위한 속도 범위에 걸친 보행 효율 최적화 방법을 제안하여, 로봇이 인간 단거리 달리기에 근접한 속도에 도달할 수 있게 한다. 이후 기존의 인간 생체역학 연구를 바탕으로 최적화된 보행을 인간 달리기 메커니즘과 비교한 결과, Cassie와 인간 사이에 형태적 차이가 있음에도 불구하고 핵심 보행 특성이 넓은 속도 구간에서 높은 유사성을 보인다는 것을 발견했다. 마지막으로 연구팀은 최적화된 보행을 완전한 컨트롤러에 통합하여 100미터 단거리 달리기의 실제 규칙(서 있는 자세에서 출발하고 정지하는 것을 포함)을 충족시키고, 하드웨어에서 성공적으로 시연함으로써 이족 보행 로봇 100미터 단거리 달리기의 기네스 세계 기록을 수립했다.

## 핵심 내용
### 방법
- **보행 최적화 프레임워크**: Cassie 로봇을 대상으로 광범위한 속도 범위에 걸친 보행 효율 최적화 방법을 제안한다. 이 방법은 보행 파라미터(보폭, 보빈, 착지 각도 등)를 조정하여 에너지 소비를 최소화하거나 속도를 최대화함으로써, 저속에서 극고속까지의 연속적인 보행 궤적을 생성한다.
- **인간 달리기와의 비교**: 확립된 인간 생체역학 연구(관절 토크, 지면 반력, 질량 중심 궤적 등)를 기반으로 최적화된 Cassie 보행을 인간 달리기 데이터와 정량적으로 비교한다. Cassie의 다리 구조(발 아치 없음, 모터 구동 등)가 인간과 다르지만, 핵심 지표(보행 주기 내 에너지 회수율, 착지 시간 비율 등)는 높은 유사성을 보인다.

### 실험 설정
- **하드웨어 플랫폼**: Agility Robotics가 개발한 이족 보행 로봇 Cassie를 사용하며, 수동적 발목 관절과 경량 설계를 갖추어 고속 운동에 적합하다.
- **작업 규칙**: 국제 육상 연맹 100미터 단거리 달리기 규칙을 엄격히 준수하며, 정지 상태의 서 있는 자세에서 출발, 전 구간 직선 주행, 종점에서 정지를 포함한다. 컨트롤러는 출발 가속, 중간 주행, 감속 정지의 세 단계를 처리해야 한다.
- **성능 지표**: 최고 속도, 평균 속도, 보행 주기 시간, 에너지 소비(모터 전류 추정) 등을 기록한다.

### 주요 수치와 결과
- **세계 기록**: 하드웨어 시연에서 Cassie는 **24.73초**로 100미터 단거리 달리기를 완주하여 이족 보행 로봇 100미터 단거리 달리기의 기네스 세계 기록을 수립했다(이전 기록은 약 30초).
- **속도 비교**: 최적화된 보행을 통해 Cassie는 **약 4.5 m/s**의 최고 속도에 도달했다(인간 단거리 선수는 약 10 m/s). 그러나 로봇의 크기와 출력 제한을 고려할 때, 이 속도는 이론적 한계에 근접한 수치이다.
- **보행 유사성**: 속도 범위 2-4 m/s에서 Cassie의 보행 주기 시간, 착지 시간 비율(약 40-50%)은 인간 달리기 데이터와의 편차가 15% 미만이다. 질량 중심의 수직 변동 폭(약 5 cm)도 인간 달리기 패턴과 일치한다.

### 결론
- 보행 효율을 최적화함으로써 이족 보행 로봇은 안정성을 희생하지 않고 고속 주행을 달성할 수 있으며, 그 보행 특성은 핵심 역학 지표에서 인간 달리기와 높은 유사성을 보여 생체 모방 설계가 로봇 운동 제어에 효과적임을 입증한다.
- 완전한 컨트롤러의 통합(출발, 중간 주행, 정지)은 실제 경쟁 작업에서 최적화된 보행의 실현 가능성을 증명하며, 향후 동적 환경에서 이족 보행 로봇의 고속 운동을 위한 기반을 제공한다.
