---
$id: ent_paper_drama_trunk_pitch_oscillations_for_j_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Trunk Pitch Oscillations for Joint Load Redistribution in Humans and Humanoid Robots
  zh: 人类与仿人机器人中躯干俯仰振荡对关节负载重分配的影响
  ko: 인간과 휴머노이드 로봇에서의 관절 하중 재분배를 위한 몸통 피치 진동
summary:
  en: This 2019 arXiv paper by Drama and Badri-Spröwitz uses a trunk-equipped spring-loaded inverted pendulum (TSLIP) model
    with a virtual point target to generate and analyze trunk pitch oscillations, showing that a virtual point below the center
    of mass can reproduce forward trunk pitching in human running and redistribute joint work between hip and leg.
  zh: Drama 和 Badri-Spröwitz 在 2019 年 arXiv 论文中，利用带躯干的弹簧负载倒立摆（TSLIP）模型与虚拟点目标，生成并分析躯干俯仰振荡。他们发现，将虚拟点置于质心下方可复现人类跑步中的前倾躯干姿态，并重新分配髋关节与腿部之间的关节做功。
  ko: Drama와 Badri-Spröwitz의 2019년 arXiv 논문은 몸통이 있는 스프링 로드 인버티드 펜듈럼(TSLIP) 모델과 가상점(VP) 목표를 사용하여 몸통 피치 진동을 생성하고 분석하며, 질량 중심
    아래의 가상점이 인간 달리기에서 관찰되는 전방 몸통 피치를 설명하고 고관절과 다리 사이의 관절 일을 재분배할 수 있음을 보여준다.
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_running
- trunk_oscillation
- spring_loaded_inverted_pendulum
- virtual_point_control
- gait_generation
- joint_load_redistribution
- bipedal_locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1909.03687v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Trunk Pitch Oscillations for Joint Load Redistribution in Humans and Humanoid Robots
  url: https://arxiv.org/abs/1909.03687
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
该研究针对人形机器人因躯干欠驱动自由度导致的自然步态生成难题，提出使用 TSLIP 模型结合虚拟点目标来模拟躯干振荡。通过分析虚拟点位置与前进速度对振荡方向及幅度的影响，作者证明质心下方的虚拟点能解释人类跑步中的躯干前倾现象。这种配置促使髋关节与腿部协同做功，从而降低腿部负载，但代价是髋关节峰值扭矩增加。研究为利用躯干运动重新分配关节负载、提升人形机器人能效提供了新思路。

## 核心内容
### 背景与问题
- 人形机器人生成自然跑步步态面临挑战，主要源于躯干欠驱动自由度导致运动规划与控制困难。
- 现有研究多聚焦下肢，常通过固定躯干角度简化问题，而人类步态中躯干会随自然动力学产生显著运动。
- 缺乏将人类运动模式迁移至机器人的形式化方法。

### 方法与模型
- 采用带躯干的弹簧负载倒立摆（TSLIP）模型，并引入虚拟点（VP）目标来生成躯干俯仰振荡。
- 通过调整 VP 位置（相对于质心 CoM）与前进速度，分析其对躯干振荡方向与幅度的影响。

### 关键发现
- **VP 位于 CoM 下方**：可复现人类跑步中躯干前倾的典型模式。
- **关节负载重分配**：VP 在 CoM 下方时，髋关节与腿部产生协同做功，使腿部负载降低，但髋关节峰值扭矩上升。
- **能效权衡**：躯干运动虽能重新分配关节负载，但需注意髋关节扭矩增加带来的潜在代价。

### 结论与意义
- 研究为利用躯干运动优化人形机器人步态提供了理论依据，尤其适用于关节负载分布与能量效率的平衡。
- 未来可基于此框架设计更自然的机器人跑步控制策略。

## Overview
Creating natural-looking running gaits for humanoid robots is a complex task due to the underactuated degree of freedom in the trunk, which makes the motion planning and control difficult. The research on trunk movements in human locomotion is insufficient, and no formalism is known to transfer human motion patterns onto robots. Related work mostly focuses on the lower extremities, and simplifies the problem by stabilizing the trunk at a fixed angle. In contrast, humans display significant trunk motions that follow the natural dynamics of the gait. In this work, we use a spring-loaded inverted pendulum model with a trunk (TSLIP) together with a virtual point (VP) target to create trunk oscillations and investigate the impact of these movements. We analyze how the VP location and forward speed determine the direction and magnitude of the trunk oscillations. We show that positioning the VP below the center of mass (CoM) can explain the forward trunk pitching observed in human running. The VP below the CoM leads to a synergistic work between the hip and leg, reducing the leg loading. However, it comes at the cost of increased peak hip torque. Our results provide insights for leveraging the trunk motion to redistribute joint loads and potentially improve the energy efficiency in humanoid robots.

## Overview
Creating natural-looking running gaits for humanoid robots is a complex task due to the underactuated degree of freedom in the trunk, which makes motion planning and control difficult. Research on trunk movements in human locomotion is insufficient, and no formalism is known to transfer human motion patterns onto robots. Related work mostly focuses on the lower extremities and simplifies the problem by stabilizing the trunk at a fixed angle. In contrast, humans display significant trunk motions that follow the natural dynamics of the gait. In this work, we use a spring-loaded inverted pendulum model with a trunk (TSLIP) together with a virtual point (VP) target to create trunk oscillations and investigate the impact of these movements. We analyze how the VP location and forward speed determine the direction and magnitude of the trunk oscillations. We show that positioning the VP below the center of mass (CoM) can explain the forward trunk pitching observed in human running. The VP below the CoM leads to synergistic work between the hip and leg, reducing leg loading. However, it comes at the cost of increased peak hip torque. Our results provide insights for leveraging trunk motion to redistribute joint loads and potentially improve energy efficiency in humanoid robots.

## Content
Creating natural-looking running gaits for humanoid robots is a complex task due to the underactuated degree of freedom in the trunk, which makes motion planning and control difficult. Research on trunk movements in human locomotion is insufficient, and no formalism is known to transfer human motion patterns onto robots. Related work mostly focuses on the lower extremities and simplifies the problem by stabilizing the trunk at a fixed angle. In contrast, humans display significant trunk motions that follow the natural dynamics of the gait. In this work, we use a spring-loaded inverted pendulum model with a trunk (TSLIP) together with a virtual point (VP) target to create trunk oscillations and investigate the impact of these movements. We analyze how the VP location and forward speed determine the direction and magnitude of the trunk oscillations. We show that positioning the VP below the center of mass (CoM) can explain the forward trunk pitching observed in human running. The VP below the CoM leads to synergistic work between the hip and leg, reducing leg loading. However, it comes at the cost of increased peak hip torque. Our results provide insights for leveraging trunk motion to redistribute joint loads and potentially improve energy efficiency in humanoid robots.

## 개요
휴머노이드 로봇의 자연스러운 달리기 보행을 생성하는 것은 몸통의 부족 구동 자유도로 인해 복잡한 작업이며, 이는 운동 계획 및 제어를 어렵게 만듭니다. 인간 보행에서의 몸통 움직임에 대한 연구는 충분하지 않으며, 인간의 운동 패턴을 로봇으로 전환하는 공식화된 방법은 알려져 있지 않습니다. 관련 연구는 주로 하지에 초점을 맞추며, 몸통을 고정된 각도로 안정화하여 문제를 단순화합니다. 이와 대조적으로, 인간은 보행의 자연스러운 동역학을 따르는 상당한 몸통 움직임을 보입니다. 본 연구에서는 몸통이 있는 스프링-장착 역진자 모델(TSLIP)과 가상 점(VP) 목표를 사용하여 몸통 진동을 생성하고 이러한 움직임의 영향을 조사합니다. VP 위치와 전진 속도가 몸통 진동의 방향과 크기를 어떻게 결정하는지 분석합니다. VP를 질량 중심(CoM) 아래에 배치하면 인간 달리기에서 관찰되는 전방 몸통 피칭을 설명할 수 있음을 보여줍니다. CoM 아래의 VP는 엉덩이와 다리 사이의 상승적 작업을 유도하여 다리 부하를 줄입니다. 그러나 이는 최대 엉덩이 토크 증가라는 비용을 수반합니다. 우리의 결과는 몸통 움직임을 활용하여 관절 부하를 재분배하고 잠재적으로 휴머노이드 로봇의 에너지 효율성을 개선하는 통찰력을 제공합니다.

## 핵심 내용
휴머노이드 로봇의 자연스러운 달리기 보행을 생성하는 것은 몸통의 부족 구동 자유도로 인해 복잡한 작업이며, 이는 운동 계획 및 제어를 어렵게 만듭니다. 인간 보행에서의 몸통 움직임에 대한 연구는 충분하지 않으며, 인간의 운동 패턴을 로봇으로 전환하는 공식화된 방법은 알려져 있지 않습니다. 관련 연구는 주로 하지에 초점을 맞추며, 몸통을 고정된 각도로 안정화하여 문제를 단순화합니다. 이와 대조적으로, 인간은 보행의 자연스러운 동역학을 따르는 상당한 몸통 움직임을 보입니다. 본 연구에서는 몸통이 있는 스프링-장착 역진자 모델(TSLIP)과 가상 점(VP) 목표를 사용하여 몸통 진동을 생성하고 이러한 움직임의 영향을 조사합니다. VP 위치와 전진 속도가 몸통 진동의 방향과 크기를 어떻게 결정하는지 분석합니다. VP를 질량 중심(CoM) 아래에 배치하면 인간 달리기에서 관찰되는 전방 몸통 피칭을 설명할 수 있음을 보여줍니다. CoM 아래의 VP는 엉덩이와 다리 사이의 상승적 작업을 유도하여 다리 부하를 줄입니다. 그러나 이는 최대 엉덩이 토크 증가라는 비용을 수반합니다. 우리의 결과는 몸통 움직임을 활용하여 관절 부하를 재분배하고 잠재적으로 휴머노이드 로봇의 에너지 효율성을 개선하는 통찰력을 제공합니다.

## 参考
- http://arxiv.org/abs/1909.03687v1
