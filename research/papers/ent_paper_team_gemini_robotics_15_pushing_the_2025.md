---
$id: ent_paper_team_gemini_robotics_15_pushing_the_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion
    Transfer'
  zh: Gemini Robotics 1.5：以高级具身推理、思考和动作迁移推动通才机器人前沿
  ko: 'Gemini Robotics 1.5: 고급 구체화 추론, 사고 및 동작 전이를 통한 범용 로봇의 최전선 확장'
summary:
  en: Gemini Robotics 1.5 introduces a multi-embodiment Vision-Language-Action model with Motion Transfer and a Thinking VLA
    that interleaves actions with natural-language reasoning, alongside Gemini Robotics-ER 1.5, an embodied reasoning model
    for spatial understanding and task planning.
  zh: Gemini Robotics 1.5 提出了一个具备动作迁移能力的多本体视觉-语言-动作模型，以及将动作与自然语言推理交织的 Thinking VLA，并配套 Gemini Robotics-ER 1.5 具身推理模型用于空间理解与任务规划。
  ko: Gemini Robotics 1.5는 동작 전이를 갖춘 다중 구체화 비전-언어-행동 모델과 자연어 추론과 행동을 교차하는 Thinking VLA를 소개하며, 공간 이해와 작업 계획을 위한 Gemini Robotics-ER
    1.5 구체화 추론 모델을 함께 제시한다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 08_software_middleware
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- vla
- vision_language_action
- embodied_reasoning
- motion_transfer
- multi_embodiment
- humanoid_robot
- apptronik_apollo
- thinking_vla
- foundation_model
- robot_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.03342v3.
sources:
- id: src_001
  type: paper
  title: 'Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion
    Transfer'
  url: https://arxiv.org/abs/2510.03342
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
General-purpose robots need a deep understanding of the physical world, advanced reasoning, and general and dexterous control. This report introduces the latest generation of the Gemini Robotics model family: Gemini Robotics 1.5, a multi-embodiment Vision-Language-Action (VLA) model, and Gemini Robotics-ER 1.5, a state-of-the-art Embodied Reasoning (ER) model. We are bringing together three major innovations. First, Gemini Robotics 1.5 features a novel architecture and a Motion Transfer (MT) mechanism, which enables it to learn from heterogeneous, multi-embodiment robot data and makes the VLA more general. Second, Gemini Robotics 1.5 interleaves actions with a multi-level internal reasoning process in natural language. This enables the robot to "think before acting" and notably improves its ability to decompose and execute complex, multi-step tasks, and also makes the robot's behavior more interpretable to the user. Third, Gemini Robotics-ER 1.5 establishes a new state-of-the-art for embodied reasoning, i.e., for reasoning capabilities that are critical for robots, such as visual and spatial understanding, task planning, and progress estimation. Together, this family of models takes us a step towards an era of physical agents-enabling robots to perceive, think and then act so they can solve complex multi-step tasks.

## 核心内容
General-purpose robots need a deep understanding of the physical world, advanced reasoning, and general and dexterous control. This report introduces the latest generation of the Gemini Robotics model family: Gemini Robotics 1.5, a multi-embodiment Vision-Language-Action (VLA) model, and Gemini Robotics-ER 1.5, a state-of-the-art Embodied Reasoning (ER) model. We are bringing together three major innovations. First, Gemini Robotics 1.5 features a novel architecture and a Motion Transfer (MT) mechanism, which enables it to learn from heterogeneous, multi-embodiment robot data and makes the VLA more general. Second, Gemini Robotics 1.5 interleaves actions with a multi-level internal reasoning process in natural language. This enables the robot to "think before acting" and notably improves its ability to decompose and execute complex, multi-step tasks, and also makes the robot's behavior more interpretable to the user. Third, Gemini Robotics-ER 1.5 establishes a new state-of-the-art for embodied reasoning, i.e., for reasoning capabilities that are critical for robots, such as visual and spatial understanding, task planning, and progress estimation. Together, this family of models takes us a step towards an era of physical agents-enabling robots to perceive, think and then act so they can solve complex multi-step tasks.

## 参考
- http://arxiv.org/abs/2510.03342v3

## Overview
General-purpose robots require a profound understanding of the physical world, advanced reasoning capabilities, and general, dexterous control. This report introduces the latest generation of the Gemini Robotics model family: Gemini Robotics 1.5, a multi-embodiment Vision-Language-Action (VLA) model, and Gemini Robotics-ER 1.5, a state-of-the-art Embodied Reasoning (ER) model. We bring together three major innovations. First, Gemini Robotics 1.5 features a novel architecture and a Motion Transfer (MT) mechanism, enabling it to learn from heterogeneous, multi-embodiment robot data and making the VLA more general. Second, Gemini Robotics 1.5 interleaves actions with a multi-level internal reasoning process in natural language. This allows the robot to "think before acting," significantly improving its ability to decompose and execute complex, multi-step tasks, while also making its behavior more interpretable to users. Third, Gemini Robotics-ER 1.5 establishes a new state-of-the-art for embodied reasoning—i.e., reasoning capabilities critical for robots, such as visual and spatial understanding, task planning, and progress estimation. Together, this family of models takes us a step closer to an era of physical agents, enabling robots to perceive, think, and then act to solve complex multi-step tasks.

## Content
General-purpose robots require a profound understanding of the physical world, advanced reasoning capabilities, and general, dexterous control. This report introduces the latest generation of the Gemini Robotics model family: Gemini Robotics 1.5, a multi-embodiment Vision-Language-Action (VLA) model, and Gemini Robotics-ER 1.5, a state-of-the-art Embodied Reasoning (ER) model. We bring together three major innovations. First, Gemini Robotics 1.5 features a novel architecture and a Motion Transfer (MT) mechanism, enabling it to learn from heterogeneous, multi-embodiment robot data and making the VLA more general. Second, Gemini Robotics 1.5 interleaves actions with a multi-level internal reasoning process in natural language. This allows the robot to "think before acting," significantly improving its ability to decompose and execute complex, multi-step tasks, while also making its behavior more interpretable to users. Third, Gemini Robotics-ER 1.5 establishes a new state-of-the-art for embodied reasoning—i.e., reasoning capabilities critical for robots, such as visual and spatial understanding, task planning, and progress estimation. Together, this family of models takes us a step closer to an era of physical agents, enabling robots to perceive, think, and then act to solve complex multi-step tasks.

## 개요
범용 로봇은 물리적 세계에 대한 깊은 이해, 고급 추론 능력, 그리고 일반적이고 정교한 제어 능력을 필요로 합니다. 본 보고서는 Gemini Robotics 모델 패밀리의 최신 세대를 소개합니다: 다중 체현 비전-언어-행동(VLA) 모델인 Gemini Robotics 1.5와 최첨단 체현 추론(ER) 모델인 Gemini Robotics-ER 1.5입니다. 우리는 세 가지 주요 혁신을 통합했습니다. 첫째, Gemini Robotics 1.5는 새로운 아키텍처와 모션 전이(MT) 메커니즘을 특징으로 하여, 이질적이고 다중 체현 로봇 데이터로부터 학습할 수 있게 하고 VLA를 더욱 일반화합니다. 둘째, Gemini Robotics 1.5는 자연어로 다단계 내부 추론 과정을 행동과 인터리브합니다. 이를 통해 로봇이 "행동하기 전에 생각"할 수 있게 하여 복잡한 다단계 작업을 분해하고 실행하는 능력을 현저히 향상시키며, 사용자에게 로봇의 행동을 더 해석 가능하게 만듭니다. 셋째, Gemini Robotics-ER 1.5는 체현 추론, 즉 로봇에게 중요한 추론 능력(예: 시각적 및 공간적 이해, 작업 계획, 진행 상황 추정)에서 새로운 최첨단을 확립합니다. 이 모델 패밀리는 함께 물리적 에이전트의 시대를 향한 한 걸음을 내딛게 하여, 로봇이 복잡한 다단계 작업을 해결할 수 있도록 인지하고, 생각한 후 행동할 수 있게 합니다.

## 핵심 내용
범용 로봇은 물리적 세계에 대한 깊은 이해, 고급 추론 능력, 그리고 일반적이고 정교한 제어 능력을 필요로 합니다. 본 보고서는 Gemini Robotics 모델 패밀리의 최신 세대를 소개합니다: 다중 체현 비전-언어-행동(VLA) 모델인 Gemini Robotics 1.5와 최첨단 체현 추론(ER) 모델인 Gemini Robotics-ER 1.5입니다. 우리는 세 가지 주요 혁신을 통합했습니다. 첫째, Gemini Robotics 1.5는 새로운 아키텍처와 모션 전이(MT) 메커니즘을 특징으로 하여, 이질적이고 다중 체현 로봇 데이터로부터 학습할 수 있게 하고 VLA를 더욱 일반화합니다. 둘째, Gemini Robotics 1.5는 자연어로 다단계 내부 추론 과정을 행동과 인터리브합니다. 이를 통해 로봇이 "행동하기 전에 생각"할 수 있게 하여 복잡한 다단계 작업을 분해하고 실행하는 능력을 현저히 향상시키며, 사용자에게 로봇의 행동을 더 해석 가능하게 만듭니다. 셋째, Gemini Robotics-ER 1.5는 체현 추론, 즉 로봇에게 중요한 추론 능력(예: 시각적 및 공간적 이해, 작업 계획, 진행 상황 추정)에서 새로운 최첨단을 확립합니다. 이 모델 패밀리는 함께 물리적 에이전트의 시대를 향한 한 걸음을 내딛게 하여, 로봇이 복잡한 다단계 작업을 해결할 수 있도록 인지하고, 생각한 후 행동할 수 있게 합니다.
