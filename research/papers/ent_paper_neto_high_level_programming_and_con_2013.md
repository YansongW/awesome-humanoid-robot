---
$id: ent_paper_neto_high_level_programming_and_con_2013
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'High-level programming and control for industrial robotics: using a hand-held
    accelerometer-based input device for gesture and posture recognition'
  zh: 基于手持加速度计输入设备的工业机器人高级编程与控制：手势与姿态识别
  ko: '손held 가속도계 기반 입력 장치를 이용한 산업용 로봇의 고급 프로그래밍 및 제어: 제스처와 자세 인식'
summary:
  en: A 2013 paper presenting a programming-by-demonstration system where a Wii Remote's
    3-axis accelerometer captures hand gestures and postures recognized by ANNs, combined
    with speech recognition, force control, and code generation to program industrial
    robots intuitively.
  zh: 2013年发表的论文，提出了一种示教编程系统，利用Wii Remote内置的三轴加速度计捕捉手部手势与姿态，并通过人工神经网络识别，结合语音识别、力控制和代码生成，实现对工业机器人的直观编程。
  ko: 2013년 발표된 논문으로, Wii Remote의 3축 가속도계로 손 제스처와 자세를 포착하고 인공신경망으로 인식한 뒤, 음성 인식, 힘
    제어, 코드 생성과 결합하여 산업용 로봇을 직관적으로 프로그래밍하는 시연 기반 프로그래밍 시스템을 제안한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    needed before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'High-level programming and control for industrial robotics: using a hand-held
    accelerometer-based input device for gesture and posture recognition'
  url: https://arxiv.org/abs/1309.2093
  date: '2013'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Industrial robots are traditionally programmed through teach pendants, a process that is tedious, time-consuming, and requires specialized expertise. This paper proposes a programming-by-demonstration framework that lowers the barrier for non-expert users by letting them instruct robots through natural human interfaces—specifically hand gestures and speech. The hand gestures and postures are captured via the 3-axis accelerometer embedded in a Wii Remote Controller and recognized using a statistical approach combined with Artificial Neural Networks.

The framework integrates gesture/posture recognition, automatic speech recognition, force control, and robot code generation. Users can demonstrate tasks at a high level of abstraction without needing to write low-level robot code. The system was evaluated in non-controlled industrial environments and compared against a manual guidance approach based on force control. Demonstrations on two distinct industrial robots, the MOTOMAN HP6 and the ABB IRB 140, show that the approach can be adapted to different users and robotic platforms.

Key reported performance metrics include a 96% recognition rate for trained users and a system response time of approximately 140 ms. For untrained users, recognition performance dropped to about 82%, highlighting the importance of user-specific training.

## Key Contributions

- Accelerometer-based gesture and posture recognition using a Wii Remote and Artificial Neural Networks for industrial robot control.
- Unified programming-by-demonstration framework integrating gesture recognition, speech recognition, force control, and robot code generation.
- Experimental validation on two different industrial robots (MOTOMAN HP6 and ABB IRB 140) in non-controlled industrial environments.
- Performance comparison between the gesture-based interface and a manual guidance system relying on force control.
- Reported 96% recognition rate for trained users and 140 ms system response time.

## Relevance to Humanoid Robotics

Although the paper focuses on conventional industrial manipulators, its core ideas are directly transferable to humanoid robots. Natural programming-by-demonstration through gestures and speech is especially relevant for humanoids intended to operate alongside humans in manufacturing or collaborative settings, where intuitive instruction can reduce deployment cost and expertise requirements. The accelerometer-based gesture/posture recognition pipeline and the integration of multimodal human-robot interfaces can inform middleware and control architectures for humanoid systems.
