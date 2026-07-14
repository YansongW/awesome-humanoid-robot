---
$id: ent_paper_liang_end_user_programming_of_low_an_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: End-User Programming of Low- and High-Level Actions for Robotic Task Planning
  zh: 面向机器人任务规划的最终用户低层与高层动作编程
  ko: 로봇 작업 계획을 위한 최종 사용자의 저수준 및 고수준 동작 프로그래밍
summary:
  en: Introduces iRoPro, an interactive Programming-by-Demonstration framework that lets end-users teach robots reusable low-level
    manipulation actions and high-level PDDL-style conditions, then reuses them with a Fast-Forward task planner to solve
    unseen tasks.
  zh: 提出iRoPro交互式演示编程框架，使最终用户能够教授机器人可复用的低层操作动作和高层PDDL风格条件，并结合Fast-Forward任务规划器解决未见过任务。
  ko: 최종 사용자가 재사용 가능한 저수준 조작 동작과 PDDL 스타일의 고수준 조건을 로봇에 가르치고 Fast-Forward 작업 플래너를 활용해 보지 못한 작업을 해결하는 iRoPro 대화형 시연 프로그래밍 프레임워크를
    소개한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- programming_by_demonstration
- task_planning
- pddl
- fast_forward_planner
- end_user_programming
- human_robot_interaction
- manipulation
- baxter
- iropro
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2103.14342v1.
sources:
- id: src_001
  type: paper
  title: End-User Programming of Low- and High-Level Actions for Robotic Task Planning
  url: https://arxiv.org/abs/2103.14342
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Programming robots for general purpose applications is extremely challenging due to the great diversity of end-user tasks ranging from manufacturing environments to personal homes. Recent work has focused on enabling end-users to program robots using Programming by Demonstration. However, teaching robots new actions from scratch that can be reused for unseen tasks remains a difficult challenge and is generally left up to robotic experts. We propose iRoPro, an interactive Robot Programming framework that allows end-users to teach robots new actions from scratch and reuse them with a task planner. In this work we provide a system implementation on a two-armed Baxter robot that (i) allows simultaneous teaching of low- and high-level actions by demonstration, (ii) includes a user interface for action creation with condition inference and modification, and (iii) allows creating and solving previously unseen problems using a task planner for the robot to execute in real-time. We evaluate the generalisation power of the system on six benchmark tasks and show how taught actions can be easily reused for complex tasks. We further demonstrate its usability with a user study (N=21), where users completed eight tasks to teach the robot new actions that are reused with a task planner. The study demonstrates that users with any programming level and educational background can easily learn and use the system.

## 核心内容
Programming robots for general purpose applications is extremely challenging due to the great diversity of end-user tasks ranging from manufacturing environments to personal homes. Recent work has focused on enabling end-users to program robots using Programming by Demonstration. However, teaching robots new actions from scratch that can be reused for unseen tasks remains a difficult challenge and is generally left up to robotic experts. We propose iRoPro, an interactive Robot Programming framework that allows end-users to teach robots new actions from scratch and reuse them with a task planner. In this work we provide a system implementation on a two-armed Baxter robot that (i) allows simultaneous teaching of low- and high-level actions by demonstration, (ii) includes a user interface for action creation with condition inference and modification, and (iii) allows creating and solving previously unseen problems using a task planner for the robot to execute in real-time. We evaluate the generalisation power of the system on six benchmark tasks and show how taught actions can be easily reused for complex tasks. We further demonstrate its usability with a user study (N=21), where users completed eight tasks to teach the robot new actions that are reused with a task planner. The study demonstrates that users with any programming level and educational background can easily learn and use the system.

## 参考
- http://arxiv.org/abs/2103.14342v1

