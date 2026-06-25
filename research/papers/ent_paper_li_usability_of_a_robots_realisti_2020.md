---
$id: ent_paper_li_usability_of_a_robots_realisti_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Usability of a Robot's Realistic Facial Expressions and Peripherals in Autistic
    Children's Therapy
  zh: 机器人真实面部表情及外设在自闭症儿童治疗中的可用性研究
  ko: 자폐 아동 치료에서 로봇의 사실적 표정 및 주변 장치의 사용성
summary:
  en: This paper reports usability tests in which 19 autistic children interacted
    with a Zeno humanoid robot and a therapist during emotion-learning activities,
    comparing realistic corpus-based and live-mirrored facial expressions with exaggerated
    expressions and evaluating tablet and tangible squishy peripherals for child-led
    control.
  zh: 本研究报告了一项可用性测试：19名自闭症儿童在人形机器人Zeno和治疗师陪伴下参与情绪学习活动，比较了基于语料库的真实表情、实时镜像表情与夸张表情的效果，并评估了平板电脑及可捏触觉方块作为儿童主导控制外设的可用性。
  ko: 본 논문은 19명의 자폐 아동이 치료사와 함께 Zeno 휴머노이드 로봇을 이용한 감정 학습 활동에 참여한 사용성 테스트를 보고하며, 코퍼스
    기반 사실적 표정과 실시간 거울 표정을 과장된 표정과 비교하고 아동 주도형 제어를 위한 태블릿과 촉각 스퀴시 주변 장치를 평가한다.
domains:
- 11_applications_markets
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- system
tags:
- autism_therapy
- robot_assisted_therapy
- facial_expressions
- zeno_robot
- child_robot_interaction
- tangible_interface
- tablet_interface
- emotion_learning
- assistive_robotics
- live_mirroring
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text section-level
    verification not performed.
sources:
- id: src_001
  type: paper
  title: Usability of a Robot's Realistic Facial Expressions and Peripherals in Autistic
    Children's Therapy
  url: https://arxiv.org/abs/2007.12236
  date: '2020'
  accessed_at: '2026-06-26'
---


## Overview

The study investigates how realistic facial expressions and child-controlled peripherals affect the usability of a small humanoid robot in therapy for autistic children. Nineteen autistic children participated in emotion-learning activities with a Zeno robot and an adult therapist. The activities compared two approaches to realistic facial expressions: expressions modelled on a pre-existing database (the Denver corpus) and expressions created by live mirroring of the child's own face. The study also tested two types of peripherals—tablet screens and tangible squishy blocks—as interfaces that let children lead or control parts of the activity.

The authors found that both forms of realistic facial expressions were less effective than exaggerated or caricatured expressions for engaging the children. Live mirroring, in particular, was difficult for children to understand and sometimes produced anxiety because of jerky robot motion. The tablet was usable as a child-led interface, but the authors note that it required immediate feedback and a latency of one second or less to work well. The squishy tangible blocks were engaging and supported functional play without preventing children from returning attention to the robot, although re-engagement depended on how much attention the child had paid to the robot beforehand.

The work contributes practical design guidance for robot-assisted autism therapy, emphasizing the importance of expression style, interface latency, feedback, and the balance between robot-directed and tangible play activities.

## Key Contributions

- Realistic facial expressions were less effective than exaggerated/caricatured expressions for engaging autistic children.
- Live facial mirroring of the child's face was largely unintuitive and sometimes anxiety-inducing due to jerky robot motions.
- Tablets were usable as child-led interfaces but required immediate feedback and a latency of one second or less.
- Tangible squishy blocks were engaging aids that supported functional play without preventing re-engagement with the robot.
- Re-engagement with the robot after tangible play depended on the child's prior attention to the robot.

## Relevance to Humanoid Robotics

The paper directly evaluates the Zeno small humanoid robot in real autism-therapy sessions, making it relevant for assistive and therapeutic applications of humanoid robots. Its findings on facial-expression design, system latency, feedback timing, and tangible peripherals provide concrete guidelines for engineers and interaction designers building humanoid robots for children with autism. Because the study identifies trade-offs between realistic and exaggerated expressions and between screen-based and tangible interfaces, it informs choices that affect both the hardware peripherals and the behavioral software of future humanoid platforms.
