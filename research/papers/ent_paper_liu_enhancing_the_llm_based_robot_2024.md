---
$id: ent_paper_liu_enhancing_the_llm_based_robot_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enhancing the LLM-Based Robot Manipulation Through Human-Robot Collaboration
  zh: 通过人机协作增强基于大语言模型的机器人操作
  ko: 인간-로봇 협업을 통한 LLM 기반 로봇 조작 향상
summary:
  en: Proposes a GPT-4-based hierarchical planning framework integrated with YOLOv5 visual perception and a teleoperation-DMP
    human-robot collaboration mechanism, validated on the Toyota Human Support Robot for complex manipulation tasks.
  zh: Large Language Models (LLMs) are gaining popularity in the field of robotics. However, LLM-based robots are limited
    to simple, repetitive motions due to the poor integration between language models, robots, and the environment. This paper
    proposes a novel approach to enhance the performance of LLM-based autonomous manipulation through Human-Robot Collaboration
    (HRC). The approach involves using a prompted GPT-4 language model to decompose high-level language commands into sequences
    of motions that can be executed by the robot. The system also employs a YOLO-based perception algorithm, providin
  ko: YOLOv5 시각 인식 및 텔레오퍼레이션-DMP 인간-로봇 협업 메커니즘을 결합한 GPT-4 기반 계층적 계획 프레임워크를 제안하고 도요타 휴먼 서포트 로봇에서 복잡한 조작 작업으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- llm_planning
- human_robot_collaboration
- teleoperation
- dynamic_movement_primitives
- yolov5
- visual_grounding
- toyota_hsr
- service_robotics
- one_shot_learning
- ros
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.14097v2.
sources:
- id: src_001
  type: paper
  title: Enhancing the LLM-Based Robot Manipulation Through Human-Robot Collaboration
  url: https://arxiv.org/abs/2406.14097
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3415931
theoretical_depth:
- method
---

## 概述
Large Language Models (LLMs) are gaining popularity in the field of robotics. However, LLM-based robots are limited to simple, repetitive motions due to the poor integration between language models, robots, and the environment. This paper proposes a novel approach to enhance the performance of LLM-based autonomous manipulation through Human-Robot Collaboration (HRC). The approach involves using a prompted GPT-4 language model to decompose high-level language commands into sequences of motions that can be executed by the robot. The system also employs a YOLO-based perception algorithm, providing visual cues to the LLM, which aids in planning feasible motions within the specific environment. Additionally, an HRC method is proposed by combining teleoperation and Dynamic Movement Primitives (DMP), allowing the LLM-based robot to learn from human guidance. Real-world experiments have been conducted using the Toyota Human Support Robot for manipulation tasks. The outcomes indicate that tasks requiring complex trajectory planning and reasoning over environments can be efficiently accomplished through the incorporation of human demonstrations.

## 核心内容
Large Language Models (LLMs) are gaining popularity in the field of robotics. However, LLM-based robots are limited to simple, repetitive motions due to the poor integration between language models, robots, and the environment. This paper proposes a novel approach to enhance the performance of LLM-based autonomous manipulation through Human-Robot Collaboration (HRC). The approach involves using a prompted GPT-4 language model to decompose high-level language commands into sequences of motions that can be executed by the robot. The system also employs a YOLO-based perception algorithm, providing visual cues to the LLM, which aids in planning feasible motions within the specific environment. Additionally, an HRC method is proposed by combining teleoperation and Dynamic Movement Primitives (DMP), allowing the LLM-based robot to learn from human guidance. Real-world experiments have been conducted using the Toyota Human Support Robot for manipulation tasks. The outcomes indicate that tasks requiring complex trajectory planning and reasoning over environments can be efficiently accomplished through the incorporation of human demonstrations.

## 参考
- http://arxiv.org/abs/2406.14097v2

## Overview
Large Language Models (LLMs) are gaining popularity in the field of robotics. However, LLM-based robots are limited to simple, repetitive motions due to the poor integration between language models, robots, and the environment. This paper proposes a novel approach to enhance the performance of LLM-based autonomous manipulation through Human-Robot Collaboration (HRC). The approach involves using a prompted GPT-4 language model to decompose high-level language commands into sequences of motions that can be executed by the robot. The system also employs a YOLO-based perception algorithm, providing visual cues to the LLM, which aids in planning feasible motions within the specific environment. Additionally, an HRC method is proposed by combining teleoperation and Dynamic Movement Primitives (DMP), allowing the LLM-based robot to learn from human guidance. Real-world experiments have been conducted using the Toyota Human Support Robot for manipulation tasks. The outcomes indicate that tasks requiring complex trajectory planning and reasoning over environments can be efficiently accomplished through the incorporation of human demonstrations.

## Content
Large Language Models (LLMs) are gaining popularity in the field of robotics. However, LLM-based robots are limited to simple, repetitive motions due to the poor integration between language models, robots, and the environment. This paper proposes a novel approach to enhance the performance of LLM-based autonomous manipulation through Human-Robot Collaboration (HRC). The approach involves using a prompted GPT-4 language model to decompose high-level language commands into sequences of motions that can be executed by the robot. The system also employs a YOLO-based perception algorithm, providing visual cues to the LLM, which aids in planning feasible motions within the specific environment. Additionally, an HRC method is proposed by combining teleoperation and Dynamic Movement Primitives (DMP), allowing the LLM-based robot to learn from human guidance. Real-world experiments have been conducted using the Toyota Human Support Robot for manipulation tasks. The outcomes indicate that tasks requiring complex trajectory planning and reasoning over environments can be efficiently accomplished through the incorporation of human demonstrations.

## 개요
대규모 언어 모델(LLM)은 로봇 공학 분야에서 점점 더 인기를 얻고 있습니다. 그러나 LLM 기반 로봇은 언어 모델, 로봇 및 환경 간의 통합이 부족하여 단순하고 반복적인 동작으로 제한됩니다. 본 논문은 인간-로봇 협업(HRC)을 통해 LLM 기반 자율 조작의 성능을 향상시키는 새로운 접근 방식을 제안합니다. 이 접근 방식은 프롬프트된 GPT-4 언어 모델을 사용하여 높은 수준의 언어 명령을 로봇이 실행할 수 있는 동작 시퀀스로 분해합니다. 또한 시스템은 YOLO 기반 인식 알고리즘을 사용하여 LLM에 시각적 단서를 제공하며, 이는 특정 환경 내에서 실행 가능한 동작을 계획하는 데 도움을 줍니다. 추가적으로, 원격 조작과 동적 운동 원시(DMP)를 결합한 HRC 방법이 제안되어 LLM 기반 로봇이 인간의 지도로부터 학습할 수 있도록 합니다. Toyota Human Support Robot을 사용한 실제 실험이 조작 작업을 위해 수행되었습니다. 결과는 복잡한 궤적 계획과 환경 추론이 필요한 작업이 인간 시연을 통합함으로써 효율적으로 수행될 수 있음을 나타냅니다.

## 핵심 내용
대규모 언어 모델(LLM)은 로봇 공학 분야에서 점점 더 인기를 얻고 있습니다. 그러나 LLM 기반 로봇은 언어 모델, 로봇 및 환경 간의 통합이 부족하여 단순하고 반복적인 동작으로 제한됩니다. 본 논문은 인간-로봇 협업(HRC)을 통해 LLM 기반 자율 조작의 성능을 향상시키는 새로운 접근 방식을 제안합니다. 이 접근 방식은 프롬프트된 GPT-4 언어 모델을 사용하여 높은 수준의 언어 명령을 로봇이 실행할 수 있는 동작 시퀀스로 분해합니다. 또한 시스템은 YOLO 기반 인식 알고리즘을 사용하여 LLM에 시각적 단서를 제공하며, 이는 특정 환경 내에서 실행 가능한 동작을 계획하는 데 도움을 줍니다. 추가적으로, 원격 조작과 동적 운동 원시(DMP)를 결합한 HRC 방법이 제안되어 LLM 기반 로봇이 인간의 지도로부터 학습할 수 있도록 합니다. Toyota Human Support Robot을 사용한 실제 실험이 조작 작업을 위해 수행되었습니다. 결과는 복잡한 궤적 계획과 환경 추론이 필요한 작업이 인간 시연을 통합함으로써 효율적으로 수행될 수 있음을 나타냅니다.
