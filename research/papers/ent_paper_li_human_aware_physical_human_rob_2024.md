---
$id: ent_paper_li_human_aware_physical_human_rob_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Human-Aware Physical Human-Robot Collaborative Transportation and Manipulation with Multiple Aerial Robots
  zh: 基于多架空中机器人的人类感知物理人机协作搬运与操作
  ko: 다중 공중 로봇을 이용한 인간 인식 물리적 인간-로봇 협력 운반 및 조작
summary:
  en: Proposes a hierarchical control framework in which a team of quadrotors carrying a cable-suspended rigid payload collaborates
    with a human to transport and manipulate the load in 6 DoF, using a force-sensorless wrench estimator, a 6-DoF admittance
    controller, and a redundant human-aware force distribution that enforces separation constraints.
  zh: 提出了一种分层控制框架，使多架携带缆绳悬挂刚性负载的四旋翼飞行器与人类协作，在6自由度下搬运与操作负载；该方法利用无 force 传感器的外力/力矩估计器、6自由度导纳控制器以及利用内部冗余的人感知力分配来满足分离约束。
  ko: 케이블로 매달린 강체 페이로드를 운반하는 쿼드로터 팀이 인간과 협력하여 6자유도로 물체를 운반 및 조작할 수 있는 계층적 제어 프레임워크를 제안한다. 이 방법은 force 센서가 없는 외력/토크 추정기, 6자유도
    어드미턴스 컨트롤러, 내부 중복성을 활용한 인간 인식 힘 분배를 통해 분리 제약을 만족한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- admittance_control
- multi_robot_coordination
- aerial_manipulation
- physical_human_robot_interaction
- collaborative_transport
- force_distribution
- wrench_estimation
- cable_suspended_payload
- human_aware_control
- redundancy_resolution
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.05894v3.
sources:
- id: src_001
  type: paper
  title: Human-Aware Physical Human-Robot Collaborative Transportation and Manipulation with Multiple Aerial Robots
  url: https://arxiv.org/abs/2210.05894
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Human-robot interaction will play an essential role in various industries and daily tasks, enabling robots to effectively collaborate with humans and reduce their physical workload. Most of the existing approaches for physical human-robot interaction focus on collaboration between a human and a single ground or aerial robot. In recent years, very little progress has been made in this research area when considering multiple aerial robots, which offer increased versatility and mobility. This paper proposes a novel approach for physical human-robot collaborative transportation and manipulation of a cable-suspended payload with multiple aerial robots. The proposed method enables smooth and intuitive interaction between the transported objects and a human worker. In the same time, we consider distance constraints during the operations by exploiting the internal redundancy of the multi-robot transportation system. The key elements of our approach are (a) a collaborative payload external wrench estimator that does not rely on any force sensor; (b) a 6D admittance controller for human-aerial-robot collaborative transportation and manipulation; (c) a human-aware force distribution that exploits the internal system redundancy to guarantee the execution of additional tasks such inter-human-robot separation without affecting the payload trajectory tracking or quality of interaction. We validate the approach through extensive simulation and real-world experiments. These include scenarios where the robot team assists the human in transporting and manipulating a load, or where the human helps the robot team navigate the environment. We experimentally demonstrate for the first time, to the best of our knowledge, that our approach enables a quadrotor team to physically collaborate with a human in manipulating a payload in all 6 DoF in collaborative human-robot transportation and manipulation tasks.

## 核心内容
Human-robot interaction will play an essential role in various industries and daily tasks, enabling robots to effectively collaborate with humans and reduce their physical workload. Most of the existing approaches for physical human-robot interaction focus on collaboration between a human and a single ground or aerial robot. In recent years, very little progress has been made in this research area when considering multiple aerial robots, which offer increased versatility and mobility. This paper proposes a novel approach for physical human-robot collaborative transportation and manipulation of a cable-suspended payload with multiple aerial robots. The proposed method enables smooth and intuitive interaction between the transported objects and a human worker. In the same time, we consider distance constraints during the operations by exploiting the internal redundancy of the multi-robot transportation system. The key elements of our approach are (a) a collaborative payload external wrench estimator that does not rely on any force sensor; (b) a 6D admittance controller for human-aerial-robot collaborative transportation and manipulation; (c) a human-aware force distribution that exploits the internal system redundancy to guarantee the execution of additional tasks such inter-human-robot separation without affecting the payload trajectory tracking or quality of interaction. We validate the approach through extensive simulation and real-world experiments. These include scenarios where the robot team assists the human in transporting and manipulating a load, or where the human helps the robot team navigate the environment. We experimentally demonstrate for the first time, to the best of our knowledge, that our approach enables a quadrotor team to physically collaborate with a human in manipulating a payload in all 6 DoF in collaborative human-robot transportation and manipulation tasks.

## 参考
- http://arxiv.org/abs/2210.05894v3

