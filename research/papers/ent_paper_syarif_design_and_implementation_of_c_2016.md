---
$id: ent_paper_syarif_design_and_implementation_of_c_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Design and Implementation of Computational Platform for Social-Humanoid Robot
    Lumen as an Exhibition Guide in Electrical Engineering Days 2015
  zh: 社交人形机器人Lumen在2015年电气工程日作为展览向导的计算平台设计与实现
  ko: 2015 전기공학의 날 전시 안내원으로서의 사회적 인간형 로봇 Lumen의 컴퓨팅 플랫폼 설계 및 구현
summary:
  en: This paper presents Lumen Server, an AMQP/RabbitMQ-based middleware that connects
    the NAO robot with independently developed AI modules, and describes Lumen Motion
    (a Mamdani fuzzy-logic head controller) and a finite-state-machine/event-driven
    integration program that enabled a NAO robot to serve as a tour guide during Electrical
    Engineering Days 2015.
  zh: 本文介绍了Lumen Server，一种基于AMQP/RabbitMQ的中间件，用于连接NAO机器人与独立开发的AI模块，并描述了Lumen Motion（基于Mamdani模糊逻辑的头部控制器）以及一个有限状态机/事件驱动的集成程序，该程序使NAO机器人能够在2015年电气工程日展览中担任导游。
  ko: 본 논문은 NAO 로봇과 독립적으로 개발된 AI 모듈을 연결하는 AMQP/RabbitMQ 기반 미들웨어인 Lumen Server를 제시하고,
    Mamdani 퍼지 로직 헤드 컨트롤러인 Lumen Motion과 2015 전기공학의 날 전시회에서 NAO 로봇이 투어 가이드 역할을 할 수
    있게 한 FSM/이벤트 기반 통합 프로그램을 설명한다.
domains:
- 08_software_middleware
- 11_applications_markets
- 06_design_engineering
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- nao_robot
- rabbitmq
- amqp
- middleware
- tour_guide_robot
- mamdani_fuzzy_logic
- finite_state_machine
- event_driven_programming
- social_humanoid_robot
- lumen_server
- lumen_motion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from arXiv PDF; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Design and Implementation of Computational Platform for Social-Humanoid Robot
    Lumen as an Exhibition Guide in Electrical Engineering Days 2015
  url: https://arxiv.org/abs/1607.04763
  date: '2016'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## Overview

This paper describes the Lumen project, which aimed to develop artificial intelligence that lets a humanoid robot communicate naturally with humans. For the Electrical Engineering Days 2015 exhibition, the authors built Lumen Server, a computational platform that connects all Lumen intelligence modules to the NAO robot and to each other. Lumen Server uses RabbitMQ to implement the AMQP protocol, with routing keys beginning with 'avatar' for robot-facing modules and 'lumen' for intelligence modules.

In addition to the server, the authors developed Lumen Motion, a motion-control subsystem for the NAO robot. It includes a Mamdani fuzzy-logic head controller that keeps the robot's head oriented toward a visitor's face using the linguistic variables FaceXLoc, FaceYLoc, AngleX, and AngleY. Walking, postures, and predefined gestures such as dancing, singing, and hand-waving are implemented through the NAOqi API.

Finally, the paper presents an AI integration layer that combines all Lumen intelligence modules into tour-guide behavior. This integration program is built with a finite-state machine and event-driven programming. The authors report that all designed features were successfully implemented and demonstrated during the exhibition.

## Key Contributions

- Lumen Server bridges the NAO robot and all Lumen intelligence modules via RabbitMQ/AMQP messaging.
- A Mamdani fuzzy logic controller keeps the NAO head oriented toward a visitor's face.
- An FSM/event-driven integration program coordinates all intelligence modules to produce tour-guide behavior.
- The complete system is implemented and demonstrated on the NAO humanoid robot during Electrical Engineering Days 2015.

## Relevance to Humanoid Robotics

The work is relevant to humanoid robotics because it presents a practical middleware and integration architecture for deploying a NAO humanoid robot as a social tour guide. It illustrates how modular AI, motion control, and messaging infrastructure can be combined for real-world humanoid robot applications. The platform also provides an example of how fuzzy-logic-based gaze control and state-machine-based behavior coordination can be layered onto a commercial humanoid platform.
