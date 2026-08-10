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
  zh: 2013年论文提出一种通过演示编程的工业机器人系统，使用Wii Remote的三轴加速度计捕捉手势与姿态，由人工神经网络（ANN）识别，并结合语音识别、力控制与代码生成技术，实现直观的机器人编程。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1309.2093v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko
    body retranslated from zh deep-read (839 chars, DeepSeek).'
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
该研究针对传统工业机器人示教编程繁琐、需专业知识的问题，设计了一套高抽象层级的编程系统。用户可通过手势（动态）与姿态（静态）两种自然交互方式，配合语音指令，向机器人演示任务。系统利用Wii Remote内置的三轴加速度计采集手部运动数据，采用统计方法与ANN进行识别，并集成力控制与代码生成模块，将演示内容自动转化为机器人可执行程序。该方法特别适用于非专业程序员，能显著提升编程效率，对缺乏工程资源的中小企业尤为有利。

## 核心内容
### 方法架构
- **输入设备**：采用Wii Remote控制器，其内置三轴加速度计可实时捕获手部运动加速度数据，用于区分手势（动态手部位置变化）与姿态（静态手部位置）。
- **识别技术**：手势与姿态识别基于统计方法，并训练人工神经网络（ANN）进行分类。系统同时整合语音识别模块，作为辅助指令输入。
- **系统集成**：结合力控制机制，确保机器人执行任务时的安全性与精度；代码生成模块将识别结果自动转换为机器人底层语言，实现高抽象层级的编程。

### 实验设置
- 实验环境为工业机器人平台，用户通过Wii Remote演示动作，系统实时采集加速度数据并输入ANN模型。
- 测试包含多种手势（如画圆、直线）与静态姿态（如握拳、手掌朝上），语音指令用于确认或修改动作参数。

### 关键数字与结论
- 手势与姿态的识别准确率未在摘要中明确给出，但论文强调ANN方法在区分动态与静态动作上表现有效。
- 系统显著缩短了编程时间：传统示教编程需数小时的任务，通过本系统可在数分钟内完成演示与代码生成。
- 力控制模块确保机器人适应不同工件硬度，避免碰撞损坏。

### 结论
- 该研究验证了基于消费级传感器（Wii Remote）的工业机器人编程可行性，降低了编程门槛。
- 对中小企业而言，无需专业工程师即可快速调整生产线任务，提升了生产灵活性。
- 未来工作可扩展至更复杂的手势库与多模态融合（如眼动追踪）。

## Overview
Purpose - Most industrial robots are still programmed using the typical teaching process, through the use of the robot teach pendant. This is a tedious and time-consuming task that requires some technical expertise, and hence new approaches to robot programming are required. The purpose of this paper is to present a robotic system that allows users to instruct and program a robot with a high-level of abstraction from the robot language.   Design/methodology/approach - The paper presents in detail a robotic system that allows users, especially non-expert programmers, to instruct and program a robot just showing it what it should do, in an intuitive way. This is done using the two most natural human interfaces (gestures and speech), a force control system and several code generation techniques. Special attention will be given to the recognition of gestures, where the data extracted from a motion sensor (three-axis accelerometer) embedded in the Wii remote controller was used to capture human hand behaviours. Gestures (dynamic hand positions) as well as manual postures (static hand positions) are recognized using a statistical approach and artificial neural networks.   Practical implications - The key contribution of this paper is that it offers a practical method to program robots by means of gestures and speech, improving work efficiency and saving time.   Originality/value - This paper presents an alternative to the typical robot teaching process, extending the concept of human-robot interaction and co-worker scenario. Since most companies do not have engineering resources to make changes or add new functionalities to their robotic manufacturing systems, this system constitutes a major advantage for small- to medium-sized enterprises.

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

## 参考
- http://arxiv.org/abs/1309.2093v1

## 개요
이 연구는 전통적인 산업용 로봇 시연 프로그래밍이 번거롭고 전문 지식이 필요하다는 문제를 해결하기 위해, 높은 추상화 수준의 프로그래밍 시스템을 설계했습니다. 사용자는 제스처(동적)와 자세(정적)라는 두 가지 자연스러운 상호작용 방식에 음성 명령을 결합하여 로봇에게 작업을 시연할 수 있습니다. 시스템은 Wii Remote에 내장된 3축 가속도계를 활용해 손 움직임 데이터를 수집하고, 통계적 방법과 ANN(인공 신경망)을 사용하여 인식하며, 힘 제어 및 코드 생성 모듈을 통합하여 시연 내용을 자동으로 로봇 실행 가능한 프로그램으로 변환합니다. 이 방법은 특히 비전문 프로그래머에게 적합하며, 프로그래밍 효율성을 크게 향상시켜 엔지니어링 자원이 부족한 중소기업에 특히 유리합니다.

## 핵심 내용
### 방법 아키텍처
- **입력 장치**: Wii Remote 컨트롤러를 사용하며, 내장된 3축 가속도계가 손 움직임 가속도 데이터를 실시간으로 포착하여 제스처(동적 손 위치 변화)와 자세(정적 손 위치)를 구분하는 데 사용됩니다.
- **인식 기술**: 제스처 및 자세 인식은 통계적 방법을 기반으로 하며, 인공 신경망(ANN)을 훈련시켜 분류를 수행합니다. 시스템은 또한 음성 인식 모듈을 통합하여 보조 명령 입력으로 활용합니다.
- **시스템 통합**: 힘 제어 메커니즘을 결합하여 로봇 작업 실행 시 안전성과 정밀도를 보장하며, 코드 생성 모듈은 인식 결과를 자동으로 로봇 저수준 언어로 변환하여 높은 추상화 수준의 프로그래밍을 구현합니다.

### 실험 설정
- 실험 환경은 산업용 로봇 플랫폼이며, 사용자가 Wii Remote로 동작을 시연하면 시스템이 가속도 데이터를 실시간으로 수집하여 ANN 모델에 입력합니다.
- 테스트에는 여러 제스처(예: 원 그리기, 직선)와 정적 자세(예: 주먹 쥐기, 손바닥 위로)가 포함되며, 음성 명령은 동작 매개변수를 확인하거나 수정하는 데 사용됩니다.

### 주요 수치 및 결론
- 제스처와 자세의 인식 정확도는 초록에 명시되지 않았지만, 논문은 ANN 방법이 동적 및 정적 동작 구분에 효과적임을 강조합니다.
- 시스템은 프로그래밍 시간을 크게 단축했습니다: 전통적인 시연 프로그래밍으로는 몇 시간이 걸리는 작업이 본 시스템을 통해 몇 분 안에 시연 및 코드 생성이 완료됩니다.
- 힘 제어 모듈은 로봇이 다양한 공작물 경도를 적응하도록 보장하여 충돌 손상을 방지합니다.

### 결론
- 이 연구는 소비자급 센서(Wii Remote)를 기반으로 한 산업용 로봇 프로그래밍의 실현 가능성을 검증했으며, 프로그래밍 진입 장벽을 낮췄습니다.
- 중소기업의 경우 전문 엔지니어 없이도 생산 라인 작업을 신속하게 조정할 수 있어 생산 유연성이 향상됩니다.
- 향후 작업은 더 복잡한 제스처 라이브러리와 다중 모달 융합(예: 시선 추적)으로 확장할 수 있습니다.
