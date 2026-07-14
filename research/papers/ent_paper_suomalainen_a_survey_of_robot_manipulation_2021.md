---
$id: ent_paper_suomalainen_a_survey_of_robot_manipulation_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Survey of Robot Manipulation in Contact
  zh: 接触式机器人操作综述
  ko: 접촉 상태에서의 로봇 조작에 대한 서베이
summary:
  en: This survey reviews robot manipulation tasks that require sustained or controlled contact with the environment, categorizing
    in-contact tasks, low-level control strategies, skill representations, and planning or learning approaches, and identifies
    open challenges in deformable objects, exception handling, and sim-to-real transfer.
  zh: 本综述回顾了需要与环境保持持续或受控接触的机器人操作任务，对接触式任务、底层控制策略、技能表示以及规划或学习方法进行了分类，并指出了可变形物体、异常处理和仿真到现实迁移中的开放挑战。
  ko: 본 서베이는 환경과의 지속적이거나 제어된 접촉을 필요로 하는 로봇 조작 작업을 검토하고, 접촉 작업, 저수준 제어 전략, 스킬 표현, 계획 및 학습 방법을 분류하며, 변형 가능한 물체, 예외 처리, 시뮬레이션에서
    실제로의 전이에서의 미해결 과제를 제시한다.
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
- contact_rich_manipulation
- force_control
- impedance_control
- admittance_control
- manipulation_survey
- peg_in_hole
- assembly
- reinforcement_learning
- imitation_learning
- sim_to_real
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2112.01942v3.
sources:
- id: src_001
  type: paper
  title: A Survey of Robot Manipulation in Contact
  url: https://arxiv.org/abs/2112.01942
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
In this survey, we present the current status on robots performing manipulation tasks that require varying contact with the environment, such that the robot must either implicitly or explicitly control the contact force with the environment to complete the task. Robots can perform more and more manipulation tasks that are still done by humans, and there is a growing number of publications on the topics of 1) performing tasks that always require contact and 2) mitigating uncertainty by leveraging the environment in tasks that, under perfect information, could be performed without contact. The recent trends have seen robots perform tasks earlier left for humans, such as massage, and in the classical tasks, such as peg-in-hole, there is a more efficient generalization to other similar tasks, better error tolerance, and faster planning or learning of the tasks. Thus, in this survey we cover the current stage of robots performing such tasks, starting from surveying all the different in-contact tasks robots can perform, observing how these tasks are controlled and represented, and finally presenting the learning and planning of the skills required to complete these tasks.

## 核心内容
In this survey, we present the current status on robots performing manipulation tasks that require varying contact with the environment, such that the robot must either implicitly or explicitly control the contact force with the environment to complete the task. Robots can perform more and more manipulation tasks that are still done by humans, and there is a growing number of publications on the topics of 1) performing tasks that always require contact and 2) mitigating uncertainty by leveraging the environment in tasks that, under perfect information, could be performed without contact. The recent trends have seen robots perform tasks earlier left for humans, such as massage, and in the classical tasks, such as peg-in-hole, there is a more efficient generalization to other similar tasks, better error tolerance, and faster planning or learning of the tasks. Thus, in this survey we cover the current stage of robots performing such tasks, starting from surveying all the different in-contact tasks robots can perform, observing how these tasks are controlled and represented, and finally presenting the learning and planning of the skills required to complete these tasks.

## 参考
- http://arxiv.org/abs/2112.01942v3

