---
$id: ent_paper_aina_fault_tolerant_multi_robot_coo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Fault-Tolerant Multi-Robot Coordination with Limited Sensing within Confined Environments
  zh: 受限环境下有限感知的多机器人容错协调
  ko: 제한된 환경에서 제한된 감지를 가진 다중 로봇의 결함 허용 조정
summary:
  en: This paper proposes Active Contact Response (ACR), a decentralized fault-tolerance method in which robots maintain an
    egocentric dynamic contact map to estimate whether a contact is a faulty stationary peer and either actively push it to
    a less obstructive configuration or fall back to passive avoidance. Physical experiments with three active robots excavating
    cohesive model pellets in a confined tunnel show that ACR nearly doubles the number of pellets excavated compared with
    a passive baseline after 30 minutes.
  zh: 本文提出一种名为Active Contact Response (ACR)的去中心化容错方法，使机器人在有限感知与狭窄环境中通过动态接触图区分故障同伴，并主动将其推至非阻塞位置。在三个机器人协作挖掘黏性颗粒的隧道实验中，ACR在30分钟内挖掘量相比被动基线方法提升近一倍。
  ko: 본 논문은 각 로봇이 자기 중심의 동적 접촉 맵을 유지하여 접촉이 고장 난 정지된 동료로부터 온 것인지 추정하고, 이를 덜 방해가 되는 구성으로 적극 밀거나 수동 회피로 대응하는 분산형 결함 허용 방법인 Active
    Contact Response(ACR)를 제안한다. 제한된 터널에서 세 대의 활성 로봇으로 응집성 모형 펠릿을 굴삭한 물리 실험 결과, 30분 후 ACR은 수동 기준 방법보다 거의 두 배의 펠릿을 굴삭했다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- active_contact_response
- fault_tolerance
- multi_robot_coordination
- decentralized_control
- contact_based_interaction
- swarm_robotics
- confined_environment
- collective_excavation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.15036v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Fault-Tolerant Multi-Robot Coordination with Limited Sensing within Confined Environments
  url: https://arxiv.org/abs/2505.15036
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
针对多机器人系统中个体故障影响群体性能的问题，本文提出ACR方法，允许机器人在缺乏全局信息与直接通信时，仅通过物理接触交互实现容错。每个机器人维护以自我为中心的动态接触图，评估接触对象是否为故障静止同伴，并选择主动推动或被动避让。实验在受限隧道环境中进行，三个自主机器人配备接触感知与抗碰撞能力，协作挖掘黏性模型颗粒。结果显示ACR显著缩短系统从故障中恢复的时间，使集体挖掘性能退化最小化。

## 核心内容
### 方法核心
- **Active Contact Response (ACR)**：去中心化算法，每个机器人基于自身接触传感器构建动态接触图，实时判断接触对象状态。
- **行为决策**：若判定接触为故障静止同伴，机器人主动将其推至较少阻碍的配置；否则采用被动避让策略。
- **适用条件**：无需全局信息或直接通信，仅依赖局部物理交互，适用于传感受限与空间狭窄环境。

### 实验设置
- **硬件平台**：三个自主移动机器人，配备接触传感器与碰撞容忍机械结构。
- **任务场景**：在受限隧道中协作挖掘黏性模型颗粒（cohesive model pellets）。
- **对比基线**：被动避让方法（仅避免碰撞，不主动干预故障机器人）。

### 关键结果
- **挖掘效率**：30分钟实验后，ACR方法挖掘的颗粒数量接近被动基线方法的两倍。
- **故障恢复**：ACR显著缩短系统因机器人故障导致的性能下降时间，维持集体挖掘连续性。
- **性能退化**：相比被动方法，ACR使故障后的群体性能退化幅度最小化。

### 结论
本文证明，在受限与极端环境中，利用局部、社交与物理交互可有效增强多机器人系统的容错性与协调能力。ACR方法为无全局通信场景下的群体鲁棒性提供了新思路。

## Overview
As robots are increasingly deployed to collaborate on tasks within shared workspaces and resources, the failure of an individual robot can critically affect the group's performance. This issue is particularly challenging when robots lack global information or direct communication, relying instead on social interaction for coordination and to complete their tasks. In this study, we propose a novel fault-tolerance technique leveraging physical contact interactions in multi-robot systems, specifically under conditions of limited sensing and spatial confinement. We introduce the "Active Contact Response" (ACR) method, where each robot modulates its behavior based on the likelihood of encountering an inoperative (faulty) robot. Active robots are capable of collectively repositioning stationary and faulty peers to reduce obstructions and maintain optimal group functionality. We implement our algorithm in a team of autonomous robots, equipped with contact-sensing and collision-tolerance capabilities, tasked with collectively excavating cohesive model pellets. Experimental results indicate that the ACR method significantly improves the system's recovery time from robot failures, enabling continued collective excavation with minimal performance degradation. Thus, this work demonstrates the potential of leveraging local, social, and physical interactions to enhance fault tolerance and coordination in multi-robot systems operating in constrained and extreme environments.

## 개요
로봇이 공유 작업 공간과 자원 내에서 협업을 위해 점점 더 많이 배치됨에 따라, 개별 로봇의 고장은 그룹 성능에 심각한 영향을 미칠 수 있습니다. 이 문제는 로봇이 글로벌 정보나 직접 통신 없이 조정과 작업 완료를 위해 사회적 상호작용에 의존할 때 특히 어려워집니다. 본 연구에서는 제한된 감지 능력과 공간적 제약 조건 하에서 다중 로봇 시스템의 물리적 접촉 상호작용을 활용한 새로운 결함 허용 기술을 제안합니다. 우리는 "능동 접촉 대응"(ACR) 방법을 소개하며, 각 로봇은 작동 불능(고장) 로봇과 마주칠 가능성에 따라 행동을 조정합니다. 능동 로봇은 정지 상태의 고장 동료를 집단적으로 재배치하여 장애를 줄이고 최적의 그룹 기능을 유지할 수 있습니다. 우리는 접촉 감지 및 충돌 허용 기능을 갖춘 자율 로봇 팀에서 알고리즘을 구현했으며, 이 로봇들은 응집성 모델 펠릿을 집단적으로 굴착하는 작업을 수행합니다. 실험 결과는 ACR 방법이 로봇 고장으로부터 시스템의 복구 시간을 크게 개선하여 최소한의 성능 저하로 지속적인 집단 굴착을 가능하게 함을 보여줍니다. 따라서 이 연구는 제한적이고 극한 환경에서 작동하는 다중 로봇 시스템의 결함 허용 및 조정을 향상시키기 위해 지역적, 사회적, 물리적 상호작용을 활용할 가능성을 입증합니다.

## 핵심 내용
로봇이 공유 작업 공간과 자원 내에서 협업을 위해 점점 더 많이 배치됨에 따라, 개별 로봇의 고장은 그룹 성능에 심각한 영향을 미칠 수 있습니다. 이 문제는 로봇이 글로벌 정보나 직접 통신 없이 조정과 작업 완료를 위해 사회적 상호작용에 의존할 때 특히 어려워집니다. 본 연구에서는 제한된 감지 능력과 공간적 제약 조건 하에서 다중 로봇 시스템의 물리적 접촉 상호작용을 활용한 새로운 결함 허용 기술을 제안합니다. 우리는 "능동 접촉 대응"(ACR) 방법을 소개하며, 각 로봇은 작동 불능(고장) 로봇과 마주칠 가능성에 따라 행동을 조정합니다. 능동 로봇은 정지 상태의 고장 동료를 집단적으로 재배치하여 장애를 줄이고 최적의 그룹 기능을 유지할 수 있습니다. 우리는 접촉 감지 및 충돌 허용 기능을 갖춘 자율 로봇 팀에서 알고리즘을 구현했으며, 이 로봇들은 응집성 모델 펠릿을 집단적으로 굴착하는 작업을 수행합니다. 실험 결과는 ACR 방법이 로봇 고장으로부터 시스템의 복구 시간을 크게 개선하여 최소한의 성능 저하로 지속적인 집단 굴착을 가능하게 함을 보여줍니다. 따라서 이 연구는 제한적이고 극한 환경에서 작동하는 다중 로봇 시스템의 결함 허용 및 조정을 향상시키기 위해 지역적, 사회적, 물리적 상호작용을 활용할 가능성을 입증합니다.

## 参考
- http://arxiv.org/abs/2505.15036v1
