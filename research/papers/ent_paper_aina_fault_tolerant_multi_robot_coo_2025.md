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
  zh: 本文提出了主动接触响应（ACR），一种去中心化的容错方法：机器人维护以自我为中心的动态接触图，估计接触是否来自故障静止同伴，并主动将其推至阻碍较小的构型或退回到被动避碰。在封闭隧道中使用三个主动机器人挖掘粘性模型颗粒的物理实验表明，30分钟后ACR挖掘的颗粒数量几乎是被动基线的两倍。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.15036v1.
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
As robots are increasingly deployed to collaborate on tasks within shared workspaces and resources, the failure of an individual robot can critically affect the group's performance. This issue is particularly challenging when robots lack global information or direct communication, relying instead on social interaction for coordination and to complete their tasks. In this study, we propose a novel fault-tolerance technique leveraging physical contact interactions in multi-robot systems, specifically under conditions of limited sensing and spatial confinement. We introduce the "Active Contact Response" (ACR) method, where each robot modulates its behavior based on the likelihood of encountering an inoperative (faulty) robot. Active robots are capable of collectively repositioning stationary and faulty peers to reduce obstructions and maintain optimal group functionality. We implement our algorithm in a team of autonomous robots, equipped with contact-sensing and collision-tolerance capabilities, tasked with collectively excavating cohesive model pellets. Experimental results indicate that the ACR method significantly improves the system's recovery time from robot failures, enabling continued collective excavation with minimal performance degradation. Thus, this work demonstrates the potential of leveraging local, social, and physical interactions to enhance fault tolerance and coordination in multi-robot systems operating in constrained and extreme environments.

## 核心内容
As robots are increasingly deployed to collaborate on tasks within shared workspaces and resources, the failure of an individual robot can critically affect the group's performance. This issue is particularly challenging when robots lack global information or direct communication, relying instead on social interaction for coordination and to complete their tasks. In this study, we propose a novel fault-tolerance technique leveraging physical contact interactions in multi-robot systems, specifically under conditions of limited sensing and spatial confinement. We introduce the "Active Contact Response" (ACR) method, where each robot modulates its behavior based on the likelihood of encountering an inoperative (faulty) robot. Active robots are capable of collectively repositioning stationary and faulty peers to reduce obstructions and maintain optimal group functionality. We implement our algorithm in a team of autonomous robots, equipped with contact-sensing and collision-tolerance capabilities, tasked with collectively excavating cohesive model pellets. Experimental results indicate that the ACR method significantly improves the system's recovery time from robot failures, enabling continued collective excavation with minimal performance degradation. Thus, this work demonstrates the potential of leveraging local, social, and physical interactions to enhance fault tolerance and coordination in multi-robot systems operating in constrained and extreme environments.

## 参考
- http://arxiv.org/abs/2505.15036v1

