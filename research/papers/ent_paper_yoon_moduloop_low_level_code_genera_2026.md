---
$id: ent_paper_yoon_moduloop_low_level_code_genera_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ModuLoop: Low-Level Code Generation using Modular Synthesizer and Closed-Loop Debugger for Robotic Control'
  zh: ModuLoop：基于模块化合成器与闭环调试器的机器人控制底层代码生成
  ko: 'ModuLoop: 모듈형 신디사이저 및 폐쇄형 루프 디버거를 활용한 로봇 제어 저수준 코드 생성'
summary:
  en: Proposes a closed-loop modular code synthesizer that converts natural-language commands into executable low-level Python
    control modules and iteratively debugs them via runtime probes, validated on RGB-D camera and UR3 arm calibration plus
    a pick-and-place task.
  zh: 提出一种闭环模块化代码合成器，将自然语言指令转换为可执行的低层Python控制模块，并通过运行时探针迭代调试，在RGB-D相机与UR3机械臂标定及抓取放置任务中得到验证。
  ko: 자연어 명령을 실행 가능한 저수준 Python 제어 모듈로 변환하고 런타임 프로브를 통해 반복적으로 디버깅하는 폐쇄 루프 모듈형 코드 합성기를 제안하며, RGB-D 카메라와 UR3 매니퓰레이터 보정 및 픽앤플레이스
    작업에서 검증함.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- low_level_code_generation
- modular_code_synthesis
- closed_loop_debugging
- llm_robotic_control
- hand_eye_calibration
- pick_and_place
- ur3
- realsense_d435i
- aruco_marker
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.03047v1.
sources:
- id: src_001
  type: paper
  title: 'ModuLoop: Low-Level Code Generation using Modular Synthesizer and Closed-Loop Debugger for Robotic Control'
  url: https://arxiv.org/abs/2606.03047
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Large Language Models (LLMs) have demonstrated impressive performance across various domains, including code generation and problem solving. However, their application in robotic control, particularly in low-level tasks that require precise manipulation, real-time feedback, and environment-dependent execution, remains limited. To address this challenge, we propose the Closed-Loop Modular Code Synthesizer framework. This framework leverages a pre-trained LLM without any task-specific fine-tuning to perform modular code planning and generation, and iteratively executes the generated code while inserting debugging probes to observe its behavior. This closed-loop structure facilitates systematic debugging and refinement, ultimately producing executable control programs. We apply the proposed framework to the calibration of an RGB-D camera and a robotic arm, validating its effectiveness in real-world settings. Furthermore, through a subsequent pick-and-place task, we demonstrate not only the accuracy of the calibration but also the potential extensibility of the framework. Across both tasks, the framework achieved high execution accuracy and autonomy, illustrating the practicality and scalability of LLM-based robotic control using our framework.

## 核心内容
Large Language Models (LLMs) have demonstrated impressive performance across various domains, including code generation and problem solving. However, their application in robotic control, particularly in low-level tasks that require precise manipulation, real-time feedback, and environment-dependent execution, remains limited. To address this challenge, we propose the Closed-Loop Modular Code Synthesizer framework. This framework leverages a pre-trained LLM without any task-specific fine-tuning to perform modular code planning and generation, and iteratively executes the generated code while inserting debugging probes to observe its behavior. This closed-loop structure facilitates systematic debugging and refinement, ultimately producing executable control programs. We apply the proposed framework to the calibration of an RGB-D camera and a robotic arm, validating its effectiveness in real-world settings. Furthermore, through a subsequent pick-and-place task, we demonstrate not only the accuracy of the calibration but also the potential extensibility of the framework. Across both tasks, the framework achieved high execution accuracy and autonomy, illustrating the practicality and scalability of LLM-based robotic control using our framework.

## 参考
- http://arxiv.org/abs/2606.03047v1

## Overview
Large Language Models (LLMs) have demonstrated impressive performance across various domains, including code generation and problem solving. However, their application in robotic control, particularly in low-level tasks that require precise manipulation, real-time feedback, and environment-dependent execution, remains limited. To address this challenge, we propose the Closed-Loop Modular Code Synthesizer framework. This framework leverages a pre-trained LLM without any task-specific fine-tuning to perform modular code planning and generation, and iteratively executes the generated code while inserting debugging probes to observe its behavior. This closed-loop structure facilitates systematic debugging and refinement, ultimately producing executable control programs. We apply the proposed framework to the calibration of an RGB-D camera and a robotic arm, validating its effectiveness in real-world settings. Furthermore, through a subsequent pick-and-place task, we demonstrate not only the accuracy of the calibration but also the potential extensibility of the framework. Across both tasks, the framework achieved high execution accuracy and autonomy, illustrating the practicality and scalability of LLM-based robotic control using our framework.

## Content
Large Language Models (LLMs) have demonstrated impressive performance across various domains, including code generation and problem solving. However, their application in robotic control, particularly in low-level tasks that require precise manipulation, real-time feedback, and environment-dependent execution, remains limited. To address this challenge, we propose the Closed-Loop Modular Code Synthesizer framework. This framework leverages a pre-trained LLM without any task-specific fine-tuning to perform modular code planning and generation, and iteratively executes the generated code while inserting debugging probes to observe its behavior. This closed-loop structure facilitates systematic debugging and refinement, ultimately producing executable control programs. We apply the proposed framework to the calibration of an RGB-D camera and a robotic arm, validating its effectiveness in real-world settings. Furthermore, through a subsequent pick-and-place task, we demonstrate not only the accuracy of the calibration but also the potential extensibility of the framework. Across both tasks, the framework achieved high execution accuracy and autonomy, illustrating the practicality and scalability of LLM-based robotic control using our framework.

## 개요
대규모 언어 모델(LLM)은 코드 생성 및 문제 해결을 포함한 다양한 영역에서 뛰어난 성능을 입증했습니다. 그러나 로봇 제어, 특히 정밀한 조작, 실시간 피드백 및 환경 의존적 실행이 필요한 저수준 작업에서의 적용은 여전히 제한적입니다. 이 문제를 해결하기 위해 우리는 폐쇄 루프 모듈식 코드 합성기(Closed-Loop Modular Code Synthesizer) 프레임워크를 제안합니다. 이 프레임워크는 사전 훈련된 LLM을 작업별 미세 조정 없이 활용하여 모듈식 코드 계획 및 생성을 수행하고, 생성된 코드를 반복적으로 실행하면서 디버깅 프로브를 삽입하여 동작을 관찰합니다. 이러한 폐쇄 루프 구조는 체계적인 디버깅 및 개선을 촉진하여 궁극적으로 실행 가능한 제어 프로그램을 생성합니다. 제안된 프레임워크를 RGB-D 카메라와 로봇 팔의 캘리브레이션에 적용하여 실제 환경에서의 효과를 검증했습니다. 또한, 후속 픽 앤 플레이스(pick-and-place) 작업을 통해 캘리브레이션의 정확성뿐만 아니라 프레임워크의 확장 가능성도 입증했습니다. 두 작업 모두에서 프레임워크는 높은 실행 정확도와 자율성을 달성하여, 우리 프레임워크를 사용한 LLM 기반 로봇 제어의 실용성과 확장성을 보여주었습니다.

## 핵심 내용
대규모 언어 모델(LLM)은 코드 생성 및 문제 해결을 포함한 다양한 영역에서 뛰어난 성능을 입증했습니다. 그러나 로봇 제어, 특히 정밀한 조작, 실시간 피드백 및 환경 의존적 실행이 필요한 저수준 작업에서의 적용은 여전히 제한적입니다. 이 문제를 해결하기 위해 우리는 폐쇄 루프 모듈식 코드 합성기(Closed-Loop Modular Code Synthesizer) 프레임워크를 제안합니다. 이 프레임워크는 사전 훈련된 LLM을 작업별 미세 조정 없이 활용하여 모듈식 코드 계획 및 생성을 수행하고, 생성된 코드를 반복적으로 실행하면서 디버깅 프로브를 삽입하여 동작을 관찰합니다. 이러한 폐쇄 루프 구조는 체계적인 디버깅 및 개선을 촉진하여 궁극적으로 실행 가능한 제어 프로그램을 생성합니다. 제안된 프레임워크를 RGB-D 카메라와 로봇 팔의 캘리브레이션에 적용하여 실제 환경에서의 효과를 검증했습니다. 또한, 후속 픽 앤 플레이스(pick-and-place) 작업을 통해 캘리브레이션의 정확성뿐만 아니라 프레임워크의 확장 가능성도 입증했습니다. 두 작업 모두에서 프레임워크는 높은 실행 정확도와 자율성을 달성하여, 우리 프레임워크를 사용한 LLM 기반 로봇 제어의 실용성과 확장성을 보여주었습니다.
