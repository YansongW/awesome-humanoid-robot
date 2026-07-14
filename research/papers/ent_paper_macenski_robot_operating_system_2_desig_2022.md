---
$id: ent_paper_macenski_robot_operating_system_2_desig_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Operating System 2: Design, Architecture, and Uses In The Wild'
  zh: 机器人操作系统2：设计、架构与真实场景应用
  ko: '로봇 운영 체제 2: 설계, 아키텍처 및 실제 활용'
summary:
  en: A 2022 review paper that presents the ground-up architectural redesign of ROS 2 around DDS middleware and documents
    its real-world adoption through case studies across land, sea, air, space, and fleet robotics.
  zh: 一篇2022年的综述论文，介绍了ROS 2围绕DDS中间件进行的自下而上架构重构，并通过陆地、海洋、空中、太空及集群机器人等案例研究记录其实际应用。
  ko: 2022년 리뷰 논문으로, DDS 미들웨어 중심의 ROS 2 전면 아키텍처 재설계를 제시하고 육상·해상·공중·우주·fleet 로보틱스 사례 연구를 통해 실제 도입 상황을 기록함.
domains:
- 08_software_middleware
- 02_components
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- ros2
- dds_middleware
- robot_middleware
- lifecycle_nodes
- component_nodes
- micro_ros
- sros2
- production_robotics
- fleet_robotics
- simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.07752v1.
sources:
- id: src_001
  type: paper
  title: 'Robot Operating System 2: Design, Architecture, and Uses In The Wild'
  url: https://arxiv.org/abs/2211.07752
  date: '2022'
  accessed_at: '2026-06-27'
  doi: 10.1126/scirobotics.abm6074
theoretical_depth:
- method
- system
---
## 概述
The next chapter of the robotics revolution is well underway with the deployment of robots for a broad range of commercial use-cases. Even in a myriad of applications and environments, there exists a common vocabulary of components that robots share - the need for a modular, scalable, and reliable architecture; sensing; planning; mobility; and autonomy. The Robot Operating System (ROS) was an integral part of the last chapter, demonstrably expediting robotics research with freely-available components and a modular framework. However, ROS 1 was not designed with many necessary production-grade features and algorithms. ROS 2 and its related projects have been redesigned from the ground up to meet the challenges set forth by modern robotic systems in new and exploratory domains at all scales. In this review, we highlight the philosophical and architectural changes of ROS 2 powering this new chapter in the robotics revolution. We also show through case studies the influence ROS 2 and its adoption has had on accelerating real robot systems to reliable deployment in an assortment of challenging environments.

## 核心内容
The next chapter of the robotics revolution is well underway with the deployment of robots for a broad range of commercial use-cases. Even in a myriad of applications and environments, there exists a common vocabulary of components that robots share - the need for a modular, scalable, and reliable architecture; sensing; planning; mobility; and autonomy. The Robot Operating System (ROS) was an integral part of the last chapter, demonstrably expediting robotics research with freely-available components and a modular framework. However, ROS 1 was not designed with many necessary production-grade features and algorithms. ROS 2 and its related projects have been redesigned from the ground up to meet the challenges set forth by modern robotic systems in new and exploratory domains at all scales. In this review, we highlight the philosophical and architectural changes of ROS 2 powering this new chapter in the robotics revolution. We also show through case studies the influence ROS 2 and its adoption has had on accelerating real robot systems to reliable deployment in an assortment of challenging environments.

## 参考
- http://arxiv.org/abs/2211.07752v1

