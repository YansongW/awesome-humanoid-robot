---
$id: ent_paper_knauer_irosa_interactive_robot_skill_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'IROSA: Interactive Robot Skill Adaptation using Natural Language'
  zh: IROSA：使用自然语言的交互式机器人技能自适应
  ko: 'IROSA: 자연어를 이용한 대화형 로봇 기술 적응'
summary:
  en: IROSA introduces a tool-based architecture in which a pre-trained LLM selects and parameterizes validated tools to adapt
    robot skills from natural-language commands, without direct LLM-to-robot interaction or fine-tuning. The framework is
    validated on a 7-DoF torque-controlled DLR SARA robot performing an industrial bearing-ring insertion task with speed
    modulation, trajectory correction, and obstacle avoidance.
  zh: IROSA提出了一种基于工具的架构，使预训练大语言模型能够选择并参数化经过验证的工具，根据自然语言指令调整机器人技能，无需大语言模型与机器人硬件直接交互或微调。该框架在7自由度力控DLR SARA机器人上执行工业轴承环插入任务，实现了速度调制、轨迹修正和避障。
  ko: IROSA는 사전 학습된 대형 언어 모델이 검증된 도구를 선택하고 매개변수화하여 자연어 명령에 따라 로봇 기술을 적응시키는 도구 기반 아키텍처를 제안하며, LLM과 로봇 하드웨어의 직접 상호작용이나 미세 조정
    없이 동작한다. 7자유도 토크 제어 DLR SARA 로봇에서 산업용 베어링 링 삽입 작업을 수행하며 속도 조절, 궤적 수정 및 장애물 회피를 검증하였다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
- 03_manufacturing_processes
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- llm_tool_use
- skill_adaptation
- imitation_learning
- kernelized_movement_primitives
- kmp
- natural_language_programming
- structured_function_calling
- industrial_manipulation
- bearing_ring_insertion
- safety
- interpretability
- dlr_sara
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.03897v3.
sources:
- id: src_001
  type: paper
  title: 'IROSA: Interactive Robot Skill Adaptation using Natural Language'
  url: https://arxiv.org/abs/2603.03897
  date: '2026'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2026.3671560
theoretical_depth:
- method
---
## 概述
Foundation models have demonstrated impressive capabilities across diverse domains, while imitation learning provides principled methods for robot skill adaptation from limited data. Combining these approaches holds significant promise for direct application to robotics, yet this combination has received limited attention, particularly for industrial deployment. We present a novel framework that enables open-vocabulary skill adaptation through a tool-based architecture, maintaining a protective abstraction layer between the language model and robot hardware. Our approach leverages pre-trained LLMs to select and parameterize specific tools for adapting robot skills without requiring fine-tuning or direct model-to-robot interaction. We demonstrate the framework on a 7-DoF torque-controlled robot performing an industrial bearing ring insertion task, showing successful skill adaptation through natural language commands for speed adjustment, trajectory correction, and obstacle avoidance while maintaining safety, transparency, and interpretability.

## 核心内容
Foundation models have demonstrated impressive capabilities across diverse domains, while imitation learning provides principled methods for robot skill adaptation from limited data. Combining these approaches holds significant promise for direct application to robotics, yet this combination has received limited attention, particularly for industrial deployment. We present a novel framework that enables open-vocabulary skill adaptation through a tool-based architecture, maintaining a protective abstraction layer between the language model and robot hardware. Our approach leverages pre-trained LLMs to select and parameterize specific tools for adapting robot skills without requiring fine-tuning or direct model-to-robot interaction. We demonstrate the framework on a 7-DoF torque-controlled robot performing an industrial bearing ring insertion task, showing successful skill adaptation through natural language commands for speed adjustment, trajectory correction, and obstacle avoidance while maintaining safety, transparency, and interpretability.

## 参考
- http://arxiv.org/abs/2603.03897v3

## Overview
Foundation models have demonstrated impressive capabilities across diverse domains, while imitation learning provides principled methods for robot skill adaptation from limited data. Combining these approaches holds significant promise for direct application to robotics, yet this combination has received limited attention, particularly for industrial deployment. We present a novel framework that enables open-vocabulary skill adaptation through a tool-based architecture, maintaining a protective abstraction layer between the language model and robot hardware. Our approach leverages pre-trained LLMs to select and parameterize specific tools for adapting robot skills without requiring fine-tuning or direct model-to-robot interaction. We demonstrate the framework on a 7-DoF torque-controlled robot performing an industrial bearing ring insertion task, showing successful skill adaptation through natural language commands for speed adjustment, trajectory correction, and obstacle avoidance while maintaining safety, transparency, and interpretability.

## Content
Foundation models have demonstrated impressive capabilities across diverse domains, while imitation learning provides principled methods for robot skill adaptation from limited data. Combining these approaches holds significant promise for direct application to robotics, yet this combination has received limited attention, particularly for industrial deployment. We present a novel framework that enables open-vocabulary skill adaptation through a tool-based architecture, maintaining a protective abstraction layer between the language model and robot hardware. Our approach leverages pre-trained LLMs to select and parameterize specific tools for adapting robot skills without requiring fine-tuning or direct model-to-robot interaction. We demonstrate the framework on a 7-DoF torque-controlled robot performing an industrial bearing ring insertion task, showing successful skill adaptation through natural language commands for speed adjustment, trajectory correction, and obstacle avoidance while maintaining safety, transparency, and interpretability.

## 개요
기반 모델(Foundation models)은 다양한 분야에서 인상적인 능력을 입증해 왔으며, 모방 학습(imitation learning)은 제한된 데이터로부터 로봇 기술을 적응시키기 위한 원칙적인 방법을 제공합니다. 이러한 접근법을 결합하면 로봇 공학에 직접 적용할 수 있는 큰 가능성이 있지만, 특히 산업 현장 배포 측면에서 이 결합은 제한적인 주목만 받아 왔습니다. 우리는 도구 기반 아키텍처를 통해 개방형 어휘 기술 적응(open-vocabulary skill adaptation)을 가능하게 하는 새로운 프레임워크를 제시하며, 언어 모델과 로봇 하드웨어 사이에 보호적 추상화 계층을 유지합니다. 우리의 접근 방식은 사전 훈련된 LLM을 활용하여 로봇 기술을 적응시키기 위한 특정 도구를 선택하고 매개변수화하며, 미세 조정이나 모델-로봇 직접 상호작용이 필요하지 않습니다. 우리는 7-DoF 토크 제어 로봇이 산업용 베어링 링 삽입 작업을 수행하는 환경에서 이 프레임워크를 시연하며, 속도 조정, 궤적 수정, 장애물 회피를 위한 자연어 명령을 통해 안전성, 투명성, 해석 가능성을 유지하면서 성공적인 기술 적응을 보여줍니다.

## 핵심 내용
기반 모델(Foundation models)은 다양한 분야에서 인상적인 능력을 입증해 왔으며, 모방 학습(imitation learning)은 제한된 데이터로부터 로봇 기술을 적응시키기 위한 원칙적인 방법을 제공합니다. 이러한 접근법을 결합하면 로봇 공학에 직접 적용할 수 있는 큰 가능성이 있지만, 특히 산업 현장 배포 측면에서 이 결합은 제한적인 주목만 받아 왔습니다. 우리는 도구 기반 아키텍처를 통해 개방형 어휘 기술 적응(open-vocabulary skill adaptation)을 가능하게 하는 새로운 프레임워크를 제시하며, 언어 모델과 로봇 하드웨어 사이에 보호적 추상화 계층을 유지합니다. 우리의 접근 방식은 사전 훈련된 LLM을 활용하여 로봇 기술을 적응시키기 위한 특정 도구를 선택하고 매개변수화하며, 미세 조정이나 모델-로봇 직접 상호작용이 필요하지 않습니다. 우리는 7-DoF 토크 제어 로봇이 산업용 베어링 링 삽입 작업을 수행하는 환경에서 이 프레임워크를 시연하며, 속도 조정, 궤적 수정, 장애물 회피를 위한 자연어 명령을 통해 안전성, 투명성, 해석 가능성을 유지하면서 성공적인 기술 적응을 보여줍니다.
