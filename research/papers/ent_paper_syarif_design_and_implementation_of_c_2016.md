---
$id: ent_paper_syarif_design_and_implementation_of_c_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Design and Implementation of Computational Platform for Social-Humanoid Robot Lumen as an Exhibition Guide in Electrical
    Engineering Days 2015
  zh: 社交人形机器人Lumen在2015年电气工程日作为展览向导的计算平台设计与实现
  ko: 2015 전기공학의 날 전시 안내원으로서의 사회적 인간형 로봇 Lumen의 컴퓨팅 플랫폼 설계 및 구현
summary:
  en: This paper presents Lumen Server, an AMQP/RabbitMQ-based middleware that connects the NAO robot with independently developed
    AI modules, and describes Lumen Motion (a Mamdani fuzzy-logic head controller) and a finite-state-machine/event-driven
    integration program that enabled a NAO robot to serve as a tour guide during Electrical Engineering Days 2015.
  zh: 本文介绍了Lumen Server，一种基于AMQP/RabbitMQ的中间件，用于连接NAO机器人与独立开发的AI模块，并描述了Lumen Motion（基于Mamdani模糊逻辑的头部控制器）以及一个有限状态机/事件驱动的集成程序，该程序使NAO机器人能够在2015年电气工程日展览中担任导游。
  ko: 본 논문은 NAO 로봇과 독립적으로 개발된 AI 모듈을 연결하는 AMQP/RabbitMQ 기반 미들웨어인 Lumen Server를 제시하고, Mamdani 퍼지 로직 헤드 컨트롤러인 Lumen Motion과
    2015 전기공학의 날 전시회에서 NAO 로봇이 투어 가이드 역할을 할 수 있게 한 FSM/이벤트 기반 통합 프로그램을 설명한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1607.04763v1.
sources:
- id: src_001
  type: paper
  title: Design and Implementation of Computational Platform for Social-Humanoid Robot Lumen as an Exhibition Guide in Electrical
    Engineering Days 2015
  url: https://arxiv.org/abs/1607.04763
  date: '2016'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Social Robot Lumen is an Artificial Intelligence development project that aims to create an Artificial Intelligence (AI) which allows a humanoid robot to communicate with human being naturally. In this study, Lumen will be developed to be a tour guide in Electrical Engineering Days 2015 exhibition. In developing an AI, there are a lot of modules that need to be developed separately. To make the development easier, we need a computational platform which becomes basis for all developers to give easiness in developing the modules in parallel way. That computational platform that developed by the writer is called Lumen Server. Lumen Server has two main function, which are to be a bridge between all Lumen intelligence modules with NAO robot, and to be the communication bridge between those Lumen intelligence modules. For the second function, Lumen Server implements the AMQP protocol using RabbitMQ. Besides that, writer also developed a control system for robot movement called Lumen Motion. Lumen motion is implemented by modelling the movement of NAO robot and also by creating a control system using fuzzy logic controller. Writer also developed a program that connects all Lumen intelligence modules so that Lumen can act like a tour guide. The implementation of this program uses FSM and event-driven program. From implementation result, all the features which were designed are successfully implemented. By the developing of this computational platform, it can ease the development of Lumen in the future. For next development, it must be focused on creating integration system so that Lumen can be more responsive to the environment.   -----   Sosial Robot Lumen adalah proyek pengembangan kecerdasan buatan yang bertujuan untuk menciptakan kecerdasan buatan atau artificial intelligence (AI) yang memungkinkan robot untuk dapat berkomunikasi dengan manusia secara alami.

## 核心内容
Social Robot Lumen is an Artificial Intelligence development project that aims to create an Artificial Intelligence (AI) which allows a humanoid robot to communicate with human being naturally. In this study, Lumen will be developed to be a tour guide in Electrical Engineering Days 2015 exhibition. In developing an AI, there are a lot of modules that need to be developed separately. To make the development easier, we need a computational platform which becomes basis for all developers to give easiness in developing the modules in parallel way. That computational platform that developed by the writer is called Lumen Server. Lumen Server has two main function, which are to be a bridge between all Lumen intelligence modules with NAO robot, and to be the communication bridge between those Lumen intelligence modules. For the second function, Lumen Server implements the AMQP protocol using RabbitMQ. Besides that, writer also developed a control system for robot movement called Lumen Motion. Lumen motion is implemented by modelling the movement of NAO robot and also by creating a control system using fuzzy logic controller. Writer also developed a program that connects all Lumen intelligence modules so that Lumen can act like a tour guide. The implementation of this program uses FSM and event-driven program. From implementation result, all the features which were designed are successfully implemented. By the developing of this computational platform, it can ease the development of Lumen in the future. For next development, it must be focused on creating integration system so that Lumen can be more responsive to the environment.   -----   Sosial Robot Lumen adalah proyek pengembangan kecerdasan buatan yang bertujuan untuk menciptakan kecerdasan buatan atau artificial intelligence (AI) yang memungkinkan robot untuk dapat berkomunikasi dengan manusia secara alami.

## 参考
- http://arxiv.org/abs/1607.04763v1

