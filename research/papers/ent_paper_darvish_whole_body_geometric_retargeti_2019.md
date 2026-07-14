---
$id: ent_paper_darvish_whole_body_geometric_retargeti_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Whole-Body Geometric Retargeting for Humanoid Robots
  zh: 面向人形机器人的全身几何重定向
  ko: 휴머노이드 로봇을 위한 전신 기하학적 리타기팅
summary:
  en: A framework for scalable whole-body teleoperation of humanoid robots that maps measured human link orientations and
    angular velocities to corresponding robot links via constant relative rotations, then solves inverse kinematics directly
    on the robot URDF model using a dynamical optimization QP formulation.
  zh: 一种可扩展的人形机器人全身遥操作框架，通过恒定相对旋转将测量的人体连杆朝向和角速度映射到对应机器人连杆，并利用动态优化二次规划在机器人URDF模型上直接求解逆运动学。
  ko: 측정된 인간 링크 방향과 각속도를 일정한 상대 회전을 통해 대응 로봇 링크에 매핑하고, 동적 최적화 QP 공식을 사용해 로봇 URDF 모델에서 직접 역기구학을 풀어 휴머노이드 로봇의 확장 가능한 전신 텔레오퍼레이션을
    위한 프레임워크.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- teleoperation
- motion_retargeting
- whole_body_control
- inverse_kinematics
- humanoid_robot
- geometric_retargeting
- urdf
- human_robot_interaction
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1909.10080v1.
sources:
- id: src_001
  type: paper
  title: Whole-Body Geometric Retargeting for Humanoid Robots
  url: https://arxiv.org/abs/1909.10080
  date: '2019'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Humanoid robot teleoperation allows humans to integrate their cognitive capabilities with the apparatus to perform tasks that need high strength, manoeuvrability and dexterity. This paper presents a framework for teleoperation of humanoid robots using a novel approach for motion retargeting through inverse kinematics over the robot model. The proposed method enhances scalability for retargeting, i.e., it allows teleoperating different robots by different human users with minimal changes to the proposed system. Our framework enables an intuitive and natural interaction between the human operator and the humanoid robot at the configuration space level. We validate our approach by demonstrating whole-body retargeting with multiple robot models. Furthermore, we present experimental validation through teleoperation experiments using two state-of-the-art whole-body controllers for humanoid robots.

## 核心内容
Humanoid robot teleoperation allows humans to integrate their cognitive capabilities with the apparatus to perform tasks that need high strength, manoeuvrability and dexterity. This paper presents a framework for teleoperation of humanoid robots using a novel approach for motion retargeting through inverse kinematics over the robot model. The proposed method enhances scalability for retargeting, i.e., it allows teleoperating different robots by different human users with minimal changes to the proposed system. Our framework enables an intuitive and natural interaction between the human operator and the humanoid robot at the configuration space level. We validate our approach by demonstrating whole-body retargeting with multiple robot models. Furthermore, we present experimental validation through teleoperation experiments using two state-of-the-art whole-body controllers for humanoid robots.

## 参考
- http://arxiv.org/abs/1909.10080v1

