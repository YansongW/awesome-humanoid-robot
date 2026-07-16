---
$id: ent_paper_neto_high_level_programming_and_con_2013
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'High-level programming and control for industrial robotics: using a hand-held accelerometer-based input device for
    gesture and posture recognition'
  zh: 基于手持加速度计输入设备的工业机器人高级编程与控制：手势与姿态识别
  ko: '손held 가속도계 기반 입력 장치를 이용한 산업용 로봇의 고급 프로그래밍 및 제어: 제스처와 자세 인식'
summary:
  en: A 2013 paper presenting a programming-by-demonstration system where a Wii Remote's 3-axis accelerometer captures hand
    gestures and postures recognized by ANNs, combined with speech recognition, force control, and code generation to program
    industrial robots intuitively.
  zh: 2013年发表的论文，提出了一种示教编程系统，利用Wii Remote内置的三轴加速度计捕捉手部手势与姿态，并通过人工神经网络识别，结合语音识别、力控制和代码生成，实现对工业机器人的直观编程。
  ko: 2013년 발표된 논문으로, Wii Remote의 3축 가속도계로 손 제스처와 자세를 포착하고 인공신경망으로 인식한 뒤, 음성 인식, 힘 제어, 코드 생성과 결합하여 산업용 로봇을 직관적으로 프로그래밍하는 시연
    기반 프로그래밍 시스템을 제안한다.
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
- system
tags:
- gesture_recognition
- programming_by_demonstration
- industrial_robotics
- accelerometer
- wii_remote
- human_robot_interaction
- artificial_neural_network
- speech_recognition
- force_control
- code_generation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1309.2093v1.
sources:
- id: src_001
  type: paper
  title: 'High-level programming and control for industrial robotics: using a hand-held accelerometer-based input device for
    gesture and posture recognition'
  url: https://arxiv.org/abs/1309.2093
  date: '2013'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Purpose - Most industrial robots are still programmed using the typical teaching process, through the use of the robot teach pendant. This is a tedious and time-consuming task that requires some technical expertise, and hence new approaches to robot programming are required. The purpose of this paper is to present a robotic system that allows users to instruct and program a robot with a high-level of abstraction from the robot language.   Design/methodology/approach - The paper presents in detail a robotic system that allows users, especially non-expert programmers, to instruct and program a robot just showing it what it should do, in an intuitive way. This is done using the two most natural human interfaces (gestures and speech), a force control system and several code generation techniques. Special attention will be given to the recognition of gestures, where the data extracted from a motion sensor (three-axis accelerometer) embedded in the Wii remote controller was used to capture human hand behaviours. Gestures (dynamic hand positions) as well as manual postures (static hand positions) are recognized using a statistical approach and artificial neural networks.   Practical implications - The key contribution of this paper is that it offers a practical method to program robots by means of gestures and speech, improving work efficiency and saving time.   Originality/value - This paper presents an alternative to the typical robot teaching process, extending the concept of human-robot interaction and co-worker scenario. Since most companies do not have engineering resources to make changes or add new functionalities to their robotic manufacturing systems, this system constitutes a major advantage for small- to medium-sized enterprises.

## 核心内容
Purpose - Most industrial robots are still programmed using the typical teaching process, through the use of the robot teach pendant. This is a tedious and time-consuming task that requires some technical expertise, and hence new approaches to robot programming are required. The purpose of this paper is to present a robotic system that allows users to instruct and program a robot with a high-level of abstraction from the robot language.   Design/methodology/approach - The paper presents in detail a robotic system that allows users, especially non-expert programmers, to instruct and program a robot just showing it what it should do, in an intuitive way. This is done using the two most natural human interfaces (gestures and speech), a force control system and several code generation techniques. Special attention will be given to the recognition of gestures, where the data extracted from a motion sensor (three-axis accelerometer) embedded in the Wii remote controller was used to capture human hand behaviours. Gestures (dynamic hand positions) as well as manual postures (static hand positions) are recognized using a statistical approach and artificial neural networks.   Practical implications - The key contribution of this paper is that it offers a practical method to program robots by means of gestures and speech, improving work efficiency and saving time.   Originality/value - This paper presents an alternative to the typical robot teaching process, extending the concept of human-robot interaction and co-worker scenario. Since most companies do not have engineering resources to make changes or add new functionalities to their robotic manufacturing systems, this system constitutes a major advantage for small- to medium-sized enterprises.

## 参考
- http://arxiv.org/abs/1309.2093v1

## Overview
Purpose - Most industrial robots are still programmed using the typical teaching process, through the use of the robot teach pendant. This is a tedious and time-consuming task that requires some technical expertise, and hence new approaches to robot programming are required. The purpose of this paper is to present a robotic system that allows users to instruct and program a robot with a high-level of abstraction from the robot language.  
Design/methodology/approach - The paper presents in detail a robotic system that allows users, especially non-expert programmers, to instruct and program a robot just showing it what it should do, in an intuitive way. This is done using the two most natural human interfaces (gestures and speech), a force control system and several code generation techniques. Special attention will be given to the recognition of gestures, where the data extracted from a motion sensor (three-axis accelerometer) embedded in the Wii remote controller was used to capture human hand behaviours. Gestures (dynamic hand positions) as well as manual postures (static hand positions) are recognized using a statistical approach and artificial neural networks.  
Practical implications - The key contribution of this paper is that it offers a practical method to program robots by means of gestures and speech, improving work efficiency and saving time.  
Originality/value - This paper presents an alternative to the typical robot teaching process, extending the concept of human-robot interaction and co-worker scenario. Since most companies do not have engineering resources to make changes or add new functionalities to their robotic manufacturing systems, this system constitutes a major advantage for small- to medium-sized enterprises.

## Content
Purpose - Most industrial robots are still programmed using the typical teaching process, through the use of the robot teach pendant. This is a tedious and time-consuming task that requires some technical expertise, and hence new approaches to robot programming are required. The purpose of this paper is to present a robotic system that allows users to instruct and program a robot with a high-level of abstraction from the robot language.  
Design/methodology/approach - The paper presents in detail a robotic system that allows users, especially non-expert programmers, to instruct and program a robot just showing it what it should do, in an intuitive way. This is done using the two most natural human interfaces (gestures and speech), a force control system and several code generation techniques. Special attention will be given to the recognition of gestures, where the data extracted from a motion sensor (three-axis accelerometer) embedded in the Wii remote controller was used to capture human hand behaviours. Gestures (dynamic hand positions) as well as manual postures (static hand positions) are recognized using a statistical approach and artificial neural networks.  
Practical implications - The key contribution of this paper is that it offers a practical method to program robots by means of gestures and speech, improving work efficiency and saving time.  
Originality/value - This paper presents an alternative to the typical robot teaching process, extending the concept of human-robot interaction and co-worker scenario. Since most companies do not have engineering resources to make changes or add new functionalities to their robotic manufacturing systems, this system constitutes a major advantage for small- to medium-sized enterprises.

## 개요
목적 - 대부분의 산업용 로봇은 여전히 로봇 티치 펜던트를 사용하는 일반적인 교육 과정을 통해 프로그래밍됩니다. 이는 기술적 전문 지식이 필요한 지루하고 시간 소모적인 작업이므로, 로봇 프로그래밍에 대한 새로운 접근 방식이 필요합니다. 본 논문의 목적은 사용자가 로봇 언어로부터 높은 수준의 추상화를 통해 로봇을 지시하고 프로그래밍할 수 있는 로봇 시스템을 제시하는 것입니다.  
설계/방법론/접근법 - 본 논문은 특히 비전문 프로그래머인 사용자가 직관적인 방식으로 로봇이 수행해야 할 작업을 보여주기만 하면 로봇을 지시하고 프로그래밍할 수 있는 로봇 시스템을 상세히 제시합니다. 이는 가장 자연스러운 두 가지 인간 인터페이스(제스처와 음성), 힘 제어 시스템 및 여러 코드 생성 기술을 사용하여 수행됩니다. 특히 제스처 인식에 중점을 두며, Wii 리모컨에 내장된 모션 센서(3축 가속도계)에서 추출한 데이터를 사용하여 인간 손 동작을 포착합니다. 제스처(동적 손 위치)와 수동 자세(정적 손 위치)는 통계적 접근 방식과 인공 신경망을 사용하여 인식됩니다.  
실용적 의미 - 본 논문의 주요 기여는 제스처와 음성을 통해 로봇을 프로그래밍하는 실용적인 방법을 제공하여 작업 효율성을 향상시키고 시간을 절약한다는 점입니다.  
독창성/가치 - 본 논문은 일반적인 로봇 교육 과정에 대한 대안을 제시하며, 인간-로봇 상호작용 및 협업 시나리오의 개념을 확장합니다. 대부분의 기업이 로봇 제조 시스템을 변경하거나 새로운 기능을 추가할 엔지니어링 자원을 보유하지 못하기 때문에, 이 시스템은 중소기업에 큰 이점을 제공합니다.

## 핵심 내용
목적 - 대부분의 산업용 로봇은 여전히 로봇 티치 펜던트를 사용하는 일반적인 교육 과정을 통해 프로그래밍됩니다. 이는 기술적 전문 지식이 필요한 지루하고 시간 소모적인 작업이므로, 로봇 프로그래밍에 대한 새로운 접근 방식이 필요합니다. 본 논문의 목적은 사용자가 로봇 언어로부터 높은 수준의 추상화를 통해 로봇을 지시하고 프로그래밍할 수 있는 로봇 시스템을 제시하는 것입니다.  
설계/방법론/접근법 - 본 논문은 특히 비전문 프로그래머인 사용자가 직관적인 방식으로 로봇이 수행해야 할 작업을 보여주기만 하면 로봇을 지시하고 프로그래밍할 수 있는 로봇 시스템을 상세히 제시합니다. 이는 가장 자연스러운 두 가지 인간 인터페이스(제스처와 음성), 힘 제어 시스템 및 여러 코드 생성 기술을 사용하여 수행됩니다. 특히 제스처 인식에 중점을 두며, Wii 리모컨에 내장된 모션 센서(3축 가속도계)에서 추출한 데이터를 사용하여 인간 손 동작을 포착합니다. 제스처(동적 손 위치)와 수동 자세(정적 손 위치)는 통계적 접근 방식과 인공 신경망을 사용하여 인식됩니다.  
실용적 의미 - 본 논문의 주요 기여는 제스처와 음성을 통해 로봇을 프로그래밍하는 실용적인 방법을 제공하여 작업 효율성을 향상시키고 시간을 절약한다는 점입니다.  
독창성/가치 - 본 논문은 일반적인 로봇 교육 과정에 대한 대안을 제시하며, 인간-로봇 상호작용 및 협업 시나리오의 개념을 확장합니다. 대부분의 기업이 로봇 제조 시스템을 변경하거나 새로운 기능을 추가할 엔지니어링 자원을 보유하지 못하기 때문에, 이 시스템은 중소기업에 큰 이점을 제공합니다.
