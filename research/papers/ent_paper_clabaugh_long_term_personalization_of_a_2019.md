---
$id: ent_paper_clabaugh_long_term_personalization_of_a_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Long-Term Personalization of an In-Home Socially Assistive Robot for Children
    with Autism Spectrum Disorders
  zh: 面向自闭症谱系障碍儿童的居家社交辅助机器人长期个性化研究
  ko: 자폐 스펙트럼 장애 아동을 위한 가정 내 사회적 보조 로봇의 장기적 개인화
summary:
  en: Presents a hierarchical human-robot learning framework that uses Q-learning
    to autonomously personalize instructional challenge and feedback levels for 17
    children with autism spectrum disorders during month-long in-home interventions
    with a socially assistive robot.
  zh: 提出一种层级式人机学习框架，利用Q学习在为期一个月的家庭干预中自主为17名自闭症谱系障碍儿童个性化教学挑战与反馈水平。
  ko: 사회적 보조 로봇을 활용한 한 달간의 가정 내 개입 동안 Q-러닝을 사용하여 17명의 자폐 스펙트럼 장애 아동을 대상으로 교육적 도전 수준과
    피드백 수준을 자율적으로 개인화하는 계층적 인간-로봇 학습 프레임워크를 제시한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- socially_assistive_robot
- reinforcement_learning
- q_learning
- personalization
- hierarchical_framework
- autism_therapy
- in_home_intervention
- longitudinal_study
- child_robot_interaction
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    full text before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Long-Term Personalization of an In-Home Socially Assistive Robot for Children
    with Autism Spectrum Disorders
  url: https://arxiv.org/abs/1911.07992
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper addresses the challenge of autonomous personalization for socially assistive robots (SAR) deployed in real homes over extended periods. The authors formalize personalization as a hierarchical human-robot learning (hHRL) framework in which a meta-controller selects among five lower-level controllers—disclosure, promise, instruction, feedback, and inquiry—to adapt the robot's behavior to each child's unique and changing needs. The meta-controller uses Q-learning reinforcement learning to personalize both the level of instructional challenge and the level of feedback based on each child's learning patterns.

The framework is instantiated on the SPRITE robot platform and evaluated in a month-long, fully autonomous, in-home study with 17 children with autism spectrum disorders (ASD), aged 3 to 7 years old. The robot delivered early mathematics instruction and adapted its behavior without human intervention. Outcomes were measured using the Wechsler Individual Achievement Test II (WIAT II) and through engagement and usability reports from families.

Results indicate that the system successfully personalized instruction and feedback over time, every child showed improvements in targeted skills and long-term retention of intervention content, children remained engaged for the majority of sessions, and families rated the system as useful and adaptable.

## Key Contributions

- Formalization of human-robot learning (HRL) and its hierarchical extension (hHRL) into five controllers: instruction, promise, feedback, disclosure, and inquiry.
- Q-learning-based personalization of challenge level and feedback level using reward functions tailored to individual children.
- Month-long fully autonomous in-home deployment with 17 children with ASD aged 3–7.
- Empirical evidence of math skill improvements, long-term retention, sustained engagement, and positive family perceptions.
- Demonstration that autonomous personalized SAR interventions are feasible and effective for long-term developmental support.

## Relevance to Humanoid Robotics

Although the study uses a small tabletop assistive robot rather than a full humanoid, the reinforcement-learning personalization framework, the long-term in-home deployment methodology, and the findings on engagement and adaptive feedback are directly transferable to future humanoid robots. As humanoids are increasingly considered for education, therapy, and home assistance, scalable personalization mechanisms such as hHRL and Q-learning-based adaptation will be essential for meeting diverse and evolving user needs over repeated long-term interactions.
