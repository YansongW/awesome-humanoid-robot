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
  en: This survey reviews robot manipulation tasks that require sustained or controlled
    contact with the environment, categorizing in-contact tasks, low-level control
    strategies, skill representations, and planning or learning approaches, and identifies
    open challenges in deformable objects, exception handling, and sim-to-real transfer.
  zh: 本综述回顾了需要与环境保持持续或受控接触的机器人操作任务，对接触式任务、底层控制策略、技能表示以及规划或学习方法进行了分类，并指出了可变形物体、异常处理和仿真到现实迁移中的开放挑战。
  ko: 본 서베이는 환경과의 지속적이거나 제어된 접촉을 필요로 하는 로봇 조작 작업을 검토하고, 접촉 작업, 저수준 제어 전략, 스킬 표현, 계획
    및 학습 방법을 분류하며, 변형 가능한 물체, 예외 처리, 시뮬레이션에서 실제로의 전이에서의 미해결 과제를 제시한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv abstract and the provided metadata; requires
    human review against the full text before verification.
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

## Overview

A Survey of Robot Manipulation in Contact surveys the state of the art in robotic manipulation tasks that require robots to maintain and regulate physical contact with the environment. The authors focus on tasks that either intrinsically require contact, such as polishing, insertion, and assembly, or tasks that exploit contact to mitigate uncertainty, such as pushing or sliding an object into alignment. The survey is organized around a task taxonomy, low-level control methods, skill representations, and the planning or learning methods used to acquire in-contact skills.

The paper distinguishes three broad task categories: environment shaping, workpiece alignment, and articulated motions. It then reviews how these tasks are controlled, covering force control, impedance control, and admittance control, and how contact skills are represented as continuous or discrete policies. Finally, it discusses planning, imitation learning, and reinforcement learning approaches for contact-rich manipulation, including recent advances in generalization, error tolerance, and sim-to-real transfer. The authors conclude by identifying open challenges, including deformable-object manipulation, exception handling, and hardware compliance.

The work is positioned as a methodological survey: it does not introduce a new algorithm or robotic system, but synthesizes existing literature into a structured taxonomy and highlights trends across tasks, control, representation, and learning.

## Key Contributions

- Taxonomy of in-contact manipulation tasks into environment shaping, workpiece alignment, and articulated motions.
- Survey of low-level control methods for contact, including force, impedance, and admittance control.
- Review of continuous and discrete policy representations used for in-contact skills.
- Overview of planning, imitation learning, and reinforcement learning approaches for contact-rich manipulation.
- Identification of open challenges and future research directions in deformable objects, exception handling, and sim-to-real transfer.

## Relevance to Humanoid Robotics

Contact-rich manipulation is a core capability for humanoid robots deployed in unstructured industrial, service, and domestic environments. Humanoids must routinely perform assembly, tool use, and physical assistance tasks where maintaining controlled contact with objects, tools, and people is unavoidable. This survey provides a structured map of the methods—force and impedance control, policy representations, and learning algorithms—that enable reliable and generalizable in-contact skills at scale.

For the knowledge base, the paper is most useful as a background reference linking high-level humanoid application domains to concrete control and learning techniques. Its coverage of peg-in-hole, small-part assembly, massage, and other contact tasks directly supports entries in applications_markets and components, while its treatment of reinforcement learning and imitation learning reinforces entries in ai_models_algorithms.
