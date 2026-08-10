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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.15036v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (761 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2505.15036v1

## 개요
다중 로봇 시스템에서 개별 로봇의 고장이 집단 성능에 영향을 미치는 문제를 해결하기 위해, 본 논문은 ACR 방법을 제안한다. 이 방법은 로봇이 전역 정보와 직접 통신이 부족한 상황에서도 물리적 접촉 상호작용만으로 결함 허용을 가능하게 한다. 각 로봇은 자기 중심의 동적 접촉 그래프를 유지하며, 접촉 대상이 고장으로 정지한 동료인지 평가하고 능동적으로 밀거나 수동적으로 회피하는 행동을 선택한다. 실험은 제한된 터널 환경에서 수행되었으며, 접촉 감지와 충돌 저항 능력을 갖춘 세 대의 자율 로봇이 점착성 모델 입자를 협력적으로 굴착했다. 결과는 ACR이 고장으로부터 시스템이 회복하는 시간을 크게 단축시키고, 집단 굴착 성능 저하를 최소화함을 보여준다.

## 핵심 내용
### 방법 핵심
- **Active Contact Response (ACR)**: 분산형 알고리즘으로, 각 로봇은 자체 접촉 센서를 기반으로 동적 접촉 그래프를 구축하고 실시간으로 접촉 대상의 상태를 판단한다.
- **행동 결정**: 접촉이 고장으로 정지한 동료로 판단되면, 로봇은 이를 장애가 적은 배치로 능동적으로 밀어낸다. 그렇지 않으면 수동적 회피 전략을 사용한다.
- **적용 조건**: 전역 정보나 직접 통신이 필요 없으며, 국소적 물리적 상호작용에만 의존하므로 센서 제한과 좁은 공간 환경에 적합하다.

### 실험 설정
- **하드웨어 플랫폼**: 접촉 센서와 충돌 허용 기계 구조를 갖춘 세 대의 자율 이동 로봇.
- **작업 시나리오**: 제한된 터널에서 점착성 모델 입자(cohesive model pellets)를 협력적으로 굴착.
- **비교 기준선**: 수동적 회피 방법(충돌만 피하고 고장 로봇에 능동적으로 개입하지 않음).

### 주요 결과
- **굴착 효율**: 30분 실험 후, ACR 방법으로 굴착한 입자 수는 수동적 기준선 방법의 약 두 배에 달했다.
- **고장 복구**: ACR은 로봇 고장으로 인한 시스템 성능 저하 시간을 크게 단축시켜 집단 굴착의 연속성을 유지한다.
- **성능 저하**: 수동적 방법에 비해 ACR은 고장 후 집단 성능 저하 폭을 최소화한다.

### 결론
본 논문은 제한되고 극한의 환경에서 국소적, 사회적, 물리적 상호작용을 활용하면 다중 로봇 시스템의 결함 허용성과 조정 능력을 효과적으로 강화할 수 있음을 증명한다. ACR 방법은 전역 통신이 없는 시나리오에서 집단 견고성을 위한 새로운 접근 방식을 제시한다.
